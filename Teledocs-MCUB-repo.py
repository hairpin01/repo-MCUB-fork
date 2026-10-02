# SPDX-License-Identifier: AGPL-3.0-or-later
# Ported from Hikari Teledocs for MCUB API only.
#
#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2022
#           https://t.me/hikariatama
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scop: kernel min v1.2.7

# May be working a lil bit weird, because info was manually
# parsed from telegram schema and official telethon search
# mechanism was used as a base for this search

# meta developer: @hikarimods

from __future__ import annotations

import html
import re

from typing import Any

import aiohttp
from telethon import events

from core.lib.loader.module_base import ModuleBase, command, inline

TL_DOCS_URL = "https://github.com/hikariatama/assets/raw/master/tl_docs.json"
TAG_RE = re.compile(r"<.*?>")


def _strip_tags(text: str) -> str:
    return TAG_RE.sub("", text or "")


def _html_escape(text: Any) -> str:
    return html.escape(str(text or ""), quote=False)


class Teledocs(ModuleBase):
    """Telethon docs in your pocket."""

    name = "Teledocs"
    version = "1.0.1"
    author = "@hikarimods; port @Hairpin00"
    description: dict[str, str] = {
        "ru": "Дoкyмeнтaция Telethon TL пoд pyкoй",
        "en": "Telethon TL docs in your pocket",
    }
    banner_url = "https://raw.githubusercontent.com/hairpin01/repo-MCUB-fork/main/assets/banner/teledocs-banner.png"

    strings = {
        "name": "Teledocs",
        "loading": "🍙 <b>Loading Telethon docs...</b>",
        "loaded": "🍙 <b>Telethon docs loaded:</b> <code>{count}</code>",
        "load_error": "🚫 <b>Failed to load Telethon docs:</b> <code>{error}</code>",
        "not_loaded": "🚫 <b>Telethon docs are not loaded yet.</b> Try again later.",
        "empty_query": "🍙 <b>Specify Telethon reference.</b>\n<i>Example:</i> <code>tl sendmessage</code>",
        "not_found": "🚫 <b>No Telethon docs found for:</b> <code>{query}</code>",
        "inline_empty": "Enter Telethon reference",
        "inline_loading": "Telethon docs are still loading",
        "inline_not_found": "No Telethon docs found",
    }

    _tl: dict[str, Any] = {}
    _load_error: str | None = None
    _loaded = False

    async def on_load(self) -> None:
        await self._load_docs()

    async def _load_docs(self) -> None:
        self._load_error = None
        self._loaded = False
        try:
            timeout = aiohttp.ClientTimeout(total=30)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(TL_DOCS_URL) as response:
                    response.raise_for_status()
                    self._tl = await response.json(content_type=None)
            self._loaded = True
            self.log.info("Telethon docs loaded: %s items", self._items_count())
        except Exception as e:
            self._tl = {}
            self._load_error = str(e)
            self.log.exception("Failed to load Telethon docs")

    def _items_count(self) -> int:
        return sum(
            len(self._tl.get(key, [])) for key in ("requests", "types", "constructors")
        )

    @staticmethod
    def _find(haystack: str, needle: str) -> int:
        if not needle or not haystack:
            return -1

        if needle in haystack:
            return 0

        haystack_index = 0
        needle_index = 0
        penalty = 0
        started = False

        while True:
            while needle_index < len(needle) and not (
                "a" <= needle[needle_index] <= "z"
            ):
                needle_index += 1
                if needle_index == len(needle):
                    return penalty

            if needle_index == len(needle):
                return penalty

            while haystack[haystack_index] != needle[needle_index]:
                haystack_index += 1
                if started:
                    penalty += 1

                if haystack_index == len(haystack):
                    return -1

            haystack_index += 1
            needle_index += 1
            started = True

            if needle_index == len(needle):
                return penalty

            if haystack_index == len(haystack):
                return -1

    def _get_search_array(
        self,
        original: list[str],
        original_urls: list[str],
        query: str,
    ) -> tuple[list[list[Any]], list[str]]:
        destination: list[list[Any]] = []
        destination_urls: list[str] = []

        for index, (item, item_url) in enumerate(
            zip(original, original_urls, strict=False)
        ):
            penalty = self._find(item.lower(), query)
            if -1 < penalty < len(item) / 3:
                destination.append([item, index])
                destination_urls.append(item_url)

        return destination, destination_urls

    def _build_list(
        self,
        found_elements: tuple[list[list[Any]], list[str]],
        requests: bool = False,
        constructors: bool = False,
    ) -> list[dict[str, Any]]:
        items, links = found_elements

        if requests or constructors:
            desc_key = "requests_desc" if requests else "constructors_desc"
            result: list[dict[str, Any]] = []
            for item, link in zip(items, links, strict=False):
                index = item[1]
                entry = {
                    "link": link,
                    "result": item[0],
                    "description": self._tl.get(desc_key, [["", ""]])[index],
                    "example": "",
                }
                if requests:
                    examples = self._tl.get("requests_ex", [])
                    entry["example"] = examples[index] if index < len(examples) else ""
                result.append(entry)
            return result

        return [
            {
                "link": link,
                "result": item[0],
                "description": ["", ""],
                "example": "",
            }
            for item, link in zip(items, links, strict=False)
        ]

    def search(self, query: str) -> list[dict[str, Any]]:
        query = query.strip().lower()
        if not query or not self._loaded:
            return []

        found_requests = self._get_search_array(
            self._tl.get("requests", []),
            self._tl.get("requests_urls", []),
            query,
        )
        found_types = self._get_search_array(
            self._tl.get("types", []),
            self._tl.get("types_urls", []),
            query,
        )
        found_constructors = self._get_search_array(
            self._tl.get("constructors", []),
            self._tl.get("constructors_urls", []),
            query,
        )

        exact: list[dict[str, Any]] = []
        requests = self._tl.get("requests", [])
        constructors = self._tl.get("constructors", [])
        request_urls = self._tl.get("requests_urls", [])
        constructor_urls = self._tl.get("constructors_urls", [])

        for index, item in enumerate(requests):
            if item.lower().replace("request", "") == query:
                exact.extend(
                    self._build_list(([[item, index]], [request_urls[index]]), True)
                )

        for index, item in enumerate(constructors):
            if item.lower() == query and index < len(constructor_urls):
                exact.extend(
                    self._build_list(
                        ([[item, index]], [constructor_urls[index]]), False, True
                    )
                )

        results = (
            exact
            + self._build_list(found_requests, True)
            + self._build_list(found_types)
            + self._build_list(found_constructors, False, True)
        )

        seen: set[tuple[str, str]] = set()
        unique: list[dict[str, Any]] = []
        for item in results:
            key = (str(item.get("result", "")), str(item.get("link", "")))
            if key not in seen:
                seen.add(key)
                unique.append(item)
        return unique

    def _get_message(self, item: dict[str, Any]) -> str:
        description = item.get("description") or ["", ""]
        first_description = description[0] if len(description) > 0 else ""
        params = description[1] if len(description) > 1 else ""
        example = item.get("example") or ""

        return (
            f'🔧 <a href="https://tl.telethon.dev/{_html_escape(item.get("link"))}">'
            f"{_html_escape(item.get('result'))}</a>\n\n"
            "🍙 <b>Parameters:</b>\n\n"
            f"ℹ️ <i>{_html_escape(_strip_tags(first_description))}</i>\n\n"
            f"{params}\n\n"
            "🦀 <b>Example:</b>\n\n"
            f"<pre>{_html_escape(example)}</pre>"
        )

    async def _answer(self, event: events.NewMessage.Event, text: str) -> None:
        await self.edit(event, text, parse_mode="html")

    @staticmethod
    def _inline_query_from_event(event: events.InlineQuery.Event) -> str:
        """Extract user query from MCUB inline event.

        MCUB routes inline handlers by the first word of ``event.text`` and passes
        the original event unchanged.  For @inline("tl") the text is usually
        ``"tl <request>"``; Hikka's ``query.args`` does not exist here.
        """
        raw_query = (
            getattr(event, "text", None) or getattr(event, "args", "") or ""
        ).strip()
        if not raw_query:
            return ""

        parts = raw_query.split(maxsplit=1)
        if parts and parts[0].lower() == "tl":
            return parts[1].strip() if len(parts) > 1 else ""
        return raw_query

    async def _ensure_loaded(self) -> bool:
        if self._loaded:
            return True
        await self._load_docs()
        return self._loaded

    async def _answer_direct_search(
        self, event: events.NewMessage.Event, query: str
    ) -> None:
        if not await self._ensure_loaded():
            await self._answer(
                event,
                self.strings["load_error"].format(
                    error=_html_escape(self._load_error or "unknown error")
                ),
            )
            return

        results = self.search(query)
        if not results:
            await self._answer(
                event, self.strings["not_found"].format(query=_html_escape(query))
            )
            return

        await self._answer(event, self._get_message(results[0]))

    @inline("tl")
    async def inline_tl(self, event: events.InlineQuery.Event) -> None:
        query = self._inline_query_from_event(event)

        if not query:
            await event.answer(
                [
                    event.builder.article(
                        title=self.strings["inline_empty"],
                        text=self.strings["empty_query"],
                        parse_mode="html",
                    )
                ]
            )
            return

        if not await self._ensure_loaded():
            text = self.strings["not_loaded"]
            if self._load_error:
                text = self.strings["load_error"].format(
                    error=_html_escape(self._load_error)
                )
            await event.answer(
                [
                    event.builder.article(
                        title=self.strings["inline_loading"],
                        text=text,
                        parse_mode="html",
                    )
                ]
            )
            return

        results = [
            item
            for item in self.search(query)
            if item.get("description") and item["description"][0]
        ]
        if not results:
            await event.answer(
                [
                    event.builder.article(
                        title=self.strings["inline_not_found"],
                        description=query,
                        text=self.strings["not_found"].format(
                            query=_html_escape(query)
                        ),
                        parse_mode="html",
                    )
                ]
            )
            return

        await event.answer(
            [
                event.builder.article(
                    title=item["result"],
                    description=_strip_tags(item.get("description", [""])[0]),
                    text=self._get_message(item),
                    parse_mode="html",
                )
                for item in results[:50]
            ]
        )

    @command(
        "tl",
        doc_ru="<ref> - нaйти cпpaвкy Telethon TL",
        doc_en="<ref> - find Telethon TL reference",
    )
    async def cmd_tl(self, event: events.NewMessage.Event) -> None:
        query = self.args_raw(event).strip()

        if not query:
            await self._answer(event, self.strings["empty_query"])
            return

        bot_username = (self.kernel.config.get("inline_bot_username") or "").strip()
        if bot_username:
            try:
                inline_results = await self.client.inline_query(
                    bot_username.lstrip("@"), f"tl {query}"
                )
                if inline_results:
                    await inline_results[0].click(
                        event.chat_id, reply_to=event.reply_to_msg_id
                    )
                    await event.delete()
                    return
            except Exception as e:
                self.log.debug("Failed to send Teledocs inline result: %s", e)

        await self._answer_direct_search(event, query)

    @command(
        "tlreload",
        doc_ru="пepeзaгpyзить индeкc Telethon TL",
        doc_en="reload Telethon TL docs index",
    )
    async def cmd_tlreload(self, event: events.NewMessage.Event) -> None:
        await self._answer(event, self.strings["loading"])
        await self._load_docs()
        if self._loaded:
            await self._answer(
                event,
                self.strings["loaded"].format(count=self._items_count()),
            )
            return

        await self._answer(
            event,
            self.strings["load_error"].format(
                error=_html_escape(self._load_error or "unknown error")
            ),
        )
