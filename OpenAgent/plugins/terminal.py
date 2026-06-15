# scop: inline
# SPDX-License-Identifier: MIT

from __future__ import annotations

import asyncio
import re
from typing import Any


class TerminalPlugin:
    name = "terminal"
    version = "0.2.0"
    author = "@dev_dolbaeb"
    description = "CLI shell and file system tools"

    tool_registry = (
        "terminal.run",
        "terminal.inspect",
        "terminal.list_files",
        "terminal.read_file",
        "terminal.git_status",
    )

    tool_map = {
        "terminal": "cmd_run",
        "terminal.run": "cmd_run",
        "terminal.inspect": "cmd_inspect",
        "terminal.list_files": "cmd_list_files",
        "terminal.read_file": "cmd_read_file",
        "terminal.git_status": "cmd_git_status",
    }

    dangerous_tools = {"terminal.run", "terminal.inspect"}

    tool_docs = {
        "terminal.run": {"desc": "Run any shell command on the server", "args": "command (str) or cmd (str) — shell command to execute", "body": "command text"},
        "terminal.inspect": {"desc": "Run an arbitrary shell command to inspect system state", "args": "command (str) or cmd (str) — command to run", "body": "command text"},
        "terminal.list_files": {"desc": "List files and directories in a folder", "args": "path (str) — directory path (default: .)", "body": "path text"},
        "terminal.read_file": {"desc": "Read a file (UTF-8, first 12k chars)", "args": "path (str) or file (str) — file to read", "body": "path text"},
        "terminal.git_status": {"desc": "Show git status of the workspace", "args": "none", "body": "not used"},
    }

    config_defaults = {
        "terminal_enabled": True,
        "terminal_steps": 3,
        "terminal_timeout": 30,
    }

    def __init__(self, agent: Any) -> None:
        self._agent = agent

    @property
    def agent(self) -> Any:
        return self._agent

    async def on_load(self) -> None:
        pass

    async def cmd_run(self, command: str) -> str:
        proc = await asyncio.create_subprocess_shell(
            command,
            cwd=self.agent._workspace_dir(),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        try:
            stdout, stderr = await asyncio.wait_for(
                proc.communicate(), timeout=int(self.agent.config["terminal_timeout"])
            )
        except asyncio.TimeoutError:
            proc.kill()
            await proc.communicate()
            return f"Command timed out after {self.agent.config['terminal_timeout']}s"

        out = stdout.decode("utf-8", errors="replace")
        err = stderr.decode("utf-8", errors="replace")
        result = f"exit_code={proc.returncode}\n"
        if out:
            result += f"stdout:\n{out}\n"
        if err:
            result += f"stderr:\n{err}\n"
        return result[-6000:]

    async def cmd_inspect(self, tool_name: str, attrs_raw: str, body: str) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        command = body.strip() or attrs.get("command") or attrs.get("cmd") or "pwd"
        return await self.cmd_run(command)

    async def cmd_list_files(self, tool_name: str, attrs_raw: str, body: str) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        path = attrs.get("path") or body.strip() or "."
        return await self.cmd_run(
            f"python - <<'PY'\nfrom pathlib import Path\np=Path({path!r})\nprint('\\n'.join(sorted(x.name + ('/' if x.is_dir() else '') for x in p.iterdir())))\nPY"
        )

    async def cmd_read_file(self, tool_name: str, attrs_raw: str, body: str) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        path = attrs.get("path") or attrs.get("file") or body.strip()
        if not path:
            return "path is required"
        return await self.cmd_run(
            f"python - <<'PY'\nfrom pathlib import Path\np=Path({path!r})\nprint(p.read_text(encoding='utf-8', errors='replace')[:12000])\nPY"
        )

    async def cmd_git_status(self, tool_name: str, attrs_raw: str, body: str) -> str:
        return await self.cmd_run("git status --short")
