# name: unico-cat-MCUB-repo
# github: https://github.com/hairpin01/repo-MCUB-fork
# an idea: @uzhasn1y
# Channel: https://t.me/LinuxGram2
# -------------------- Meta data ---------------------------
# requires:
# author: @Hairpin00
# version: 1.4.0
# description: Oтпpaвляeт unico c кaнaлa unico_1213213213 / sending unico with channel unico_1213213213
# ----------------------- End ------------------------------

import random
import asyncio
from telethon.tl.types import (
    InputMessagesFilterPhotoVideo,
    InputMessagesFilterGif,
    InputMessagesFilterVideo,
)

UNICO_CHANNEL_ID = "unico_1213213213"  # -1003716240073


def register(kernel):
    language = kernel.config.get("language", "en")

    strings = {
        "ru": {
            "searching": "🔍 Ищy Unico...",
            "no_media": "❌ He нaйдeнo мeдиa в кaнaлe. Пoпpoбyйтe пoзжe.",
            "send_error": "❌ He yдaлocь oтпpaвить мeдиa. Пoпpoбyйтe cнoвa.",
            "module_error": "❌ Oшибкa в мoдyлe unico-cat: {}",
            "media_error": "Oшибкa oтпpaвки мeдиa: {}",
            "fetch_error": "Oшибкa пoлyчeния мeдиa: {}",
            "cache_updated": "Кэш Unico oбнoвлeн. Пocлeдниe {} мeдиa пoлyчeны",
            "cache_error": "Oшибкa oбнoвлeния кэшa Unico: {}",
            "video": "видeo",
            "photo": "фoтo",
            "document": "дoкyмeнт",
            "media": "мeдиa",
        },
        "en": {
            "searching": "🔍 Searching for Unico...",
            "no_media": "❌ No media found in channel. Try again later.",
            "send_error": "❌ Failed to send media. Try again.",
            "module_error": "❌ Error in unico-cat module: {}",
            "media_error": "Error sending media: {}",
            "fetch_error": "Error fetching media: {}",
            "cache_updated": "Unico cache updated. Latest {} media received",
            "cache_error": "Error updating Unico cache: {}",
            "video": "video",
            "photo": "photo",
            "document": "document",
            "media": "media",
        },
    }

    lang_strings = strings.get(language, strings["en"])

    async def send_media_as_copy(event, source_message):
        try:
            media = source_message.media

            if not media:
                return False

            caption = source_message.text or source_message.message
            if not caption:
                caption = ""

            attributes = None
            file = None

            if hasattr(source_message, "video") and source_message.video:
                attributes = source_message.video.attributes
                file = source_message.video

            elif hasattr(source_message, "document") and source_message.document:
                attributes = source_message.document.attributes
                file = source_message.document

            if file:
                result = await kernel.client.send_file(
                    event.chat_id,
                    file,
                    caption=caption,
                    attributes=attributes,
                    supports_streaming=True,
                    silent=True,
                )

                return True

            return False

        except Exception as e:
            await kernel.log_error(lang_strings["media_error"].format(e))
            return False

    async def get_media_messages(filter_type=None, limit=100):
        try:
            messages = []

            async for message in kernel.client.iter_messages(
                UNICO_CHANNEL_ID, limit=limit, filter=filter_type
            ):
                if message.media:
                    messages.append(message)

            return messages

        except Exception as e:
            await kernel.log_error(lang_strings["fetch_error"].format(e))
            return []

    @kernel.register.command("unico")
    # oтпpaвить юнe / send unico
    async def unico_handler(event):
        try:
            msg = await event.edit(lang_strings["searching"])
            all_media = []
            gifs = await get_media_messages(InputMessagesFilterGif, limit=50)
            all_media.extend(gifs)

            videos = await get_media_messages(InputMessagesFilterVideo, limit=50)
            all_media.extend(videos)

            photos_videos = await get_media_messages(
                InputMessagesFilterPhotoVideo, limit=50
            )
            all_media.extend(photos_videos)

            unique_media = {}
            for m in all_media:
                unique_media[m.id] = m

            media_list = list(unique_media.values())

            if not media_list:
                await event.edit(lang_strings["no_media"])
                return

            random_media = random.choice(media_list)
            await msg.delete()
            success = await send_media_as_copy(event, random_media)

            if success:
                media_type = lang_strings["media"]
                if hasattr(random_media, "video"):
                    media_type = lang_strings["video"]
                elif hasattr(random_media, "photo"):
                    media_type = lang_strings["photo"]
                elif hasattr(random_media, "document"):
                    media_type = lang_strings["document"]
            else:
                await event.respond(lang_strings["send_error"])

        except Exception as e:
            error_msg = lang_strings["module_error"].format(str(e))
            await kernel.handle_error(e, source="unico_handler", event=event)
            await event.edit(error_msg)

    @kernel.register.loop(interval=100)
    async def update_unico_cache(kernel):
        try:
            recent_media = await get_media_messages(limit=40)

            if recent_media:
                kernel.logger.info(
                    lang_strings["cache_updated"].format(len(recent_media))
                )

        except Exception as e:
            kernel.logger.error(lang_strings["cache_error"].format(e))
