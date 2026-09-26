from __future__ import annotations

# scop: inline

import html
from typing import Any

import aiohttp
from telethon import events
from telethon.errors.rpcerrorlist import BadRequestError
from telethon.tl.functions.payments import (
    GetPaymentFormRequest,
    GetStarsStatusRequest,
    SendStarsFormRequest,
)
from telethon.tl.types import InputInvoiceStarGift, TextWithEntities
from telethon.utils import sanitize_parse_mode

import core.lib.loader.module_base as loader


class SenderGifts(loader.ModuleBase):
    """Модуль для отправки обычных и уникальных подарков Telegram прямо в чате."""

    name = "SenderGifts"
    version = "1.2.4"
    author = "@mead0wssMods x @nullmod"
    description = {
        "ru": "Отправка обычных и уникальных Telegram-подарков в чате",
        "en": "Send regular and unique Telegram gifts in chat",
    }
    banner_url = "https://files.catbox.moe/nie3ef.jpg"

    _messages = {
        "name": "SenderGifts",
        "usage": "<emoji document_id=4958526153955476488>❌</emoji> Используйте в формате: <code>.sendgift @username текст</code> или реплай + <code>.sendgift текст</code>",
        "checking_user": "<emoji document_id=5206634672204829887>🔍</emoji> Проверка пользователя...",
        "checking_balance": "<emoji document_id=5206634672204829887>🔍</emoji> Проверка баланса...",
        "user_not_found": "<emoji document_id=4958526153955476488>❌</emoji> Пользователь не найден",
        "gift_menu": "<tg-emoji emoji-id=5370781982886220096>🎁</tg-emoji> Выберите категорию подарков.\n\n<tg-emoji emoji-id=6048471184461271609>👤</tg-emoji> Пользователь: {}\n<tg-emoji emoji-id=6048762138430803961>📂</tg-emoji> Текст: {}\n<tg-emoji emoji-id=5321485469249198987>⭐️</tg-emoji> Баланс: {} звезд",
        "category_menu": "<tg-emoji emoji-id=5370781982886220096>🎁</tg-emoji> Подарки за {} ⭐\n\n<tg-emoji emoji-id=6048471184461271609>👤</tg-emoji> Пользователь: {}\n<tg-emoji emoji-id=6048762138430803961>📂</tg-emoji> Текст: {}",
        "unique_category_menu": "<tg-emoji emoji-id=5370781982886220096>🎁</tg-emoji> {}\n\n<tg-emoji emoji-id=6048471184461271609>👤</tg-emoji> Пользователь: {}\n<tg-emoji emoji-id=6048762138430803961>📂</tg-emoji> Текст: {}",
        "privacy_menu": "<tg-emoji emoji-id=5370781982886220096>🎁</tg-emoji> Выбран подарок: {}\n\nКак отправить подарок?",
        "sending_gift": "<emoji document_id=5201691993775818138>🛫</emoji> Отправка подарка...",
        "gift_sent": "<emoji document_id=5021905410089550576>✅</emoji> Подарок успешно отправлен!",
        "not_enough_stars": "<emoji document_id=4958526153955476488>❌</emoji> Недостаточно звезд для отправки подарка {}!",
        "min_stars_error": "<emoji document_id=4958526153955476488>❌</emoji> Недостаточно звезд для отправки минимального подарка!",
        "no_available_gifts": "<emoji document_id=4958526153955476488>❌</emoji> Нет доступных подарков для вашего баланса",
        "balance_error": "<emoji document_id=4958526153955476488>❌</emoji> Ошибка при проверке баланса",
        "user_disallowed_gifts": "<emoji document_id=4958526153955476488>❌</emoji> Данный пользователь не принимает подарки!",
        "btn_public": "📢 Публично",
        "btn_anon": "🕵️ Анонимно",
    }
    strings = {"ru": _messages, "en": _messages}

    regular_gifts: dict[int, list[dict[str, Any]]] = {
        15: [
            {"id": 5170145012310081615, "emoji": "❤️", "name": "Сердце"},
            {"id": 5170233102089322756, "emoji": "🧸", "name": "Мишка"},
        ],
        25: [
            {"id": 5170250947678437525, "emoji": "🎁", "name": "Подарок"},
            {"id": 5168103777563050263, "emoji": "🌹", "name": "Роза"},
        ],
        50: [
            {"id": 5170144170496491616, "emoji": "🎂", "name": "Тортик"},
            {"id": 5170314324215857265, "emoji": "💐", "name": "Цветы"},
            {"id": 5170564780938756245, "emoji": "🚀", "name": "Ракета"},
        ],
        100: [
            {"id": 5168043875654172773, "emoji": "🏆", "name": "Кубок"},
            {"id": 5170690322832818290, "emoji": "💍", "name": "Кольцо"},
            {"id": 5170521118301225164, "emoji": "💎", "name": "Алмаз"},
        ],
    }

    unique_gifts: dict[str, dict[str, Any]] = {
        "new_year": {
            "name": "🎄 Новогодние подарки",
            "gifts": [
                {"id": 5922558454332916696, "emoji": "🎄", "name": "Ёлка", "price": 50},
                {
                    "id": 5956217000635139069,
                    "emoji": "🧸",
                    "name": "Новогодний мишка",
                    "price": 50,
                },
            ],
        },
        "valentines": {
            "name": "💘 День святого валентина",
            "gifts": [
                {
                    "id": 5800655655995968830,
                    "emoji": "🧸",
                    "name": "14 Февраля мишка",
                    "price": 50,
                },
                {
                    "id": 5801108895304779062,
                    "emoji": "💘",
                    "name": "14 Февраля сердце",
                    "price": 50,
                },
            ],
        },
        "march_8th": {
            "name": "🌷 8 Марта",
            "gifts": [
                {
                    "id": 5866352046986232958,
                    "emoji": "🧸",
                    "name": "8 Марта мишка",
                    "price": 50,
                },
            ],
        },
        "saint_patricks_day": {
            "name": "💰 День святого патрика",
            "gifts": [
                {
                    "id": 5893356958802511476,
                    "emoji": "🧸",
                    "name": "Лепрекон мишка",
                    "price": 50,
                },
            ],
        },
        "april_1th": {
            "name": "🤪 1 Апреля",
            "gifts": [
                {
                    "id": 5935895822435615975,
                    "emoji": "🧸",
                    "name": "1 Апреля мишка",
                    "price": 50,
                },
            ],
        },
    }

    async def fetch_gifts_from_github(self) -> None:
        url = "https://raw.githubusercontent.com/mead0wsss/mead0wsMods/main/gifts.json"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=5) as response:
                    if response.status != 200:
                        return

                    data = await response.json(content_type=None)
                    if "regular_gifts" in data:
                        self.regular_gifts = {
                            int(price): gifts
                            for price, gifts in data["regular_gifts"].items()
                        }
                    if "unique_gifts" in data:
                        self.unique_gifts = data["unique_gifts"]
        except Exception as e:
            self.log.error(f"Не удалось загрузить подарки с GitHub: {e}")

    async def get_star_balance(self) -> int:
        try:
            balance_info = await self.client(GetStarsStatusRequest("me"))
            return int(balance_info.balance.amount)
        except Exception as e:
            self.log.error(f"Error getting balance: {e}")
            return 0

    async def _user_display(self, user_id: int) -> str:
        try:
            user = await self.client.get_entity(user_id)
            if getattr(user, "username", None):
                return f"@{html.escape(user.username)}"
            return html.escape(getattr(user, "first_name", None) or str(user_id))
        except Exception:
            return f"ID: {user_id}"

    async def _edit_form(
        self,
        call: events.CallbackQuery.Event,
        text: str,
        buttons: list[list[Any]] | None = None,
    ) -> None:
        await call.edit(text, buttons=buttons, parse_mode="html")
        await call.answer()

    @loader.command(
        "sendgift",
        doc_ru="<username> <text*> — отправить подарок пользователю",
        doc_en="<username> <text*> — send a Telegram gift",
    )
    async def cmd_sendgift(self, message: events.NewMessage.Event) -> None:
        await self.fetch_gifts_from_github()

        args = self.args_html(message)
        reply = await message.get_reply_message()
        if reply:
            user = reply.sender
            text = args or ""
        else:
            if not args:
                await self.edit(message, self.strings["usage"], parse_mode="html")
                return

            parts = args.split(maxsplit=1)
            if not parts:
                await self.edit(message, self.strings["usage"], parse_mode="html")
                return

            username: str | int = parts[0]
            text = parts[1] if len(parts) > 1 else ""
            if isinstance(username, str) and username.startswith("@"):
                username = username[1:]
            try:
                username = int(username)
            except (TypeError, ValueError):
                pass

            await self.edit(message, self.strings["checking_user"], parse_mode="html")
            try:
                user = await self.client.get_entity(username)
            except Exception as e:
                self.log.error(f"User not found: {e}")
                await self.edit(
                    message, self.strings["user_not_found"], parse_mode="html"
                )
                return

        await self.edit(message, self.strings["checking_balance"], parse_mode="html")
        try:
            balance = await self.get_star_balance()
            # balance = 100 # test
        except Exception as e:
            self.log.error(f"Balance error: {e}")
            await self.edit(message, self.strings["balance_error"], parse_mode="html")
            return

        min_price = min(self.regular_gifts.keys())
        if balance < min_price:
            await self.edit(message, self.strings["min_stars_error"], parse_mode="html")
            return

        buttons = [
            [
                self.Button.inline(
                    " ",
                    self._show_main_menu,
                    args=(user.id, text, balance, message.id),
                    ttl=900,
                )
            ]
        ]
        _, form_message = await self.inline(
            message.chat_id, "🪐", buttons=buttons, ttl=900
        )  # кастыль, да, иди нахуй
        if form_message:
            await form_message.click(0)
            try:
                await message.delete()
            except Exception:
                pass

    @loader.callback(ttl=900)
    async def _show_main_menu(
        self,
        call: events.CallbackQuery.Event,
        user_id: int,
        text: str,
        balance: int,
        msg_id: int,
    ) -> None:
        user_display = await self._user_display(user_id)
        buttons = [
            [
                self.Button.inline(
                    "🎁 Обычные подарки",
                    self._show_regular_categories,
                    args=(user_id, text, balance, msg_id),
                    ttl=900,
                )
            ],
            [
                self.Button.inline(
                    "✨ Уникальные подарки",
                    self._show_unique_categories,
                    args=(user_id, text, balance, msg_id),
                    ttl=900,
                )
            ],
        ]
        await self._edit_form(
            call,
            self.strings["gift_menu"].format(
                user_display, text if text else "-", balance
            ),
            buttons,
        )

    @loader.callback(ttl=900)
    async def _show_regular_categories(
        self,
        call: events.CallbackQuery.Event,
        user_id: int,
        text: str,
        balance: int,
        msg_id: int,
    ) -> None:
        user_display = await self._user_display(user_id)
        available_categories = [
            price for price in self.regular_gifts.keys() if balance >= price
        ]

        buttons: list[list[Any]] = []
        row: list[Any] = []
        for price in sorted(available_categories):
            row.append(
                self.Button.inline(
                    f"{price} ⭐",
                    self._show_category,
                    args=(user_id, price, text, balance, msg_id),
                    ttl=900,
                )
            )
            if len(row) == 2:
                buttons.append(row)
                row = []
        if row:
            buttons.append(row)

        buttons.append(
            [
                self.Button.inline(
                    "⬅️ Назад",
                    self._show_main_menu,
                    args=(user_id, text, balance, msg_id),
                    ttl=900,
                )
            ]
        )
        await self._edit_form(
            call,
            self.strings["gift_menu"].format(
                user_display, text if text else "-", balance
            ),
            buttons,
        )

    @loader.callback(ttl=900)
    async def _show_unique_categories(
        self,
        call: events.CallbackQuery.Event,
        user_id: int,
        text: str,
        balance: int,
        msg_id: int,
    ) -> None:
        user_display = await self._user_display(user_id)
        buttons: list[list[Any]] = []
        for cat_id, cat_data in self.unique_gifts.items():
            if any(balance >= gift["price"] for gift in cat_data["gifts"]):
                buttons.append(
                    [
                        self.Button.inline(
                            cat_data["name"],
                            self._show_unique_category_gifts,
                            args=(user_id, cat_id, text, balance, msg_id),
                            ttl=900,
                        )
                    ]
                )

        if not buttons:
            buttons.append(
                [
                    self.Button.inline(
                        "❌ Нет доступных (баланс)",
                        self._show_main_menu,
                        args=(user_id, text, balance, msg_id),
                        ttl=900,
                    )
                ]
            )

        buttons.append(
            [
                self.Button.inline(
                    "⬅️ Назад",
                    self._show_main_menu,
                    args=(user_id, text, balance, msg_id),
                    ttl=900,
                )
            ]
        )
        await self._edit_form(
            call,
            self.strings["gift_menu"].format(
                user_display, text if text else "-", balance
            ),
            buttons,
        )

    @loader.callback(ttl=900)
    async def _show_category(
        self,
        call: events.CallbackQuery.Event,
        user_id: int,
        price: int,
        text: str,
        balance: int,
        msg_id: int,
    ) -> None:
        gifts = self.regular_gifts[price]
        buttons: list[list[Any]] = []
        row: list[Any] = []
        for gift in gifts:
            row.append(
                self.Button.inline(
                    gift["emoji"],
                    self._select_privacy,
                    args=(
                        user_id,
                        gift["id"],
                        text,
                        gift["emoji"],
                        msg_id,
                        balance,
                        "regular",
                        price,
                    ),
                    ttl=900,
                )
            )
            if len(row) == 3:
                buttons.append(row)
                row = []

        if row:
            buttons.append(row)
        buttons.append(
            [
                self.Button.inline(
                    "⬅️ Назад",
                    self._show_regular_categories,
                    args=(user_id, text, balance, msg_id),
                    ttl=900,
                )
            ]
        )

        user_display = await self._user_display(user_id)
        await self._edit_form(
            call,
            self.strings["category_menu"].format(
                price, user_display, text if text else "-"
            ),
            buttons,
        )

    @loader.callback(ttl=900)
    async def _show_unique_category_gifts(
        self,
        call: events.CallbackQuery.Event,
        user_id: int,
        cat_id: str,
        text: str,
        balance: int,
        msg_id: int,
    ) -> None:
        category = self.unique_gifts[cat_id]
        buttons: list[list[Any]] = []
        row: list[Any] = []
        for gift in category["gifts"]:
            if balance >= gift["price"]:
                row.append(
                    self.Button.inline(
                        gift["emoji"],
                        self._select_privacy,
                        args=(
                            user_id,
                            gift["id"],
                            text,
                            gift["emoji"],
                            msg_id,
                            balance,
                            "unique",
                            cat_id,
                        ),
                        ttl=900,
                    )
                )
            if len(row) == 3:
                buttons.append(row)
                row = []

        if row:
            buttons.append(row)
        buttons.append(
            [
                self.Button.inline(
                    "⬅️ Назад",
                    self._show_unique_categories,
                    args=(user_id, text, balance, msg_id),
                    ttl=900,
                )
            ]
        )

        user_display = await self._user_display(user_id)
        await self._edit_form(
            call,
            self.strings["unique_category_menu"].format(
                category["name"], user_display, text if text else "-"
            ),
            buttons,
        )

    @loader.callback(ttl=900)
    async def _select_privacy(
        self,
        call: events.CallbackQuery.Event,
        user_id: int,
        gift_id: int,
        text: str,
        gift_emoji: str,
        msg_id: int,
        balance: int,
        gift_type: str,
        type_arg: int | str,
    ) -> None:
        back_callback = (
            self._show_category
            if gift_type == "regular"
            else self._show_unique_category_gifts
        )
        buttons = [
            [
                self.Button.inline(
                    self.strings["btn_public"],
                    self._send_gift,
                    args=(user_id, gift_id, text, gift_emoji, msg_id, balance, False),
                    ttl=900,
                ),
                self.Button.inline(
                    self.strings["btn_anon"],
                    self._send_gift,
                    args=(user_id, gift_id, text, gift_emoji, msg_id, balance, True),
                    ttl=900,
                ),
            ],
            [
                self.Button.inline(
                    "⬅️ Назад",
                    back_callback,
                    args=(user_id, type_arg, text, balance, msg_id),
                    ttl=900,
                )
            ],
        ]
        await self._edit_form(
            call, self.strings["privacy_menu"].format(gift_emoji), buttons
        )

    @loader.callback(ttl=900)
    async def _send_gift(
        self,
        call: events.CallbackQuery.Event,
        user_id: int,
        gift_id: int,
        text: str,
        gift_emoji: str,
        msg_id: int,
        balance: int,
        hide_name: bool,
    ) -> None:
        try:
            await call.edit(
                self.strings["sending_gift"], buttons=None, parse_mode="html"
            )
            await call.answer()

            parse_mode = sanitize_parse_mode(self.client.parse_mode)
            parsed_text, entities = parse_mode.parse(text)
            user = await self.client.get_input_entity(user_id)
            invoice = InputInvoiceStarGift(
                user,
                gift_id,
                hide_name=hide_name,
                message=(
                    TextWithEntities(parsed_text, entities)
                    if parsed_text
                    else TextWithEntities("", [])
                ),
            )
            form = await self.client(GetPaymentFormRequest(invoice))
            await self.client(SendStarsFormRequest(form.form_id, invoice))

            await call.edit(self.strings["gift_sent"], parse_mode="html")
        except BadRequestError as e:
            error_text = str(e)
            if "BALANCE_TOO_LOW" in error_text:
                await call.edit(
                    self.strings["not_enough_stars"].format(gift_emoji),
                    buttons=None,
                    parse_mode="html",
                )
            elif "USER_DISALLOWED_STARGIFTS" in error_text:
                await call.edit(
                    self.strings["user_disallowed_gifts"],
                    buttons=None,
                    parse_mode="html",
                )
            else:
                self.log.error(f"Error sending gift: {e}")
                await call.edit(
                    f"<emoji document_id=4958526153955476488>❌</emoji> Ошибка при отправке подарка: {html.escape(error_text)}",
                    buttons=None,
                    parse_mode="html",
                )
        except Exception as e:
            self.log.error(f"Error sending gift: {e}")
            await call.edit(
                f"<emoji document_id=4958526153955476488>❌</emoji> Ошибка при отправке подарка: {html.escape(str(e))}",
                buttons=None,
                parse_mode="html",
            )
