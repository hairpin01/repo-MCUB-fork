from __future__ import annotations

from typing import Any
import contextlib
import re
import random
import time

_PLACEHOLDER_RE = re.compile(r"\{([a-zA-Z0-9_]+)\}")

class OpenAgentProviderService:
    """Provider/model config helpers independent from MCUB runtime."""

    _ALIASES = {
        "custom": "other",
        "open_router": "openrouter",
        "open-router": "openrouter",
        "grok": "xai",
    }

    def provider(self, config: Any, providers: Any) -> str:
        provider = str(config.get("provider", "openai")).lower().strip()
        return provider if provider in providers else "openai"

    def normalize_provider(self, provider: str) -> str:
        provider = provider.lower().strip()
        return self._ALIASES.get(provider, provider)

    def model(self, config: Any, default_models: dict[str, str], provider: str) -> str:
        model = str(config.get("model", "")).strip()
        return model or default_models[provider]

    @staticmethod
    def api_key(config: Any) -> str:
        return str(config.get("api_key", "") or "").strip()

    @staticmethod
    def provider_label(provider: str, labels: dict[str, str]) -> str:
        return labels.get(provider, "Custom")


class OpenAgentTemplateService:
    """Template, placeholder, and small formatting helpers for isolated tests."""

    _PLACEHOLDER_DESCRIPTIONS = {
        "agent_version": "OpenAgent version",
        "provider": "Provider label",
        "provider_key": "Provider key",
        "model": "Current model",
        "reasoning_effort": "Reasoning effort",
        "chat_id": "Current chat id",
        "user_id": "Current user id",
        "session_name": "Active OpenAgent session name",
        "session_messages": "Active session message count",
        "runtime_comments_count": "Queued live comments count",
        "runtime_comments": "Last 3 queued live comments",
        "tool_count": "Tools used in current response",
        "available_tool_count": "Available tool count",
        "elapsed": "Elapsed seconds",
        "input_tokens": "Last input tokens",
        "output_tokens": "Last output tokens",
        "total_tokens": "Last total tokens",
        "thinking": "Thinking notes text",
        "todo": "Formatted TODO list",
        "random": "Random thinking string",
        "prefix": "Command prefix",
        "time": "Current time",
        "date": "Current date",
    }

    @staticmethod
    def format_thinking_notes(
        thinking_notes: list[str] | None,
        *,
        display_limit: int,
        empty_text: str,
        bullet: str,
    ) -> str:
        notes = [str(note).strip() for note in (thinking_notes or []) if str(note).strip()]
        if display_limit > 0:
            notes = notes[-display_limit:]
        else:
            notes = []
        if not notes:
            return empty_text
        bullet = (bullet or "").strip()
        prefix = f"{bullet} " if bullet else ""
        return "\n".join(f"{prefix}{note}" for note in notes)

    @staticmethod
    def random_placeholder(raw_random: Any) -> str:
        if isinstance(raw_random, str):
            raw_random = raw_random.splitlines()
        raw_random = raw_random or []
        random_lines = [str(line).strip() for line in raw_random if str(line).strip()]
        return random.choice(random_lines) if random_lines else "Thinking..."

    @staticmethod
    def placeholder_keys(template: str) -> set[str]:
        return set(_PLACEHOLDER_RE.findall(template or ""))

    @staticmethod
    def render(template: str, values: dict[str, Any]) -> str:
        result = template or ""
        for key, value in values.items():
            result = result.replace("{" + key + "}", str(value))
        return result

    @staticmethod
    def event_chat_id(event: Any | None) -> int | None:
        if event is None:
            return None
        chat_id = getattr(event, "chat_id", None) or getattr(event, "_openagent_source_chat_id", None)
        with contextlib.suppress(Exception):
            return int(chat_id) if chat_id is not None else None
        return None

    def format_placeholder_help(self) -> str:
        return "\n".join(
            f"{{{key}}} - {value}"
            for key, value in self._PLACEHOLDER_DESCRIPTIONS.items()
        )


class _OpenAgentProviderMixin:
    """Provider selection and text/template helpers."""

    def _provider_service(self) -> OpenAgentProviderService:
        service = getattr(self, "_provider_service_instance", None)
        if not isinstance(service, OpenAgentProviderService):
            service = OpenAgentProviderService()
            self._provider_service_instance = service
        return service

    def _template_service(self) -> OpenAgentTemplateService:
        service = getattr(self, "_template_service_instance", None)
        if not isinstance(service, OpenAgentTemplateService):
            service = OpenAgentTemplateService()
            self._template_service_instance = service
        return service

    def _provider(self) -> str:
        return self._provider_service().provider(self.config, self.PROVIDERS)

    def _normalize_provider(self, provider: str) -> str:
        return self._provider_service().normalize_provider(provider)

    def _model(self, provider: str | None = None) -> str:
        provider = provider or self._provider()
        return self._provider_service().model(self.config, self.DEFAULT_MODELS, provider)

    def _api_key(self) -> str:
        return self._provider_service().api_key(self.config)

    def _provider_label(self) -> str:
        return self._provider_service().provider_label(self._provider(), self.PROVIDER_LABELS)

    def _response_title(
        self,
        elapsed: float,
        *,
        tool_count: int = 0,
        thinking_notes: list[str] | None = None,
    ) -> str:
        return self._render_template(
            str(self.config.get("response_header", ""))
            or "<blockquote><a href=\"tg://emoji?id=6010179991944305029\">☺️</a> <strong>OpenAgent</strong>: <a href=\"tg://emoji?id=5325872701032635449\">⏳</a>  <em>{elapsed}</em>s\n• <u>{provider}/{model}</u>  •  <code>{reasoning_effort}</code>\n| | | | | | | | | | | | | | | | | | | | | | | | | | |\n<a href=\"tg://emoji?id=5408994848084624514\">💸</a> <strong>in</strong> <em>{input_tokens}</em>, <strong>out</strong> <em>{output_tokens}</em> | <b>total</b>\n<i>{total_tokens}</i> | <strong>tool use:</strong> <em>{tool_count}</em></blockquote>\n<blockquote expandable><i>{thinking}</i></blockquote>",
            elapsed=elapsed,
            tool_count=tool_count,
            thinking_notes=thinking_notes,
        )

    def _format_thinking_notes(self, thinking_notes: list[str] | None = None) -> str:
        return self._template_service().format_thinking_notes(
            thinking_notes,
            display_limit=int(self.config.get("thinking_display_limit", 3) or 0),
            empty_text=str(self.config.get("thinking_empty_text", "") or self.strings("thinking_empty_text")),
            bullet=str(self.config.get("thinking_bullet", "•") or ""),
        )

    def _emoji(self, key: str, fallback: str = "") -> str:
        return self.PREMIUM_EMOJIS.get(key, fallback)

    def _placeholder_values(
        self,
        *,
        elapsed: float | None = None,
        tool_count: int | None = None,
        thinking_notes: list[str] | None = None,
        keys: set[str] | None = None,
    ) -> dict[str, str]:
        requested = set(keys or ()) if keys is not None else None

        def wants(name: str) -> bool:
            return requested is None or name in requested

        def put(name: str, value: Any) -> None:
            if wants(name):
                values[name] = str(value)

        values: dict[str, str] = {}
        context_keys = {
            "chat_id",
            "user_id",
            "session_name",
            "session_messages",
            "runtime_comments_count",
            "runtime_comments",
        }
        ctx: dict[str, Any] = {}
        chat_id = None
        user_id = None
        cancel_token = None
        if requested is None or requested.intersection(context_keys):
            raw_ctx = getattr(self, "_placeholder_context", {})
            ctx = raw_ctx if isinstance(raw_ctx, dict) else {}
            chat_id = ctx.get("chat_id")
            user_id = ctx.get("user_id")
            cancel_token = ctx.get("cancel_token")

        put("agent_version", getattr(self, "version", ""))
        if wants("provider"):
            values["provider"] = self._provider_label()
        if wants("provider_key"):
            values["provider_key"] = self._provider()
        if wants("model"):
            values["model"] = self._model()
        if wants("reasoning_effort"):
            values["reasoning_effort"] = self._reasoning_effort()
        put("chat_id", chat_id or "")
        put("user_id", user_id or "")

        if wants("session_name") or wants("session_messages"):
            session_name = ""
            session_messages = "0"
            if chat_id is not None:
                with contextlib.suppress(Exception):
                    cid = int(chat_id)
                    active_id = getattr(self, "_active_session", {}).get(cid)
                    session = getattr(self, "_sessions", {}).get(active_id) if active_id else None
                    if session is None:
                        sessions = [
                            item for item in getattr(self, "_sessions", {}).values()
                            if getattr(item, "chat_id", None) == cid
                        ]
                        session = max(sessions, key=lambda item: getattr(item, "updated_at", 0), default=None)
                    if session is not None:
                        session_name = str(session.name or "")
                        session_messages = str(len(session.messages or []))
            put("session_name", session_name)
            put("session_messages", session_messages)

        if wants("runtime_comments_count") or wants("runtime_comments"):
            runtime_comments = list(getattr(self, "_runtime_comments", {}).get(str(cancel_token), [])) if cancel_token else []
            put("runtime_comments_count", len(runtime_comments))
            put("runtime_comments", "\n".join(str(item) for item in runtime_comments[-3:]))

        put("tool_count", tool_count if tool_count is not None else 0)
        if wants("available_tool_count"):
            values["available_tool_count"] = str(len(self._effective_tool_registry()))
        put("elapsed", f"{elapsed:.1f}" if elapsed is not None else "0.0")
        if wants("input_tokens"):
            values["input_tokens"] = str(self._last_token_usage.get("input_tokens", 0))
        if wants("output_tokens"):
            values["output_tokens"] = str(self._last_token_usage.get("output_tokens", 0))
        if wants("total_tokens"):
            values["total_tokens"] = str(self._last_token_usage.get("total_tokens", 0))
        if wants("thinking"):
            values["thinking"] = self._format_thinking_notes(thinking_notes)
        if wants("todo"):
            values["todo"] = self._format_todo_placeholder()
        if wants("random"):
            values["random"] = self._random_placeholder()
        put("prefix", getattr(self.kernel, "custom_prefix", ".") or ".")
        if wants("time"):
            values["time"] = time.strftime("%H:%M:%S")
        if wants("date"):
            values["date"] = time.strftime("%Y-%m-%d")
        if requested is None:
            for key, value in self.PREMIUM_EMOJIS.items():
                values[f"emoji_{key}"] = value
        else:
            for key in requested:
                if key.startswith("emoji_"):
                    emoji_key = key[6:]
                    if emoji_key in self.PREMIUM_EMOJIS:
                        values[key] = self.PREMIUM_EMOJIS[emoji_key]
        return values

    def _random_placeholder(self) -> str:
        raw_random = self.config.get("random_strings", []) or []
        return self._template_service().random_placeholder(raw_random)

    def _template_placeholder_keys(self, template: str) -> set[str]:
        return self._template_service().placeholder_keys(template)

    def _event_chat_id(self, event: Any | None) -> int | None:
        return self._template_service().event_chat_id(event)

    def _set_placeholder_context(self, event: Any | None = None, cancel_token: str | None = None) -> None:
        chat_id = None
        user_id = None
        if event is not None:
            chat_id = self._event_chat_id(event)
            user_id = getattr(event, "sender_id", None) or getattr(event, "user_id", None)
        self._placeholder_context = {
            "chat_id": chat_id,
            "user_id": user_id,
            "cancel_token": cancel_token,
        }

    def _render_template(
        self,
        template: str,
        *,
        elapsed: float | None = None,
        tool_count: int | None = None,
        thinking_notes: list[str] | None = None,
    ) -> str:
        result = template or ""
        values = self._placeholder_values(
            elapsed=elapsed,
            tool_count=tool_count,
            thinking_notes=thinking_notes,
            keys=self._template_placeholder_keys(result),
        )
        return self._template_service().render(result, values)

    def _thinking_text(self) -> str:
        return self._render_template(
            str(self.config.get("thinking_template", "") or self.strings("thinking_template_default"))
        )

    def _format_placeholders(self) -> str:
        return self._template_service().format_placeholder_help()

__all__ = [
    '_PLACEHOLDER_RE',
    'OpenAgentProviderService',
    'OpenAgentTemplateService',
    '_OpenAgentProviderMixin',
]
