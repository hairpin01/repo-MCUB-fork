from __future__ import annotations

import hashlib
import logging
import unicodedata
from contextlib import suppress
from typing import Any
from urllib.parse import quote

# local
from ..Const import API_BASE, _esc

LOG = logging.getLogger("VectorMonolith")


class VectorMainPageMixin:

    @staticmethod
    def _norm_hash_name(value: str) -> str:
        value = unicodedata.normalize("NFKC", str(value or ""))
        value = (
            value.replace("\u200b", "")
            .replace("\u200c", "")
            .replace("\u200d", "")
            .replace("\ufeff", "")
        )
        return hashlib.sha256(value.encode()).hexdigest()[:16]

    def _detect_lang_suffix(self) -> str:
        variants = {"en", "ru", "jp", "uk", "de", "neofit", "tiktok", "leet", "uwu"}
        lang = str(self.strings.get("lang", "en")).strip().lower()
        return lang if lang in variants else "en"

    def _normalize_module(self, raw: dict) -> dict:
        LOG.debug("_normalize_module: name=%s", raw.get("name", "?"))
        lang = self._detect_lang_suffix()
        content_lang = (
            "ru"
            if lang in ("ru", "neofit", "tiktok", "leet", "uwu")
            else ("ua" if lang == "uk" else lang)
        )
        cmds = []
        for c in raw.get("commands") or []:
            if isinstance(c, dict):
                cmd_desc = (
                    c.get(f"desc_{content_lang}")
                    or c.get("description")
                    or c.get("desc")
                    or ""
                )
                cmds.append(
                    {
                        "name": c.get("name") or c.get("cmd") or "",
                        "description": cmd_desc,
                        "is_inline": bool(c.get("is_inline")),
                        "is_placeholder": bool(c.get("is_placeholder")),
                    }
                )
        dev = str(raw.get("developer") or raw.get("author") or "@Unknown")
        ioff = bool(
            raw.get("official")
            or raw.get("is_official")
            or raw.get("verified")
            or raw.get("is_verified")
            or raw.get("telegram_verified")
            or raw.get("official_developer")
            or raw.get("is_official_developer")
        )
        name = str(raw.get("name") or raw.get("class_name") or "Unknown")
        locales = raw.get("locales")
        desc = raw.get("description") or ""
        if isinstance(locales, dict):
            loc_key = f"description_{content_lang}"
            loc_val = locales.get(loc_key)
            if isinstance(loc_val, str) and loc_val.strip():
                desc = loc_val
        return {
            "name": name,
            "owner": raw.get("source_owner") or "unknown",
            "version": raw.get("version") or "?.?.?",
            "author": dev,
            "description": desc,
            "commands": cmds,
            "dependencies": [str(d) for d in (raw.get("dependencies") or [])],
            "official": ioff,
            "likes": int(raw.get("likes") or 0),
            "dislikes": int(raw.get("dislikes") or 0),
            "banner": raw.get("banner"),
            "tags": raw.get("tags") or [],
            "source_url": raw.get("source_url")
            or f"{API_BASE}/modules/{quote(raw.get('source_owner', 'unknown'), safe='')}/{quote(name, safe='')}/source",
            "dl_url": raw.get("source_url")
            or f"{API_BASE}/modules/{quote(raw.get('source_owner', 'unknown'), safe='')}/{quote(name, safe='')}/source",
        }

    @staticmethod
    def _extract_counts(data: dict) -> tuple[int | None, int | None]:
        likes = dislikes = None
        for container in (
            data,
            data.get("module"),
            data.get("data"),
            data.get("result"),
            data.get("summary"),
        ):
            if not isinstance(container, dict):
                continue
            for lk in ("likes", "likes_count", "likesCount", "likeCount", "like_count"):
                v = container.get(lk)
                if v is not None:
                    try:
                        likes = int(v)
                    except (ValueError, TypeError):
                        pass
                    break
            for dk in (
                "dislikes",
                "dislikes_count",
                "dislikesCount",
                "dislikeCount",
                "dislike_count",
            ):
                v = container.get(dk)
                if v is not None:
                    try:
                        dislikes = int(v)
                    except (ValueError, TypeError):
                        pass
                    break
            if likes is not None and dislikes is not None:
                break
        return likes, dislikes

    def _build_html(self, item: dict, idx: int, total: int) -> str:
        name, author, version = (
            item.get("name", "?"),
            item.get("author", "?"),
            item.get("version", "?"),
        )
        description = item.get("description", "")
        commands, deps = item.get("commands", []), item.get("dependencies", [])
        official = item.get("official", False)

        parts = []

        # header block
        header = f"{self.ICONS['module']} <code>{_esc(name)}</code> by <code>{_esc(author)}</code>"
        if version and version != "?.?.?":
            header += f" (<code>v{_esc(version)}</code>)"

        status_text = (
            self.strings("v_dev_ofc") if official else self.strings("v_dev_unofc")
        )
        status_line = f"{self.ICONS['verified'] if official else self.ICONS['module']} dev {_esc(status_text)}"

        header_block = header + "\n" + status_line
        if total > 1:
            header_block += (
                "\n"
                + f"{self.ICONS['modules_list']} {self.strings('v_page', idx=idx, total=total)}"
            )
        parts.append(f"<blockquote expandable>{header_block}</blockquote>")

        # description block
        if description and description.strip():
            desc_text = _esc(description.strip()[:200])
            parts.append(
                f"<blockquote expandable>{self.ICONS['description']} {self.strings('v_info')}\n{desc_text}</blockquote>"
            )
        else:
            parts.append(
                f"<blockquote>{self.ICONS['description']} {self.strings('v_info')}\n\u2014</blockquote>"
            )

        tags = [str(tag).strip() for tag in item.get("tags", []) if str(tag).strip()]
        if tags:
            tag_text = ", ".join(f"<code>{_esc(tag)}</code>" for tag in tags[:12])
            parts.append(
                f"<blockquote expandable>{self.ICONS['stats']} {self.strings('v_tags')}\n{tag_text}</blockquote>"
            )

        # commands block
        if commands:
            cmd_lines = []
            visible_count = 0
            for c in commands[:15]:
                if isinstance(c, dict):
                    cn = c.get("name", "")
                    cd = (c.get("description", "") or "").split("\n")[0]
                    if c.get("is_placeholder"):
                        line = (
                            f"<code>{{{_esc(cn)}}}</code> {_esc(cd)}"
                            if cd
                            else f"<code>{{{_esc(cn)}}}</code>"
                        )
                    elif c.get("is_inline"):
                        line = (
                            f"<code>@bot {_esc(cn)}</code> {_esc(cd)}"
                            if cd
                            else f"<code>@bot {_esc(cn)}</code>"
                        )
                    else:
                        line = f".{_esc(cn)} {_esc(cd)}" if cd else f".{_esc(cn)}"
                    if not c.get("is_placeholder"):
                        visible_count += 1
                    cmd_lines.append(line)
                elif isinstance(c, str):
                    c2 = c.strip()
                    if c2 and not c2.startswith("+"):
                        cmd_lines.append(f".{_esc(c2)}")
                        visible_count += 1
            hidden = len(commands) - visible_count
            extra = (
                f"\n{self.strings('v_hid_cmd', rem=str(hidden))}" if hidden > 0 else ""
            )
            parts.append(
                f"<blockquote expandable>{self.ICONS['command']} {self.strings('v_cmds')}\n{chr(10).join(cmd_lines)}{extra}</blockquote>"
            )
        else:
            parts.append(
                f"<blockquote>{self.ICONS['command']} {self.strings('v_cmds')}\n\u2014</blockquote>"
            )

        # deps block
        if deps:
            dep_str = ", ".join(f"<code>{_esc(d)}</code>" for d in deps[:8])
            parts.append(
                f"<blockquote expandable>{self.ICONS['dependency']} {self.strings('v_deps')}\n{dep_str}</blockquote>"
            )
        else:
            parts.append(
                f"<blockquote>{self.ICONS['dependency']} {self.strings('v_deps')}\n\u2014</blockquote>"
            )

        return "\n".join(parts)

    def _cb_data(self, handler: str, **kwargs) -> dict:
        return {"h": handler, **kwargs}

    def _build_kbd(
        self,
        item: dict,
        i: int,
        group: list | None,
        q: str,
        expanded: bool = False,
        comments_pg: int = 0,
    ) -> list:
        name, owner = item.get("name", "?"), item.get("owner", "?")
        likes, dislikes = item.get("likes", 0), item.get("dislikes", 0)
        gl = len(group) if group else 1

        kbd = [
            [
                self.Button.copy(self.strings["v_btn_copy"], q),
                self.Button.inline(
                    self.strings["v_btn_dl"],
                    self.cb_install,
                    data=self._cb_data(
                        "install", owner=owner, name=name, i=i, gl=gl, q=q
                    ),
                ),
                self.Button.url(
                    self.strings["v_btn_code"], item.get("source_url", "") or ""
                ),
            ],
            [
                self.Button.inline(
                    f"\U0001f44d {likes}",
                    self.cb_rate,
                    data=self._cb_data(
                        "rate", action="like", owner=owner, name=name, i=i, gl=gl, q=q
                    ),
                ),
                self.Button.inline(
                    f"\U0001f44e {dislikes}",
                    self.cb_rate,
                    data=self._cb_data(
                        "rate",
                        action="dislike",
                        owner=owner,
                        name=name,
                        i=i,
                        gl=gl,
                        q=q,
                    ),
                ),
            ],
        ]

        if group and gl > 1:
            prev_i = (i - 1) % gl
            next_i = (i + 1) % gl
            kbd.append(
                [
                    self.Button.inline(
                        "\u25c0\ufe0f",
                        self.cb_nav,
                        data=self._cb_data(
                            "nav", i=prev_i, gl=gl, q=q, expanded=expanded, cp=comments_pg
                        ),
                    ),
                    self.Button.inline(
                        self.strings("v_page", idx=i + 1, total=gl),
                        self.cb_list,
                        data=self._cb_data(
                            "list", i=i, gl=gl, q=q, expanded=expanded, cp=comments_pg
                        ),
                    ),
                    self.Button.inline(
                        "\u25b6\ufe0f",
                        self.cb_nav,
                        data=self._cb_data(
                            "nav", i=next_i, gl=gl, q=q, expanded=expanded, cp=comments_pg
                        ),
                    ),
                ]
            )

        kbd.append(
            [
                self.Button.inline(
                    self.strings["v_btn_col" if expanded else "v_btn_exp"],
                    self.cb_toggle,
                    data=self._cb_data(
                        "toggle", i=i, gl=gl, q=q, expanded=not expanded
                    ),
                ),
            ]
        )

        if expanded:
            kbd.append(
                [
                    self.Button.inline(
                        self.strings["v_btn_talk"],
                        self.cb_talk,
                        data=self._cb_data(
                            "talk", owner=owner, name=name, i=i, gl=gl, q=q
                        ),
                    ),
                    self.Button.inline(
                        self.strings["v_btn_sec"],
                        self.cb_sec_check,
                        data=self._cb_data(
                            "sec", owner=owner, name=name, i=i, gl=gl, q=q
                        ),
                    ),
                ]
            )

        return kbd

    async def _safe_edit(
        self,
        event: Any,
        text: str,
        buttons: list | None = None,
        banner_url: str | None = None,
    ) -> None:
        try:
            kw: dict[str, Any] = {}
            if buttons:
                kw["buttons"] = buttons
            if banner_url:
                kw["file"] = banner_url
            try:
                await event.edit(text, parse_mode="html", link_preview=False, **kw)
            except Exception as e:
                ename = type(e).__name__
                if (
                    "WebpageMediaEmpty" in ename
                    or "WebpageCurlFailed" in ename
                    or "MediaCaptionTooLong" in ename
                ):
                    kw.pop("file", None)
                    with suppress(Exception):
                        await event.edit(
                            text, parse_mode="html", link_preview=False, **kw
                        )
                else:
                    raise
        except Exception as e:
            LOG.warning("_safe_edit: %r", e)
            with suppress(Exception):
                await event.answer(self.strings("v_err_gui"), alert=True)
