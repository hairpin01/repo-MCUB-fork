# scop: inline
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Any


class McubPlugin:
    name = "mcub"
    version = "0.2.0"
    author = "@dev_dolbaeb"
    description = "MCUB kernel command tools"

    tool_registry = (
        "mcub.command",
        "mcub.config",
        "mcub.modules",
        "mcub.install",
        "mcub.reload",
    )

    dangerous_tools = {"mcub.command", "mcub.install", "mcub.reload"}

    tool_docs = {
        "mcub.command": {"desc": "Execute any MCUB userbot command", "args": "command (str) or cmd (str) — command text (prefix auto-added)", "body": "command text"},
        "mcub.config": {"desc": "Get or set MCUB module configuration", "args": "command (str) or query (str) — config command like 'module.key=value'", "body": "config command"},
        "mcub.modules": {"desc": "List loaded MCUB modules", "args": "command (str) or query (str)", "body": "not used"},
        "mcub.install": {"desc": "Install a module from a repo URL", "args": "command (str) or query (str) — module URL or name", "body": "URL or name"},
        "mcub.reload": {"desc": "Reload all modules (equivalent to .restart)", "args": "none", "body": "not used"},
    }

    tool_map = {
        "mcub": "cmd_mcub",
        "mcub.command": "cmd_mcub",
        "mcub.config": "cmd_mcub",
        "mcub.modules": "cmd_mcub",
        "mcub.install": "cmd_mcub",
        "mcub.reload": "cmd_mcub",
    }

    def __init__(self, agent: Any) -> None:
        self.agent = agent
    
    async def cmd_mcub(self, tool_name: str, attrs_raw: str, body: str, source_event: Any) -> str:
        command_map = {
            "mcub.modules": "modules",
            "mcub.config": "cfg",
            "mcub.install": "dlm",
            "mcub.reload": "restart",
        }
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        command = (
            command_map.get(tool_name, "")
            or attrs.get("command")
            or attrs.get("cmd")
            or attrs.get("text")
            or attrs.get("query")
            or body.strip()
        )
        command = command.strip()
        if not command:
            return "Empty MCUB command"
        prefix = getattr(self.agent.kernel, "custom_prefix", ".") or "."
        if not command.startswith(prefix):
            command = prefix + command
        
        cmd_name = command[len(prefix):].split(maxsplit=1)[0].lower()
        if cmd_name in {"oa", "agent"}:
            return "Blocked recursive OpenAgent command"
        
        event = self.agent._MCUBEvent(self.agent, source_event, command)
        try:
            handled = await self.agent.kernel.process_command(event)
        except Exception as exc:
            await self.agent.kernel.handle_error(exc, source="OpenAgent:mcub", event=source_event)
            return f"MCUB command failed: {exc}"
        output = event.output or f"Command handled: {handled}"
        return output[-6000:]
