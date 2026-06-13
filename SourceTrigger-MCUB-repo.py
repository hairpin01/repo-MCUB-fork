# repo - https://github.com/hairpin01/repo-MCUB-fork/edit/main/SourceTrigger-MCUB-repo.py
# RnDev - https://t.me/RnPlugins
# scop: kernel min v1.4.0

from __future__ import annotations

import asyncio
import json
import logging
import os
import re
from datetime import datetime, timezone

from telethon import events
from telethon.tl.patched import Message


def _escape_html(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


from core.lib.loader.module_config import (
    Boolean,
    ConfigValue,
    Float,
    Integer,
    ModuleConfig,
)

from core.lib.loader.module_base import (
    ModuleBase,
    command,
    event,
    watcher,
)


logger = logging.getLogger(__name__)


class SourceTriggerMod(ModuleBase):
    name = "SourceTrigger"
    version = "1.1.4-beta"
    author = "@RnPlugins"
    description = {
        "ru": "Отправляет медиа/текст из исходного канала в ответ на текстовые триггеры.",
        "en": "Sends media/text from source channel in response to text triggers.",
    }
    banner_url = 'https://x0.at/NcPW.png'

    strings: dict[str, dict[str, str]] = {
        "ru": {
            "parsing_started": (
                "<emoji document_id=5204189706237004154>\u27a1\ufe0f</emoji> <b>\u0418\u043d\u0434\u0435\u043a\u0441\u0430\u0446\u0438\u044f \u043d\u0430\u0447\u0430\u0442\u0430.</b> "
                "\u0412\u0441\u0435 \u0441\u0442\u0430\u0440\u044b\u0435 \u0442\u0440\u0438\u0433\u0433\u0435\u0440\u044b \u0431\u0443\u0434\u0443\u0442 \u0443\u0434\u0430\u043b\u0435\u043d\u044b, \u043a\u0430\u043d\u0430\u043b \u0431\u0443\u0434\u0435\u0442 \u043f\u0440\u043e\u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d \u0437\u0430\u043d\u043e\u0432\u043e. \u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u043f\u043e\u0434\u043e\u0436\u0434\u0438\u0442\u0435..."
            ),
            "parsing_progress": (
                "<emoji document_id=5429411030960711866>\U0001f4ac</emoji> <b>\u0418\u043d\u0434\u0435\u043a\u0441\u0430\u0446\u0438\u044f \u0432 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435...</b>\n"
                "\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e <b>{}</b> \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0439."
            ),
            "parsing_complete": (
                "<emoji document_id=5260726538302660868>\u2705</emoji> <b>\u0418\u043d\u0434\u0435\u043a\u0441\u0430\u0446\u0438\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0430!</b>\n"
                "\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0439 \u0442\u0440\u0438\u0433\u0433\u0435\u0440\u043e\u0432:\n"
                "<b>{}</b> \u0442\u043e\u0447\u043d\u044b\u0445 (<code>~</code>)\n"
                "<b>{}</b> \u043f\u043e \u0432\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044e (<code>~~</code>)\n"
                "<b>{}</b> \u0442\u043e\u0447\u043d\u044b\u0445+\u0443\u0434\u0430\u043b\u0438\u0442\u044c (<code>~~~</code>)\n"
                "<b>{}</b> regex (<code>~|</code>)\n"
                "<b>{}</b> regex+\u0443\u0434\u0430\u043b\u0438\u0442\u044c (<code>~~~|</code>)"
            ),
            "channel_error": (
                "<emoji document_id=5260342697075416641>\u274c</emoji> <b>\u041e\u0448\u0438\u0431\u043a\u0430 \u0434\u043e\u0441\u0442\u0443\u043f\u0430 \u043a \u043a\u0430\u043d\u0430\u043b\u0443.</b> "
                "\u0423\u0431\u0435\u0434\u0438\u0442\u0435\u0441\u044c, \u0447\u0442\u043e ID \u0443\u043a\u0430\u0437\u0430\u043d \u0432\u0435\u0440\u043d\u043e \u0438 \u0432\u044b \u0441\u043e\u0441\u0442\u043e\u0438\u0442\u0435 \u0432 \u043a\u0430\u043d\u0430\u043b\u0435. "
                "\u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u043f\u0435\u0440\u0435\u0441\u043b\u0430\u0442\u044c \u043b\u044e\u0431\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0438\u0437 \u043d\u0435\u0433\u043e \u0432 '\u0418\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0435'."
            ),
            "add_trigger_error": (
                "<emoji document_id=5258474669769497337>\u2757\ufe0f</emoji> <b>\u041d\u0435 \u0443\u0434\u0430\u043b\u043e\u0441\u044c \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0440\u0438\u0433\u0433\u0435\u0440.</b>\n"
                "\u0423\u0431\u0435\u0434\u0438\u0442\u0435\u0441\u044c, \u0447\u0442\u043e \u0432\u0430\u0448 \u044e\u0437\u0435\u0440\u0431\u043e\u0442 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u043c \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u043a\u0430\u043d\u0430\u043b\u0430 \u0438 \u0438\u043c\u0435\u0435\u0442 \u043f\u0440\u0430\u0432\u0430 \u043d\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0443 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0439."
            ),
            "config_source_channel": "ID \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u043a\u0430\u043d\u0430\u043b\u0430 \u0441 \u0442\u0440\u0438\u0433\u0433\u0435\u0440\u0430\u043c\u0438 \u0438 \u043c\u0435\u0434\u0438\u0430/\u0442\u0435\u043a\u0441\u0442\u043e\u043c.",
            "config_auto_parse_on_start": "\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0437\u0430\u043f\u0443\u0441\u043a\u0430\u0442\u044c \u0438\u043d\u0434\u0435\u043a\u0441\u0430\u0446\u0438\u044e \u043f\u0440\u0438 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0435 \u043c\u043e\u0434\u0443\u043b\u044f.",
            "config_trigger_in_channels": "\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0442\u0440\u0438\u0433\u0433\u0435\u0440\u044b \u0432 \u043a\u0430\u043d\u0430\u043b\u0430\u0445.",
            "config_trigger_in_groups": "\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0442\u0440\u0438\u0433\u0433\u0435\u0440\u044b \u0432 \u0433\u0440\u0443\u043f\u043f\u0430\u0445.",
            "config_trigger_in_pm": "\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0442\u0440\u0438\u0433\u0433\u0435\u0440\u044b \u0432 \u043b\u0438\u0447\u043d\u044b\u0445 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f\u0445 (\u041b\u0421).",
            "config_max_delay": "\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0430 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445 \u0434\u043b\u044f \u0441\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043d\u0438\u044f \u0442\u0440\u0438\u0433\u0433\u0435\u0440\u043e\u0432 \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u0432\u0438\u0441\u0430\u043d\u0438\u044f.",
            "trigger_added": (
                "<emoji document_id=5260726538302660868>\u2705</emoji> <b>\u041d\u043e\u0432\u044b\u0439 \u043e\u0442\u0432\u0435\u0442 \u0434\u043b\u044f \u0442\u0440\u0438\u0433\u0433\u0435\u0440\u0430"
                " <code>{}</code> \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d.</b> <a href='{}'>\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044e</a>."
            ),
            "must_be_reply": "<blockquote><tg-emoji emoji-id=5260450573768990626>\u27a1\ufe0f</tg-emoji> <b>\u041d\u0443\u0436\u043d\u043e \u043e\u0442\u0432\u0435\u0442\u0438\u0442\u044c \u043d\u0430 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435.</b></blockquote>",
            "no_trigger_specified": "<blockquote><tg-emoji emoji-id=5257965174979042426>\U0001f4dd</tg-emoji> <b>\u041d\u0443\u0436\u043d\u043e \u0443\u043a\u0430\u0437\u0430\u0442\u044c \u0442\u0440\u0438\u0433\u0433\u0435\u0440.</b> \u041f\u0440\u0438\u043c\u0435\u0440: <code>.tadd ~\u043f\u0440\u0438\u0432\u0435\u0442</code></blockquote>",
            "invalid_trigger_format": "<blockquote><tg-emoji emoji-id=5260342697075416641>\u274c</tg-emoji> <b>\u041d\u0435\u0432\u0435\u0440\u043d\u044b\u0439 \u0444\u043e\u0440\u043c\u0430\u0442 \u0442\u0440\u0438\u0433\u0433\u0435\u0440\u0430.</b> \u0414\u043e\u043b\u0436\u0435\u043d \u043d\u0430\u0447\u0438\u043d\u0430\u0442\u044c\u0441\u044f \u0441 <code>~</code>, <code>~~</code>, \u0438\u043b\u0438 <code>~~~</code>.</blockquote>",
            "processing_add": "<emoji document_id=5427181942934088912>\U0001f4ac</emoji> <b>\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430...</b>",
            "empty_response": "<b>\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435-\u043e\u0442\u0432\u0435\u0442 \u043f\u0443\u0441\u0442\u043e\u0435 \u0438 \u043d\u0435 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043c\u0435\u0434\u0438\u0430.</b>",
            "search_progress": "<tg-emoji emoji-id=5425000812512308882>\u2708\ufe0f</tg-emoji> <b>\u041f\u043e\u0438\u0441\u043a...</b>",
            "search_no_results": "<b>\u041f\u043e \u0437\u0430\u043f\u0440\u043e\u0441\u0443 \u00ab<code>{}</code>\u00bb \u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449\u0438\u0445 \u0442\u0440\u0438\u0433\u0433\u0435\u0440\u043e\u0432 \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u043e.</b>",
            "invalid_search_query": "<b>\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u043f\u0440\u043e\u0441 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u0442\u0440\u0438\u0433\u0433\u0435\u0440\u043e\u0432.</b> \u041f\u0440\u0438\u043c\u0435\u0440: <code>tsearch \u043f\u0440\u0438\u0432\u0435\u0442</code>",
            "ignore_invalid_chat": "<b>\u041d\u0435\u0432\u0435\u0440\u043d\u044b\u0439 ID \u0447\u0430\u0442\u0430 \u0438\u043b\u0438 \u044e\u0437\u0435\u0440\u043d\u0435\u0439\u043c.</b>",
            "ignore_no_chat": "<b>\u041d\u0435 \u0443\u0434\u0430\u043b\u043e\u0441\u044c \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c ID \u0447\u0430\u0442\u0430.</b>",
            "ignore_removed": "<b>\u0427\u0430\u0442 <code>{}</code> \u0443\u0434\u0430\u043b\u0435\u043d \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430 \u0438\u0441\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0439.</b>",
            "ignore_added": "<b>\u0427\u0430\u0442 <code>{}</code> \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d \u0432 \u0441\u043f\u0438\u0441\u043e\u043a \u0438\u0441\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0439.</b>",
            "source_set": "<b>\u0427\u0430\u0442 <code>{}</code> \u0443\u0441\u043f\u0435\u0448\u043d\u043e \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d \u0432 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430 \u0442\u0440\u0438\u0433\u0433\u0435\u0440\u043e\u0432.</b>",
        },
        "en": {
            "parsing_started": "<emoji document_id=5204189706237004154>\u27a1\ufe0f</emoji> <b>Parsing started.</b> This will clear all old triggers and scan the channel from scratch. Please wait...",
            "parsing_progress": "<emoji document_id=5429411030960711866>\U0001f4ac</emoji> <b>Parsing in progress...</b>\nProcessed <b>{}</b> messages.",
            "parsing_complete": (
                "<emoji document_id=5260726538302660868>\u2705</emoji> <b>Parsing complete!</b>\n"
                "Parsed trigger definitions:\n"
                "<b>{}</b> exact (<code>~</code>)\n"
                "<b>{}</b> contains (<code>~~</code>)\n"
                "<b>{}</b> exact+del (<code>~~~</code>)\n"
                "<b>{}</b> regex (<code>~|</code>)\n"
                "<b>{}</b> regex+del (<code>~~~|</code>)"
            ),
            "channel_error": "<emoji document_id=5260342697075416641>\u274c</emoji> <b>Error accessing channel.</b> Make sure the ID is correct and you are a member of the channel. Try forwarding any message from it to your Saved Messages.",
            "add_trigger_error": "<emoji document_id=5258474669769497337>\u2757\ufe0f</emoji> <b>Failed to add trigger.</b>\nMake sure your userbot is a member of the source channel and has permission to post messages.",
            "config_source_channel": "ID of the source channel with triggers and media/text.",
            "config_auto_parse_on_start": "Automatically run parsing when the module loads.",
            "config_trigger_in_channels": "Enable triggers in channels.",
            "config_trigger_in_groups": "Enable triggers in groups.",
            "config_trigger_in_pm": "Enable triggers in private messages (PM).",
            "config_max_delay": "Maximum delay in seconds for trigger execution after network lag.",
            "trigger_added": "<emoji document_id=5260726538302660868>\u2705</emoji> <b>New response for trigger <code>{}</code> added.</b> <a href='{}'>Go to message</a>.",
            "must_be_reply": "<blockquote><tg-emoji emoji-id=5260450573768990626>\u27a1\ufe0f</tg-emoji> <b>You must reply to a message.</b></blockquote>",
            "no_trigger_specified": "<blockquote><tg-emoji emoji-id=5257965174979042426>\U0001f4dd</tg-emoji> <b>You must specify a trigger.</b> Example: <code>.tadd ~hi</code></blockquote>",
            "invalid_trigger_format": "<blockquote><tg-emoji emoji-id=5260342697075416641>\u274c</tg-emoji> <b>Invalid trigger format.</b> Must start with <code>~</code>, <code>~~</code>, or <code>~~~</code>.</blockquote>",
            "processing_add": "<emoji document_id=5427181942934088912>\U0001f4ac</emoji> <b>Processing...</b>",
            "empty_response": "<b>Reply message is empty and has no media.</b>",
            "search_progress": "<tg-emoji emoji-id=5425000812512308882>\u2708\ufe0f</tg-emoji> <b>Searching...</b>",
            "search_no_results": "<b>No triggers found for query \u00ab<code>{}</code>\u00bb.</b>",
            "invalid_search_query": "<b>Enter a search query.</b> Example: <code>tsearch hello</code>",
            "ignore_invalid_chat": "<b>Invalid chat ID or username.</b>",
            "ignore_no_chat": "<b>Could not determine chat ID.</b>",
            "ignore_removed": "<b>Chat <code>{}</code> removed from ignore list.</b>",
            "ignore_added": "<b>Chat <code>{}</code> added to ignore list.</b>",
            "source_set": "<b>Chat <code>{}</code> set as trigger source.</b>",
        },
    }

    config = ModuleConfig(
        ConfigValue(
            "source_channel_id",
            0,
            description="ID исходного канала с триггерами и медиа/текстом.",
            validator=Integer(default=0),
        ),
        ConfigValue(
            "allow_incoming",
            True,
            description="",
            validator=Boolean(default=True),
            hidden=True,
        ),
        ConfigValue(
            "auto_parse_on_start",
            True,
            description="Автоматически запускать индексацию при загрузке модуля.",
            validator=Boolean(default=True),
        ),
        ConfigValue(
            "trigger_in_channels",
            False,
            description="Включить триггеры в каналах.",
            validator=Boolean(default=False),
        ),
        ConfigValue(
            "trigger_in_groups",
            True,
            description="Включить триггеры в группах.",
            validator=Boolean(default=True),
        ),
        ConfigValue(
            "trigger_in_pm",
            True,
            description="Включить триггеры в личных сообщениях (ЛС).",
            validator=Boolean(default=True),
        ),
        ConfigValue(
            "max_delay",
            3.0,
            description="Максимальная задержка в секундах для срабатывания триггеров после зависания.",
            validator=Float(default=3.0, min=0.0),
        ),
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.triggers: dict[str, list[dict | int]] = {}
        self.BATCH_SIZE: int = 200
        self._edited_msg_ids: set[int] = set()
        self._outgoing_text_cache: dict[int, tuple[str, datetime]] = {}
        self.me = None

    def _prune_outgoing_text_cache(self, now: datetime | None = None) -> None:
        now = now or datetime.now(timezone.utc)
        cutoff = now.timestamp() - 600
        for msg_id, (_, ts) in list(self._outgoing_text_cache.items()):
            if ts.timestamp() < cutoff:
                self._outgoing_text_cache.pop(msg_id, None)

    def _remember_outgoing_text(self, message: Message) -> None:
        if not message or not message.out:
            return
        text = (message.raw_text or message.text or "").strip()
        if not text:
            return
        ts = message.date or datetime.now(timezone.utc)
        self._prune_outgoing_text_cache(ts)
        self._outgoing_text_cache[message.id] = (text, ts)

    def _cached_outgoing_text(self, message_id: int) -> str | None:
        cached = self._outgoing_text_cache.get(message_id)
        return cached[0] if cached else None

    async def _get_ignored_chats(self) -> list:
        raw = await self.db.db_get(self.name, "ignored_chats")
        if raw is None:
            return []
        if isinstance(raw, str):
            try:
                return json.loads(raw) or []
            except (json.JSONDecodeError, TypeError):
                return []
        if isinstance(raw, list):
            return raw
        return []

    async def _persist_config(self) -> None:
        try:
            config_dict = await self.kernel.get_module_config(
                self.name, self.config.to_dict()
            )
            cleaned = {k: v for k, v in config_dict.items() if v is not None}
            self.config.from_dict(cleaned)
            self.kernel.store_module_config_schema(self.name, self.config)
        except Exception as e:
            logger.warning(f"Failed to persist config: {e}")

    async def on_load(self) -> None:
        await self._persist_config()
        await self._load_triggers()
        try:
            self.me = await self.client.get_me()
        except Exception as e:
            logger.error(f"Failed to cache self entity: {e}")
        installed = await self.db.db_get(self.name, "installed_notified")
        if not installed:
            await self.db.db_set(self.name, "installed_notified", True)
            try:
                await self.client.send_message("me", (
                    '<blockquote><tg-emoji emoji-id=5424678651310404309>\U0001f319</tg-emoji>'
                    ' \u0412\u044b \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u043b\u0438 \u043c\u043e\u0434\u0443\u043b\u044c "SourceTrigger"!</blockquote>\n'
                    '<blockquote><tg-emoji emoji-id=5424865813100260137>\U0001f310</tg-emoji>'
                    ' \u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e - <a href="https://stm.yufic.ru">stm.yufic.ru</a></blockquote>\n'
                    '<blockquote><tg-emoji emoji-id=5424767119046766924>\u27a1\ufe0f</tg-emoji>'
                    ' \u041f\u0440\u0438\u044f\u0442\u043d\u043e\u0433\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044f!</blockquote>'
                ), parse_mode="html", disable_web_page_preview=True)
            except Exception as e:
                logger.error(f"Failed to send welcome message: {e}")
        should_parse = True
        last_parse_str = await self.db.db_get(self.name, "last_parse_time")
        if last_parse_str:
            try:
                last_parse = datetime.fromisoformat(last_parse_str)
                if (datetime.now(timezone.utc) - last_parse).total_seconds() < 7200:
                    should_parse = False
            except Exception as e:
                logger.error(f"Error parsing last_parse_time: {e}")
        if self.config["auto_parse_on_start"] and should_parse:
            logger.info("Auto-parsing triggers on startup launched in background...")
            asyncio.create_task(self._run_parser(event=None))

    async def on_unload(self) -> None:
        pass

    @event("messageedited")
    async def on_message_edited(self, event: events.MessageEdited.Event) -> None:
        message = getattr(event, "message", None)
        if not message or not message.out or not message.text:
            return
        if not getattr(message, "edit_date", None):
            return
        if (datetime.now(timezone.utc) - message.date).total_seconds() > 300:
            return
        current_text = (message.raw_text or message.text or "").strip()
        cached_text = self._cached_outgoing_text(message.id)
        if cached_text is not None and cached_text == current_text:
            return
        self._edited_msg_ids.add(message.id)
        try:
            matched = self._find_match(message.raw_text)
            if matched:
                key, match_obj = matched
                should_delete = "delete" in key.split("::", 1)[0]
                entries = self.triggers.get(key, [])
                proxy = self.kernel.register.message_proxy(msg=message, original_event=event)
                tasks = [
                    self._process_and_send(proxy, e["content_id"] if isinstance(e, dict) else e, should_delete, match_obj)
                    for e in entries
                ]
                await asyncio.gather(*tasks)
        finally:
            self._edited_msg_ids.discard(message.id)
            self._remember_outgoing_text(message)

    def _get_data_path(self) -> str:
        try:
            return os.path.join(os.path.dirname(__file__), "sourcetrigger_data.json")
        except Exception:
            return "sourcetrigger_data.json"

    async def _load_triggers(self) -> None:
        path = self._get_data_path()
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    self.triggers = json.load(f)
                self._migrate_triggers()
                await self.db.db_set(self.name, "triggers", self.triggers)
                return
            except Exception as e:
                logger.error(f"Error loading triggers from file: {e}")
        db_triggers = await self.db.db_get(self.name, "triggers")
        self.triggers = db_triggers if db_triggers else {}
        self._migrate_triggers()
        await self._save_triggers()

    def _migrate_triggers(self) -> None:
        updated = False
        for key in list(self.triggers.keys()):
            items = self.triggers[key]
            new_items: list[dict] = []
            for item in items:
                if isinstance(item, int):
                    new_items.append({"content_id": item, "trigger_id": None})
                    updated = True
                elif isinstance(item, dict) and "content_id" in item:
                    new_items.append(item)
            if updated:
                self.triggers[key] = new_items

    async def _save_triggers(self) -> None:
        await self.db.db_set(self.name, "triggers", self.triggers)
        path = self._get_data_path()
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.triggers, f, ensure_ascii=False, indent=4)
        except Exception as e:
            logger.error(f"Error saving triggers to file: {e}")

    async def _process_message_for_triggers(self, msg: Message) -> tuple[str, str, int, int] | None:
        if not msg or not getattr(msg, "text", None):
            return None
        trigger_def_msg = msg
        content_msg = msg
        if msg.is_reply:
            replied = await msg.get_reply_message()
            if replied:
                content_msg = replied
            else:
                return None
        text = trigger_def_msg.text.strip()
        first_line = text.split("\n", 1)[0].strip()
        ttype: str | None = None
        trigger: str | None = None
        if re.match(r"^~{1,3}", first_line):
            if first_line.startswith("~~~"):
                ca = first_line[3:].lstrip()
                if ca.startswith("|"):
                    p = ca[1:].strip()
                    if p:
                        try:
                            re.compile(p, re.IGNORECASE)
                            ttype, trigger = "regex_delete", p
                        except re.error:
                            pass
                else:
                    ttype, trigger = "exact_delete", ca.strip().lower()
            elif first_line.startswith("~~"):
                ttype, trigger = "contains", first_line[2:].strip().lower()
            elif first_line.startswith("~"):
                ca = first_line[1:].lstrip()
                if ca.startswith("|"):
                    p = ca[1:].strip()
                    if p:
                        try:
                            re.compile(p, re.IGNORECASE)
                            ttype, trigger = "regex", p
                        except re.error:
                            pass
                else:
                    ttype, trigger = "exact", ca.strip().lower()
        if ttype and trigger:
            return ttype, trigger, content_msg.id, trigger_def_msg.id
        return None

    def _parse_trigger_string(self, text: str) -> tuple[str | None, str | None]:
        text = text.strip()
        if text.startswith("~~~"):
            ca = text[3:].lstrip()
            if ca.startswith("|"):
                p = ca[1:].strip()
                if p:
                    try:
                        re.compile(p, re.IGNORECASE)
                        return "regex_delete", p
                    except re.error:
                        return None, None
            return "exact_delete", ca.strip().lower()
        elif text.startswith("~~"):
            return "contains", text[2:].strip().lower()
        elif text.startswith("~"):
            ca = text[1:].lstrip()
            if ca.startswith("|"):
                p = ca[1:].strip()
                if p:
                    try:
                        re.compile(p, re.IGNORECASE)
                        return "regex", p
                    except re.error:
                        return None, None
            return "exact", ca.strip().lower()
        return None, None

    def _find_match(self, text: str) -> tuple[str, re.Match | None] | None:
        low = text.strip().lower()
        for key in self.triggers:
            if key.startswith("regex_delete::"):
                try:
                    m = re.fullmatch(key.split("::", 1)[1], text, re.IGNORECASE)
                    if m:
                        return key, m
                except re.error:
                    continue
        edk = f"exact_delete::{low}"
        if edk in self.triggers:
            return edk, None
        for key in self.triggers:
            if key.startswith("regex::"):
                try:
                    m = re.fullmatch(key.split("::", 1)[1], text, re.IGNORECASE)
                    if m:
                        return key, m
                except re.error:
                    continue
        ek = f"exact::{low}"
        if ek in self.triggers:
            return ek, None
        for key in self.triggers:
            if key.startswith("contains::"):
                if key.split("::", 1)[1] in text.lower():
                    return key, None
        return None

    def _find_matching_triggers(self, text: str) -> list[tuple[str, str, str]]:
        low = text.strip().lower()
        matched: list[tuple[str, str, str]] = []
        for key in self.triggers:
            parts = key.split("::", 1)
            if len(parts) != 2:
                continue
            ttype, trigger = parts
            match = False
            if ttype in ("regex", "regex_delete"):
                try:
                    if re.fullmatch(trigger, text, re.IGNORECASE):
                        match = True
                except re.error:
                    pass
            elif ttype in ("exact", "exact_delete"):
                if trigger == low:
                    match = True
            elif ttype == "contains":
                if trigger in text.lower():
                    match = True
            if match:
                matched.append((key, ttype, trigger))
        return matched

    async def _process_batch(self, tasks, triggers_dict, counts_dict, status_event, total_processed):
        results = await asyncio.gather(*tasks)
        for result in results:
            if not result:
                continue
            ttype, trigger, content_id, trigger_id = result
            key = f"{ttype}::{trigger}"
            if key not in triggers_dict:
                triggers_dict[key] = []
            exists = any(
                (isinstance(e, dict) and e["content_id"] == content_id)
                or (isinstance(e, int) and e == content_id)
                for e in triggers_dict[key]
            )
            if not exists:
                triggers_dict[key].append({"content_id": content_id, "trigger_id": trigger_id})
            counts_dict[ttype] += 1
        if status_event and total_processed % (self.BATCH_SIZE * 5) == 0:
            try:
                await self.edit(status_event, self.strings("parsing_progress").format(total_processed), as_html=True)
            except Exception:
                pass

    async def _run_parser(self, event: events.NewMessage.Event | None = None) -> None:
        if event:
            await self.edit(event, self.strings("parsing_started"), as_html=True)
        self.triggers.clear()
        counts = {"exact": 0, "contains": 0, "exact_delete": 0, "regex": 0, "regex_delete": 0}
        source_id = self.config["source_channel_id"]
        if not source_id:
            if event:
                await self.edit(event, self.strings("channel_error") + "\n<code>Source channel ID not configured.</code>", as_html=True)
            return
        try:
            channel_entity = await self.client.get_entity(source_id)
            tasks = []
            processed_count = 0
            async for msg in self.client.iter_messages(channel_entity, limit=None):
                tasks.append(asyncio.create_task(self._process_message_for_triggers(msg)))
                processed_count += 1
                if len(tasks) >= self.BATCH_SIZE:
                    await self._process_batch(tasks, self.triggers, counts, event, processed_count)
                    tasks.clear()
            if tasks:
                await self._process_batch(tasks, self.triggers, counts, event, processed_count)
            await self._save_triggers()
            await self.db.db_set(self.name, "last_parse_time", datetime.now(timezone.utc).isoformat())
            if event:
                await self.edit(
                    event,
                    self.strings("parsing_complete").format(
                        counts["exact"], counts["contains"], counts["exact_delete"], counts["regex"], counts["regex_delete"]
                    ),
                    as_html=True,
                )
        except Exception as e:
            logger.exception("Failed to parse triggers")
            if event:
                await self.edit(event, self.strings("channel_error") + f"\n<code>{_escape_html(str(e))}</code>", as_html=True)

    def _replace_placeholders_fast(self, text: str, trigger_msg: Message | None = None, match_obj: re.Match | None = None) -> str:
        if not text:
            return text
        placeholders = {}
        now = datetime.now()
        MONTHS_SHORT = ["янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
        MONTHS_FULL = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
        WEEKDAYS_SHORT = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
        WEEKDAYS_FULL = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
        placeholders["hour"] = now.strftime("%H")
        placeholders["minute"] = now.strftime("%M")
        placeholders["second"] = now.strftime("%S")
        placeholders["day"] = now.strftime("%d")
        placeholders["year"] = now.strftime("%Y")
        placeholders["month"] = now.strftime("%m")
        mi = now.month - 1
        for k, v in [("month_short_lower", MONTHS_SHORT[mi]), ("month_short_title", MONTHS_SHORT[mi].title()),
                     ("month_short_upper", MONTHS_SHORT[mi].upper()),
                     ("month_full_lower", MONTHS_FULL[mi]), ("month_full_title", MONTHS_FULL[mi].title()),
                     ("month_full_upper", MONTHS_FULL[mi].upper())]:
            placeholders[k] = v
        wi = now.weekday()
        for k, v in [("weekday_num", str(wi + 1)), ("weekday_short_lower", WEEKDAYS_SHORT[wi]),
                     ("weekday_short_title", WEEKDAYS_SHORT[wi].title()), ("weekday_short_upper", WEEKDAYS_SHORT[wi].upper()),
                     ("weekday_full_lower", WEEKDAYS_FULL[wi]), ("weekday_full_title", WEEKDAYS_FULL[wi].title()),
                     ("weekday_full_upper", WEEKDAYS_FULL[wi].upper())]:
            placeholders[k] = v
        if "{total_triggers}" in text:
            placeholders["total_triggers"] = str(len(self.triggers))
        if "{sent_count}" in text:
            sc = asyncio.run_coroutine_threadsafe(self.db.db_get(self.name, "sent_count"), self.client.loop).result()
            placeholders["sent_count"] = str(sc or 0)
        if trigger_msg:
            t = trigger_msg.text or ""
            for k in ("message", "msg", "message_text"):
                placeholders[k] = t
        if match_obj:
            for i, gv in enumerate(match_obj.groups(), 1):
                v = gv or ""
                placeholders[f"msg-{i}"] = v
                placeholders[f"message-{i}"] = v
            placeholders["msg-0"] = match_obj.group(0) or ""
            placeholders["message-0"] = match_obj.group(0) or ""
            for gn, gv in match_obj.groupdict().items():
                v = gv or ""
                placeholders[gn] = v
                placeholders[f"msg-{gn}"] = v
                placeholders[f"message-{gn}"] = v
        is_premium = bool(self.me and getattr(self.me, "premium", False))
        loading = "<tg-emoji emoji-id=5425141893598046671>\U0001f4e4</tg-emoji>" if is_premium else "Загрузка..."

        def replacer(m: re.Match) -> str:
            name = m.group(1)
            default = m.group(2) if m.group(2) is not None else ""
            if name in placeholders:
                return placeholders[name]
            if name.startswith("msg-") or name.startswith("message-"):
                return default
            if m.group(2) is not None:
                return default
            return loading
        for _ in range(3):
            if "{" not in text:
                break
            text = re.sub(r"\{([a-zA-Z0-9_-]+)(?::([^{}]*(?:\{[^{}]+\}[^{}]*)*))?\}", replacer, text)
        return text

    def _has_slow_placeholders(self, text: str) -> bool:
        if not text:
            return False
        matches = re.findall(r"\{([a-zA-Z0-9_-]+)(?::([^{}]*(?:\{[^{}]+\}[^{}]*)*))?\}", text)
        fast = {
            "total_triggers", "sent_count", "hour", "minute", "second", "day", "year", "month",
            "month_short_lower", "month_short_title", "month_short_upper",
            "month_full_lower", "month_full_title", "month_full_upper",
            "weekday_num", "weekday_short_lower", "weekday_short_title", "weekday_short_upper",
            "weekday_full_lower", "weekday_full_title", "weekday_full_upper",
            "message", "msg", "message_text",
        }
        for name, default in matches:
            if default and self._has_slow_placeholders(default):
                return True
            if name.startswith("msg-") or name.startswith("message-"):
                continue
            if name not in fast:
                return True
        return False

    async def _replace_placeholders(
        self, text: str, event_obj=None, match_obj: re.Match | None = None
    ) -> str:
        if not text:
            return text
        placeholders = {}
        now = datetime.now()
        MONTHS_SHORT = ["янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
        MONTHS_FULL = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
        WEEKDAYS_SHORT = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
        WEEKDAYS_FULL = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
        placeholders["hour"] = now.strftime("%H")
        placeholders["minute"] = now.strftime("%M")
        placeholders["second"] = now.strftime("%S")
        placeholders["day"] = now.strftime("%d")
        placeholders["year"] = now.strftime("%Y")
        placeholders["month"] = now.strftime("%m")
        mi = now.month - 1
        for k, v in [("month_short_lower", MONTHS_SHORT[mi]), ("month_short_title", MONTHS_SHORT[mi].title()),
                     ("month_short_upper", MONTHS_SHORT[mi].upper()),
                     ("month_full_lower", MONTHS_FULL[mi]), ("month_full_title", MONTHS_FULL[mi].title()),
                     ("month_full_upper", MONTHS_FULL[mi].upper())]:
            placeholders[k] = v
        wi = now.weekday()
        for k, v in [("weekday_num", str(wi + 1)), ("weekday_short_lower", WEEKDAYS_SHORT[wi]),
                     ("weekday_short_title", WEEKDAYS_SHORT[wi].title()), ("weekday_short_upper", WEEKDAYS_SHORT[wi].upper()),
                     ("weekday_full_lower", WEEKDAYS_FULL[wi]), ("weekday_full_title", WEEKDAYS_FULL[wi].title()),
                     ("weekday_full_upper", WEEKDAYS_FULL[wi].upper())]:
            placeholders[k] = v
        if "{total_triggers}" in text:
            placeholders["total_triggers"] = str(len(self.triggers))
        if "{sent_count}" in text:
            sc = await self.db.db_get(self.name, "sent_count") or 0
            placeholders["sent_count"] = str(sc)
        msg = event_obj.message if event_obj else None
        if msg:
            t = msg.text or ""
            for k in ("message", "msg", "message_text"):
                placeholders[k] = t
        if match_obj:
            for i, gv in enumerate(match_obj.groups(), 1):
                v = gv or ""
                placeholders[f"msg-{i}"] = v
                placeholders[f"message-{i}"] = v
            placeholders["msg-0"] = match_obj.group(0) or ""
            placeholders["message-0"] = match_obj.group(0) or ""
            for gn, gv in match_obj.groupdict().items():
                v = gv or ""
                placeholders[gn] = v
                placeholders[f"msg-{gn}"] = v
                placeholders[f"message-{gn}"] = v
        if "{owner_username}" in text:
            if not self.me:
                try:
                    self.me = await self.client.get_me()
                except Exception:
                    self.me = None
            placeholders["owner_username"] = (
                getattr(self.me, "username", None) or getattr(self.me, "first_name", None) or ""
            ) if self.me else ""
        matches = re.findall(r"\{([a-zA-Z0-9_-]+)(?::([^{}]*(?:\{[^{}]+\}[^{}]*)*))?\}", text)
        needed = {m[0] for m in matches}
        if "reply_username" in needed and msg:
            reply_user = None
            try:
                if msg.is_reply:
                    replied = await msg.get_reply_message()
                    if replied:
                        reply_user = await self.client.get_entity(replied.sender_id)
                elif msg.is_private:
                    reply_user = await self.client.get_entity(msg.peer_id)
            except Exception:
                pass
            placeholders["reply_username"] = (
                getattr(reply_user, "username", None) or getattr(reply_user, "first_name", None) or ""
            ) if reply_user else ""
        if "cur_chat_username" in needed and msg:
            try:
                chat = await self.client.get_entity(msg.peer_id)
                placeholders["cur_chat_username"] = getattr(chat, "username", None) or ""
            except Exception:
                placeholders["cur_chat_username"] = ""
        if "cur_chat_name" in needed and msg:
            try:
                chat = await self.client.get_entity(msg.peer_id)
                cn = getattr(chat, "title", None)
                if not cn:
                    fn = getattr(chat, "first_name", "") or ""
                    ln = getattr(chat, "last_name", "") or ""
                    cn = f"{fn} {ln}".strip()
                placeholders["cur_chat_name"] = cn
            except Exception:
                placeholders["cur_chat_name"] = ""
        if ("reply_firstname" in needed or "reply_lastname" in needed) and msg:
            reply_user = None
            try:
                if msg.is_reply:
                    replied = await msg.get_reply_message()
                    if replied:
                        reply_user = await self.client.get_entity(replied.sender_id)
                elif msg.is_private:
                    reply_user = await self.client.get_entity(msg.peer_id)
            except Exception:
                pass
            if reply_user:
                placeholders["reply_firstname"] = getattr(reply_user, "first_name", None) or getattr(reply_user, "title", "") or ""
                placeholders["reply_lastname"] = getattr(reply_user, "last_name", "") or ""
            else:
                placeholders["reply_firstname"] = ""
                placeholders["reply_lastname"] = ""

        def replacer(m: re.Match) -> str:
            name = m.group(1)
            default = m.group(2) if m.group(2) is not None else ""
            val = placeholders.get(name)
            return default if val is None or val == "" else val
        for _ in range(3):
            if "{" not in text:
                break
            text = re.sub(r"\{([a-zA-Z0-9_-]+)(?::([^{}]*(?:\{[^{}]+\}[^{}]*)*))?\}", replacer, text)
        return text

    async def _can_embed_links(self, chat_id: int) -> bool:
        try:
            permissions = await self.client.get_permissions(chat_id, "me")
            if hasattr(permissions, "embed_links"):
                return bool(permissions.embed_links)
        except Exception:
            pass
        return True

    async def _process_and_send(self, event, msg_id: int, should_delete: bool, match_obj: re.Match | None = None) -> bool:
        source_id = self.config["source_channel_id"]
        if not source_id:
            return False
        try:
            source_msg = await self.client.get_messages(source_id, ids=msg_id)
            if not source_msg:
                return False
            caption = source_msg.html_text or ""
            if caption:
                first_line = caption.split("\n", 1)[0].strip()
                if re.match(r"^~{1,3}", first_line):
                    caption = "\n".join(caption.split("\n")[1:]).strip()
            reply_to_id = event.message.reply_to_msg_id if event.message.is_reply else None
            is_webpage = source_msg.media and source_msg.media.__class__.__name__ == "MessageMediaWebPage"
            is_media = bool(source_msg.media) and not is_webpage
            if is_media or should_delete:
                is_edited = event.message.id in self._edited_msg_ids
                msg_time = (
                    event.message.edit_date
                    or (datetime.now(timezone.utc) if is_edited else event.message.date)
                )
                delay = (datetime.now(timezone.utc) - msg_time).total_seconds()
                if delay > self.config["max_delay"]:
                    logger.info(f"Skipping trigger response due to delay: {delay}s (limit: {self.config['max_delay']}s)")
                    return False
            if is_media:
                fast_cap = self._replace_placeholders_fast(caption, event.message, match_obj) if caption else None
                sent = await self.client.send_file(
                    event.chat_id, source_msg, caption=fast_cap or None,
                    reply_to=reply_to_id, parse_mode="html",
                )
                sc = await self.db.db_get(self.name, "sent_count") or 0
                await self.db.db_set(self.name, "sent_count", sc + 1)
                if caption and self._has_slow_placeholders(caption) and sent:
                    _fc, _sm = fast_cap, sent
                    async def _upd(fc=_fc, sm=_sm):
                        slow = await self._replace_placeholders(caption, event, match_obj)
                        if slow != fc:
                            try:
                                await self.client.edit_message(event.chat_id, sm.id, text=slow)
                            except Exception as e:
                                if "not modified" not in str(e).lower():
                                    logger.error(f"Error updating media caption: {e}")
                    asyncio.create_task(_upd())
                if should_delete:
                    try:
                        await self.client.delete_messages(event.chat_id, [event.message.id])
                    except Exception:
                        pass
                return True
            else:
                can_embed = await self._can_embed_links(event.chat_id)
                preview = can_embed and is_webpage
                text_to_send = caption or ""
                if should_delete:
                    fast_text = self._replace_placeholders_fast(text_to_send, event.message, match_obj) if text_to_send else ""
                    sent = await self.client.send_message(
                        event.chat_id, fast_text, reply_to=reply_to_id,
                        parse_mode="html", link_preview=preview,
                    )
                    sc = await self.db.db_get(self.name, "sent_count") or 0
                    await self.db.db_set(self.name, "sent_count", sc + 1)
                    if text_to_send and self._has_slow_placeholders(text_to_send) and sent:
                        _ft, _sm = fast_text, sent
                        async def _upd2(ft=_ft, sm=_sm):
                            slow = await self._replace_placeholders(text_to_send, event, match_obj)
                            if slow != ft:
                                try:
                                    await self.client.edit_message(event.chat_id, sm.id, text=slow, link_preview=preview)
                                except Exception as e:
                                    if "not modified" not in str(e).lower():
                                        logger.error(f"Error updating delete text: {e}")
                        asyncio.create_task(_upd2())
                    if event.message.out:
                        try:
                            await self.client.delete_messages(event.chat_id, [event.message.id])
                        except Exception:
                            pass
                    return True
                else:
                    fast_text = self._replace_placeholders_fast(text_to_send, event.message, match_obj) if text_to_send else ""
                    if not fast_text:
                        return False
                    await self.edit(event, fast_text, as_html=True)
                    sc = await self.db.db_get(self.name, "sent_count") or 0
                    await self.db.db_set(self.name, "sent_count", sc + 1)
                    if text_to_send and self._has_slow_placeholders(text_to_send):
                        _ft, _ev = fast_text, event
                        async def _upd3(ft=_ft, ev=_ev):
                            slow = await self._replace_placeholders(text_to_send, ev, match_obj)
                            if slow != ft:
                                try:
                                    await self.edit(ev, slow, as_html=True)
                                except Exception as e:
                                    if "not modified" not in str(e).lower():
                                        logger.error(f"Error updating edit text: {e}")
                        asyncio.create_task(_upd3())
                    return True
        except Exception as e:
            if "not modified" not in str(e).lower():
                logger.error(f"Error sending trigger response for msg_id {msg_id}: {e}")
        return False

    @watcher()
    async def trigger_watcher(self, event: events.NewMessage.Event) -> None:
        message = event.message
        if not message.out or not message.text:
            return
        self._remember_outgoing_text(message)
        chat_id = message.chat_id
        ignored = await self._get_ignored_chats()
        if chat_id in ignored:
            return
        if message.is_channel and not message.is_group:
            if not self.config["trigger_in_channels"]:
                return
        elif message.is_group:
            if not self.config["trigger_in_groups"]:
                return
        elif message.is_private:
            if not self.config["trigger_in_pm"]:
                return
        matched = self._find_match(message.raw_text)
        if not matched:
            return
        key, match_obj = matched
        entries = self.triggers.get(key, [])
        if not entries:
            return
        should_delete = "delete" in key.split("::", 1)[0]
        tasks = [
            self._process_and_send(event, e["content_id"] if isinstance(e, dict) else e, should_delete, match_obj)
            for e in entries
        ]
        results = await asyncio.gather(*tasks)
        if should_delete and message.out and any(results):
            try:
                await event.delete()
            except Exception:
                pass

    @watcher()
    async def source_channel_watcher(self, event: events.NewMessage.Event) -> None:
        source_id = self.config["source_channel_id"]
        if not source_id or event.chat_id != source_id:
            return
        result = await self._process_message_for_triggers(event.message)
        if not result:
            return
        ttype, trigger, content_id, trigger_id = result
        key = f"{ttype}::{trigger}"
        if key not in self.triggers:
            self.triggers[key] = []
        exists = any(
            (isinstance(e, dict) and e["content_id"] == content_id) or (isinstance(e, int) and e == content_id)
            for e in self.triggers[key]
        )
        if not exists:
            self.triggers[key].append({"content_id": content_id, "trigger_id": trigger_id})
        await self._save_triggers()

    @command("tparse", doc_ru="Сканировать исходный канал для обновления триггеров", doc_en="Scan the source channel to update triggers")
    async def cmd_tparse(self, event: events.NewMessage.Event) -> None:
        await self._run_parser(event)

    @command("tadd", doc_ru="<reply> <trigger> - Добавить новый триггер", doc_en="<reply> <trigger> - Add a new trigger")
    async def cmd_tadd(self, event: events.NewMessage.Event) -> None:
        reply = await event.get_reply_message()
        if not reply:
            await self.edit(event, self.strings("must_be_reply") + f"\n<code>{_escape_html(event.raw_text)}</code>", as_html=True)
            return
        parts = event.raw_text.split(maxsplit=1)
        args = parts[1] if len(parts) > 1 else ""
        if not args:
            await self.edit(event, self.strings("no_trigger_specified") + f"\n<code>{_escape_html(event.raw_text)}</code>", as_html=True)
            return
        ttype, trigger = self._parse_trigger_string(args)
        if not ttype or not trigger:
            await self.edit(event, self.strings("invalid_trigger_format") + f"\n<code>{_escape_html(event.raw_text)}</code>", as_html=True)
            return
        await self.edit(event, self.strings("processing_add"), as_html=True)
        source_id = self.config["source_channel_id"]
        if not source_id:
            await self.edit(event, self.strings("channel_error") + "\n<code>Source channel ID not configured.</code>", as_html=True)
            return
        try:
            is_webpage = reply.media and reply.media.__class__.__name__ == "MessageMediaWebPage"
            if reply.media and not is_webpage:
                content_msg = await self.client.send_file(source_id, reply, caption=reply.text or None, parse_mode="html")
            elif reply.text:
                content_msg = await self.client.send_message(source_id, reply.text, parse_mode="html")
            else:
                await self.edit(event, self.strings("empty_response"), as_html=True)
                return
            trigger_msg = await self.client.send_message(source_id, args, reply_to=content_msg.id, parse_mode="html")
            key = f"{ttype}::{trigger}"
            if key not in self.triggers:
                self.triggers[key] = []
            entry = {"content_id": content_msg.id, "trigger_id": trigger_msg.id}
            exists = any(
                (isinstance(e, dict) and e["content_id"] == content_msg.id) or (isinstance(e, int) and e == content_msg.id)
                for e in self.triggers[key]
            )
            if not exists:
                self.triggers[key].append(entry)
            await self._save_triggers()
            channel_id_str = str(source_id).replace("-100", "")
            link = f"https://t.me/c/{channel_id_str}/{trigger_msg.id}"
            await self.edit(event, self.strings("trigger_added").format(_escape_html(args), link), as_html=True)
            if event.message.out:
                try:
                    await self.client.delete_messages(event.chat_id, [event.message.id])
                except Exception:
                    pass
        except Exception as e:
            logger.exception("Failed to add trigger")
            await self.edit(event, self.strings("add_trigger_error") + f"\n<code>{_escape_html(str(e))}</code>", as_html=True)

    @command("tsearch", doc_ru="<query> - Найти триггеры", doc_en="<query> - Search triggers")
    async def cmd_tsearch(self, event: events.NewMessage.Event) -> None:
        parts = event.raw_text.split(maxsplit=1)
        args = parts[1] if len(parts) > 1 else ""
        if not args:
            await self.edit(event, self.strings("invalid_search_query"), as_html=True)
            return
        await self.edit(event, self.strings("search_progress"), as_html=True)
        matched = self._find_matching_triggers(args)
        if not matched:
            await self.edit(event, self.strings("search_no_results").format(_escape_html(args)), as_html=True)
            return
        source_id = self.config["source_channel_id"]
        if not source_id:
            await self.edit(event, self.strings("search_no_source"), as_html=True)
            return
        channel_id_str = str(source_id).replace("-100", "")

        type_names = {
            "exact": "Точный (~)",
            "contains": "Содержит (~~)",
            "exact_delete": "Точный с удалением (~~~)",
            "regex": "Regex (~|)",
            "regex_delete": "Regex с удалением (~~~|)",
        }

        lines = [
            f"<blockquote><tg-emoji emoji-id=5471981045991632785>🔍</tg-emoji>"
            f" <b>Результаты поиска для: «</b>{_escape_html(args)}<b>»</b></blockquote>\n"
        ]
        total_found = 0

        for key, ttype, trigger in matched:
            entries = self.triggers[key]
            if not entries:
                continue

            ttype_readable = type_names.get(ttype, ttype)

            lines.append(
                f"<blockquote><tg-emoji emoji-id=5424692575594376190>📌</tg-emoji>"
                f" <b>Триггер:</b> <code>{_escape_html(trigger)}</code>"
                f" ({ttype_readable})</blockquote>"
            )

            links = []
            for entry in entries:
                total_found += 1
                cid = entry["content_id"] if isinstance(entry, dict) else entry
                tid = entry.get("trigger_id") if isinstance(entry, dict) else None

                content_link = f"<a href='https://t.me/c/{channel_id_str}/{cid}'>Ответ #{cid}</a>"
                if tid:
                    trigger_link = f"<a href='https://t.me/c/{channel_id_str}/{tid}'>Триггер #{tid}</a>"
                    links.append(f"{trigger_link} ({content_link})")
                else:
                    links.append(content_link)

            lines.append(
                f"<blockquote><tg-emoji emoji-id=5208730126619005798>🔗</tg-emoji>"
                f" Сообщения: {', '.join(links)}</blockquote>"
            )
            lines.append("")

        lines.append(
            f"\n<blockquote><tg-emoji emoji-id=5258503720928288433>ℹ️</tg-emoji>"
            f" Всего найдено совпадений: <b>{total_found}</b></blockquote>"
        )
        await self.edit(event, "\n".join(lines), as_html=True)

    @command("tignore", doc_ru="[chat_id] - Исключить чат", doc_en="[chat_id] - Ignore chat")
    async def cmd_tignore(self, event: events.NewMessage.Event) -> None:
        parts = event.raw_text.split(maxsplit=1)
        args = parts[1] if len(parts) > 1 else ""
        chat_id = None
        if args:
            try:
                chat_id = int(args)
            except ValueError:
                try:
                    entity = await self.client.get_entity(args)
                    chat_id = entity.id
                except Exception:
                    await self.edit(event, self.strings("ignore_invalid_chat"), as_html=True)
                    return
        else:
            chat_id = event.chat_id
        if not chat_id:
            await self.edit(event, self.strings("ignore_no_chat"), as_html=True)
            return
        ignored = await self._get_ignored_chats()
        if chat_id in ignored:
            ignored.remove(chat_id)
            await self.db.db_set(self.name, "ignored_chats", ignored)
            await self.edit(event, self.strings("ignore_removed").format(chat_id), as_html=True)
        else:
            ignored.append(chat_id)
            await self.db.db_set(self.name, "ignored_chats", ignored)
            await self.edit(event, self.strings("ignore_added").format(chat_id), as_html=True)

    @command("tsetsource", doc_ru="[chat_id] - Установить источник триггеров", doc_en="[chat_id] - Set trigger source")
    async def cmd_tsetsource(self, event: events.NewMessage.Event) -> None:
        parts = event.raw_text.split(maxsplit=1)
        args = parts[1] if len(parts) > 1 else ""
        chat_id = None
        if args:
            try:
                chat_id = int(args)
            except ValueError:
                try:
                    entity = await self.client.get_entity(args)
                    chat_id = entity.id
                except Exception:
                    await self.edit(event, self.strings("ignore_invalid_chat"), as_html=True)
                    return
        else:
            chat_id = event.chat_id
        if not chat_id:
            await self.edit(event, self.strings("ignore_no_chat"), as_html=True)
            return
        self.config["source_channel_id"] = chat_id
        await self.edit(event, self.strings("source_set").format(chat_id), as_html=True)
