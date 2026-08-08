from __future__ import annotations

import hashlib
import hmac
import logging
import re
import time
from contextlib import suppress
from urllib.parse import quote

from telethon.tl.functions.account import GetNotifySettingsRequest, UpdateNotifySettingsRequest
from telethon.tl.types import InputNotifyPeer, InputPeerNotifySettings

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
        if getattr(event, "out", False):
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

        text = (getattr(event, "text", None) or getattr(event, "raw_text", "") or "").strip()
        notify_peer = None
        saved_notify = None
        with suppress(Exception):
            peer = await self.client.get_input_entity(event.chat_id)
            notify_peer = InputNotifyPeer(peer=peer)
        if notify_peer is not None:
            with suppress(Exception):
                saved_notify = await self.client(GetNotifySettingsRequest(notify_peer))
            with suppress(Exception):
                await self.client(
                    UpdateNotifySettingsRequest(
                        peer=notify_peer,
                        settings=InputPeerNotifySettings(mute_until=2**31 - 1),
                    )
                )

        try:
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
            if action not in {"install", "like", "dislike", "update"}:
                return
            if not owner_module or not action or not ts_raw or not signature:
                return
            if not re.fullmatch(r"[^:]+", module_name) or not ts_raw.isdigit():
                return

            await self._ensure_time_synced()
            ts = int(ts_raw)
            if abs(int(self._now()) - ts) > 60:
                return

            local_payload = f"{owner_module}:{action}:{ts}"
            local_signature = hmac.new(
                AUTH_SECRET.encode("utf-8"), local_payload.encode("utf-8"), hashlib.sha256
            ).hexdigest()
            if not hmac.compare_digest(local_signature, signature):
                return
            with suppress(Exception):
                await event.delete()

            async def send_feedback(
                status: str, reason: str = "", b_until: str = ""
            ) -> None:
                fb_ts = int(self._now())
                safe_r = (reason or "").replace(":", " ").strip()[:200]
                safe_u = (b_until or "").replace(":", " ").strip()[:50]
                fb_payload = f"{owner_module}:{action}:{status}:{fb_ts}:{safe_r}:{safe_u}"
                fb_sig = hmac.new(
                    AUTH_SECRET.encode("utf-8"), fb_payload.encode("utf-8"), hashlib.sha256
                ).hexdigest()
                with suppress(Exception):
                    await self.client.send_message(
                        event.chat_id,
                        f"#v_feedback:{owner_module}:{action}:{status}:{fb_ts}:{safe_r}:{safe_u}:{fb_sig}",
                    )
                with suppress(Exception):
                    await self._net_req(
                        "POST",
                        "/api/tg-bot/install-feedback",
                        json_data={
                            "owner_module": owner_module,
                            "status": status,
                            "reason": safe_r,
                        },
                        extra_headers={"x-bot-secret": AUTH_SECRET},
                        timeout=5,
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
                res, _errors = await self._safe_install(module_name, dl_url, notify=False)
                await send_feedback("ok" if res == 1 else "error")
                return
            if action == "update":
                mod_info = await self._net_req(
                    "GET", f"/api/modules/by-id/{quote(owner_module, safe='')}", token=token
                )
                if not mod_info or not mod_info.get("ok"):
                    await send_feedback("error", "module not found")
                    return
                mod_data = mod_info.get("module", {})
                mod_name = mod_data.get("name", "")
                mod_owner = mod_data.get("source_owner", "") or owner
                if not mod_name:
                    await send_feedback("error", "invalid module data")
                    return
                dl_url = f"{API_BASE}/modules/{quote(mod_owner, safe='')}/{quote(mod_name, safe='')}/source"
                res, _errors = await self._safe_install(mod_name, dl_url, notify=False)
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
        finally:
            if notify_peer is not None:
                with suppress(Exception):
                    await self.client(
                        UpdateNotifySettingsRequest(
                            peer=notify_peer,
                            settings=InputPeerNotifySettings(
                                mute_until=getattr(saved_notify, "mute_until", 0)
                                if saved_notify is not None
                                else 0,
                            ),
                        )
                    )
