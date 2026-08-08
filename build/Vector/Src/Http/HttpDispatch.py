from __future__ import annotations

import asyncio
import base64
import hashlib
import hmac
import json
import logging
import socket
import struct
import time
from contextlib import suppress
from email.utils import parsedate_to_datetime
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
    HTTP_TIME_HOSTS,
    JWT_RE,
    NTP_EPOCH_DELTA,
    NTP_HOSTS,
    _esc,
)

LOG = logging.getLogger("VectorMonolith")


class VectorHttpDispatchMixin:
    _http: aiohttp.ClientSession | None = None
    _http_lock: Any = None  # filled in on_load
    _time_offset: float = 0.0
    _time_offset_ts: float = 0.0
    _time_sync_lock: Any = None
    _ban_check_done: bool = False
    bannote: str | None = None
    btid: int = 0
    httpc: int = 0
    http_user_agent = "Vector/MCUB/2.4.4"

    async def on_load(self) -> None:
        LOG.info("Vector loaded")
        self._http_lock = asyncio.Lock()
        self._time_sync_lock = asyncio.Lock()
        self._time_offset = 0.0
        self._time_offset_ts = 0.0
        self._http = aiohttp.ClientSession(
            headers={"User-Agent": self.http_user_agent},
            timeout=aiohttp.ClientTimeout(total=30),
        )
        await super().on_load()
        asyncio.ensure_future(self._check_ban())

    async def on_unload(self) -> None:
        LOG.info("Vector unloading")
        if self._http and not self._http.closed:
            await self._http.close()

    async def _ensure_http(self) -> aiohttp.ClientSession:
        if self._http_lock is None:
            self._http_lock = asyncio.Lock()
        if self._http is None or self._http.closed:
            async with self._http_lock:
                if self._http is None or self._http.closed:
                    self._http = aiohttp.ClientSession(
                        headers={"User-Agent": self.http_user_agent},
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
        timeout: int = 15,
        extra_headers: dict[str, str] | None = None,
    ) -> Any:
        url = urljoin(API_BASE, path.lstrip("/"))
        headers: dict[str, str] = dict(extra_headers or {})
        if token:
            headers["Authorization"] = f"Bearer {token}"
        self.httpc = 0
        try:
            http = await self._ensure_http()
            async with http.request(
                method,
                url,
                headers=headers,
                json=json_data,
                params=params,
                timeout=aiohttp.ClientTimeout(total=timeout),
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
            self.httpc = -1
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

    @staticmethod
    def _ntp_query(host: str, timeout: float = 1.5) -> float | None:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.settimeout(timeout)
                request = b"\x1b" + 47 * b"\0"
                start = time.time()
                sock.sendto(request, (host, 123))
                response, _ = sock.recvfrom(48)
                end = time.time()
            if len(response) < 48:
                return None
            seconds, fraction = struct.unpack("!II", response[40:48])
            server_ts = (seconds - NTP_EPOCH_DELTA) + fraction / 2**32
            midpoint = (start + end) / 2
            return server_ts - midpoint
        except Exception as e:
            LOG.debug("_ntp_query: host=%s failed: %r", host, e)
            return None

    async def _sync_via_ntp(self) -> float | None:
        loop = asyncio.get_event_loop()
        for host in NTP_HOSTS:
            offset = await loop.run_in_executor(None, self._ntp_query, host)
            if offset is not None:
                LOG.debug("_sync_via_ntp: host=%s offset=%.3fs", host, offset)
                return offset
        return None

    async def _sync_via_https(self) -> float | None:
        http = await self._ensure_http()
        for url in HTTP_TIME_HOSTS:
            with suppress(Exception):
                start = time.time()
                async with http.head(url, timeout=aiohttp.ClientTimeout(total=3)) as resp:
                    end = time.time()
                    date_header = resp.headers.get("Date")
                if not date_header:
                    continue
                server_ts = parsedate_to_datetime(date_header).timestamp()
                midpoint = (start + end) / 2
                offset = server_ts - midpoint
                LOG.debug("_sync_via_https: url=%s offset=%.3fs", url, offset)
                return offset
        return None

    async def _ensure_time_synced(
        self, max_age: float = 300.0, force: bool = False
    ) -> None:
        now = time.time()
        if not force and self._time_offset_ts and now - self._time_offset_ts < max_age:
            return
        if self._time_sync_lock is None:
            self._time_sync_lock = asyncio.Lock()
        async with self._time_sync_lock:
            now = time.time()
            if (
                not force
                and self._time_offset_ts
                and now - self._time_offset_ts < max_age
            ):
                return
            source = "ntp"
            offset = await self._sync_via_ntp()
            if offset is None:
                source = "https"
                offset = await self._sync_via_https()
            if offset is None:
                LOG.warning("_ensure_time_synced: all time sources failed")
                return
            self._time_offset = offset
            self._time_offset_ts = time.time()
            LOG.debug(
                "_ensure_time_synced: source=%s offset=%.3fs", source, offset
            )

    def _now(self) -> float:
        return time.time() + self._time_offset

    async def _get_active_token(self, force: bool = False) -> str | None:
        LOG.debug("_get_active_token: force=%s", force)
        await self._ensure_time_synced(force=force)
        if force:
            await self.db.db_delete(self.name, "auth_token")
            LOG.debug("_get_active_token: auth_token cleared (force)")

        cached = await self.db.db_get(self.name, "auth_token")
        if cached:
            try:
                payload = self._parse_jwt(cached)
                if payload.get("exp", 0) - self._now() > 60:
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
            b_stamp = int(self._now() // 10) - attempt
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
            self.bannote = self.strings(
                "v_ban_notice",
                reason=_esc(reason or "-"),
                term=_esc(until or "permanent"),
            )
            LOG.warning("_check_ban: %s", self.bannote)

    async def _run_search(
        self, query: str, limit: int = 30, lang: str = "en", _retried: bool = False
    ) -> tuple[list[dict[str, Any]] | None, bool]:
        token = await self._get_active_token()
        if not token:
            LOG.warning("_run_search: no token")
            return [], False

        params = {"q": query, "limit": str(limit), "lang": lang}
        res = await self._net_req("GET", "/api/search", token=token, params=params)
        if res is None and self.httpc != 401:
            if not _retried:
                LOG.warning("_run_search: first attempt failed, retrying")
                return await self._run_search(query, limit, lang, _retried=True)
            return None, True

        if self.httpc == 401:
            LOG.info("_run_search: got 401, forcing token refresh")
            token = await self._get_active_token(force=True)
            if not token:
                return [], False
            res = await self._net_req("GET", "/api/search", token=token, params=params)

        if res is None and self.httpc != 401:
            return None, True

        raw_list = (
            res.get("results", [])
            if isinstance(res, dict)
            else (res if isinstance(res, list) else [])
        )
        modules = [self._normalize_module(m) for m in raw_list if isinstance(m, dict)]
        LOG.info("_run_search: %d results", len(modules))
        return modules, True

    async def _search_modules(
        self, query: str, limit: int = 30, lang: str = "en"
    ) -> list[dict[str, Any]]:
        modules, _token_ok = await self._run_search(query, limit, lang)
        return modules or []

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
