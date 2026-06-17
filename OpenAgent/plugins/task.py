# scop: inline
# SPDX-License-Identifier: MIT

from __future__ import annotations

import html
import json
from typing import Any


class TaskPlugin:
    name = "task"
    version = "0.1.0"
    author = "@dev_dolbaeb"
    description = "Run OpenAgent tools in background and report completion as a live comment"

    tool_registry = (
        "task.background",
        "task.run_background",
    )

    tool_docs = {
        "task.background": {
            "desc": "Start another OpenAgent tool in background. When it finishes, a live user.comment is queued for the current run.",
            "args": "tool/name (str) — tool to run; attrs (str) — inner attrs; label (str)",
            "body": "body for the inner tool",
        },
        "task.run_background": {
            "desc": "Alias of task.background",
            "args": "tool/name (str); attrs (str); label (str)",
            "body": "body for the inner tool",
        },
    }

    tool_map = {
        "task.background": "cmd_background",
        "task.run_background": "cmd_background",
    }

    config_defaults = {
        "task_background_enabled": True,
        "task_background_max": 5,
    }

    def __init__(self, agent: Any) -> None:
        self.agent = agent

    def _attrs_to_raw(self, attrs: dict[str, Any]) -> str:
        parts = []
        for key, value in attrs.items():
            if value is None or isinstance(value, (dict, list)):
                continue
            clean_key = str(key).strip().lower()
            if not clean_key:
                continue
            clean_value = html.escape(str(value), quote=True)
            parts.append(f'{clean_key}="{clean_value}"')
        return " ".join(parts)

    def _json_payload(self, body: str) -> dict[str, Any] | None:
        text = (body or "").strip()
        if not text.startswith("{"):
            return None
        try:
            payload = json.loads(text)
        except Exception:
            return None
        return payload if isinstance(payload, dict) else None

    async def cmd_background(
        self,
        attrs_raw: str,
        body: str,
        source_event: Any | None = None,
        status_event: Any | None = None,
        runtime_token: str | None = None,
    ) -> str:
        if not bool(self.agent.config.get("task_background_enabled", True)):
            return "Background tasks are disabled by config."

        max_tasks = int(self.agent.config.get("task_background_max", 5) or 5)
        active_tasks = len(getattr(self.agent, "_background_tool_tasks", {}) or {})
        if active_tasks >= max_tasks:
            return f"Background task limit reached: {active_tasks}/{max_tasks}."

        attrs = self.agent._parse_xml_attrs(attrs_raw)
        payload = self._json_payload(body)
        tool_name = (attrs.get("tool") or attrs.get("name") or attrs.get("target") or "").strip().lower()
        if payload:
            tool_name = (str(payload.get("tool") or payload.get("name") or payload.get("target") or tool_name)).strip().lower()
        if not tool_name:
            return "tool/name attribute is required, e.g. <tool_call name=\"task.background\" tool=\"web.fetch\">...</tool_call>"

        inner_attrs = attrs.get("attrs") or attrs.get("tool_attrs") or ""
        inner_body = body
        if payload:
            raw_args = payload.get("args") or payload.get("attrs") or {}
            if isinstance(raw_args, dict):
                inner_attrs = " ".join(filter(None, [inner_attrs, self._attrs_to_raw(raw_args)]))
            elif raw_args and not inner_attrs:
                inner_attrs = str(raw_args)
            for key in ("body", "content", "text", "message", "command", "cmd", "query"):
                if key in payload and not isinstance(payload.get(key), (dict, list)):
                    inner_body = str(payload.get(key) or "")
                    break
            else:
                if isinstance(raw_args, dict):
                    for key in ("body", "content", "text", "message", "command", "cmd", "query"):
                        if key in raw_args and not isinstance(raw_args.get(key), (dict, list)):
                            inner_body = str(raw_args.get(key) or "")
                            break
        label = attrs.get("label") or attrs.get("title") or tool_name
        try:
            task_id = self.agent.create_background_tool_task(
                tool_name=tool_name,
                attrs_raw=inner_attrs,
                body=inner_body,
                source_event=source_event,
                status_event=status_event,
                runtime_token=runtime_token,
                label=label,
            )
        except Exception as exc:
            return f"Failed to start background task: {type(exc).__name__}: {exc}"

        return (
            f"Started background task {task_id} for tool <{tool_name}>. "
            "Continue the current work; when the task finishes, it will be delivered as user.comment."
        )
