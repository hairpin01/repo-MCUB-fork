import asyncio
import contextlib
import datetime
import logging
import re
import time
from typing import Union
from telethon import events
from telethon.tl.types import User, Channel, PeerUser
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest, DeleteHistoryRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.users import GetFullUserRequest

logger = logging.getLogger(__name__)

CUSTOM_EMOJI = {
    'question': '<tg-emoji emoji-id="5334768819548200731">❔</tg-emoji>',
    'check': '<tg-emoji emoji-id="5330115548900501467">✅</tg-emoji>',
    'no': '<tg-emoji emoji-id="5854929766146118183">❌</tg-emoji>',
    'cloud': '<tg-emoji emoji-id="5188705588925702510">😶‍🌫️</tg-emoji>',
    'warning': '<tg-emoji emoji-id="5472308992514464048">🚫</tg-emoji>',
    'info': '<tg-emoji emoji-id="5431376038628171216">ℹ️</tg-emoji>',
    'fox': '<tg-emoji emoji-id="5271604874419647061">🦊</tg-emoji>',
    'police': '<tg-emoji emoji-id="5472308992514464048">👮</tg-emoji>',
    'fist': '<tg-emoji emoji-id="5334768819548200731">✊</tg-emoji>',
    'lock': '<tg-emoji emoji-id="5330115548900501467">🔏</tg-emoji>',
}

def register(kernel):
    client = kernel.client
    prefix = kernel.custom_prefix
    
    kernel.config.setdefault('dnd_pmbl_active', True)
    kernel.config.setdefault('dnd_active_threshold', 5)
    kernel.config.setdefault('dnd_afk_gone_time', True)
    kernel.config.setdefault('dnd_afk_group_list', [])
    kernel.config.setdefault('dnd_afk_show_duration', True)
    kernel.config.setdefault('dnd_afk_tag_whitelist', True)
    kernel.config.setdefault('dnd_custom_message', '')
    kernel.config.setdefault('dnd_delete_dialog', False)
    kernel.config.setdefault('dnd_ignore_active', True)
    kernel.config.setdefault('dnd_ignore_contacts', True)
    kernel.config.setdefault('dnd_photo', 'https://github.com/hikariatama/assets/raw/master/unit_sigma.png')
    kernel.config.setdefault('dnd_report_spam', False)
    kernel.config.setdefault('dnd_use_bio', True)
    kernel.config.setdefault('dnd_whitelist', [])
    kernel.config.setdefault('dnd_ignore_hello', False)
    kernel.config.setdefault('dnd_status', False)
    kernel.config.setdefault('dnd_status_duration', 0)
    kernel.config.setdefault('dnd_gone', 0)
    kernel.config.setdefault('dnd_further', '')
    kernel.config.setdefault('dnd_old_bio', '')
    kernel.config.setdefault('dnd_texts', {})
    kernel.config.setdefault('dnd_notif', {})
    
    _ratelimit_afk = []
    _ratelimit_pmbl = []
    _ratelimit_pmbl_threshold = 10
    _ratelimit_pmbl_timeout = 5 * 60
    _sent_messages = []
    
    def get_display_name(user):
        if hasattr(user, 'first_name') and hasattr(user, 'last_name'):
            return f"{user.first_name or ''} {user.last_name or ''}".strip()
        elif hasattr(user, 'title'):
            return user.title
        elif hasattr(user, 'username'):
            return f"@{user.username}"
        else:
            return "Unknown"
    
    def format_state(state):
        if state is None:
            return f"{CUSTOM_EMOJI['question']}"
        return f"{CUSTOM_EMOJI['check']}" if state else f"{CUSTOM_EMOJI['no']}"
    
    def get_tag(user, html=False):
        if hasattr(user, 'id'):
            if html:
                return f'<a href="tg://user?id={user.id}">{get_display_name(user)}</a>'
            return f"{get_display_name(user)} (id{user.id})"
        return "Unknown"
    
    def raw_text(message, strip_command=False):
        if not hasattr(message, 'text'):
            return ''
        text = message.text
        if strip_command and text.startswith(prefix):
            text = ' '.join(text.split(' ')[1:])
        return text
    
    def time_formatter(seconds, short=False):
        periods = [
            ('y', 31536000),
            ('mo', 2592000),
            ('w', 604800),
            ('d', 86400),
            ('h', 3600),
            ('m', 60),
            ('s', 1)
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
        
        return ''.join(result) if result else '0s'
    
    def convert_time(time_str):
        units = {
            's': 1,
            'm': 60,
            'h': 3600,
            'd': 86400,
            'w': 604800,
            'mo': 2592000,
            'y': 31536000
        }
        
        match = re.match(r'(\d+)([a-zA-Z]+)', time_str)
        if match:
            value = int(match.group(1))
            unit = match.group(2).lower()
            if unit in units:
                return value * units[unit]
        return 0
    
    def _approve(user_id, reason="unknown"):
        whitelist = kernel.config.get('dnd_whitelist', [])
        if user_id not in whitelist:
            whitelist.append(user_id)
            kernel.config['dnd_whitelist'] = whitelist
            logger.info(f"User {user_id} approved in pm, reason: {reason}")
    
    def _unapprove(user_id):
        whitelist = kernel.config.get('dnd_whitelist', [])
        if user_id in whitelist:
            whitelist.remove(user_id)
            kernel.config['dnd_whitelist'] = whitelist
            logger.info(f"User {user_id} unapproved in pm")
    
    async def _send_pmbl_message(message, peer, contact, started_by_you, active_peer, self_id):
        global _ratelimit_pmbl
        
        if len(_ratelimit_pmbl) < _ratelimit_pmbl_threshold:
            caption = kernel.config.get('dnd_custom_message') or (
                "😊 <b>Hey there •ᴗ•</b>\n<b>i am Unit «SIGMA»<b>, the "
                "<b>guardian</b> of this account. You are <b>not approved</b>! You "
                "can contact my owner <b>in a groupchat</b>, if you need "
                "help.\n<b>I need to ban you in terms of security.</b>"
            )
            
            try:
                await client.send_file(
                    peer,
                    kernel.config.get('dnd_photo'),
                    caption=caption,
                    parse_mode='html'
                )
            except Exception:
                await message.edit(caption, parse_mode='html')
            
            _ratelimit_pmbl.append(int(time.time()))
            
            try:
                peer_entity = await client.get_entity(peer)
            except Exception:
                await asyncio.sleep(1)
                peer_entity = await client.get_entity(peer)
            
            banned_log = (
                f"{CUSTOM_EMOJI['police']} <b>I banned {get_tag(peer_entity, True)}.</b>\n\n"
                f"<b>{format_state(contact)} Contact</b>\n"
                f"<b>{format_state(started_by_you)} Started by you</b>\n"
                f"<b>{format_state(active_peer)} Active conversation</b>\n\n"
                f"<b>{CUSTOM_EMOJI['fist']} Actions</b>\n\n"
                f"<b>{format_state(kernel.config.get('dnd_report_spam'))} Reported spam</b>\n"
                f"<b>{format_state(kernel.config.get('dnd_delete_dialog'))} Deleted dialog</b>\n"
                f"<b>{format_state(True)} Blocked</b>\n\n"
                f"<b>{CUSTOM_EMOJI['info']} Message</b>\n"
                f"<code>{raw_text(message)[:3000]}</code>"
            )
            
            me = await client.get_me()
            await client.send_message(me.id, banned_log, parse_mode='html')
    
    async def _active_peer(cid, peer):
        if kernel.config.get('dnd_ignore_active'):
            q = 0
            async for msg in client.iter_messages(peer, limit=200):
                me = await client.get_me()
                if msg.sender_id == me.id:
                    q += 1
                if q >= kernel.config.get('dnd_active_threshold'):
                    _approve(cid, "active_threshold")
                    return True
        return False
    
    async def _punish_handler(cid):
        from telethon.tl.functions.contacts import BlockRequest
        from telethon.tl.functions.messages import ReportSpamRequest, DeleteHistoryRequest
        
        await client(BlockRequest(id=cid))
        if kernel.config.get('dnd_report_spam'):
            await client(ReportSpamRequest(peer=cid))
        if kernel.config.get('dnd_delete_dialog'):
            await client(DeleteHistoryRequest(peer=cid, just_clear=True, max_id=0))
    
    async def _unstatus_func(delay=None):
        if delay:
            await asyncio.sleep(delay)
        
        kernel.config['dnd_status'] = False
        kernel.config['dnd_status_duration'] = 0
        kernel.config['dnd_gone'] = 0
        kernel.config['dnd_further'] = ''
        
        if kernel.config.get('dnd_old_bio'):
            from telethon.tl.functions.account import UpdateProfileRequest
            await client(UpdateProfileRequest(about=kernel.config['dnd_old_bio']))
            kernel.config['dnd_old_bio'] = ''
        
        global _sent_messages
        for m in _sent_messages:
            try:
                await m.delete()
            except Exception as e:
                logger.debug(f"Message not deleted due to {e}")
        
        _sent_messages = []
        _ratelimit_afk.clear()
    
    @kernel.register_command('cdnd')
    # Открыть конфигурацию модуля
    async def cdnd_cmd(event):

        await event.edit(f"{CUSTOM_EMOJI['lock']} <b>Используйте:</b> <code>{prefix}cfg</code> <b>для настройки модуля</b>", parse_mode='html')
    
    @kernel.register_command('pmbanlast')
    # <число> - Заблокировать последние N диалогов
    async def pmbanlast_cmd(event):
        from telethon.tl.functions.contacts import BlockRequest
        from telethon.tl.functions.messages import DeleteHistoryRequest
        
        args = event.text.split()
        if len(args) < 2 or not args[1].isdigit():
            await event.edit(f"{CUSTOM_EMOJI['info']} <b>Пример использования: </b><code>{prefix}pmbanlast 5</code>", parse_mode='html')
            return
        
        n = int(args[1])
        await event.edit(f"{CUSTOM_EMOJI['cloud']} <b>Удаляю {n} последних диалогов...</b>", parse_mode='html')
        
        dialogs = []
        async for dialog in client.iter_dialogs(ignore_pinned=True):
            from telethon.tl.types import PeerUser
            if isinstance(dialog.entity, PeerUser):
                m = await client.get_messages(dialog.entity, limit=1, reverse=True)
                if m:
                    dialogs.append((dialog.entity, int(time.mktime(m[0].date.timetuple()))))
        
        dialogs.sort(key=lambda x: x[1])
        to_ban = [d for d, _ in dialogs[-n:]]
        
        for d in to_ban:
            await client(BlockRequest(id=d))
            await client(DeleteHistoryRequest(peer=d, just_clear=True, max_id=0))
        
        await event.edit(f"{CUSTOM_EMOJI['cloud']} <b>Удалил {n} последних диалогов!</b>", parse_mode='html')
    
    @kernel.register_command('allowpm')
    # <ответ или username> - Разрешить пользователю писать в ЛС
    async def allowpm_cmd(event):

        user = None
        args = event.text.split()
        
        if event.is_reply:
            reply = await event.get_reply_message()
            user = await reply.get_sender()
        elif len(args) > 1:
            try:
                user = await client.get_entity(args[1])
            except Exception:
                await event.edit(f"{CUSTOM_EMOJI['warning']} <b>Не удалось найти пользователя</b>", parse_mode='html')
                return
        
        if not user:
            chat = await event.get_chat()
            from telethon.tl.types import User
            if isinstance(chat, User):
                user = chat
            else:
                await event.edit(f"{CUSTOM_EMOJI['warning']} <b>Вы не указали пользователя</b>", parse_mode='html')
                return
        
        _approve(user.id, "manual_approve")
        await event.edit(f'{CUSTOM_EMOJI["cloud"]} <b><a href="tg://user?id={user.id}">{get_display_name(user)}</a> допущен к ЛС.</b>', parse_mode='html')
    
    @kernel.register_command('denypm')
    # <ответ или username> - Запретить пользователю писать в ЛС
    async def denypm_cmd(event):

        user = None
        args = event.text.split()
        
        if event.is_reply:
            reply = await event.get_reply_message()
            user = await reply.get_sender()
        elif len(args) > 1:
            try:
                user = await client.get_entity(args[1])
            except Exception:
                await event.edit(f"{CUSTOM_EMOJI['warning']} <b>Не удалось найти пользователя</b>", parse_mode='html')
                return
        
        if not user:
            chat = await event.get_chat()
            from telethon.tl.types import User
            if isinstance(chat, User):
                user = chat
            else:
                await event.edit(f"{CUSTOM_EMOJI['warning']} <b>Вы не указали пользователя</b>", parse_mode='html')
                return
        
        _unapprove(user.id)
        await event.edit(f'{CUSTOM_EMOJI["cloud"]} <b><a href="tg://user?id={user.id}">{get_display_name(user)}</a> не допущен к ЛС.</b>', parse_mode='html')
    
    @kernel.register_command('block')
    # <ответ> - Заблокировать пользователя
    async def block_cmd(event):

        if not event.is_reply:
            await event.edit(f"{CUSTOM_EMOJI['info']} <b>Ответьте на сообщение, чтобы заблокировать пользователя</b>", parse_mode='html')
            return
        
        from telethon.tl.functions.contacts import BlockRequest
        reply = await event.get_reply_message()
        user = await reply.get_sender()
        
        await client(BlockRequest(id=user.id))
        await event.edit(f'{CUSTOM_EMOJI["cloud"]} <b><a href="tg://user?id={user.id}">{get_display_name(user)}</a> заблокирован.</b>', parse_mode='html')
    
    @kernel.register_command('unblock')
    # <ответ> - Разблокировать пользователя
    async def unblock_cmd(event):

        if not event.is_reply:
            await event.edit(f"{CUSTOM_EMOJI['info']} <b>Ответьте на сообщение, чтобы разблокировать пользователя</b>", parse_mode='html')
            return
        
        from telethon.tl.functions.contacts import UnblockRequest
        reply = await event.get_reply_message()
        user = await reply.get_sender()
        
        await client(UnblockRequest(id=user.id))
        await event.edit(f'{CUSTOM_EMOJI["cloud"]} <b><a href="tg://user?id={user.id}">{get_display_name(user)}</a> разблокирован.</b>', parse_mode='html')
    
    @kernel.register_command('report')
    # <ответ> - Пожаловаться на спам (только в ЛС)
    async def report_cmd(event):

        from telethon.tl.types import User
        from telethon.tl.functions.messages import ReportSpamRequest
        
        chat = await event.get_chat()
        if not isinstance(chat, User):
            await event.edit(f"{CUSTOM_EMOJI['warning']} <b>Эта команда работает только в ЛС</b>", parse_mode='html')
            return
        
        await client(ReportSpamRequest(peer=chat.id))
        await event.edit("⚠️ <b>Отправил жалобу на спам!</b>", parse_mode='html')
    
    @kernel.register_command('newstatus')
    # <название> <уведомления 0/1> <текст> - Создать новый статус
    async def newstatus_cmd(event):

        args = raw_text(event, strip_command=True).split(' ', 2)
        if len(args) < 3:
            await event.edit(f"{CUSTOM_EMOJI['warning']} <b>Аргументы некорректны</b>", parse_mode='html')
            return
        
        name, notify, text = args
        notify_bool = notify in ["1", "true", "yes", "+"]
        
        texts = kernel.config.get('dnd_texts', {})
        texts[name] = text
        kernel.config['dnd_texts'] = texts
        
        notifs = kernel.config.get('dnd_notif', {})
        notifs[name] = notify_bool
        kernel.config['dnd_notif'] = notifs
        
        await event.edit(
            f"<b>{CUSTOM_EMOJI['check']} Статус {name} создан.</b>\n"
            f"<code>{text}</code>\n"
            f"Уведомления: {notify_bool}",
            parse_mode='html'
        )
    
    @kernel.register_command('delstatus')
    # <название> - Удалить статус
    async def delstatus_cmd(event):

        args = event.text.split()
        if len(args) < 2:
            await event.edit(f"{CUSTOM_EMOJI['warning']} <b>Укажите название статуса</b>", parse_mode='html')
            return
        
        name = args[1]
        texts = kernel.config.get('dnd_texts', {})
        notifs = kernel.config.get('dnd_notif', {})
        
        if name not in texts:
            await event.edit(f"{CUSTOM_EMOJI['warning']} <b>Статус не найден</b>", parse_mode='html')
            return
        
        del texts[name]
        if name in notifs:
            del notifs[name]
        
        kernel.config['dnd_texts'] = texts
        kernel.config['dnd_notif'] = notifs
        
        await event.edit(f"<b>{CUSTOM_EMOJI['check']} Статус {name} удалён</b>", parse_mode='html')
    
    @kernel.register_command('statuses')
    # Показать доступные статусы
    async def statuses_cmd(event):

        texts = kernel.config.get('dnd_texts', {})
        notifs = kernel.config.get('dnd_notif', {})
        
        if not texts:
            await event.edit(f"{CUSTOM_EMOJI['fox']} <b>Нет доступных статусов</b>", parse_mode='html')
            return
        
        res = f"{CUSTOM_EMOJI['fox']} <b>Доступные статусы:</b>\n\n"
        for name, text in texts.items():
            notify = notifs.get(name, False)
            res += f"<b><u>{name}</u></b> | Уведомления: <b>{notify}</b>\n{text}\n➖➖➖➖➖➖➖➖➖\n"
        
        await event.edit(res, parse_mode='html')
    
    @kernel.register_command('status')
    # <название> [длительность] [доп.инфо] - Установить статус
    async def status_cmd(event):

        from telethon.tl.functions.account import UpdateProfileRequest
        from telethon.tl.functions.users import GetFullUserRequest
        
        args = raw_text(event, strip_command=True).split(' ', 2)
        if len(args) < 1:
            await event.edit(f"{CUSTOM_EMOJI['warning']} <b>Укажите название статуса</b>", parse_mode='html')
            return
        
        name = args[0]
        texts = kernel.config.get('dnd_texts', {})
        
        if name not in texts:
            await event.edit(f"{CUSTOM_EMOJI['warning']} <b>Статус не найден</b>", parse_mode='html')
            return
        
        duration = 0
        further = ""
        
        if len(args) > 1:
            # Parse duration
            duration_str = args[1]
            duration = convert_time(duration_str) if re.match(r'\d+[a-zA-Z]', duration_str) else 0
            
            if len(args) > 2 and not duration:
                further = args[1] + ' ' + args[2] if len(args) > 2 else args[1]
            elif len(args) > 2 and duration:
                further = args[2]
        
        if kernel.config.get('dnd_status'):
            await _unstatus_func()
        
        if kernel.config.get('dnd_use_bio') and not kernel.config.get('dnd_old_bio'):
            me = await client.get_me()
            full = await client(GetFullUserRequest(me))
            kernel.config['dnd_old_bio'] = getattr(full.full_user, 'about', '')
        
        kernel.config['dnd_status'] = name
        kernel.config['dnd_gone'] = time.time()
        kernel.config['dnd_further'] = further
        
        if duration:
            if '_unstatus_task' in globals():
                try:
                    globals()['_unstatus_task'].cancel()
                except:
                    pass
            globals()['_unstatus_task'] = asyncio.create_task(_unstatus_func(duration))
            kernel.config['dnd_status_duration'] = time.time() + duration
        
        status_text = (
            f"<b>{CUSTOM_EMOJI['check']} Статус установлен</b>\n"
            f"<code>{texts[name]}</code>\n"
            f"Уведомления: <code>{kernel.config.get('dnd_notif', {}).get(name, False)}</code>"
        )
        
        if further:
            status_text += f"\nДополнительно: <code>{further}</code>"
        if duration:
            status_text += f"\nПродолжительность: <code>{time_formatter(duration, short=True)}</code>"
        
        if kernel.config.get('dnd_use_bio'):
            bio = texts[name]
            if further:
                bio += f" | {further}"
            bio = bio[:70]  # Limit bio length
            await client(UpdateProfileRequest(about=bio))
        
        msg = await event.edit(status_text, parse_mode='html')
        _sent_messages.append(msg)
    
    @kernel.register_command('unstatus')
    # Снять статус
    async def unstatus_cmd(event):

        if not kernel.config.get('dnd_status'):
            await event.edit(f"{CUSTOM_EMOJI['warning']} <b>Нет активного статуса</b>", parse_mode='html')
            return
        
        if '_unstatus_task' in globals():
            try:
                globals()['_unstatus_task'].cancel()
            except:
                pass
        
        await _unstatus_func()
        msg = await event.edit(f"<b>{CUSTOM_EMOJI['check']} Статус удалён</b>", parse_mode='html')
        await asyncio.sleep(10)
        await msg.delete()
    
    async def message_watcher(event):
        
        try:
            chat_id = event.chat_id
            me = await client.get_me()
            
            if chat_id in {1271266957, 777000, me.id}:
                return
            
            # PMBL handling
            if (kernel.config.get('dnd_pmbl_active') and 
                isinstance(event.chat, User) and
                not isinstance(event.chat, Channel)):
                
                cid = event.chat_id
                whitelist = kernel.config.get('dnd_whitelist', [])
                
                if cid in whitelist:
                    return
                
                sender = await event.get_sender()
                if sender.bot:
                    _approve(cid, "bot")
                    return
                
                if kernel.config.get('dnd_ignore_contacts') and sender.contact:
                    _approve(cid, "ignore_contacts")
                    return
                
                # Check first message
                try:
                    first_msg = await client.get_messages(event.chat, limit=1, reverse=True)
                    if first_msg and first_msg[0].sender_id == me.id:
                        _approve(cid, "started_by_you")
                        return
                except:
                    pass
                
                active_peer = await _active_peer(cid, event.chat)
                if active_peer:
                    return
                
                global _ratelimit_pmbl
                _ratelimit_pmbl = [
                    t for t in _ratelimit_pmbl 
                    if t + _ratelimit_pmbl_timeout > time.time()
                ]
                
                contact = not (kernel.config.get('dnd_ignore_contacts') and sender.contact)
                started_by_you = False
                
                await _send_pmbl_message(
                    event, event.chat, contact, started_by_you, active_peer, me.id
                )
                await _punish_handler(cid)
                _approve(cid, "blocked")
                logger.warning(f"Intruder punished: {cid}")
            
            # AFK handling
            elif (kernel.config.get('dnd_status') and 
                  (isinstance(event.chat, User) or 
                   (kernel.config.get('dnd_afk_tag_whitelist') and 
                    chat_id in kernel.config.get('dnd_afk_group_list', [])) or
                   (not kernel.config.get('dnd_afk_tag_whitelist') and 
                    chat_id not in kernel.config.get('dnd_afk_group_list', [])))):
                
                if chat_id in _ratelimit_afk:
                    return
                
                sender = await event.get_sender()
                if (sender.is_self or sender.bot or sender.verified):
                    return
                
                if isinstance(event.chat, User):
                    mentioned = True
                else:
                    mentioned = event.mentioned
                
                if not mentioned:
                    return
                
                now = datetime.datetime.now().replace(microsecond=0)
                gone = datetime.datetime.fromtimestamp(kernel.config.get('dnd_gone', 0)).replace(microsecond=0)
                
                if kernel.config.get('dnd_status_duration'):
                    status_duration = datetime.datetime.fromtimestamp(
                        kernel.config.get('dnd_status_duration')
                    ).replace(microsecond=0)
                    if now > status_duration:
                        await _unstatus_func()
                        return
                
                diff = now - gone
                diff_sec = diff.total_seconds()
                
                further = kernel.config.get('dnd_further', '')
                status_name = kernel.config.get('dnd_status')
                texts = kernel.config.get('dnd_texts', {})
                
                afk_string = f"{texts.get(status_name, '')}\n"
                if further:
                    afk_string += f"\n<b><u>Подробнее:</u></b>\n<code>{further}</code>"
                
                if kernel.config.get('dnd_afk_gone_time'):
                    afk_string += f"\n<b><u>Отсутствую:</u></b>\n<code>{time_formatter(diff_sec, short=True)}</code>"
                
                if kernel.config.get('dnd_status_duration') and kernel.config.get('dnd_afk_show_duration'):
                    remaining = kernel.config.get('dnd_status_duration') - time.time()
                    if remaining > 0:
                        afk_string += f"\n<b><u>Буду AFK:</u></b>\n<code>{time_formatter(remaining, short=True)}</code>"
                
                m = await event.reply(afk_string, parse_mode='html')
                _sent_messages.append(m)
                
                if not kernel.config.get('dnd_notif', {}).get(status_name, False):
                    await client.send_read_acknowledge(
                        event.chat_id,
                        clear_mentions=True
                    )
                
                _ratelimit_afk.append(chat_id)
                
        except Exception as e:
            logger.error(f"Error in DND watcher: {e}")
    
    client.on(events.NewMessage())(message_watcher)
    
    async def startup_check():
        if not kernel.config.get('dnd_ignore_hello'):
            me = await client.get_me()
            hello_msg = (
                f"{CUSTOM_EMOJI['lock']} <b>Unit «SIGMA»</b> защищает ваши личные сообщения "
                f"от нежелательного контакта. Это будет блокировать всех, кто попытается "
                f"связаться с Вами.\n\nИспользуйте <code>{prefix}pmbanlast</code> если уже "
                f"были попытки нежелательного вторжения."
            )
            try:
                await client.send_file(
                    me.id,
                    'https://github.com/hikariatama/assets/raw/master/unit_sigma.png',
                    caption=hello_msg,
                    parse_mode='html'
                )
            except:
                await client.send_message(me.id, hello_msg, parse_mode='html')
            
            kernel.config['dnd_ignore_hello'] = True
    
    asyncio.create_task(startup_check())
