# SPDX-License-Identifier: MIT
"""AST-grep tools executed only through bounded process capabilities."""
from __future__ import annotations

from typing import Any, Callable, Mapping

from OpenAgentLib.PluginSDK import CapabilityClient, PluginManifest
from OpenAgentLib.ToolKernel import ToolCall

from ._resource_v2 import bounded_text, declaration, grant_relative_path, required_text, response_data


_AST_GREP = "ast-grep"
_MAX_PATTERN_LENGTH = 8_192
_MAX_GLOBS = 32
_MAX_GLOB_LENGTH = 256
_TIMEOUT_SECONDS = 30
_MAX_OUTPUT_BYTES = 24_000
_LANGUAGES = [
    "bash", "c", "cpp", "csharp", "css", "go", "html", "java", "javascript", "json", "kotlin",
    "php", "python", "ruby", "rust", "swift", "tsx", "typescript", "yaml",
]

_SEARCH_SCHEMA = {
    "type": "object",
    "properties": {
        "pattern": {"type": "string"}, "lang": {"type": "string", "enum": _LANGUAGES},
        "path": {"type": "string"}, "globs": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["pattern", "lang", "path"],
    "additionalProperties": False,
}
_REPLACE_SCHEMA = {
    "type": "object",
    "properties": {
        "pattern": {"type": "string"}, "rewrite": {"type": "string"},
        "lang": {"type": "string", "enum": _LANGUAGES}, "path": {"type": "string"},
        "globs": {"type": "array", "items": {"type": "string"}}, "apply": {"type": "boolean"},
    },
    "required": ["pattern", "rewrite", "lang", "path"],
    "additionalProperties": False,
}
_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "ok": {"type": "boolean"}, "exit_code": {"type": "integer"}, "result": {"type": "string"},
        "truncated": {"type": "boolean"}, "applied": {"type": "boolean"},
    },
    "required": ["ok", "exit_code", "result", "truncated", "applied"],
    "additionalProperties": False,
}


def _bounded_string(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value or len(value) > _MAX_PATTERN_LENGTH or "\x00" in value:
        raise ValueError(f"{field} must be bounded non-empty text")
    return value


def _globs(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, (list, tuple)) or len(value) > _MAX_GLOBS:
        raise ValueError("globs must be a bounded string array")
    if any(
        not isinstance(glob, str)
        or not glob
        or len(glob) > _MAX_GLOB_LENGTH
        or "\x00" in glob
        or glob.startswith("/")
        or "\\" in glob
        or ".." in glob.split("/")
        for glob in value
    ):
        raise ValueError("glob must be bounded non-empty text")
    return tuple(value)


def _argv(arguments: Mapping[str, Any], *, rewrite: bool) -> tuple[str, ...]:
    pattern = _bounded_string(arguments["pattern"], "pattern")
    path = grant_relative_path(arguments["path"])
    argv: list[str] = [_AST_GREP, "run", "--pattern", pattern, "--lang", arguments["lang"], "--json=compact"]
    for glob in _globs(arguments.get("globs")):
        argv.extend(("--globs", glob))
    if rewrite:
        argv.extend(("--rewrite", _bounded_string(arguments["rewrite"], "rewrite")))
        if arguments.get("apply", False):
            argv.append("--update-all")
    argv.append(path)
    return tuple(argv)


def _result(response: Mapping[str, Any], *, applied: bool) -> Mapping[str, Any]:
    data = response_data(response)
    exit_code = data.get("exit_code")
    if not isinstance(exit_code, int) or isinstance(exit_code, bool):
        raise ValueError("process response exit_code must be an integer")
    stdout, stdout_truncated = bounded_text(required_text(data, "stdout"), _MAX_OUTPUT_BYTES)
    stderr, stderr_truncated = bounded_text(required_text(data, "stderr"), _MAX_OUTPUT_BYTES)
    result = stdout if stdout else stderr
    return {
        "ok": True,
        "exit_code": exit_code,
        "result": result,
        "truncated": bool(data.get("truncated", False) or stdout_truncated or stderr_truncated),
        "applied": applied,
    }


def _search(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    response = capability.process(
        _argv(call.arguments, rewrite=False),
        f"{call.call_id}:ast-grep.search",
        cwd=".",
        timeout_seconds=_TIMEOUT_SECONDS,
        max_output_bytes=_MAX_OUTPUT_BYTES,
    )
    return _result(response, applied=False)


def _replace(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    applied = bool(call.arguments.get("apply", False))
    response = capability.process(
        _argv(call.arguments, rewrite=True),
        f"{call.call_id}:ast-grep.replace",
        cwd=".",
        timeout_seconds=_TIMEOUT_SECONDS,
        max_output_bytes=_MAX_OUTPUT_BYTES,
    )
    return _result(response, applied=applied)


_TOOLS = (
    declaration("ast_grep.search", _SEARCH_SCHEMA, _OUTPUT_SCHEMA, "Search a granted workspace with exact ast-grep argv."),
    declaration("ast_grep.replace", _REPLACE_SCHEMA, _OUTPUT_SCHEMA, "Rewrite a granted workspace with exact ast-grep argv."),
)
MANIFEST = PluginManifest(
    plugin_id="openagent.ast_grep",
    version="2.0.0",
    api_version="2",
    entrypoint="plugins.ast_grep.HANDLERS",
    tools=_TOOLS,
    capabilities=frozenset({capability for tool in _TOOLS for capability in tool.capabilities}),
)
HANDLERS: Mapping[str, Callable[[ToolCall, CapabilityClient], Mapping[str, Any]]] = {
    "ast_grep.search": _search,
    "ast_grep.replace": _replace,
}
PLUGIN_MANIFEST = MANIFEST
TOOL_HANDLERS = HANDLERS
