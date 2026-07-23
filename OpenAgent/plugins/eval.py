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

import core.lib.loader.module_base as loader
import core.lib.loader.module_config as mod_cfg
import utils

import aiohttp


class EvalPlugin:
    name = "eval"
    version = "0.1.0"
    author = "@dev_dolbaeb"
    description = "Async Python eval tool for OpenAgent runtime debugging"

    tool_registry = (
        "eval.python",
        "eval.python.telegram.help",
    )

    dangerous_tools = {"eval.python", "eval", "eval.python.telegram"}

    tool_docs = {
        "eval.python": {
            "desc": "Execute Python code inside an async function with OpenAgent runtime objects available and client/event/loader etc...",
            "args": "code (str) or expr (str); timeout (int)",
            "body": "Python code. You may use await and return from the async function.",
            "returns": "Confirmation text with the performed action details, or an error message.",
            "example": "{\"tool\": \"eval.python\", \"body\": \"return 2 + 2\"}",
            "notes": "Debug-only runtime execution; use only for trusted code.",
        },
    }

    tool_map = {
        "eval": "cmd_eval",
        "eval.python": "cmd_eval",
        "eval.python.telegram": 'cmd_eval',
        "eval.python.telegram.help": 'cmd_help',
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

    async def cmd_help(self):
        return """
inline:
The first important thing to know: inline buttons mean that sending (EXACTLY SENDING) is done via `self.inline()`:
```python
await self.inline(event.chat_id, 'text', reply_to=getattr(reply, 'id', None), buttons=None)
```
peer, text form, reply_to=None, buttons=None, parse_mode='html', file: str = None (link to file), photo: str = None (link to photo)
buttons: these are the buttons; they can be made in any way, but the best and most universally suitable one is:
```python
# loader already available, and it's core.lib.loader.module_base
@loader.callback()
async def on_click(self, call, data=None) -> None:
   await call.answer('test')

ok, message = await self.inline(event.chat_id, 'success', buttons=[[self.Button.inline('text', on_click)]]
```
More details in doc/inline/inline-form.md|doc/inline/*.md

client:
```python
await self.client(Any_request)
# client from telethon-mkub, almost the same as in regular telethon, import:
import telethon
return telethon.__version__
```
```python
m = await self.client.send_message(
    event.chat_id,
    '<b>text</b>',
    reply_to=getattr(event, 'reply_to', None),
    parse_mode='html',
    file='path/to/file/or/url',
)
await m.edit('NEW text!')
await m.delete()
# DO NOT DELETE `event`!

from telethon import events
from core.lib.utils.exceptions import CallInsecure
try:
    @self.client.on(events.Raw) # blocked from ClientProxy!
    async def deny_watcher(event):
        pass
except CallInsecure as e:
    return e
# GOOD:
@loader.watcher()
async def good_watcher(self, event) -> None:
    self.log.info(event)
```
doc: doc/api/*.md|API_DOC.md
utils:
```python
# invoke - run mcub command:
await self.invoke('cmd', chat_id=event.chat_id, reply_to=None, args='args') # run '.cmd args'
```
"""

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
            "loader": loader,
            "mod_cfg": mod_cfg,
            "utils": utils,
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
