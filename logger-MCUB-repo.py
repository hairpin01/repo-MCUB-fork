# requires: aiosqlite, aiofiles
# author: @Mitritchq && @Hairpin00
# version: 2.0.0
# description: message logger module for tracking deleted and edited messages

import asyncio
import aiosqlite
import aiofiles
import io
from datetime import datetime
from telethon import events

def register(kernel):
    client = kernel.client
    prefix = kernel.custom_prefix
    DB_FILE = 'logger.db'

    async def init_db():

        try:
            async with aiosqlite.connect(DB_FILE) as db:
                await db.execute('''CREATE TABLE IF NOT EXISTS deleted
                                 (chat_id INTEGER, user_id INTEGER, username TEXT,
                                  first_name TEXT, last_name TEXT, message TEXT, timestamp INTEGER)''')
                await db.execute('''CREATE TABLE IF NOT EXISTS edited
                                 (chat_id INTEGER, user_id INTEGER, username TEXT,
                                  first_name TEXT, last_name TEXT, old_text TEXT, new_text TEXT, timestamp INTEGER)''')
                await db.execute('''CREATE TABLE IF NOT EXISTS logging
                                 (chat_id INTEGER PRIMARY KEY)''')
                await db.commit()
                kernel.cprint(f'{kernel.Colors.GREEN}✅ Logger database initialized{kernel.Colors.RESET}')
        except Exception as e:
            await kernel.handle_error(e, source="init_db", event=event)

    asyncio.create_task(init_db())
    message_cache = {}

    async def is_logging_enabled(chat_id):

        try:
            async with aiosqlite.connect(DB_FILE) as db:
                cursor = await db.execute('SELECT chat_id FROM logging WHERE chat_id = ?', (chat_id,))
                result = await cursor.fetchone()
                return result is not None
        except aiosqlite.OperationalError:
            return False

    @kernel.register_command('log')
    # usage: log on/off/clear/deleted/edited
    async def log_cmd(event):
        try:
            args = event.text.split(maxsplit=1)
            if len(args) < 2:
                await event.edit('⚪ <b>usage:</b> .log on/off/clear/deleted/edited', parse_mode='html')
                return

            subcmd = args[1].lower()

            if subcmd == 'on':
                await init_db()
                async with aiosqlite.connect(DB_FILE) as db:
                    await db.execute('INSERT OR IGNORE INTO logging VALUES (?)', (event.chat_id,))
                    await db.commit()
                await event.edit('✅ <b>logging enabled for this chat</b>', parse_mode='html')
                await event.delete()

            elif subcmd == 'off':
                async with aiosqlite.connect(DB_FILE) as db:
                    await db.execute('DELETE FROM logging WHERE chat_id = ?', (event.chat_id,))
                    await db.commit()
                await event.edit('🔕 <b>logging disabled for this chat</b>', parse_mode='html')
                await event.delete()

            elif subcmd == 'clear':
                async with aiosqlite.connect(DB_FILE) as db:
                    await db.execute('DELETE FROM deleted WHERE chat_id = ?', (event.chat_id,))
                    await db.execute('DELETE FROM edited WHERE chat_id = ?', (event.chat_id,))
                    await db.commit()
                await event.edit('🗑️ <b>chat logs cleared</b>', parse_mode='html')

            elif subcmd == 'deleted':
                await show_deleted(event)

            elif subcmd == 'edited':
                await show_edited(event)

            else:
                await event.edit('⚪ <b>usage:</b> .log on/off/clear/deleted/edited', parse_mode='html')

        except Exception as e:
            await kernel.handle_error(e, source="log_cmd", event=event)
            await event.edit("🌩️ <b>error, check logs</b>", parse_mode='html')

    async def show_deleted(event):
        try:
            await init_db()
            async with aiosqlite.connect(DB_FILE) as db:
                cursor = await db.execute('''SELECT * FROM deleted WHERE chat_id = ?
                                         ORDER BY timestamp DESC LIMIT 100''', (event.chat_id,))
                msgs = await cursor.fetchall()

            if not msgs:
                await event.edit('📋 <b>no deleted messages</b>', parse_mode='html')
                return


            file_content = f'🗑️ Deleted messages in chat {event.chat_id}\n{"="*50}\n\n'
            preview_text = '🗑️ <b>Deleted messages (last 10):</b>\n\n'

            for i, (chat_id, uid, uname, fname, lname, text, ts) in enumerate(msgs):
                dt = datetime.fromtimestamp(ts).strftime('%d.%m.%Y %H:%M:%S')
                name = fname or uname or f'User {uid}'
                if lname:
                    name = f"{fname or ''} {lname}".strip()

                entry = f'[{dt}] {name} (ID: {uid}, @{uname or "no username"}):\n{text}\n{"-"*30}\n'


                file_content += entry


                if i < 10:
                    short_text = text[:50] + '...' if len(text) > 50 else text
                    preview_text += f'<b>{dt}</b> - {name}:\n<code>{short_text}</code>\n\n'


            if len(msgs) > 10:
                await event.delete()
                file_io = io.BytesIO(file_content.encode('utf-8'))
                file_io.name = f'deleted_messages_{event.chat_id}_{int(datetime.now().timestamp())}.txt'

                await client.send_file(
                    event.chat_id,
                    file_io,
                    caption=f'📄 <b>Deleted messages for chat {event.chat_id} ({len(msgs)} total)</b>',
                    parse_mode='html'
                )
            else:
                await event.edit(preview_text, parse_mode='html')

        except Exception as e:
            await kernel.handle_error(e, source="show_deleted", event=event)
            await event.edit("🌩️ <b>error, check logs</b>", parse_mode='html')

    async def show_edited(event):
        try:
            await init_db()
            async with aiosqlite.connect(DB_FILE) as db:
                cursor = await db.execute('''SELECT * FROM edited WHERE chat_id = ?
                                         ORDER BY timestamp DESC LIMIT 100''', (event.chat_id,))
                msgs = await cursor.fetchall()

            if not msgs:
                await event.edit('📋 <b>no edited messages</b>', parse_mode='html')
                return

            file_content = f'✏️ Edited messages in chat {event.chat_id}\n{"="*50}\n\n'
            preview_text = '✏️ <b>Edited messages (last 5):</b>\n\n'

            for i, (chat_id, uid, uname, fname, lname, old, new, ts) in enumerate(msgs):
                dt = datetime.fromtimestamp(ts).strftime('%d.%m.%Y %H:%M:%S')
                name = fname or uname or f'User {uid}'
                if lname:
                    name = f"{fname or ''} {lname}".strip()

                entry = f'[{dt}] {name} (ID: {uid}, @{uname or "no username"}):\n'
                entry += f'Old: {old}\nNew: {new}\n{"-"*30}\n'


                file_content += entry


                if i < 5:
                    short_old = old[:30] + '...' if len(old) > 30 else old
                    short_new = new[:30] + '...' if len(new) > 30 else new
                    preview_text += f'<b>{dt}</b> - {name}:\n'
                    preview_text += f'Was: <code>{short_old}</code>\n'
                    preview_text += f'Now: <code>{short_new}</code>\n\n'


            if len(msgs) > 5:
                await event.delete()
                file_io = io.BytesIO(file_content.encode('utf-8'))
                file_io.name = f'edited_messages_{event.chat_id}_{int(datetime.now().timestamp())}.txt'

                await client.send_file(
                    event.chat_id,
                    file_io,
                    caption=f'📄 <b>Edited messages for chat {event.chat_id} ({len(msgs)} total)</b>',
                    parse_mode='html'
                )
            else:
                await event.edit(preview_text, parse_mode='html')

        except Exception as e:
            await kernel.handle_error(e, source="show_edited", event=event)
            await event.edit("🌩️ <b>error, check logs</b>", parse_mode='html')

    @client.on(events.NewMessage)
    async def cache_message(event):
        try:
            if not await is_logging_enabled(event.chat_id):
                return


            if not event.text:
                return

            sender = await event.get_sender()
            message_cache[event.id] = (
                sender.id if sender else 0,
                sender.username if sender else '',
                sender.first_name if sender else '',
                sender.last_name if sender else '',
                event.text
            )
        except Exception as e:
            await kernel.handle_error(e, source="cache_message", event=event)

    @client.on(events.MessageDeleted)
    async def log_deleted(event):
        try:
            if not await is_logging_enabled(event.chat_id):
                return

            for msg_id in event.deleted_ids:
                if msg_id in message_cache:
                    uid, uname, fname, lname, text = message_cache[msg_id]

                    async with aiosqlite.connect(DB_FILE) as db:
                        await db.execute('INSERT INTO deleted VALUES (?, ?, ?, ?, ?, ?, ?)',
                                      (event.chat_id, uid, uname, fname, lname,
                                       text, int(datetime.now().timestamp())))
                        await db.commit()


                    del message_cache[msg_id]
        except Exception as e:
            await kernel.handle_error(e, source="log_deleted", event=event)

    @client.on(events.MessageEdited)
    async def log_edited(event):

        try:
            if not await is_logging_enabled(event.chat_id):
                return

            old_data = message_cache.get(event.id)
            new_text = event.text or ''

            if old_data and old_data[4] != new_text:
                uid, uname, fname, lname, old_text = old_data


                async with aiosqlite.connect(DB_FILE) as db:
                    await db.execute('INSERT INTO edited VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                                  (event.chat_id, uid, uname, fname, lname,
                                   old_text, new_text, int(datetime.now().timestamp())))
                    await db.commit()


                message_cache[event.id] = (uid, uname, fname, lname, new_text)
        except Exception as e:
            await kernel.handle_error(e, source="log_edited", event=event)
