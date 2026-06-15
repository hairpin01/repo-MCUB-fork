# scop: inline
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Any
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditTitleRequest,
    ToggleSlowModeRequest,
    UpdateUsernameRequest,
)
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import EditChatAboutRequest, ExportChatInviteRequest
from telethon.tl.types import ChatAdminRights, ChannelParticipantsAdmins


class ChatPlugin:
    name = "chat"
    version = "0.2.0"
    author = "@dev_dolbaeb"
    description = "Telegram chat information and settings tools"

    tool_registry = (
        "chat.info", "chat.participants", "chat.admins", "chat.permissions", "chat.common_with_user",
        "chat.set_title", "chat.set_about", "chat.set_username", "chat.slowmode", "chat.invite_link",
    )

    dangerous_tools = {
        "chat.set_title", "chat.set_about", "chat.set_username", "chat.slowmode",
    }

    tool_docs = {
        "chat.info": {"desc": "Get info about a Telegram chat/group/channel", "args": "chat (str) or query (str) — username, ID, or link", "body": "chat identifier"},
        "chat.participants": {"desc": "List participants in a chat", "args": "chat (str); limit (int) — max results (default 30)", "body": "chat identifier"},
        "chat.admins": {"desc": "List admins of a chat", "args": "chat (str) — chat identifier", "body": "chat identifier"},
        "chat.permissions": {"desc": "Get permissions of a chat", "args": "chat (str) — chat identifier", "body": "chat identifier"},
        "chat.common_with_user": {"desc": "Find common chats with a user", "args": "user (str) — target user", "body": "user identifier"},
        "chat.set_title": {"desc": "Change the title of a chat", "args": "chat (str) — target; title (str) — new title", "body": "title text"},
        "chat.set_about": {"desc": "Change the description/about of a chat", "args": "chat (str) — target; about (str) or description (str) — new text", "body": "about text"},
        "chat.set_username": {"desc": "Change the username of a chat/channel", "args": "chat (str) — target; username (str) — new username", "body": "not used"},
        "chat.slowmode": {"desc": "Set slowmode interval in seconds", "args": "chat (str) — target; seconds (int) — slowmode delay", "body": "not used"},
        "chat.invite_link": {"desc": "Get or create an invite link for a chat", "args": "chat (str) — target chat", "body": "not used"},
    }

    tool_map = {
        "chat": "cmd_info",
        "chat.info": "cmd_info",
        "chat.participants": "cmd_participants",
        "chat.search": "cmd_search",
        "chat.admins": "cmd_admins",
        "chat.permissions": "cmd_permissions",
        "chat.common_with_user": "cmd_common_chats",
        "chat.set_username": "cmd_set_username",
        "chat.invite_link": "cmd_invite_link",
        "set_slowmode": "cmd_slowmode",
        "chat.slowmode": "cmd_slowmode",
        "set_chat_title": "cmd_title",
        "chat.set_title": "cmd_title",
        "set_chat_about": "cmd_about",
        "chat.set_about": "cmd_about",
        "join_chat": "cmd_join",
    }

    def __init__(self, agent: Any) -> None:
        self.agent = agent

    async def cmd_info(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        query = body.strip() or attrs.get("chat") or attrs.get("query") or ""
        try:
            if query:
                chat = await self.agent.client.get_entity(query)
            else:
                chat = await self.agent._resolve_tool_chat(None, source_event)
            title = getattr(chat, "title", None) or getattr(chat, "first_name", None) or "Unknown"
            username = f"@{chat.username}" if getattr(chat, "username", None) else ""
            result = f"Title: {title}\nID: {chat.id}\n{username}\n".strip()
            if getattr(chat, "participants_count", None):
                result += f"\nParticipants: {chat.participants_count}"
            if getattr(chat, "megagroup", None):
                result += "\nType: Supergroup"
            elif getattr(chat, "broadcast", None):
                result += "\nType: Channel"
            elif getattr(chat, "first_name", None):
                result += "\nType: User"
            return result
        except Exception as exc:
            return f"Chat info failed: {exc}"

    async def cmd_participants(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        query = body.strip() or attrs.get("chat") or ""
        limit = max(1, min(int(attrs.get("limit", "20") or 20), 100))
        try:
            chat = await self.agent.client.get_entity(query) if query else await self.agent._resolve_tool_chat(None, source_event)
            participants = await self.agent.client.get_participants(chat, limit=limit)
            lines = []
            for u in participants:
                name = f"{u.first_name or ''} {u.last_name or ''}".strip() or "Unknown"
                username = f"@{u.username}" if getattr(u, "username", None) else ""
                lines.append(f"{name} {username} [id={u.id}]".strip())
            return "\n".join(lines) if lines else "No participants"
        except Exception as exc:
            return f"Participants failed: {exc}"

    async def cmd_search(self, attrs_raw: str, body: str, source_event: Any) -> str:
        return await self.agent._search_messages_tool(attrs_raw, body, source_event)

    async def cmd_admins(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        try:
            admins = await self.agent.client.get_participants(chat, filter=ChannelParticipantsAdmins)
            lines = []
            for admin in admins:
                name = f"{admin.first_name or ''} {admin.last_name or ''}".strip() or "Unknown"
                username = f"@{admin.username}" if getattr(admin, "username", None) else ""
                lines.append(f"{name} {username} [id={admin.id}]".strip())
            return "\n".join(lines) if lines else "No admins found"
        except Exception as exc:
            return f"Get admins failed: {exc}"

    async def cmd_permissions(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        user = await self.agent._resolve_tool_user(attrs.get("user") or "", source_event)
        try:
            perms = await self.agent.client.get_permissions(chat, user)
            return "\n".join(f"{k}: {v}" for k, v in sorted(vars(perms).items()) if not k.startswith("_"))[:4000]
        except Exception as exc:
            return f"Permissions failed: {exc}"

    async def cmd_common_chats(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        user = await self.agent._resolve_tool_user(attrs.get("user") or body.strip(), source_event)
        limit = max(1, min(int(attrs.get("limit", "20") or 20), 100))
        try:
            chats = await self.agent.client.get_common_chats(user, limit=limit)
            lines = []
            for c in chats:
                title = getattr(c, "title", None) or getattr(c, "first_name", None) or "Unknown"
                username = f"@{c.username}" if getattr(c, "username", None) else ""
                lines.append(f"{title} {username} [id={getattr(c, 'id', None)}]".strip())
            return "\n".join(lines) if lines else "No common chats"
        except Exception as exc:
            return f"Common chats failed: {exc}"

    async def cmd_set_username(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        username = attrs.get("username") or body.strip()
        if not username:
            return "username is required"
        try:
            await self.agent.client(UpdateUsernameRequest(chat, username=username))
            return f"Username set: @{username}"
        except Exception as exc:
            return f"Set username failed: {exc}"

    async def cmd_invite_link(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat") or body.strip(), source_event)
        try:
            link = await self.agent.client(ExportChatInviteRequest(chat))
            return f"Invite link: {link.link}"
        except Exception as exc:
            return f"Export invite failed: {exc}"

    async def cmd_slowmode(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        seconds = int(attrs.get("seconds") or body.strip() or "10")
        try:
            await self.agent.client(ToggleSlowModeRequest(chat, seconds))
            return f"Slow mode set to {seconds}s"
        except Exception as exc:
            return f"Slowmode failed: {exc}"

    async def cmd_title(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        title = attrs.get("title") or body.strip()
        if not title:
            return "title is required"
        try:
            await self.agent.client(EditTitleRequest(chat, title))
            return f"Title set: {title}"
        except Exception as exc:
            return f"Set title failed: {exc}"

    async def cmd_about(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        about = attrs.get("about") or attrs.get("description") or body.strip()
        try:
            await self.agent.client(EditChatAboutRequest(chat, about))
            return f"About set: {about}"
        except Exception as exc:
            return f"Set about failed: {exc}"

    async def cmd_join(self, attrs_raw: str, body: str) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        target = attrs.get("invite") or attrs.get("chat") or attrs.get("link") or body.strip()
        if not target:
            return "invite link or username is required"
        from telethon.tl.functions.channels import JoinChannelRequest
        from telethon.tl.functions.messages import ImportChatInviteRequest
        try:
            if target.startswith(("https://t.me/", "t.me/")):
                parts = target.rstrip("/").split("/")
                target = parts[-1]
                if "joinchat" in target:
                    await self.agent.client(ImportChatInviteRequest(target.split("/")[-1]))
                    return "Joined via invite"
            if target.startswith("+"):
                await self.agent.client(ImportChatInviteRequest(target[1:]))
                return "Joined via hash"
            entity = await self.agent.client.get_entity(target)
            await self.agent.client(JoinChannelRequest(entity))
            return f"Joined: {target}"
        except Exception as exc:
            return f"Join failed: {exc}"
