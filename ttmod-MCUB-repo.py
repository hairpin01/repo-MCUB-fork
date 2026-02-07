# requires: yt-dlp
# author: MCUB Developer
# version: 1.0.0
# description: TikTok video downloader
import asyncio
import os
import tempfile
from urllib.parse import urlparse

# Premium emoji definitions
CUSTOM_EMOJI = {
    'success': '<tg-emoji emoji-id="5321304062715517873">🛰</tg-emoji>',
    'error': '<tg-emoji emoji-id="5433784166661513639">🎁</tg-emoji>',
    'download': '<tg-emoji emoji-id="5332654441508119011">🫥</tg-emoji>',
    'info': '<tg-emoji emoji-id="5334882760735598374">📝</tg-emoji>',
    'link': '<tg-emoji emoji-id="5377844313575150051">📎</tg-emoji>',
    'time': '<tg-emoji emoji-id="5350813992732338949">🐢</tg-emoji>',
    'disk': '<tg-emoji emoji-id="5433653135799228968">📁</tg-emoji>'
}

# Localization strings
LOCALIZATION = {
    'en': {
        'usage': 'Usage: <code>.tiktok [URL]</code> or <code>.tt [URL]</code>',
        'downloading': 'Downloading TikTok video...',
        'success': 'Video downloaded successfully!',
        'no_url': 'Please provide a TikTok URL',
        'invalid_url': 'Invalid TikTok URL',
        'download_failed': 'Failed to download video',
        'file_too_large': 'Video file is too large',
        'error': 'An error occurred',
        'stats': 'Video information:',
        'duration': 'Duration:',
        'resolution': 'Resolution:',
        'size': 'Size:',
        'author': 'Author:',
        'description': 'Description:',
        'processing': 'Processing video...',
        'cleaning': 'Cleaning temporary files...'
    },
    'ru': {
        'usage': 'Использование: <code>.tiktok [URL]</code> или <code>.tt [URL]</code>',
        'downloading': 'Скачивание видео из TikTok...',
        'success': 'Видео успешно скачано!',
        'no_url': 'Пожалуйста, укажите ссылку на TikTok',
        'invalid_url': 'Некорректная ссылка на TikTok',
        'download_failed': 'Не удалось скачать видео',
        'file_too_large': 'Файл видео слишком большой',
        'error': 'Произошла ошибка',
        'stats': 'Информация о видео:',
        'duration': 'Длительность:',
        'resolution': 'Разрешение:',
        'size': 'Размер:',
        'author': 'Автор:',
        'description': 'Описание:',
        'processing': 'Обработка видео...',
        'cleaning': 'Очистка временных файлов...'
    }
}

def is_valid_tiktok_url(url):
    """Validate TikTok URL"""
    try:
        parsed = urlparse(url)
        if not parsed.netloc:
            return False

        valid_domains = ['tiktok.com', 'vt.tiktok.com', 'vm.tiktok.com', 'www.tiktok.com']
        domain = parsed.netloc.lower()

        return any(valid_domain in domain for valid_domain in valid_domains)
    except:
        return False

async def download_tiktok_video(url, temp_dir):
    """Download TikTok video using yt-dlp"""
    import yt_dlp

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
        'extract_flat': False,
        'noplaylist': True,
        'progress_hooks': [],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            kernel.logger.debug(f"[TikTok] Starting download: {url}")

            # Get video info
            info = await asyncio.to_thread(ydl.extract_info, url, download=False)

            if not info:
                await kernel.logger.error("[TikTok] Failed to extract video info")
                return None, None

            # Download video
            kernel.logger.debug(f"[TikTok] Downloading: {info.get('title', 'Unknown')}")
            result = await asyncio.to_thread(ydl.extract_info, url, download=True)

            if not result:
                kernel.logger.error("[TikTok] Download failed")
                return None, None

            # Find downloaded file
            downloaded_files = []
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    if file.endswith(('.mp4', '.webm', '.mkv')):
                        downloaded_files.append(os.path.join(root, file))

            if not downloaded_files:
                await kernel.logger.error("[TikTok] No video file found after download")
                return None, result

            return downloaded_files[0], result

    except Exception as e:
        kernel.logger.error(f"[TikTok] Download error: {str(e)}")
        return None, None

def register(kernel):
    """Register TikTok downloader module"""

    # Get current language
    language = kernel.config.get('language', 'en')
    lang_strings = LOCALIZATION.get(language, LOCALIZATION['en'])

    # Register command using new API
    @kernel.register.command('tiktok', alias=['tt', 'tik'])
    async def tiktok_downloader(event):
        """Download TikTok videos"""

        try:
            # Log command usage
            kernel.logger.debug(
                f"[TikTok] Command invoked by user {event.sender_id} "
                f"in chat {event.chat_id}"
            )

            # Get URL from message
            args = event.text.split(maxsplit=1)
            if len(args) < 2:
                await kernel.edit_with_html(
                    event,
                    f"{CUSTOM_EMOJI['error']} <b>{lang_strings['no_url']}</b>\n\n"
                    f"{CUSTOM_EMOJI['info']} {lang_strings['usage']}"
                )
                kernel.logger.warning("[TikTok] No URL provided")
                return

            url = args[1].strip()

            # Validate URL
            if not is_valid_tiktok_url(url):
                await kernel.edit_with_html(
                    event,
                    f"{CUSTOM_EMOJI['error']} <b>{lang_strings['invalid_url']}</b>\n\n"
                    f"{CUSTOM_EMOJI['link']} <code>{url}</code>"
                )
                kernel.logger.warning(f"[TikTok] Invalid URL: {url}")
                return

            kernel.logger.info(f"[TikTok] Processing URL: {url}")

            # Update message to show downloading status
            await kernel.edit_with_html(
                event,
                f"{CUSTOM_EMOJI['download']} <b>{lang_strings['downloading']}</b>\n\n"
                f"{CUSTOM_EMOJI['link']} <code>{url}</code>"
            )

            # Create temporary directory
            with tempfile.TemporaryDirectory() as temp_dir:
                kernel.logger.debug(f"[TikTok] Created temp dir: {temp_dir}")

                # Download video
                file_path, video_info = await download_tiktok_video(url, temp_dir)

                if not file_path or not video_info:
                    await kernel.edit_with_html(
                        event,
                        f"{CUSTOM_EMOJI['error']} <b>{lang_strings['download_failed']}</b>"
                    )
                    kernel.logger.error(f"[TikTok] Download failed for URL: {url}")
                    return


                file_size = os.path.getsize(file_path)
                if file_size > 50 * 1024 * 1024:  # 50MB
                    await kernel.edit_with_html(
                        event,
                        f"{CUSTOM_EMOJI['error']} <b>{lang_strings['file_too_large']}</b>\n"
                        f"{CUSTOM_EMOJI['disk']} Size: {file_size / (1024*1024):.1f}MB"
                    )
                    await kernel.logger.warning(
                        f"[TikTok] File too large: {file_size / (1024*1024):.1f}MB"
                    )


                kernel.logger.info(
                    f"[TikTok] Download completed: {file_path} "
                    f"({file_size / (1024*1024):.1f}MB)"
                )

                # Update message to show processing
                await kernel.edit_with_html(
                    event,
                    f"{CUSTOM_EMOJI['info']} <b>{lang_strings['processing']}</b>"
                )

                # Prepare caption with video info
                caption = (
                    f"{CUSTOM_EMOJI['success']} <b>{lang_strings['success']}</b>\n\n"
                    f"{CUSTOM_EMOJI['info']} <b>{lang_strings['stats']}</b>\n"
                )

                # Add video information
                if video_info.get('title'):
                    caption += f"📝 <b>Title:</b> {video_info['title']}\n"

                if video_info.get('duration'):
                    minutes = int(video_info['duration'] // 60)
                    seconds = int(video_info['duration'] % 60)
                    caption += (
                        f"{CUSTOM_EMOJI['time']} <b>{lang_strings['duration']}</b> "
                        f"{minutes}:{seconds:02d}\n"
                    )

                if video_info.get('resolution'):
                    caption += f"🖨 <b>{lang_strings['resolution']}</b> {video_info['resolution']}\n"

                caption += f"{CUSTOM_EMOJI['disk']} <b>{lang_strings['size']}</b> {file_size / (1024*1024):.1f}MB\n"

                if video_info.get('uploader'):
                    caption += f"👤 <b>{lang_strings['author']}</b> {video_info['uploader']}\n"

                if video_info.get('description'):
                    desc = video_info['description'][:100] + "..." if len(video_info['description']) > 100 else video_info['description']
                    caption += f"📖 <b>{lang_strings['description']}</b> {desc}\n"

                # Send video
                kernel.logger.info("[TikTok] Sending video to chat...")

                try:
                    await event.edit(
                        text=caption,
                        file=file_path,
                        parse_mode='html',
                        link_preview=False
                    )

                    # Delete the original command message
                    # await event.delete()

                    kernel.logger.info("[TikTok] Video sent successfully")

                except Exception as send_error:
                    kernel.logger.error(f"[TikTok] Failed to send video: {str(send_error)}")
                    await kernel.edit_with_html(
                        event,
                        f"{CUSTOM_EMOJI['error']} <b>{lang_strings['error']}:</b> {str(send_error)}"
                    )

                # Cleanup
                kernel.logger.debug("[TikTok] Cleaning up temporary files")

        except Exception as e:
            # Log detailed error
            kernel.logger.error(f"[TikTok] Critical error: {str(e)}")

            # Handle error with kernel's error handler
            await kernel.handle_error(e, source="tiktok_downloader", event=event)

            # Send error message to user
            try:
                await kernel.edit_with_html(
                    event,
                    f"{CUSTOM_EMOJI['error']} <b>{lang_strings['error']}</b>\n\n"
                    f"<code>{str(e)[:200]}</code>"
                )
            except:
                pass

