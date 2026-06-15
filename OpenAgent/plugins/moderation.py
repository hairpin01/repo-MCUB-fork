# scop: inline
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Any


class ModerationPlugin:
    name = "moderation"
    version = "0.2.0"
    author = "@dev_dolbaeb"
    description = "Telegram moderation tools"

    tool_registry = (
        "moderation.mute", "moderation.unmute", "moderation.ban", "moderation.unban", "moderation.kick",
        "moderation.promote", "moderation.demote", "moderation.pin", "moderation.delete_messages", "moderation.get_admins",
    )

    dangerous_tools = {
        "moderation.mute", "moderation.ban", "moderation.kick",
        "moderation.promote", "moderation.demote", "moderation.pin", "moderation.delete_messages",
    }

    tool_docs = {
        "moderation.mute": {"desc": "Mute a user in a chat", "args": "chat (str); user (str); until (int) — seconds (default 3600)", "body": "user identifier"},
        "moderation.unmute": {"desc": "Unmute a user in a chat", "args": "chat (str); user (str)", "body": "user identifier"},
        "moderation.ban": {"desc": "Ban a user from a chat", "args": "chat (str); user (str); reason (str) — optional", "body": "user identifier"},
        "moderation.unban": {"desc": "Unban a user from a chat", "args": "chat (str); user (str)", "body": "user identifier"},
        "moderation.kick": {"desc": "Kick a user from a chat (can rejoin)", "args": "chat (str); user (str); reason (str) — optional", "body": "user identifier"},
        "moderation.promote": {"desc": "Promote a user to admin", "args": "chat (str); user (str); rank (str) — admin title", "body": "user identifier"},
        "moderation.demote": {"desc": "Demote an admin back to member", "args": "chat (str); user (str)", "body": "user identifier"},
        "moderation.pin": {"desc": "Pin a message in a chat", "args": "chat (str); message (str) or msg (str) — message ID", "body": "not used"},
        "moderation.delete_messages": {"desc": "Delete multiple messages in a chat", "args": "chat (str); ids (str) — comma-separated IDs", "body": "not used"},
        "moderation.get_admins": {"desc": "List admins of a chat", "args": "chat (str)", "body": "not used"},
    }

    tool_map = {
        "mute_user": "cmd_mute",
        "chat.mute": "cmd_mute",
        "moderation.mute": "cmd_mute",
        "unmute_user": "cmd_unmute",
        "chat.unmute": "cmd_unmute",
        "moderation.unmute": "cmd_unmute",
        "ban_user": "cmd_ban",
        "chat.ban": "cmd_ban",
        "moderation.ban": "cmd_ban",
        "unban_user": "cmd_unban",
        "chat.unban": "cmd_unban",
        "moderation.unban": "cmd_unban",
        "kick_user": "cmd_kick",
        "chat.kick": "cmd_kick",
        "moderation.kick": "cmd_kick",
        "promote_user": "cmd_promote",
        "chat.promote": "cmd_promote",
        "moderation.promote": "cmd_promote",
        "demote_user": "cmd_demote",
        "chat.demote": "cmd_demote",
        "moderation.demote": "cmd_demote",
        "moderation.pin": "cmd_pin",
        "moderation.delete_messages": "cmd_delete",
        "moderation.get_admins": "cmd_admins",
    }

    def __init__(self, agent: Any) -> None:
        self.agent = agent

    async def cmd_mute(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        user = await self.agent._resolve_tool_user(attrs.get("user") or body.strip(), source_event)
        until = int(attrs.get("until") or attrs.get("time") or "3600")
        from datetime import timedelta
        try:
            await self.agent.client.edit_permissions(chat, user, until_date=timedelta(seconds=until), send_messages=False)
            return f"User muted for {until}s"
        except Exception as exc:
            return f"Mute failed: {exc}"

    async def cmd_unmute(self, attrs_raw: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        user = await self.agent._resolve_tool_user(attrs.get("user") or "", source_event)
        try:
            await self.agent.client.edit_permissions(chat, user, send_messages=True)
            return "User unmuted"
        except Exception as exc:
            return f"Unmute failed: {exc}"

    async def cmd_ban(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        user = await self.agent._resolve_tool_user(attrs.get("user") or body.strip(), source_event)
        try:
            await self.agent.client.edit_permissions(chat, user, view_messages=False)
            return "User banned"
        except Exception as exc:
            return f"Ban failed: {exc}"

    async def cmd_unban(self, attrs_raw: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        user = await self.agent._resolve_tool_user(attrs.get("user") or "", source_event)
        try:
            await self.agent.client.edit_permissions(chat, user, view_messages=True)
            return "User unbanned"
        except Exception as exc:
            return f"Unban failed: {exc}"

    async def cmd_kick(self, attrs_raw: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        user = await self.agent._resolve_tool_user(attrs.get("user") or "", source_event)
        try:
            await self.agent.client.kick_participant(chat, user)
            return "User kicked"
        except Exception as exc:
            return f"Kick failed: {exc}"

    async def cmd_promote(self, attrs_raw: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        user = await self.agent._resolve_tool_user(attrs.get("user") or "", source_event)
        from telethon.tl.functions.channels import EditAdminRequest
        from telethon.tl.types import ChatAdminRights
        rights = ChatAdminRights(
            change_info=True, post_messages=True, edit_messages=True,
            delete_messages=True, ban_users=True, invite_users=True,
            pin_messages=True, add_admins=True, manage_call=True,
            other=True, anonymous=False,
        )
        try:
            await self.agent.client(EditAdminRequest(chat, user, rights, rank=attrs.get("rank", "admin")))
            return "User promoted"
        except Exception as exc:
            return f"Promote failed: {exc}"

    async def cmd_demote(self, attrs_raw: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        user = await self.agent._resolve_tool_user(attrs.get("user") or "", source_event)
        from telethon.tl.functions.channels import EditAdminRequest
        from telethon.tl.types import ChatAdminRights
        try:
            await self.agent.client(EditAdminRequest(chat, user, ChatAdminRights(), rank=""))
            return "User demoted"
        except Exception as exc:
            return f"Demote failed: {exc}"

    async def cmd_pin(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        msg_id = attrs.get("message") or attrs.get("msg") or body.strip()
        chat = await self.agent._resolve_tool_chat(attrs.get("chat") or attrs.get("to"), source_event)
        try:
            if msg_id and msg_id.isdigit():
                msg = await self.agent.client.get_messages(chat, ids=int(msg_id))
            else:
                reply = await source_event.get_reply_message() if source_event else None
                msg = reply
            if not msg:
                return "Message not found"
            await self.agent.client.pin_message(chat, msg.id)
            return f"Message pinned"
        except Exception as exc:
            return f"Pin failed: {exc}"

    async def cmd_delete(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        msg_ids = []
        raw = attrs.get("ids") or attrs.get("messages") or attrs.get("id") or body.strip()
        if raw:
            msg_ids = [int(x.strip()) for x in raw.split(",") if x.strip().isdigit()]
        if not msg_ids:
            reply = await source_event.get_reply_message() if source_event else None
            if reply:
                msg_ids = [reply.id]
        if not msg_ids:
            return "message id(s) required"
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        try:
            await self.agent.client.delete_messages(chat, msg_ids)
            return f"{len(msg_ids)} message(s) deleted"
        except Exception as exc:
            return f"Delete failed: {exc}"

    async def cmd_admins(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        from telethon.tl.types import ChannelParticipantsAdmins
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
