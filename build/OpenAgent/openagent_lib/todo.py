from __future__ import annotations

import json
import html
import asyncio
import re

from typing import Any

_TODO_STATUS_ALIASES = {
    "open": "open",
    "active": "open",
    "todo": "open",
    "new": "open",
    "pending": "pending",
    "later": "pending",
    "wait": "pending",
    "backlog": "pending",
    "closed": "closed",
    "close": "closed",
    "done": "closed",
    "completed": "closed",
    "complete": "closed",
    "finished": "closed",
}

_DEFAULT_TODO_STATUS_MAP = {
    "pending": "...",
    "open": ">>>",
    "closed": "---",
}
_WHITESPACE_RE = re.compile(r"\s+")

class OpenAgentTodoService:
    """Pure TODO parsing/formatting logic, isolated from MCUB runtime."""

    def __init__(self) -> None:
        self._status_map_raw: str | None = None
        self._status_map_cache: dict[str, str] | None = None

    def parse_items_raw(self, raw: str | None) -> list[dict[str, str]]:
        raw_text = str(raw or "").strip()
        if not raw_text:
            return []
        try:
            parsed = json.loads(raw_text)
        except Exception:
            return []
        if not isinstance(parsed, list):
            return []
        return self.clean_items(parsed)

    def parse_html_text(self, text: str) -> str:
        value = html.unescape(str(text or "")).strip()
        value = _WHITESPACE_RE.sub(" ", value).strip()
        return value[:500]

    def normalize_status(self, status: str) -> str:
        status = (status or "").strip().lower()
        return _TODO_STATUS_ALIASES.get(status, "pending")

    def clean_items(self, items: list[dict[str, str]] | list[Any]) -> list[dict[str, str]]:
        cleaned: list[dict[str, str]] = []
        for item in items:
            if not isinstance(item, dict):
                continue
            text = self.parse_html_text(str(item.get("text", "") or ""))
            if not text:
                continue
            cleaned.append(
                {
                    "text": text[:500],
                    "status": self.normalize_status(str(item.get("status", "pending") or "pending")),
                }
            )
        return cleaned

    def status_map(self, raw: str | None) -> dict[str, str]:
        raw_text = str(raw or "")
        if raw_text == self._status_map_raw and isinstance(self._status_map_cache, dict):
            return dict(self._status_map_cache)
        mapping = dict(_DEFAULT_TODO_STATUS_MAP)
        for line in raw_text.splitlines():
            if "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = self.normalize_status(key.strip().lower())
            value = value.strip()
            if key and value:
                mapping[key] = value
        self._status_map_raw = raw_text
        self._status_map_cache = dict(mapping)
        return dict(mapping)

    def format_placeholder(self, items: list[dict[str, str]], raw_status_map: str | None = None) -> str:
        if not items:
            return "TODO empty"
        status_map = self.status_map(raw_status_map)
        return "\n".join(
            f"{status_map.get(item['status'], '...')} {item['text']}"
            for item in items
        )

    def target_index(
        self,
        items: list[dict[str, str]],
        attrs: dict[str, str],
        body: str,
        *,
        allow_body_text: bool = True,
    ) -> tuple[int | None, str]:
        target_raw = (
            attrs.get("index")
            or attrs.get("idx")
            or attrs.get("id")
            or attrs.get("number")
            or attrs.get("target")
            or attrs.get("item")
            or ""
        ).strip()
        body_raw = (body or "").strip()
        if not target_raw and body_raw and "\n" not in body_raw and "|" not in body_raw:
            target_raw = body_raw
        if not target_raw:
            return None, "todo index/text is required"
        if target_raw.isdigit():
            idx = int(target_raw) - 1
            if 0 <= idx < len(items):
                return idx, ""
            return None, f"todo index out of range: {target_raw}"
        if allow_body_text:
            needle = target_raw.lower()
            for idx, item in enumerate(items):
                if needle in item["text"].lower():
                    return idx, ""
        return None, "todo item not found"


class _OpenAgentTodoMixin:
    """TODO parsing, formatting and persistence helpers."""

    def _todo_service(self) -> OpenAgentTodoService:
        service = getattr(self, "_todo_service_instance", None)
        if not isinstance(service, OpenAgentTodoService):
            service = OpenAgentTodoService()
            self._todo_service_instance = service
        return service

    def _parse_todo_items_raw(self, raw: str | None) -> list[dict[str, str]]:
        return self._todo_service().parse_items_raw(raw)

    def _todo_parse_html_text(self, text: str) -> str:
        return self._todo_service().parse_html_text(text)

    def _todo_items(self) -> list[dict[str, str]]:
        cached = getattr(self, "_todo_items_cache", None)
        if isinstance(cached, list):
            return [dict(item) for item in cached if isinstance(item, dict)]
        return []

    async def _load_todo_items_storage(self) -> None:
        self._todo_items_cache = []

    def _todo_normalize_status(self, status: str) -> str:
        return self._todo_service().normalize_status(status)

    def _todo_status_map(self) -> dict[str, str]:
        raw = str(self.config.get("todo_status_emojis", "") or "")
        return self._todo_service().status_map(raw)

    def _format_todo_placeholder(self) -> str:
        raw = str(self.config.get("todo_status_emojis", "") or "")
        return self._todo_service().format_placeholder(self._todo_items(), raw)

    async def _save_todo_items(self, items: list[dict[str, str]]) -> list[dict[str, str]]:
        cleaned = self._todo_service().clean_items(items)
        self._todo_items_cache = cleaned
        await asyncio.sleep(0)
        return cleaned

    def _todo_target_index(
        self,
        items: list[dict[str, str]],
        attrs: dict[str, str],
        body: str,
        *,
        allow_body_text: bool = True,
    ) -> tuple[int | None, str]:
        return self._todo_service().target_index(
            items,
            attrs,
            body,
            allow_body_text=allow_body_text,
        )

__all__ = [
     'OpenAgentTodoService',
     '_OpenAgentTodoMixin',
     '_TODO_STATUS_ALIASES',
     '_DEFAULT_TODO_STATUS_MAP',
     '_WHITESPACE_RE',
]
