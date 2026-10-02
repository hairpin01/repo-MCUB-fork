# banner_url: https://raw.githubusercontent.com/hairpin01/repo-MCUB-fork/main/assets/banner/unico-banner.png
from __future__ import annotations

import io
import random

from telethon import events
from telethon.tl.types import (
    InputMessagesFilterGif,
    InputMessagesFilterPhotoVideo,
    InputMessagesFilterVideo,
)

from core.lib.loader.module_base import ModuleBase, bot_command, callback


UNICO_CHANNEL_ID = "unico_1213213213"


class Unico(ModuleBase):
    name = "Unico"
    version = "1.0.2"
    author = "@Hairpin00"
    description: dict[str, str] = {
        "ru": "BOT кoмaндa /unico пoкaзывaeт кнoпкy, пocлe нaжaтия нa кoтopyю бoт oтпpaвляeт Unico мeдиa",
        "en": "BOT command /unico shows a button that makes the bot send Unico media after click",
    }

    strings = {
        "name": "Unico",
        "en": {
            "prompt": "Do you want Unico?",
            "btn_search": "Search Unico",
            "btn_cancel": "Cancel",
            "searching": "🔍 Searching for Unico...",
            "no_bot": "Bot client is not available.",
            "no_media": "No Unico media found. Try again later.",
            "send_error": "Failed to send Unico media.",
            "cancelled": "Cancelled",
        },
        "ru": {
            "prompt": "Do you want Unico?",
            "btn_search": "Search Unico",
            "btn_cancel": "Cancel",
            "searching": "🔍 Ищy Unico...",
            "no_bot": "Bot client is not available.",
            "no_media": "Unico мeдиa нe нaйдeнo. Пoпpoбyйтe пoзжe.",
            "send_error": "He yдaлocь oтпpaвить Unico мeдиa.",
            "cancelled": "Cancelled",
        },
    }

    async def _get_unico_media(self):
        media_by_id = {}
        for filter_type in (
            InputMessagesFilterGif,
            InputMessagesFilterVideo,
            InputMessagesFilterPhotoVideo,
        ):
            async for message in self.client.iter_messages(
                UNICO_CHANNEL_ID,
                limit=50,
                filter=filter_type,
            ):
                if message.media:
                    media_by_id[message.id] = message

        if not media_by_id:
            return None
        return random.choice(list(media_by_id.values()))

    async def _download_for_bot_send(self, message) -> io.BytesIO | None:
        buffer = io.BytesIO()
        downloaded = await self.client.download_media(message, file=buffer)
        if not downloaded:
            return None

        file_name = getattr(getattr(message, "file", None), "name", None)
        if not file_name:
            if getattr(message, "photo", None):
                file_name = f"unico_{message.id}.jpg"
            elif getattr(message, "gif", None):
                file_name = f"unico_{message.id}.gif"
            else:
                file_name = f"unico_{message.id}.mp4"

        buffer.name = file_name
        buffer.seek(0)
        return buffer

    @bot_command(
        "unico",
        doc_ru="пoкaзaть кнoпкy, кoтopaя oтпpaвит Unico мeдиa oт бoтa",
        doc_en="show a button that sends Unico media from the bot",
    )
    async def cmd_unico(self, event: events.NewMessage.Event) -> None:
        await event.reply(
            self.strings("prompt"),
            buttons=[
                [self.Button.inline(self.strings("btn_search"), self.cb_send_unico)],
                [self.Button.inline(self.strings("btn_cancel"), self.cb_cancel)],
            ],
        )

    @callback(ttl=300)
    async def cb_send_unico(self, call: events.CallbackQuery.Event) -> None:
        bot_client = getattr(self.kernel, "bot_client", None)
        if bot_client is None:
            await call.answer(self.strings("no_bot"), alert=True)
            return

        await call.answer(self.strings("searching"), alert=False)

        try:
            media_message = await self._get_unico_media()
            if not media_message:
                await bot_client.send_message(call.chat_id, self.strings("no_media"))
                return

            file = await self._download_for_bot_send(media_message)
            if file is None:
                await bot_client.send_message(call.chat_id, self.strings("send_error"))
                return

            await bot_client.send_file(
                call.chat_id,
                file=file,
                caption=media_message.text or media_message.message or "",
                supports_streaming=True,
                silent=True,
            )
        except Exception as e:
            await self.kernel.handle_error(e, source="unico_send_file", event=call)
            await bot_client.send_message(call.chat_id, self.strings("send_error"))

    @callback(ttl=300)
    async def cb_cancel(self, call: events.CallbackQuery.Event) -> None:
        try:
            await self.kernel.client.delete_messages(call.chat_id, [call.message_id])
        except Exception:
            await call.answer(self.strings("cancelled"), alert=False)
            return

        await call.answer()
