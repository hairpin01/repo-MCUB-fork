# scop: inline
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Any
from telethon.tl.functions.contacts import (
    AddContactRequest,
    BlockRequest,
    DeleteContactsRequest,
    UnblockRequest,
)


class ContactsPlugin:
    name = "contacts"
    version = "0.2.0"
    author = "@dev_dolbaeb"
    description = "Telegram contacts tools"

    tool_registry = (
        "contacts.add",
        "contacts.delete",
        "contacts.block",
        "contacts.unblock",
        "contacts.entity",
    )

    dangerous_tools = {
        "contacts.add", "contacts.delete", "contacts.block", "contacts.unblock",
    }

    tool_docs = {
        "contacts.add": {"desc": "Add a user to your contacts", "args": "user (str); first_name (str); last_name (str); phone (str)", "body": "user identifier"},
        "contacts.delete": {"desc": "Delete a contact from your contacts list", "args": "user (str) — user to remove", "body": "user identifier"},
        "contacts.block": {"desc": "Block a user", "args": "user (str) — user to block", "body": "user identifier"},
        "contacts.unblock": {"desc": "Unblock a previously blocked user", "args": "user (str) — user to unblock", "body": "user identifier"},
        "contacts.entity": {"desc": "Resolve a username or ID to entity info", "args": "user (str) — username or ID", "body": "user identifier"},
    }

    tool_map = {
        "contacts.add": "cmd_add",
        "contacts.delete": "cmd_delete",
        "contacts.block": "cmd_block",
        "contacts.unblock": "cmd_unblock",
        "contacts.entity": "cmd_entity",
    }

    def __init__(self, agent: Any) -> None:
        self.agent = agent

    async def cmd_add(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        user = await self.agent._resolve_tool_user(attrs.get("user") or body.strip(), source_event)
        first = attrs.get("first_name") or attrs.get("first") or getattr(user, "first_name", "") or ""
        last = attrs.get("last_name") or attrs.get("last") or getattr(user, "last_name", "") or ""
        phone = attrs.get("phone") or ""
        try:
            await self.agent.client(AddContactRequest(
                id=user.id,
                first_name=first,
                last_name=last,
                phone=phone,
                add_phone_privacy_exception=False,
            ))
            return f"Contact added: {first} {last}"
        except Exception as exc:
            return f"Add contact failed: {exc}"

    async def cmd_delete(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        user = await self.agent._resolve_tool_user(attrs.get("user") or body.strip(), source_event)
        try:
            await self.agent.client(DeleteContactsRequest(id=[user.id]))
            return f"Contact deleted"
        except Exception as exc:
            return f"Delete contact failed: {exc}"

    async def cmd_block(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        user = await self.agent._resolve_tool_user(attrs.get("user") or body.strip(), source_event)
        try:
            await self.agent.client(BlockRequest(id=user.id))
            return f"User blocked"
        except Exception as exc:
            return f"Block failed: {exc}"

    async def cmd_unblock(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        user = await self.agent._resolve_tool_user(attrs.get("user") or body.strip(), source_event)
        try:
            await self.agent.client(UnblockRequest(id=user.id))
            return f"User unblocked"
        except Exception as exc:
            return f"Unblock failed: {exc}"

    async def cmd_entity(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        target = body.strip() or attrs.get("user") or attrs.get("chat") or attrs.get("entity") or ""
        if not target:
            return "user/chat is required"
        try:
            entity = await self.agent.client.get_entity(target)
            lines = [f"ID: {entity.id}"]
            if getattr(entity, "title", None):
                lines.append(f"Title: {entity.title}")
            if getattr(entity, "username", None):
                lines.append(f"Username: @{entity.username}")
            if getattr(entity, "first_name", None):
                lines.append(f"First name: {entity.first_name}")
            if getattr(entity, "last_name", None):
                lines.append(f"Last name: {entity.last_name}")
            if getattr(entity, "phone", None):
                lines.append(f"Phone: {entity.phone}")
            if getattr(entity, "participants_count", None):
                lines.append(f"Participants: {entity.participants_count}")
            return "\n".join(lines)
        except Exception as exc:
            return f"Entity lookup failed: {exc}"
