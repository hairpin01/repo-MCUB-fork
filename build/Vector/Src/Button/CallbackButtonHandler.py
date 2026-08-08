from __future__ import annotations

import asyncio
import logging
import time
from contextlib import suppress
from typing import Any
from urllib.parse import quote

# api
from core.lib.loader.module_base import callback
from core.lib.types import InlineMessage

# local
from ..Const import (
    API_BASE,
    _esc,
    FALLBACK_BANNER,
    LOADING_BANNER
)

LOG = logging.getLogger("VectorMonolith")


class VectorCallbackButtonHandlerMixin:

    @callback()
    async def force_update(
        self, event: InlineMessage, data: dict[str, Any] | None = None
    ) -> None:
        if not data:
            return
        with suppress(Exception):
            await event.answer()
        with suppress(Exception):
            await event.edit(
                f"{self.ICONS['search']} <b>{self.strings('v_upd_req')}</b>",
                parse_mode="html",
                link_preview=False,
            )
        res, _ = await self._safe_install("Vector", data.get("url", ""), notify=False)
        with suppress(Exception):
            await event.edit(
                (
                    f"{self.ICONS['safe']} <b>{self.strings('v_upd_ok')}</b>"
                    if res == 1
                    else f"{self.ICONS['error']} <b>{self.strings('v_upd_err')}</b>"
                ),
                parse_mode="html",
                link_preview=False,
            )

    @callback()
    async def cb_vecdl_install(
        self, event: InlineMessage, data: dict[str, Any] | None = None
    ) -> None:
        if not data:
            return
        with suppress(Exception):
            await event.answer()
        modules = data.get("modules", [])
        col_name = data.get("col_name", "?")
        total_orig = data.get("total_orig", 0)
        max_batch = data.get("max_batch", 50)
        await self._safe_edit(
            event,
            f"{self.ICONS['modules_list']} {self.strings('v_dlcoll_hdr', name=_esc(col_name))}\n{self.strings('v_dlcoll_count', count=len(modules))}\n\n{self.ICONS['search']} {self.strings('v_dlcoll_start')}",
            [
                [
                    self.Button.inline(
                        "\u2026", self.cb_dummy, data=self._cb_data("dummy")
                    )
                ]
            ],
        )
        ok = 0
        failed: list[str] = []
        for mod in modules:
            dl_url = (
                mod.get("source_download_url")
                or mod.get("source_raw_url")
                or f"{API_BASE}/modules/{quote(str(mod.get('source_owner', 'unknown')), safe='')}/{quote((mod.get('name') or ''), safe='')}/source"
            )
            m_name = mod.get("name", "?")
            res, errors = await self._safe_install(m_name, dl_url, notify=False)
            if res == 1:
                ok += 1
            else:
                err_text = "unknown"
                if errors:
                    err_text = errors[0].get("type", "unknown")
                elif res == -1:
                    err_text = self.strings("v_install_fail_not_found")
                else:
                    err_text = self.strings("v_dl_err")
                failed.append(
                    self.strings(
                        "v_dlcoll_fail_item", name=_esc(m_name), reason=err_text
                    )
                )
            await asyncio.sleep(2)
        if ok == len(modules):
            result = f"{self.ICONS['safe']} {self.strings('v_dlcoll_done')}"
        elif ok > 0:
            result = f"{self.ICONS['warn']} {self.strings('v_dlcoll_done_partial')}"
        else:
            result = f"{self.ICONS['error']} {self.strings('v_dlcoll_done_none')}"
        result += f"\n<b>{ok}/{len(modules)}</b>"
        if failed:
            result += "\n\n" + "\n".join(failed[:8])
            if len(failed) > 8:
                result += f"\n\u2026 +{len(failed) - 8} more"
        if total_orig > max_batch:
            result += f"\n\n<i>{self.strings('v_dlcoll_max_batch', total=total_orig, max=max_batch)}</i>"
        await self._safe_edit(
            event,
            result,
            [
                [
                    self.Button.inline(
                        "\u2716\ufe0f", self.cb_dummy, data=self._cb_data("close")
                    )
                ]
            ],
        )

    @callback()
    async def cb_vector_search(
        self, event: InlineMessage, data: dict[str, Any] | None = None
    ) -> None:
        with suppress(Exception):
            await event.answer()
        if not data:
            return
        q = data.get("q", "")
        if not q:
            with suppress(Exception):
                await event.edit(
                    f"{self.ICONS['error']} <b>{self.strings('v_err_404', q='?')}</b>",
                    parse_mode="html",
                    link_preview=False,
                )
            return

        m_list, token_ok = await self._run_search(
            q, limit=self.config["limit"], lang=self._detect_lang_suffix()
        )
        if not token_ok:
            with suppress(Exception):
                await event.edit(
                    self.bannote
                    or f"{self.ICONS['error']} <b>{self.strings('v_err_api')}</b>",
                    parse_mode="html",
                    link_preview=False,
                )
            return
        if m_list is None:
            with suppress(Exception):
                await event.edit(
                    f"{self.ICONS['error']} <b>{self.strings('v_err_api')}</b>",
                    parse_mode="html",
                    link_preview=False,
                )
            return

        LOG.info("cb_vector_search: %d results for q=%r", len(m_list), q)
        if not m_list:
            with suppress(Exception):
                await event.edit(
                    f"{self.ICONS['error']} <b>{self.strings('v_err_404', q=_esc(q))}</b>",
                    parse_mode="html",
                    link_preview=False,
                )
            return

        cache_key = f"v_{self._norm_hash_name(q)}_{int(time.time())}"
        self._cached_groups[cache_key] = m_list
        if len(self._cached_groups) > 50:
            old = sorted(self._cached_groups.keys())[:-40]
            for k in old:
                self._cached_groups.pop(k, None)

        item = m_list[0]
        await self._safe_edit(
            event,
            self._build_html(item, 1, len(m_list)),
            self._build_kbd(item, 0, m_list, cache_key),
            item.get("banner") or FALLBACK_BANNER,
        )

    @callback()
    async def cb_toggle(
        self, event: InlineMessage, data: dict[str, Any] | None = None
    ) -> None:
        with suppress(Exception):
            await event.answer()
        if not data:
            return
        i = data.get("i", 0)
        q = data.get("q", "")
        expanded = bool(data.get("expanded", False))
        group = self._cached_groups.get(q, [])
        if 0 <= i < len(group):
            item = group[i]
            await self._safe_edit(
                event,
                self._build_html(item, i + 1, len(group)),
                self._build_kbd(item, i, group, q, expanded=expanded),
                item.get("banner"),
            )

    @callback()
    async def cb_dummy(self, event: InlineMessage) -> None:
        with suppress(Exception):
            await event.answer()

    @callback()
    async def cb_nav(
        self, event: InlineMessage, data: dict[str, Any] | None = None
    ) -> None:
        with suppress(Exception):
            await event.answer()
        if not data:
            return
        group = self._cached_groups.get(data.get("q", ""), [])
        i = data.get("i", 0)
        expanded = bool(data.get("expanded", False))
        cp = data.get("cp", 0)
        if 0 <= i < len(group):
            await self._safe_edit(
                event,
                self._build_html(group[i], i + 1, len(group)),
                self._build_kbd(
                    group[i],
                    i,
                    group,
                    data.get("q", ""),
                    expanded=expanded,
                    comments_pg=cp,
                ),
                group[i].get("banner"),
            )

    def _list_button_text(self, index: int, item: dict[str, Any]) -> str:
        name = str(item.get("name") or "?").strip()
        author = str(item.get("author") or "?").strip()
        text = f"{index + 1}. {name} by {author}"
        return text if len(text) <= 64 else text[:61].rstrip() + "…"

    def _build_list_kbd(
        self,
        group: list[dict[str, Any]],
        q: str,
        pg: int,
        orig_i: int,
        expanded: bool = False,
    ) -> list:
        gl = len(group)
        total_pages = max(1, (gl + 4) // 5)
        pg = pg % total_pages
        start, end = pg * 5, min((pg + 1) * 5, gl)
        kbd = []
        for idx in range(start, end):
            item = group[idx]
            kbd.append(
                [
                    self.Button.inline(
                        self._list_button_text(idx, item),
                        self.cb_nav,
                        data=self._cb_data(
                            "nav", i=idx, gl=gl, q=q, expanded=False
                        ),
                    )
                ]
            )

        prev_pg = (pg - 1) % total_pages
        next_pg = (pg + 1) % total_pages
        kbd.append(
            [
                self.Button.inline(
                    "◀️",
                    self.cb_page,
                    data=self._cb_data(
                        "page", pg=prev_pg, i=orig_i, gl=gl, q=q, expanded=expanded
                    ),
                ),
                self.Button.inline(
                    self.strings("v_page", idx=pg + 1, total=total_pages),
                    self.cb_dummy,
                ),
                self.Button.inline(
                    "▶️",
                    self.cb_page,
                    data=self._cb_data(
                        "page", pg=next_pg, i=orig_i, gl=gl, q=q, expanded=expanded
                    ),
                ),
            ]
        )
        kbd.append(
            [
                self.Button.inline(
                    self.strings["v_btn_bck"],
                    self.cb_nav,
                    data=self._cb_data(
                        "nav", i=orig_i, gl=gl, q=q, expanded=expanded
                    ),
                )
            ]
        )
        return kbd

    @callback()
    async def cb_list(
        self, event: InlineMessage, data: dict[str, Any] | None = None
    ) -> None:
        with suppress(Exception):
            await event.answer()
        if not data:
            return
        q = data.get("q", "")
        group = self._cached_groups.get(q, [])
        i = data.get("i", 0)
        expanded = bool(data.get("expanded", False))
        if not group:
            with suppress(Exception):
                await event.edit(
                    f"{self.ICONS['error']} {self.strings('v_err_404', q='?')}",
                    parse_mode="html",
                    link_preview=False,
                )
            return
        i = i if 0 <= i < len(group) else 0
        pg = int(data.get("pg", i // 5))
        title = f"{self.ICONS['modules_list']} <b>{self.strings('v_res_hdr')}</b>"
        await self._safe_edit(
            event,
            title,
            self._build_list_kbd(group, q, pg, i, expanded=expanded),
        )

    @callback()
    async def cb_page(
        self, event: InlineMessage, data: dict[str, Any] | None = None
    ) -> None:
        with suppress(Exception):
            await event.answer()
        if not data:
            return
        q = data.get("q", "")
        group = self._cached_groups.get(q, [])
        if not group:
            return
        orig_i = data.get("i", 0)
        orig_i = orig_i if 0 <= orig_i < len(group) else 0
        pg = int(data.get("pg", 0))
        expanded = bool(data.get("expanded", False))
        title = f"{self.ICONS['modules_list']} <b>{self.strings('v_res_hdr')}</b>"
        await self._safe_edit(
            event,
            title,
            self._build_list_kbd(group, q, pg, orig_i, expanded=expanded),
        )

    @callback()
    async def cb_rate(
        self, event: InlineMessage, data: dict[str, Any] | None = None
    ) -> None:
        if not data:
            return
        action = data.get("action", "like")
        m_owner, m_name = data.get("owner", ""), data.get("name", "")
        i, q = data.get("i", 0), data.get("q", "")
        group = self._cached_groups.get(q, [])
        token = await self._get_active_token()
        if not token:
            with suppress(Exception):
                await event.answer(
                    self.bannote or self.strings("v_err_api"), alert=True
                )
            return

        async def _send_rate(active_token: str) -> dict[str, Any] | None:
            uid = self._parse_jwt(active_token).get("sub", "")
            return await self._net_req(
                "POST",
                f"/api/rate/{quote(str(uid), safe='')}/{quote(m_owner, safe='')}/{quote(m_name, safe='')}/{action}",
                token=active_token,
            )

        res = await _send_rate(token)
        if not res or (isinstance(res, dict) and res.get("ok") is False):
            token = await self._get_active_token(force=True)
            if token:
                res = await _send_rate(token)
        if not res or (isinstance(res, dict) and res.get("ok") is False):
            with suppress(Exception):
                await event.answer(self.strings("v_err_api"), alert=True)
            return

        nl, nd = self._extract_counts(res)
        if group and i < len(group):
            if nl is not None:
                group[i]["likes"] = nl
            if nd is not None:
                group[i]["dislikes"] = nd
            item = group[i]
        else:
            item = {
                "name": m_name,
                "owner": m_owner,
                "likes": nl or 0,
                "dislikes": nd or 0,
                "source_url": f"{API_BASE}/modules/{quote(m_owner, safe='')}/{quote(m_name, safe='')}/source",
            }
        await self._safe_edit(
            event,
            self._build_html(item, i + 1, len(group or [item])),
            self._build_kbd(item, i, group, q),
            item.get("banner"),
        )
        s_val = res.get("rating", {}).get("state")
        with suppress(Exception):
            await event.answer(
                self.strings("v_fb_rm" if s_val == "removed" else "v_fb_add"),
                alert=True,
            )

    @callback()
    async def cb_install(
        self, event: InlineMessage, data: dict[str, Any] | None = None
    ) -> None:
        if not data:
            return
        m_owner, m_name = data.get("owner", ""), data.get("name", "")
        i, q = data.get("i", 0), data.get("q", "")
        group = self._cached_groups.get(q, [])
        token = await self._get_active_token()
        if not token:
            with suppress(Exception):
                await event.answer(
                    self.bannote or self.strings("v_err_api"), alert=True
                )
            return
        dl_url = f"{API_BASE}/modules/{quote(m_owner, safe='')}/{quote(m_name, safe='')}/source"
        res, errors = await self._safe_install(m_name, dl_url)
        if res == -1:
            with suppress(Exception):
                await event.answer(self.strings("v_dl_err"), alert=True)
            return
        if res == 1:
            with suppress(Exception):
                await event.answer(self.strings("v_dl_ok"), alert=True)
            return
        if errors:
            item = group[i] if group and 0 <= i < len(group) else {"name": m_name}
            await self._safe_edit(
                event,
                self._fmt_install_errors(m_name, errors),
                self._build_kbd(item, i, group, q),
                item.get("banner"),
            )
        else:
            with suppress(Exception):
                await event.answer(self.strings("v_dl_err"), alert=True)

    @callback()
    async def cb_sec_check(
        self, event: InlineMessage, data: dict[str, Any] | None = None
    ) -> None:
        if not data:
            return
        m_owner, m_name = data.get("owner", ""), data.get("name", "")
        i, q = data.get("i", 0), data.get("q", "")
        group = self._cached_groups.get(q, [])
        item = (
            group[i]
            if group and 0 <= i < len(group)
            else {"name": m_name, "owner": m_owner}
        )

        cached = self.seccache.get(m_name)
        if cached and cached.get("check"):
            await self._safe_edit(
                event,
                f"{self.ICONS['safe']} <i>{self.strings('v_aud_mem')}</i>\n\n{self._build_sec_html(item, cached)}",
                self._build_sec_kbd(item, i, group, q, True),
                item.get("banner"),
            )
            return

        token = await self._get_active_token()
        if not token:
            with suppress(Exception):
                await event.answer(self.bannote or self.strings("v_err_api"), alert=True)
            return
        res = await self._net_req(
            "GET",
            f"/api/modules/{quote(m_owner, safe='')}/{quote(m_name, safe='')}/security-check",
            token=token,
        )
        if not res or self.httpc >= 400:
            await self._safe_edit(
                event,
                f"{self.ICONS['error']} <b>{self.strings('v_aud_err')}</b>",
                self._build_sec_kbd(item, i, group, q, True),
                item.get("banner"),
            )
            return
        if res.get("check"):
            self.seccache[m_name] = res
        await self._safe_edit(
            event,
            self._build_sec_html(item, res),
            self._build_sec_kbd(item, i, group, q, bool(res.get("check"))),
            item.get("banner"),
        )

    @callback()
    async def cb_scan_go(
        self, event: InlineMessage, data: dict[str, Any] | None = None
    ) -> None:
        if not data:
            return
        m_owner, m_name = data.get("owner", ""), data.get("name", "")
        i, q = data.get("i", 0), data.get("q", "")
        group = self._cached_groups.get(q, [])
        item = (
            group[i]
            if group and 0 <= i < len(group)
            else {"name": m_name, "owner": m_owner}
        )
        token = await self._get_active_token()
        if not token:
            with suppress(Exception):
                await event.answer(self.bannote or self.strings("v_err_api"), alert=True)
            return
        await self._safe_edit(
            event,
            f"{self.ICONS['search']} <b>{self.strings('v_aud_proc')}</b>",
            self._build_sec_kbd(item, i, group, q, True),
            item.get("banner"),
        )
        res = await self._net_req(
            "POST",
            f"/api/modules/{quote(m_owner, safe='')}/{quote(m_name, safe='')}/security-check",
            token=token,
            timeout=120,
        )
        if self.httpc == 429:
            await self._safe_edit(
                event,
                f"{self.ICONS['warn']} <b>{self.strings('v_aud_zero')}</b>",
                self._build_sec_kbd(item, i, group, q, True),
                item.get("banner"),
            )
            return
        if not res or self.httpc >= 400:
            await self._safe_edit(
                event,
                f"{self.ICONS['error']} <b>{self.strings('v_aud_err')}</b>",
                self._build_sec_kbd(item, i, group, q, True),
                item.get("banner"),
            )
            return
        if res.get("check"):
            self.seccache[m_name] = res
        await self._safe_edit(
            event,
            self._build_sec_html(item, res),
            self._build_sec_kbd(item, i, group, q, True),
            item.get("banner"),
        )

    @callback()
    async def cb_talk(
        self, event: InlineMessage, data: dict[str, Any] | None = None
    ) -> None:
        if not data:
            return
        m_owner, m_name = data.get("owner", ""), data.get("name", "")
        i, q = data.get("i", 0), data.get("q", "")
        group = self._cached_groups.get(q, [])
        disc = await self._get_discussion(m_owner, m_name)
        html = self._build_discussion_html(disc, m_name)
        kbd = self._build_discussion_kbd(
            m_owner, m_name, i, len(group) if group else 1, q
        )
        item = group[i] if group and 0 <= i < len(group) else {"name": m_name}
        await self._safe_edit(event, html, kbd, item.get("banner"))
