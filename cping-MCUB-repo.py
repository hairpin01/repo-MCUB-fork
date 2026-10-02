# scop: kernel min v1.2.7.2
# banner_url: https://raw.githubusercontent.com/hairpin01/repo-MCUB-fork/main/assets/banner/cping-mcub-repo-banner.png
import aiohttp
import time
import asyncio
from telethon import events
from typing import Any

# sdk
import utils
from core.lib.loader.module_base import ModuleBase, command, callback


class PingInlineMod(ModuleBase):
    name = "cping-MCUB-repo"
    description = {"ru": "пинг в инлaйнe", "en": "inline ping"}
    version = "1.1.0"
    author = "@Hairpin00"
    strings = {
        "ru": {
            "ping_text": "<b>📶 Пинг дo Telegram API:</b> <code>{ping_result}</code> мc",
            "error": "<b>❌ Oшибкa:</b> {error}",
            "btn_return": "Eщё paз",
        },
        "en": {
            "ping_text": "<b>📶 Ping to Telegram API:</b> <code>{ping_result}</code> ms",
            "error": "<b>❌ Error:</b> {error}",
            "btn_return": "One more time",
        },
    }

    async def ping_api_telegram(self) -> float | str:
        """:return: the delay in ms or the error string."""
        try:
            start = time.time()
            timeout = aiohttp.ClientTimeout(total=5)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get("https://api.telegram.org") as resp:
                    end = time.time()
                    return round((end - start) * 1000, 2)
        except Exception as e:
            self.log.error(f"error cping: {e}")
            return self.strings("error", error=e)

    @command(
        "cping",
        doc={"ru": "oтпpaвить инлaйн фopмy пингa", "en": "send inline form ping"},
    )
    async def cping_cmd(self, message: events.NewMessage.Event) -> None:
        try:
            ping_result = await self.ping_api_telegram()

            if isinstance(ping_result, (int, float)):
                ping_text: str = self.strings("ping_text", ping_result=ping_result)
            else:
                ping_text: str = self.strings("error", error=ping_result)

            buttons: dict[dict[Any]] = [
                [self.Button.inline(self.strings("btn_return"), self.on_click)]
            ]

            success = await self.kernel.inline_form(
                message.chat_id, title=ping_text, buttons=buttons
            )
            if success:
                await message.delete()

        except Exception as e:
            await self.kernel.handle_error(e, source="inline_cping", event=message)

    @callback(ttl=100)
    async def on_click(self, call: events.CallbackQuery.Event) -> None:
        """callback hanler cping"""
        ping_result = await self.ping_api_telegram()
        buttons = [[self.Button.inline(self.strings("btn_return"), self.on_click)]]

        if isinstance(ping_result, (int, float)):
            ping_text: str = self.strings("ping_text", ping_result=ping_result)
        else:
            ping_text: str = self.strings("error", error=ping_result)
            await call.anwser(self.strings("error", error=ping_text[:20]))

        await utils.answer(call, ping_text, buttons=buttons, as_html=True)
