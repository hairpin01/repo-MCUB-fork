# author: @kmodules && @Hairpin00
# version: 1.0.4
# description: универсальный AFK модуль 

import time
import datetime
import asyncio
from collections import defaultdict
from telethon import events, functions, types

def register(kernel):
    client = kernel.client

    kernel.config.setdefault('afk_always_answer', False)
    kernel.config.setdefault('afk_set_premium_status', True)
    kernel.config.setdefault('afk_time_zone', 'UTC')
    kernel.config.setdefault('afk_custom_message', '{default}')
    kernel.config.setdefault('afk_custom_emoji_status', 4969889971700761796)

    PREMIUM_EMOJI = {
        'afk_on': '<tg-emoji emoji-id="5994473545650934240">😀</tg-emoji>',
        'afk_off': '<tg-emoji emoji-id="5343636681473935403">💎</tg-emoji>',
        'error': '<tg-emoji emoji-id="5330273431898318607">🌩</tg-emoji>',
        'wave': '<tg-emoji emoji-id="5258362429389152256">✋</tg-emoji>',
        'clock': '<tg-emoji emoji-id="5469913852462242978">⏰</tg-emoji>',
        'microphone': '<tg-emoji emoji-id="5256054356913957552">🎙</tg-emoji>',
        'stats': '<tg-emoji emoji-id="5895444149699612825">📊</tg-emoji>',
        'success': '<tg-emoji emoji-id="5404754074685966817">✅</tg-emoji>',
        'failure': '<tg-emoji emoji-id="5893081007153746175">❌</tg-emoji>',
        'plane': '<tg-emoji emoji-id="5372849966689566579">✈️</tg-emoji>',
        'snowflake': '<tg-emoji emoji-id="5368513458469878442">❄️</tg-emoji>',
        'timer': '<tg-emoji emoji-id="5373236586760651455">⏱️</tg-emoji>'
    }

    answered_users = set()
    chat_messages = defaultdict(list)

    ignore_limit = None
    ignore_time = None
    pm_limit = None
    chat_limit = None
    time_interval = None

    old_emoji_status = None

    def format_time_delta(delta):
        days = delta.days
        hours = delta.seconds // 3600
        minutes = (delta.seconds % 3600) // 60
        seconds = delta.seconds % 60

        parts = []
        if days > 0:
            parts.append(f"{days}д")
        if hours > 0:
            parts.append(f"{hours}ч")
        if minutes > 0:
            parts.append(f"{minutes}м")
        if seconds > 0 or not parts:
            parts.append(f"{seconds}с")

        return " ".join(parts)

    def format_custom_message(was_online, reason=None, come_time=None):
        reason_text = f"{PREMIUM_EMOJI['clock']} <b>Ушел по причине:</b> <i>{reason}</i>\n" if reason and reason != "Нету" else ""
        come_time_text = f"{PREMIUM_EMOJI['microphone']} <b>Прийду в:</b> <b>{come_time}</b>" if come_time else ""

        default_message = f"""{PREMIUM_EMOJI['wave']} <b>Сейчас я в AFK режиме</b>
{PREMIUM_EMOJI['afk_off']} <b>Был в сети:</b> {was_online} назад
{reason_text}{come_time_text}""".strip()

        custom_message = kernel.config.get('afk_custom_message', '{default}')
        if custom_message == "{default}":
            return default_message

        return custom_message.format(
            was_online=was_online,
            reason=reason if reason else "Нету",
            come_time=come_time if come_time else "",
            default=default_message
        )

    def check_limits(chat_id, is_pm=False):
        current_time = time.time()

        if ignore_limit and ignore_time:
            chat_messages[chat_id] = [
                msg_time for msg_time in chat_messages[chat_id]
                if current_time - msg_time < ignore_time
            ]
            if len(chat_messages[chat_id]) >= ignore_limit:
                return False

        if time_interval:
            limit = pm_limit if is_pm else chat_limit
            recent_msgs = [
                msg_time for msg_time in chat_messages[chat_id]
                if current_time - msg_time < time_interval
            ]
            if len(recent_msgs) >= limit:
                return False
            chat_messages[chat_id] = recent_msgs

        chat_messages[chat_id].append(current_time)
        return True

    async def set_emoji_status(document_id=None):
        try:
            if document_id:
                await client(functions.account.UpdateEmojiStatusRequest(
                    emoji_status=types.EmojiStatus(document_id=document_id)
                ))
            else:
                await client(functions.account.UpdateEmojiStatusRequest(
                    emoji_status=types.EmojiStatusEmpty()
                ))
        except Exception as e:
            await kernel.handle_error(e, source="set_emoji_status", event=None)

    @kernel.register_command('afk')
    async def afk_cmd(event):
        try:
            args = event.text.split(maxsplit=2)
            reason = None
            return_time = None

            if len(args) > 1:
                parts = args[1].split(' ', 1)
                if len(parts) == 2:
                    reason, return_time = parts
                else:
                    reason = parts[0]

            if reason == "Нету":
                reason = None

            if kernel.config.get('afk_set_premium_status', True):
                try:
                    me = await client.get_me()
                    if hasattr(me, 'emoji_status') and me.emoji_status:
                        nonlocal old_emoji_status
                        old_emoji_status = me.emoji_status

                    custom_emoji = kernel.config.get('afk_custom_emoji_status')
                    await set_emoji_status(custom_emoji)
                except Exception as e:
                    await kernel.handle_error(e, source="afk_cmd:set_status", event=event)

            kernel.config['afk_status'] = reason or True
            kernel.config['afk_gone_time'] = time.time()
            if return_time:
                kernel.config['afk_return_time'] = return_time
            else:
                kernel.config.pop('afk_return_time', None)

            kernel.save_config()

            answered_users.clear()
            chat_messages.clear()

            preview = format_custom_message("Только что", reason, return_time)
            await event.edit(f"{PREMIUM_EMOJI['afk_on']} <b>AFK режим включен!</b>\n{PREMIUM_EMOJI['plane']} <b>Буду отвечать этим сообщением:</b>\n\n{preview}", parse_mode='html')

        except Exception as e:
            await kernel.handle_error(e, source="afk_cmd", event=event)
            await event.edit(f"{PREMIUM_EMOJI['error']} <b>Ошибка, смотри логи</b>", parse_mode='html')

    @kernel.register_command('unafk')
    async def unafk_cmd(event):
        try:
            kernel.config['afk_status'] = False
            kernel.config.pop('afk_gone_time', None)
            kernel.config.pop('afk_return_time', None)

            kernel.save_config()

            answered_users.clear()
            chat_messages.clear()

            if kernel.config.get('afk_set_premium_status', True):
                try:
                    await set_emoji_status(None)
                except Exception as e:
                    await kernel.handle_error(e, source="unafk_cmd:reset_status", event=event)

            await event.edit(f"{PREMIUM_EMOJI['afk_off']} <b>Больше не в режиме AFK.</b>", parse_mode='html')

        except Exception as e:
            await kernel.handle_error(e, source="unafk_cmd", event=event)
            await event.edit(f"{PREMIUM_EMOJI['error']} <b>Ошибка, смотри логи</b>", parse_mode='html')

    @kernel.register_command('afkstatus')
    async def afkstatus_cmd(event):
        try:
            afk_status = kernel.config.get('afk_status')
            if not afk_status:
                await event.edit(f"{PREMIUM_EMOJI['afk_off']} <b>AFK режим выключен.</b>", parse_mode='html')
                return

            gone_time = kernel.config.get('afk_gone_time')
            reason = afk_status if isinstance(afk_status, str) else None
            return_time = kernel.config.get('afk_return_time')

            now = datetime.datetime.now().replace(microsecond=0)
            gone = datetime.datetime.fromtimestamp(gone_time).replace(microsecond=0)
            diff = now - gone

            was_online = format_time_delta(diff)
            status_message = format_custom_message(was_online, reason, return_time)

            await event.edit(f"{PREMIUM_EMOJI['stats']} <b>Текущий статус AFK:</b>\n\n{status_message}", parse_mode='html')

        except Exception as e:
            await kernel.handle_error(e, source="afkstatus_cmd", event=event)
            await event.edit(f"{PREMIUM_EMOJI['error']} <b>Ошибка, смотри логи</b>", parse_mode='html')

    @kernel.register_command('ignorusers')
    async def ignorusers_cmd(event):
        try:
            args = event.text.split()
            if len(args) != 3:
                await event.edit(f"{PREMIUM_EMOJI['failure']} Использование: .ignorusers <количество> <минуты>", parse_mode='html')
                return

            try:
                msg_limit = int(args[1])
                time_limit = int(args[2])
            except ValueError:
                await event.edit(f"{PREMIUM_EMOJI['failure']} Аргументы должны быть числами", parse_mode='html')
                return

            nonlocal ignore_limit, ignore_time
            ignore_limit = msg_limit
            ignore_time = time_limit * 60

            await event.edit(f"{PREMIUM_EMOJI['success']} Установлено ограничение: {msg_limit} сообщений за {time_limit} минут в одном чате", parse_mode='html')

        except Exception as e:
            await kernel.handle_error(e, source="ignorusers_cmd", event=event)
            await event.edit(f"{PREMIUM_EMOJI['error']} <b>Ошибка, смотри логи</b>", parse_mode='html')

    @kernel.register_command('timeafk')
    async def timeafk_cmd(event):
        try:
            args = event.text.split()
            if len(args) != 3:
                await event.edit(f"{PREMIUM_EMOJI['failure']} Использование: .timeafk <минуты> <макс.сообщений>", parse_mode='html')
                return

            try:
                interval = int(args[1])
                max_msgs = int(args[2])
            except ValueError:
                await event.edit(f"{PREMIUM_EMOJI['failure']} Аргументы должны быть числами", parse_mode='html')
                return

            nonlocal time_interval, pm_limit, chat_limit
            time_interval = interval * 60
            pm_limit = 2
            chat_limit = max_msgs

            await event.edit(f"{PREMIUM_EMOJI['success']} Установлено ограничение: {max_msgs} сообщений за {interval} минут (ЛС: {pm_limit} сообщений)", parse_mode='html')

        except Exception as e:
            await kernel.handle_error(e, source="timeafk_cmd", event=event)
            await event.edit(f"{PREMIUM_EMOJI['error']} <b>Ошибка, смотри логи</b>", parse_mode='html')

    async def afk_watcher(event):
        try:
            afk_status = kernel.config.get('afk_status')
            if not afk_status or afk_status is False:
                return

            user = await event.get_sender()
            if not user:
                return

            if getattr(user, 'bot', False) or getattr(user, 'verified', False):
                return

            me = await client.get_me()
            is_mentioned = f"@{me.username}" in event.text if me.username else False
            is_pm = event.is_private

            if not (is_mentioned or is_pm):
                return

            always_answer = kernel.config.get('afk_always_answer', False)
            if not always_answer and user.id in answered_users:
                return

            chat_id = user.id if is_pm else event.chat_id

            if not check_limits(chat_id, is_pm):
                return

            if not always_answer:
                answered_users.add(user.id)

            gone_time = kernel.config.get('afk_gone_time')
            if not gone_time:
                return

            now = datetime.datetime.now().replace(microsecond=0)
            gone = datetime.datetime.fromtimestamp(gone_time).replace(microsecond=0)
            diff = now - gone

            reason = afk_status if isinstance(afk_status, str) else None
            return_time = kernel.config.get('afk_return_time')

            was_online = format_time_delta(diff)
            response = format_custom_message(was_online, reason, return_time)

            await event.reply(response, parse_mode='html')

        except Exception as e:
            await kernel.handle_error(e, source="afk_watcher", event=event)

    client.on(events.NewMessage(incoming=True))(afk_watcher)
