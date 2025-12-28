# requires: telethon
# author: @hikariatama (ported to MCUB)
# version: 2.1.0
# description: Mutes tags and logs them to the bot logs with chat ignore list

import asyncio
from telethon import events

CUSTOM_EMOJI = {
    'silent': '<tg-emoji emoji-id="5278524998741412656">🤫</tg-emoji>',
    'melting': '<tg-emoji emoji-id="5222202120471591480">🫠</tg-emoji>',
    'ignore': '<tg-emoji emoji-id="5222202120471591480">🚫</tg-emoji>'
}

def register(kernel):
    client = kernel.client

    kernel.config.setdefault('stags_active', False)
    kernel.config.setdefault('stags_silent_mode', False)
    kernel.config.setdefault('stags_ignore_bots', True)
    kernel.config.setdefault('stags_ignored_chats', [])

    @kernel.register_command('stags')
    # <on/off/ignore [id]> - Toggle notifications or add chat to ignore list
    async def stags_cmd(event):
        try:
            args = event.text.split()
            if len(args) < 2:
                status = "active" if kernel.config.get('stags_active') else "inactive"
                await event.edit(f"{CUSTOM_EMOJI['silent']} <b>Silent Tags are {status}</b>", parse_mode='html')
                return

            action = args[1].lower()

            if action == "on":
                kernel.config['stags_active'] = True
                await event.edit(f"{CUSTOM_EMOJI['silent']} <b>Silent Tags: ON</b>", parse_mode='html')
                await asyncio.sleep(1)
                await event.delete()


            elif action == "off":
                kernel.config['stags_active'] = False
                await event.edit(f"{CUSTOM_EMOJI['melting']} <b>Silent Tags: OFF</b>", parse_mode='html')
                await asyncio.sleep(1)
                await event.delete()


            elif action == "ignore":
                ignored_chats = kernel.config.get('stags_ignored_chats', [])
                await asyncio.sleep(1)
                await event.delete()

                if len(args) > 2:
                    try:
                        chat_id = int(args[2])
                        if chat_id in ignored_chats:
                            ignored_chats.remove(chat_id)
                            res = f"Chat {chat_id} removed from ignore list"
                        else:
                            ignored_chats.append(chat_id)
                            res = f"Chat {chat_id} added to ignore list"

                        kernel.config['stags_ignored_chats'] = ignored_chats
                        await event.edit(f"<b>{res}</b>", parse_mode='html')
                    except ValueError:
                        await event.edit("<b>Invalid Chat ID</b>")
                else:
                    current_chat = event.chat_id
                    if current_chat in ignored_chats:
                        ignored_chats.remove(current_chat)
                        res = "this chat removed from ignore list"
                    else:
                        ignored_chats.append(current_chat)
                        res = "this chat added to ignore list"

                    kernel.config['stags_ignored_chats'] = ignored_chats
                    await event.edit(f"<b>{res}</b>", parse_mode='html')

            kernel.save_config()
        except Exception as e:
            await kernel.handle_error(e, source="stags_cmd", event=event)

    async def watcher(event):
        if not kernel.config.get('stags_active'):
            return

        if not event.mentioned:
            return

        if event.chat_id in kernel.config.get('stags_ignored_chats', []):
            return

        if kernel.config.get('stags_ignore_bots') and event.sender and getattr(event.sender, 'bot', False):
            return

        try:
            await client.send_read_acknowledge(event.chat_id, clear_mentions=True)

            chat = await event.get_chat()
            chat_title = getattr(chat, 'title', 'Private Chat')
            sender = await event.get_sender()
            sender_name = getattr(sender, 'first_name', 'Unknown')

            log_text = (
                f"{CUSTOM_EMOJI['silent']} <b>You were tagged!</b>\n"
                f"<b>Chat:</b> {chat_title} (<code>{event.chat_id}</code>)\n"
                f"<b>From:</b> <a href='tg://user?id={event.sender_id}'>{sender_name}</a>\n"
                f"<b>Message:</b> <code>{event.raw_text[:500]}</code>"
            )

            await kernel.send_log_message(log_text)

            if not kernel.config.get('stags_silent_mode'):
                msg = await event.reply(f"{CUSTOM_EMOJI['silent']} <b>Silent Tags are active</b>", parse_mode='html')
                await asyncio.sleep(3)
                await msg.delete()

        except Exception as e:
            await kernel.handle_error(e, source="stags_watcher")

    client.on(events.NewMessage(incoming=True))(watcher)
