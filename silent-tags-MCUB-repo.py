# meta: requires: telethon>=1.24.0
# meta: author: @hikarimods
# meta: version: 2.0.3
# meta: description: Mutes tags and logs them

import asyncio
import time
import html
from telethon.tl.functions.contacts import GetBlockedRequest
from telethon.tl.types import Channel, Message
from telethon import events

def register(kernel):
    client = kernel.client
    prefix = kernel.custom_prefix
    
    kernel.config.setdefault('stags_enabled', False)
    kernel.config.setdefault('silent', False)
    kernel.config.setdefault('ignore_bots', False)
    kernel.config.setdefault('ignore_blocked', False)
    kernel.config.setdefault('ignore_users', [])
    kernel.config.setdefault('ignore_chats', [])
    kernel.config.setdefault('silent_bots', False)
    kernel.config.setdefault('silent_blocked', False)
    kernel.config.setdefault('silent_users', [])
    kernel.config.setdefault('silent_chats', [])
    kernel.config.setdefault('use_whitelist', False)
    kernel.config.setdefault('log_chat_id', 'me')
    
    kernel.silent_tags_ratelimit = []
    kernel.silent_tags_fw_protect = {}
    kernel.silent_tags_blocked = []
    kernel.silent_tags_fw_protect_limit = 5
    
    CUSTOM_EMOJI = {
        'shushing': '<tg-emoji emoji-id="5370930189322688800">🤫</tg-emoji>',
    }
    
    strings = {
        "tagged": (
            '<b>{} You were tagged in <a href="{}">{}</a> by <a'
            ' href="tg://openmessage?user_id={}">{}</a></b>\n<code>Message:</code>\n<code>{}</code>\n<b>Link:'
            ' <a href="https://t.me/c/{}/{}">click</a></b>'
        ),
        "tag_mentioned": '<b>{} Silent Tags are active</b>',
        "stags_status": '<b>{} Silent Tags are {}</b>',
    }
    
    async def update_blocked_list():
        try:
            blocked = await client(GetBlockedRequest(offset=0, limit=1000))
            kernel.silent_tags_blocked = [user.id for user in blocked.users]
        except Exception as e:
            await kernel.handle_error(e, source="silent_tags:update_blocked_list")
    
    @kernel.register_command('stags')
    # <on\off> - Toggle notifications about tags
    async def stagscmd(event):
        try:
            args = event.text.split(maxsplit=1)[1] if len(event.text.split()) > 1 else ""
            
            if args not in ["on", "off"]:
                await event.edit(
                    strings["stags_status"].format(
                        CUSTOM_EMOJI["shushing"],
                        "active" if kernel.config.get('stags_enabled', False) else "inactive"
                    ),
                    parse_mode='html'
                )
                return
            
            args = args == "on"
            kernel.config['stags_enabled'] = args
            kernel.silent_tags_ratelimit = []
            kernel.save_config()
            
            await event.edit(
                strings["stags_status"].format(CUSTOM_EMOJI["shushing"], "now on" if args else "now off"),
                parse_mode='html'
            )
        except Exception as e:
            await kernel.handle_error(e, source="silent_tags:stagscmd", event=event)
            await event.edit("Error, check logs", parse_mode='html')
    
    async def message_watcher(event):
        try:
            if not hasattr(event.message, 'mentioned') or not event.message.mentioned:
                return
            
            if not kernel.config.get('stags_enabled', False):
                return
            
            if event.chat_id == kernel.config.get('log_chat_id', 'me'):
                return
            
            sender_id = event.sender_id
            
            if kernel.config.get('ignore_blocked', False):
                if not kernel.silent_tags_blocked:
                    await update_blocked_list()
                if sender_id in kernel.silent_tags_blocked:
                    return
            
            if kernel.config.get('ignore_bots', False) and event.sender.bot:
                return
            
            ignore_users = kernel.config.get('ignore_users', [])
            if kernel.config.get('use_whitelist', False):
                if sender_id not in ignore_users:
                    return
            else:
                if sender_id in ignore_users:
                    return
            
            ignore_chats = kernel.config.get('ignore_chats', [])
            if kernel.config.get('use_whitelist', False):
                if event.chat_id not in ignore_chats:
                    return
            else:
                if event.chat_id in ignore_chats:
                    return
            
            await client.send_read_acknowledge(
                event.chat_id,
                clear_mentions=True,
            )
            
            cid = event.chat_id
            
            if (
                cid in kernel.silent_tags_fw_protect
                and len(list(filter(lambda x: x > time.time(), kernel.silent_tags_fw_protect[cid])))
                > kernel.silent_tags_fw_protect_limit
            ):
                return
            
            if event.is_private:
                ctitle = "pm"
                grouplink = ""
            else:
                chat = await event.get_chat()
                grouplink = (
                    f"https://t.me/{chat.username}"
                    if getattr(chat, "username", None) is not None
                    else ""
                )
                ctitle = getattr(chat, "title", "Unknown Chat")
            
            if cid not in kernel.silent_tags_fw_protect:
                kernel.silent_tags_fw_protect[cid] = []
            
            uid = event.sender_id
            
            try:
                user = await event.get_sender()
                uname = user.first_name
            except Exception:
                uname = "Unknown user"
                user = None
            
            if kernel.config.get('silent_blocked', False):
                if not kernel.silent_tags_blocked:
                    await update_blocked_list()
                if sender_id in kernel.silent_tags_blocked:
                    return
            
            silent_users = kernel.config.get('silent_users', [])
            if kernel.config.get('use_whitelist', False):
                if sender_id not in silent_users:
                    return
            else:
                if sender_id in silent_users:
                    return
            
            silent_chats = kernel.config.get('silent_chats', [])
            if kernel.config.get('use_whitelist', False):
                if cid not in silent_chats:
                    return
            else:
                if cid in silent_chats:
                    return
            
            if not (isinstance(user, Channel)) and kernel.config.get('silent_bots', False) and event.sender.bot:
                return
            
            log_chat_id = kernel.config.get('log_chat_id', 'me')
            
            await client.send_message(
                log_chat_id,
                strings["tagged"].format(
                    CUSTOM_EMOJI["shushing"],
                    grouplink,
                    html.escape(ctitle),
                    uid,
                    html.escape(uname),
                    html.escape(event.raw_text),
                    str(cid).replace('-100', ''),
                    event.id,
                ),
                parse_mode='html',
            )
            
            kernel.silent_tags_fw_protect[cid] = kernel.silent_tags_fw_protect.get(cid, []) + [time.time() + 5 * 60]
            
            if cid not in kernel.silent_tags_ratelimit and not kernel.config.get('silent', False):
                kernel.silent_tags_ratelimit += [cid]
                msg = await event.reply(strings["tag_mentioned"].format(CUSTOM_EMOJI["shushing"]), parse_mode='html')
                await asyncio.sleep(3)
                await msg.delete()
                
        except Exception as e:
            await kernel.handle_error(e, source="silent_tags:message_watcher", event=event)
    
    client.on(events.NewMessage(incoming=True))(message_watcher)
    
    if kernel.config.get('ignore_blocked', False) or kernel.config.get('silent_blocked', False):
        async def init_blocked():
            await update_blocked_list()
        
        asyncio.create_task(init_blocked())