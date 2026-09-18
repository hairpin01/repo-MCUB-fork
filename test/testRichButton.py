# repo: https://github.com/hairpin01/repo-MCUB-fork
# dir: test
# file: 'test-rich-buttons.py'

from html import escape
from typing import Any

import core.lib.loader.module_base as loader
from core.lib.types import Event, InlineMessage
from utils import Strings


class ModuleTestRichButton(loader.ModuleBase):
    """модуль для теста rich кнопок и форматированья"""
    name = "testRichButton"
    strings: Strings | dict = {"name": "null"}

    async def on_load(self) -> None:
        await super().on_load()

        self.layout_ru: list[str] = [
            "<tg-button-row>",
            "й", "ц", "у", "к", "е", "н", "<slice>",
            "</tg-button-row>",
            "<tg-button-row>",
            "г", "ш", "щ", "з", "х", "ъ", "\\n",
            "</tg-button-row>",
            "<tg-button-row>",
            "ф", "ы", "в", "а", "п", "р",
            "</tg-button-row>",
            "<tg-button-row>",
            "о", "л", "д", "ж", "э", "ё",
            "</tg-button-row>",
            "<tg-button-row>",
            "я", "ч", "с", "м", "и", "т",
            "</tg-button-row>",
            "<tg-button-row>",
            "ь", "б", "ю",
            "</tg-button-row>",
            '<tg-button-row>',
            '.', ',',
            '</tg-button-row>',
            '<tg-button-row>',
            '<shift>', ' ', '<switch_layout>', "<hide_panel>",
            '</tg-button-row>'
        ]

        self.layout_en: list[str] = [
            "<tg-button-row>",
            "q", "w", "e", "r", "t", "y", "<slice>",
            "</tg-button-row>",
            "<tg-button-row>",
            "u", "i", "o", "p", '\\n',
            "</tg-button-row>",
            "<tg-button-row>",
            "a", "s", "d", "f", "g", "h",
            "</tg-button-row>",
            "<tg-button-row>",
            "j", "k", "l", "z", "x",
            "</tg-button-row>",
            "<tg-button-row>",
            "c", "v", "b", "n", "m",
            "</tg-button-row>",
            '<tg-button-row>',
            '.', ',',
            '</tg-button-row>',
            '<tg-button-row>',
            '<shift>', ' ', '<switch_layout>', "<hide_panel>", # панель и switch_layout
            '</tg-button-row>'
        ]
        self.hide_panel = False
        self.layout_hide_panel: list[str] = [
            "<tg-button-row>",
            '<send_in_chat>', '<copy>', # клутые штуки
            "</tg-button-row>",
            "<tg-button-row>",
            '(', ')', '<', '>', '"', "'",
            "</tg-button-row>",
            "<tg-button-row>",
            '-', '=', '+', '_',
            "</tg-button-row>",
            "<tg-button-row>",
            "<input>",
            "</tg-button-row>",
            "<tg-button-row>",
            "<hide_panel>",
            "</tg-button-row>"
        ]
        self.line: str = ""
        self.lang = 'ru'
        self.shift = False
        self.caps_lock = False
        self.chat_id: int | None = None

    @loader.command("клава", doc_uk="клавэ", doc_ru="клава")
    async def cmd_klava(self, message: Event) -> None:
        keyboard, buttons = await self._build_keyboard(message)
        self.chat_id = message.chat_id

        await self.subinline.rich_form(
            message,
            keyboard,
            buttons=buttons,
        )

    @loader.callback()
    async def on_keyboard(
        self,
        call: InlineMessage,
        args: tuple[str] | None,
        data: Any = None,
    ) -> None:
        if args:
            self.line += args[0]
            if not args in ('\n', ' '):
                self.shift = False

        keyboard, buttons = await self._build_keyboard(call)
        if keyboard and buttons:
            await call.edit_rich(keyboard, buttons=buttons)

    @loader.callback()
    async def on_send_in_chat(
        self,
        call: InlineMessage,
        data=None
    ) -> None:
        if not self.line:
            await call.answer('Напиши что-то')
            return None

        chat_id = self.chat_id
        if not self.chat_id:
            me = await self.client.get_me()
            chat_id = me.id

        await self.client.send_message(
            chat_id,
            self.line,
        )
        await call.answer(f'Success send message in chat {self.chat_id}')

    # @loader.callback()
    # async def on_eval(self, call: InlineMessage, data=None) -> None:
    #     mod_eval = self.require_module('evaluator')
    #     call.raw_text = self.line
    #     call.text = self.line
    #     await mod_eval.cmd_py(mod_eval, call)
    # потом, щас лень

    @loader.callback()
    async def on_close(
        self,
        call: InlineMessage,
        data: Any = None,
    ) -> None:
        self.line = ""
        await self.client.delete_messages(call.chat_id, [call.message_id])

    @loader.callback()
    async def on_clear_line(
        self,
        call: InlineMessage,
        data: Any = None,
    ) -> None:
        self.line = ""

        keyboard, buttons = await self._build_keyboard(call)
        if keyboard and buttons:
            await call.edit_rich(keyboard, buttons=buttons)
            await call.answer("Ввод очищен")

    @loader.callback()
    async def on_slice(self, call: InlineMessage, data=None) -> None:
        self.line = self.line[:-1]
        text, buttons = await self._build_keyboard(call)
        if text and buttons:
            await call.edit_rich(text, buttons=buttons)

    @loader.callback()
    async def on_switch_layout(self, call: InlineMessage, data=None) -> None:
        if self.lang == 'ru':
            self.lang = 'en'
        else:
            self.lang = 'ru'

        text, buttons = await self._build_keyboard(call)
        if text and buttons:
            await call.edit_rich(text, buttons=buttons)

    @loader.callback()
    async def on_switch_hide_panel(self, call: InlineMessage, data=None) -> None:
        match self.hide_panel:
            case True:
                self.hide_panel = False
            case _:
                self.hide_panel = True
        text, buttons = await self._build_keyboard(call)
        if text and buttons:
            await call.edit_rich(text, buttons=buttons)

    @loader.callback()
    async def on_switch_shift(self, call: InlineMessage, data=None) -> None:
        match self.shift:
            case True:
                self.shift = False
                self.caps_lock = True
            case _:
                if self.caps_lock:
                    self.caps_lock = False
                else:
                    self.shift = True

        text, buttons = await self._build_keyboard(call)
        if text and buttons:
            await call.edit_rich(
                text,
                buttons=buttons,
            )

    def _build_button(self) -> list[list[Any]]:
        return [
            [self.Button.inline("Очистить ввод", self.on_clear_line)],
            [self.Button.inline(self.strings("buttons")("close"), self.on_close)],
        ]

    @loader.callback()
    async def on_input_menu(self, call: InlineMessage, data=None) -> None:
        self._event = call
        text, buttons = self._build_input_menu(call)
        await call.edit_rich(
            text, buttons=buttons
        )

    async def on_input(self, call: Event, args: str, data= None) -> None:
        message = self._event
        if message is None:
            return None

        await message.answer('Принято')
        self.line = args
        text, buttons = self._build_keyboard(message)
        if text and buttons:
            await message.edit_rich(
                text, buttons=buttons
            )

    def _build_input_menu(self, message: InlineMessage) -> tuple[str, list[list[Any]]]:
        lines = [
            '<h1 align="center">Вести свой текст через inline input...</h1>',
            '<aside>Вот сейчас:</aside>',
            f"<pre><code>{escape(self.line) + '_' if self.line else 'щас нечего не написано...'}</code></pre>"
            '<aside><i>Жми...</i></aside>',
            '<tg-button-row align="center">{input}</tg-button-row>',
            '<aside><b>Назад<b></aside>'
            '<tg-button-row align="center">{back}</tg-button-row>',
        ]
        text = '\n'.join(lines)
        buttons = self._build_button()
        return text.format(
            input=self.Button.rich.input(
                '✏️ Вести...',
                self.on_input,
                style='success',
                html_tag=True,
            ),
            back=self.Button.rich.inline(
                '<-',
                self.on_keyboard,
                args=(None,),
                style='danger',
                html_tag=True,
            )
        ), buttons

    async def _build_hide_keyboard(
        self,
        message: InlineMessage | Event,
    ) -> tuple[str, list[list[Any]]]:

        value = f'{escape(self.line)}_' if self.line else "_"
        keyboard = (
            f"<h1>{self.strings('material_emoji')('load_1')} Набирай чот</h1>\n"
            f"<pre><code>⌨️ {value}</code></pre>\n"
        )
        for key in self.layout_hide_panel:
            if key in ("<tg-button-row>", "</tg-button-row>"):
                keyboard += key
                continue

            elif key == '<hide_panel>':
                keyboard += self.Button.rich.inline(
                    '↑',
                    self.on_switch_hide_panel,
                    html_tag=True,
                    style='primary',
                )
                continue

            elif key == '<send_in_chat>':
                keyboard += self.Button.rich.inline(
                    '✊ Send in chat',
                    self.on_send_in_chat,
                    html_tag=True,
                    style='success'
                )
                continue

            elif key == '<copy>':
                if len(self.line) > 0:
                    keyboard += self.Button.rich.copy(
                        '📜 Copy',
                        self.line,
                        html_tag=True,
                        style='primary',
                    )
                else:
                    keyboard += self.Button.rich.text(
                        '❌ Copy',
                        html_tag=True,
                        style='danger',
                    )
                continue

            elif key == '<input>':
                keyboard += self.Button.rich.inline(
                    '✏️ Input...',
                    self.on_input_menu,
                    style='danger',
                    html_tag=True,
                )
                continue

            keyboard += self.Button.rich.inline(
                key,
                self.on_keyboard,
                args=(key,),
                html_tag=True,
            )

        buttons = self._build_button()

        return keyboard, buttons

    def _upper_key(self, key: str) -> str:
        if self.shift or self.caps_lock:
            return key.upper()
        return key

    async def _build_keyboard(
        self,
        message: InlineMessage | Event,
    ) -> tuple[str, list[list[Any]]]:

        if self.hide_panel:
            return await self._build_hide_keyboard(message)

        layout_dict = getattr(self, f'layout_{self.lang}', None)

        if layout_dict is None:
            await self.edit(message, "Раскладка пуста")
            return "", []

        value = f'{escape(self.line)}_' if self.line else "_"
        keyboard = (
            f"<h1>{self.strings('material_emoji')('load_1')} Набирай чот</h1>\n"
            f"<pre><code>⌨️ {value}</code></pre>\n"
        )

        for key in layout_dict:
            if key in ("<tg-button-row>", "</tg-button-row>"):
                keyboard += key
                continue

            elif key == '<hide_panel>':
                keyboard += self.Button.rich.inline(
                    '↓',
                    self.on_switch_hide_panel,
                    html_tag=True,
                    style='primary'
                )
                continue

            elif key == '\\n':
                keyboard += self.Button.rich.inline(
                    'Enter',
                    self.on_keyboard,
                    args=('\n',),
                    html_tag=True,
                    style='success'
                )
                continue

            elif key == '<slice>':
                keyboard += self.Button.rich.inline(
                    '←',
                    self.on_slice,
                    html_tag=True,
                    style='danger',
                )
                continue

            elif key == ' ':
                keyboard += self.Button.rich.inline(
                    'Space',
                    self.on_keyboard,
                    args=(key,),
                    html_tag=True,
                    style='primary'
                )
                continue

            elif key == '<switch_layout>':
                keyboard += self.Button.rich.inline(
                    self.lang.upper(),
                    self.on_switch_layout,
                    html_tag=True,
                    style='primary'
                )
                continue

            elif key == '<shift>':
                keyboard += self.Button.rich.inline(
                    'Shift' if not self.caps_lock else 'SHIFT',
                    self.on_switch_shift,
                    html_tag=True,
                    style='success' if self.shift or self.caps_lock else 'primary',
                )
                continue


            keyboard += self.Button.rich.inline(
                self._upper_key(key),
                self.on_keyboard,
                args=(self._upper_key(key),),
                html_tag=True,
            )

        buttons = self._build_button()

        return keyboard, buttons
