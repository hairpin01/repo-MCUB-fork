from __future__ import annotations

from typing import Any, Callable
import html
import asyncio
import time
import inspect
import io
import difflib
import re
from pathlib import Path
import contextlib
import json

from .oasession import OASession

_TOOL_GROUP_ALIASES = {
    "web_search": "web",
    "send_message": "message",
    "dialogs": "dialog",
    "history": "message",
    "search_messages": "message",
}

_DEFAULT_TOOL_STATUS_EMOJIS = {
    "thinking": "❔",
    "terminal": "🖥",
    "web": "🌐",
    "file": "📦",
    "mcub": "🧲",
    "message": "💬",
    "dialog": "🗂",
    "chat": "🐈‍⬛",
    "moderation": "🛡",
    "profile": "👤",
    "contacts": "👥",
    "creation": "✨",
    "skills": "🧠",
    "code": "🧬",
    "context": "🧾",
    "todo": "📝",
    "utility": "🛠",
    "default": "🛠",
}

from .plugin import (
    OpenAgentPlugin,
)


class _OpenAgentToolRegistryMixin:
    """Built-in tool registry handlers and dispatch."""

    def _tool_attr_or_body(self, attrs_raw: str, body: str, *keys: str) -> str:
        attrs = self._parse_xml_attrs(attrs_raw)
        for key in keys:
            value = attrs.get(key)
            if value:
                return value.strip()
        return (body or "").strip()

    async def _skills_registry_tool(self, tool_name: str, attrs_raw: str, body: str) -> str:
        await asyncio.sleep(0)
        attrs = self._parse_xml_attrs(attrs_raw)
        if tool_name == "skills.list":
            skills = self._list_skills()
            return "\n".join(self._skill_name_from_path(path) for path in skills) or self.strings("skills_empty")
        if tool_name == "skills.repo_list":
            return await self._format_skill_repo_list()
        if tool_name == "skills.install":
            name = attrs.get("name") or body.strip()
            if not name:
                return self.strings("skill_name_required")
            saved = await self._install_repo_skill(name)
            return self.strings("skill_installed", name=saved)
        if tool_name == "skills.activate":
            query = attrs.get("query") or attrs.get("name") or body.strip()
            return self._activate_skill_text(query)
        if tool_name in {"skills.read", "skills.export_md"}:
            name = attrs.get("name") or body.strip()
            if not name:
                return self.strings("skill_name_required")
            path = self._find_skill_path(name)
            if not path.exists():
                return self.strings("skill_not_found")
            return path.read_text(encoding="utf-8", errors="replace")[:12000]
        if tool_name in {"skills.save_from_ai", "skills.import_md", "skill.save", "skill"}:
            name = attrs.get("name") or attrs.get("title") or "skill"
            if not body.strip():
                return self.strings("skill_empty")
            saved = self._save_skill(name, body)
            return self.strings("skill_saved", name=saved)
        return self.strings("unknown_skills_tool", tool=tool_name)

    async def _code_registry_tool(
        self,
        tool_name: str,
        attrs_raw: str,
        body: str,
        source_event: Any | None = None,
    ) -> str:
        """Handle code tools advertised in the OpenAgent tool registry."""
        await asyncio.sleep(0)
        attrs = self._parse_xml_attrs(attrs_raw)
        name = attrs.get("name") or attrs.get("path") or attrs.get("file") or "generated.py"
        content = body or attrs.get("content") or ""

        if tool_name == "code.choose_filename":
            filename = self._safe_generated_filename(name or content or "generated.py")
            self._last_generated_file = {"name": filename, "content": content}
            return filename

        if tool_name == "code.generate_file":
            filename = self._safe_generated_filename(name)
            if not content.strip():
                return "File content is required in tool body"
            self._last_generated_file = {"name": filename, "content": content}
            return f"Generated file prepared: {filename} ({len(content)} chars)"

        if tool_name == "code.generate_mcub_module":
            filename = self._safe_generated_filename(name)
            if not filename.endswith(".py"):
                filename = self._safe_generated_filename(f"{Path(filename).stem}.py")
            if not content.strip():
                return "MCUB module code is required in tool body"
            self._last_generated_file = {"name": filename, "content": content}
            return f"MCUB module prepared: {filename} ({len(content)} chars)"

        if tool_name == "code.attach_result":
            latest = getattr(self, "_last_generated_file", None)
            if not latest:
                return "No generated file is available to attach"
            filename = self._safe_generated_filename(str(latest.get("name") or "generated.py"))
            content = str(latest.get("content") or "")
            if not content:
                return "Generated file is empty"
            if source_event is None:
                return f"Generated file ready: {filename} ({len(content)} chars)"
            try:
                data = io.BytesIO(content.encode("utf-8"))
                data.name = filename
                await self.client.send_file(
                    self._event_chat_id(source_event) or source_event,
                    data,
                    caption=f"Generated file: {filename}",
                )
                return f"Generated file attached: {filename}"
            except Exception as exc:
                return f"Attach failed: {exc}"

        return "Unknown code tool"

    def _active_session_readonly(self, chat_id: int | None) -> OASession | None:
        if chat_id is None:
            return None
        with contextlib.suppress(Exception):
            cid = int(chat_id)
            active_id = getattr(self, "_active_session", {}).get(cid)
            if active_id:
                return getattr(self, "_sessions", {}).get(active_id)
        return None

    async def _prune_context_tool(self, attrs_raw: str, body: str, source_event: Any | None) -> str:
        attrs = self._parse_xml_attrs(attrs_raw)
        chat_id = self._event_chat_id(source_event)
        target_raw = attrs.get("target") or attrs.get("targets") or body.strip() or "all"
        targets = {
            item.strip().lower()
            for item in re.split(r"[,\s]+", target_raw)
            if item.strip()
        }
        if "all" in targets:
            targets.update({"history", "tools", "tool_memory", "runtime_comments"})
        keep = max(0, int(attrs.get("keep", "0") or 0))
        changed: list[str] = []
        session = self._active_session_readonly(int(chat_id)) if chat_id is not None else None

        if "history" in targets:
            if session is not None:
                if keep:
                    del session.messages[:-keep]
                else:
                    session.messages.clear()
                self._touch_session(session)
                changed.append(f"history:{len(session.messages)} kept")
            else:
                changed.append("history:no active session")

        if "tools" in targets or "tool_trace" in targets or "tool_outputs" in targets:
            if session is not None:
                before = len(session.messages)
                session.messages = [
                    msg for msg in session.messages
                    if "OpenAgent tool trace:" not in str(msg.get("content", ""))
                    and "Tool <" not in str(msg.get("content", ""))
                ]
                self._touch_session(session)
                changed.append(f"tools:{before - len(session.messages)} removed")
            else:
                changed.append("tools:no active session")

        if "tool_memory" in targets or "memory" in targets:
            if chat_id is not None:
                removed = len(self._tool_memory.pop(int(chat_id), []))
                changed.append(f"tool_memory:{removed} removed")
            else:
                changed.append("tool_memory:no chat")

        if "runtime_comments" in targets or "comments" in targets:
            token = attrs.get("token") or getattr(self, "_placeholder_context", {}).get("cancel_token")
            if token:
                removed = len(self._runtime_comments.pop(str(token), []))
            else:
                removed = sum(len(items) for items in self._runtime_comments.values())
                self._runtime_comments.clear()
            changed.append(f"runtime_comments:{removed} removed")

        return "Context prune complete: " + ("; ".join(changed) if changed else "nothing matched")

    async def _context_registry_tool(self, tool_name: str, attrs_raw: str, body: str, source_event: Any | None) -> str:
        chat_id = self._event_chat_id(source_event)
        if tool_name in {"context.prune", "context.discard"}:
            return await self._prune_context_tool(attrs_raw, body, source_event)
        if tool_name == "context.clear":
            if chat_id is not None:
                session = self._get_active_session(int(chat_id))
                session.messages.clear()
                self._touch_session(session)
                self._tool_memory.pop(int(chat_id), None)
            return "Context cleared"
        if tool_name == "context.remember":
            if chat_id is None:
                return "No chat context available"
            self._remember_context(chat_id, "Memory note", body.strip())
            return "Remembered in current chat context"
        if tool_name in {"context.reply_context", "context.media_context"} and source_event is not None:
            reply_context, _attachments = await self._reply_context(source_event)
            return reply_context or "No reply/media context available"
        if tool_name == "context.regenerate":
            return "Use the regenerate button under the last OpenAgent response"
        return f"Unknown context tool: {tool_name}"

    async def _utility_registry_tool(self, tool_name: str, attrs_raw: str, body: str) -> str:
        await asyncio.sleep(0)
        if tool_name == "utility.placeholders":
            return self._format_placeholders()
        if tool_name == "utility.random_template":
            return self._thinking_text()
        if tool_name == "utility.token_usage":
            usage = self._last_token_usage
            return "\n".join(f"{key}: {value}" for key, value in usage.items())
        if tool_name == "utility.agent_log":
            return "Agent log is shown under the final answer when tools are used"
        if tool_name == "utility.error_file":
            return "Errors are reported through the MCUB kernel error handler"
        if tool_name == "utility.tool_help":
            attrs = self._parse_xml_attrs(attrs_raw)
            query = body.strip() or attrs.get("tool") or ""
            query = str(query or "").strip().lower()
            if not query:
                return "Specify a tool name, e.g. utility.tool_help tool=message.send"
            docs = self._get_tool_docs(query)
            if query not in docs:
                return f"No documentation found for '{query}'. Available tools: {', '.join(sorted(self._get_tool_map().keys()))}"
            return self._format_tool_doc(query, docs[query])
        if tool_name == "utility.list_tools":
            all_docs = self._get_tool_docs()
            groups: dict[str, list[str]] = {}
            for tname, tdoc in sorted(all_docs.items()):
                group = self._tool_group(tname)
                groups.setdefault(group, []).append(tname)
            lines = ["📋 Available tools by category:"]
            for group in sorted(groups):
                names = sorted(groups[group])
                emoji = {
                    "thinking": "❔", "terminal": "🖥", "web": "🌐", "file": "📦",
                    "mcub": "🧲", "message": "💬", "dialog": "🗂", "chat": "🐈‍⬛",
                    "moderation": "🛡", "profile": "👤", "contacts": "👥",
                    "creation": "✨", "skills": "🧠", "code": "🧬",
                    "context": "🧾", "todo": "📝", "utility": "🛠",
                }.get(group, "🛠")
                items = "\n".join(f"  · {n} — {all_docs.get(n, {}).get('desc', '')}" for n in names)
                lines.append(f"\n{emoji} {group} ({len(names)}):\n{items}")
            lines.append("\nTip: call utility.tool_help tool=<tool.name> for arguments/body; call utility.plugin_docs for plugin docs.")
            return "\n".join(lines)[:9000]
        if tool_name == "utility.plugin_docs":
            attrs = self._parse_xml_attrs(attrs_raw)
            query = body.strip() or attrs.get("plugin") or attrs.get("name") or attrs.get("tool") or ""
            return self._format_plugin_docs(query or None)
        return f"Unknown utility tool: {tool_name}"

    async def _todo_registry_tool(self, tool_name: str, attrs_raw: str, body: str) -> str:
        await asyncio.sleep(0)
        attrs = self._parse_xml_attrs(attrs_raw)
        items = self._todo_items()

        if tool_name == "todo.add":
            text = (
                attrs.get("text")
                or attrs.get("task")
                or attrs.get("item")
                or attrs.get("title")
                or body.strip()
            )
            text = self._todo_parse_html_text(text)
            if not text:
                return "todo text is required"
            status = self._todo_normalize_status(attrs.get("status") or attrs.get("state") or "pending")
            items.append({"text": text[:500], "status": status})
            await self._save_todo_items(items)
            return "TODO item added\n" + self._format_todo_placeholder()

        if tool_name == "todo.closeall":
            if not items:
                return "TODO list is empty"
            for item in items:
                item["status"] = "closed"
            await self._save_todo_items(items)
            return "All TODO items closed\n" + self._format_todo_placeholder()

        if tool_name == "todo.clear":
            if not items:
                return "TODO list is already empty"
            await self._save_todo_items([])
            return "TODO list cleared"

        if tool_name == "todo.current":
            idx, error = self._todo_target_index(items, attrs, body)
            if idx is None:
                return error
            for i, item in enumerate(items):
                if item.get("status") == "open" and i != idx:
                    item["status"] = "pending"
            items[idx]["status"] = "open"
            await self._save_todo_items(items)
            return f"Current TODO: {items[idx]['text']}\n" + self._format_todo_placeholder()

        if tool_name == "todo.delete":
            idx, error = self._todo_target_index(items, attrs, body)
            if idx is None:
                return error
            removed = items.pop(idx)
            await self._save_todo_items(items)
            return f"TODO deleted: {removed['text']}\n" + self._format_todo_placeholder()

        if tool_name == "todo.close":
            idx, error = self._todo_target_index(items, attrs, body)
            if idx is None:
                return error
            items[idx]["status"] = "closed"
            await self._save_todo_items(items)
            return f"TODO closed: {items[idx]['text']}\n" + self._format_todo_placeholder()

        if tool_name == "todo.edit":
            target_body = body
            new_text = (
                attrs.get("new")
                or attrs.get("value")
                or attrs.get("text")
                or ""
            ).strip()
            if not attrs.get("index") and "|" in (body or ""):
                target_part, new_part = body.split("|", 1)
                target_body = target_part.strip()
                if not new_text:
                    new_text = new_part.strip()
            idx, error = self._todo_target_index(items, attrs, target_body)
            if idx is None:
                return error
            if not new_text:
                return "new todo text is required"
            parsed_text = self._todo_parse_html_text(new_text)
            if not parsed_text:
                return "new todo text is empty"
            items[idx]["text"] = parsed_text[:500]
            if attrs.get("status") or attrs.get("state"):
                items[idx]["status"] = self._todo_normalize_status(attrs.get("status") or attrs.get("state") or "")
            await self._save_todo_items(items)
            return f"TODO updated: {items[idx]['text']}\n" + self._format_todo_placeholder()

        return f"Unknown todo tool: {tool_name}"

    async def _thinking_note_tool(self, attrs_raw: str, body: str) -> str:
        await asyncio.sleep(0)
        # Detect when the model incorrectly put a real tool call inside the note body.
        # Surface an actionable error so the retry loop corrects the format.
        raw_body = (body or "").strip()
        embedded = self._extract_json_tool_calls(raw_body)
        real_embedded = [c for c in embedded if c[0] != "thinking.note"]
        if real_embedded:
            names = ", ".join(c[0] for c in real_embedded)
            return (
                f"[FORMAT ERROR] Tool call(s) found inside thinking.note body: {names}. "
                "The embedded tool(s) were NOT executed. "
                "Emit each tool as its own separate ```tool_call``` block. "
                "thinking.note must contain plain text only, never JSON tool calls."
            )
        note = self._thinking_note_text(attrs_raw, body)
        if not note:
            return "Thinking note recorded."
        return "Thinking note: " + note[:1200]

    def _thinking_note_text(self, attrs_raw: str, body: str) -> str:
        attrs = self._parse_xml_attrs(attrs_raw)
        text = (body or attrs.get("text") or attrs.get("note") or "").strip()
        text = html.unescape(text).strip()
        text = re.sub(r"^❔\s*", "", text).strip()
        text = re.sub(r"</?tool_call>", "", text, flags=re.I).strip()
        fenced = self.TOOL_CALL_JSON_RE.search(text)
        if fenced:
            text = fenced.group(1).strip()
        else:
            text = re.sub(r"^```(?:tool_call|json)?\s*|\s*```$", "", text, flags=re.I | re.S).strip()

        json_text = text
        if not json_text.startswith("{"):
            start = json_text.find("{")
            if start >= 0:
                json_text = json_text[start:]
        if json_text.startswith("{"):
            try:
                payload, _end = json.JSONDecoder().raw_decode(json_text)
                if isinstance(payload, dict):
                    args = payload.get("args") or {}
                    if isinstance(args, dict):
                        text = str(
                            args.get("note")
                            or args.get("text")
                            or payload.get("note")
                            or payload.get("text")
                            or text
                        ).strip()
                    else:
                        text = str(payload.get("note") or payload.get("text") or text).strip()
            except Exception:
                pass
        return text

    def _get_tool_map(self) -> dict[str, str]:
        """Unified mapping of tool tags to internal methods. Merges core + plugin maps.

        Cached after first build; invalidated by _register_plugin / _unregister_plugin.
        """
        if getattr(self, "_tool_map_cache", None) is not None:
            return self._tool_map_cache  # type: ignore[return-value]
        core = {
            # Core tools tightly coupled with module internals.
            "thinking.note": "_thinking_note_tool",
            "skill": "_skills_registry_tool",
            "skill.save": "_skills_registry_tool",
            "skills.list": "_skills_registry_tool",
            "skills.read": "_skills_registry_tool",
            "skills.activate": "_skills_registry_tool",
            "skills.import_md": "_skills_registry_tool",
            "skills.export_md": "_skills_registry_tool",
            "skills.save_from_ai": "_skills_registry_tool",
            "skills.install": "_skills_registry_tool",
            "skills.repo_list": "_skills_registry_tool",
            "code.generate_file": "_code_registry_tool",
            "code.generate_mcub_module": "_code_registry_tool",
            "code.choose_filename": "_code_registry_tool",
            "code.attach_result": "_code_registry_tool",
            "code.read_docs": "_fetch_mcub_docs",
            "context.remember": "_context_registry_tool",
            "context.clear": "_context_registry_tool",
            "context.prune": "_context_registry_tool",
            "context.discard": "_context_registry_tool",
            "context.regenerate": "_context_registry_tool",
            "context.reply_context": "_context_registry_tool",
            "context.media_context": "_context_registry_tool",
            "todo.add": "_todo_registry_tool",
            "todo.delete": "_todo_registry_tool",
            "todo.edit": "_todo_registry_tool",
            "todo.current": "_todo_registry_tool",
            "todo.close": "_todo_registry_tool",
            "todo.closeall": "_todo_registry_tool",
            "todo.clear": "_todo_registry_tool",
            "utility.token_usage": "_utility_registry_tool",
            "utility.placeholders": "_utility_registry_tool",
            "utility.random_template": "_utility_registry_tool",
            "utility.agent_log": "_utility_registry_tool",
            "utility.error_file": "_utility_registry_tool",
            "utility.tool_help": "_utility_registry_tool",
            "utility.list_tools": "_utility_registry_tool",
            "utility.plugin_docs": "_utility_registry_tool",
        }

        for plugin in self._plugins.values():
            for tname, handler in getattr(plugin, "tool_map", {}).items():
                if not tname or not handler:
                    continue
                core[str(tname).strip().lower()] = str(handler).strip()
        self._tool_map_cache: dict[str, str] = core
        return core

    async def _dispatch_tool(
        self,
        name: str,
        attrs_raw: str,
        body: str,
        source_event: Any,
        status_event: Any,
        agent_log: list[str],
        *,
        started_at: float | None = None,
        thinking_notes: list[str] | None = None,
    ) -> str:
        name = name.lower().strip()
        tmap = self._get_tool_map()
        # Plugin dispatch handles aliases via tool_map.

        # 1. Direct match or alias
        method_name = tmap.get(name)
        handler_method = None
        plugin_owner: OpenAgentPlugin | None = None

        # Check plugin handlers first. Exact tool_map ownership supports
        # legacy aliases like web_search/send_message/dialogs too.
        plugin_owner = self._get_plugin_for_tool(name)
        if plugin_owner:
            if method_name and hasattr(plugin_owner, method_name):
                handler_method = getattr(plugin_owner, method_name)
            else:
                pmap = getattr(plugin_owner, "tool_map", {})
                p_handler = pmap.get(name)
                if p_handler:
                    handler_method = getattr(plugin_owner, p_handler, None)
        if not handler_method and method_name:
            handler_method = getattr(self, method_name, None)
        if not handler_method:
            candidates = sorted(self._tool_names())
            nearest = ", ".join(difflib.get_close_matches(name, candidates, n=5, cutoff=0.45))
            suggestion = f" Closest matches: {nearest}." if nearest else ""
            return f"Error: Tool <{name}> not found in registry.{suggestion}"

        agent_log.append(name)
        if name == "thinking.note" and thinking_notes is not None:
            note = self._thinking_note_text(attrs_raw, body)
            if note:
                thinking_notes.append(note[:1200])
        display_value = "" if name == "thinking.note" else (attrs_raw or body)
        if self._requires_tool_confirmation(name, attrs_raw, body):
            if not status_event:
                self.log.debug(
                    "OA dispatch NO_CONFIRM_FORM: tool=%s no status_event, rejecting",
                    name,
                )
                return f"Tool <{name}> was not executed: user confirmation is required."
            elapsed = time.monotonic() - started_at if started_at is not None else None
            self.log.debug(
                "OA dispatch CONFIRM_TOOL: tool=%s status_has_edit=%s",
                name, hasattr(status_event, "edit"),
            )
            approved = await self._confirm_dangerous_tool(
                status_event,
                name,
                display_value,
                elapsed=elapsed,
            )
            if not approved:
                self.log.debug("OA dispatch TOOL_CANCELLED: tool=%s", name)
                return f"Tool <{name}> was cancelled by the user. Do not retry it unless the user explicitly asks."
            self.log.debug("OA dispatch TOOL_APPROVED: tool=%s", name)
        if status_event:
            elapsed = time.monotonic() - started_at if started_at is not None else None
            await self._show_agent_action(
                status_event,
                f"Executing {name}...",
                display_value,
                agent_log,
                tool_name=name,
                elapsed=elapsed,
                thinking_notes=thinking_notes,
            )

        try:
            # Normalize arguments based on method signature
            sig = inspect.signature(handler_method)
            params = sig.parameters
            # Parse XML attrs once; reused for mode/target/mcub/skill branches below.
            attrs = self._parse_xml_attrs(attrs_raw)

            kwargs = {}
            if "tool_name" in params: kwargs["tool_name"] = name
            if "attrs_raw" in params: kwargs["attrs_raw"] = attrs_raw
            if "body" in params: kwargs["body"] = body
            if "source_event" in params: kwargs["source_event"] = source_event
            if "status_event" in params: kwargs["status_event"] = status_event
            if "agent_log" in params: kwargs["agent_log"] = agent_log
            if "started_at" in params: kwargs["started_at"] = started_at
            if "thinking_notes" in params: kwargs["thinking_notes"] = thinking_notes
            if "runtime_token" in params: kwargs["runtime_token"] = self._placeholder_context.get("cancel_token")
            if "kind" in params:
                kwargs["kind"] = "group" if name.endswith("group") else "channel"
            if "command" in params: kwargs["command"] = body.strip() # for _run_terminal
            if "query" in params: kwargs["query"] = body.strip() or attrs_raw # fallback
            if "mode" in params:
                if name.endswith("list_groups"):
                    kwargs["mode"] = "groups"
                elif name.endswith("list_all"):
                    kwargs["mode"] = "all"
                else:
                    kwargs["mode"] = body.strip() or attrs.get("mode") or "private"
            if "target" in params: kwargs["target"] = body.strip() or attrs.get("target", "")

            if method_name == "_run_mcub_command" and not kwargs.get("command"):
                command_map = {
                    "mcub.modules": "man",
                    "mcub.config": "cfg",
                    "mcub.install": "dlm",
                    "mcub.reload": "restart",
                }
                kwargs["command"] = (
                    command_map.get(name, "")
                    or attrs.get("command")
                    or attrs.get("cmd")
                    or attrs.get("text")
                    or attrs.get("query")
                    or ""
                )
                result = await handler_method(**kwargs)
            elif method_name == "_save_skill":
                result = await self._skills_registry_tool(name, attrs_raw, body or attrs.get("content", ""))
            else:
                result = await handler_method(**kwargs)

            if status_event:
                elapsed = time.monotonic() - started_at if started_at is not None else None
                await self._show_agent_action(
                    status_event,
                    f"Updated {name}" if name.startswith("todo.") else f"Completed {name}",
                    result,
                    agent_log,
                    tool_name=name,
                    elapsed=elapsed,
                    thinking_notes=thinking_notes,
                    tool_done=True,
                )
            return result
        except Exception as e:
            err_type = type(e).__name__
            details = str(e).strip() or "no details"
            return (
                f"Tool <{name}> execution failed.\n"
                f"Error type: {err_type}\n"
                f"Details: {details[:1200]}\n"
                "Fix args and retry with a corrected tool call."
            )

class OpenAgentToolDisplayService:
    """Tool status/rendering helpers that can be tested without MCUB runtime."""

    def __init__(self) -> None:
        self._status_emojis_raw: str | None = None
        self._status_emojis_cache: dict[str, str] | None = None

    def tool_group(self, tool_name: str) -> str:
        tool_name = (tool_name or "").lower().strip()
        if "." in tool_name:
            return tool_name.split(".", 1)[0]
        if tool_name in _TOOL_GROUP_ALIASES:
            return _TOOL_GROUP_ALIASES[tool_name]
        return tool_name or "tool"

    def status_emoji_map(self, raw: str | None) -> dict[str, str]:
        raw_text = str(raw or "")
        if raw_text == self._status_emojis_raw and isinstance(self._status_emojis_cache, dict):
            return dict(self._status_emojis_cache)
        configured: dict[str, str] = {}
        for line in raw_text.splitlines():
            if "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip().lower()
            value = value.strip()
            if key and value:
                configured[key] = value
        self._status_emojis_raw = raw_text
        self._status_emojis_cache = dict(configured)
        return dict(configured)

    def status_emoji(
        self,
        tool_name: str,
        raw_status_emojis: str | None,
        emoji_getter: Callable[[str, str], str],
    ) -> str:
        tool_name = (tool_name or "").lower().strip()
        group = self.tool_group(tool_name)
        configured = self.status_emoji_map(raw_status_emojis)
        if tool_name in configured:
            return configured[tool_name]
        if group in configured:
            return configured[group]
        if "default" in configured:
            return configured["default"]
        if group == "reconnect":
            return emoji_getter("reconnect", "🔄")
        return _DEFAULT_TOOL_STATUS_EMOJIS.get(group, _DEFAULT_TOOL_STATUS_EMOJIS["default"])

    def status_text(self, tool_name: str, title: str, strings_getter: Callable[..., str]) -> str:
        tool_name = (tool_name or "").lower().strip()
        group = self.tool_group(tool_name)
        if tool_name == "thinking.note":
            return strings_getter("status_thinking")
        if group == "reconnect":
            return title or "Reconnect"
        status_key = {
            "terminal": "status_terminal",
            "web": "status_web",
            "file": "status_file",
            "mcub": "status_mcub",
            "message": "status_message",
            "chat": "status_chat",
            "dialog": "status_dialog",
            "code": "status_code",
            "todo": "status_todo",
        }.get(group)
        if status_key:
            return strings_getter(status_key)
        return title or strings_getter("status_default", tool=tool_name or "tool")

    @staticmethod
    def progress_bar(step: int, total: int, width: int = 10) -> str:
        total = max(1, total)
        step = max(0, min(step, total))
        filled = max(0, min(width, round(width * step / total)))
        return "▰" * filled + "▱" * (width - filled)

    @staticmethod
    def display_text(value: str, log: list[str], max_chars: int, log_lines: int) -> tuple[str, str]:
        safe_value = value if len(value) <= max_chars else value[:max_chars] + "..."
        log_text = "\n".join(log[-log_lines:]) if log_lines > 0 else ""
        if len(log_text) > 1800:
            log_text = log_text[-1800:]
        return safe_value, log_text

    def semantic_values(
        self,
        *,
        title: str,
        tool_name: str,
        safe_value: str,
        log_text: str,
        log: list[str],
        elapsed: float | None,
        thinking_line: str,
        tool_done: bool,
        agent_max_steps: int,
        raw_status_emojis: str | None,
        token_usage: dict[str, Any],
        provider_label: str,
        model: str,
        activity_text: str,
        emoji_getter: Callable[[str, str], str],
        strings_getter: Callable[..., str],
    ) -> dict[str, str]:
        step = len(log)
        total = agent_max_steps
        group = self.tool_group(tool_name)
        short = (tool_name or title or "tool").split(".")[-1]
        status_emoji = self.status_emoji(tool_name, raw_status_emojis, emoji_getter)
        status_text = self.status_text(tool_name, title, strings_getter)
        log_lines = html.escape(log_text)
        tool_input = "" if (tool_name or "").lower().strip() == "thinking.note" else html.escape(safe_value)
        tool_input_block = (
            f"<blockquote expandable><b>{emoji_getter('bubble', '📦')} Tool input</b>\n"
            f"<code>{tool_input}</code></blockquote>"
            if tool_input
            else ""
        )
        log_block = (
            f"<blockquote expandable><b>{emoji_getter('loading_lava', '😪')} Log tools</b>\n"
            f"<code>{log_lines}</code></blockquote>"
            if log_lines
            else ""
        )
        thinking_block = (
            f"<blockquote expandable><b>{emoji_getter('loading_dots', '❔')} Thinking</b>\n"
            f"{thinking_line}</blockquote>"
        )
        elapsed_text = f"{elapsed:.1f}s" if elapsed is not None else "0.0s"
        token_line = (
            f"{emoji_getter('grid', '💸')} in {token_usage.get('input_tokens', 0)}, "
            f"out {token_usage.get('output_tokens', 0)} | "
            f"total {token_usage.get('total_tokens', 0)}"
        )
        tool_running_emoji = "✍️"
        tool_done_emoji = "🌙"
        tool_running_emoji_html = '<tg-emoji emoji-id="5220046725493828505">✍️</tg-emoji>'
        tool_done_emoji_html = '<tg-emoji emoji-id="5253521692008917018">🌙</tg-emoji>'
        tool_state_emoji = tool_done_emoji if tool_done else tool_running_emoji
        tool_state_emoji_html = tool_done_emoji_html if tool_done else tool_running_emoji_html
        progress_percent = str(int(round(100 * min(step, total) / max(1, total))))
        return {
            "round": str(step),
            "round_total": str(total),
            "progress_bar": self.progress_bar(step, total),
            "progress_percent": progress_percent,
            "status_emoji": html.escape(status_emoji),
            "status_icon": html.escape(status_emoji),
            "status_emoji_html": status_emoji,
            "status_icon_html": status_emoji,
            "status_text": html.escape(status_text),
            "tool_state": "done" if tool_done else "running",
            "tool_state_emoji": tool_state_emoji,
            "tool_state_icon": tool_state_emoji,
            "tool_state_emoji_html": tool_state_emoji_html,
            "tool_state_icon_html": tool_state_emoji_html,
            "tool_running_emoji": tool_running_emoji,
            "tool_running_icon": tool_running_emoji,
            "tool_running_emoji_html": tool_running_emoji_html,
            "tool_running_icon_html": tool_running_emoji_html,
            "tool_done_emoji": tool_done_emoji,
            "tool_done_icon": tool_done_emoji,
            "tool_done_emoji_html": tool_done_emoji_html,
            "tool_done_icon_html": tool_done_emoji_html,
            "tool_group": html.escape(group),
            "tool_short": html.escape(short),
            "tool_input": tool_input,
            "tool_input_block": tool_input_block,
            "thinking_line": thinking_line,
            "thinking_block": thinking_block,
            "log_lines": log_lines,
            "log_block": log_block,
            "log_count": str(len(log)),
            "elapsed_line": f"⏳ {elapsed_text}",
            "token_line": html.escape(token_line),
            "model_line": html.escape(f"{provider_label} / {model}"),
            "activity_line": html.escape(f"{activity_text} {elapsed_text}"),
        }


class _OpenAgentToolDisplayMixin:
    """Tool grouping, status text and display rendering."""

    def _tool_display_service(self) -> OpenAgentToolDisplayService:
        service = getattr(self, "_tool_display_service_instance", None)
        if not isinstance(service, OpenAgentToolDisplayService):
            service = OpenAgentToolDisplayService()
            self._tool_display_service_instance = service
        return service

    def _tool_group(self, tool_name: str) -> str:
        return self._tool_display_service().tool_group(tool_name)

    def _tool_status_emoji_map(self) -> dict[str, str]:
        raw = self.config.get("tool_status_emojis", "") if hasattr(self, "config") else ""
        return self._tool_display_service().status_emoji_map(str(raw or ""))

    def _tool_status_emoji(self, tool_name: str) -> str:
        raw = self.config.get("tool_status_emojis", "") if hasattr(self, "config") else ""
        return self._tool_display_service().status_emoji(tool_name, str(raw or ""), self._emoji)

    def _tool_status_text(self, tool_name: str, title: str) -> str:
        return self._tool_display_service().status_text(tool_name, title, self.strings)

    def _progress_bar(self, step: int, total: int, width: int = 10) -> str:
        return self._tool_display_service().progress_bar(step, total, width)

    def _tool_display_semantic_values(
        self,
        *,
        title: str,
        tool_name: str,
        safe_value: str,
        log_text: str,
        log: list[str],
        elapsed: float | None,
        thinking_notes: list[str] | None,
        tool_done: bool = False,
    ) -> dict[str, str]:
        raw = self.config.get("tool_status_emojis", "") if hasattr(self, "config") else ""
        return self._tool_display_service().semantic_values(
            title=title,
            tool_name=tool_name,
            safe_value=safe_value,
            log_text=log_text,
            log=log,
            elapsed=elapsed,
            thinking_line=self._format_thinking_notes(thinking_notes),
            tool_done=tool_done,
            agent_max_steps=self.AGENT_MAX_STEPS,
            raw_status_emojis=str(raw or ""),
            token_usage=self._last_token_usage,
            provider_label=self._provider_label(),
            model=self._model(),
            activity_text=self._random_placeholder(),
            emoji_getter=self._emoji,
            strings_getter=self.strings,
        )

    def _render_tool_display(
        self,
        *,
        title: str,
        tool_name: str,
        value: str,
        log: list[str],
        elapsed: float | None = None,
        thinking_notes: list[str] | None = None,
        tool_done: bool = False,
    ) -> str:
        max_chars = int(self.config.get("tool_display_max_chars", 30) or 30)
        log_lines = int(self.config.get("tool_display_log_lines", 8) or 8)
        safe_value, log_text = self._tool_display_service().display_text(value, log, max_chars, log_lines)
        template = str(self.config.get("tool_display_template", "") or "")
        if not template:
            template = "<blockquote expandable><i>{thinking_line}</i></blockquote>\n<blockquote expandable><strong>┌|</strong> {tool_state_emoji_html} {status_emoji_html} <em>{status_text}</em> <code>{tool}</code>\n<strong>└|</strong> <a href=\"tg://emoji?id=6010570945637392851\">🥳</a>  <b>Round:</b> <code>{round}/{round_total}</code> • <b>Reasoning:</b>\n<code>{reasoning_effort}</code>\n</blockquote><blockquote><a href=\"tg://emoji?id=5310041868191407556\">🩸</a> <strong>{activity_line}</strong></blockquote>\n<blockquote expandable><a href=\"tg://emoji?id=6012361831035705571\">😪</a> <strong>Log tools</strong>\n<code>{log_lines}</code></blockquote>"
        template_keys = self._template_placeholder_keys(template)
        placeholder_keys = set(template_keys)
        if "todo_html" in placeholder_keys:
            placeholder_keys.add("todo")
        placeholder_values = self._placeholder_values(
            elapsed=elapsed,
            tool_count=len(log),
            thinking_notes=thinking_notes,
            keys=placeholder_keys,
        )
        values = {
            key: html.escape(value)
            for key, value in placeholder_values.items()
        }
        todo_raw = placeholder_values.get("todo", "")
        values["todo"] = todo_raw
        values["todo_html"] = todo_raw
        values.update({
            "title": html.escape(title),
            "tool": html.escape(tool_name or title),
            "value": html.escape(safe_value),
            "log": html.escape(log_text),
            "step": str(len(log)),
            "tool_count": str(len(log)),
        })
        values.update(
            self._tool_display_semantic_values(
                title=title,
                tool_name=tool_name,
                safe_value=safe_value,
                log_text=log_text,
                log=log,
                elapsed=elapsed,
                thinking_notes=thinking_notes,
                tool_done=tool_done,
            )
        )
        for key, item in values.items():
            template = template.replace("{" + key + "}", item)
        return template

    def _tool_registry_prompt(self) -> str:
        lines = []
        for index, name in enumerate(self._effective_tool_registry(), 1):
            lines.append(f"{index}. {name}")
        return "\n".join(lines)


class _OpenAgentRuntimeToolsMixin:
    """System prompt construction and local runtime tools."""

    def _flash_system_prompt(self) -> str:
        return (
            "You are OpenAgent in flash mode inside a Telegram userbot. "
            "Answer the user's current request directly, briefly, and practically. "
            "Do not use tool calls, XML tags, or fenced tool_call JSON. "
            "Use the provided context only when it is clearly relevant."
        )

    def _active_plugins_prompt(self) -> str:
        lines = ["\n\n## Activated plugins"]
        plugins = getattr(self, "_plugins", {}) or {}
        if not plugins:
            lines.append("- none")
            return "\n".join(lines)

        lines.append(
            "Plugin docs below are compact. For full docs call utility.plugin_docs; "
            "for one tool call utility.tool_help."
        )
        lines.append(self._format_plugin_docs(max_tools=8))
        return "\n".join(lines)

    def _thinking_system_prompt(self, flash_mode: bool = False) -> str:
        base = self._flash_system_prompt() if flash_mode else str(self.config["system_prompt"]).strip()
        effort = self._reasoning_effort()
        profiles = {
            "off": (
                "Default to SKIP. Use thinking.note only for clearly multi-step tasks or risky actions. "
                "Limit: 60 chars."
            ),
            "low": (
                "Use thinking.note only for the most necessary progress notes. "
                "No meta chatter. Limit: 80 chars."
            ),
            "medium": (
                "Use thinking.note for useful planning, findings, risks, or next steps. "
                "Limit: 180 chars."
            ),
            "high": (
                "Use richer thinking.note entries for complex debugging/refactoring: current hypothesis, evidence, risk, or next action. "
                "Limit: 360 chars."
            ),
            "xhigh": (
                "Use detailed but user-facing thinking.note entries for hard multi-step work, similar to a compact DeepSeek-style work log. "
                "Include hypothesis/evidence/next action when useful. Limit: 700 chars."
            ),
        }
        profile = profiles.get(effort, profiles["off"])
        return (
            f"{base}\n\n"
            f"Your ONLY task right now: decide whether a progress note is useful. Current reasoning_effort={effort}.\n"
            f"Thinking note policy: {profile}\n"
            "For simple chat, greetings, or short answers, output only: SKIP\n"
            "When using thinking.note, write any note you find useful: thought, plan, finding, risk, or next action. Follow the profile limit above.\n"
            "Do NOT write a generic heartbeat. Do NOT put any tool call JSON inside the note text.\n\n"
            "If useful, output only this shape:\n"
            "```tool_call\n"
            "{\"tool\":\"thinking.note\",\"args\":{\"note\":\"<your own short note>\"}}\n"
            "```"
        )

    def _system_prompt(self, user_prompt: str = "", flash_mode: bool = False) -> str:
        if flash_mode:
            return self._flash_system_prompt()

        prompt = str(self.config["system_prompt"]).strip()
        tlist = ", ".join(sorted(self._get_tool_map().keys()))
        todo_snapshot = self._format_todo_placeholder()
        prompt += (
            f"\n\n{self.name} {self.version} is active. Author: {self.author}. You have access to {len(self._effective_tool_registry())} tool operations.\n"
            "\n## What tools are\n"
            "Tools are OpenAgent operations that let you do work outside plain text: inspect the workspace, run terminal commands, use MCUB/Telegram actions, manage skills/todos/context, and call plugin features.\n"
            "Core tools are built into OpenAgent. Plugin tools are created and registered by activated OpenAgent plugins; a plugin can add new tool names, handlers, and documentation.\n"
            "Always call tools when you need external state, actions, files, Telegram/MCUB operations, or tool/plugin documentation.\n"
            "\n## Tool call format\n"
            "Output one or more fenced JSON blocks. Each block is ONE tool call:\n"
            "```tool_call\n"
            "{\"tool\":\"tool.name\",\"args\":{\"key\":\"value\"},\"body\":\"optional long text\"}\n"
            "```\n"
            "Use `args` for structured parameters. Use `body` for commands, messages, file content, or long text.\n"
            "\n## Batching — emit multiple blocks in ONE turn to save steps\n"
            "```tool_call\n"
            "{\"tool\":\"thinking.note\",\"args\":{\"note\":\"Listing files to find the config\"}}\n"
            "```\n"
            "```tool_call\n"
            "{\"tool\":\"terminal.run\",\"args\":{\"cmd\":\"ls -la\"}}\n"
            "```\n"
            "RULE: thinking.note body/note MUST be plain text. NEVER put a tool call JSON inside thinking.note.\n"
            "WRONG: {\"tool\":\"thinking.note\",\"args\":{\"note\":\"{\\\"tool\\\":\\\"terminal.run\\\",\\\"args\\\":{\\\"cmd\\\":\\\"ls\\\"}}\"}}\n"
            "RIGHT: two separate ```tool_call``` blocks as shown above.\n"
            "\n## Format rules\n"
            "- ONLY ```tool_call``` fenced JSON blocks. No XML tags. No plain JSON outside fences.\n"
            "- When no tool is needed: reply in plain text with no ```tool_call``` blocks at all.\n"
             f"Available tool names: {tlist}\n"
             "\n## Tool discovery and docs\n"
             "- Call utility.list_tools to get the current list of core and plugin tools grouped by category.\n"
             "- Call utility.tool_help with args {\"tool\":\"tool.name\"} to get one tool's description, arguments, and body usage.\n"
             "- Call utility.plugin_docs with optional args {\"plugin\":\"plugin_name\"} to inspect activated plugin docs and tools.\n"
             "- These discovery utilities are tools too: call them with ```tool_call``` blocks instead of guessing.\n"
             "\n## Guidelines\n"
             "1. Use only tools from 'Available tool names'. Wrong names fail immediately.\n"
             "2. mcub.* tools: omit the userbot prefix (body='ping', not '.ping').\n"
             "3. Unknown domain? Call skills.activate first. To persist knowledge: skills.save_from_ai.\n"
             "4. Simple greetings/questions: answer in plain text, no tools.\n"
             "5. thinking.note: use for meaningful progress updates only — findings, risky actions, approach changes.\n"
             "6. Multi-step tasks: keep todo.* in sync (todo.add → todo.current → todo.close → todo.clear).\n"
             "7. Don't know how to use a tool? Call utility.tool_help tool=<name> to see its arguments and description.\n"
             "   Or utility.list_tools to browse all tools by category, utility.plugin_docs for plugin docs.\n"
             "Never explain tool calls. Output the block(s) and wait for results."
        )
        prompt += "\n\nCurrent TODO state:\n" + todo_snapshot
        prompt += self._load_skills_prompt(user_prompt)
        prompt += self._repo_context_prompt()
        prompt += self._active_plugins_prompt()
        return prompt

    async def _run_terminal(self, command: str) -> str:
        proc = await asyncio.create_subprocess_shell(
            command,
            cwd=self._workspace_dir(),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        try:
            stdout, stderr = await asyncio.wait_for(
                proc.communicate(), timeout=int(self.config["terminal_timeout"])
            )
        except asyncio.TimeoutError:
            proc.kill()
            await proc.communicate()
            return f"Command timed out after {self.config['terminal_timeout']}s"

        out = stdout.decode("utf-8", errors="replace")
        err = stderr.decode("utf-8", errors="replace")
        result = f"exit_code={proc.returncode}\n"
        if out:
            result += f"stdout:\n{out}\n"
        if err:
            result += f"stderr:\n{err}\n"
        return result[-6000:]


__all__ = [
    '_DEFAULT_TOOL_STATUS_EMOJIS',
    '_TOOL_GROUP_ALIASES',
    'OpenAgentToolDisplayService',
    '_OpenAgentToolDisplayMixin',
    '_OpenAgentRuntimeToolsMixin',
    '_OpenAgentToolRegistryMixin'
]
