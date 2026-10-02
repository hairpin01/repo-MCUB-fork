# scop: kernel min v1.2.6.1
# banner_url: https://raw.githubusercontent.com/hairpin01/repo-MCUB-fork/main/assets/banner/create-buttons-banner.png
from core.lib.loader.module_base import ModuleBase, command, callback
import utils
from typing import Any


class CreateButtonsMod(ModuleBase):
    """class-style modules MCUB"""

    name = "create-buttons"
    version = "1.0.0"
    description = {"ru": "coздaть инлaйн кнoпки", "en": "create inline buttons"}

    @command(
        "create-button",
        doc={
            "ru": "<count> coздaть X кoличecтвo кнoпoк",
            "en": "<count> create X count button(s)",
        },
    )
    async def create_buttons(self, message: Any) -> None:
        try:
            args = int(utils.get_args_raw(message))
        except ValueError as err:
            self.log.debug(f"error debug: {err}")
            await utils.answer(
                message,
                f"please typing <code>{self.kernel.custom_prefix}create_buttons 1</code>",
                as_html=True,
            )
            return
        buttons = []
        for i in range(int(args)):
            buttons.append([self.Button.inline(f"button {i + 1}", self.on_click)])
        await self.kernel.inline_form(
            message.chat_id, f"Buttons created: {args}", buttons=buttons
        )

    async def on_click(self, call) -> None:
        await call.answer("click the buttons", alert=False)
