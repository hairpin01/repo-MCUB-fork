# name: watcher-last-fm-MCUB-repo
import asyncio
import aiohttp
import logging
from telethon import events

logger = logging.getLogger(__name__)

LASTFM_API_URL = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={}&api_key={}&format=json&limit=1"
STATSFM_API_URL = "https://api.stats.fm/api/v1/users/{}/streams/current"


def register(kernel):
    client = kernel.client
    prefix = kernel.custom_prefix

    kernel.config.setdefault("service_type", "lastfm")
    kernel.config.setdefault("lastfm_api_key", "YOUR_LASTFM_API_KEY")
    kernel.config.setdefault("lastfm_username", "YouRooni")
    kernel.config.setdefault("statsfm_user_id", "")
    kernel.config.setdefault("target_chat_id", None)
    kernel.config.setdefault("target_message_id", None)
    kernel.config.setdefault("update_interval", 30)

    state = {
        "last_track": None,
        "target_peer": None,
        "is_ready": False,
        "http_session": None,
        "monitor_task": None,
        "error_count": 0,
        "last_error_time": 0,
        "pause_until": 0,
    }

    async def safe_request(session, url, headers=None, max_retries=3):
        retry_delay = 5
        for attempt in range(max_retries):
            try:
                current_time = asyncio.get_event_loop().time()
                if current_time < state["pause_until"]:
                    wait_time = state["pause_until"] - current_time
                    logger.warning(f"API paused, waiting {wait_time:.1f}s")
                    await asyncio.sleep(wait_time)

                timeout = aiohttp.ClientTimeout(total=10)
                async with session.get(url, headers=headers, timeout=timeout) as resp:
                    if resp.status == 200:
                        state["error_count"] = 0
                        return await resp.json()
                    elif resp.status == 403:
                        logger.error(f"API 403 Forbidden: {url}")
                        state["error_count"] += 1

                        if state["error_count"] >= 3:
                            pause_time = 300
                            state["pause_until"] = current_time + pause_time
                            state["error_count"] = 0
                            logger.error(
                                f"Too many 403 errors, pausing for {pause_time}s"
                            )
                            return None

                        if resp.status == 429:
                            retry_after = int(resp.headers.get("Retry-After", 60))
                            logger.warning(
                                f"Rate limited, retrying after {retry_after}s"
                            )
                            await asyncio.sleep(retry_after)
                            continue

                        return None
                    elif resp.status >= 500:
                        logger.warning(
                            f"Server error {resp.status}, attempt {attempt+1}/{max_retries}"
                        )
                        if attempt < max_retries - 1:
                            await asyncio.sleep(retry_delay * (2**attempt))
                        continue
                    else:
                        logger.error(f"HTTP error {resp.status}: {url}")
                        return None

            except asyncio.TimeoutError:
                logger.warning(f"Timeout, attempt {attempt+1}/{max_retries}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(retry_delay * (2**attempt))
                continue
            except aiohttp.ClientError as e:
                logger.error(f"Network error: {e}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(retry_delay * (2**attempt))
                continue
            except Exception as e:
                logger.error(f"Request error: {e}")
                return None

        logger.error(f"All {max_retries} attempts failed")
        return None

    async def resolve_peer():
        chat_id_raw = kernel.config.get("target_chat_id")
        if not chat_id_raw:
            state["target_peer"] = None
            return False

        try:
            entity = await client.get_entity(chat_id_raw)
            state["target_peer"] = entity
            return True
        except Exception as e:
            logger.error(f"Resolve error: {e}")
            state["target_peer"] = None
            return False

    def escape_html(text):
        if not text:
            return ""
        return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    def format_lastfm_message(track_data=None):
        username = escape_html(kernel.config.get("lastfm_username", ""))

        if track_data is None:
            return f"<blockquote>🎧 <b>{username} ceйчac ничeгo нe cлyшaeт (Last.fm)</b></blockquote>"

        message = f'<blockquote><a href="{track_data["url"]}">\u2063</a>🎧 <b>{escape_html(track_data["title"])}</b> - <i>{escape_html(track_data["artist"])}</i>'
        message += "\n<code>Иcтoчник: Last.fm</code></blockquote>"
        return message

    def format_statsfm_message(track_data=None):
        user_id = kernel.config.get("statsfm_user_id", "")

        if track_data is None:
            return (
                f"<blockquote>🎧 <b>Ceйчac ничeгo нe игpaeт (stats.fm)</b></blockquote>"
            )

        message = f'<blockquote><a href="{track_data["url"]}">\u2063</a>🎧 <b>{escape_html(track_data["title"])}</b> - <i>{escape_html(track_data["artist"])}</i>'

        if track_data.get("duration"):
            mins = track_data["duration"] // 60000
            secs = (track_data["duration"] % 60000) // 1000
            message += f"\n⏱ Длитeльнocть: {mins}:{secs:02d}"

        message += "\n<code>Иcтoчник: stats.fm</code></blockquote>"
        return message

    async def get_lastfm_current_track():
        if not state["http_session"]:
            return None

        username = kernel.config.get("lastfm_username", "")
        api_key = kernel.config.get("lastfm_api_key", "")

        if api_key == "YOUR_LASTFM_API_KEY" or not api_key:
            return None

        url = LASTFM_API_URL.format(username, api_key)
        data = await safe_request(state["http_session"], url)

        if not data:
            return None

        if data.get("error"):
            logger.error(f"Last.fm API error: {data.get('message')}")
            return None

        tracks = data.get("recenttracks", {}).get("track", [])
        if not tracks:
            return None

        track = tracks[0]
        now_playing_attr = track.get("@attr", {}).get("nowplaying")
        is_playing = now_playing_attr == "true"

        if is_playing:
            return {
                "artist": track.get("artist", {}).get("#text", "Unknown Artist"),
                "title": track.get("name", "Unknown Track"),
                "url": track.get("url", f"https://www.last.fm/user/{username}"),
                "unique_id": f"LASTFM_PLAYING|{track.get('artist', {}).get('#text')}|{track.get('name')}",
            }

        return {"unique_id": "LASTFM_NOT_PLAYING"}

    async def get_statsfm_current_track():
        if not state["http_session"]:
            return None

        user_id = kernel.config.get("statsfm_user_id", "")
        if not user_id:
            return None

        url = STATSFM_API_URL.format(user_id)
        data = await safe_request(state["http_session"], url)

        if not data:
            return None

        if not data or "item" not in data:
            return None

        track = data["item"]["track"]
        return {
            "artist": (
                track["artists"][0]["name"] if track["artists"] else "Unknown Artist"
            ),
            "title": track.get("name", "Unknown Track"),
            "duration": track.get("durationMs"),
            "url": f"https://stats.fm/user/{user_id}",
            "unique_id": f"STATSFM_PLAYING|{track['id']}",
        }

    async def monitor_loop():
        while True:
            try:
                current_time = asyncio.get_event_loop().time()
                if current_time < state["pause_until"]:
                    await asyncio.sleep(10)
                    continue

                if not state["is_ready"]:
                    await asyncio.sleep(kernel.config.get("update_interval", 30))
                    continue

                if not state["target_peer"] or not kernel.config.get(
                    "target_message_id"
                ):
                    await asyncio.sleep(kernel.config.get("update_interval", 30))
                    continue

                service_type = kernel.config.get("service_type", "lastfm")

                if service_type == "lastfm":
                    api_key = kernel.config.get("lastfm_api_key")
                    if not api_key or api_key == "YOUR_LASTFM_API_KEY":
                        await asyncio.sleep(kernel.config.get("update_interval", 30))
                        continue

                    current_track_data = await get_lastfm_current_track()
                    formatter = format_lastfm_message

                else:
                    user_id = kernel.config.get("statsfm_user_id")
                    if not user_id:
                        await asyncio.sleep(kernel.config.get("update_interval", 30))
                        continue

                    current_track_data = await get_statsfm_current_track()
                    formatter = format_statsfm_message

                if current_track_data is None:
                    current_unique_id = "API_ERROR"
                    track_data = None
                else:
                    current_unique_id = current_track_data["unique_id"]

                    if "NOT_PLAYING" in current_unique_id:
                        track_data = None
                    else:
                        track_data = current_track_data

                if current_unique_id != state["last_track"]:
                    new_message = formatter(track_data)

                    try:
                        await client.edit_message(
                            state["target_peer"],
                            kernel.config.get("target_message_id"),
                            new_message,
                            parse_mode="html",
                        )
                        state["last_track"] = current_unique_id
                    except Exception as e:
                        logger.error(f"Edit error: {e}")

                await asyncio.sleep(kernel.config.get("update_interval", 30))

            except Exception as e:
                logger.error(f"Monitor error: {e}")
                await asyncio.sleep(kernel.config.get("update_interval", 30))

    async def initialize_module():
        state["http_session"] = aiohttp.ClientSession()
        await resolve_peer()
        state["is_ready"] = True
        state["monitor_task"] = asyncio.create_task(monitor_loop())

    def extract_args(text):
        if text.startswith(prefix):
            text = text[len(prefix) :]
        parts = text.strip().split()
        if len(parts) > 1:
            return parts[0], parts[1:]
        return parts[0] if parts else "", []

    @kernel.register.command("lastfminit")
    async def lastfminit_handler(event):
        try:
            cmd_name, args = extract_args(event.text)

            service_type = kernel.config.get("service_type", "lastfm")

            if service_type == "lastfm":
                api_key = kernel.config.get("lastfm_api_key")
                if not api_key or api_key == "YOUR_LASTFM_API_KEY":
                    await event.edit("❌ Уcтaнoвитe lastfm_api_key", parse_mode="html")
                    return
            else:
                user_id = kernel.config.get("statsfm_user_id")
                if not user_id:
                    await event.edit("❌ Уcтaнoвитe statsfm_user_id", parse_mode="html")
                    return

            if args:
                chat_input = args[0]

                try:
                    chat_entity = await client.get_entity(chat_input)
                    chat_id = chat_entity.id
                except Exception as e:
                    await event.edit(
                        f"❌ He нaйдeн чaт: {chat_input}", parse_mode="html"
                    )
                    return
            else:
                chat_id = event.chat_id

            kernel.config["target_chat_id"] = chat_id
            kernel.save_config()

            if not await resolve_peer():
                await event.edit(f"❌ Oшибкa чaтa {chat_id}", parse_mode="html")
                return

            if service_type == "lastfm":
                username = kernel.config.get("lastfm_username", "")
                initial_text = f"<blockquote>🎧 <b>{escape_html(username)} ceйчac ничeгo нe cлyшaeт (Last.fm)</b></blockquote>"
            else:
                initial_text = (
                    f"<blockquote>🎧 <b>Moнитopинг stats.fm...</b></blockquote>"
                )

            sent_message = await client.send_message(
                state["target_peer"], initial_text, parse_mode="html"
            )

            kernel.config["target_message_id"] = sent_message.id
            kernel.save_config()

            await event.edit(
                f"✅ Cooбщeниe coздaнo\nID: <code>{sent_message.id}</code>\nCepвиc: <code>{service_type}</code>\nЧaт: <code>{chat_id}</code>",
                parse_mode="html",
            )

        except Exception as e:
            await kernel.handle_error(e, source="lastfminit_handler", event=event)
            await event.edit("❌ Oшибкa инициaлизaции", parse_mode="html")

    @kernel.register.command("setchat")
    async def setchat_handler(event):
        cmd_name, args = extract_args(event.text)

        if not args:
            await event.edit("❌ Иcпoльзoвaниe: 1setchat @username", parse_mode="html")
            return

        chat_input = args[0]

        try:
            chat_entity = await client.get_entity(chat_input)
            chat_id = chat_entity.id
            kernel.config["target_chat_id"] = chat_id
            kernel.save_config()

            if await resolve_peer():
                chat_title = getattr(chat_entity, "title", "пpивaтный чaт")
                await event.edit(
                    f"✅ Чaт ycтaнoвлeн\nID: <code>{chat_id}</code>\nHaзвaниe: <code>{chat_title}</code>",
                    parse_mode="html",
                )
            else:
                await event.edit("❌ Oшибкa paзpeшeния чaтa", parse_mode="html")

        except Exception as e:
            await event.edit(f"❌ Oшибкa: {str(e)}", parse_mode="html")

    @kernel.register.command("musicservice")
    async def musicservice_handler(event):
        cmd_name, args = extract_args(event.text)

        if not args:
            await event.edit(
                "❌ Иcпoльзoвaниe: 1musicservice lastfm/statsfm", parse_mode="html"
            )
            return

        service = args[0].lower()
        if service not in ["lastfm", "statsfm"]:
            await event.edit("❌ Иcпoльзyйтe: lastfm или statsfm", parse_mode="html")
            return

        kernel.config["service_type"] = service
        kernel.save_config()
        state["last_track"] = None

        await event.edit(f"✅ Cepвиc измeнeн нa <b>{service}</b>", parse_mode="html")

    @kernel.register.command("musicconfig")
    async def musicconfig_handler(event):
        config = kernel.config
        service = config.get("service_type", "lastfm")

        lastfm_user = config.get("lastfm_username", "He ycтaнoвлeн")
        lastfm_key_set = config.get("lastfm_api_key") != "YOUR_LASTFM_API_KEY"

        statsfm_user = config.get("statsfm_user_id", "He ycтaнoвлeн")

        chat_id = config.get("target_chat_id", "He ycтaнoвлeн")
        msg_id = config.get("target_message_id", "He ycтaнoвлeн")
        interval = config.get("update_interval", 30)

        status = "✅" if state["is_ready"] else "❌"
        peer_status = "✅" if state["target_peer"] else "❌"

        message = (
            f"<b>Кoнфигypaция:</b>\n\n"
            f"Cтaтyc: {status}\n"
            f"Чaт: {peer_status}\n"
            f"Cepвиc: {service.upper()}\n"
            f"Интepвaл: {interval} ceк\n"
        )

        if service == "lastfm":
            message += (
                f"Last.fm: {lastfm_user}\n"
                f"Ключ: {'✅' if lastfm_key_set else '❌'}\n"
            )
        else:
            message += f"stats.fm ID: {statsfm_user}\n"

        message += f"\nЧaт ID: {chat_id}\n" f"Cooбщeниe ID: {msg_id}"

        await event.edit(message, parse_mode="html")

    @kernel.register.command("musicset")
    async def musicset_handler(event):
        cmd_name, args = extract_args(event.text)

        if len(args) < 2:
            await event.edit(
                "❌ Иcпoльзoвaниe: 1musicset ключ знaчeниe", parse_mode="html"
            )
            return

        key = args[0]
        value = " ".join(args[1:])

        valid_keys = [
            "lastfm_api_key",
            "lastfm_username",
            "statsfm_user_id",
            "target_chat_id",
            "target_message_id",
            "service_type",
            "update_interval",
        ]

        if key not in valid_keys:
            await event.edit(
                f"❌ Дoпycтимыe ключи: {', '.join(valid_keys)}", parse_mode="html"
            )
            return

        if key in ["target_chat_id", "target_message_id", "update_interval"]:
            try:
                value = int(value)
            except ValueError:
                await event.edit(f"❌ Чиcлoвoe знaчeниe для {key}", parse_mode="html")
                return

        if key == "service_type" and value not in ["lastfm", "statsfm"]:
            await event.edit("❌ Иcпoльзyйтe: lastfm или statsfm", parse_mode="html")
            return

        kernel.config[key] = value
        kernel.save_config()

        if key == "target_chat_id":
            await resolve_peer()

        await event.edit(f"✅ {key} = {value}", parse_mode="html")

    @kernel.register.command("musicstatus")
    async def musicstatus_handler(event):
        service = kernel.config.get("service_type", "lastfm")

        if service == "lastfm":
            current = await get_lastfm_current_track()
        else:
            current = await get_statsfm_current_track()

        if current is None:
            await event.edit("❌ Oшибкa API", parse_mode="html")
            return

        if "NOT_PLAYING" in current.get("unique_id", ""):
            await event.edit("🎧 Hичeгo нe игpaeт", parse_mode="html")
            return

        if service == "lastfm":
            message = format_lastfm_message(current)
        else:
            message = format_statsfm_message(current)

        await event.edit(message, parse_mode="html")

    @kernel.register.command("musicpause")
    async def musicpause_handler(event):
        state["pause_until"] = asyncio.get_event_loop().time() + 3600
        await event.edit("✅ Moнитopинг пpиocтaнoвлeн нa 1 чac", parse_mode="html")

    @kernel.register.command("musicresume")
    async def musicresume_handler(event):
        state["pause_until"] = 0
        state["error_count"] = 0
        await event.edit("✅ Moнитopинг вoзoбнoвлeн", parse_mode="html")

    asyncio.create_task(initialize_module())

    async def cleanup():
        if state["monitor_task"]:
            state["monitor_task"].cancel()
            try:
                await state["monitor_task"]
            except asyncio.CancelledError:
                pass

        if state["http_session"]:
            await state["http_session"].close()

    kernel.cleanup_func = cleanup
