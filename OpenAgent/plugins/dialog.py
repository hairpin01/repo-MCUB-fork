# scop: inline
# SPDX-License-Identifier: MIT

from __future__ import annotations

import asyncio
from typing import Any
from telethon.tl.functions.messages import ExportChatInviteRequest


class DialogPlugin:
    name = "dialog"
    version = "0.2.0"
    author = "@dev_dolbaeb"
    description = "Telegram dialog listing and management tools"

    tool_registry = (
        "dialog.list_private", "dialog.list_groups", "dialog.list_all", "dialog.search", "dialog.archive",
        "dialog.unarchive", "dialog.leave", "dialog.export_invite", "dialog.get_photo", "dialog.set_photo",
    )

    dangerous_tools = {
        "dialog.archive", "dialog.unarchive", "dialog.leave", "dialog.set_photo",
    }

    tool_docs = {
        "dialog.list_private": {
            "desc": "List private chats (PMs/DMs)",
            "args": "none",
            "body": "not used",
            "returns": "Text result with the requested data, or an error message.",
            "example": "{\"tool\": \"dialog.list_private\", \"args\": {}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "dialog.list_groups": {
            "desc": "List groups and channels",
            "args": "none",
            "body": "not used",
            "returns": "Text result with the requested data, or an error message.",
            "example": "{\"tool\": \"dialog.list_groups\", \"args\": {}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "dialog.list_all": {
            "desc": "List all dialogs",
            "args": "none",
            "body": "not used",
            "returns": "Text result with the requested data, or an error message.",
            "example": "{\"tool\": \"dialog.list_all\", \"args\": {}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "dialog.search": {
            "desc": "Search dialogs by name",
            "args": "q (str) or query (str) — search term",
            "body": "search term",
            "returns": "Text result with the requested data, or an error message.",
            "example": "{\"tool\": \"dialog.search\", \"args\": {\"chat\": \"@chat\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "dialog.archive": {
            "desc": "Archive a chat",
            "args": "chat (str) or id (str) — target",
            "body": "chat identifier",
            "returns": "Confirmation text with the performed action details, or an error message.",
            "example": "{\"tool\": \"dialog.archive\", \"args\": {\"chat\": \"@chat\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "dialog.unarchive": {
            "desc": "Unarchive a chat",
            "args": "chat (str) or id (str) — target",
            "body": "chat identifier",
            "returns": "Confirmation text with the performed action details, or an error message.",
            "example": "{\"tool\": \"dialog.unarchive\", \"args\": {\"chat\": \"@chat\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "dialog.leave": {
            "desc": "Leave a chat/group/channel",
            "args": "chat (str) or id (str) — target",
            "body": "chat identifier",
            "returns": "Confirmation text with the performed action details, or an error message.",
            "example": "{\"tool\": \"dialog.leave\", \"args\": {\"chat\": \"@chat\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "dialog.export_invite": {
            "desc": "Export an invite link for a chat",
            "args": "chat (str) — target chat",
            "body": "not used",
            "returns": "Text result or an error message.",
            "example": "{\"tool\": \"dialog.export_invite\", \"args\": {\"chat\": \"@chat\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "dialog.get_photo": {
            "desc": "Get the photo of a dialog",
            "args": "chat (str) — target",
            "body": "not used",
            "returns": "Text result with the requested data, or an error message.",
            "example": "{\"tool\": \"dialog.get_photo\", \"args\": {\"chat\": \"@chat\", \"path\": \"photo.jpg\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "dialog.set_photo": {
            "desc": "Set the photo of a dialog",
            "args": "chat (str) — target; photo (str) — file path",
            "body": "not used",
            "returns": "Confirmation text with the performed action details, or an error message.",
            "example": "{\"tool\": \"dialog.set_photo\", \"args\": {\"chat\": \"@chat\", \"path\": \"photo.jpg\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
    }

    tool_map = {
        "dialogs": "cmd_list",
        "dialog.list": "cmd_list",
        "dialog.list_private": "cmd_list",
        "dialog.list_groups": "cmd_list",
        "dialog.list_all": "cmd_list",
        "dialog.search": "cmd_search",
        "dialog.archive": "cmd_archive",
        "dialog.unarchive": "cmd_unarchive",
        "dialog.leave": "cmd_leave",
        "dialog.export_invite": "cmd_export_invite",
        "dialog.get_photo": "cmd_get_photo",
        "dialog.set_photo": "cmd_set_photo",
    }

    def __init__(self, agent: Any) -> None:
        self.agent = agent

    async def cmd_list(self, tool_name: str, attrs_raw: str, body: str) -> str:
        await asyncio.sleep(0)
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        if tool_name == "dialog.list_groups":
            mode = "groups"
        elif tool_name == "dialog.list_all":
            mode = "all"
        else:
            mode = body.strip() or attrs.get("mode") or "private"
        mode = mode.strip().lower()
        lines = []
        try:
            async for dialog in self.agent.client.iter_dialogs(limit=80):
                entity = dialog.entity
                is_user = bool(getattr(entity, "first_name", None) or getattr(entity, "last_name", None))
                is_bot = bool(getattr(entity, "bot", False))
                is_group = bool(getattr(entity, "megagroup", False) or getattr(entity, "broadcast", False))
                if mode in {"private", "pm", "dm"} and (not is_user or is_bot):
                    continue
                if mode in {"groups", "group", "chats"} and not is_group:
                    continue
                username = f"@{entity.username}" if getattr(entity, "username", None) else ""
                name = getattr(dialog, "name", None) or " ".join(
                    p for p in (
                        getattr(entity, "first_name", None),
                        getattr(entity, "last_name", None),
                    ) if p
                ) or getattr(entity, "title", None) or "Unknown"
                unread = getattr(dialog, "unread_count", 0)
                lines.append(f"{name} {username} [id={getattr(entity, 'id', None)}] unread={unread}".strip())
                if len(lines) >= 40:
                    break
        except Exception as exc:
            return f"Dialogs failed: {exc}"
        return "\n".join(lines) or "No dialogs"

    async def cmd_search(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        query = (attrs.get("query") or body.strip()).lower()
        limit = max(1, min(int(attrs.get("limit", "20") or 20), 100))
        if not query:
            return "query is required"
        lines = []
        try:
            async for dialog in self.agent.client.iter_dialogs(limit=300):
                entity = dialog.entity
                username = getattr(entity, "username", None) or ""
                title = getattr(dialog, "name", None) or getattr(entity, "title", None) or " ".join(
                    p for p in (getattr(entity, "first_name", None), getattr(entity, "last_name", None)) if p
                )
                if query in f"{title} {username}".lower():
                    lines.append(f"{title} @{username} [id={getattr(entity, 'id', None)}]".strip())
                    if len(lines) >= limit:
                        break
        except Exception:
            pass
        return "\n".join(lines) or "No dialogs found"

    async def cmd_archive(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat") or body.strip(), source_event)
        try:
            from telethon.tl.functions.folders import EditPeerFoldersRequest
            from telethon.tl.types import InputFolderPeer
            await self.agent.client(EditPeerFoldersRequest([InputFolderPeer(chat, 1)]))
            return "Dialog archived"
        except Exception as exc:
            return f"Archive failed: {exc}"

    async def cmd_unarchive(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat") or body.strip(), source_event)
        try:
            from telethon.tl.functions.folders import EditPeerFoldersRequest
            from telethon.tl.types import InputFolderPeer
            await self.agent.client(EditPeerFoldersRequest([InputFolderPeer(chat, 0)]))
            return "Dialog unarchived"
        except Exception as exc:
            return f"Unarchive failed: {exc}"

    async def cmd_leave(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat") or body.strip(), source_event)
        try:
            from telethon.tl.functions.messages import DeleteChatRequest
            await self.agent.client(DeleteChatRequest(chat))
            return "Left the chat"
        except Exception as exc:
            return f"Leave failed: {exc}"

    async def cmd_export_invite(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat") or body.strip(), source_event)
        try:
            link = await self.agent.client(ExportChatInviteRequest(chat))
            return f"Invite link: {link.link}"
        except Exception as exc:
            return f"Export invite failed: {exc}"

    async def cmd_get_photo(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = await self.agent._resolve_tool_chat(attrs.get("chat") or body.strip(), source_event)
        try:
            photo = getattr(chat, "photo", None)
            if not photo:
                return "No photo"
            return f"Has photo: {photo.sizes[-1].type if photo.sizes else 'unknown'}"
        except Exception as exc:
            return f"Get photo failed: {exc}"

    async def cmd_set_photo(self, attrs_raw: str, body: str, source_event: Any) -> str:
        import io
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        path_str = attrs.get("path") or attrs.get("file") or body.strip()
        if path_str:
            from pathlib import Path as P
            fpath = P(path_str).expanduser()
            if not fpath.is_absolute():
                fpath = P.cwd() / fpath
            chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
            if not fpath.is_file():
                return f"File not found: {fpath}"
            try:
                from telethon.tl.functions.channels import EditPhotoRequest
                from telethon.tl.types import InputChatUploadedPhoto
                uploaded = await self.agent.client.upload_file(str(fpath))
                await self.agent.client(EditPhotoRequest(chat, InputChatUploadedPhoto(uploaded)))
                return "Photo updated"
            except Exception as exc:
                return f"Set photo failed: {exc}"
        reply = await source_event.get_reply_message() if source_event else None
        if reply and reply.media:
            try:
                chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
                data = await reply.download_media(file=bytes)
                if data:
                    from telethon.tl.functions.channels import EditPhotoRequest
                    from telethon.tl.types import InputChatUploadedPhoto
                    uploaded = await self.agent.client.upload_file(io.BytesIO(data))
                    await self.agent.client(EditPhotoRequest(chat, InputChatUploadedPhoto(uploaded)))
                    return "Photo updated from replied media"
            except Exception as exc:
                return f"Set photo from reply failed: {exc}"
        return "path or replied media required"
