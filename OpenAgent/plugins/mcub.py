# SPDX-License-Identifier: MIT
"""Named MCUB control requests without kernel or command access."""
from __future__ import annotations

import json
from typing import Any, Callable, Mapping

from OpenAgentLib.PluginSDK import CapabilityClient, CapabilityFamily, PluginManifest, PluginToolDeclaration
from OpenAgentLib.ToolCompatibility import TOOL_COMPATIBILITY_MATRIX
from OpenAgentLib.ToolKernel import ToolCall


_CONFIG_KEYS = ("openagent.system_prompt", "openagent.eval_timeout", "openagent.task_background_enabled", "openagent.task_background_max")
_EMPTY_SCHEMA = {"type": "object", "properties": {}, "additionalProperties": False}
_COMMAND_SCHEMA = {"type": "object", "properties": {"operation": {"type": "string", "enum": ["module-list", "module-reload"]}}, "required": ["operation"], "additionalProperties": False}
_INSTALL_SCHEMA = {"type": "object", "properties": {"module_url": {"type": "string"}}, "required": ["module_url"], "additionalProperties": False}
_CONFIG_VALUE_SCHEMA = {"type": "object", "properties": {"json": {"type": "string"}}, "required": ["json"], "additionalProperties": False}
_CONFIG_SCHEMA = {"type": "object", "properties": {"operation": {"type": "string", "enum": ["get", "set"]}, "key": {"type": "string", "enum": list(_CONFIG_KEYS)}, "value": _CONFIG_VALUE_SCHEMA}, "required": ["operation", "key"], "additionalProperties": False}
_OUTPUT_SCHEMA = {"type": "object", "properties": {"ok": {"type": "boolean"}, "operation": {"type": "string"}, "data": {"type": "object"}}, "required": ["ok", "operation", "data"], "additionalProperties": False}


def _declaration(tool_id: str, schema: Mapping[str, Any], description: str) -> PluginToolDeclaration:
    entry = next(item for item in TOOL_COMPATIBILITY_MATRIX if item.canonical_id == tool_id)
    return PluginToolDeclaration(entry.canonical_id, aliases=entry.aliases, input_schema=schema, output_schema=_OUTPUT_SCHEMA, capabilities=frozenset({entry.capability_class}), description=description, confirmation=entry.confirmation_class, concurrency=entry.concurrency_class, idempotency=entry.idempotency_class, migration_disposition=entry.migration_disposition)


def _response(capability: CapabilityClient, operation: str, payload: Mapping[str, Any], call: ToolCall) -> Mapping[str, Any]:
    response = capability.request(CapabilityFamily.MCUB_CONTROL, operation, payload, f"{call.call_id}:mcub:{operation}")
    if response.get("ok") is not True or not isinstance(response.get("data"), Mapping):
        raise ValueError("MCUB control request was denied")
    return {"ok": True, "operation": operation, "data": dict(response["data"])}


def _command(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    return _response(capability, call.arguments["operation"], {}, call)


def _config(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    operation = call.arguments["operation"]
    if operation == "set" and "value" not in call.arguments:
        raise ValueError("config-set requires an explicit JSON value")
    payload = {"key": call.arguments["key"]}
    if operation == "set":
        try:
            payload["value"] = json.loads(call.arguments["value"]["json"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError("config-set requires a JSON value") from exc
    return _response(capability, f"config-{operation}", payload, call)


def _modules(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    return _response(capability, "module-list", {}, call)


def _install(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    return _response(capability, "module-install", {"module_url": call.arguments["module_url"]}, call)


def _reload(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    return _response(capability, "module-reload", {}, call)


_TOOLS = (
    _declaration("mcub.command", _COMMAND_SCHEMA, "Run one named safe MCUB control operation."),
    _declaration("mcub.config", _CONFIG_SCHEMA, "Read or write one allowlisted OpenAgent configuration key."),
    _declaration("mcub.modules", _EMPTY_SCHEMA, "List MCUB modules."),
    _declaration("mcub.install", _INSTALL_SCHEMA, "Install a module from a credential-free HTTPS URL."),
    _declaration("mcub.reload", _EMPTY_SCHEMA, "Reload MCUB modules."),
)
MANIFEST = PluginManifest("openagent.mcub", "2.0.0", "2", "plugins.mcub.HANDLERS", _TOOLS, frozenset({"runtime-control"}))
HANDLERS: Mapping[str, Callable[[ToolCall, CapabilityClient], Mapping[str, Any]]] = {"mcub.command": _command, "mcub.config": _config, "mcub.modules": _modules, "mcub.install": _install, "mcub.reload": _reload}
PLUGIN_MANIFEST = MANIFEST
TOOL_HANDLERS = HANDLERS
