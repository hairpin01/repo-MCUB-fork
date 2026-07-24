from __future__ import annotations

from typing import Any
import re

from core.lib.types import Event

class OpenAgentContextService:
    """Conversation-history helpers that do not depend on MCUB objects."""

    _COMPACTION_SYSTEM_PROMPT = (
        "You compact an OpenAgent chat session. Read the full prior context and "
        "write a concise continuity summary that lets the assistant continue work "
        "without needing the omitted messages. Preserve: user goals, decisions, "
        "constraints, files changed/read, commands run, test results, current TODOs, "
        "open questions, and important warnings. Do not invent facts. Do not include "
        "irrelevant chatter. Output plain text markdown only."
    )

    @staticmethod
    def history_message(role: str, content: Any, limit: int = 12000) -> dict[str, str]:
        text = str(content or "")
        if len(text) > limit:
            text = text[:limit] + "\n...[truncated]"
        return {"role": role, "content": text}

    def context_entries(
        self,
        prompt: str,
        answer: str,
        tool_trace: list[dict[str, str]] | None = None,
    ) -> list[dict[str, str]]:
        entries = [self.history_message("user", prompt, limit=8000)]
        for item in tool_trace or []:
            role = str(item.get("role") or "assistant")
            if role not in {"system", "user", "assistant"}:
                role = "assistant"
            entries.append(self.history_message(role, item.get("content", "")))
        entries.append(self.history_message("assistant", answer, limit=8000))
        return entries

    @staticmethod
    def clean_thinking_notes(thinking_notes: list[str] | None) -> list[str]:
        return [str(item).strip() for item in (thinking_notes or []) if str(item).strip()]

    @staticmethod
    def history_chars(history: list[dict[str, str]]) -> int:
        return sum(len(str(item.get("content", ""))) for item in history)

    @staticmethod
    def format_history_for_compaction(history: list[dict[str, str]]) -> str:
        parts = []
        for index, item in enumerate(history, 1):
            role = str(item.get("role", "unknown"))
            content = str(item.get("content", ""))
            parts.append(f"[{index}] {role}:\n{content}")
        return "\n\n".join(parts)

    def compaction_system_prompt(self) -> str:
        return self._COMPACTION_SYSTEM_PROMPT


class _OpenAgentContextMixin:
    """Conversation context, compaction, tool memory and config helpers."""

    def _context_service(self) -> OpenAgentContextService:
        service = getattr(self, "_context_service_instance", None)
        if not isinstance(service, OpenAgentContextService):
            service = OpenAgentContextService()
            self._context_service_instance = service
        return service

    def _request_label(
        self,
        *,
        elapsed: float | None = None,
        thinking_notes: list[str] | None = None,
    ) -> str:
        return self._render_template(
            str(self.config.get("request_label", "") or self.strings("request_label_default")),
            elapsed=elapsed,
            thinking_notes=thinking_notes,
        )

    def _response_label(
        self,
        *,
        elapsed: float | None = None,
        thinking_notes: list[str] | None = None,
    ) -> str:
        return self._render_template(
            str(self.config.get("response_label", "") or self.strings("response_label_default")),
            elapsed=elapsed,
            thinking_notes=thinking_notes,
        )

    def _history_message(self, role: str, content: Any, limit: int = 12000) -> dict[str, str]:
        return self._context_service().history_message(role, content, limit)

    def _remember_context(
        self,
        chat_id: int | None,
        prompt: str,
        answer: str,
        tool_trace: list[dict[str, str]] | None = None,
        thinking_notes: list[str] | None = None,
    ) -> None:
        if not chat_id or not self.config["context_enabled"]:
            return
        session = self._get_active_session(int(chat_id))
        history = session.messages
        entries = self._context_service().context_entries(prompt, answer, tool_trace)
        session.thinking_notes = self._context_service().clean_thinking_notes(thinking_notes)
        history.extend(entries)
        context_turns = int(self.config["context_turns"])
        if context_turns <= 0:
            history.clear()
            session.thinking_notes = []
        elif history and history[0].get("role") == "system" and str(history[0].get("content", "")).startswith("Compacted previous OpenAgent session context:"):
            max_messages = max(context_turns * 4, len(entries))
            keep_tail = max(0, max_messages - 1)
            tail_source = history[1:]
            session.messages = [history[0], *tail_source[-keep_tail:]] if keep_tail else [history[0]]
        else:
            max_messages = max(context_turns * 4, len(entries))
            del history[:-max_messages]
        self._touch_session(session)
        self._schedule_auto_name_session(session)

    def _history_for_chat(self, chat_id: int | None) -> list[dict[str, str]]:
        if not chat_id or not self.config["context_enabled"]:
            return []
        return list(self._get_active_session(int(chat_id)).messages)

    def _history_chars(self, history: list[dict[str, str]]) -> int:
        return self._context_service().history_chars(history)

    def _format_history_for_compaction(self, history: list[dict[str, str]]) -> str:
        return self._context_service().format_history_for_compaction(history)

    def _compaction_system_prompt(self) -> str:
        return self._context_service().compaction_system_prompt()

    async def _compact_chat_history_if_needed(
        self,
        chat_id: int | None,
        provider: str,
        api_key: str,
    ) -> bool:
        if not chat_id or not bool(self.config.get("context_enabled", True)):
            return False
        if not bool(self.config.get("context_compaction_enabled", True)):
            return False

        _compact_session = self._get_active_session(int(chat_id))
        history = _compact_session.messages
        threshold = int(self.config.get("context_compaction_chars", 18000) or 18000)
        if not history or self._history_chars(history) <= threshold:
            return False

        keep_messages = max(0, int(self.config.get("context_compaction_keep_turns", 2) or 2) * 2)
        old_history = history[:-keep_messages] if keep_messages else history
        recent_history = history[-keep_messages:] if keep_messages else []
        if not old_history:
            return False

        max_chars = max(threshold * 2, threshold + 4000)
        compact_input = self._format_history_for_compaction(old_history)
        if len(compact_input) > max_chars:
            compact_input = compact_input[-max_chars:]

        messages: list[dict[str, Any]] = [
            {"role": "system", "content": self._compaction_system_prompt()},
            {
                "role": "user",
                "content": (
                    "Compact this OpenAgent session context. The assistant will continue "
                    "after your summary, with the newest turns kept separately.\n\n"
                    f"{compact_input}"
                ),
            },
        ]
        max_tokens = int(self.config.get("context_compaction_max_tokens", 900) or 900)
        try:
            if provider in ("openai", "openrouter", "groq", "deepseek", "xai", "other"):
                summary = await self._ask_openai_compatible(
                    provider,
                    messages,
                    api_key,
                    max_tokens_override=max_tokens,
                )
            elif provider == "google":
                summary = await self._ask_google(
                    messages,
                    api_key,
                    max_tokens_override=max_tokens,
                )
            else:
                return False
        except Exception as exc:
            self.log.warning(f"OpenAgent context compaction failed: {exc}")
            return False

        summary = (summary or "").strip()
        if not summary:
            return False

        _compact_session.messages = [
            {
                "role": "system",
                "content": "Compacted previous OpenAgent session context:\n" + summary[-12000:],
            },
            *recent_history,
        ]
        self._touch_session(_compact_session)
        return True

    def _tool_memory_note(self, text: str) -> str:
        text = re.sub(r"\s+", " ", text or "").strip()
        if not text:
            return ""
        max_chars = int(self.config.get("tool_memory_max_chars", 500) or 500)
        if len(text) > max_chars:
            text = text[:max_chars].rstrip() + "..."
        return text

    def _remember_tool_output(self, chat_id: int | None, tool_name: str, output: str) -> None:
        if not chat_id or not bool(self.config.get("tool_memory_enabled", False)):
            return
        note = self._tool_memory_note(output)
        if not note:
            return
        memory = self._tool_memory.setdefault(int(chat_id), [])
        memory.append(f"{tool_name}: {note}")
        max_items = int(self.config.get("tool_memory_items", 20) or 20)
        if max_items <= 0:
            memory.clear()
        else:
            del memory[:-max_items]

    def _tool_memory_prompt(self, chat_id: int | None) -> str:
        if not chat_id or not bool(self.config.get("tool_memory_enabled", False)):
            return ""
        notes = self._tool_memory.get(int(chat_id), [])
        if not notes:
            return ""
        return "Recent tool memory:\n" + "\n".join(f"- {line}" for line in notes[-int(self.config.get("tool_memory_items", 20) or 20):])

    def _base_url(self, provider: str) -> str:
        if provider == "other":
            return str(self.config.get("custom_base_url", "") or "").strip().rstrip("/")
        return self.BASE_URLS[provider].rstrip("/")

    def _args_raw(self, event: Event) -> str:
        return self.args_raw(event).strip()

    def _invalidate_config_caches(self, key: str | None = None) -> None:
        if key in {None, "todo_status_emojis"}:
            self._todo_status_map_raw = None
            self._todo_status_map_cache = None
        if key in {None, "tool_status_emojis"}:
            self._tool_status_emojis_raw = None
            self._tool_status_emojis_cache = None

    async def _set_config_value(self, key: str, value: Any) -> None:
        self.config[key] = value
        self._invalidate_config_caches(key)
        await self.save_config()

__all__ = [
    "_OpenAgentContextMixin",
    "OpenAgentContextService",
]
