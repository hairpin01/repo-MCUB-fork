# scop: inline
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Any
from telethon.tl.functions.channels import (
    CreateChannelRequest,
    EditPhotoRequest,
    EditTitleRequest,
    JoinChannelRequest,
    ToggleSlowModeRequest,
    UpdateUsernameRequest,
)
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import ChatAdminRights


class CreationPlugin:
    name = "creation"
    version = "0.2.0"
    author = "@dev_dolbaeb"
    description = "Telegram channel/group/bot creation tools"

    tool_registry = (
        "creation.channel",
        "creation.group",
        "creation.bot",
        "creation.private_invite",
    )

    dangerous_tools = {
        "creation.channel", "creation.group", "creation.bot", "creation.private_invite",
    }

    tool_docs = {
        "creation.channel": {
            "desc": "Create a Telegram channel",
            "args": "title (str) or name (str); about (str) or description (str)",
            "body": "title",
            "returns": "Confirmation text with the performed action details, or an error message.",
            "example": "{\"tool\": \"creation.channel\", \"args\": {\"title\": \"New channel\", \"about\": \"Description\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "creation.group": {
            "desc": "Create a Telegram group",
            "args": "title (str) or name (str); about (str) or description (str)",
            "body": "title",
            "returns": "Confirmation text with the performed action details, or an error message.",
            "example": "{\"tool\": \"creation.group\", \"args\": {\"title\": \"New group\", \"about\": \"Description\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "creation.bot": {
            "desc": "Create a Telegram bot via BotFather",
            "args": "name (str) or title (str); username (str) or bot (str); about (str)",
            "body": "not used",
            "returns": "Confirmation text with the performed action details, or an error message.",
            "example": "{\"tool\": \"creation.bot\", \"args\": {\"name\": \"My Bot\", \"username\": \"my_example_bot\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
        "creation.private_invite": {
            "desc": "Join a chat by invite link",
            "args": "link (str) — invite link",
            "body": "invite link",
            "returns": "Confirmation text with the performed action details, or an error message.",
            "example": "{\"tool\": \"creation.private_invite\", \"args\": {\"link\": \"https://t.me/+invite\"}}",
            "notes": "Requires the current Telegram account to have access and sufficient permissions.",
        },
    }

    tool_map = {
        "create_channel": "cmd_channel_or_group",
        "creation.channel": "cmd_channel_or_group",
        "create_group": "cmd_channel_or_group",
        "creation.group": "cmd_channel_or_group",
        "create_bot": "cmd_bot",
        "creation.bot": "cmd_bot",
        "join_chat": "cmd_join",
        "creation.private_invite": "cmd_join",
    }

    def __init__(self, agent: Any) -> None:
        self.agent = agent

    async def cmd_channel_or_group(self, tool_name: str, attrs_raw: str, body: str) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        kind = "group" if tool_name.endswith("group") else "channel"
        title = attrs.get("title") or attrs.get("name") or body.strip()
        about = attrs.get("about") or attrs.get("description") or ""
        if not title:
            return "Title is required"
        try:
            if kind == "group":
                result = await self.agent.client(CreateChannelRequest(title, about, megagroup=True))
                peer = result.chats[0]
                return f"Group created: @{peer.username if getattr(peer, 'username', None) else peer.id}"
            else:
                result = await self.agent.client(CreateChannelRequest(title, about, megagroup=False))
                peer = result.chats[0]
                return f"Channel created: @{peer.username if getattr(peer, 'username', None) else peer.id}"
        except Exception as exc:
            return f"Creation failed: {exc}"

    async def cmd_bot(self, attrs_raw: str, body: str) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        name = attrs.get("name") or attrs.get("title") or body.strip()
        username = attrs.get("username") or attrs.get("bot") or ""
        about = attrs.get("about") or attrs.get("description") or ""
        if not name or not username:
            return "name and username are required"
        from telethon.tl.functions.bots import CreateBotRequest
        try:
            result = await self.agent.client(CreateBotRequest(bot=username, name=name, about=about))
            token = result.token
            return f"Bot @{username} created. Token: {token}"
        except Exception as exc:
            return f"Bot creation failed: {exc}"

    async def cmd_join(self, attrs_raw: str, body: str) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        target = attrs.get("invite") or attrs.get("chat") or attrs.get("link") or body.strip()
        if not target:
            return "invite link or username is required"
        try:
            if target.startswith(("https://t.me/", "t.me/")):
                parts = target.rstrip("/").split("/")
                target = parts[-1]
                if "joinchat" in target:
                    hash_part = target.split("/")[-1] if "/" in target else target.split("=")[-1] if "=" in target else target
                    await self.agent.client(ImportChatInviteRequest(hash_part))
                    return f"Joined via invite link"
            elif target.startswith("+"):
                await self.agent.client(ImportChatInviteRequest(target[1:]))
                return f"Joined via invite hash"
            else:
                entity = await self.agent.client.get_entity(target)
                await self.agent.client(JoinChannelRequest(entity))
                return f"Joined: {target}"
        except Exception as exc:
            return f"Join failed: {exc}"
