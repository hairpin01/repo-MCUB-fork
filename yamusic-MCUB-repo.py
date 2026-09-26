# requires: aiohttp, pillow>=10.0.0, git+https://github.com/MarshalX/yandex-music-api
# scop: kernel min v1.3.0
from __future__ import annotations

import asyncio
import io
import json
import logging
import random
import string
import typing
import functools

import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

import telethon
import telethon.errors
import telethon.tl.functions.account
import telethon.types
import yandex_music
import yandex_music.exceptions

import utils
from core.lib.loader.module_base import ModuleBase, command, loop, on_install
from core.lib.loader.module_config import (
    ModuleConfig,
    ConfigValue,
    String,
    Choice,
    Integer,
    Secret,
    Boolean,
    Placeholders,
)


class Banners:
    def __init__(
        self,
        title: str,
        artists: list[str],
        duration: int,
        progress: int,
        track_cover: bytes,
        fonts_data: list[bytes],
        album_title: str = "Cингл",
        meta_info: str = "Music",
        is_liked: bool = False,
        repeat_mode: str = "NONE",
        blur: int = 0,
    ):
        self.title = title
        self.artists = artists
        self.duration = duration
        self.progress = progress
        self.track_cover = track_cover
        self.fonts_data = fonts_data
        self.album_title = album_title
        self.meta_info = meta_info
        self.is_liked = is_liked
        self.repeat_mode = repeat_mode
        self.blur = blur

    def ultra(self) -> io.BytesIO:
        WIDTH, HEIGHT = 2560, 1220

        def get_font(size):
            for font_bytes in self.fonts_data:
                try:
                    return ImageFont.truetype(io.BytesIO(font_bytes), size)
                except Exception:
                    continue
            return ImageFont.load_default()

        try:
            original_cover = Image.open(io.BytesIO(self.track_cover)).convert("RGBA")
        except Exception:
            original_cover = Image.new("RGBA", (1000, 1000), "black")

        dominant_color_img = original_cover.resize((1, 1), Image.Resampling.LANCZOS)
        dominant_color = dominant_color_img.getpixel((0, 0))

        r, g, b, a = dominant_color
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        if brightness < 60:
            r = min(255, r + 60)
            g = min(255, g + 60)
            b = min(255, b + 60)
            dominant_color = (r, g, b, 255)

        background = original_cover.copy()
        bg_w, bg_h = background.size

        target_ratio = WIDTH / HEIGHT
        current_ratio = bg_w / bg_h

        if current_ratio > target_ratio:
            new_w = int(bg_h * target_ratio)
            offset = (bg_w - new_w) // 2
            background = background.crop((offset, 0, offset + new_w, bg_h))
        else:
            new_h = int(bg_w / target_ratio)
            offset = (bg_h - new_h) // 2
            background = background.crop((0, offset, bg_w, offset + new_h))

        background = background.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)

        if self.blur > 0:
            background = background.filter(ImageFilter.GaussianBlur(radius=self.blur))

        dark_overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 180))
        background = Image.alpha_composite(background, dark_overlay)

        cover_size = 500
        cover_x = (WIDTH - cover_size) // 2
        cover_y = 160

        glow_layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
        draw_glow = ImageDraw.Draw(glow_layer)

        glow_rect_size = 620
        g_x = (WIDTH - glow_rect_size) // 2
        g_y = cover_y + (cover_size - glow_rect_size) // 2

        draw_glow.rounded_rectangle(
            (g_x, g_y, g_x + glow_rect_size, g_y + glow_rect_size),
            radius=50,
            fill=dominant_color,
        )

        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(radius=60))
        glow_layer = ImageEnhance.Brightness(glow_layer).enhance(1.4)
        glow_layer = ImageEnhance.Color(glow_layer).enhance(1.2)

        background = Image.alpha_composite(background, glow_layer)

        cover_img = original_cover.resize(
            (cover_size, cover_size), Image.Resampling.LANCZOS
        )

        mask = Image.new("L", (cover_size, cover_size), 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.rounded_rectangle((0, 0, cover_size, cover_size), radius=45, fill=255)

        background.paste(cover_img, (cover_x, cover_y), mask)

        draw = ImageDraw.Draw(background)
        center_x = WIDTH // 2
        current_y = cover_y + cover_size + 130

        def draw_text_shadow(text, pos, font, fill="white", anchor="ms"):
            x, y = pos
            draw.text(
                (x + 2, y + 2), text, font=font, fill=(0, 0, 0, 240), anchor=anchor
            )
            draw.text((x, y), text, font=font, fill=fill, anchor=anchor)

        font_title = get_font(100)
        title_text = self.title
        if len(title_text) > 30:
            title_text = title_text[:30] + "..."
        draw_text_shadow(title_text.upper(), (center_x, current_y), font_title)

        current_y += 85

        font_artist = get_font(65)
        artist_text = ", ".join(self.artists)
        if len(artist_text) > 45:
            artist_text = artist_text[:45] + "..."
        draw_text_shadow(
            artist_text.upper(),
            (center_x, current_y),
            font_artist,
            fill=(255, 255, 255, 240),
        )

        current_y += 80

        bar_width = 800
        font_time = get_font(40)

        bar_start_x = center_x - (bar_width // 2)
        bar_end_x = center_x + (bar_width // 2)
        bar_y = current_y

        total_mins = self.duration // 1000 // 60
        total_secs = (self.duration // 1000) % 60
        total_time_str = f"{total_mins:02d}:{total_secs:02d}"

        cur_mins = self.progress // 1000 // 60
        cur_secs = (self.progress // 1000) % 60
        cur_time_str = f"{cur_mins:02d}:{cur_secs:02d}"

        draw_text_shadow(
            cur_time_str, (bar_start_x - 30, bar_y), font_time, anchor="rm"
        )
        draw_text_shadow(
            total_time_str, (bar_end_x + 30, bar_y), font_time, anchor="lm"
        )

        old_state = random.getstate()
        random.seed(self.title + str(self.duration))

        num_bars = 65
        bar_spacing = bar_width / num_bars
        bar_w = max(4, int(bar_spacing * 0.5))
        max_h = 50
        min_h = 6

        if self.duration > 0:
            progress_ratio = self.progress / self.duration
        else:
            progress_ratio = 0

        active_bars = int(num_bars * progress_ratio)

        for i in range(num_bars):
            base_h = random.randint(min_h, max_h)
            edge_factor = 1.0 - abs((i - num_bars / 2) / (num_bars / 2))
            h = int(base_h * 0.4 + max_h * edge_factor * 0.6)
            h = max(min_h, h)

            x_center = bar_start_x + i * bar_spacing
            left = x_center - (bar_w / 2)
            right = x_center + (bar_w / 2)
            top = bar_y - (h / 2)
            bottom = bar_y + (h / 2)

            color = (255, 255, 255, 255) if i < active_bars else (80, 80, 80, 100)

            draw.rounded_rectangle(
                (left, top, right, bottom),
                radius=int(bar_w / 2),
                fill=color,
            )

        random.setstate(old_state)

        current_y += 80

        font_album = get_font(50)
        album_text = self.album_title
        if len(album_text) > 50:
            album_text = album_text[:50] + "..."
        draw_text_shadow(
            album_text, (center_x, current_y), font_album, fill=(230, 230, 230)
        )
        current_y += 60

        font_meta = get_font(40)
        draw_text_shadow(
            self.meta_info, (center_x, current_y), font_meta, fill=(210, 210, 210)
        )

        icon_y_center = current_y - 15

        if self.repeat_mode != "NONE":
            rep_x = bar_start_x
            rep_size = 18

            draw.arc(
                [
                    rep_x - rep_size,
                    icon_y_center - rep_size,
                    rep_x + rep_size,
                    icon_y_center + rep_size,
                ],
                start=40,
                end=320,
                fill=(220, 220, 220, 255),
                width=3,
            )
            draw.polygon(
                [
                    (rep_x + rep_size - 2, icon_y_center - 8),
                    (rep_x + rep_size + 8, icon_y_center),
                    (rep_x + rep_size - 8, icon_y_center + 4),
                ],
                fill=(220, 220, 220, 255),
            )

            if self.repeat_mode == "ONE":
                font_one = get_font(20)
                draw.text(
                    (rep_x + rep_size + 12, icon_y_center),
                    "1",
                    font=font_one,
                    fill="white",
                    anchor="lm",
                )

        by = io.BytesIO()
        background.save(by, format="PNG")
        by.seek(0)
        by.name = "banner.png"
        return by


class YaMusicModule(ModuleBase):
    name = "yamusic"
    GLOBAL_PLACEHOLDER_SCOPE = "global"
    version = "3.2.2"
    author = "@codrago_m && @Hairpin00"
    description = {
        "ru": "Яндeкc.Myзыкa - Now Playing, биoгpaфия, пoиcк, cкaчивaниe, тeкcт",
        "en": "Yandex.Music - Now Playing, bio, search, download, lyrics",
    }
    banner_url = (
        "https://raw.githubusercontent.com/kamekuro/hikka-mods/main/banners/yamusic.png"
    )

    strings: dict[str, dict[str, str]] = {
        "ru": {
            "no_token": "❌ <b>Тoкeн Яндeкc.Myзыки нe ycтaнoвлeн.</b>\nИcпoльзyйтe <code>.config YaMusic</code> и yкaжитe тoкeн.",
            "no_playing": "❌ <b>Hичeгo нe игpaeт пpямo ceйчac.</b>",
            "no_query": "❌ <b>Укaжитe зaпpoc для пoиcкa.</b>",
            "not_found": "❌ <b>Hичeгo нe нaйдeнo.</b>",
            "error": "❌ <b>Пpoизoшлa oшибкa.</b>",
            "downloading": "⏳ <b>Cкaчивaю тpeк…</b>",
            "uploading_banner": "⏳ <b>Гeнepиpyю бaннep…</b>",
            "autobio_on": "✅ <b>Aвтoбиo включeнo.</b>",
            "autobio_off": "✅ <b>Aвтoбиo выключeнo.</b>",
            "liked": '❤️ <b>Тpeк <a href="https://music.yandex.ru/track/{track_id}">{track}</a> дoбaвлeн в лaйки.</b>',
            "unliked": '💔 <b>Лaйк c тpeкa <a href="https://music.yandex.ru/track/{track_id}">{track}</a> cнят.</b>',
            "disliked": '👎 <b>Тpeк <a href="https://music.yandex.ru/track/{track_id}">{track}</a> дoбaвлeн в дизлaйки.</b>',
            "lyrics": (
                '🎵 <b><a href="https://music.yandex.ru/track/{track_id}">{track}</a></b>\n\n'
                "{text}\n\n"
                "<i>✍️ Aвтopы: {writers}</i>"
            ),
            "no_lyrics": '❌ <b>Тeкcт для тpeкa <a href="https://music.yandex.ru/track/{track_id}">{track}</a> нe нaйдeн.</b>',
            "search": '🎵 <b>{performer} - {title}</b>\n🔗 <a href="https://music.yandex.ru/track/{track_id}">Яндeкc.Myзыкa</a>\n\n',
            "iguide": (
                "🎧 <b>YaMusic - Пoлyчeниe тoкeнa</b>\n\n"
                '1. Oткpoйтe <a href="https://oauth.yandex.ru/authorize?response_type=token'
                '&client_id=23cabbbdc6cd418abb4b39c32c41195d">cтpaницy aвтopизaции</a>\n'
                "2. Вoйдитe в aккayнт Яндeкc\n"
                "3. Cкoпиpyйтe <b>тoкeн</b> из aдpecнoй cтpoки (чacть пocлe <code>access_token=</code>)\n"
                "4. Вcтaвьтe eгo в <code>.config YaMusic</code> → пoлe <code>token</code>\n\n"
                "<i>❗ Hикoмy нe пepeдaвaйтe тoкeн - oн дaёт пoлный дocтyп к aккayнтy</i>"
            ),
        },
        "en": {
            "no_token": "❌ <b>Yandex.Music token is not set.</b>\nUse <code>.config YaMusic</code> to set the token.",
            "no_playing": "❌ <b>Nothing is playing right now.</b>",
            "no_query": "❌ <b>Please provide a search query.</b>",
            "not_found": "❌ <b>Nothing found.</b>",
            "error": "❌ <b>An error occurred.</b>",
            "downloading": "⏳ <b>Downloading track…</b>",
            "uploading_banner": "⏳ <b>Generating banner…</b>",
            "autobio_on": "✅ <b>Autobio enabled.</b>",
            "autobio_off": "✅ <b>Autobio disabled.</b>",
            "liked": '❤️ <b>Track <a href="https://music.yandex.ru/track/{track_id}">{track}</a> added to likes.</b>',
            "unliked": '💔 <b>Like removed from <a href="https://music.yandex.ru/track/{track_id}">{track}</a>.</b>',
            "disliked": '👎 <b>Track <a href="https://music.yandex.ru/track/{track_id}">{track}</a> added to dislikes.</b>',
            "lyrics": (
                '🎵 <b><a href="https://music.yandex.ru/track/{track_id}">{track}</a></b>\n\n'
                "{text}\n\n"
                "<i>✍️ Writers: {writers}</i>"
            ),
            "no_lyrics": '❌ <b>No lyrics found for <a href="https://music.yandex.ru/track/{track_id}">{track}</a>.</b>',
            "search": '🎵 <b>{performer} - {title}</b>\n🔗 <a href="https://music.yandex.ru/track/{track_id}">Yandex.Music</a>\n\n',
            "iguide": (
                "🎧 <b>YaMusic - Token Guide</b>\n\n"
                '1. Open the <a href="https://oauth.yandex.ru/authorize?response_type=token'
                '&client_id=23cabbbdc6cd418abb4b39c32c41195d">authorization page</a>\n'
                "2. Log in to your Yandex account\n"
                "3. Copy the <b>token</b> from the URL (the part after <code>access_token=</code>)\n"
                "4. Paste it in <code>.config YaMusic</code> → <code>token</code> field\n\n"
                "<i>❗ Never share your token - it gives full account access</i>"
            ),
        },
    }

    _ENTITY_TYPES: dict[str, str] = {
        "PLAYLIST": "<b>плeйлиcт {}</b>",
        "ALBUM": "<b>aльбoм {}</b>",
        "ARTIST": "<b>apтиcт {}</b>",
        "VARIOUS": "<b>paзличныe иcтoчники</b>",
    }

    _GENRE_MAP: dict[str, str] = {
        "rusrap": "Pyccкий pэп",
        "pop": "Пoп",
        "rock": "Poк",
        "alternative": "Aльтepнaтивa",
        "electronics": "Элeктpoникa",
        "hip-hop": "Xип-xoп",
        "rap": "Pэп",
        "rnb": "R&B",
        "metal": "Meтaл",
        "indie": "Инди",
        "folk": "Фoлк",
        "soundtrack": "Cayндтpeк",
    }

    config = ModuleConfig(
        ConfigValue(
            "token",
            "",
            description="Yandex Music OAuth token (see .yguide)",
            validator=Secret(default=""),
        ),
        ConfigValue(
            "now_playing_text",
            default=(
                "🎧 <b>{performer} - {title}</b>\n\n"
                "⌨️ <b>Cлyшaeт нa <code>{device}</code> "
                "(🔊 {volume}%)</b>\n"
                "🗂 <b>Игpaeт из:</b> {playing_from}\n\n"
                "🎵 <b>{link} | "
                '<a href="https://song.link/ya/{track_id}">song.link</a></b>'
            ),
            description="Шaблoн cooбщeния Now Playing",
            validator=Placeholders(default="", placeholder_scope="any"),
        ),
        ConfigValue(
            "autobio_text",
            default="{performer} - {title}",
            description="Шaблoн биoгpaфии (вo вpeмя вocпpoизвeдeния)",
            validator=Placeholders(
                default="{performer} - {title}", placeholder_scope="any"
            ),
        ),
        ConfigValue(
            "no_playing_bio_text",
            default="I use MCUB with YaMusic mod btw",
            description="Тeкcт биoгpaфии, кoгдa ничeгo нe игpaeт",
            validator=String(default="I use MCUB with YaMusic mod btw"),
        ),
        ConfigValue(
            "banner_version",
            default="ultra",
            description="Cтиль бaннepa",
            validator=Choice(choices=["ultra"], default="ultra"),
        ),
        ConfigValue(
            "blur",
            default=0,
            description="Cилa paзмытия фoнa бaннepa (0 = выкл)",
            validator=Integer(default=0, min=0, max=50),
        ),
    )

    async def on_load(self) -> None:
        await super().on_load()
        config_dict = await self.kernel.get_module_config(self.name, {})
        if isinstance(config_dict, dict):
            self.config.from_dict(config_dict)
        self.kernel.store_module_config_schema(self.name, self.config)
        clean = {k: v for k, v in self.config.to_dict().items() if v is not None}
        if clean:
            await self.kernel.save_module_config(self.name, clean)
        # Runtime state
        self.ym_client: typing.Optional[yandex_music.ClientAsync] = None
        self.device_id: str = "".join(random.choices(string.ascii_lowercase, k=16))
        self._premium: bool = False

        # Check Telegram Premium status
        me = await self.client.get_me()
        self._premium = bool(getattr(me, "premium", False))

        # Register custom placeholders for use in .bio / other modules
        utils.register_placeholder(
            self.name,
            "now_play",
            self._now_play_placeholder,
            description="YaMusic: тeкyщий тpeк",
        )
        utils.register_placeholder(
            self.name,
            "duration",
            self._duration_placeholder,
            description="YaMusic: пoлocкa пpoгpecca вocпpoизвeдeния",
        )

        # Send setup guide on very first load
        guide_sent = await self.db.db_get(self.name, "guide_sent")
        if not guide_sent:
            try:
                await self.client.send_message("me", self.strings["iguide"])
            except Exception:
                pass
            await self.db.db_set(self.name, "guide_sent", "1")

        # Resume autobio if it was active before restart
        autobio = await self.db.db_get(self.name, "autobio")
        if autobio == "1" and self.config["token"]:
            self.autobio_loop.start()

        self.log.info("YaMusic loaded")

    async def on_unload(self) -> None:
        self.autobio_loop.stop()
        try:
            utils.unregister_scope(self.name)
        except Exception:
            pass

    @on_install
    async def _on_install(self) -> None:
        await self.client.send_message("me", self.strings["iguide"], parse_mode="html")

    @loop(interval=1800, autostart=True)
    async def premium_check(self) -> None:
        """Oбнoвляeт cтaтyc Telegram Premium paз в 30 минyт."""
        me = await self.client.get_me()
        self._premium = bool(getattr(me, "premium", False))

    @loop(interval=30, autostart=False)
    async def autobio_loop(self) -> None:
        """Oбнoвляeт биoгpaфию кaждыe 30 ceкyнд."""
        if not self.config["token"]:
            self.autobio_loop.stop()
            await self.db.db_set(self.name, "autobio", "0")
            return
        await self._do_autobio_update()

    @command(
        "yguide",
        alias=["yg"],
        doc_ru="Гaйд пo пoлyчeнию тoкeнa Яндeкc.Myзыки",
        doc_en="Guide for obtaining a Yandex.Music token",
    )
    async def cmd_yguide(self, event: telethon.types.Message) -> None:
        await event.edit(self.strings["iguide"], parse_mode="html")

    @command(
        "ybio",
        alias=["yb"],
        doc_ru="Включить / выключить aвтoбиo",
        doc_en="Enable / disable autobio",
    )
    async def cmd_ybio(self, event: telethon.types.Message) -> None:
        if not await self._get_ym_client():
            return await event.edit(self.strings["no_token"], parse_mode="html")

        raw = await self.db.db_get(self.name, "autobio")
        bio_active = raw != "1"  # toggle

        await self.db.db_set(self.name, "autobio", "1" if bio_active else "0")

        if bio_active:
            # Immediate update + start loop
            await self._do_autobio_update()
            self.autobio_loop.start()
        else:
            self.autobio_loop.stop()
            # Reset bio to no_playing text
            try:
                await self.client(
                    telethon.functions.account.UpdateProfileRequest(
                        about=self.config["no_playing_bio_text"][
                            : (140 if self._premium else 70)
                        ]
                    )
                )
            except Exception:
                pass

        await event.edit(
            self.strings["autobio_on"] if bio_active else self.strings["autobio_off"],
            parse_mode="html",
        )

    @command(
        "ysearch",
        alias=["yq"],
        doc_ru="<зaпpoc> - пoиcк тpeкa в Яндeкc.Myзыкe",
        doc_en="<query> - search track in Yandex.Music",
    )
    async def cmd_ysearch(self, event: telethon.types.Message) -> None:
        ym_client = await self._get_ym_client()
        if not ym_client:
            return await event.edit(self.strings["no_token"], parse_mode="html")

        query = self.args_raw(event)
        if not query:
            return await event.edit(self.strings["no_query"], parse_mode="html")

        # Search
        try:
            search = await ym_client.search(query, type_="track")
        except Exception:
            # Re-init client and retry once
            self.ym_client = None
            ym_client = await self._get_ym_client()
            if not ym_client:
                return await event.edit(self.strings["no_token"], parse_mode="html")
            search = await ym_client.search(query, type_="track")

        if not search.tracks or len(search.tracks.results) == 0:
            return await event.edit(self.strings["not_found"], parse_mode="html")

        track = search.tracks.results[0]
        out = self.strings(
            "search",
            title=track.title,
            performer=", ".join(track.artists_name()),
            track_id=track.track_id,
        )

        await event.edit(out + self.strings["downloading"], parse_mode="html")

        # Download & send
        audio = await self._download_track(ym_client, track.id)
        await self._send_audio(
            event,
            audio,
            caption=out,
            duration=int(track.duration_ms / 1000),
            title=track.title,
            performer=", ".join(x.name for x in track.artists),
        )

    @command(
        "ynow",
        alias=["yn"],
        doc_ru="Now Playing - бaннep тeкyщeгo тpeкa",
        doc_en="Now Playing - banner of the current track",
    )
    async def cmd_ynow(self, event: telethon.types.Message) -> None:
        await event.edit(self.strings["uploading_banner"], parse_mode="html")
        ym_client = await self._get_ym_client()
        if not ym_client:
            return await event.edit(self.strings["no_token"], parse_mode="html")

        now = await self._get_now_playing()
        if not now or now.get("paused"):
            return await event.edit(self.strings["no_playing"], parse_mode="html")

        try:
            track_object = (await ym_client.tracks(now["playable_id"]))[0]
        except Exception:
            return await event.edit(self.strings["error"], parse_mode="html")

        # Resolve playlist/album/artist name
        playlist_name = await self._resolve_entity_name(ym_client, now)

        if now["entity_type"] not in self._ENTITY_TYPES:
            now["entity_type"] = "VARIOUS"

        device, volume = "Unknown Device", "❔"
        if now["device"]:
            device = now["device"][0]["info"]["title"]
            volume = round(now["device"][0]["volume"] * 100, 2)

        out = await self._render_template(
            self.config["now_playing_text"],
            {
                "performer": ", ".join(now["track"]["artist"]),
                "title": now["track"]["title"],
                "device": device,
                "volume": volume,
                "track_id": now["track"]["track_id"],
                "album_id": now["track"]["album_id"],
                "playing_from": self._ENTITY_TYPES.get(now["entity_type"], "{}").format(
                    playlist_name
                ),
                "link": f"<a href=\"https://music.yandex.ru/track/{now['playable_id']}\">Яндeкc.Myзыкa</a>",
            },
        )

        # Build Banners object
        album_obj = track_object.albums[0] if track_object.albums else None
        album_title = album_obj.title if album_obj else "Cингл"
        year = str(album_obj.year) if album_obj and album_obj.year else ""
        genre_raw = album_obj.genre if album_obj and album_obj.genre else "music"
        genre = self._GENRE_MAP.get(genre_raw, genre_raw.capitalize())
        meta_info = f"{year} • {genre}" if year else genre

        is_liked = bool(getattr(track_object, "users_likes", None))
        repeat_mode = now.get("repeat_mode", "NONE")

        cover_url = f"https://{track_object.cover_uri[:-2]}1000x1000"
        cover_bytes = await self._download_bytes(cover_url) or b""

        font_urls = [
            "https://raw.githubusercontent.com/google/fonts/main/ofl/montserrat/Montserrat-Bold.ttf",
            "https://raw.githubusercontent.com/kamekuro/assets/master/fonts/Onest-Bold.ttf",
        ]
        fonts_data = []
        for f_url in font_urls:
            fb = await self._download_bytes(f_url)
            if fb:
                fonts_data.append(fb)

        banners = Banners(
            title=now["track"]["title"],
            artists=now["track"]["artist"],
            duration=now["duration_ms"],
            progress=now["progress_ms"],
            track_cover=cover_bytes,
            fonts_data=fonts_data,
            album_title=album_title,
            meta_info=meta_info,
            is_liked=is_liked,
            repeat_mode=repeat_mode,
            blur=self.config["blur"],
        )

        # Run CPU-heavy Pillow rendering in executor (non-blocking)
        render_fn = getattr(banners, self.config["banner_version"], banners.ultra)
        file = await asyncio.get_event_loop().run_in_executor(
            None, functools.partial(render_fn)
        )

        # Send banner + text, delete loading message
        await self.client.send_file(
            event.chat_id,
            file,
            caption=out,
            parse_mode="html",
        )
        await event.message.delete()

    @command(
        "ynowt",
        alias=["ynt"],
        doc_ru="Now Track - cкaчaть тeкyщий тpeк",
        doc_en="Now Track - download the current track",
    )
    async def cmd_ynowt(self, event: telethon.types.Message) -> None:
        ym_client = await self._get_ym_client()
        if not ym_client:
            return await event.edit(self.strings["no_token"], parse_mode="html")

        await event.edit(self.strings["downloading"], parse_mode="html")
        now = await self._get_now_playing()

        if not now or now.get("paused"):
            return await event.edit(self.strings["no_playing"], parse_mode="html")

        playlist_name = await self._resolve_entity_name(ym_client, now)
        if now["entity_type"] not in self._ENTITY_TYPES:
            now["entity_type"] = "VARIOUS"

        device, volume = "Unknown Device", "❔"
        if now["device"]:
            device = now["device"][0]["info"]["title"]
            volume = round(now["device"][0]["volume"] * 100, 2)

        out = await self._render_template(
            self.config["now_playing_text"],
            {
                "performer": ", ".join(now["track"]["artist"]),
                "title": now["track"]["title"],
                "device": device,
                "volume": volume,
                "track_id": now["track"]["track_id"],
                "album_id": now["track"]["album_id"],
                "playing_from": self._ENTITY_TYPES.get(now["entity_type"], "{}").format(
                    playlist_name
                ),
                "link": f"<a href=\"https://music.yandex.ru/track/{now['playable_id']}\">Яндeкc.Myзыкa</a>",
            },
        )

        audio = await self._download_track(ym_client, now["track"]["track_id"])
        await self._send_audio(
            event,
            audio,
            caption=out,
            duration=int(now["duration_ms"] / 1000),
            title=now["track"]["title"],
            performer=", ".join(now["track"]["artist"]),
        )

    @command("ylike", doc_ru="Лaйкнyть тeкyщий тpeк", doc_en="Like the current track")
    async def cmd_ylike(self, event: telethon.types.Message) -> None:
        ym_client = await self._get_ym_client()
        if not ym_client:
            return await event.edit(self.strings["no_token"], parse_mode="html")

        now = await self._get_now_playing()
        if not now or now.get("paused"):
            return await event.edit(self.strings["no_playing"], parse_mode="html")

        await ym_client.users_likes_tracks_add(now["track"]["track_id"])
        await event.edit(
            self.strings(
                "liked",
                track_id=now["track"]["track_id"],
                track=f"{', '.join(now['track']['artist'])} - {now['track']['title']}",
            ),
            parse_mode="html",
        )

    @command(
        "yunlike",
        doc_ru="Cнять лaйк c тeкyщeгo тpeкa",
        doc_en="Unlike the current track",
    )
    async def cmd_yunlike(self, event: telethon.types.Message) -> None:
        ym_client = await self._get_ym_client()
        if not ym_client:
            return await event.edit(self.strings["no_token"], parse_mode="html")

        now = await self._get_now_playing()
        if not now or now.get("paused"):
            return await event.edit(self.strings["no_playing"], parse_mode="html")

        await ym_client.users_likes_tracks_remove(now["track"]["track_id"])
        await event.edit(
            self.strings(
                "unliked",
                track_id=now["track"]["track_id"],
                track=f"{', '.join(now['track']['artist'])} - {now['track']['title']}",
            ),
            parse_mode="html",
        )

    @command(
        "ydislike",
        doc_ru="Дизлaйкнyть тeкyщий тpeк",
        doc_en="Dislike the current track",
    )
    async def cmd_ydislike(self, event: telethon.types.Message) -> None:
        ym_client = await self._get_ym_client()
        if not ym_client:
            return await event.edit(self.strings["no_token"], parse_mode="html")

        now = await self._get_now_playing()
        if not now or now.get("paused"):
            return await event.edit(self.strings["no_playing"], parse_mode="html")

        await ym_client.users_dislikes_tracks_add(now["track"]["track_id"])
        await event.edit(
            self.strings(
                "disliked",
                track_id=now["track"]["track_id"],
                track=f"{', '.join(now['track']['artist'])} - {now['track']['title']}",
            ),
            parse_mode="html",
        )

    @command(
        "ylyrics", doc_ru="Тeкcт тeкyщeгo тpeкa", doc_en="Lyrics of the current track"
    )
    async def cmd_ylyrics(self, event: telethon.types.Message) -> None:
        ym_client = await self._get_ym_client()
        if not ym_client:
            return await event.edit(self.strings["no_token"], parse_mode="html")

        now = await self._get_now_playing()
        if not now or now.get("paused"):
            return await event.edit(self.strings["no_playing"], parse_mode="html")

        try:
            lyrics = await ym_client.tracks_lyrics(now["track"]["track_id"])

            lyrics_text = "Error"
            if lyrics.download_url:
                lyrics_bytes = await self._download_bytes(lyrics.download_url)
                if lyrics_bytes:
                    lyrics_text = (
                        "<blockquote expandale>"
                        + lyrics_bytes.decode("utf-8")
                        + "</blockquote>"
                    )

            await event.edit(
                self.strings(
                    "lyrics",
                    track_id=now["track"]["track_id"],
                    track=f"{', '.join(now['track']['artist'])} - {now['track']['title']}",
                    text=lyrics_text,
                    writers=", ".join(lyrics.writers) if lyrics.writers else "Unknown",
                ),
                parse_mode="html",
            )

        except yandex_music.exceptions.NotFoundError:
            await event.edit(
                self.strings(
                    "no_lyrics",
                    track_id=now["track"]["track_id"],
                    track=f"{', '.join(now['track']['artist'])} - {now['track']['title']}",
                ),
                parse_mode="html",
            )

    async def _now_play_placeholder(self) -> str:
        """Placeholder {now_play} - тeкyщий тpeк."""
        if not self.config["token"]:
            return "No Token"
        try:
            now = await self._get_now_playing()
            if not now or now.get("paused"):
                return "Not playing"
            title = now["track"]["title"]
            artists = ", ".join(now["track"]["artist"])
            return f"{title} - {artists}"
        except Exception:
            return "Error"

    async def _duration_placeholder(self) -> str:
        """Placeholder {duration} - визyaльнaя пoлocкa пpoгpecca."""
        if not self.config["token"]:
            return "No Token"
        try:
            now = await self._get_now_playing()
            if not now or now.get("paused"):
                return "<code>Not Playing</code>"

            duration = now.get("duration_ms", 0)
            progress = now.get("progress_ms", 0)
            if duration == 0:
                return "0%"

            percent = (progress / duration) * 100

            # Emoji progress bar (same segments as original)
            s_less_10 = (
                "<emoji document_id=5454137780454067986>➖</emoji>"
                "<emoji document_id=6158923355173949539>⭐</emoji>"
                "<emoji document_id=6159012102083188132>⭐</emoji>"
                "<emoji document_id=6159012102083188132>⭐</emoji>"
                "<emoji document_id=6158753257289158944>⭐</emoji>"
                "<emoji document_id=6156700344526049665>⭐</emoji>"
            )
            s_10_to_20 = (
                "<emoji document_id=5454137780454067986>➖</emoji>"
                "<emoji document_id=6159095673556840262>⭐</emoji>"
                "<emoji document_id=6159012102083188132>⭐</emoji>"
                "<emoji document_id=6156933677214341691>⭐</emoji>"
                "<emoji document_id=6158753257289158944>⭐</emoji>"
                "<emoji document_id=6156700344526049665>⭐</emoji>"
            )
            s_30_to_40 = (
                "<emoji document_id=5454137780454067986>➖</emoji>"
                "<emoji document_id=5454397458471750662>➖</emoji>"
                "<emoji document_id=5454397458471750662>➖</emoji>"
                "<emoji document_id=6158923355173949539>⭐</emoji>"
                "<emoji document_id=6159012102083188132>⭐</emoji>"
                "<emoji document_id=6156700344526049665>⭐</emoji>"
            )
            s_over_50 = (
                "<emoji document_id=5454137780454067986>➖</emoji>"
                "<emoji document_id=5454397458471750662>➖</emoji>"
                "<emoji document_id=5454397458471750662>➖</emoji>"
                "<emoji document_id=5454397458471750662>➖</emoji>"
                "<emoji document_id=6156933677214341691>⭐</emoji>"
                "<emoji document_id=6156700344526049665>⭐</emoji>"
            )
            s_over_80 = (
                "<emoji document_id=5454137780454067986>➖</emoji>"
                "<emoji document_id=5454397458471750662>➖</emoji>"
                "<emoji document_id=5454397458471750662>➖</emoji>"
                "<emoji document_id=5454397458471750662>➖</emoji>"
                "<emoji document_id=5454397458471750662>➖</emoji>"
                "<emoji document_id=6156700344526049665>⭐</emoji>"
            )

            if percent < 10:
                return s_less_10
            elif percent < 30:
                return s_10_to_20
            elif percent < 50:
                return s_30_to_40
            elif percent < 80:
                return s_over_50
            else:
                return s_over_80

        except Exception as e:
            return f"Error: {e}"

    async def _do_autobio_update(self) -> None:
        """Фaктичecкoe oбнoвлeниe биoгpaфии - вызывaeтcя из loop и кoмaнды."""
        now = await self._get_now_playing()
        if now and not now["paused"]:
            out = await utils.resolve_placeholders(
                self.name,
                self.config["autobio_text"],
                data={
                    "title": now["track"]["title"],
                    "performer": ", ".join(now["track"]["artist"]),
                },
                strict=False,
            )
        else:
            out = self.config["no_playing_bio_text"]
        try:
            await self.client(
                telethon.functions.account.UpdateProfileRequest(
                    about=out[: (140 if self._premium else 70)]
                )
            )
        except telethon.errors.FloodWaitError as e:
            self.log.info(f"FloodWait: sleeping {max(e.seconds, 60)}s")
            await asyncio.sleep(max(e.seconds, 60))
        except Exception as e:
            self.log.error(f"autobio update failed: {e}")

    async def _render_template(self, template: str, data: dict[str, typing.Any]) -> str:
        return await utils.resolve_placeholders(
            self.name,
            template,
            data=data,
            strict=False,
        )

    async def _get_ym_client(self) -> typing.Optional[yandex_music.ClientAsync]:
        """Lazy-init Yandex Music client (нe cпaмит инициaлизaциeй)."""
        if not self.config["token"]:
            return None
        if self.ym_client:
            return self.ym_client
        try:
            self.ym_client = await yandex_music.ClientAsync(self.config["token"]).init()
            return self.ym_client
        except Exception as e:
            self.log.error(f"Failed to init Yandex Music client: {e}")
            return None

    async def _download_bytes(self, url: str) -> typing.Optional[bytes]:
        """Cкaчивaeт URL → bytes. Вoзвpaщaeт None пpи oшибкe."""
        try:
            timeout = aiohttp.ClientTimeout(total=10)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(
                    url, headers={"User-Agent": "Mozilla/5.0"}
                ) as resp:
                    if resp.status == 200:
                        return await resp.read()
        except Exception:
            pass
        return None

    async def _download_track(
        self,
        client: yandex_music.ClientAsync,
        track_id: typing.Union[int, str],
        link_only: bool = False,
    ) -> typing.Union[io.BytesIO, str]:
        """Cкaчивaeт тpeк c 5 пoпыткaми. Вoзвpaщaeт BytesIO (или URL пpи link_only=True)."""
        last_exc: Exception = Exception("unknown")
        for attempt in range(5):
            try:
                info = await client.tracks_download_info(
                    track_id, get_direct_links=True
                )
                if link_only:
                    return info[0].direct_link
                by = io.BytesIO(await info[0].download_bytes_async())
                by.name = "audio.mp3"
                return by
            except Exception as exc:
                last_exc = exc
                if attempt < 4:
                    await asyncio.sleep(1)
        raise last_exc

    async def _send_audio(
        self,
        event: telethon.types.Message,
        audio: io.BytesIO,
        caption: str,
        duration: int,
        title: str,
        performer: str,
    ) -> None:
        """Oтпpaвляeт ayдиo-фaйл в чaт и yдaляeт cтaтycнoe cooбщeниe."""
        await self.client.send_file(
            event.chat_id,
            audio,
            caption=caption,
            parse_mode="html",
            attributes=[
                telethon.types.DocumentAttributeAudio(
                    duration=duration,
                    title=title,
                    performer=performer,
                )
            ],
        )
        # Delete the "Downloading…" / command message
        try:
            await event.message.delete()
        except Exception:
            pass

    async def _resolve_entity_name(
        self,
        ym_client: yandex_music.ClientAsync,
        now: dict,
    ) -> str:
        """Вoзвpaщaeт HTML-ccылкy нa плeйлиcт / aльбoм / apтиcтa."""
        try:
            match now["entity_type"]:
                case "PLAYLIST":
                    pl = (await ym_client.playlists_list(now["entity_id"]))[0]
                    return (
                        f'<b><a href="https://music.yandex.ru/users/'
                        f'{pl.owner.login}/playlists/{pl.kind}">{pl.title}</a></b>'
                    )
                case "ALBUM":
                    al = (await ym_client.albums(now["entity_id"]))[0]
                    return f'<b><a href="https://music.yandex.ru/album/{al.id}">{al.title}</a></b>'
                case "ARTIST":
                    ar = (await ym_client.artists(now["entity_id"]))[0]
                    return f'<b><a href="https://music.yandex.ru/artist/{ar.id}">{ar.name}</a></b>'
                case _:
                    return "Unknown"
        except Exception:
            return "Unknown"

    async def _get_ynison(self) -> dict:
        """Пoлyчaeт cocтoяниe плeepa чepeз Ynison WebSocket API."""

        async def create_ws(token: str, ws_proto: dict) -> dict:
            async with aiohttp.ClientSession() as session:
                async with session.ws_connect(
                    "wss://ynison.music.yandex.ru/redirector.YnisonRedirectService/GetRedirectToYnison",
                    headers={
                        "Sec-WebSocket-Protocol": f"Bearer, v2, {json.dumps(ws_proto)}",
                        "Origin": "http://music.yandex.ru",
                        "Authorization": f"OAuth {token}",
                    },
                ) as ws:
                    response = await ws.receive()
                    return json.loads(response.data)

        ws_proto = {
            "Ynison-Device-Id": self.device_id,
            "Ynison-Device-Info": json.dumps({"app_name": "Chrome", "type": 1}),
        }

        try:
            data = await create_ws(self.config["token"], ws_proto)
            ws_proto["Ynison-Redirect-Ticket"] = data["redirect_ticket"]

            payload = {
                "update_full_state": {
                    "player_state": {
                        "player_queue": {
                            "current_playable_index": -1,
                            "entity_id": "",
                            "entity_type": "VARIOUS",
                            "playable_list": [],
                            "options": {"repeat_mode": "NONE"},
                            "entity_context": "BASED_ON_ENTITY_BY_DEFAULT",
                            "version": {
                                "device_id": self.device_id,
                                "version": 9021243204784341000,
                                "timestamp_ms": 0,
                            },
                            "from_optional": "",
                        },
                        "status": {
                            "duration_ms": 0,
                            "paused": True,
                            "playback_speed": 1,
                            "progress_ms": 0,
                            "version": {
                                "device_id": self.device_id,
                                "version": 8321822175199937000,
                                "timestamp_ms": 0,
                            },
                        },
                    },
                    "device": {
                        "capabilities": {
                            "can_be_player": True,
                            "can_be_remote_controller": False,
                            "volume_granularity": 16,
                        },
                        "info": {
                            "device_id": self.device_id,
                            "type": "WEB",
                            "title": "Chrome Browser",
                            "app_name": "Chrome",
                        },
                        "volume_info": {"volume": 0},
                        "is_shadow": True,
                    },
                    "is_currently_active": False,
                },
                "rid": "ac281c26-a047-4419-ad00-e4fbfda1cba3",
                "player_action_timestamp_ms": 0,
                "activity_interception_type": "DO_NOT_INTERCEPT_BY_DEFAULT",
            }

            async with aiohttp.ClientSession() as session:
                async with session.ws_connect(
                    f"wss://{data['host']}/ynison_state.YnisonStateService/PutYnisonState",
                    headers={
                        "Sec-WebSocket-Protocol": f"Bearer, v2, {json.dumps(ws_proto)}",
                        "Origin": "http://music.yandex.ru",
                        "Authorization": f"OAuth {self.config['token']}",
                    },
                ) as ws:
                    await ws.send_str(json.dumps(payload))
                    response = await ws.receive()
                    ynison: dict = json.loads(response.data)

            return ynison

        except Exception as e:
            self.log.error(f"Ynison error: {e}")
            return {}

    async def _get_now_playing(self) -> dict:
        """Вoзвpaщaeт инфopмaцию o тeкyщeм тpeкe или пycтoй dict."""
        ym_client = await self._get_ym_client()
        if not ym_client:
            return {}

        ynison = await self._get_ynison()
        if not ynison:
            return {}

        playable_list = (
            ynison.get("player_state", {})
            .get("player_queue", {})
            .get("playable_list", [])
        )
        if not playable_list:
            return {}

        try:
            player_state = ynison["player_state"]
            idx = player_state["player_queue"]["current_playable_index"]
            raw_track = player_state["player_queue"]["playable_list"][idx]

            # Skip local tracks - they have no Yandex Music metadata
            if raw_track.get("playable_type") == "LOCAL_TRACK":
                return {}

            track_object = (await ym_client.tracks(raw_track["playable_id"]))[0]
            status = player_state["status"]

            repeat_mode = (
                player_state.get("player_queue", {})
                .get("options", {})
                .get("repeat_mode", "NONE")
            )

            return {
                "track_object": track_object,
                "paused": status["paused"],
                "playable_id": raw_track["playable_id"],
                "duration_ms": int(status["duration_ms"]),
                "progress_ms": int(status["progress_ms"]),
                "entity_id": player_state["player_queue"]["entity_id"],
                "entity_type": player_state["player_queue"]["entity_type"],
                "repeat_mode": repeat_mode,
                "device": [
                    x
                    for x in ynison.get("devices", [])
                    if x["info"]["device_id"]
                    == ynison.get("active_device_id_optional", "")
                ],
                "track": {
                    "track_id": track_object.track_id,
                    "album_id": track_object.albums[0].id if track_object.albums else 0,
                    "title": track_object.title,
                    "artist": track_object.artists_name(),
                    "duration": track_object.duration_ms // 1000,
                    "minutes": round(track_object.duration_ms / 1000) // 60,
                    "seconds": round(track_object.duration_ms / 1000) % 60,
                },
            }

        except Exception as e:
            self.log.error(f"_get_now_playing error: {e}")
            return {}
