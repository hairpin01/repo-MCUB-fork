# author: @Hairpin00
# version: 1.0.1
# description: админ модуль

import time
import asyncio
from telethon import events, Button
from telethon.tl import functions, types
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

def register(kernel):
    client = kernel.client

    kernel.config.setdefault('admin_log_chat_id', None)
    kernel.config.setdefault('admin_max_warns', 3)
    kernel.config.setdefault('admin_mute_duration', 3600)
    kernel.config.setdefault('admin_use_bot', True)

    warns_storage = {}

    def get_warns_key(chat_id, user_id):
        return f"{chat_id}_{user_id}"

    def get_user_warns(chat_id, user_id):
        key = get_warns_key(chat_id, user_id)
        return warns_storage.get(key, 0)

    def add_user_warn(chat_id, user_id):
        key = get_warns_key(chat_id, user_id)
        current = warns_storage.get(key, 0)
        warns_storage[key] = current + 1
        return warns_storage[key]

    def remove_user_warn(chat_id, user_id):
        key = get_warns_key(chat_id, user_id)
        current = warns_storage.get(key, 0)
        if current > 0:
            warns_storage[key] = current - 1
        return warns_storage[key]

    def clear_user_warns(chat_id, user_id):
        key = get_warns_key(chat_id, user_id)
        warns_storage.pop(key, None)

    async def resolve_user(event, user_arg):
        if not user_arg:
            if event.reply_to_msg_id:
                reply = await event.get_reply_message()
                if reply:
                    return await reply.get_sender()
            return None

        try:
            if user_arg.isdigit():
                return await client.get_entity(int(user_arg))
            elif user_arg.startswith('@'):
                return await client.get_entity(user_arg[1:])
            else:
                return await client.get_entity(user_arg)
        except Exception:
            return None

    async def send_admin_log_bot(action, target_user, chat, reason, source_message=None):
        try:
            inline_bot_username = kernel.config.get('inline_bot_username')
            if not inline_bot_username:
                return None

            chat_title = getattr(chat, 'title', 'Private Chat')
            user_name = getattr(target_user, 'first_name', 'Unknown')
            if hasattr(target_user, 'last_name') and target_user.last_name:
                user_name = f"{user_name} {target_user.last_name}"

            username = getattr(target_user, 'username', None)
            user_link = f"@{username}" if username else f"ID: {target_user.id}"

            log_text = f"""🔨 Админ действие

Действие: {action}
Пользователь: {user_name} ({user_link})
Чат: {chat_title}
Причина: {reason or 'Не указана'}
Время: {time.strftime('%Y-%m-%d %H:%M:%S')}"""

            buttons = []

            if action == 'бан':
                buttons.append([Button.inline("🔓 Разбанить", f"unban_{chat.id}_{target_user.id}".encode())])
            elif action == 'кик':
                buttons.append([Button.inline("📥 Пригласить обратно", f"invite_{chat.id}_{target_user.id}".encode())])
            elif action == 'мут':
                buttons.append([Button.inline("🔊 Размутить", f"unmute_{chat.id}_{target_user.id}".encode())])
            elif action == 'варн':
                buttons.append([Button.inline("❌ Снять варн", f"unwarn_{chat.id}_{target_user.id}".encode())])

            if source_message:
                chat_id_for_link = str(chat.id).replace('-100', '')
                message_link = f"https://t.me/c/{chat_id_for_link}/{source_message.id}"
                buttons.append([Button.url("👁️ Посмотреть сообщение", message_link)])

            log_chat_id = kernel.config.get('admin_log_chat_id')
            if not log_chat_id:
                return None

            log_chat = await client.get_entity(log_chat_id)

            sent_msg = await client.send_message(
                log_chat,
                log_text,
                parse_mode='html',
                buttons=buttons if buttons else None
            )

            return sent_msg

        except Exception as e:
            await kernel.handle_error(e, source="send_admin_log_bot", event=None)
            return None

    async def send_admin_log_inline(action, target_user, chat, reason, source_message=None):
        try:
            inline_bot_username = kernel.config.get('inline_bot_username')
            if not inline_bot_username:
                return None

            chat_title = getattr(chat, 'title', 'Private Chat')
            user_name = getattr(target_user, 'first_name', 'Unknown')
            if hasattr(target_user, 'last_name') and target_user.last_name:
                user_name = f"{user_name} {target_user.last_name}"

            username = getattr(target_user, 'username', None)
            user_link = f"@{username}" if username else f"ID: {target_user.id}"

            log_text = f"""🔨 Админ действие

Действие: {action}
Пользователь: {user_name} ({user_link})
Чат: {chat_title}
Причина: {reason or 'Не указана'}
Время: {time.strftime('%Y-%m-%d %H:%M:%S')}"""

            buttons = []

            if action == 'бан':
                buttons.append([Button.inline("🔓 Разбанить", f"unban_{chat.id}_{target_user.id}".encode())])
            elif action == 'кик':
                buttons.append([Button.inline("📥 Пригласить обратно", f"invite_{chat.id}_{target_user.id}".encode())])
            elif action == 'мут':
                buttons.append([Button.inline("🔊 Размутить", f"unmute_{chat.id}_{target_user.id}".encode())])
            elif action == 'варн':
                buttons.append([Button.inline("❌ Снять варн", f"unwarn_{chat.id}_{target_user.id}".encode())])

            if source_message:
                chat_id_for_link = str(chat.id).replace('-100', '')
                message_link = f"https://t.me/c/{chat_id_for_link}/{source_message.id}"
                buttons.append([Button.url("👁️ Посмотреть сообщение", message_link)])

            log_chat_id = kernel.config.get('admin_log_chat_id')
            if not log_chat_id:
                return None

            try:
                await kernel.send_inline(log_chat_id, 'admin_log', text=log_text, buttons=buttons)
                return True
            except Exception as e:
                await kernel.handle_error(e, source="send_admin_log_inline", event=None)
                return None

        except Exception as e:
            await kernel.handle_error(e, source="send_admin_log_inline", event=None)
            return None

    async def send_admin_log(action, target_user, chat, reason, source_message=None):
        use_bot = kernel.config.get('admin_use_bot', True)

        if use_bot:
            return await send_admin_log_bot(action, target_user, chat, reason, source_message)
        else:
            return await send_admin_log_inline(action, target_user, chat, reason, source_message)

    @kernel.register_command('ban')
    async def ban_cmd(event):
        try:
            if not event.is_group and not event.is_channel:
                await event.edit("❌ Эта команда только для групп и каналов")
                return

            args = event.text.split()
            if len(args) < 2 and not event.reply_to_msg_id:
                await event.edit("❌ Использование: .ban [@username/id/ответ] [причина]")
                return

            user_arg = args[1] if len(args) > 1 else None
            reason = ' '.join(args[2:]) if len(args) > 2 else None

            target_user = await resolve_user(event, user_arg)
            if not target_user:
                await event.edit("❌ Пользователь не найден")
                return

            if target_user.id == (await client.get_me()).id:
                await event.edit("❌ Не могу забанить себя")
                return

            try:
                banned_rights = ChatBannedRights(
                    until_date=None,
                    view_messages=True,
                    send_messages=True,
                    send_media=True,
                    send_stickers=True,
                    send_gifs=True,
                    send_games=True,
                    send_inline=True,
                    send_polls=True,
                    change_info=True,
                    invite_users=True,
                    pin_messages=True
                )

                await client(EditBannedRequest(
                    channel=event.chat_id,
                    participant=target_user,
                    banned_rights=banned_rights
                ))

                await send_admin_log('бан', target_user, await event.get_chat(), reason, event.message)

                user_name = getattr(target_user, 'first_name', 'Пользователь')
                await event.edit(f"✅ Пользователь {user_name} забанен")

            except Exception as e:
                if "not admin" in str(e).lower():
                    await event.edit("❌ Нет прав администратора")
                else:
                    raise

        except Exception as e:
            await kernel.handle_error(e, source="ban_cmd", event=event)
            await event.edit("🌩️ <b>Ошибка, смотри логи</b>", parse_mode='html')

    @kernel.register_command('unban')
    async def unban_cmd(event):
        try:
            if not event.is_group and not event.is_channel:
                await event.edit("❌ Эта команда только для групп и каналов")
                return

            args = event.text.split()
            if len(args) < 2 and not event.reply_to_msg_id:
                await event.edit("❌ Использование: .unban [@username/id/ответ]")
                return

            user_arg = args[1] if len(args) > 1 else None
            target_user = await resolve_user(event, user_arg)
            if not target_user:
                await event.edit("❌ Пользователь не найден")
                return

            try:
                unbanned_rights = ChatBannedRights(
                    until_date=None,
                    view_messages=False,
                    send_messages=False,
                    send_media=False,
                    send_stickers=False,
                    send_gifs=False,
                    send_games=False,
                    send_inline=False,
                    send_polls=False,
                    change_info=False,
                    invite_users=False,
                    pin_messages=False
                )

                await client(EditBannedRequest(
                    channel=event.chat_id,
                    participant=target_user,
                    banned_rights=unbanned_rights
                ))

                user_name = getattr(target_user, 'first_name', 'Пользователь')
                await event.edit(f"✅ Пользователь {user_name} разбанен")

            except Exception as e:
                if "not admin" in str(e).lower():
                    await event.edit("❌ Нет прав администратора")
                else:
                    raise

        except Exception as e:
            await kernel.handle_error(e, source="unban_cmd", event=event)
            await event.edit("🌩️ <b>Ошибка, смотри логи</b>", parse_mode='html')

    @kernel.register_command('kick')
    async def kick_cmd(event):
        try:
            if not event.is_group and not event.is_channel:
                await event.edit("❌ Эта команда только для групп и каналов")
                return

            args = event.text.split()
            if len(args) < 2 and not event.reply_to_msg_id:
                await event.edit("❌ Использование: .kick [@username/id/ответ] [причина]")
                return

            user_arg = args[1] if len(args) > 1 else None
            reason = ' '.join(args[2:]) if len(args) > 2 else None

            target_user = await resolve_user(event, user_arg)
            if not target_user:
                await event.edit("❌ Пользователь не найден")
                return

            if target_user.id == (await client.get_me()).id:
                await event.edit("❌ Не могу кикнуть себя")
                return

            try:
                await client.kick_participant(event.chat_id, target_user)

                await send_admin_log('кик', target_user, await event.get_chat(), reason, event.message)

                user_name = getattr(target_user, 'first_name', 'Пользователь')
                await event.edit(f"✅ Пользователь {user_name} кикнут")

            except Exception as e:
                if "not admin" in str(e).lower():
                    await event.edit("❌ Нет прав администратора")
                else:
                    raise

        except Exception as e:
            await kernel.handle_error(e, source="kick_cmd", event=event)
            await event.edit("🌩️ <b>Ошибка, смотри логи</b>", parse_mode='html')

    @kernel.register_command('mute')
    async def mute_cmd(event):
        try:
            if not event.is_group and not event.is_channel:
                await event.edit("❌ Эта команда только для групп и каналов")
                return

            args = event.text.split()
            if len(args) < 2 and not event.reply_to_msg_id:
                await event.edit("❌ Использование: .mute [@username/id/ответ] [время в минутах] [причина]")
                return

            user_arg = args[1] if len(args) > 1 else None

            duration = kernel.config.get('admin_mute_duration', 3600)
            reason_start = 2

            if len(args) > 2 and args[2].isdigit():
                duration = int(args[2]) * 60
                reason_start = 3

            reason = ' '.join(args[reason_start:]) if len(args) > reason_start else None

            target_user = await resolve_user(event, user_arg)
            if not target_user:
                await event.edit("❌ Пользователь не найден")
                return

            if target_user.id == (await client.get_me()).id:
                await event.edit("❌ Не могу замутить себя")
                return

            try:
                until_date = int(time.time() + duration) if duration > 0 else None

                muted_rights = ChatBannedRights(
                    until_date=until_date,
                    send_messages=True,
                    send_media=True,
                    send_stickers=True,
                    send_gifs=True,
                    send_games=True,
                    send_inline=True,
                    send_polls=True
                )

                await client(EditBannedRequest(
                    channel=event.chat_id,
                    participant=target_user,
                    banned_rights=muted_rights
                ))

                await send_admin_log('мут', target_user, await event.get_chat(), reason, event.message)

                user_name = getattr(target_user, 'first_name', 'Пользователь')
                duration_text = f"{duration // 60} минут" if duration > 0 else "навсегда"
                await event.edit(f"✅ Пользователь {user_name} замучен на {duration_text}")

            except Exception as e:
                if "not admin" in str(e).lower():
                    await event.edit("❌ Нет прав администратора")
                else:
                    raise

        except Exception as e:
            await kernel.handle_error(e, source="mute_cmd", event=event)
            await event.edit("🌩️ <b>Ошибка, смотри логи</b>", parse_mode='html')

    @kernel.register_command('unmute')
    async def unmute_cmd(event):
        try:
            if not event.is_group and not event.is_channel:
                await event.edit("❌ Эта команда только для групп и каналов")
                return

            args = event.text.split()
            if len(args) < 2 and not event.reply_to_msg_id:
                await event.edit("❌ Использование: .unmute [@username/id/ответ]")
                return

            user_arg = args[1] if len(args) > 1 else None
            target_user = await resolve_user(event, user_arg)
            if not target_user:
                await event.edit("❌ Пользователь не найден")
                return

            try:
                unmuted_rights = ChatBannedRights(
                    until_date=None,
                    send_messages=False,
                    send_media=False,
                    send_stickers=False,
                    send_gifs=False,
                    send_games=False,
                    send_inline=False,
                    send_polls=False
                )

                await client(EditBannedRequest(
                    channel=event.chat_id,
                    participant=target_user,
                    banned_rights=unmuted_rights
                ))

                user_name = getattr(target_user, 'first_name', 'Пользователь')
                await event.edit(f"✅ Пользователь {user_name} размучен")

            except Exception as e:
                if "not admin" in str(e).lower():
                    await event.edit("❌ Нет прав администратора")
                else:
                    raise

        except Exception as e:
            await kernel.handle_error(e, source="unmute_cmd", event=event)
            await event.edit("🌩️ <b>Ошибка, смотри логи</b>", parse_mode='html')

    @kernel.register_command('warn')
    async def warn_cmd(event):
        try:
            if not event.is_group and not event.is_channel:
                await event.edit("❌ Эта команда только для групп и каналов")
                return

            args = event.text.split()
            if len(args) < 2 and not event.reply_to_msg_id:
                await event.edit("❌ Использование: .warn [@username/id/ответ] [причина]")
                return

            user_arg = args[1] if len(args) > 1 else None
            reason = ' '.join(args[2:]) if len(args) > 2 else None

            target_user = await resolve_user(event, user_arg)
            if not target_user:
                await event.edit("❌ Пользователь не найден")
                return

            if target_user.id == (await client.get_me()).id:
                await event.edit("❌ Не могу выдать варн себе")
                return

            chat = await event.get_chat()
            warns_count = add_user_warn(chat.id, target_user.id)

            await send_admin_log('варн', target_user, chat, reason, event.message)

            user_name = getattr(target_user, 'first_name', 'Пользователь')
            max_warns = kernel.config.get('admin_max_warns', 3)

            if warns_count >= max_warns:
                try:
                    banned_rights = ChatBannedRights(
                        until_date=None,
                        view_messages=True,
                        send_messages=True
                    )

                    await client(EditBannedRequest(
                        channel=event.chat_id,
                        participant=target_user,
                        banned_rights=banned_rights
                    ))

                    clear_user_warns(chat.id, target_user.id)
                    await event.edit(f"⚠️ Пользователь {user_name} получил {warns_count}/{max_warns} варнов и был забанен")
                except Exception:
                    await event.edit(f"⚠️ Пользователь {user_name} получил {warns_count}/{max_warns} варнов (не удалось забанить)")
            else:
                await event.edit(f"⚠️ Пользователь {user_name} получил варн ({warns_count}/{max_warns})")

        except Exception as e:
            await kernel.handle_error(e, source="warn_cmd", event=event)
            await event.edit("🌩️ <b>Ошибка, смотри логи</b>", parse_mode='html')

    @kernel.register_command('unwarn')
    async def unwarn_cmd(event):
        try:
            if not event.is_group and not event.is_channel:
                await event.edit("❌ Эта команда только для групп и каналов")
                return

            args = event.text.split()
            if len(args) < 2 and not event.reply_to_msg_id:
                await event.edit("❌ Использование: .unwarn [@username/id/ответ]")
                return

            user_arg = args[1] if len(args) > 1 else None
            target_user = await resolve_user(event, user_arg)
            if not target_user:
                await event.edit("❌ Пользователь не найден")
                return

            chat = await event.get_chat()
            warns_count = remove_user_warn(chat.id, target_user.id)

            user_name = getattr(target_user, 'first_name', 'Пользователь')
            await event.edit(f"✅ Снят варн с пользователя {user_name} (осталось: {warns_count})")

        except Exception as e:
            await kernel.handle_error(e, source="unwarn_cmd", event=event)
            await event.edit("🌩️ <b>Ошибка, смотри логи</b>", parse_mode='html')

    @kernel.register_command('warns')
    async def warns_cmd(event):
        try:
            if not event.is_group and not event.is_channel:
                await event.edit("❌ Эта команда только для групп и каналов")
                return

            args = event.text.split()
            if len(args) < 2 and not event.reply_to_msg_id:
                await event.edit("❌ Использование: .warns [@username/id/ответ]")
                return

            user_arg = args[1] if len(args) > 1 else None
            target_user = await resolve_user(event, user_arg)
            if not target_user:
                await event.edit("❌ Пользователь не найден")
                return

            chat = await event.get_chat()
            warns_count = get_user_warns(chat.id, target_user.id)

            user_name = getattr(target_user, 'first_name', 'Пользователь')
            max_warns = kernel.config.get('admin_max_warns', 3)
            await event.edit(f"⚠️ Пользователь {user_name} имеет {warns_count}/{max_warns} варнов")

        except Exception as e:
            await kernel.handle_error(e, source="warns_cmd", event=event)
            await event.edit("🌩️ <b>Ошибка, смотри логи</b>", parse_mode='html')

    @kernel.register_command('purge')
    async def purge_cmd(event):
        try:
            if not event.is_group and not event.is_channel:
                await event.edit("❌ Эта команда только для групп и каналов")
                return

            if not event.reply_to_msg_id:
                await event.edit("❌ Ответьте на сообщение для очистки")
                return

            try:
                await event.delete()

                reply = await event.get_reply_message()
                deleted = await client.delete_messages(
                    event.chat_id,
                    list(range(reply.id, event.id))
                )

                msg = await event.respond(f"✅ Удалено {len(deleted)} сообщений")
                await asyncio.sleep(3)
                await msg.delete()

            except Exception as e:
                if "not admin" in str(e).lower():
                    await event.edit("❌ Нет прав администратора")
                else:
                    raise

        except Exception as e:
            await kernel.handle_error(e, source="purge_cmd", event=event)
            await event.edit("🌩️ <b>Ошибка, смотри логи</b>", parse_mode='html')

    async def inline_admin_handler(event):
        try:
            builder = event.builder.article(
                title="Админ действие",
                text="Логирование админ действий",
                buttons=[
                    [Button.inline("🔓 Разбанить", b"test_unban"),
                     Button.inline("📥 Пригласить", b"test_invite")],
                    [Button.inline("🔊 Размутить", b"test_unmute"),
                     Button.inline("❌ Снять варн", b"test_unwarn")],
                    [Button.url("👁️ Посмотреть", "https://t.me")]
                ]
            )
            await event.answer([builder])
        except Exception as e:
            await kernel.handle_error(e, source="inline_admin_handler", event=event)

    kernel.register_inline_handler('admin_log', inline_admin_handler)

    async def admin_callback_handler(event):
        try:
            data = event.data.decode()

            if data.startswith('unban_'):
                _, chat_id, user_id = data.split('_')
                chat_id = int(chat_id)
                user_id = int(user_id)

                try:
                    unbanned_rights = ChatBannedRights(
                        until_date=None,
                        view_messages=False
                    )

                    user_entity = await client.get_entity(user_id)
                    await client(EditBannedRequest(
                        channel=chat_id,
                        participant=user_entity,
                        banned_rights=unbanned_rights
                    ))

                    await event.answer("✅ Пользователь разбанен", alert=True)
                    await event.edit(buttons=None)

                except Exception as e:
                    await event.answer("❌ Ошибка при разбане", alert=True)

            elif data.startswith('invite_'):
                _, chat_id, user_id = data.split('_')
                chat_id = int(chat_id)
                user_id = int(user_id)

                try:
                    user_entity = await client.get_entity(user_id)
                    await client.add_chat_users(chat_id, [user_entity])

                    await event.answer("✅ Пользователь приглашен", alert=True)
                    await event.edit(buttons=None)

                except Exception as e:
                    await event.answer("❌ Ошибка при приглашении", alert=True)

            elif data.startswith('unmute_'):
                _, chat_id, user_id = data.split('_')
                chat_id = int(chat_id)
                user_id = int(user_id)

                try:
                    unmuted_rights = ChatBannedRights(
                        until_date=None,
                        send_messages=False
                    )

                    user_entity = await client.get_entity(user_id)
                    await client(EditBannedRequest(
                        channel=chat_id,
                        participant=user_entity,
                        banned_rights=unmuted_rights
                    ))

                    await event.answer("✅ Пользователь размучен", alert=True)
                    await event.edit(buttons=None)

                except Exception as e:
                    await event.answer("❌ Ошибка при размуте", alert=True)

            elif data.startswith('unwarn_'):
                _, chat_id, user_id = data.split('_')
                chat_id = int(chat_id)
                user_id = int(user_id)

                remove_user_warn(chat_id, user_id)
                await event.answer("✅ Варн снят", alert=True)
                await event.edit(buttons=None)

        except Exception as e:
            await kernel.handle_error(e, source="admin_callback_handler", event=event)
            await event.answer("❌ Произошла ошибка", alert=True)

    kernel.register_callback_handler('unban_', admin_callback_handler)
    kernel.register_callback_handler('invite_', admin_callback_handler)
    kernel.register_callback_handler('unmute_', admin_callback_handler)
    kernel.register_callback_handler('unwarn_', admin_callback_handler)
