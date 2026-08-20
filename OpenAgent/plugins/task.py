# SPDX-License-Identifier: MIT
"""Schedule one bounded child call through the parent executor."""
from __future__ import annotations

from typing import Any, Callable, Mapping
from uuid import uuid4

from OpenAgentLib.PluginSDK import CapabilityClient, PluginManifest, PluginToolDeclaration
from OpenAgentLib.ToolCompatibility import TOOL_COMPATIBILITY_MATRIX
from OpenAgentLib.ToolKernel import ToolCall, normalize_tool_name


_INPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "canonical_tool_id": {"type": "string"}, "arguments": {"type": "object"},
        "remaining_calls": {"type": "integer"},
        "remaining_token_budget": {"type": "integer"},
        "remaining_depth": {"type": "integer"},
        "cancellation_parent_id": {"type": "string"},
    },
    "required": ["canonical_tool_id", "arguments", "remaining_calls", "remaining_token_budget", "remaining_depth", "cancellation_parent_id"],
    "additionalProperties": False,
}
_OUTPUT_SCHEMA = {"type": "object", "properties": {"ok": {"type": "boolean"}, "child_call_id": {"type": "string"}, "data": {"type": "object"}}, "required": ["ok", "child_call_id", "data"], "additionalProperties": False}


def _declaration(tool_id: str) -> PluginToolDeclaration:
    entry = next(item for item in TOOL_COMPATIBILITY_MATRIX if item.canonical_id == tool_id)
    return PluginToolDeclaration(entry.canonical_id, aliases=entry.aliases, input_schema=_INPUT_SCHEMA, output_schema=_OUTPUT_SCHEMA, capabilities=frozenset({entry.capability_class}), description="Schedule a bounded canonical child call through the parent.", confirmation=entry.confirmation_class, concurrency=entry.concurrency_class, idempotency=entry.idempotency_class, migration_disposition=entry.migration_disposition)


def _schedule(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    canonical_tool_id = normalize_tool_name(call.arguments["canonical_tool_id"], canonical=True)
    if canonical_tool_id.startswith("task."):
        raise ValueError("task tools cannot recursively schedule task tools")
    child = {
        "call_id": f"child-{uuid4().hex}", "canonical_tool_id": canonical_tool_id,
        "arguments": dict(call.arguments["arguments"]), "remaining_calls": call.arguments["remaining_calls"],
        "remaining_token_budget": call.arguments["remaining_token_budget"], "remaining_depth": call.arguments["remaining_depth"],
        "parent_call_id": call.call_id, "cancellation_parent_id": call.arguments["cancellation_parent_id"],
    }
    response = capability.schedule(child, f"{call.call_id}:task.schedule")
    if response.get("ok") is not True or not isinstance(response.get("data"), Mapping):
        raise ValueError("child scheduling request was denied")
    return {"ok": True, "child_call_id": child["call_id"], "data": dict(response["data"])}


_TOOLS = (_declaration("task.background"), _declaration("task.run_background"))
MANIFEST = PluginManifest("openagent.task", "2.0.0", "2", "plugins.task.HANDLERS", _TOOLS, frozenset({"runtime-control"}))
HANDLERS: Mapping[str, Callable[[ToolCall, CapabilityClient], Mapping[str, Any]]] = {"task.background": _schedule, "task.run_background": _schedule}
PLUGIN_MANIFEST = MANIFEST
TOOL_HANDLERS = HANDLERS
