# ‼️‼️‼️‼️ THE MODULE IS A PORT WITH HEROKU ‼️‼️‼️‼️
# ====================================================================================================================
# Repo MCUB - https://github.com/hairpin01/repo-MCUB-fork
# MCUB - https://github.com/hairpin01/MCUB-fork
# ====================================================================================================================
#   ██████╗  ██████╗ ██╗   ██╗███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗███████╗
#  ██╔════╝ ██╔═══██╗╚██╗ ██╔╝████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
#  ██║  ███╗██║   ██║ ╚████╔╝ ██╔████╔██║██║   ██║██║  ██║██║   ██║██║     █████╗  ███████╗
#  ██║   ██║██║   ██║  ╚██╔╝  ██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══╝  ╚════██║
#  ╚██████╔╝╚██████╔╝   ██║   ██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗███████╗███████║
#   ╚═════╝  ╚═════╝    ╚═╝   ╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝
#
#   OFFICIAL USERNAMES: @goymodules | @samsepi0l_ovf
#   MODULE: Vector (PORT FOR MCUB @Hairpin00)
#
#   THIS MODULE IS LICENSED UNDER GNU AGPLv3, PROTECTED AGAINST UNAUTHORIZED COPYING/RESALE,
#   AND ITS ORIGINAL AUTHORSHIP BELONGS TO @samsepi0l_ovf.
#   ALL OFFICIAL UPDATES, RELEASE NOTES, AND PATCHES ARE PUBLISHED IN THE TELEGRAM CHANNEL @goymodules.
# ====================================================================================================================
# scop: kernel min v1.4.6

from __future__ import annotations

import hashlib
import inspect
import logging
import sys
from typing import Any
from urllib.parse import quote

# api
from core.lib.loader.module_base import ModuleBase, command, loop
from core.lib.loader.module_config import (
    Boolean,
    ConfigValue,
    Integer,
    ModuleConfig,
)
from core.lib.types import Event

# local
from .Const import (
    LOADING_BANNER,
    _esc,
)
from .Button.CallbackButtonHandler import VectorCallbackButtonHandlerMixin
from .Button.InputButtonHandler import VectorInputButtonHandlerMixin
from .Button.InstallPayloadHandler import VectorInstallPayloadHandlerMixin
from .Http.HttpDispatch import VectorHttpDispatchMixin
from .BuilderPage.AntiVirusPage import VectorAntiVirusPageMixin
from .BuilderPage.DiscussionPage import VectorDiscussionPageMixin
from .BuilderPage.InstallPage import VectorInstallPageMixin
from .BuilderPage.MainPage import VectorMainPageMixin

LOG = logging.getLogger("VectorMonolith")
LOG.setLevel(logging.DEBUG)

class Vector(
    VectorHttpDispatchMixin,
    VectorInstallPageMixin,
    VectorMainPageMixin,
    VectorDiscussionPageMixin,
    VectorAntiVirusPageMixin,
    VectorInputButtonHandlerMixin,
    VectorInstallPayloadHandlerMixin,
    VectorCallbackButtonHandlerMixin,
    ModuleBase,
):
    name = "Vector"
    version = "2.4.4"
    author = "@samsepi0l_ovf"
    description = {
        "en": "Vector module registry browser.\nhttps://www.0xvector.lol",
        "ru": "Бpayзep peecтpa мoдyлeй Vector.\nhttps://www.0xvector.lol",
        "uk": "Браузер реєстру модулів Vector.\nhttps://www.0xvector.lol",
    }
    dependencies = ["aiohttp"]
    banner_url = "https://raw.githubusercontent.com/sepiol026-wq/GoyModules/refs/heads/main/assets/vector.png"

    config = ModuleConfig(
        ConfigValue(
            "limit",
            30,
            description="Search output limits.",
            validator=Integer(min=1, max=100),
        ),
        ConfigValue(
            "max_batch",
            50,
            description="Max modules per batch install.",
            validator=Integer(min=1, max=100),
        ),
        ConfigValue(
            "auto_update_notify",
            True,
            description="Notify me about module updates (hashing-based).",
            validator=Boolean(),
        ),
        ConfigValue(
            "VectorInstall",
            True,
            description="Enable Vector Install",
            validator=Boolean(),
        ),
    )
    from .Const import (
        ICONS,
        _ierrs,
        strings_i18n,
    )

    strings: dict[str, dict[str, str]] = strings_i18n
    _cached_groups: dict[str, list[dict[str, Any]]] = {}
    seccache: dict[str, dict[str, Any]] = {}


    @command(
        "vector",
        doc_en="<query> \u2014 search modules in Vector.",
        doc_ru="<\u0437\u0430\u043f\u0440\u043e\u0441> \u2014 \u043f\u043e\u0438\u0441\u043a \u043c\u043e\u0434\u0443\u043b\u0435\u0439 \u0432 Vector.",
        doc_uk="<запит> — пошук модулів у Vector.",
    )
    async def vectorcmd(self, event: Event) -> None:
        q = event.text.split(maxsplit=1)
        q = q[1].strip() if len(q) > 1 else ""
        LOG.info("vectorcmd: query=%r", q)
        if not q:
            await event.edit(
                f"{self.ICONS['error']} <b>{self.strings('v_err_empty', p='<code>.</code>')}</b>",
                parse_mode="html",
                link_preview=False,
            )
            return
        if len(q) > 120:
            await event.edit(
                f"{self.ICONS['warn']} <b>{self.strings('v_err_len')}</b>",
                parse_mode="html",
                link_preview=False,
            )
            return

        success, form_msg = await self.subinline.form(
            event.chat_id,
            f"{self.ICONS['search']} <b>{self.strings('v_sending')}</b>",
            buttons=[
                [
                    self.Button.inline(
                        "\u2800",
                        self.cb_vector_search,
                        data=self._cb_data("v_search", q=q),
                    )
                ]
            ],
            media=LOADING_BANNER,
            ttl=300,
        )
        if success and form_msg:
            await form_msg.click(0)
        else:
            await event.edit(
                f"{self.ICONS['error']} <b>{self.strings('v_err_api')}</b>",
                parse_mode="html",
                link_preview=False,
            )

    def _hash_module_source(self, module_instance: Any | None = None) -> str:
        target = module_instance or self
        module = sys.modules.get(target.__class__.__module__)
        loader = getattr(module, "__loader__", None)
        if loader and hasattr(loader, "get_source"):
            try:
                source = loader.get_source(target.__class__.__module__)
                if source:
                    return hashlib.sha256(source.encode("utf-8")).hexdigest()
            except Exception as e:
                LOG.debug("_hash_module_source: loader.get_source failed: %r", e)

        if module:
            try:
                source = inspect.getsource(module)
                return hashlib.sha256(source.encode("utf-8")).hexdigest()
            except Exception as e:
                LOG.debug("_hash_module_source: inspect.getsource failed: %r", e)
        return ""

    async def _sync_installed_modules(self) -> bool:
        token = await self._get_active_token()
        if not token:
            return False
        modules_data: list[dict[str, str]] = []
        lang = self._detect_lang_suffix()
        for collection_name in ("loaded_modules", "system_modules"):
            collection = getattr(self.kernel, collection_name, {}) or {}
            for module in collection.values():
                module_hash = self._hash_module_source(module)
                if not module_hash:
                    continue
                modules_data.append(
                    {
                        "class_name": module.__class__.__name__,
                        "contentHash": module_hash,
                        "language": lang,
                    }
                )
        if not modules_data:
            return False
        res = await self._net_req(
            "PUT",
            "/api/users/me/modules",
            token=token,
            json_data={"modules": modules_data},
            timeout=30,
        )
        return bool(res and res.get("ok"))

    @loop(interval=86_400, autostart=True)
    async def _sync_modules_keeper(self) -> None:
        if not self.config["auto_update_notify"]:
            return
        try:
            await self._sync_installed_modules()
        except Exception as e:
            LOG.debug("_sync_modules_keeper: failed: %r", e)

    async def _install_vector_update(self, event: Event, dl_url: str) -> None:
        await event.edit(
            f"{self.ICONS['search']} <b>{self.strings('v_upd_req')}</b>",
            parse_mode="html",
            link_preview=False,
        )
        res, _errors = await self._safe_install("Vector", dl_url, notify=False)
        text = (
            f"{self.ICONS['safe']} <b>{self.strings('v_upd_ok')}</b>"
            if res == 1
            else f"{self.ICONS['error']} <b>{self.strings('v_upd_err')}</b>"
        )
        await event.edit(text, parse_mode="html", link_preview=False)

    @command(
        "vecupdate",
        doc_en="[-f|--force] \u2014 update Vector module.",
        doc_ru="[-f|--force] \u2014 \u043e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u043c\u043e\u0434\u0443\u043b\u044c Vector.",
        doc_uk="[-f|--force] — оновити модуль Vector.",
    )
    async def vecupdate(self, event: Event) -> None:
        args = event.text.split(maxsplit=1)
        args_str = args[1].strip() if len(args) > 1 else ""
        force = "-f" in args_str or "--force" in args_str
        LOG.info("vecupdate: force=%s", force)

        dl_url = "https://raw.githubusercontent.com/hairpin01/repo-MCUB-fork/refs/heads/main/Vector-MCUB-repo.py"
        if force:
            await self._install_vector_update(event, dl_url)
            return

        await event.edit(
            f"{self.ICONS['search']} <b>{self.strings('v_upd_check')}</b>",
            parse_mode="html",
            link_preview=False,
        )

        remote_bytes = await self._net_req("GET", dl_url, as_bytes=True, timeout=30)
        if not remote_bytes:
            LOG.warning("vecupdate: remote source unavailable, installing anyway")
            await self._install_vector_update(event, dl_url)
            return

        remote_hash = hashlib.sha256(remote_bytes).hexdigest()
        local_hash = self._hash_module_source()
        if local_hash:
            LOG.debug(
                "vecupdate: local_hash=%s remote_hash=%s",
                local_hash[:16],
                remote_hash[:16],
            )
        else:
            LOG.warning("vecupdate: local source hash unavailable, assuming update needed")

        if local_hash and local_hash == remote_hash:
            await self.subinline.form(
                event.chat_id,
                f"{self.ICONS['search']} <b>{self.strings('v_upd_req')}</b>\n\n{self.strings('v_upd_same')}",
                buttons=[
                    [
                        self.Button.inline(
                            self.strings["v_upd_force_btn"],
                            self.force_update,
                            data=self._cb_data("force_upd", url=dl_url),
                        ),
                        self.Button.inline(
                            self.strings["v_upd_cancel"],
                            self.cb_dummy,
                            data=self._cb_data("cancel_update"),
                        ),
                    ]
                ],
                parse_mode="html",
            )
            return

        await self._install_vector_update(event, dl_url)


    @command(
        "vecme",
        doc_en="\u2014 open Vector as Telegram Mini App.",
        doc_ru="\u2014 \u043e\u0442\u043a\u0440\u044b\u0442\u044c Vector \u043a\u0430\u043a Telegram Mini App.",
        doc_uk="— відкрити Vector як Telegram Mini App.",
    )
    async def vecmecmd(self, event: Event) -> None:
        bot_info = await self._net_req("GET", "/api/tg-bot")
        bot_uname = (bot_info or {}).get("username", "").strip().lstrip("@")
        if not bot_uname:
            await event.edit(
                f"{self.ICONS['error']} <b>{self.strings('v_err_api')}</b>",
                parse_mode="html",
                link_preview=False,
            )
            return
        link = f"https://t.me/{bot_uname}/vector"
        text = (
            f"{self.ICONS['shield']} <b>{self.strings('v_miniapp_title')}</b>\n\n"
            f"{self.strings('v_miniapp_body')}"
        )
        await self.subinline.form(
            event.chat_id,
            text,
            buttons=[[self.Button.url(self.strings("v_miniapp_btn"), link)]],
            parse_mode="html",
        )

    @command(
        "vecdl",
        doc_en="<slug or URL> \u2014 download and install entire module collection from Vector.",
        doc_ru="<slug \u0438\u043b\u0438 \u0441\u0441\u044b\u043b\u043a\u0430> \u2014 \u0441\u043a\u0430\u0447\u0430\u0442\u044c \u0438 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u044e \u0438\u0437 Vector.",
        doc_uk="<slug або URL> — завантажити та встановити колекцію з Vector.",
    )
    async def vecdlcmd(self, event: Event) -> None:
        args = event.text.split(maxsplit=1)
        raw_arg = args[1].strip() if len(args) > 1 else ""
        slug = (
            raw_arg.split("/collections/")[-1].split("/")[0].split("?")[0]
            if "/collections/" in raw_arg
            else raw_arg
        )
        LOG.info("vecdl: slug=%r", slug)
        if not slug:
            await event.edit(
                f"{self.ICONS['error']} <b>{self.strings('v_vecdl_usage', p='<code>.</code>')}</b>",
                parse_mode="html",
                link_preview=False,
            )
            return
        token = await self._get_active_token()
        if not token:
            await event.edit(
                self.bannote
                or f"{self.ICONS['error']} <b>{self.strings('v_err_api')}</b>",
                parse_mode="html",
                link_preview=False,
            )
            return
        raw = await self._net_req(
            "GET", f"/api/collections/{quote(slug, safe='')}", token=token
        )
        if not raw or not raw.get("ok"):
            await event.edit(
                f"{self.ICONS['error']} <b>{self.strings('v_dlcoll_not_found')}</b>",
                parse_mode="html",
                link_preview=False,
            )
            return
        col = raw["collection"]
        modules = [
            entry["module"]
            for entry in (col.get("modules") or [])
            if entry.get("module")
        ]
        if not modules:
            await event.edit(
                f"{self.ICONS['warn']} <b>{self.strings('v_dlcoll_empty')}</b>",
                parse_mode="html",
                link_preview=False,
            )
            return
        await event.edit(
            f"{self.ICONS['search']} <b>{self.strings('v_sending')}</b>",
            parse_mode="html",
            link_preview=False,
        )
        max_batch = int(self.config["max_batch"])
        total_orig = len(modules)
        if total_orig > max_batch:
            modules = modules[:max_batch]
        col_name = col.get("name", slug)
        await self._safe_edit(
            event,
            f"{self.ICONS['modules_list']} {self.strings('v_dlcoll_hdr', name=_esc(col_name))}\n{self.strings('v_dlcoll_count', count=len(modules))}",
            [
                [
                    self.Button.inline(
                        self.strings["v_btn_dl"],
                        self.cb_vecdl_install,
                        data=self._cb_data(
                            "vecdl_install",
                            modules=modules,
                            col_name=col_name,
                            total_orig=total_orig,
                            max_batch=max_batch,
                        ),
                    )
                ]
            ],
        )
