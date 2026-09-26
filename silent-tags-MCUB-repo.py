# name: silent-tags-MCUB-repo
# meta: requires: telethon>=1.24.0
# meta: author: @hikarimods
# meta: version: 2.1.0
# meta: description: Mutes tags and logs them

import asyncio
import json
import time
import html
from telethon.tl.functions.contacts import GetBlockedRequest
from telethon.tl.types import Channel, Message
from core.lib.loader.module_config import (
    ModuleConfig,
    ConfigValue,
    Boolean,
    String,
    Secret,
)


def register(kernel):
    client = kernel.client
    prefix = kernel.custom_prefix

    config = ModuleConfig(
        ConfigValue(
            "stags_enabled",
            False,
            description="Enable silent tags",
            validator=Boolean(default=False),
        ),
        ConfigValue(
            "silent",
            False,
            description="Don't reply in chat on tag",
            validator=Boolean(default=False),
        ),
        ConfigValue(
            "ignore_bots",
            False,
            description="Ignore bots",
            validator=Boolean(default=False),
        ),
        ConfigValue(
            "ignore_blocked",
            False,
            description="Ignore blocked users",
            validator=Boolean(default=False),
        ),
        ConfigValue(
            "silent_bots",
            False,
            description="Don't log bot tags",
            validator=Boolean(default=False),
        ),
        ConfigValue(
            "silent_blocked",
            False,
            description="Don't log blocked user tags",
            validator=Boolean(default=False),
        ),
        ConfigValue(
            "use_whitelist",
            False,
            description="Treat user/chat lists as whitelist",
            validator=Boolean(default=False),
        ),
        ConfigValue(
            "ignore_users",
            "[]",
            description="JSON list of ignored user IDs",
            validator=String(default="[]"),
        ),
        ConfigValue(
            "ignore_chats",
            "[]",
            description="JSON list of ignored chat IDs",
            validator=String(default="[]"),
        ),
        ConfigValue(
            "silent_users",
            "[]",
            description="JSON list of silent user IDs",
            validator=String(default="[]"),
        ),
        ConfigValue(
            "silent_chats",
            "[]",
            description="JSON list of silent chat IDs",
            validator=String(default="[]"),
        ),
        ConfigValue(
            "log_chat_id",
            "me",
            description="Chat ID to log tags to",
            validator=String(default="me"),
        ),
    )

    def get_config():
        """Always read live config to avoid stale cached values."""
        live = getattr(kernel, "_live_module_configs", {}).get(__name__)
        return live if live else config

    def _json_list(key: str) -> list:
        """Parse a JSON-list config value safely."""
        try:
            return json.loads(get_config().get(key, "[]") or "[]")
        except (json.JSONDecodeError, TypeError):
            return []

    async def _load_config():
        config_dict = await kernel.get_module_config(
            __name__,
            {
                "stags_enabled": False,
                "silent": False,
                "ignore_bots": False,
                "ignore_blocked": False,
                "silent_bots": False,
                "silent_blocked": False,
                "use_whitelist": False,
                "ignore_users": "[]",
                "ignore_chats": "[]",
                "silent_users": "[]",
                "silent_chats": "[]",
                "log_chat_id": "me",
            },
        )
        config.from_dict(config_dict)
        await kernel.save_module_config(__name__, config.to_dict())
        kernel.store_module_config_schema(__name__, config)

    asyncio.create_task(_load_config())

    kernel.silent_tags_ratelimit = []
    kernel.silent_tags_fw_protect = {}
    kernel.silent_tags_blocked = []
    kernel.silent_tags_fw_protect_limit = 5

    CUSTOM_EMOJI = {
        "shushing": '<tg-emoji emoji-id="5370930189322688800">🤫</tg-emoji>',
    }

    strings = {
        "tagged": (
            '<b>{} You were tagged in <a href="{}">{}</a> by <a'
            ' href="tg://openmessage?user_id={}">{}</a></b>\n<code>Message:</code>\n<code>{}</code>\n<b>Link:'
            ' <a href="https://t.me/c/{}/{}">click</a></b>'
        ),
        "tag_mentioned": "<b>{} Silent Tags are active</b>",
        "stags_status": "<b>{} Silent Tags are {}</b>",
    }

    async def update_blocked_list():
        try:
            blocked = await client(GetBlockedRequest(offset=0, limit=1000))
            kernel.silent_tags_blocked = [user.id for user in blocked.users]
        except Exception as e:
            await kernel.handle_error(e, source="silent_tags:update_blocked_list")

    @kernel.register.command("stags")
    # <on|off> - Toggle notifications about tags
    async def stagscmd(event):
        try:
            args = (
                event.text.split(maxsplit=1)[1] if len(event.text.split()) > 1 else ""
            )

            cfg = get_config()

            if args not in ["on", "off"]:
                await event.edit(
                    strings["stags_status"].format(
                        CUSTOM_EMOJI["shushing"],
                        "active" if cfg["stags_enabled"] else "inactive",
                    ),
                    parse_mode="html",
                )
                return

            new_value = args == "on"
            cfg["stags_enabled"] = new_value
            kernel.silent_tags_ratelimit = []
            await kernel.save_module_config(__name__, cfg.to_dict())

            await event.edit(
                strings["stags_status"].format(
                    CUSTOM_EMOJI["shushing"], "now on" if new_value else "now off"
                ),
                parse_mode="html",
            )
        except Exception as e:
            await kernel.handle_error(e, source="silent_tags:stagscmd", event=event)
            await event.edit("Error, check logs", parse_mode="html")

    @kernel.register.watcher("newmessage", incoming=True)
    async def message_watcher(event):
        try:
            if not hasattr(event.message, "mentioned") or not event.message.mentioned:
                return

            cfg = get_config()

            if not cfg["stags_enabled"]:
                return

            raw_log_chat_id = cfg["log_chat_id"]
            try:
                log_chat_id = int(raw_log_chat_id)
            except (ValueError, TypeError):
                log_chat_id = raw_log_chat_id

            sender_id = event.sender_id

            if cfg["ignore_blocked"]:
                if not kernel.silent_tags_blocked:
                    await update_blocked_list()
                if sender_id in kernel.silent_tags_blocked:
                    return

            if cfg["ignore_bots"] and event.sender.bot:
                return

            ignore_users = _json_list("ignore_users")
            use_whitelist = cfg["use_whitelist"]
            if use_whitelist:
                if sender_id not in ignore_users:
                    return
            else:
                if sender_id in ignore_users:
                    return

            ignore_chats = _json_list("ignore_chats")
            if use_whitelist:
                if event.chat_id not in ignore_chats:
                    return
            else:
                if event.chat_id in ignore_chats:
                    return

            await client.send_read_acknowledge(event.chat_id, clear_mentions=True)

            cid = event.chat_id

            if (
                cid in kernel.silent_tags_fw_protect
                and len(
                    list(
                        filter(
                            lambda x: x > time.time(),
                            kernel.silent_tags_fw_protect[cid],
                        )
                    )
                )
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

            # re-read cfg because we're deeper in the handler now
            cfg = get_config()

            if cfg["silent_blocked"]:
                if not kernel.silent_tags_blocked:
                    await update_blocked_list()
                if sender_id in kernel.silent_tags_blocked:
                    return

            silent_users = _json_list("silent_users")
            if use_whitelist:
                if sender_id not in silent_users:
                    return
            else:
                if sender_id in silent_users:
                    return

            silent_chats = _json_list("silent_chats")
            if use_whitelist:
                if cid not in silent_chats:
                    return
            else:
                if cid in silent_chats:
                    return

            if (
                not isinstance(user, Channel)
                and cfg["silent_bots"]
                and event.sender.bot
            ):
                return

            await client.send_message(
                log_chat_id,
                strings["tagged"].format(
                    CUSTOM_EMOJI["shushing"],
                    grouplink,
                    html.escape(ctitle),
                    uid,
                    html.escape(uname),
                    html.escape(event.raw_text),
                    str(cid).replace("-100", ""),
                    event.id,
                ),
                parse_mode="html",
            )

            kernel.silent_tags_fw_protect[cid] = kernel.silent_tags_fw_protect.get(
                cid, []
            ) + [time.time() + 5 * 60]

            if cid not in kernel.silent_tags_ratelimit and not cfg["silent"]:
                kernel.silent_tags_ratelimit += [cid]
                msg = await event.reply(
                    strings["tag_mentioned"].format(CUSTOM_EMOJI["shushing"]),
                    parse_mode="html",
                )
                await asyncio.sleep(3)
                await msg.delete()

        except Exception as e:
            await kernel.handle_error(
                e, source="silent_tags:message_watcher", event=event
            )

    async def _maybe_init_blocked():
        cfg = get_config()
        if cfg["ignore_blocked"] or cfg["silent_blocked"]:
            await update_blocked_list()

    asyncio.create_task(_maybe_init_blocked())
