# name: ytm-beta-MCUB-repo
# requires: yt-dlp, ytmusicapi
# author: OpenAI && @Hairpin00
# version: 1.0.0-beta
# description: YouTube Music audio downloader with beta now playing integration

import asyncio
import os
import tempfile
from urllib.parse import urlparse

import aiohttp
from telethon import types

from utils import escape_html, get_args_raw

EMOJI = {
    "music": '<tg-emoji emoji-id="5870794890006237381">🎶</tg-emoji>',
    "link": '<tg-emoji emoji-id="5271604874419647061">🔗</tg-emoji>',
    "error": '<tg-emoji emoji-id="5854929766146118183">❌</tg-emoji>',
    "load": '<tg-emoji emoji-id="5334768819548200731">💻</tg-emoji>',
    "beta": '<tg-emoji emoji-id="5460932990283153991">🧪</tg-emoji>',
    "ok": '<tg-emoji emoji-id="5321304062715517873">🛰</tg-emoji>',
}

STRINGS = {
    "ru": {
        "help": (
            "<b>YouTube Music beta</b>\n"
            "<code>{p}ytm &lt;ccылкa|зaпpoc&gt;</code> - cкaчaть ayдиo\n"
            "<code>{p}ytmauth &lt;path&gt;</code> - пyть к headers_auth.json для YouTube Music\n"
            "<code>{p}ytnow</code> - beta now playing из иcтopии aккayнтa YouTube Music\n"
            "<code>{p}ytnowdl</code> - cкaчaть пocлeдний тpeк из beta now playing\n"
            "<i>Для beta now playing нyжeн <code>ytmusicapi</code> и экcпopтиpoвaнный auth headers json.</i>"
        ),
        "no_query": "Укaжи ccылкy или пoиcкoвый зaпpoc.",
        "downloading": "Ищy и пoдгoтaвливaю ayдиo...",
        "sending": "Oтпpaвляю тpeк...",
        "download_failed": "He yдaлocь пoлyчить тpeк.",
        "auth_usage": "Иcпoльзoвaниe: <code>{p}ytmauth &lt;/path/to/headers_auth.json&gt;</code>",
        "auth_missing": "Cнaчaлa yкaжи auth headers: <code>{p}ytmauth &lt;path&gt;</code>",
        "auth_saved": "Пyть к auth headers coxpaнён:\n<code>{path}</code>",
        "auth_not_found": "Фaйл нe нaйдeн:\n<code>{path}</code>",
        "ytm_missing": "He ycтaнoвлeн <code>ytmusicapi</code>.",
        "ytdlp_missing": "He ycтaнoвлeн <code>yt-dlp</code>.",
        "beta_empty": "Иcтopия YouTube Music пycтa или нeдocтyпнa.",
        "beta_now": '{beta} <b>Now Playing Beta</b>\n\n<b>{title}</b>\n<i>{artist}</i>\n\n{link} <a href="{url}">Open in YouTube Music</a>',
        "beta_note": "Beta: иcпoльзyeтcя пocлeдний тpeк из иcтopии YouTube Music, нe peaльный playback API.",
        "beta_dl": "Cкaчивaю пocлeдний тpeк из beta now playing...",
        "send_error": "He yдaлocь oтпpaвить тpeк:\n<code>{error}</code>",
    },
    "en": {
        "help": (
            "<b>YouTube Music beta</b>\n"
            "<code>{p}ytm &lt;url|query&gt;</code> - download audio\n"
            "<code>{p}ytmauth &lt;path&gt;</code> - path to YouTube Music headers_auth.json\n"
            "<code>{p}ytnow</code> - beta now playing from your YouTube Music account history\n"
            "<code>{p}ytnowdl</code> - download the latest track from beta now playing\n"
            "<i>Beta now playing requires <code>ytmusicapi</code> and exported auth headers json.</i>"
        ),
        "no_query": "Provide a URL or search query.",
        "downloading": "Searching and preparing audio...",
        "sending": "Sending track...",
        "download_failed": "Failed to fetch track.",
        "auth_usage": "Usage: <code>{p}ytmauth &lt;/path/to/headers_auth.json&gt;</code>",
        "auth_missing": "Set auth headers first: <code>{p}ytmauth &lt;path&gt;</code>",
        "auth_saved": "Auth headers path saved:\n<code>{path}</code>",
        "auth_not_found": "File not found:\n<code>{path}</code>",
        "ytm_missing": "<code>ytmusicapi</code> is not installed.",
        "ytdlp_missing": "<code>yt-dlp</code> is not installed.",
        "beta_empty": "YouTube Music history is empty or unavailable.",
        "beta_now": '{beta} <b>Now Playing Beta</b>\n\n<b>{title}</b>\n<i>{artist}</i>\n\n{link} <a href="{url}">Open in YouTube Music</a>',
        "beta_note": "Beta: this uses the latest item from YouTube Music history, not a real playback API.",
        "beta_dl": "Downloading the latest beta now playing track...",
        "send_error": "Failed to send track:\n<code>{error}</code>",
    },
}


def is_youtube_url(value):
    try:
        parsed = urlparse(value)
        domain = parsed.netloc.lower()
        return any(
            token in domain
            for token in (
                "youtube.com",
                "youtu.be",
                "music.youtube.com",
                "youtube-nocookie.com",
            )
        )
    except Exception:
        return False


def _pick_artist(info):
    artists = info.get("artists") or []
    if artists:
        first = artists[0]
        if isinstance(first, dict):
            return first.get("name") or "Unknown Artist"
        return str(first)
    return info.get("uploader") or info.get("channel") or "Unknown Artist"


async def _download_file(url, dest):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return False
            with open(dest, "wb") as f:
                f.write(await response.read())
            return True


def register(kernel):
    prefix = kernel.custom_prefix
    lang = kernel.config.get("language", "en")
    s = STRINGS.get(lang, STRINGS["en"])

    kernel.config.setdefault("ytm_auth_headers_path", "")

    async def ensure_ytdlp():
        try:
            import yt_dlp

            return yt_dlp
        except ImportError:
            return None

    async def ensure_ytmusic():
        try:
            from ytmusicapi import YTMusic

            return YTMusic
        except ImportError:
            return None

    async def resolve_and_download(query, temp_dir):
        yt_dlp = await ensure_ytdlp()
        if yt_dlp is None:
            return None, None, s["ytdlp_missing"]

        source = query if is_youtube_url(query) else f"ytsearch1:{query}"
        ydl_opts = {
            "format": "bestaudio[ext=m4a]/bestaudio/best",
            "outtmpl": os.path.join(temp_dir, "%(title)s.%(ext)s"),
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True,
            "retries": 5,
        }

        def _work():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(source, download=False)
                if info and "entries" in info:
                    info = next((item for item in info["entries"] if item), None)
                if not info:
                    return None, None
                ydl.download([info.get("webpage_url") or source])
                files = []
                for root, _, names in os.walk(temp_dir):
                    for name in names:
                        if name.lower().endswith(
                            (".m4a", ".mp3", ".webm", ".opus", ".ogg")
                        ):
                            files.append(os.path.join(root, name))
                if not files:
                    return None, info
                return max(files, key=os.path.getsize), info

        try:
            file_path, info = await asyncio.to_thread(_work)
            if not file_path or not info:
                return None, None, s["download_failed"]
            return file_path, info, None
        except Exception as e:
            return None, None, str(e)

    async def get_now_playing():
        auth_path = kernel.config.get("ytm_auth_headers_path", "")
        if not auth_path:
            return None, s["auth_missing"].format(p=prefix)
        if not os.path.exists(auth_path):
            return None, s["auth_not_found"].format(path=auth_path)

        YTMusic = await ensure_ytmusic()
        if YTMusic is None:
            return None, s["ytm_missing"]

        def _work():
            client = YTMusic(auth=auth_path)
            history = client.get_history()
            return history[0] if history else None

        try:
            item = await asyncio.to_thread(_work)
            if not item:
                return None, s["beta_empty"]
            return item, None
        except Exception as e:
            return None, str(e)

    @kernel.register.command("ytm", alias=["ytmusic", "ytplay"])
    # <url|query> - download audio from YouTube/YouTube Music
    async def ytm_handler(event):
        try:
            raw = get_args_raw(event)
            if not raw or raw.strip() == "help":
                await event.edit(s["help"].format(p=prefix), parse_mode="html")
                return

            query = raw.strip()
            await event.edit(
                f"{EMOJI['load']} <b>{s['downloading']}</b>", parse_mode="html"
            )

            with tempfile.TemporaryDirectory() as temp_dir:
                file_path, info, error = await resolve_and_download(query, temp_dir)
                if error:
                    await event.edit(
                        f"{EMOJI['error']} <b>{escape_html(error)}</b>",
                        parse_mode="html",
                    )
                    return

                title = info.get("title") or "Unknown title"
                artist = _pick_artist(info)
                duration = info.get("duration") or 0
                thumb_path = None
                thumb_url = info.get("thumbnail")
                if thumb_url:
                    thumb_path = os.path.join(temp_dir, "cover.jpg")
                    ok = await _download_file(thumb_url, thumb_path)
                    if not ok:
                        thumb_path = None

                await event.edit(
                    f"{EMOJI['music']} <b>{s['sending']}</b>", parse_mode="html"
                )
                caption = (
                    f"{EMOJI['ok']} <b>{escape_html(title)}</b>\n"
                    f"<i>{escape_html(artist)}</i>\n"
                    f"{EMOJI['link']} <a href=\"{escape_html(info.get('webpage_url') or query)}\">YouTube</a>"
                )
                await kernel.client.send_file(
                    event.chat_id,
                    file_path,
                    caption=caption,
                    parse_mode="html",
                    thumb=thumb_path,
                    attributes=[
                        types.DocumentAttributeAudio(
                            duration=int(duration),
                            title=title[:128],
                            performer=artist[:128],
                        )
                    ],
                    reply_to=event.reply_to_msg_id if event.is_reply else None,
                )
                await event.delete()

        except Exception as e:
            await kernel.handle_error(e, source="ytm_beta:ytm_handler", event=event)
            try:
                await event.edit(
                    f"{EMOJI['error']} <b>{s['send_error'].format(error=escape_html(str(e)[:300]))}</b>",
                    parse_mode="html",
                )
            except Exception:
                pass

    @kernel.register.command("ytmauth")
    # <path> - set path to YouTube Music headers_auth.json
    async def ytmauth_handler(event):
        raw = (get_args_raw(event) or "").strip()
        if not raw:
            await event.edit(s["auth_usage"].format(p=prefix), parse_mode="html")
            return
        if not os.path.exists(raw):
            await event.edit(s["auth_not_found"].format(path=raw), parse_mode="html")
            return
        kernel.config["ytm_auth_headers_path"] = raw
        if hasattr(kernel, "save_config"):
            kernel.save_config()
        await event.edit(s["auth_saved"].format(path=raw), parse_mode="html")

    @kernel.register.command("ytnow", alias=["ytnowbeta"])
    # beta now playing via YouTube Music account history
    async def ytnow_handler(event):
        try:
            item, error = await get_now_playing()
            if error:
                await event.edit(
                    f"{EMOJI['error']} <b>{escape_html(error)}</b>", parse_mode="html"
                )
                return

            video_id = item.get("videoId") or item.get("videoId".lower())
            title = item.get("title") or "Unknown title"
            artist = _pick_artist(item)
            url = (
                f"https://music.youtube.com/watch?v={video_id}"
                if video_id
                else "https://music.youtube.com"
            )
            text = (
                s["beta_now"].format(
                    beta=EMOJI["beta"],
                    title=escape_html(title),
                    artist=escape_html(artist),
                    link=EMOJI["link"],
                    url=escape_html(url),
                )
                + "\n\n"
                + f"<i>{escape_html(s['beta_note'])}</i>"
            )
            await event.edit(text, parse_mode="html", link_preview=False)
        except Exception as e:
            await kernel.handle_error(e, source="ytm_beta:ytnow_handler", event=event)
            await event.edit(
                f"{EMOJI['error']} <b>{escape_html(str(e)[:300])}</b>",
                parse_mode="html",
            )

    @kernel.register.command("ytnowdl", alias=["ytmdl"])
    # download the latest track from beta now playing
    async def ytnowdl_handler(event):
        try:
            item, error = await get_now_playing()
            if error:
                await event.edit(
                    f"{EMOJI['error']} <b>{escape_html(error)}</b>", parse_mode="html"
                )
                return

            video_id = item.get("videoId") or item.get("videoId".lower())
            query = (
                f"https://music.youtube.com/watch?v={video_id}"
                if video_id
                else item.get("title") or ""
            )
            if not query:
                await event.edit(
                    f"{EMOJI['error']} <b>{escape_html(s['download_failed'])}</b>",
                    parse_mode="html",
                )
                return

            await event.edit(
                f"{EMOJI['beta']} <b>{s['beta_dl']}</b>", parse_mode="html"
            )

            with tempfile.TemporaryDirectory() as temp_dir:
                file_path, info, dl_error = await resolve_and_download(query, temp_dir)
                if dl_error:
                    await event.edit(
                        f"{EMOJI['error']} <b>{escape_html(dl_error)}</b>",
                        parse_mode="html",
                    )
                    return

                title = info.get("title") or item.get("title") or "Unknown title"
                artist = _pick_artist(info) or _pick_artist(item)
                duration = info.get("duration") or 0
                thumb_path = None
                thumb_url = info.get("thumbnail") or item.get("thumbnails", [{}])[
                    0
                ].get("url")
                if thumb_url:
                    thumb_path = os.path.join(temp_dir, "cover.jpg")
                    ok = await _download_file(thumb_url, thumb_path)
                    if not ok:
                        thumb_path = None

                caption = (
                    f"{EMOJI['beta']} <b>{escape_html(title)}</b>\n"
                    f"<i>{escape_html(artist)}</i>\n"
                    f"{EMOJI['link']} <a href=\"{escape_html(info.get('webpage_url') or query)}\">YouTube Music</a>"
                )
                await kernel.client.send_file(
                    event.chat_id,
                    file_path,
                    caption=caption,
                    parse_mode="html",
                    thumb=thumb_path,
                    attributes=[
                        types.DocumentAttributeAudio(
                            duration=int(duration),
                            title=title[:128],
                            performer=artist[:128],
                        )
                    ],
                    reply_to=event.reply_to_msg_id if event.is_reply else None,
                )
                await event.delete()
        except Exception as e:
            await kernel.handle_error(e, source="ytm_beta:ytnowdl_handler", event=event)
            await event.edit(
                f"{EMOJI['error']} <b>{escape_html(str(e)[:300])}</b>",
                parse_mode="html",
            )
