from __future__ import annotations

# Standard library
import time

# Third-party
from telethon import events

# SDK
import core.lib.loader.module_base as loader
import utils


class HerokuTime(loader.ModuleBase):
    name = "HerokuTime"
    version = "1.0.1"
    author = "@SunnexGB"
    description: dict[str, str] = {
        "ru": "Показывает сколько времени вы используете юзербот (с момента установки)",
        "en": "Shows how long you have been using the userbot (since installation)",
    }

    strings = {
        "ru": {
            "uptime": "⏱ Время работы: {time}",
            "not_set": "Время старта не установлено.",
        },
        "en": {
            "uptime": "⏱ Uptime: {time}",
            "not_set": "Start time is not set.",
        },
    }

    @loader.on_install
    async def first_install(self) -> None:
        """Save start_time only on first install."""
        await self.db.db_set(self.name, "start_time", str(int(time.time())))
        self.log.info("HerokuTime: start_time saved on install.")

    async def on_load(self) -> None:
        # Ensure start_time exists even if on_install was skipped (e.g. manual load)
        existing = await self.db.db_get(self.name, "start_time")
        if not existing:
            await self.db.db_set(self.name, "start_time", str(int(time.time())))
            self.log.info("HerokuTime: start_time initialized on load.")

        utils.register_decorated_placeholders(self.name, self)

    async def on_unload(self) -> None:
        utils.unregister_scope(self.name)

    @utils.placeholders(
        "alltime", description="Total userbot uptime since installation"
    )
    async def _placeholder_alltime(self, data: dict) -> str:
        raw = await self.db.db_get(self.name, "start_time")
        if not raw:
            return self.strings["not_set"]
        elapsed = int(time.time()) - int(raw)
        return utils.format_time(elapsed, detailed=True)
