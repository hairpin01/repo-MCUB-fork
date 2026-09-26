# name: kickme-MCUB-repo
# requires:
# author:
# version: 1.0.3
# description: Kick users who send /kickme command with proper async structure

import re
from telethon import events


def register(kernel):
    client = kernel.client

    kernel.config.setdefault("kickme_chat_id", None)

    async def kickme_handler(event):
        chat_id = kernel.config.get("kickme_chat_id")

        if chat_id is None:
            try:
                await kernel.send_log_message(
                    "❌ kickme_chat_id not configured in config"
                )
            except:
                pass
            return

        try:
            chat_id = int(chat_id)
        except (ValueError, TypeError):
            try:
                await kernel.send_log_message(
                    f"❌ Invalid kickme_chat_id format: {chat_id}"
                )
            except:
                pass
            return

        try:
            await kernel.send_log_message(
                f"🔍 Received message in chat {event.chat_id}, configured chat: {chat_id}"
            )
        except:
            pass

        if event.chat_id != chat_id:
            return

        try:
            chat = await event.get_chat()
            is_group = (
                chat.megagroup
                or chat.gigagroup
                or (hasattr(chat, "group") and chat.group)
            )

            if not is_group:
                try:
                    await kernel.send_log_message(
                        f"❌ Chat {chat_id} is not a group (type: {type(chat).__name__})"
                    )
                except:
                    pass
                return

            try:
                await kernel.send_log_message(
                    f"✅ Chat {chat_id} is a group, checking admin permissions..."
                )
            except:
                pass

            me = await event.client.get_me()
            my_permissions = await event.client.get_permissions(chat_id, me)

            if not my_permissions.is_admin:
                try:
                    await kernel.send_log_message(
                        f"❌ Bot is not admin in chat {chat_id}, cannot kick"
                    )
                except:
                    pass
                return

            if not my_permissions.ban_users:
                try:
                    await kernel.send_log_message(
                        f"❌ Bot doesn't have ban/kick permissions in chat {chat_id}"
                    )
                except:
                    pass
                return

            try:
                await kernel.send_log_message(
                    f"✅ Bot has admin and kick permissions in chat {chat_id}"
                )
            except:
                pass

            user = await event.get_sender()
            username = f"@{user.username}" if user.username else f"id{user.id}"

            try:
                await kernel.send_log_message(
                    f"🔄 Attempting to kick {username} (ID: {user.id}) from chat {event.chat_id}"
                )
            except:
                pass

            result = await event.client.kick_participant(event.chat_id, user)

            try:
                await kernel.send_log_message(
                    f"✅ Successfully kicked {username} (ID: {user.id}) from chat {event.chat_id}"
                )
            except:
                pass

        except Exception as e:
            error_msg = f"❌ Failed to kick user: {str(e)}"
            try:
                await kernel.send_log_message(error_msg)
            except:
                pass
            await kernel.handle_error(e, source="kickme_handler", event=event)

    kernel.register.watcher(incoming=True, regex=r"^/kickme$")(kickme_handler)

    @kernel.register.command("kickme_status")
    # show kickme module status
    async def status_cmd(event):
        try:
            chat_id = kernel.config.get("kickme_chat_id")
            if chat_id:
                await event.edit(f"✅ Module active for chat ID: {chat_id}")
            else:
                await event.edit("❌ Module not configured (kickme_chat_id not set)")
        except Exception as e:
            await kernel.handle_error(e, source="status_cmd", event=event)
            await event.edit("🌩️ <b>Error, check logs</b>", parse_mode="html")

    @kernel.register.command("set_kickme_chat")
    # set kickme chat id
    async def set_chat_cmd(event):
        try:
            args = event.text.split()
            if len(args) < 2:
                await event.edit("Usage: .set_kickme_chat <chat_id>")
                return

            new_chat_id = args[1]
            try:
                new_chat_id = int(new_chat_id)
            except ValueError:
                await event.edit("Chat ID must be a number")
                return

            kernel.config["kickme_chat_id"] = new_chat_id
            kernel.save_config()

            await event.edit(f"✅ KickMe chat ID set to: {new_chat_id}")
            try:
                await kernel.send_log_message(
                    f"✅ KickMe chat ID updated to: {new_chat_id}"
                )
            except:
                pass
        except Exception as e:
            await kernel.handle_error(e, source="set_chat_cmd", event=event)
            await event.edit("🌩️ <b>Error, check logs</b>", parse_mode="html")
