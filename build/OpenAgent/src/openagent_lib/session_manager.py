from __future__ import annotations
"""Plain service for OpenAgent chat sessions and persistence."""

import re
import json
import time
import uuid
import html
import asyncio
import tempfile
import datetime
import contextlib
from pathlib import Path
from typing import (
    Any,
    Callable,
)

from .oasession import OASession

_SESSION_PREFERENCES = frozenset({"ask", "continue", "new"})


class _OpenAgentSessionsMixin:
    """Named OA sessions, choice panels and pending prompts."""

    def _sessions_file(self) -> Path:
        return self.session_manager.sessions_file

    async def _load_sessions(self) -> None:
        """Load persisted sessions from disk."""
        await self.session_manager.load()

    async def _save_sessions(self) -> None:
        """Persist sessions to disk (fire-and-forget via create_task)."""
        await self.session_manager.save()

    def _new_session(self, chat_id: int, name: str | None = None) -> OASession:
        """Create a fresh session and make it active for chat_id."""
        return self.session_manager.new_session(chat_id, name)

    def _fresh_session(self, chat_id: int, name: str | None = None) -> OASession:
        """Reuse current empty chat; otherwise create a fresh session."""
        return self.session_manager.get_fresh_session(chat_id, name)

    def _get_active_session(self, chat_id: int) -> OASession:
        """Return active session for chat_id, creating one if needed."""
        return self.session_manager.get_active_session(chat_id)

    def _get_chat_sessions(self, chat_id: int) -> list[OASession]:
        """Return all sessions for a chat, sorted newest-first."""
        return self.session_manager.get_chat_sessions(chat_id)

    def _enforce_session_limit(self, chat_id: int) -> None:
        """Keep at most SESSION_LIMIT sessions per chat, pruning oldest."""
        self.session_manager.enforce_limit(chat_id)

    def _touch_session(self, session: OASession) -> None:
        self.session_manager.touch_session(session)

    def _set_active_session(self, chat_id: int, session_id: str) -> OASession | None:
        return self.session_manager.set_active_session(chat_id, session_id)

    def _session_default_names(self) -> set[str]:
        return {
            "New chat",
            "Новый чат",
            "Новый чатик",
            "new-chat",
            self.strings("new_session_name"),
        }

    def _session_needs_auto_name(self, session: OASession) -> bool:
        return bool(session.messages) and (session.name or "").strip() in self._session_default_names()

    def _schedule_auto_name_session(self, session: OASession) -> None:
        if not self._session_needs_auto_name(session):
            return
        asyncio.get_event_loop().call_soon(
            lambda: asyncio.ensure_future(self._auto_name_session(session.id))
        )

    async def _auto_name_session(self, session_id: str) -> None:
        session = self._sessions.get(session_id)
        if session is None or not self._session_needs_auto_name(session):
            return
        api_key = self._api_key()
        if not api_key:
            return
        first_prompt = ""
        for item in session.messages:
            if item.get("role") == "user":
                first_prompt = str(item.get("content", "")).strip()
                break
        if not first_prompt:
            return
        provider = self._provider()
        prompt = self.strings("auto_name_prompt", prompt=first_prompt[:200])
        messages = [
            {"role": "system", "content": "Return only a short title, no quotes, no punctuation at the end."},
            {"role": "user", "content": prompt},
        ]
        try:
            if provider in ("openai", "openrouter", "groq", "deepseek", "xai", "other"):
                title = await self._ask_openai_compatible(provider, messages, api_key, max_tokens_override=32)
            elif provider == "google":
                title = await self._ask_google(messages, api_key)
            else:
                return
        except Exception as exc:
            self.log.debug("OpenAgent: session auto-name failed: %s", exc)
            return
        title = re.sub(r"[\r\n]+", " ", str(title or "")).strip(" `\"'«»“”.,;:!-_")
        title = re.sub(r"\s+", " ", title)[:64].strip()
        if not title or not self._session_needs_auto_name(session):
            return
        session.name = title
        session.model = self._model(provider)
        self._touch_session(session)

    def _session_age_label(self, timestamp: float) -> str:
        try:
            dt = datetime.fromtimestamp(timestamp)
        except Exception:
            return ""
        today = datetime.now().date()
        day = dt.date()
        delta = (today - day).days
        if delta <= 0:
            return self.strings("chat_today")
        if delta == 1:
            return self.strings("chat_yesterday")
        if delta < 7:
            return self.strings("chat_days_ago", days=delta)
        return dt.strftime("%d.%m.%Y")

    def _cleanup_session_inputs(self) -> None:
        if len(self._session_input_events) <= 50:
            return
        stale = sorted(
            self._session_input_events,
            key=lambda key: self._session_input_events[key].get("created_at", 0),
        )[:-50]
        for key in stale:
            self._session_input_events.pop(key, None)

    def _make_session_input_token(self, chat_id: int, kind: str, source_event: Any | None = None) -> str:
        token = str(uuid.uuid4())
        self._session_input_events[token] = {
            "event": source_event,
            "chat_id": chat_id,
            "kind": kind,
            "created_at": time.time(),
        }
        self._cleanup_session_inputs()
        return token

    async def _inline_target(self, event: Any, chat_id: int | None = None) -> Any | None:
        """Resolve a concrete entity for inline forms.

        Telethon's InlineResult.click requires a non-empty entity. Some callback
        events do not expose ``chat_id`` directly, so fall back to the event's
        input chat/chat object before giving up.
        """
        if chat_id not in (None, 0, ""):
            return chat_id
        for attr in ("input_chat", "chat", "entity"):
            target = getattr(event, attr, None)
            if target:
                return target
        for method_name in ("get_input_chat", "get_chat"):
            method = getattr(event, method_name, None)
            if callable(method):
                with contextlib.suppress(Exception):
                    target = await method()
                    if target:
                        return target
        return None

    def _render_sessions_panel(self, chat_id: int) -> str:
        active_id = self._active_session.get(chat_id)
        lines = [self.strings("chats_title"), html.escape(self.strings("oa_choose_chat")), ""]
        for session in self._get_chat_sessions(chat_id):
            marker = "●" if session.id == active_id else " "
            name = html.escape(session.name or self.strings("new_session_name"))
            age = html.escape(self._session_age_label(session.updated_at))
            if session.messages:
                lines.append(f"{marker} <b>{name}</b>     <i>{age}</i>")
            else:
                lines.append(f"{marker} <b>{name}</b>     <i>{html.escape(self.strings('chat_empty'))}</i>")
        return "\n".join(lines)

    def _last_saved_assistant_turn(self, chat_id: int) -> tuple[str, str, list[str]] | None:
        """Return (prompt, answer, thinking_notes) from the active session history."""
        session = self._get_active_session(chat_id)
        messages = session.messages or []
        for index in range(len(messages) - 1, -1, -1):
            item = messages[index]
            if item.get("role") != "assistant":
                continue
            answer = str(item.get("content") or "").strip()
            if not answer:
                continue
            prompt = ""
            for prev in range(index - 1, -1, -1):
                prev_item = messages[prev]
                if prev_item.get("role") == "user":
                    prompt = str(prev_item.get("content") or "").strip()
                    break
            return prompt, answer, list(getattr(session, "thinking_notes", []) or [])
        return None

    def _sessions_panel_buttons(self, chat_id: int, source_event: Any | None = None) -> list[list[Any]]:
        rows: list[list[Any]] = []
        allow_user = getattr(source_event, "sender_id", None)
        for session in self._get_chat_sessions(chat_id):
            marker = "●" if self._active_session.get(chat_id) == session.id else " "
            label = f"{marker} {session.name or self.strings('new_session_name')}"
            rows.append([self.Button.inline(label[:64], self._switch_session, args=(session.id,), style="primary")])
        rows.append([
            self.Button.input(
                self.strings("new_chat_button"),
                self._on_new_session_input,
                placeholder=self.strings("new_chat_placeholder"),
                allow_user=allow_user,
                style="primary",
                data=self._make_session_input_token(chat_id, "new", source_event),
            )
        ])
        rows.append([
            self.Button.input(
                self.strings("ask_this_chat_button"),
                self._on_ask_this_session_input,
                placeholder=self.strings("ask_this_chat_placeholder"),
                allow_user=allow_user,
                style="primary",
                data=self._make_session_input_token(chat_id, "ask", source_event),
            )
        ])
        if self._last_saved_assistant_turn(int(chat_id)) is not None:
            rows.append([
                self.Button.inline(
                    self.strings("return_to_chat_button"),
                    self._return_to_last_response,
                    args=(chat_id,),
                    style="primary",
                )
            ])
        rows.append([
            self.Button.input(
                self.strings("rename_chat_button"),
                self._on_rename_session_input,
                placeholder=self.strings("rename_chat_placeholder"),
                allow_user=allow_user,
                style="primary",
                data=self._make_session_input_token(chat_id, "rename", source_event),
            ),
            self.Button.inline(self.strings("delete_chat_button"), self._delete_active_session, args=(chat_id,), style="danger"),
        ])
        rows.append([self.Button.inline(self.strings("remember_chat_button"), self._remember_session_choice, args=(chat_id,), style="primary")])
        return rows

    async def _show_sessions_panel(
        self,
        event: Any,
        chat_id: int,
        *,
        alert: str | None = None,
        force_inline: bool = False,
    ) -> None:
        self._get_active_session(chat_id)
        text = self._render_sessions_panel(chat_id)
        if alert and hasattr(event, "answer"):
            with contextlib.suppress(Exception):
                await event.answer(alert, alert=False)
        if force_inline:
            target = await self._inline_target(event, chat_id)
            if not target:
                await self.edit(event, text, as_html=True)
                return
            token = str(uuid.uuid4())
            loop = asyncio.get_running_loop()
            future: asyncio.Future[Any] = loop.create_future()
            self._inline_status_waiters[token] = future
            try:
                _unit, sms = await self.inline(
                    target,
                    text,
                    buttons=[[self.Button.inline(" ", self._activate_inline_status, args=(token,), style="primary")]],
                    ttl=900,
                    parse_mode="html",
                    reply_to=getattr(event, "reply_to", None),
                )

                if sms:
                    with contextlib.suppress(Exception):
                        await sms.click(0)
                try:
                    panel_event = await asyncio.wait_for(future, timeout=5)
                except asyncio.TimeoutError:
                    panel_event = sms or event
                buttons = self._sessions_panel_buttons(chat_id, source_event=panel_event)
                if hasattr(panel_event, "edit"):
                    await panel_event.edit(text, buttons=buttons, parse_mode="html")
                with contextlib.suppress(Exception):
                    setattr(panel_event, "_openagent_source_chat_id", chat_id)
                with contextlib.suppress(Exception):
                    await event.delete()
                return
            except Exception as exc:
                self.log.debug("OpenAgent: inline sessions panel fallback: %s", exc)
            finally:
                self._inline_status_waiters.pop(token, None)

        buttons = self._sessions_panel_buttons(chat_id, source_event=event)
        try:
            if hasattr(event, "edit"):
                await event.edit(text, buttons=buttons, parse_mode="html")
                return
        except Exception:
            pass
        try:
            target = await self._inline_target(event, chat_id)
            if not target:
                raise ValueError("chat target is missing")
            _unit, _sms = await self.inline(target, text, buttons=buttons, ttl=900, parse_mode="html", reply_to=getattr(event, "reply_to", None))
            if hasattr(event, "delete"):
                with contextlib.suppress(Exception):
                    await event.delete()
        except Exception:
            await self.edit(event, text, as_html=True)





    async def _on_new_session_input(self, event: Any, text: str, data: str) -> None:
        entry = self._session_input_events.pop(data, None)
        if not entry:
            return
        chat_id = int(entry["chat_id"])
        name = (text or "").strip() or None
        session = self._new_session(chat_id, name=name)
        panel_event = entry.get("event") or event
        await self._show_sessions_panel(panel_event, chat_id, alert=self.strings("chat_created", name=session.name))

    async def _on_rename_session_input(self, event: Any, text: str, data: str) -> None:
        entry = self._session_input_events.pop(data, None)
        if not entry:
            return
        chat_id = int(entry["chat_id"])
        name = (text or "").strip()
        if not name:
            return
        session = self._get_active_session(chat_id)
        session.name = name[:64]
        self._touch_session(session)
        panel_event = entry.get("event") or event
        await self._show_sessions_panel(panel_event, chat_id, alert=self.strings("chat_renamed", name=session.name))

    async def _on_ask_this_session_input(self, event: Any, text: str, data: str) -> None:
        entry = self._session_input_events.pop(data, None)
        prompt = (text or "").strip()
        if not entry or not prompt:
            return
        chat_id = int(entry["chat_id"])
        source_event = entry.get("event") or event
        prompt_token = self._store_pending_prompt(
            chat_id,
            prompt,
            prompt,
            [],
            source_event=source_event,
        )
        await self._execute_pending(event, prompt_token)

    def _store_pending_prompt(
        self,
        chat_id: int,
        prompt: str,
        full_prompt: str,
        attachments: list[dict[str, str]],
        source_event: Any | None = None,
    ) -> str:
        token = str(uuid.uuid4())
        self._pending_prompts[token] = {
            "chat_id": chat_id,
            "prompt": prompt,
            "full_prompt": full_prompt,
            "attachments": attachments,
            "source_event": source_event,
            "created_at": time.time(),
        }
        if len(self._pending_prompts) > 30:
            stale = sorted(
                self._pending_prompts,
                key=lambda k: self._pending_prompts[k]["created_at"],
            )[:-30]
            for k in stale:
                self._pending_prompts.pop(k, None)
        return token

    def _oa_choice_text(self, chat_id: int) -> str:
        active_id = self._active_session.get(chat_id)
        lines = [self.strings("oa_chat_choice_title"), ""]
        for session in self._get_chat_sessions(chat_id):
            marker = "●" if session.id == active_id else " "
            name = html.escape(session.name or self.strings("new_session_name"))
            if session.messages:
                age = html.escape(self._session_age_label(session.updated_at))
                lines.append(f"{marker} <b>{name}</b>     <i>{age}</i>")
            else:
                lines.append(f"{marker} <b>{name}</b>     <i>{html.escape(self.strings('chat_empty'))}</i>")
        return "\n".join(lines)

    def _oa_choice_buttons(
        self,
        chat_id: int,
        prompt_token: str,
        source_event: Any | None = None,
    ) -> list[list[Any]]:
        allow_user = getattr(source_event, "sender_id", None)
        rows: list[list[Any]] = []
        active_id = self._active_session.get(chat_id)
        for session in self._get_chat_sessions(chat_id):
            marker = "●" if session.id == active_id else " "
            label = f"{marker} {session.name or self.strings('new_session_name')}"
            if session.id == active_id:
                btn = self.Button.inline(
                    label[:64],
                    self._run_pending_here,
                    args=(prompt_token,),
                    style="primary",
                )
            else:
                btn = self.Button.inline(
                    label[:64],
                    self._run_pending_in,
                    args=(prompt_token, session.id),
                    style="primary",
                )
            rows.append([btn])
        rows.append([
            self.Button.input(
                self.strings("new_chat_button"),
                self._on_new_session_for_pending,
                placeholder=self.strings("new_chat_placeholder"),
                allow_user=allow_user,
                style="primary",
                data=f"{prompt_token}:{chat_id}",
            ),
        ])
        rows.append([
            self.Button.inline(
                self.strings("remember_pref_continue"),
                self._remember_pref_continue,
                args=(prompt_token, chat_id),
                style="primary",
            ),
            self.Button.inline(
                self.strings("remember_pref_new"),
                self._remember_pref_new,
                args=(prompt_token, chat_id),
                style="primary",
            ),
        ])
        return rows

    async def _show_oa_choice_panel(
        self,
        event: Any,
        chat_id: int,
        prompt_token: str,
    ) -> None:
        text = self._oa_choice_text(chat_id)
        buttons = self._oa_choice_buttons(chat_id, prompt_token, source_event=event)
        try:
            target = await self._inline_target(event, chat_id)
            if not target:
                raise ValueError("chat target is missing")
            _unit, _sms = await self.inline(target, text, buttons=buttons, ttl=900, parse_mode="html", reply_to=getattr(event, "reply_to", None))
            with contextlib.suppress(Exception):
                await event.delete()
        except Exception:
            await self.edit(event, text, as_html=True)

    async def _execute_pending(self, event: Any, prompt_token: str) -> None:
        """Run a stored pending prompt using event for status display."""
        entry = self._pending_prompts.pop(prompt_token, None)
        if not entry:
            return
        prompt = entry["prompt"]
        full_prompt = entry["full_prompt"]
        attachments = entry.get("attachments") or []
        chat_id = entry.get("chat_id") or getattr(event, "chat_id", None)
        source_event = entry.get("source_event") or event
        status_event = event
        if getattr(status_event, "chat_id", None) is None and not hasattr(status_event, "edit"):
            status_event = source_event
        cancel_token = str(uuid.uuid4())
        self._set_placeholder_context(source_event, cancel_token)
        loading = await self._start_inline_status(
            status_event,
            self._thinking_text(),
            self._runtime_control_buttons(cancel_token, source_event),
        )
        started = time.monotonic()
        try:
            answer, agent_log, thinking_notes, tool_trace = await self._ask_agent(
                full_prompt,
                status_event=loading or event,
                source_event=source_event,
                attachments=attachments,
                cancel_token=cancel_token,
                started_at=started,
            )
            self._last_request_at = time.time()
            elapsed = time.monotonic() - started
            self._remember_context(chat_id, full_prompt, answer, tool_trace, thinking_notes)
            await self._reply_text(
                loading or status_event,
                answer,
                title=self._response_title(
                    elapsed,
                    tool_count=len(agent_log),
                    thinking_notes=thinking_notes,
                ),
                prompt=prompt,
                agent_log=agent_log,
                thinking_notes=thinking_notes,
                buttons=self._final_buttons(
                    chat_id,
                    prompt,
                    full_prompt,
                    attachments,
                    source_event=source_event,
                ),
                edit_current=True,
            )
            self._store_last_loading(chat_id, loading)
            self._cleanup_runtime_run(cancel_token)
        except Exception as exc:
            self._cleanup_runtime_run(cancel_token)
            await self._reply_error_answer(
                loading or status_event,
                exc,
                prompt=prompt,
                full_prompt=full_prompt,
                attachments=attachments,
                source_event=source_event,
                chat_id=chat_id,
                started_at=started,
                source="OpenAgent:pending",
            )

    async def _on_new_session_for_pending(self, event: Any, text: str, data: str) -> None:
        """Button.input: create a new session then run the pending prompt."""
        parts = str(data).split(":", 1)
        if len(parts) != 2:
            return
        prompt_token, chat_id_str = parts
        chat_id = int(chat_id_str)
        name = (text or "").strip() or None
        self._new_session(chat_id, name=name)
        await self._execute_pending(event, prompt_token)

class SessionManager:
    """Plain service for OpenAgent chat sessions and persistence."""

    def __init__(
        self,
        sessions_file: Path,
        *,
        logger: Any,
        model_getter: Callable[[], str],
        default_name_getter: Callable[[], str],
        session_limit: int,
    ) -> None:
        self.sessions_file = sessions_file
        self.sessions_file.parent.mkdir(parents=True, exist_ok=True)
        with contextlib.suppress(Exception):
            self.sessions_file.parent.chmod(0o700)
        self.log = logger
        self._model_getter = model_getter
        self._default_name_getter = default_name_getter
        self._session_limit = session_limit
        self.sessions: dict[str, OASession] = {}
        self.active_session: dict[int, str] = {}
        self.session_prefs: dict[int, str] = {}
        self._save_lock: asyncio.Lock | None = None
        self._save_task: asyncio.Task[Any] | None = None
        self._save_generation = 0
        self._saved_generation = 0
        self._save_debounce_seconds = 0.4

    @property
    def _backup_file(self) -> Path:
        return self.sessions_file.with_suffix(self.sessions_file.suffix + ".bak")

    def _chmod_private_file(self, path: Path) -> None:
        with contextlib.suppress(Exception):
            if path.exists():
                path.chmod(0o600)

    def _write_private_bytes(self, path: Path, data: bytes) -> None:
        tmp_path: Path | None = None
        try:
            with tempfile.NamedTemporaryFile(
                "wb",
                dir=str(path.parent),
                prefix=f".{path.name}.",
                suffix=".tmp",
                delete=False,
            ) as tmp:
                tmp_path = Path(tmp.name)
                tmp.write(data)
            tmp_path.chmod(0o600)
            tmp_path.replace(path)
            self._chmod_private_file(path)
        finally:
            if tmp_path is not None and tmp_path.exists():
                with contextlib.suppress(Exception):
                    tmp_path.unlink()

    def _load_payload_sync(self) -> dict[str, Any] | None:
        """Read sessions JSON, falling back to the last known-good backup."""
        for path in (self.sessions_file, self._backup_file):
            if not path.exists():
                continue
            self._chmod_private_file(path)
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
                if isinstance(payload, dict):
                    if path != self.sessions_file:
                        self.log.warning("OpenAgent: restored sessions from backup")
                    return payload
            except Exception as exc:
                self.log.warning(f"OpenAgent: failed to read sessions file {path}: {exc}")
        return None

    async def _load_payload(self) -> dict[str, Any] | None:
        return await asyncio.to_thread(self._load_payload_sync)

    def _session_payload(self) -> dict[str, Any]:
        return {
            "sessions": [s.to_dict() for s in self.sessions.values()],
            "active": {str(k): v for k, v in self.active_session.items()},
            "prefs": {str(k): v for k, v in self.session_prefs.items()},
        }

    @staticmethod
    def _payload_list(value: Any) -> list[Any]:
        return value if isinstance(value, list) else []

    @staticmethod
    def _payload_dict(value: Any) -> dict[Any, Any]:
        return value if isinstance(value, dict) else {}

    @staticmethod
    def _json_bytes(data: dict[str, Any]) -> bytes:
        return json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode("utf-8") + b"\n"

    def _backup_current_sessions_file(self) -> None:
        if not self.sessions_file.exists():
            return
        current_payload = self.sessions_file.read_bytes()
        try:
            json.loads(current_payload.decode("utf-8"))
        except Exception:
            self.log.warning("OpenAgent: current sessions file is invalid, keeping previous backup")
        else:
            self._write_private_bytes(self._backup_file, current_payload)

    def _restore_sessions(self, raw_sessions: Any) -> None:
        for raw in self._payload_list(raw_sessions):
            if not isinstance(raw, dict):
                continue
            with contextlib.suppress(Exception):
                session = OASession.from_dict(raw)
                if session.id and session.chat_id:
                    self.sessions[session.id] = session

    def _restore_active_sessions(self, raw_active: Any) -> None:
        for chat_id_str, session_id in self._payload_dict(raw_active).items():
            with contextlib.suppress(Exception):
                cid = int(chat_id_str)
                if session_id in self.sessions:
                    self.active_session[cid] = session_id

    def _restore_preferences(self, raw_prefs: Any) -> None:
        for chat_id_str, pref in self._payload_dict(raw_prefs).items():
            with contextlib.suppress(Exception):
                if pref in _SESSION_PREFERENCES:
                    self.session_prefs[int(chat_id_str)] = pref

    def _repair_active_sessions(self) -> bool:
        repaired = False
        for session in sorted(self.sessions.values(), key=lambda item: item.updated_at, reverse=True):
            if session.chat_id and session.chat_id not in self.active_session:
                self.active_session[session.chat_id] = session.id
                repaired = True
        return repaired

    def _save_payload_sync(self, data: dict[str, Any]) -> None:
        self._backup_current_sessions_file()
        self._write_private_bytes(self.sessions_file, self._json_bytes(data))

    async def load(self) -> None:
        """Load persisted sessions without replacing public dict objects."""
        if not self.sessions_file.exists() and not self._backup_file.exists():
            return
        try:
            data = await self._load_payload()
            if not data:
                return
            self.sessions.clear()
            self.active_session.clear()
            self.session_prefs.clear()
            self._restore_sessions(data.get("sessions"))
            self._restore_active_sessions(data.get("active"))
            self._restore_preferences(data.get("prefs"))
            if self._repair_active_sessions():
                await self.save()
        except Exception as exc:
            self.log.warning(f"OpenAgent: failed to load sessions: {exc}")

    async def save(self) -> None:
        """Persist sessions to disk."""
        if self._save_lock is None:
            self._save_lock = asyncio.Lock()
        try:
            async with self._save_lock:
                await asyncio.to_thread(self._save_payload_sync, self._session_payload())
        except Exception as exc:
            self.log.warning(f"OpenAgent: failed to save sessions: {exc}")

    async def _scheduled_save(self) -> None:
        try:
            await asyncio.sleep(self._save_debounce_seconds)
            while self._saved_generation < self._save_generation:
                generation = self._save_generation
                await self.save()
                self._saved_generation = max(self._saved_generation, generation)
        finally:
            self._save_task = None
            if self._saved_generation < self._save_generation:
                self.schedule_save(mark_dirty=False)

    def schedule_save(self, *, mark_dirty: bool = True) -> None:
        if mark_dirty:
            self._save_generation += 1
        loop: asyncio.AbstractEventLoop | None = None
        with contextlib.suppress(RuntimeError):
            loop = asyncio.get_running_loop()
        if loop is None:
            with contextlib.suppress(RuntimeError):
                loop = asyncio.get_event_loop()
        if loop is None or loop.is_closed():
            return
        if self._save_task is not None and not self._save_task.done():
            return
        self._save_task = loop.create_task(self._scheduled_save())

    def new_session(self, chat_id: int, name: str | None = None) -> OASession:
        """Create a fresh session and make it active for chat_id."""
        session = OASession(
            id=str(uuid.uuid4()),
            name=name or self._default_name_getter(),
            chat_id=chat_id,
            created_at=time.time(),
            updated_at=time.time(),
            model=self._model_getter(),
        )
        self.sessions[session.id] = session
        self.active_session[chat_id] = session.id
        self.enforce_limit(chat_id)
        self.touch_session(session)
        return session

    def get_active_session(self, chat_id: int) -> OASession:
        """Return active session for chat_id, creating one if needed."""
        session_id = self.active_session.get(chat_id)
        if session_id and session_id in self.sessions:
            return self.sessions[session_id]
        existing = self.get_chat_sessions(chat_id)
        if existing:
            session = existing[0]
            self.active_session[chat_id] = session.id
            self.schedule_save()
            return session
        return self.new_session(chat_id)

    def get_fresh_session(self, chat_id: int, name: str | None = None) -> OASession:
        """Return an empty active session, or create a new one if current has history."""
        session = self.get_active_session(chat_id)
        if not session.messages:
            return session
        return self.new_session(chat_id, name)

    def get_chat_sessions(self, chat_id: int) -> list[OASession]:
        """Return all sessions for a chat, sorted newest-first."""
        return sorted(
            (s for s in self.sessions.values() if s.chat_id == chat_id),
            key=lambda s: s.updated_at,
            reverse=True,
        )

    def enforce_limit(self, chat_id: int) -> None:
        """Keep at most session_limit sessions per chat, pruning oldest."""
        chat_sessions = self.get_chat_sessions(chat_id)
        for session in chat_sessions[self._session_limit:]:
            self.sessions.pop(session.id, None)

    def touch_session(self, session: OASession) -> None:
        session.updated_at = time.time()
        session.model = session.model or self._model_getter()
        self.schedule_save()

    def set_active_session(self, chat_id: int, session_id: str) -> OASession | None:
        session = self.sessions.get(session_id)
        if session is None or session.chat_id != chat_id:
            return None
        self.active_session[chat_id] = session.id
        self.schedule_save()
        return session

    def set_preference(self, chat_id: int, pref: str) -> None:
        if pref not in _SESSION_PREFERENCES:
            return
        self.session_prefs[chat_id] = pref
        self.schedule_save()

__all__ = [
    'SessionManager',
    '_OpenAgentSessionsMixin',
    '_SESSION_PREFERENCES',
]
