# requires: shazamio, aiofiles, aiohttp
# author: @Mitrichq && @Hairpin00
# version: 2.0.0
# description: music recognition module with inline results

import asyncio
import aiofiles
import aiohttp
import os
import io
from shazamio import Shazam
from telethon import Button

def register(kernel):
    client = kernel.client
    prefix = kernel.custom_prefix

    @kernel.register_command('shazam')
    # recognize music from audio/video/voice message
    async def shazam_cmd(event):
        try:
            if not event.is_reply:
                await event.edit('🔇 <b>reply to audio/video/voice message</b>', parse_mode='html')
                return

            reply = await event.get_reply_message()
            if not (reply.audio or reply.voice or reply.video):
                await event.edit('🎵 <b>message must contain audio/video</b>', parse_mode='html')
                return

            await event.edit('🎧 <b>recognizing music...</b>', parse_mode='html')

            file_path = await reply.download_media()

            try:
                shazam = Shazam()
                result = await shazam.recognize_song(file_path)

                if os.path.exists(file_path):
                    await asyncio.to_thread(os.remove, file_path)

                if 'track' in result:
                    track = result['track']
                    title = track.get('title', 'Unknown')
                    artist = track.get('subtitle', 'Unknown Artist')


                    cover_url = None
                    if 'images' in track and 'coverarthq' in track['images']:
                        cover_url = track['images']['coverarthq']


                    album = 'Unknown Album'
                    year = 'Unknown Year'
                    if 'sections' in track:
                        for section in track['sections']:
                            if section['type'] == 'SONG':
                                metadata = section.get('metadata', [])
                                for item in metadata:
                                    if item['title'] == 'Альбом':
                                        album = item['text']
                                    elif item['title'] == 'Выпущено':
                                        year = item['text']


                    shazam_link = track.get('share', {}).get('href', '')


                    buttons = []
                    if shazam_link:
                        buttons.append([Button.url('🎵 Listen on Shazam', shazam_link)])

                    if kernel.config.get('inline_bot_username'):
                        await event.delete()


                        result_text = (
                            f"🎵 <b>{title}</b>\n"
                            f"👤 <b>Artist:</b> {artist}\n"
                            f"💿 <b>Album:</b> {album}\n"
                            f"📅 <b>Year:</b> {year}\n\n"
                            f"🔍 <i>Recognized via Shazam</i>"
                        )


                        photo = None
                        if cover_url:
                            try:
                                timeout = aiohttp.ClientTimeout(total=10)
                                async with aiohttp.ClientSession(timeout=timeout) as session:
                                    async with session.get(cover_url) as resp:
                                        if resp.status == 200:
                                            photo_data = await resp.read()
                                            photo = io.BytesIO(photo_data)
                                            photo.name = 'cover.jpg'
                            except Exception:
                                photo = None


                        if photo:
                            await client.send_file(
                                event.chat_id,
                                photo,
                                caption=result_text,
                                buttons=buttons if buttons else None,
                                parse_mode='html'
                            )
                        else:
                            await client.send_message(
                                event.chat_id,
                                result_text,
                                buttons=buttons if buttons else None,
                                parse_mode='html'
                            )
                    else:

                        result_text = (
                            f"🎵 <b>{title}</b>\n"
                            f"👤 <b>Artist:</b> {artist}\n"
                            f"💿 <b>Album:</b> {album}\n"
                            f"📅 <b>Year:</b> {year}\n"
                        )

                        if shazam_link:
                            result_text += f"\n🔗 <a href='{shazam_link}'>Open in Shazam</a>"

                        await event.edit(result_text, parse_mode='html')

                else:
                    await event.edit('🎼 <b>music not recognized</b>', parse_mode='html')
            except asyncio.TimeoutError:
                if os.path.exists(file_path):
                    await asyncio.to_thread(os.remove, file_path)
                await event.edit('⛈️ <b>recognition timeout</b>', parse_mode='html')
        except Exception as e:
            await kernel.handle_error(e, source="shazam_cmd", event=event)
            await event.edit("🌩️ <b>error, check logs</b>", parse_mode='html')

    async def shazam_inline_handler(event):
        """Inline search for music (requires text query)"""
        try:
            query = event.text
            if not query:
                builder = event.builder.article(
                    title='🎵 Music Recognition',
                    text='Send me an audio message or type song name',
                    buttons=[[Button.switch_inline('Search Music', query='')]]
                )
                await event.answer([builder])
                return

            # Search for music (simplified example)
            builder = event.builder.article(
                title=f'Search: {query}',
                text=f'🔍 Searching for "{query}" on Shazam...\n\nUse .shazam command on audio files for recognition.',
                buttons=[
                    [Button.url('Search on Shazam', f'https://www.shazam.com/search?term={query}')],
                    [Button.switch_inline('New Search', query='')]
                ]
            )
            await event.answer([builder])
        except Exception as e:
            await kernel.handle_error(e, source="shazam_inline", event=event)

    kernel.register_inline_handler('shazam', shazam_inline_handler)
