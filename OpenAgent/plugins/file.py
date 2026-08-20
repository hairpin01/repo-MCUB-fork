# SPDX-License-Identifier: MIT
"""Opaque Telegram media plus guarded workspace file operations."""
from __future__ import annotations

import re
from typing import Any, Callable, Mapping

from OpenAgentLib.PluginSDK import CapabilityClient, PluginManifest
from OpenAgentLib.ToolKernel import ToolCall

from ._resource_v2 import declaration, grant_relative_path, required_text, response_data
from ._telegram_v2 import build_plugin


_MAX_CONTENT_BYTES = 262_144
_MAX_REPLACEMENTS = 10_000
_HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@(?: .*|)$")

_READ_SCHEMA = {
    "type": "object",
    "properties": {"path": {"type": "string"}},
    "required": ["path"],
    "additionalProperties": False,
}
_WRITE_SCHEMA = {
    "type": "object",
    "properties": {
        "path": {"type": "string"}, "content": {"type": "string"},
        "mode": {"type": "string", "enum": ["overwrite", "append"]},
    },
    "required": ["path", "content"],
    "additionalProperties": False,
}
_EDIT_SCHEMA = {
    "type": "object",
    "properties": {
        "path": {"type": "string"}, "search": {"type": "string"}, "replace": {"type": "string"},
        "count": {"type": "integer"},
    },
    "required": ["path", "search", "replace"],
    "additionalProperties": False,
}
_PATCH_SCHEMA = {
    "type": "object",
    "properties": {"path": {"type": "string"}, "patch": {"type": "string"}, "reverse": {"type": "boolean"}},
    "required": ["path", "patch"],
    "additionalProperties": False,
}
_READ_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {"ok": {"type": "boolean"}, "content": {"type": "string"}, "version": {"type": "string"}},
    "required": ["ok", "content", "version"],
    "additionalProperties": False,
}
_WRITE_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "ok": {"type": "boolean"}, "path": {"type": "string"}, "changed": {"type": "boolean"},
        "version": {"type": "string"},
    },
    "required": ["ok", "path", "changed", "version"],
    "additionalProperties": False,
}


def _bounded_content(value: Any, field: str) -> str:
    if not isinstance(value, str) or len(value.encode("utf-8", errors="replace")) > _MAX_CONTENT_BYTES:
        raise ValueError(f"{field} must be bounded text")
    return value


def _read_with_version(capability: CapabilityClient, path: str, request_id: str) -> tuple[str, str]:
    data = response_data(capability.filesystem("read", path, request_id))
    content = required_text(data, "content", limit=_MAX_CONTENT_BYTES)
    version = data.get("version", data.get("hash"))
    if not isinstance(version, str) or not version:
        raise ValueError("filesystem read response requires an opaque version")
    return content, version


def _write(
    capability: CapabilityClient,
    path: str,
    content: str,
    request_id: str,
    *,
    mode: str,
    expected_hash: str | None = None,
) -> tuple[str, bool]:
    response = capability.filesystem(
        "write",
        path,
        request_id,
        content=content,
        mode=mode,
        **({"expected_hash": expected_hash} if expected_hash is not None else {}),
    )
    data = response_data(response)
    version = data.get("version", data.get("hash"))
    if not isinstance(version, str) or not version:
        raise ValueError("filesystem write response version is invalid")
    changed = data.get("changed", True)
    if not isinstance(changed, bool):
        raise ValueError("filesystem write response changed is invalid")
    return version, changed


def _read_text(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    path = grant_relative_path(call.arguments["path"])
    content, version = _read_with_version(capability, path, f"{call.call_id}:file.read")
    return {"ok": True, "content": content, "version": version}


def _write_text(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    path = grant_relative_path(call.arguments["path"])
    content = _bounded_content(call.arguments["content"], "content")
    mode = call.arguments.get("mode", "overwrite")
    version, changed = _write(capability, path, content, f"{call.call_id}:file.write", mode=mode)
    return {"ok": True, "path": path, "changed": changed, "version": version}


def _edit(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    path = grant_relative_path(call.arguments["path"])
    search = _bounded_content(call.arguments["search"], "search")
    replacement = _bounded_content(call.arguments["replace"], "replace")
    if not search:
        raise ValueError("search must not be empty")
    count = call.arguments.get("count", -1)
    if not isinstance(count, int) or isinstance(count, bool) or count < -1 or count > _MAX_REPLACEMENTS:
        raise ValueError("count must be between -1 and 10000")
    content, version = _read_with_version(capability, path, f"{call.call_id}:file.edit.read")
    updated = content.replace(search, replacement, count)
    if updated == content:
        return {"ok": True, "path": path, "changed": False, "version": version}
    next_version, _changed = _write(
        capability,
        path,
        updated,
        f"{call.call_id}:file.edit.write",
        mode="overwrite",
        expected_hash=version,
    )
    return {"ok": True, "path": path, "changed": True, "version": next_version}


def _patch_path(header: str, prefix: str, path: str) -> None:
    if not header.startswith(prefix):
        raise ValueError("patch is missing a unified diff header")
    raw = header[len(prefix):].split("\t", 1)[0].strip()
    if raw.startswith(("a/", "b/")):
        raw = raw[2:]
    if grant_relative_path(raw) != path:
        raise ValueError("patch header path does not match requested path")


def _validate_patch_headers(patch: str, path: str) -> list[str]:
    if len(patch.encode("utf-8", errors="replace")) > _MAX_CONTENT_BYTES:
        raise ValueError("patch must be bounded text")
    rows = patch.splitlines(keepends=True)
    if len(rows) < 3:
        raise ValueError("patch must contain unified diff headers and hunks")
    _patch_path(rows[0], "--- ", path)
    _patch_path(rows[1], "+++ ", path)
    return rows


def _apply_patch(content: str, patch: str, path: str, *, reverse: bool) -> str:
    rows = _validate_patch_headers(patch, path)
    source_marker, target_marker = (("+", "-") if reverse else ("-", "+"))
    source_start_index, source_count_index = ((3, 4) if reverse else (1, 2))
    source = content.splitlines(keepends=True)
    output: list[str] = []
    position = 0
    index = 2
    hunk_count = 0
    while index < len(rows):
        match = _HUNK.match(rows[index].rstrip("\n"))
        if match is None:
            raise ValueError("patch contains an invalid hunk header")
        hunk_count += 1
        if hunk_count > 1_000:
            raise ValueError("patch has too many hunks")
        source_start = int(match.group(source_start_index))
        source_count = int(match.group(source_count_index) or "1")
        start = source_start - 1
        if start < position or start > len(source):
            raise ValueError("patch hunk lies outside the source file")
        output.extend(source[position:start])
        position = start
        index += 1
        consumed = 0
        while index < len(rows) and not rows[index].startswith("@@ "):
            row = rows[index]
            if not row or row[0] not in {" ", "+", "-"}:
                raise ValueError("patch contains an unsupported line")
            marker, value = row[0], row[1:]
            if marker == " ":
                if position >= len(source) or source[position] != value:
                    raise ValueError("patch context does not match the source file")
                output.append(value)
                position += 1
                consumed += 1
            elif marker == source_marker:
                if position >= len(source) or source[position] != value:
                    raise ValueError("patch deletion does not match the source file")
                position += 1
                consumed += 1
            else:
                output.append(value)
            index += 1
        if consumed != source_count:
            raise ValueError("patch hunk line count does not match its header")
    if hunk_count == 0:
        raise ValueError("patch must contain at least one hunk")
    output.extend(source[position:])
    updated = "".join(output)
    return _bounded_content(updated, "patched content")


def _patch(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    path = grant_relative_path(call.arguments["path"])
    patch = _bounded_content(call.arguments["patch"], "patch")
    _validate_patch_headers(patch, path)
    content, version = _read_with_version(capability, path, f"{call.call_id}:file.patch.read")
    updated = _apply_patch(content, patch, path, reverse=bool(call.arguments.get("reverse", False)))
    if updated == content:
        return {"ok": True, "path": path, "changed": False, "version": version}
    next_version, _changed = _write(
        capability,
        path,
        updated,
        f"{call.call_id}:file.patch.write",
        mode="overwrite",
        expected_hash=version,
    )
    return {"ok": True, "path": path, "changed": True, "version": next_version}


_MEDIA_MANIFEST, _MEDIA_HANDLERS = build_plugin("file", include=("file.send", "file.download_media"))
_LOCAL_TOOLS = (
    declaration("file.read_text", _READ_SCHEMA, _READ_OUTPUT_SCHEMA, "Read a granted workspace file with its opaque version."),
    declaration("file.write", _WRITE_SCHEMA, _WRITE_OUTPUT_SCHEMA, "Write bounded workspace text."),
    declaration("file.edit", _EDIT_SCHEMA, _WRITE_OUTPUT_SCHEMA, "Edit workspace text with an optimistic version guard."),
    declaration("file.patch", _PATCH_SCHEMA, _WRITE_OUTPUT_SCHEMA, "Apply a bounded unified patch with an optimistic version guard."),
)
_TOOLS = _MEDIA_MANIFEST.tools + _LOCAL_TOOLS
MANIFEST = PluginManifest(
    plugin_id="openagent.file",
    version="2.0.0",
    api_version="2",
    entrypoint="plugins.file.HANDLERS",
    tools=_TOOLS,
    capabilities=frozenset({capability for tool in _TOOLS for capability in tool.capabilities}),
)
HANDLERS: Mapping[str, Callable[[ToolCall, CapabilityClient], Mapping[str, Any]]] = {
    **_MEDIA_HANDLERS,
    "file.read_text": _read_text,
    "file.write": _write_text,
    "file.edit": _edit,
    "file.patch": _patch,
}
PLUGIN_MANIFEST = MANIFEST
TOOL_HANDLERS = HANDLERS
