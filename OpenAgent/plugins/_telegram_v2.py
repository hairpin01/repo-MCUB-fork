# SPDX-License-Identifier: MIT
"""Pure v2 declarations shared by the Telegram-facing sibling plugins.

This module deliberately knows only opaque JSON references.  Telegram client
resolution and authorization stay in the parent capability broker.
"""
from __future__ import annotations

from typing import Any, Callable, Mapping

from OpenAgentLib.PluginSDK import CapabilityClient, PluginManifest, PluginToolDeclaration
from OpenAgentLib.ToolCompatibility import TOOL_COMPATIBILITY_MATRIX
from OpenAgentLib.ToolKernel import ToolCall


_STRING = {"type": "string"}
_OPTIONAL_STRING = {"type": "string"}
_INTEGER = {"type": "integer"}

# These are intentionally opaque IDs, never usernames, links, Telethon entities,
# or application event objects.
_INPUTS: Mapping[str, tuple[tuple[str, ...], tuple[str, ...]]] = {
    "chat.info": ((), ("peer_id",)),
    "chat.participants": (("peer_id",), ("limit",)),
    "chat.admins": (("peer_id",), ()),
    "chat.permissions": (("peer_id",), ()),
    "chat.common_with_user": (("user_id",), ("limit",)),
    "chat.set_title": (("peer_id", "title"), ()),
    "chat.set_about": (("peer_id", "about"), ()),
    "chat.set_username": (("peer_id", "username"), ()),
    "chat.slowmode": (("peer_id", "seconds"), ()),
    "chat.invite_link": (("peer_id",), ()),
    "contacts.add": (("user_id", "first_name"), ("last_name", "phone")),
    "contacts.delete": (("user_id",), ()), "contacts.block": (("user_id",), ()),
    "contacts.unblock": (("user_id",), ()), "contacts.entity": (("user_id",), ()),
    "creation.channel": (("title",), ("about",)), "creation.group": (("title",), ("about",)),
    "creation.bot": (("name", "username"), ("about",)), "creation.private_invite": (("invite_id",), ()),
    "dialog.list_private": ((), ("limit",)), "dialog.list_groups": ((), ("limit",)),
    "dialog.list_all": ((), ("limit",)), "dialog.search": (("query",), ("limit",)),
    "dialog.archive": (("peer_id",), ()), "dialog.unarchive": (("peer_id",), ()),
    "dialog.leave": (("peer_id",), ()), "dialog.export_invite": (("peer_id",), ()),
    "dialog.get_photo": (("peer_id",), ()), "dialog.set_photo": (("peer_id", "media_id"), ()),
    "message.send_current": (("peer_id", "text"), ("reply_to_message_id",)),
    "message.send_target": (("peer_id", "text"), ("reply_to_message_id",)),
    "message.reply": (("peer_id", "message_id", "text"), ()),
    "message.edit": (("peer_id", "message_id", "text"), ()),
    "message.forward": (("peer_id", "message_id", "destination_peer_id"), ()),
    "message.delete": (("peer_id", "message_id"), ()), "message.pin": (("peer_id", "message_id"), ()),
    "message.react": (("peer_id", "message_id", "reaction"), ()),
    "message.get": (("peer_id", "message_id"), ()), "message.search": (("peer_id", "query"), ("limit",)),
    "message.history": (("peer_id",), ("limit",)), "message.mark_read": (("peer_id", "message_id"), ()),
    "message.typing": (("peer_id",), ()), "message.schedule": (("peer_id", "text", "schedule_at"), ()),
    "message.draft": (("peer_id", "text"), ()),
    "moderation.mute": (("peer_id", "user_id"), ("until_seconds",)),
    "moderation.unmute": (("peer_id", "user_id"), ()), "moderation.ban": (("peer_id", "user_id"), ("reason",)),
    "moderation.unban": (("peer_id", "user_id"), ()), "moderation.kick": (("peer_id", "user_id"), ()),
    "moderation.promote": (("peer_id", "user_id"), ("rights",)), "moderation.demote": (("peer_id", "user_id"), ()),
    "moderation.pin": (("peer_id", "message_id"), ()), "moderation.delete_messages": (("peer_id", "message_id"), ()),
    "moderation.get_admins": (("peer_id",), ()),
    "profile.get": (("user_id",), ()), "profile.get_full": (("user_id",), ()), "profile.get_me": ((), ()),
    "profile.update_name": (("first_name",), ("last_name",)), "profile.update_bio": (("bio",), ()),
    "profile.update_username": (("username",), ()), "profile.set_photo": (("media_id",), ()),
    "profile.download_photo": (("user_id",), ()), "profile.get_photos": (("user_id",), ("limit",)),
    "profile.common_chats": (("user_id",), ("limit",)),
    "file.send": (("peer_id", "media_id"), ("caption",)),
    "file.download_media": (("peer_id", "message_id"), ()),
}

_OPERATIONS = {
    "message.send_current": "send-message", "message.send_target": "send-message",
    "message.edit": "edit-message", "message.delete": "delete-message", "message.react": "react",
    "message.get": "get-message", "file.send": "send-media", "file.download_media": "download-media",
}


def _schema(tool_id: str) -> Mapping[str, Any]:
    required, optional = _INPUTS[tool_id]
    properties: dict[str, Mapping[str, Any]] = {}
    for key in (*required, *optional):
        if key in {"limit", "seconds", "until_seconds"}:
            properties[key] = _INTEGER
        elif key == "rights":
            properties[key] = {"type": "array", "items": _STRING}
        else:
            properties[key] = _STRING if key in required else _OPTIONAL_STRING
    return {"type": "object", "properties": properties, "required": list(required), "additionalProperties": False}


_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "ok": {"type": "boolean"}, "operation": _STRING,
        "result_id": _OPTIONAL_STRING, "peer_id": _OPTIONAL_STRING,
        "message_id": _OPTIONAL_STRING, "media_id": _OPTIONAL_STRING,
        "artifact_id": _OPTIONAL_STRING,
    },
    "required": ["ok", "operation"], "additionalProperties": False,
}


def _operation(tool_id: str) -> str:
    return _OPERATIONS.get(tool_id, tool_id.replace(".", "-"))


def _result(operation: str, response: Mapping[str, Any]) -> Mapping[str, Any]:
    data = response.get("data", response)
    result: dict[str, Any] = {"ok": bool(response.get("ok", True)), "operation": operation}
    if isinstance(data, Mapping):
        for key in ("result_id", "peer_id", "message_id", "media_id", "artifact_id"):
            value = data.get(key)
            if isinstance(value, str):
                result[key] = value
    return result


def _handler(tool_id: str) -> Callable[[ToolCall, CapabilityClient], Mapping[str, Any]]:
    operation = _operation(tool_id)

    def handle(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
        if call.spec.canonical_id != tool_id:
            raise ValueError("tool call does not match its Telegram handler")
        response = capability.telegram(operation, call.arguments, f"{call.call_id}:{tool_id}")
        return _result(operation, response)

    return handle


def build_plugin(module: str, *, include: tuple[str, ...] | None = None) -> tuple[PluginManifest, Mapping[str, Callable[[ToolCall, CapabilityClient], Mapping[str, Any]]]]:
    entries = tuple(entry for entry in TOOL_COMPATIBILITY_MATRIX if entry.source_module == module)
    if include is not None:
        entries = tuple(entry for entry in entries if entry.canonical_id in include)
    missing = sorted(entry.canonical_id for entry in entries if entry.canonical_id not in _INPUTS)
    if missing:
        raise RuntimeError(f"Telegram v2 schemas missing: {', '.join(missing)}")
    tools = tuple(PluginToolDeclaration(
        entry.canonical_id, aliases=entry.aliases, input_schema=_schema(entry.canonical_id),
        output_schema=_OUTPUT_SCHEMA, capabilities=frozenset({entry.capability_class}),
        description=f"Telegram capability operation for {entry.canonical_id}", confirmation=entry.confirmation_class,
        concurrency=entry.concurrency_class, idempotency=entry.idempotency_class,
        migration_disposition=entry.migration_disposition,
    ) for entry in entries)
    manifest = PluginManifest(
        plugin_id=f"openagent.{module}", version="2.0.0", api_version="2",
        entrypoint=f"plugins.{module}.HANDLERS", tools=tools,
        capabilities=frozenset({capability for tool in tools for capability in tool.capabilities}),
    )
    return manifest, {tool.canonical_id: _handler(tool.canonical_id) for tool in tools}
