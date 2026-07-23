from __future__ import annotations
"""Plain service for OpenAgent chat sessions and persistence."""

from typing import (
    Any,
    Callable,
)
import asyncio
import contextlib
from pathlib import Path
import tempfile
import json
import time
import uuid

from .oasession import OASession
_SESSION_PREFERENCES = frozenset({"ask", "continue", "new"})

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
    '_SESSION_PREFERENCES',
]
