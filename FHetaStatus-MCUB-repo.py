from __future__ import annotations

# requires: aiohttp
# author: @midga3_modules / port by OpenAgent
# version: 1.0.4
# description: NOT OFFICIAL FHeta status checker for MCUB
# banner_url: https://raw.githubusercontent.com/hairpin01/repo-MCUB-fork/main/assets/banner/fhetastatus-banner.png

import asyncio
from typing import Any

import aiohttp

from core.lib.loader.module_base import ModuleBase, command


class FHetaStatusModule(ModuleBase):
    """NOT OFFICIAL FHeta MODULE. Check FHeta status."""

    name = "FHetaStatus"
    version = "1.0.4"
    author = "@midga3_modules / port by OpenAgent"
    description = "Heoфициaльнaя пpoвepкa дocтyпнocти FHeta."

    check_url = "https://api.fixyres.com/module/Midga3/heroku-modules/radiolistener.py"

    texts = {
        "checking": '<b><emoji document_id="5427009714745517609">🔄</emoji> Checking FHeta...</b>',
        "working": '<b><emoji document_id="5427009714745517609">✅</emoji> FHeta is working</b>',
        "not_working": '<b><emoji document_id="5465665476971471368">❌</emoji> FHeta is unavailable</b>',
        "error": '<b><emoji document_id="5465665476971471368">❌</emoji> FHeta check failed:</b> <code>{error}</code>',
    }

    async def _edit_html(self, message: Any, text: str) -> None:
        await message.edit(text, parse_mode="html")

    @command(
        "fping",
        doc={
            "en": "check FHeta status",
            "ru": "пpoвepить cтaтyc FHeta",
        },
    )
    async def fping(self, message: Any) -> None:
        """Check FHeta status."""
        await self._edit_html(message, self.texts["checking"])

        try:
            timeout = aiohttp.ClientTimeout(total=15)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(self.check_url) as response:
                    text = await response.text()
                    is_working = response.status == 200 and text.strip() != "[]"
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            await self.kernel.handle_error(e, source="fping", event=message)
            await self._edit_html(
                message,
                self.texts["error"].format(error=type(e).__name__),
            )
            return

        if is_working:
            await self._edit_html(message, self.texts["working"])
        else:
            await self._edit_html(message, self.texts["not_working"])
