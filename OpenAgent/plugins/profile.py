# scop: inline
# SPDX-License-Identifier: MIT

from __future__ import annotations

from pathlib import Path
from typing import Any
from telethon.tl.functions.account import (
    UpdateProfileRequest,
    UpdateUsernameRequest,
)
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.users import GetFullUserRequest


class ProfilePlugin:
    name = "profile"
    version = "0.2.0"
    author = "@dev_dolbaeb"
    description = "Telegram profile tools"

    tool_registry = (
        "profile.get", "profile.get_full", "profile.get_me", "profile.update_name", "profile.update_bio",
        "profile.update_username", "profile.set_photo", "profile.download_photo", "profile.get_photos", "profile.common_chats",
    )

    dangerous_tools = {
        "profile.update_name", "profile.update_bio", "profile.update_username",
        "profile.set_photo",
    }

    tool_docs = {
        "profile.get": {
            "desc": "Get basic profile info for a user",
            "args": "target (str) or user (str) — username or ID",
            "body": "user identifier",
            "returns": "Text result with the requested data, or an error message.",
            "example": "{\"tool\": \"profile.get\", \"args\": {\"user\": \"@user\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "profile.get_full": {
            "desc": "Get full profile info (includes bio, photo, etc.)",
            "args": "target (str) or user (str) — username or ID",
            "body": "user identifier",
            "returns": "Text result with the requested data, or an error message.",
            "example": "{\"tool\": \"profile.get_full\", \"args\": {\"user\": \"@user\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "profile.get_me": {
            "desc": "Get your own profile info",
            "args": "none",
            "body": "not used",
            "returns": "Text result with the requested data, or an error message.",
            "example": "{\"tool\": \"profile.get_me\", \"args\": {}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "profile.get_photos": {
            "desc": "List or download profile photos",
            "args": "target (str) or user (str); download (str) — set to 'true' to download",
            "body": "user identifier",
            "returns": "Text result with the requested data, or an error message.",
            "example": "{\"tool\": \"profile.get_photos\", \"args\": {\"user\": \"@user\", \"limit\": 10}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "profile.common_chats": {
            "desc": "Find common chats with another user",
            "args": "target (str) or user (str)",
            "body": "user identifier",
            "returns": "Text result with the requested data, or an error message.",
            "example": "{\"tool\": \"profile.common_chats\", \"args\": {\"user\": \"@user\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "profile.update_name": {
            "desc": "Update your first/last name",
            "args": "first_name (str); last_name (str) — optional",
            "body": "not used",
            "returns": "Confirmation text with the performed action details, or an error message.",
            "example": "{\"tool\": \"profile.update_name\", \"args\": {\"user\": \"@user\", \"first_name\": \"First\", \"last_name\": \"Last\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "profile.update_bio": {
            "desc": "Update your profile bio/about",
            "args": "bio (str) or about (str) — new bio text",
            "body": "bio text",
            "returns": "Confirmation text with the performed action details, or an error message.",
            "example": "{\"tool\": \"profile.update_bio\", \"args\": {\"user\": \"@user\", \"about\": \"New description\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "profile.update_username": {
            "desc": "Change your Telegram username",
            "args": "username (str) — new username (without @)",
            "body": "not used",
            "returns": "Confirmation text with the performed action details, or an error message.",
            "example": "{\"tool\": \"profile.update_username\", \"args\": {\"user\": \"@user\", \"username\": \"new_username\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "profile.set_photo": {
            "desc": "Set your profile photo from a file",
            "args": "photo (str) or file (str) — path to image",
            "body": "not used",
            "returns": "Confirmation text with the performed action details, or an error message.",
            "example": "{\"tool\": \"profile.set_photo\", \"args\": {\"user\": \"@user\", \"path\": \"photo.jpg\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "profile.download_photo": {
            "desc": "Download a user's profile photo",
            "args": "target (str) or user (str)",
            "body": "user identifier",
            "returns": "Confirmation text with the performed action details, or an error message.",
            "example": "{\"tool\": \"profile.download_photo\", \"args\": {\"user\": \"@user\", \"path\": \"photo.jpg\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
    }

    tool_map = {
        "profile": "cmd_get",
        "profile.get": "cmd_get",
        "profile.get_full": "cmd_get_full",
        "profile.get_me": "cmd_get_me",
        "profile.get_photos": "cmd_get_photos",
        "profile.common_chats": "cmd_common_chats",
        "profile.download_photo": "cmd_get_photos",
        "update_profile": "cmd_update",
        "profile.update": "cmd_update",
        "profile.update_name": "cmd_update",
        "profile.update_bio": "cmd_update",
        "profile.update_username": "cmd_update",
        "set_profile_photo": "cmd_set_photo",
        "profile.set_photo": "cmd_set_photo",
    }

    def __init__(self, agent: Any) -> None:
        self.agent = agent

    async def cmd_get(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        target = body.strip() or attrs.get("target") or attrs.get("user") or ""
        if not target:
            return "user is required"
        try:
            user = await self.agent.client.get_entity(target)
            lines = [f"ID: {user.id}"]
            if getattr(user, "first_name", None):
                lines.append(f"Name: {user.first_name} {getattr(user, 'last_name', '') or ''}".strip())
            if getattr(user, "username", None):
                lines.append(f"Username: @{user.username}")
            if getattr(user, "phone", None):
                lines.append(f"Phone: {user.phone}")
            if getattr(user, "photo", None):
                lines.append("Has photo")
            return "\n".join(lines)
        except Exception as exc:
            return f"Profile lookup failed: {exc}"

    async def cmd_get_full(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        target = body.strip() or attrs.get("target") or attrs.get("user") or ""
        if not target:
            return "user is required"
        try:
            user = await self.agent.client.get_entity(target)
            full = await self.agent.client(GetFullUserRequest(user.id))
            about = getattr(full.full_user, "about", None) or ""
            common = getattr(full.full_user, "common_chats_count", 0)
            return f"About: {about}\nCommon chats: {common}"
        except Exception as exc:
            return f"Full profile failed: {exc}"

    async def cmd_get_me(self, attrs_raw: str, body: str, source_event: Any) -> str:
        try:
            me = await self.agent.client.get_me()
            lines = [f"ID: {me.id}"]
            if getattr(me, "first_name", None):
                lines.append(f"Name: {me.first_name} {getattr(me, 'last_name', '') or ''}".strip())
            if getattr(me, "username", None):
                lines.append(f"Username: @{me.username}")
            if getattr(me, "phone", None):
                lines.append(f"Phone: {me.phone}")
            return "\n".join(lines)
        except Exception as exc:
            return f"Get me failed: {exc}"

    async def cmd_get_photos(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        target = body.strip() or attrs.get("user") or ""
        try:
            if target:
                user = await self.agent.client.get_entity(target)
            elif source_event:
                user = await source_event.get_sender()
            else:
                user = await self.agent.client.get_me()
            photos = await self.agent.client.get_profile_photos(user)
            return f"Profile photos: {len(photos)}" if photos else "No profile photos"
        except Exception as exc:
            return f"Get photos failed: {exc}"

    async def cmd_common_chats(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        user = await self.agent._resolve_tool_user(attrs.get("user") or body.strip(), source_event)
        limit = max(1, min(int(attrs.get("limit", "20") or 20), 100))
        try:
            chats = await self.agent.client.get_common_chats(user, limit=limit)
            lines = []
            for chat in chats:
                title = getattr(chat, "title", None) or getattr(chat, "first_name", None) or "Unknown"
                username = f"@{chat.username}" if getattr(chat, "username", None) else ""
                lines.append(f"{title} {username} [id={getattr(chat, 'id', None)}]".strip())
            return "\n".join(lines) or "No common chats"
        except Exception as exc:
            return f"Common chats failed: {exc}"

    async def cmd_update(self, attrs_raw: str, body: str) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        first_name = attrs.get("first_name") or attrs.get("first") or ""
        last_name = attrs.get("last_name") or attrs.get("last") or ""
        bio = attrs.get("bio") or attrs.get("about") or ""
        username = attrs.get("username") or attrs.get("user") or ""
        results = []
        if first_name or last_name:
            try:
                await self.agent.client(UpdateProfileRequest(first_name=first_name, last_name=last_name))
                results.append("Name updated")
            except Exception as exc:
                results.append(f"Name failed: {exc}")
        if bio:
            try:
                await self.agent.client(UpdateProfileRequest(about=bio))
                results.append("Bio updated")
            except Exception as exc:
                results.append(f"Bio failed: {exc}")
        if username:
            try:
                await self.agent.client(UpdateUsernameRequest(username=username))
                results.append("Username updated")
            except Exception as exc:
                results.append(f"Username failed: {exc}")
        return "; ".join(results) if results else "Nothing to update"

    async def cmd_set_photo(self, attrs_raw: str, body: str, source_event: Any) -> str:
        import io
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        path_str = attrs.get("path") or attrs.get("file") or body.strip()
        if not path_str:
            reply = await source_event.get_reply_message() if source_event else None
            if reply and reply.media:
                data = await reply.download_media(file=bytes)
                if data:
                    try:
                        await self.agent.client(UploadProfilePhotoRequest(await self.agent.client.upload_file(io.BytesIO(data))))
                        return "Profile photo updated from replied media"
                    except Exception as exc:
                        return f"Set photo failed: {exc}"
            return "path or replied media is required"
        fpath = Path(path_str).expanduser() if isinstance(path_str, str) else Path(path_str)
        if not fpath.is_absolute():
            fpath = Path.cwd() / fpath
        if not fpath.is_file():
            return f"File not found: {fpath}"
        try:
            uploaded = await self.agent.client.upload_file(str(fpath))
            await self.agent.client(UploadProfilePhotoRequest(uploaded))
            return f"Profile photo updated: {fpath.name}"
        except Exception as exc:
            return f"Set photo failed: {exc}"
