from __future__ import annotations

import asyncio
import base64
import hashlib
import hmac
import json
import logging
import time
from contextlib import suppress
from typing import Any
from urllib.parse import quote, urljoin

import aiohttp
from telethon.tl.functions.contacts import UnblockRequest

# local
from ..Const import (
    API_BASE,
    AUTH_SECRET,
    BAN_REASON_RE,
    BAN_TERM_RE,
    JWT_RE,
    _esc,
)

LOG = logging.getLogger("VectorMonolith")


class VectorHttpDispatchMixin:
    _http: aiohttp.ClientSession | None = None
    _http_lock: Any = None  # filled in on_load
    _ban_check_done: bool = False
    bannote: str | None = None
    btid: int = 0
    httpc: int = 0

    async def on_load(self) -> None:
        LOG.info("Vector loaded")
        self._http_lock = asyncio.Lock()
        self._http = aiohttp.ClientSession(
            headers={"User-Agent": "Vector/MCUB/2.3.9"},
            timeout=aiohttp.ClientTimeout(total=30),
        )
        await super().on_load()
        asyncio.ensure_future(self._check_ban())

    async def on_unload(self) -> None:
        LOG.info("Vector unloading")
        if self._http and not self._http.closed:
            await self._http.close()

    async def _ensure_http(self) -> aiohttp.ClientSession:
        if self._http is None or self._http.closed:
            async with self._http_lock:
                if self._http is None or self._http.closed:
                    self._http = aiohttp.ClientSession(
                        headers={"User-Agent": "Vector/MCUB/2.3.9"},
                        timeout=aiohttp.ClientTimeout(total=30),
                    )
        return self._http

    async def _net_req(
        self,
        method: str,
        path: str,
        token: str | None = None,
        json_data: dict | None = None,
        params: dict | None = None,
        as_bytes: bool = False,
    ) -> Any:
        url = urljoin(API_BASE, path.lstrip("/"))
        headers: dict[str, str] = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        try:
            http = await self._ensure_http()
            async with http.request(
                method, url, headers=headers, json=json_data, params=params
            ) as resp:
                self.httpc = resp.status
                if resp.status == 204:
                    return {"ok": True}
                if resp.status >= 400:
                    LOG.warning("_net_req: HTTP %d for %s %s", resp.status, method, url)
                    return None
                if as_bytes:
                    return await resp.read()
                ct = resp.headers.get("Content-Type", "")
                if "application/json" in ct:
                    return await resp.json()
                text = await resp.text()
                try:
                    return json.loads(text)
                except (json.JSONDecodeError, ValueError):
                    return {"ok": True, "raw": text}
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            LOG.warning("_net_req: request failed: %r", e)
            return None

    async def _fetch_banner(self, url: str | None) -> bytes | None:
        if not url:
            return None
        try:
            http = await self._ensure_http()
            async with http.get(url) as resp:
                return await resp.read() if resp.status == 200 else None
        except Exception as e:
            LOG.debug("_fetch_banner: failed for %s: %r", url, e)
        return None

    async def _get_active_token(self, force: bool = False) -> str | None:
        LOG.debug("_get_active_token: force=%s", force)
        if force:
            await self.db.db_delete(self.name, "auth_token")
            LOG.debug("_get_active_token: auth_token cleared (force)")

        cached = await self.db.db_get(self.name, "auth_token")
        if cached:
            try:
                payload = self._parse_jwt(cached)
                if payload.get("exp", 0) - time.time() > 60:
                    LOG.debug(
                        "_get_active_token: cached token valid, exp=%s",
                        payload.get("exp"),
                    )
                    return cached
                LOG.debug("_get_active_token: cached token expired or expiring")
            except Exception:
                cached = None

        LOG.info("_get_active_token: requesting fresh token")
        bot_info = await self._net_req("GET", "/api/tg-bot")
        bot_username = (bot_info or {}).get("username", "").strip().lstrip("@")
        if not bot_username:
            LOG.warning("No bot username returned from /api/tg-bot")
            return None

        me = await self.client.get_me()
        uid = str(getattr(me, "id", ""))
        uname = getattr(me, "username", "") or ""
        fname = getattr(me, "first_name", "") or ""
        lname = getattr(me, "last_name", "") or ""
        dname = " ".join(filter(None, [fname, lname])).strip() or uname or uid

        uname = self._norm_hash_name(uname).lower()
        dname = self._norm_hash_name(dname)

        with suppress(Exception):
            await self.client(UnblockRequest(bot_username))

        new_jwt = ""
        ban_notice = ""
        for attempt in range(2):
            b_stamp = int(time.time() // 10) - attempt
            cmd_hash = hashlib.sha256(
                f"vector-token-v2|{uid}|{b_stamp}|{AUTH_SECRET}".encode()
            ).hexdigest()[:32]
            cmd_str = f"/{cmd_hash}"

            try:
                async with self.client.conversation(
                    bot_username, timeout=12, exclusive=False
                ) as conv:
                    out_msg = await conv.send_message(cmd_str)
                    try:
                        resp = await asyncio.wait_for(conv.get_response(), timeout=10)
                        txt = getattr(resp, "raw_text", getattr(resp, "text", ""))
                        match = JWT_RE.search(txt)
                        if match:
                            new_jwt = match.group(0)
                        elif "зaблoк" in txt.lower() or "\u26db" in txt:
                            ban_notice = self._format_ban_notice(txt)
                        with suppress(Exception):
                            await out_msg.delete()
                        if new_jwt:
                            break
                    except asyncio.TimeoutError:
                        with suppress(Exception):
                            await out_msg.delete()
            except Exception as e:
                LOG.warning("Token conversation attempt=%s failed: %r", attempt, e)

        if new_jwt:
            await self.db.db_set(self.name, "auth_token", new_jwt)
            self.bannote = None
            LOG.info("_get_active_token: new token obtained")
        elif ban_notice:
            self.bannote = ban_notice
            LOG.warning("_get_active_token: user banned")
        else:
            LOG.warning("_get_active_token: no token obtained")
        return new_jwt or None

    def _format_ban_notice(self, raw_text: str) -> str:
        LOG.debug("_format_ban_notice: raw_len=%d", len(raw_text) if raw_text else 0)
        txt = str(raw_text or "").strip()
        reason_match = BAN_REASON_RE.search(txt)
        term_match = BAN_TERM_RE.search(txt)

        reason_raw = reason_match.group(1).strip() if reason_match else ""
        term_raw = term_match.group(1).strip() if term_match else ""

        if not reason_raw or not term_raw:
            for line in txt.splitlines():
                if ":" not in line:
                    continue
                key, value = line.split(":", 1)
                key_l = key.strip().lower()
                val = value.strip()
                if not reason_raw and key_l in {
                    "пpичинa",
                    "reason",
                    "理由",
                    "grund",
                    "r3450n",
                    "weason",
                    "charge",
                }:
                    reason_raw = val
                if not term_raw and key_l in {
                    "cpoк",
                    "term",
                    "期間",
                    "dauer",
                    "73rm",
                    "tewm",
                }:
                    term_raw = val

        reason = _esc(reason_raw or "-")
        term = _esc(term_raw or "permanent")
        return self.strings("v_ban_notice", reason=reason, term=term)

    def _compute_hmac(self, payload: str) -> str:
        return hmac.new(
            AUTH_SECRET.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256
        ).hexdigest()

    def _verify_hmac(self, payload: str, signature: str) -> bool:
        return hmac.compare_digest(self._compute_hmac(payload), signature)

    def _parse_jwt(self, token: str) -> dict:
        try:
            b64_part = token.split(".")[1]
            b64_part += "=" * (-len(b64_part) % 4)
            return json.loads(base64.urlsafe_b64decode(b64_part.encode()).decode())
        except Exception:
            return {}

    async def _check_ban(self) -> None:
        if self._ban_check_done:
            return
        self._ban_check_done = True
        token = await self._get_active_token()
        if not token:
            return
        res = await self._net_req("GET", "/api/status", token=token)
        if res is None:
            return
        ban = res.get("ban") or res.get("banned") or res.get("is_banned")
        if ban:
            reason = ban.get("reason") or ""
            until = ban.get("until") or ""
            self.bannote = (
                f"\U0001f6ab Banned: {reason}" if reason else "\U0001f6ab Banned"
            )
            if until:
                self.bannote += f" until {until}"
            LOG.warning("_check_ban: %s", self.bannote)

    async def _search_modules(
        self, query: str, limit: int = 30, lang: str = "en"
    ) -> list[dict[str, Any]]:
        token = await self._get_active_token()
        params = {"q": query, "limit": str(limit), "lang": lang}
        res = await self._net_req("GET", "/api/search", token=token, params=params)
        if self.httpc == 401:
            LOG.info("_search_modules: got 401, forcing token refresh")
            token = await self._get_active_token()
            if token:
                res = await self._net_req(
                    "GET", "/api/search", token=token, params=params
                )
        if not res:
            return []
        raw_list = (
            res.get("results", [])
            if isinstance(res, dict)
            else (res if isinstance(res, list) else [])
        )
        return [self._normalize_module(m) for m in raw_list if isinstance(m, dict)]

    async def _get_discussion(self, owner: str, name: str) -> dict | None:
        token = await self._get_active_token()
        return await self._net_req(
            "GET",
            f"/api/discuss/{quote(owner, safe='')}/{quote(name, safe='')}",
            token=token,
        )

    async def _post_discussion(self, owner: str, name: str, text: str) -> bool:
        token = await self._get_active_token()
        if not token:
            return False
        res = await self._net_req(
            "POST",
            f"/api/discuss/{quote(owner, safe='')}/{quote(name, safe='')}",
            token=token,
            json_data={"text": text},
        )
        return bool(res and res.get("ok"))
