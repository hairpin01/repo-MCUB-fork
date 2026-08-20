# SPDX-License-Identifier: MIT
"""Least-privilege terminal and workspace inspection tools."""
from __future__ import annotations

from typing import Any, Callable, Mapping

from OpenAgentLib.PluginSDK import CapabilityClient, PluginManifest
from OpenAgentLib.ToolKernel import ToolCall

from ._resource_v2 import bounded_text, declaration, grant_relative_path, required_text, response_data


_MAX_ARGUMENTS = 32
_MAX_ARGUMENT_LENGTH = 4_096
_TIMEOUT_SECONDS = 30
_MAX_OUTPUT_BYTES = 12_000
_ALLOWED_EXECUTABLES = frozenset({
    "cat", "echo", "grep", "head", "ls", "pwd", "tail", "wc",
})

_EMPTY_SCHEMA = {"type": "object", "properties": {}, "additionalProperties": False}
_PATH_SCHEMA = {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"], "additionalProperties": False}
_RUN_SCHEMA = {
    "type": "object",
    "properties": {"argv": {"type": "array", "items": {"type": "string"}}, "cwd": {"type": "string"}},
    "required": ["argv", "cwd"],
    "additionalProperties": False,
}
_INSPECT_SCHEMA = {
    "type": "object",
    "properties": {
        "operation": {"type": "string", "enum": ["git-status", "git-diff-stat"]},
        "cwd": {"type": "string"},
    },
    "required": ["operation", "cwd"],
    "additionalProperties": False,
}
_PROCESS_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "ok": {"type": "boolean"}, "exit_code": {"type": "integer"},
        "stdout": {"type": "string"}, "stderr": {"type": "string"}, "truncated": {"type": "boolean"},
    },
    "required": ["ok", "exit_code", "stdout", "stderr", "truncated"],
    "additionalProperties": False,
}
_READ_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {"ok": {"type": "boolean"}, "content": {"type": "string"}, "truncated": {"type": "boolean"}},
    "required": ["ok", "content", "truncated"],
    "additionalProperties": False,
}
_LIST_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {"ok": {"type": "boolean"}, "entries": {"type": "array", "items": {"type": "string"}}},
    "required": ["ok", "entries"],
    "additionalProperties": False,
}


def _bounded_argv(value: Any) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)) or not value or len(value) > _MAX_ARGUMENTS:
        raise ValueError("argv must contain between one and 32 arguments")
    if any(not isinstance(arg, str) or not arg or len(arg) > _MAX_ARGUMENT_LENGTH or "\x00" in arg for arg in value):
        raise ValueError("argv contains an invalid argument")
    argv = tuple(value)
    if argv[0] not in _ALLOWED_EXECUTABLES:
        raise ValueError("executable is not allowlisted")
    executable, arguments = argv[0], argv[1:]
    if executable == "echo":
        return argv
    if executable == "pwd":
        if arguments:
            raise ValueError("pwd does not accept arguments")
        return argv
    if executable == "ls":
        return ("ls", "--", *(grant_relative_path(path, allow_root=True, field="argv path") for path in arguments))
    if executable == "grep":
        if len(arguments) < 2:
            raise ValueError("grep requires a pattern and at least one grant-relative path")
        pattern, *paths = arguments
        return ("grep", "--", pattern, *(grant_relative_path(path, allow_root=True, field="argv path") for path in paths))
    if not arguments:
        raise ValueError(f"{executable} requires at least one grant-relative path")
    return (executable, "--", *(grant_relative_path(path, allow_root=True, field="argv path") for path in arguments))


def _process_result(response: Mapping[str, Any]) -> Mapping[str, Any]:
    data = response_data(response)
    stdout, stdout_truncated = bounded_text(required_text(data, "stdout"))
    stderr, stderr_truncated = bounded_text(required_text(data, "stderr"))
    exit_code = data.get("exit_code")
    if not isinstance(exit_code, int) or isinstance(exit_code, bool):
        raise ValueError("process response exit_code must be an integer")
    return {
        "ok": True,
        "exit_code": exit_code,
        "stdout": stdout,
        "stderr": stderr,
        "truncated": bool(data.get("truncated", False) or stdout_truncated or stderr_truncated),
    }


def _run(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    argv = _bounded_argv(call.arguments["argv"])
    cwd = grant_relative_path(call.arguments["cwd"], allow_root=True, field="cwd")
    response = capability.process(
        argv,
        f"{call.call_id}:terminal.run",
        cwd=cwd,
        timeout_seconds=_TIMEOUT_SECONDS,
        max_output_bytes=_MAX_OUTPUT_BYTES,
    )
    return _process_result(response)


def _inspect(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    cwd = grant_relative_path(call.arguments["cwd"], allow_root=True, field="cwd")
    argv = ("git", "status", "--short") if call.arguments["operation"] == "git-status" else ("git", "diff", "--stat")
    response = capability.process(
        argv,
        f"{call.call_id}:terminal.inspect",
        cwd=cwd,
        timeout_seconds=_TIMEOUT_SECONDS,
        max_output_bytes=_MAX_OUTPUT_BYTES,
    )
    return _process_result(response)


def _list_files(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    path = grant_relative_path(call.arguments["path"], allow_root=True)
    data = response_data(capability.filesystem("list", path, f"{call.call_id}:terminal.list"))
    entries = data.get("entries", ())
    if not isinstance(entries, (list, tuple)) or len(entries) > 2_000 or any(not isinstance(entry, str) for entry in entries):
        raise ValueError("filesystem list response is invalid")
    return {"ok": True, "entries": list(entries)}


def _read_file(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    path = grant_relative_path(call.arguments["path"])
    data = response_data(capability.filesystem("read", path, f"{call.call_id}:terminal.read"))
    content, truncated = bounded_text(data.get("content", ""))
    return {"ok": True, "content": content, "truncated": bool(data.get("truncated", False) or truncated)}


def _git_status(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    response = capability.process(
        ("git", "status", "--short"),
        f"{call.call_id}:terminal.git-status",
        cwd=".",
        timeout_seconds=_TIMEOUT_SECONDS,
        max_output_bytes=_MAX_OUTPUT_BYTES,
    )
    return _process_result(response)


_TOOLS = (
    declaration("terminal.run", _RUN_SCHEMA, _PROCESS_OUTPUT_SCHEMA, "Run a bounded argv command in the granted workspace."),
    declaration("terminal.inspect", _INSPECT_SCHEMA, _PROCESS_OUTPUT_SCHEMA, "Inspect granted Git metadata without arbitrary commands."),
    declaration("terminal.list_files", _PATH_SCHEMA, _LIST_OUTPUT_SCHEMA, "List a granted workspace directory."),
    declaration("terminal.read_file", _PATH_SCHEMA, _READ_OUTPUT_SCHEMA, "Read a granted workspace file."),
    declaration("terminal.git_status", _EMPTY_SCHEMA, _PROCESS_OUTPUT_SCHEMA, "Show granted workspace Git status."),
)
MANIFEST = PluginManifest(
    plugin_id="openagent.terminal",
    version="2.0.0",
    api_version="2",
    entrypoint="plugins.terminal.HANDLERS",
    tools=_TOOLS,
    capabilities=frozenset({capability for tool in _TOOLS for capability in tool.capabilities}),
)
HANDLERS: Mapping[str, Callable[[ToolCall, CapabilityClient], Mapping[str, Any]]] = {
    "terminal.run": _run,
    "terminal.inspect": _inspect,
    "terminal.list_files": _list_files,
    "terminal.read_file": _read_file,
    "terminal.git_status": _git_status,
}
PLUGIN_MANIFEST = MANIFEST
TOOL_HANDLERS = HANDLERS
