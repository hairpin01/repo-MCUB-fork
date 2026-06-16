# scop: inline
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Any


class MessagePlugin:
    name = "message"
    version = "0.2.0"
    author = "@dev_dolbaeb"
    description = "Telegram message tools"

    tool_registry = (
        "message.send_current", "message.send_target", "message.reply", "message.edit", "message.forward",
        "message.delete", "message.pin", "message.react", "message.get", "message.search",
        "message.history", "message.mark_read", "message.typing", "message.schedule", "message.draft",
    )

    dangerous_tools = {
        "message.send_current", "message.send_target", "message.edit",
        "message.forward", "message.delete", "message.pin",
        "message.schedule", "message.draft",
    }

    tool_docs = {
        "message.send_current": {"desc": "Send a message to the current chat", "args": "message (str) or text (str) — content", "body": "message text"},
        "message.send_target": {"desc": "Send a message to a specific chat", "args": "chat (str) or to (str) — target; message (str) or text (str) — content", "body": "message text"},
        "message.edit": {"desc": "Edit a previously sent message", "args": "message (str) or msg (str) — message ID or link", "body": "new text"},
        "message.delete": {"desc": "Delete one or more messages", "args": "ids (str) — comma-separated IDs", "body": "not used"},
        "message.history": {"desc": "Get recent messages from a chat", "args": "chat (str) — optional; limit (int) — max messages (default 20)", "body": "not used"},
        "message.search": {"desc": "Search messages across chats", "args": "q (str) or query (str) — search text; chat (str) — optional scope", "body": "query text"},
        "message.forward": {"desc": "Forward a message to another chat", "args": "from_chat (str); msg_id (int); to (str) — destination", "body": "not used"},
        "message.pin": {"desc": "Pin a message in a chat", "args": "chat (str) — target; message (str) or msg (str) — message ID", "body": "not used"},
        "message.reply": {"desc": "Reply to a message", "args": "chat (str); reply_to (int) — message ID; message (str) — content", "body": "reply text"},
        "message.react": {"desc": "React to a message with an emoji", "args": "chat (str); message (str) or msg (str) — message ID; emoji (str) — reaction", "body": "not used"},
        "message.get": {"desc": "Get a specific message by ID", "args": "chat (str); message (str) or msg (str) — message ID", "body": "not used"},
        "message.mark_read": {"desc": "Mark messages as read in a chat", "args": "chat (str); max_id (int) — optional", "body": "not used"},
        "message.typing": {"desc": "Show typing indicator in a chat", "args": "chat (str) — target chat", "body": "not used"},
        "message.schedule": {"desc": "Schedule a message for later", "args": "chat (str); message (str) — content; schedule (int) — unix timestamp", "body": "message text"},
        "message.draft": {"desc": "Save or update a draft message", "args": "chat (str); message (str) — draft text", "body": "draft text"},
    }

    tool_map = {
        "send_message": "cmd_send",
        "message.send": "cmd_send",
        "message.send_current": "cmd_send",
        "message.send_target": "cmd_send",
        "history": "cmd_history",
        "message.history": "cmd_history",
        "search_messages": "cmd_search",
        "message.search": "cmd_search",
        "message.delete": "cmd_delete",
        "delete_messages": "cmd_delete",
        "message.forward": "cmd_forward",
        "forward_message": "cmd_forward",
        "message.pin": "cmd_pin",
        "pin_message": "cmd_pin",
        "message.edit": "cmd_misc",
        "message.reply": "cmd_misc",
        "message.react": "cmd_misc",
        "message.get": "cmd_misc",
        "message.mark_read": "cmd_misc",
        "message.typing": "cmd_misc",
        "message.schedule": "cmd_misc",
        "message.draft": "cmd_misc",
    }

    _MISC = {
        "message.edit": "edit_message",
        "message.reply": "reply_message",
        "message.react": "react_message",
        "message.get": "get_message",
        "message.mark_read": "mark_read",
        "message.typing": "typing",
        "message.schedule": "schedule_message",
        "message.draft": "save_draft",
    }

    def __init__(self, agent: Any) -> None:
        self.agent = agent

    async def cmd_send(self, tool_name: str, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        chat = attrs.get("chat") or attrs.get("to") or attrs.get("target")
        if tool_name == "message.send_current":
            chat = None
        message = body.strip() or attrs.get("message") or attrs.get("text") or ""
        if not message:
            return "message text is required"
        try:
            if chat:
                target = await self.agent._resolve_tool_chat(chat, source_event)
                msg = await self.agent.client.send_message(target, message)
                return f"Sent to {chat}: {message[:200]}"
            else:
                msg = await self.agent.client.send_message(source_event.chat_id, message, reply_to=source_event.id if source_event else None)
                return f"Sent: {message[:200]}"
        except Exception as exc:
            return f"Send failed: {exc}"

    async def cmd_history(self, attrs_raw: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        limit = max(1, min(int(attrs.get("limit", "20") or 20), 100))
        chat = await self.agent._resolve_tool_chat(attrs.get("chat"), source_event)
        lines = []
        try:
            async for msg in self.agent.client.iter_messages(chat, limit=limit):
                sender = await msg.get_sender()
                name = self.agent._format_sender_short(sender)
                text = getattr(msg, "raw_text", None) or getattr(msg, "text", "") or ""
                media = " [media]" if getattr(msg, "media", None) else ""
                lines.append(f"#{msg.id} {name}: {text[:500]}{media}".strip())
        except Exception as exc:
            return f"History failed: {exc}"
        return "\n".join(reversed(lines)) or "No messages"

    async def cmd_search(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        query = attrs.get("query") or body.strip()
        if not query:
            return "Search query is empty"
        limit = max(1, min(int(attrs.get("limit", "20") or 20), 100))
        chat = await self.agent._resolve_tool_chat(attrs.get("chat") or attrs.get("chat_id"), source_event)
        lines = []
        try:
            async for msg in self.agent.client.iter_messages(chat, search=query, limit=limit):
                sender = await msg.get_sender()
                name = self.agent._format_sender_short(sender)
                text = getattr(msg, "raw_text", None) or getattr(msg, "text", "") or ""
                lines.append(f"#{msg.id} {name}: {text[:500]}")
        except Exception as exc:
            return f"Search failed: {exc}"
        return "\n".join(lines) or "No messages found"

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

    async def cmd_forward(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        msg_id = attrs.get("message") or attrs.get("msg") or ""
        src = await self.agent._resolve_tool_chat(attrs.get("from") or attrs.get("src"), source_event)
        dst = await self.agent._resolve_tool_chat(attrs.get("to") or attrs.get("dst") or body.strip(), source_event)
        try:
            if msg_id and str(msg_id).isdigit():
                msg = await self.agent.client.get_messages(src, ids=int(msg_id))
                await self.agent.client.forward_messages(dst, msg)
                return f"Message #{msg_id} forwarded"
            reply = await source_event.get_reply_message() if source_event else None
            if reply:
                await self.agent.client.forward_messages(dst, reply)
                return "Replied message forwarded"
            return "message id or reply is needed"
        except Exception as exc:
            return f"Forward failed: {exc}"

    async def cmd_pin(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        msg_id = attrs.get("message") or attrs.get("msg") or body.strip()
        chat = await self.agent._resolve_tool_chat(attrs.get("chat") or attrs.get("to"), source_event)
        try:
            if msg_id and str(msg_id).isdigit():
                msg = await self.agent.client.get_messages(chat, ids=int(msg_id))
            else:
                msg = await source_event.get_reply_message() if source_event else None
            if not msg:
                return "Message not found"
            await self.agent.client.pin_message(chat, msg.id)
            return "Message pinned"
        except Exception as exc:
            return f"Pin failed: {exc}"

    async def cmd_misc(self, tool_name: str, attrs_raw: str, body: str, source_event: Any) -> str:
        op = self._MISC.get(tool_name, tool_name)
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        try:
            if op == "edit_message":
                chat = await self.agent._resolve_tool_chat(attrs.get("chat") or attrs.get("to"), source_event)
                msg_id = attrs.get("message") or attrs.get("msg") or ""
                text = body.strip() or attrs.get("text") or attrs.get("message") or ""
                if not text:
                    return "text is required"
                if msg_id and str(msg_id).isdigit():
                    msg = await self.agent.client.get_messages(chat, ids=int(msg_id))
                    await msg.edit(text)
                    return f"Message #{msg_id} edited"
                reply = await source_event.get_reply_message() if source_event else None
                if reply:
                    await reply.edit(text)
                    return "Replied message edited"
                return "message id or reply needed"
            
            elif op == "reply_message":
                chat = await self.agent._resolve_tool_chat(attrs.get("chat") or attrs.get("to"), source_event)
                text = body.strip() or attrs.get("text") or attrs.get("message") or ""
                msg_id = attrs.get("message") or attrs.get("msg") or ""
                if not text:
                    return "reply text is required"
                if msg_id and str(msg_id).isdigit():
                    msg = await self.agent.client.get_messages(chat, ids=int(msg_id))
                    await self.agent.client.send_message(chat, text, reply_to=msg.id)
                    return f"Replied to #{msg_id}"
                reply = await source_event.get_reply_message() if source_event else None
                if reply:
                    await self.agent.client.send_message(chat, text, reply_to=reply.id)
                    return "Replied"
                return "message id or reply needed"
            
            elif op == "react_message":
                chat = await self.agent._resolve_tool_chat(attrs.get("chat") or attrs.get("to"), source_event)
                msg_id = attrs.get("message") or attrs.get("msg") or ""
                emoji = attrs.get("emoji") or attrs.get("reaction") or body.strip() or "👍"
                try:
                    if msg_id and str(msg_id).isdigit():
                        msg = await self.agent.client.get_messages(chat, ids=int(msg_id))
                    else:
                        msg = await source_event.get_reply_message() if source_event else None
                    if not msg:
                        return "Message not found"
                    await msg.react(emoji)
                    return f"Reacted {emoji}"
                except Exception as exc:
                    return f"React failed: {exc}"
            
            elif op == "get_message":
                chat = await self.agent._resolve_tool_chat(attrs.get("chat") or attrs.get("to"), source_event)
                msg_id = attrs.get("message") or attrs.get("msg") or ""
                if not msg_id or not str(msg_id).isdigit():
                    reply = await source_event.get_reply_message() if source_event else None
                    if reply:
                        msg_id = str(reply.id)
                    else:
                        return "message id or reply needed"
                try:
                    msg = await self.agent.client.get_messages(chat, ids=int(msg_id))
                    if not msg:
                        return "Message not found"
                    sender = await msg.get_sender()
                    name = self.agent._format_sender_short(sender)
                    text = getattr(msg, "raw_text", None) or getattr(msg, "text", "") or ""
                    media = " [media]" if getattr(msg, "media", None) else ""
                    return f"#{msg.id} {name}: {text[:2000]}{media}"
                except Exception as exc:
                    return f"Get message failed: {exc}"
            
            elif op == "mark_read":
                chat = await self.agent._resolve_tool_chat(attrs.get("chat") or body.strip(), source_event)
                try:
                    await self.agent.client.send_read_acknowledge(chat)
                    return "Marked as read"
                except Exception as exc:
                    return f"Mark read failed: {exc}"
            
            elif op == "typing":
                chat = await self.agent._resolve_tool_chat(attrs.get("chat") or body.strip(), source_event)
                try:
                    from telethon.tl.functions.messages import SetTypingRequest
                    from telethon.tl.types import SendMessageTypingAction
                    await self.agent.client(SetTypingRequest(chat, SendMessageTypingAction()))
                    return "Typing signal sent"
                except Exception as exc:
                    return f"Typing failed: {exc}"
            
            elif op == "schedule_message":
                chat = await self.agent._resolve_tool_chat(attrs.get("chat") or attrs.get("to"), source_event)
                text = body.strip() or attrs.get("text") or attrs.get("message") or ""
                schedule_str = attrs.get("schedule") or attrs.get("when") or ""
                if not text or not schedule_str:
                    return "text and schedule time are required"
                from datetime import datetime, timedelta
                try:
                    minutes = int(schedule_str)
                    when = datetime.now() + timedelta(minutes=minutes)
                except ValueError:
                    return "schedule: minutes as integer"
                try:
                    msg = await self.agent.client.send_message(chat, text, schedule=when)
                    return f"Message scheduled for {schedule_str} min"
                except Exception as exc:
                    return f"Schedule failed: {exc}"
            
            elif op == "save_draft":
                chat = await self.agent._resolve_tool_chat(attrs.get("chat") or attrs.get("to"), source_event)
                text = body.strip() or attrs.get("text") or attrs.get("message") or ""
                try:
                    from telethon.tl.functions.messages import SaveDraftRequest
                    await self.agent.client(SaveDraftRequest(peer=chat, message=text))
                    return "Draft saved"
                except Exception as exc:
                    return f"Draft failed: {exc}"
            
            return f"Unknown message op: {op}"
        except Exception as e:
            return f"Message op {op} failed: {e}"
