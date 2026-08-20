# SPDX-License-Identifier: MIT
"""Pure v2 helpers shared by resource-scoped sibling plugins."""
from __future__ import annotations

from typing import Any, Mapping

from OpenAgentLib.PluginSDK import PluginToolDeclaration
from OpenAgentLib.ToolCompatibility import TOOL_COMPATIBILITY_MATRIX


MAX_OUTPUT_BYTES = 12_000


def declaration(
    tool_id: str,
    input_schema: Mapping[str, Any],
    output_schema: Mapping[str, Any],
    description: str,
) -> PluginToolDeclaration:
    entry = next((item for item in TOOL_COMPATIBILITY_MATRIX if item.canonical_id == tool_id), None)
    if entry is None:
        raise RuntimeError(f"missing frozen tool compatibility entry: {tool_id}")
    return PluginToolDeclaration(
        tool_id,
        aliases=entry.aliases,
        input_schema=input_schema,
        output_schema=output_schema,
        capabilities=frozenset({entry.capability_class}),
        description=description,
        confirmation=entry.confirmation_class,
        concurrency=entry.concurrency_class,
        idempotency=entry.idempotency_class,
        migration_disposition=entry.migration_disposition,
    )


def grant_relative_path(value: Any, *, allow_root: bool = False, field: str = "path") -> str:
    if not isinstance(value, str) or not value or len(value) > 512:
        raise ValueError(f"{field} must be a bounded non-empty string")
    if "\x00" in value or "\\" in value or value.startswith("/"):
        raise ValueError(f"{field} must be a grant-relative path")
    parts = value.split("/")
    if any(part in {"", ".."} for part in parts) or (value == "." and not allow_root):
        raise ValueError(f"{field} must be a grant-relative path")
    return value


def bounded_text(value: Any, limit: int = MAX_OUTPUT_BYTES) -> tuple[str, bool]:
    if not isinstance(value, str):
        raise ValueError("capability response text must be a string")
    encoded = value.encode("utf-8", errors="replace")
    if len(encoded) <= limit:
        return value, False
    return encoded[:limit].decode("utf-8", errors="ignore"), True


def response_data(response: Mapping[str, Any]) -> Mapping[str, Any]:
    if not isinstance(response.get("ok"), bool):
        raise ValueError("capability response must declare a boolean ok field")
    if response["ok"] is False:
        raise ValueError("capability request was denied")
    data = response.get("data", response)
    if not isinstance(data, Mapping):
        raise ValueError("capability response data must be an object")
    return data


def required_text(data: Mapping[str, Any], field: str, *, limit: int = 262_144) -> str:
    value = data.get(field)
    if not isinstance(value, str) or len(value.encode("utf-8", errors="replace")) > limit:
        raise ValueError(f"capability response {field} must be bounded text")
    return value
