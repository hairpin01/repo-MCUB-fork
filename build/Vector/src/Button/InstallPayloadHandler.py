from __future__ import annotations

import hashlib
import hmac
import logging
import re
import time
from contextlib import suppress
from urllib.parse import quote

# api
from core.lib.loader.module_base import watcher
from core.lib.types import Event

# local
from ..Const import (
    API_BASE,
    AUTH_SECRET,
    LANG_PING,
    LANG_PONG,
)

LOG = logging.getLogger("VectorMonolith")


class VectorInstallPayloadHandlerMixin:

    @watcher()
    async def vector_install_payload_watcher(
        self, event: Event
    ) -> None:
        if event.out:
            return
        if not self.config["VectorInstall"]:
            return
        if not self.btid:
            try:
                binfo = await self._net_req("GET", "/api/tg-bot")
                buname = (binfo or {}).get("username", "").strip().lstrip("@")
                if buname:
                    self.btid = getattr(await self.client.get_entity(buname), "id", 0)
            except Exception:
                self.btid = -1
        if self.btid <= 0:
            return
        sid = getattr(event, "sender_id", None) or 0
        if sid and int(sid) != self.btid:
            return
        text = (event.text or "").strip()
        if text == LANG_PING:
            with suppress(Exception):
                await self.client.send_message(
                    event.chat_id, f"{LANG_PONG}{self._detect_lang_suffix()}"
                )
            with suppress(Exception):
                await event.delete()
            return
        if not text.startswith("#v_payload:"):
            return
        parts = text.split(":", 4)
        if len(parts) != 5:
            return
        _, owner_module, action, ts_raw, signature = parts
        LOG.info("vector_watcher: owner_module=%s action=%s", owner_module, action)
        owner, module_name = (
            owner_module.split("|", 1)
            if "|" in owner_module
            else ("unknown", owner_module)
        )
        if action not in {"install", "like", "dislike"}:
            return
        if not re.fullmatch(r"[A-Za-z0-9._-]+", module_name) or not ts_raw.isdigit():
            return
        if abs(int(time.time()) - int(ts_raw)) > 60:
            return
        local_signature = hmac.new(
            AUTH_SECRET.encode("utf-8"),
            f"{owner_module}:{action}:{ts_raw}".encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
        if not hmac.compare_digest(local_signature, signature):
            return
        with suppress(Exception):
            await event.delete()

        async def send_feedback(
            status: str, reason: str = "", b_until: str = ""
        ) -> None:
            fb_ts = int(time.time())
            safe_r = reason.replace(":", " ").strip()[:200]
            safe_u = b_until.replace(":", " ").strip()[:50]
            fb_payload = f"{owner_module}:{action}:{status}:{fb_ts}:{safe_r}:{safe_u}"
            fb_sig = hmac.new(
                AUTH_SECRET.encode("utf-8"), fb_payload.encode("utf-8"), hashlib.sha256
            ).hexdigest()
            with suppress(Exception):
                await self.client.send_message(
                    event.chat_id,
                    f"#v_feedback:{owner_module}:{action}:{status}:{fb_ts}:{safe_r}:{safe_u}:{fb_sig}",
                )

        token = await self._get_active_token()
        if not token:
            await send_feedback(
                "banned",
                "User is banned" if not self.bannote else str(self.bannote),
                "permanent",
            )
            return
        if action == "install":
            dl_url = f"{API_BASE}/modules/{quote(owner, safe='')}/{quote(module_name, safe='')}/source"
            res, _ = await self._safe_install(module_name, dl_url, notify=False)
            await send_feedback("ok" if res == 1 else "error")
            return
        uid = self._parse_jwt(token).get("sub", "")
        res = await self._net_req(
            "POST",
            f"/api/rate/{quote(str(uid), safe='')}/{quote(owner, safe='')}/{quote(module_name, safe='')}/{action}",
            token=token,
        )
        if not res and self.httpc in {401, 403}:
            await send_feedback("banned", "User is banned", "permanent")
            return
        await send_feedback("ok" if res and res.get("ok") else "error")
