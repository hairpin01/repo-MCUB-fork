# scop: inline
# SPDX-License-Identifier: MIT

from __future__ import annotations

import asyncio
import contextlib
import html
import io
import json
import re
import textwrap
import time
from pathlib import Path
from typing import Any
from contextlib import redirect_stdout, redirect_stderr

import aiohttp


class EvalPlugin:
    name = "eval"
    version = "0.1.0"
    author = "@dev_dolbaeb"
    description = "Async Python eval tool for OpenAgent runtime debugging"

    tool_registry = (
        "eval.python",
    )

    dangerous_tools = {"eval.python", "eval"}

    tool_docs = {
        "eval.python": {
            "desc": "Execute Python code inside an async function with OpenAgent runtime objects available",
            "args": "code (str) or expr (str); timeout (int)",
            "body": "Python code. You may use await and return from the async function.",
        },
    }

    tool_map = {
        "eval": "cmd_eval",
        "eval.python": "cmd_eval",
    }

    config_defaults = {
        "eval_timeout": 30,
    }

    def __init__(self, agent: Any) -> None:
        self.agent = agent

    def _trim(self, text: str, limit: int = 12000) -> str:
        text = str(text or "")
        if len(text) <= limit:
            return text
        return text[:limit] + "\n...[truncated]"

    async def cmd_eval(self, attrs_raw: str, body: str, source_event: Any | None = None) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        code = attrs.get("code") or body
        expr = attrs.get("expr") or attrs.get("expression")
        if expr and not str(code or "").strip():
            code = f"return {expr}"
        code = textwrap.dedent(str(code or "")).strip("\n")
        if not code.strip():
            return "Python code is required in body or code/expr attr"

        timeout = int(attrs.get("timeout") or self.agent.config.get("eval_timeout", 30) or 30)
        timeout = max(1, min(timeout, 120))

        reply = None
        if source_event is not None and hasattr(source_event, "get_reply_message"):
            with contextlib.suppress(Exception):
                reply = await source_event.get_reply_message()

        stdout = io.StringIO()
        stderr = io.StringIO()
        env: dict[str, Any] = {
            "self": self.agent,
            "agent": self.agent,
            "plugin": self,
            "client": getattr(self.agent, "client", None),
            "kernel": getattr(self.agent, "kernel", None),
            "db": getattr(self.agent, "db", None),
            "cache": getattr(self.agent, "cache", None),
            "config": getattr(self.agent, "config", None),
            "event": source_event,
            "source_event": source_event,
            "reply": reply,
            "chat_id": getattr(source_event, "chat_id", None) if source_event is not None else None,
            "sender_id": getattr(source_event, "sender_id", None) if source_event is not None else None,
            "asyncio": asyncio,
            "aiohttp": aiohttp,
            "Path": Path,
            "json": json,
            "re": re,
            "time": time,
            "html": html,
            "contextlib": contextlib,
        }
        function_source = "async def __openagent_eval__():\n" + textwrap.indent(code, "    ")
        local_env: dict[str, Any] = {}
        try:
            exec(compile(function_source, "<openagent-eval>", "exec"), env, local_env)
            func = local_env["__openagent_eval__"]
            with redirect_stdout(stdout), redirect_stderr(stderr):
                result = await asyncio.wait_for(func(), timeout=timeout)
        except Exception as exc:
            out = stdout.getvalue().strip()
            err = stderr.getvalue().strip()
            parts = [f"Eval failed: {type(exc).__name__}: {exc}"]
            if out:
                parts.append("stdout:\n" + self._trim(out))
            if err:
                parts.append("stderr:\n" + self._trim(err))
            return "\n\n".join(parts)

        out = stdout.getvalue().strip()
        err = stderr.getvalue().strip()
        parts = []
        if result is not None:
            parts.append("result:\n" + self._trim(repr(result)))
        if out:
            parts.append("stdout:\n" + self._trim(out))
        if err:
            parts.append("stderr:\n" + self._trim(err))
        return "\n\n".join(parts) if parts else "Eval completed with no output"
