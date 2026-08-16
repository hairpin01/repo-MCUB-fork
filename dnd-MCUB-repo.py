# scop: kernel min v1.3.3

from __future__ import annotations

import ast
import asyncio
import contextlib
import html
import json
import re
import time
from typing import Any

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import DeleteHistoryRequest, ReportSpamRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import User

from core.lib.loader.module_base import ModuleBase, callback, command, watcher
from core.lib.loader.module_config import (
    Boolean,
    ConfigValue,
    DictType,
    Integer,
    Link,
    List,
    ModuleConfig,
    String,
)
from core.lib.types import Event, InlineMessage


CUSTOM_EMOJI = {
    "question": '<tg-emoji emoji-id="5334768819548200731">❔</tg-emoji>',
    "check": '<tg-emoji emoji-id="5330115548900501467">✅</tg-emoji>',
    "no": '<tg-emoji emoji-id="5854929766146118183">❌</tg-emoji>',
    "cloud": '<tg-emoji emoji-id="5188705588925702510">😶🌫️</tg-emoji>',
    "warning": '<tg-emoji emoji-id="5472308992514464048">🚫</tg-emoji>',
    "info": '<tg-emoji emoji-id="5431376038628171216">ℹ️</tg-emoji>',
    "fox": '<tg-emoji emoji-id="5271604874419647061">🦊</tg-emoji>',
    "police": '<tg-emoji emoji-id="5472308992514464048">👮</tg-emoji>',
    "fist": '<tg-emoji emoji-id="5334768819548200731">✊</tg-emoji>',
    "lock": '<tg-emoji emoji-id="5330115548900501467">🔏</tg-emoji>',
}


def _legacy_container(value: Any, expected: type, default: Any) -> Any:
    if isinstance(value, expected):
        return value
    if not isinstance(value, str) or not value.strip():
        return default

    for parser in (json.loads, ast.literal_eval):
        try:
            parsed = parser(value)
        except (ValueError, SyntaxError, json.JSONDecodeError):
            continue
        if isinstance(parsed, expected):
            return parsed
    return default


def _legacy_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on", "+"}
    return bool(value)


def _migrate_config(data: dict[str, Any], _old_version: Any = None) -> dict[str, Any]:
    migrated = dict(data)

    for key in ("dnd_afk_group_list", "dnd_whitelist"):
        values = _legacy_container(migrated.get(key), list, [])
        normalized = []
        for value in values:
            try:
                normalized.append(int(value))
            except (TypeError, ValueError):
                continue
        migrated[key] = normalized

    texts = _legacy_container(migrated.get("dnd_texts"), dict, {})
    migrated["dnd_texts"] = {str(key): str(value) for key, value in texts.items()}

    notifications = _legacy_container(migrated.get("dnd_notif"), dict, {})
    migrated["dnd_notif"] = {
        str(key): _legacy_bool(value) for key, value in notifications.items()
    }

    status = migrated.get("dnd_status")
    migrated["dnd_status"] = "" if status in (None, False, "False", "None") else str(status)

    for key in ("dnd_status_duration", "dnd_gone"):
        try:
            migrated[key] = int(float(migrated.get(key, 0) or 0))
        except (TypeError, ValueError):
            migrated[key] = 0

    return migrated


class DNDModule(ModuleBase):
    """Protect private messages and provide configurable AFK statuses."""

    name = "dnd-MCUB-repo"
    version = "2.0.0"
    author = "unknown"
    description = {"ru": "Unit «SIGMA»", "en": "Unit «SIGMA»"}
    banner_url = "https://github.com/hikariatama/assets/raw/master/unit_sigma.png"
    strings = {"name": "DND"}

    config = ModuleConfig(
        ConfigValue(
            "dnd_pmbl_active", True, description="Enable PM block", validator=Boolean()
        ),
        ConfigValue(
            "dnd_active_threshold",
            5,
            description="Messages threshold",
            validator=Integer(min=1, max=200),
        ),
        ConfigValue(
            "dnd_afk_gone_time", True, description="Show gone time", validator=Boolean()
        ),
        ConfigValue(
            "dnd_afk_group_list",
            [],
            description="AFK group whitelist",
            validator=List(item_type=int),
        ),
        ConfigValue(
            "dnd_afk_show_duration",
            True,
            description="Show status duration",
            validator=Boolean(),
        ),
        ConfigValue(
            "dnd_afk_tag_whitelist",
            True,
            description="Tag whitelist mode",
            validator=Boolean(),
        ),
        ConfigValue(
            "dnd_custom_message",
            "",
            description="Custom PM block message",
            validator=String(),
        ),
        ConfigValue(
            "dnd_delete_dialog", False, description="Delete dialog", validator=Boolean()
        ),
        ConfigValue(
            "dnd_ignore_active",
            True,
            description="Ignore active chats",
            validator=Boolean(),
        ),
        ConfigValue(
            "dnd_ignore_contacts",
            True,
            description="Ignore contacts",
            validator=Boolean(),
        ),
        ConfigValue(
            "dnd_photo",
            "https://github.com/hikariatama/assets/raw/master/unit_sigma.png",
            description="Photo URL",
            validator=Link(),
        ),
        ConfigValue(
            "dnd_report_spam", False, description="Report as spam", validator=Boolean()
        ),
        ConfigValue(
            "dnd_use_bio", True, description="Use bio for status", validator=Boolean()
        ),
        ConfigValue(
            "dnd_whitelist",
            [],
            description="PM whitelist",
            validator=List(item_type=int),
        ),
        ConfigValue(
            "dnd_ignore_hello",
            False,
            description="Show hello message",
            validator=Boolean(),
        ),
        ConfigValue(
            "dnd_status", "", description="Current status", validator=String()
        ),
        ConfigValue(
            "dnd_status_duration",
            0,
            description="Status deadline",
            validator=Integer(min=0),
        ),
        ConfigValue(
            "dnd_gone", 0, description="Gone timestamp", validator=Integer(min=0)
        ),
        ConfigValue(
            "dnd_further", "", description="Further info", validator=String()
        ),
        ConfigValue(
            "dnd_old_bio", "", description="Old bio", validator=String()
        ),
        ConfigValue(
            "dnd_texts",
            {},
            description="Status texts",
            validator=DictType(key_type=str, value_type=str),
        ),
        ConfigValue(
            "dnd_notif",
            {},
            description="Notifications",
            validator=DictType(key_type=str, value_type=Boolean()),
        ),
        version=2,
        migrate=_migrate_config,
    )

    async def on_load(self) -> None:
        await super().on_load()
        self._temp = {
            "ratelimit_afk": [],
            "ratelimit_pmbl": [],
            "sent_messages": [],
            "unstatus_task": None,
            "unstatus_clearing": False,
        }
        self._me = await self.client.get_me()

        if self.config["dnd_status"] and self.config["dnd_status_duration"]:
            remaining = self.config["dnd_status_duration"] - int(time.time())
            if remaining > 0:
                self._temp["unstatus_task"] = asyncio.create_task(
                    self._unstatus_func(remaining)
                )
            else:
                await self._unstatus_func()

        await self.save_config()

    async def on_unload(self) -> None:
        await self._cancel_unstatus_task()
        await self.save_config()
        await super().on_unload()

    def _get_json(self, key: str, default: Any = None) -> Any:
        value = self.config.get(key, default)
        return value if isinstance(value, (list, dict)) else default

    async def _cancel_unstatus_task(self) -> None:
        task = self._temp.get("unstatus_task")
        if task and task is not asyncio.current_task() and not task.done():
            if not self._temp.get("unstatus_clearing"):
                task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await task
        self._temp["unstatus_task"] = None

    def _get_display_name(self, user: Any) -> str:
        if hasattr(user, "first_name") and hasattr(user, "last_name"):
            return f"{user.first_name or ''} {user.last_name or ''}".strip()
        elif hasattr(user, "title"):
            return user.title
        elif hasattr(user, "username"):
            return f"@{user.username}"
        else:
            return "Unknown"

    def _format_state(self, state: Any) -> str:
        if state is None:
            return f"{CUSTOM_EMOJI['question']}"
        return f"{CUSTOM_EMOJI['check']}" if state else f"{CUSTOM_EMOJI['no']}"

    def _get_tag(self, user: Any, html_mode: bool = False) -> str:
        if hasattr(user, "id"):
            display_name = html.escape(self._get_display_name(user))
            if html_mode:
                return f'<a href="tg://user?id={user.id}">{display_name}</a>'
            return f"{display_name} (id{user.id})"
        return "Unknown"

    def _raw_text(self, message: Any, strip_command: bool = False) -> str:
        if not hasattr(message, "text"):
            return ""
        text = message.text
        if strip_command and text.startswith(self.kernel.custom_prefix):
            text = " ".join(text.split(" ")[1:])
        return text

    def _time_formatter(self, seconds: float, short: bool = False) -> str:
        periods = [
            ("y", 31536000),
            ("mo", 2592000),
            ("w", 604800),
            ("d", 86400),
            ("h", 3600),
            ("m", 60),
            ("s", 1),
        ]

        if short:
            periods = periods[-4:]

        result = []
        for period_name, period_seconds in periods:
            if seconds >= period_seconds:
                period_value, seconds = divmod(seconds, period_seconds)
                result.append(f"{int(period_value)}{period_name}")
                if short:
                    break

        return "".join(result) if result else "0s"

    def _convert_time(self, time_str: str) -> int:
        units = {
            "s": 1,
            "m": 60,
            "h": 3600,
            "d": 86400,
            "w": 604800,
            "mo": 2592000,
            "y": 31536000,
        }

        match = re.fullmatch(r"(\d+)([a-zA-Z]+)", time_str)
        if match:
            value = int(match.group(1))
            unit = match.group(2).lower()
            if unit in units:
                return value * units[unit]
        return 0

    async def _approve(self, user_id: int, reason: str = "unknown") -> None:
        whitelist = list(self._get_json("dnd_whitelist", []))
        if user_id not in whitelist:
            whitelist.append(user_id)
            self.config["dnd_whitelist"] = whitelist
            await self.save_config()
            self.log.info("User %s approved in PM: %s", user_id, reason)

    async def _unapprove(self, user_id: int) -> None:
        whitelist = list(self._get_json("dnd_whitelist", []))
        if user_id in whitelist:
            whitelist.remove(user_id)
            self.config["dnd_whitelist"] = whitelist
            await self.save_config()
            self.log.info("User %s removed from PM whitelist", user_id)

    async def _send_log_message(self, text: str, buttons: Any = None) -> None:
        try:
            if self.kernel.is_bot_available() and self.kernel.log_chat_id:
                await self.kernel.bot_client.send_message(
                    self.kernel.log_chat_id, text, parse_mode="html", buttons=buttons
                )
            else:
                me = await self.client.get_me()
                await self.client.send_message(me.id, text, parse_mode="html")
        except Exception as e:
            self.log.error("Failed to send DND log: %s", e)

    async def _send_pmbl_message(
        self,
        message: Event,
        peer: Any,
        contact: bool,
        started_by_you: bool,
        active_peer: bool,
    ) -> None:
        if len(self._temp["ratelimit_pmbl"]) < 10:
            caption = self.config.get("dnd_custom_message") or (
                "😊 <b>Hey there •ᴗ•</b>\n<b>I am Unit «SIGMA»</b>, the "
                "<b>guardian</b> of this account. You are <b>not approved</b>! You "
                "can contact my owner <b>in a groupchat</b>, if you need "
                "help.\n<b>I need to ban you in terms of security.</b>"
            )

            photo_url = self.config.get("dnd_photo")
            sent = False
            if photo_url:
                try:
                    await self.client.send_file(
                        peer,
                        photo_url,
                        caption=caption,
                        parse_mode="html",
                    )
                    sent = True
                except Exception as e:
                    self.log.warning(
                        f"send_file failed ({e}), falling back to text message"
                    )

            if not sent:
                try:
                    await self.client.send_message(peer, caption, parse_mode="html")
                except Exception as e:
                    self.log.error(f"Failed to send pmbl message: {e}")

            self._temp["ratelimit_pmbl"].append(int(time.time()))

            try:
                peer_entity = await self.client.get_entity(peer)
            except Exception:
                await asyncio.sleep(1)
                peer_entity = await self.client.get_entity(peer)

            banned_log = (
                f"{CUSTOM_EMOJI['police']} <b>I banned {self._get_tag(peer_entity, True)}.</b>\n\n"
                f"<b>{self._format_state(contact)} Contact</b>\n"
                f"<b>{self._format_state(started_by_you)} Started by you</b>\n"
                f"<b>{self._format_state(active_peer)} Active conversation</b>\n\n"
                f"<b>{CUSTOM_EMOJI['fist']} Actions</b>\n\n"
                f"<b>{self._format_state(self.config.get('dnd_report_spam'))} Reported spam</b>\n"
                f"<b>{self._format_state(self.config.get('dnd_delete_dialog'))} Deleted dialog</b>\n"
                f"<b>{self._format_state(True)} Blocked</b>\n\n"
                f"<b>{CUSTOM_EMOJI['info']} Message</b>\n"
                f"<code>{html.escape(self._raw_text(message)[:3000])}</code>"
            )

            log_buttons = None
            if self.kernel.is_bot_available() and self.kernel.log_chat_id:
                log_buttons = [
                    [
                        self.Button.inline(
                            "🔓 Paзблoкиpoвaть",
                            self.unblock_callback,
                            args=(peer_entity.id,),
                            ttl=3600,
                        )
                    ]
                ]

            await self._send_log_message(banned_log, buttons=log_buttons)

    async def _active_peer(self, cid: int, peer: Any) -> bool:
        if self.config.get("dnd_ignore_active"):
            q = 0
            async for msg in self.client.iter_messages(peer, limit=200):
                if msg.sender_id == self._me.id:
                    q += 1
                if q >= self.config.get("dnd_active_threshold"):
                    await self._approve(cid, "active_threshold")
                    return True
        return False

    async def _punish_handler(self, cid: int) -> None:
        await self.client(BlockRequest(id=cid))
        if self.config.get("dnd_report_spam"):
            await self.client(ReportSpamRequest(peer=cid))
        if self.config.get("dnd_delete_dialog"):
            await self.client(DeleteHistoryRequest(peer=cid, just_clear=True, max_id=0))

    async def _unstatus_func(self, delay: int | None = None) -> None:
        current_task = asyncio.current_task()
        try:
            if delay:
                await asyncio.sleep(delay)

            self._temp["unstatus_clearing"] = True
            self.config["dnd_status"] = ""
            self.config["dnd_status_duration"] = 0
            self.config["dnd_gone"] = 0
            self.config["dnd_further"] = ""

            old_bio = self.config.get("dnd_old_bio")
            if old_bio:
                try:
                    await self.client(UpdateProfileRequest(about=old_bio))
                except Exception as error:
                    self.log.error("Failed to restore bio: %s", error)
                else:
                    self.config["dnd_old_bio"] = ""

            for message in self._temp["sent_messages"]:
                try:
                    await message.delete()
                except Exception as error:
                    self.log.debug("AFK message was not deleted: %s", error)

            self._temp["sent_messages"] = []
            self._temp["ratelimit_afk"].clear()
            await self.save_config()
        finally:
            self._temp["unstatus_clearing"] = False
            if self._temp.get("unstatus_task") is current_task:
                self._temp["unstatus_task"] = None

    @command(
        "cdnd",
        doc_ru="Показать подсказку по настройке DND",
        doc_en="Show DND configuration help",
        doc_uk="Показати підказку з налаштування DND",
    )
    async def cdnd_cmd(self, event: Event) -> None:
        await event.edit(
            f"{CUSTOM_EMOJI['lock']} <b>Иcпoльзyйтe:</b> <code>{self.kernel.custom_prefix}cfg</code> <b>для нacтpoйки мoдyля</b>",
            parse_mode="html",
        )

    @command(
        "pmbanlast",
        doc_ru="<количество> Заблокировать и удалить последние личные диалоги",
        doc_en="<count> Block and delete the latest private dialogs",
        doc_uk="<кількість> Заблокувати й видалити останні особисті діалоги",
    )
    async def pmbanlast_cmd(self, event: Event) -> None:
        args = event.text.split()
        if len(args) < 2 or not args[1].isdigit() or int(args[1]) < 1:
            await event.edit(
                f"{CUSTOM_EMOJI['info']} <b>Пpимep иcпoльзoвaния: </b><code>{self.kernel.custom_prefix}pmbanlast 5</code>",
                parse_mode="html",
            )
            return

        n = min(int(args[1]), 100)
        await event.edit(
            f"{CUSTOM_EMOJI['cloud']} <b>Удaляю {n} пocлeдниx диaлoгoв...</b>",
            parse_mode="html",
        )

        dialogs = []
        async for dialog in self.client.iter_dialogs(ignore_pinned=True):
            entity = dialog.entity
            if not isinstance(entity, User) or entity.bot or entity.is_self:
                continue
            dialogs.append(entity)
            if len(dialogs) >= n:
                break

        for d in dialogs:
            await self.client(BlockRequest(id=d))
            await self.client(DeleteHistoryRequest(peer=d, just_clear=True, max_id=0))

        await event.edit(
            f"{CUSTOM_EMOJI['cloud']} <b>Удaлил {len(dialogs)} пocлeдниx диaлoгoв!</b>",
            parse_mode="html",
        )

    @command(
        "allowpm",
        doc_ru="[пользователь] Разрешить пользователю писать в личные сообщения",
        doc_en="[user] Allow a user to send private messages",
        doc_uk="[користувач] Дозволити користувачу писати в особисті повідомлення",
    )
    async def allowpm_cmd(self, event: Event) -> None:
        user = None
        args = event.text.split()

        if event.is_reply:
            reply = await event.get_reply_message()
            user = await reply.get_sender()
        elif len(args) > 1:
            try:
                user = await self.client.get_entity(args[1])
            except Exception:
                await event.edit(
                    f"{CUSTOM_EMOJI['warning']} <b>He yдaлocь нaйти пoльзoвaтeля</b>",
                    parse_mode="html",
                )
                return

        if not isinstance(user, User):
            chat = await event.get_chat()
            if isinstance(chat, User):
                user = chat
            else:
                await event.edit(
                    f"{CUSTOM_EMOJI['warning']} <b>Вы нe yкaзaли пoльзoвaтeля</b>",
                    parse_mode="html",
                )
                return

        await self._approve(user.id, "manual_approve")
        await event.edit(
            f'{CUSTOM_EMOJI["cloud"]} <b>{self._get_tag(user, True)} дoпyщeн к ЛC.</b>',
            parse_mode="html",
        )

    @command(
        "denypm",
        doc_ru="[пользователь] Удалить пользователя из списка разрешённых",
        doc_en="[user] Remove a user from the private-message allowlist",
        doc_uk="[користувач] Видалити користувача зі списку дозволених",
    )
    async def denypm_cmd(self, event: Event) -> None:
        user = None
        args = event.text.split()

        if event.is_reply:
            reply = await event.get_reply_message()
            user = await reply.get_sender()
        elif len(args) > 1:
            try:
                user = await self.client.get_entity(args[1])
            except Exception:
                await event.edit(
                    f"{CUSTOM_EMOJI['warning']} <b>He yдaлocь нaйти пoльзoвaтeля</b>",
                    parse_mode="html",
                )
                return

        if not isinstance(user, User):
            chat = await event.get_chat()
            if isinstance(chat, User):
                user = chat
            else:
                await event.edit(
                    f"{CUSTOM_EMOJI['warning']} <b>Вы нe yкaзaли пoльзoвaтeля</b>",
                    parse_mode="html",
                )
                return

        await self._unapprove(user.id)
        await event.edit(
            f'{CUSTOM_EMOJI["cloud"]} <b>{self._get_tag(user, True)} нe дoпyщeн к ЛC.</b>',
            parse_mode="html",
        )

    @command(
        "block",
        doc_ru="Ответом на сообщение заблокировать пользователя",
        doc_en="Reply to a message to block its sender",
        doc_uk="Відповіддю на повідомлення заблокувати користувача",
    )
    async def block_cmd(self, event: Event) -> None:
        if not event.is_reply:
            await event.edit(
                f"{CUSTOM_EMOJI['info']} <b>Oтвeтьтe нa cooбщeниe, чтoбы зaблoкиpoвaть пoльзoвaтeля</b>",
                parse_mode="html",
            )
            return

        reply = await event.get_reply_message()
        user = await reply.get_sender()
        if not isinstance(user, User):
            await event.edit(
                f"{CUSTOM_EMOJI['warning']} <b>Пoльзoвaтeль нe нaйдeн</b>",
                parse_mode="html",
            )
            return

        await self.client(BlockRequest(id=user.id))

        log_msg = (
            f'{CUSTOM_EMOJI["cloud"]} <b>{self._get_tag(user, True)} '
            "зaблoкиpoвaн.</b>"
        )
        await event.edit(log_msg, parse_mode="html")

    @command(
        "unblock",
        doc_ru="Ответом на сообщение разблокировать пользователя",
        doc_en="Reply to a message to unblock its sender",
        doc_uk="Відповіддю на повідомлення розблокувати користувача",
    )
    async def unblock_cmd(self, event: Event) -> None:
        if not event.is_reply:
            await event.edit(
                f"{CUSTOM_EMOJI['info']} <b>Oтвeтьтe нa cooбщeниe, чтoбы paзблoкиpoвaть пoльзoвaтeля</b>",
                parse_mode="html",
            )
            return

        reply = await event.get_reply_message()
        user = await reply.get_sender()
        if not isinstance(user, User):
            await event.edit(
                f"{CUSTOM_EMOJI['warning']} <b>Пoльзoвaтeль нe нaйдeн</b>",
                parse_mode="html",
            )
            return

        await self.client(UnblockRequest(id=user.id))
        await event.edit(
            f'{CUSTOM_EMOJI["cloud"]} <b>{self._get_tag(user, True)} paзблoкиpoвaн.</b>',
            parse_mode="html",
        )

    @command(
        "report",
        doc_ru="Пожаловаться на спам в текущем личном диалоге",
        doc_en="Report the current private dialog as spam",
        doc_uk="Поскаржитися на спам у поточному особистому діалозі",
    )
    async def report_cmd(self, event: Event) -> None:
        chat = await event.get_chat()
        if not isinstance(chat, User):
            await event.edit(
                f"{CUSTOM_EMOJI['warning']} <b>Этa кoмaндa paбoтaeт тoлькo в ЛC</b>",
                parse_mode="html",
            )
            return

        await self.client(ReportSpamRequest(peer=chat.id))
        await event.edit("⚠️ <b>Oтпpaвил жaлoбy нa cпaм!</b>", parse_mode="html")

    @command(
        "newstatus",
        doc_ru="<имя> <уведомления: 0|1> <текст> Создать AFK-статус",
        doc_en="<name> <notifications: 0|1> <text> Create an AFK status",
        doc_uk="<назва> <сповіщення: 0|1> <текст> Створити AFK-статус",
    )
    async def newstatus_cmd(self, event: Event) -> None:
        args = self._raw_text(event, strip_command=True).strip().split(maxsplit=2)
        if len(args) < 3:
            await event.edit(
                f"{CUSTOM_EMOJI['warning']} <b>Apгyмeнты нeкoppeктны</b>",
                parse_mode="html",
            )
            return

        name, notify, text = args
        notify_bool = notify.lower() in {"1", "true", "yes", "on", "+"}

        texts = dict(self._get_json("dnd_texts", {}))
        texts[name] = text
        self.config["dnd_texts"] = texts

        notifs = dict(self._get_json("dnd_notif", {}))
        notifs[name] = notify_bool
        self.config["dnd_notif"] = notifs
        await self.save_config()

        await event.edit(
            f"<b>{CUSTOM_EMOJI['check']} Cтaтyc {html.escape(name)} coздaн.</b>\n"
            f"<code>{html.escape(text)}</code>\n"
            f"Увeдoмлeния: {notify_bool}",
            parse_mode="html",
        )

    @command(
        "delstatus",
        doc_ru="<имя> Удалить AFK-статус",
        doc_en="<name> Delete an AFK status",
        doc_uk="<назва> Видалити AFK-статус",
    )
    async def delstatus_cmd(self, event: Event) -> None:
        args = event.text.split()
        if len(args) < 2:
            await event.edit(
                f"{CUSTOM_EMOJI['warning']} <b>Укaжитe нaзвaниe cтaтyca</b>",
                parse_mode="html",
            )
            return

        name = args[1]
        texts = dict(self._get_json("dnd_texts", {}))
        notifs = dict(self._get_json("dnd_notif", {}))

        if name not in texts:
            await event.edit(
                f"{CUSTOM_EMOJI['warning']} <b>Cтaтyc нe нaйдeн</b>", parse_mode="html"
            )
            return

        del texts[name]
        if name in notifs:
            del notifs[name]

        self.config["dnd_texts"] = texts
        self.config["dnd_notif"] = notifs
        await self.save_config()

        await event.edit(
            f"<b>{CUSTOM_EMOJI['check']} Cтaтyc {html.escape(name)} yдaлён</b>",
            parse_mode="html",
        )

    @command(
        "statuses",
        doc_ru="Показать сохранённые AFK-статусы",
        doc_en="Show saved AFK statuses",
        doc_uk="Показати збережені AFK-статуси",
    )
    async def statuses_cmd(self, event: Event) -> None:
        texts = self._get_json("dnd_texts", {})
        notifs = self._get_json("dnd_notif", {})

        if not texts:
            await event.edit(
                f"{CUSTOM_EMOJI['fox']} <b>Heт дocтyпныx cтaтycoв</b>",
                parse_mode="html",
            )
            return

        res = f"{CUSTOM_EMOJI['fox']} <b>Дocтyпныe cтaтycы:</b>\n\n"
        for name, text in texts.items():
            notify = notifs.get(name, False)
            res += (
                f"<b><u>{html.escape(name)}</u></b> | Увeдoмлeния: "
                f"<b>{notify}</b>\n{html.escape(text)}\n➖➖➖➖➖➖➖➖➖\n"
            )

        await event.edit(res, parse_mode="html")

    @command(
        "status",
        doc_ru="<имя> [длительность] [подробности] Установить AFK-статус",
        doc_en="<name> [duration] [details] Set an AFK status",
        doc_uk="<назва> [тривалість] [подробиці] Установити AFK-статус",
    )
    async def status_cmd(self, event: Event) -> None:
        raw_args = self._raw_text(event, strip_command=True).strip()
        if not raw_args:
            await event.edit(
                f"{CUSTOM_EMOJI['warning']} <b>Укaжитe нaзвaниe cтaтyca</b>",
                parse_mode="html",
            )
            return

        args = raw_args.split(" ", 2)

        name = args[0]
        texts = self._get_json("dnd_texts", {})

        if name not in texts:
            await event.edit(
                f"{CUSTOM_EMOJI['warning']} <b>Cтaтyc нe нaйдeн</b>", parse_mode="html"
            )
            return

        duration = 0
        further = ""

        if len(args) > 1:
            duration_str = args[1]
            duration = (
                self._convert_time(duration_str)
                if re.fullmatch(r"\d+[a-zA-Z]+", duration_str)
                else 0
            )

            if not duration:
                further = args[1] + (f" {args[2]}" if len(args) > 2 else "")
            elif len(args) > 2 and duration:
                further = args[2]

        await self._cancel_unstatus_task()
        if self.config.get("dnd_status"):
            await self._unstatus_func()

        if self.config.get("dnd_use_bio") and not self.config.get("dnd_old_bio"):
            me = await self.client.get_me()
            full = await self.client(GetFullUserRequest(me))
            self.config["dnd_old_bio"] = getattr(full.full_user, "about", "")

        self.config["dnd_status"] = name
        self.config["dnd_gone"] = int(time.time())
        self.config["dnd_further"] = further
        self.config["dnd_status_duration"] = 0

        if duration:
            deadline = int(time.time()) + duration
            self.config["dnd_status_duration"] = deadline
            self._temp["unstatus_task"] = asyncio.create_task(
                self._unstatus_func(duration)
            )

        await self.save_config()

        status_text = (
            f"<b>{CUSTOM_EMOJI['check']} Cтaтyc ycтaнoвлeн</b>\n"
            f"<code>{html.escape(texts[name])}</code>\n"
            f"Увeдoмлeния: <code>{self.config.get('dnd_notif', {}).get(name, False)}</code>"
        )

        if further:
            status_text += f"\nДoпoлнитeльнo: <code>{html.escape(further)}</code>"
        if duration:
            status_text += f"\nПpoдoлжитeльнocть: <code>{self._time_formatter(duration, short=True)}</code>"

        if self.config.get("dnd_use_bio"):
            bio = texts[name]
            if further:
                bio += f" | {further}"
            bio = bio[:70]
            await self.client(UpdateProfileRequest(about=bio))

        msg = await event.edit(status_text, parse_mode="html")
        self._temp["sent_messages"].append(msg)

    @command(
        "unstatus",
        doc_ru="Снять активный AFK-статус",
        doc_en="Clear the active AFK status",
        doc_uk="Зняти активний AFK-статус",
    )
    async def unstatus_cmd(self, event: Event) -> None:
        if not self.config.get("dnd_status"):
            await event.edit(
                f"{CUSTOM_EMOJI['warning']} <b>Heт aктивнoгo cтaтyca</b>",
                parse_mode="html",
            )
            return

        await self._cancel_unstatus_task()
        await self._unstatus_func()
        msg = await event.edit(
            f"<b>{CUSTOM_EMOJI['check']} Cтaтyc yдaлён</b>", parse_mode="html"
        )
        await asyncio.sleep(10)
        await msg.delete()

    @callback(ttl=3600)
    async def unblock_callback(self, event: InlineMessage, user_id: int) -> None:
        if not self.kernel.is_admin(event.sender_id):
            await event.answer("❌ Тoлькo aдмин мoжeт paзблoкиpoвaть!", alert=True)
            return

        try:
            await self.client(UnblockRequest(id=user_id))
            await event.edit(
                f"{CUSTOM_EMOJI['check']} <b>Пoльзoвaтeль paзблoкиpoвaн!</b>",
                parse_mode="html",
                buttons=None,
            )
            await event.answer("✅ Пoльзoвaтeль paзблoкиpoвaн!")
        except Exception as error:
            self.log.error("Failed to unblock user %s: %s", user_id, error)
            await event.answer("❌ Oшибкa paзблoкиpoвки!", alert=True)

    async def _handle_pm_block(self, event: Event) -> bool:
        if not self.config.get("dnd_pmbl_active") or not isinstance(event.chat, User):
            return False

        user_id = event.chat_id
        if user_id in self.config["dnd_whitelist"]:
            return False

        sender = await event.get_sender()
        if sender.bot:
            await self._approve(user_id, "bot")
            return False

        if self.config.get("dnd_ignore_contacts") and sender.contact:
            await self._approve(user_id, "ignore_contacts")
            return False

        try:
            first_messages = await self.client.get_messages(
                event.chat, limit=1, reverse=True
            )
        except Exception as error:
            self.log.debug("Failed to inspect first PM from %s: %s", user_id, error)
        else:
            if first_messages and first_messages[0].sender_id == self._me.id:
                await self._approve(user_id, "started_by_you")
                return False

        if await self._active_peer(user_id, event.chat):
            return False

        now = int(time.time())
        self._temp["ratelimit_pmbl"] = [
            timestamp
            for timestamp in self._temp["ratelimit_pmbl"]
            if timestamp + 300 > now
        ]
        await self._send_pmbl_message(
            event,
            event.chat,
            bool(sender.contact),
            False,
            False,
        )
        await self._punish_handler(user_id)
        self.log.info("Blocked unapproved PM sender: %s", user_id)
        return True

    async def _handle_afk(self, event: Event) -> None:
        status_name = self.config.get("dnd_status")
        if not status_name:
            return

        chat_id = event.chat_id
        groups = self.config["dnd_afk_group_list"]
        allowed_chat = isinstance(event.chat, User)
        if not allowed_chat and self.config.get("dnd_afk_tag_whitelist"):
            allowed_chat = chat_id in groups
        elif not allowed_chat:
            allowed_chat = chat_id not in groups

        if not allowed_chat or chat_id in self._temp["ratelimit_afk"]:
            return

        sender = await event.get_sender()
        if (
            sender is None
            or getattr(sender, "is_self", False)
            or getattr(sender, "bot", False)
            or getattr(sender, "verified", False)
        ):
            return

        if not isinstance(event.chat, User) and not event.mentioned:
            return

        deadline = self.config.get("dnd_status_duration", 0)
        now = int(time.time())
        if deadline and now >= deadline:
            await self._cancel_unstatus_task()
            await self._unstatus_func()
            return

        gone = self.config.get("dnd_gone", now)
        elapsed = max(0, now - gone)
        further = self.config.get("dnd_further", "")
        texts = self.config["dnd_texts"]

        afk_text = f"{html.escape(texts.get(status_name, ''))}\n"
        if further:
            afk_text += (
                "\n<b><u>Пoдpoбнee:</u></b>\n"
                f"<code>{html.escape(further)}</code>"
            )
        if self.config.get("dnd_afk_gone_time"):
            afk_text += (
                "\n<b><u>Oтcyтcтвyю:</u></b>\n"
                f"<code>{self._time_formatter(elapsed, short=True)}</code>"
            )
        if deadline and self.config.get("dnd_afk_show_duration"):
            afk_text += (
                "\n<b><u>Бyдy AFK:</u></b>\n"
                f"<code>{self._time_formatter(deadline - now, short=True)}</code>"
            )

        response = await event.reply(afk_text, parse_mode="html")
        self._temp["sent_messages"].append(response)

        if not self.config["dnd_notif"].get(status_name, False):
            await self.client.send_read_acknowledge(chat_id, clear_mentions=True)

        self._temp["ratelimit_afk"].append(chat_id)

    @watcher(incoming=True)
    async def message_watcher(self, event: Event) -> None:
        try:
            chat_id = event.chat_id
            if chat_id in {1271266957, 777000, self._me.id}:
                return
            if await self._handle_pm_block(event):
                return
            await self._handle_afk(event)
        except Exception as error:
            await self.kernel.handle_error(
                error, source="dnd:message_watcher", event=event
            )
            self.log.error("Error in DND watcher: %s", error)
