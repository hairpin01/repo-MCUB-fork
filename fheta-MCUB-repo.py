# name: fheta-MCUB-repo
# github MCUB repo: https://github.com/hairpin01/repo-MCUB-fork
# github fheta https://github.com/Fixyres/FModules/
# Fheta Updates Channel: https://t.me/FHeta_Updates
# Bot fheta: @FHeta_Robot
# My channel: https://t.me/LinuxGram2
# -------------------- Meta data ---------------------------
# requires:
# author: @Fixyres && @Hairpin00
# version: 2.1.0
# description: Fheta for MCUB! / Фxeтa в MCUB! @FHeta_Updates
# scop: kernel min v1.1.6
# banner_url: https://github.com/Fixyres/FModules/blob/main/assets/FHeta/logo.png?raw=true
# ----------------------- End ------------------------------
import asyncio
import aiohttp
import html
import re
import ssl
from urllib.parse import unquote

from telethon import Button
from core_inline.api.inline import make_cb_button
from core.lib.loader.module_config import (
    ModuleConfig,
    Boolean,
    Choice,
    ConfigValue,
)


def register(kernel):

    THEMES = {
        "default": {
            "search": '<tg-emoji emoji-id="5188217332748527444">🔍</tg-emoji>',
            "error": '<tg-emoji emoji-id="5465665476971471368">❌</tg-emoji>',
            "warn": '<tg-emoji emoji-id="5447644880824181073">⚠️</tg-emoji>',
            "description": '<tg-emoji emoji-id="5334882760735598374">📝</tg-emoji>',
            "command": '<tg-emoji emoji-id="5341715473882955310">⚙️</tg-emoji>',
            "placeholder": '<tg-emoji emoji-id="5359785904535774578">🗒️</tg-emoji>',
            "module": '<tg-emoji emoji-id="5454112830989025752">📦</tg-emoji>',
            "channel": '<tg-emoji emoji-id="5278256077954105203">📢</tg-emoji>',
            "modules_list": '<tg-emoji emoji-id="5197269100878907942">📋</tg-emoji>',
        },
        "winter": {
            "search": '<tg-emoji emoji-id="5431895003821513760">❄️</tg-emoji>',
            "error": '<tg-emoji emoji-id="5404728536810398694">🧊</tg-emoji>',
            "warn": '<tg-emoji emoji-id="5447644880824181073">🌨️</tg-emoji>',
            "description": '<tg-emoji emoji-id="5255850496291259327">📜</tg-emoji>',
            "command": '<tg-emoji emoji-id="5199503707938505333">🎅</tg-emoji>',
            "placeholder": '<tg-emoji emoji-id="5204046675236109418">🗒️</tg-emoji>',
            "module": '<tg-emoji emoji-id="5197708768091061888">🎁</tg-emoji>',
            "channel": '<tg-emoji emoji-id="5278256077954105203">📢</tg-emoji>',
            "modules_list": '<tg-emoji emoji-id="5345935030143196497">🎄</tg-emoji>',
        },
        "summer": {
            "search": '<tg-emoji emoji-id="5188217332748527444">🔍</tg-emoji>',
            "error": '<tg-emoji emoji-id="5470049770997292425">🌡️</tg-emoji>',
            "warn": '<tg-emoji emoji-id="5447644880824181073">⚠️</tg-emoji>',
            "description": '<tg-emoji emoji-id="5361684086807076580">🍹</tg-emoji>',
            "command": '<tg-emoji emoji-id="5442644589703866634">🏄</tg-emoji>',
            "placeholder": '<tg-emoji emoji-id="5434121252874756456">🗒️</tg-emoji>',
            "module": '<tg-emoji emoji-id="5433645645376264953">🏖️</tg-emoji>',
            "channel": '<tg-emoji emoji-id="5278256077954105203">📢</tg-emoji>',
            "modules_list": '<tg-emoji emoji-id="5472178859300363509">🏖️</tg-emoji>',
        },
        "spring": {
            "search": '<tg-emoji emoji-id="5449885771420934013">🌱</tg-emoji>',
            "error": '<tg-emoji emoji-id="5208923808169222461">🥀</tg-emoji>',
            "warn": '<tg-emoji emoji-id="5447644880824181073">⚠️</tg-emoji>',
            "description": '<tg-emoji emoji-id="5251524493561569780">🍃</tg-emoji>',
            "command": '<tg-emoji emoji-id="5449850741667668411">🦋</tg-emoji>',
            "placeholder": '<tg-emoji emoji-id="5434121252874756456">🗒️</tg-emoji>',
            "module": '<tg-emoji emoji-id="5440911110838425969">🌿</tg-emoji>',
            "channel": '<tg-emoji emoji-id="5278256077954105203">📢</tg-emoji>',
            "modules_list": '<tg-emoji emoji-id="5440748683765227563">🌺</tg-emoji>',
        },
        "autumn": {
            "search": '<tg-emoji emoji-id="5253944419870062295">🍂</tg-emoji>',
            "error": '<tg-emoji emoji-id="5281026503658728615">🍁</tg-emoji>',
            "warn": '<tg-emoji emoji-id="5447644880824181073">⚠️</tg-emoji>',
            "description": '<tg-emoji emoji-id="5406631276042002796">📜</tg-emoji>',
            "command": '<tg-emoji emoji-id="5212963577098417551">🍂</tg-emoji>',
            "placeholder": '<tg-emoji emoji-id="5363965354391388799">🗒️</tg-emoji>',
            "module": '<tg-emoji emoji-id="5249157915041865558">🍄</tg-emoji>',
            "channel": '<tg-emoji emoji-id="5278256077954105203">📢</tg-emoji>',
            "modules_list": '<tg-emoji emoji-id="5305495722618010655">🍂</tg-emoji>',
        },
    }

    STRINGS = {
        "ru": {
            "lang": "ru",
            "author": "oт",
            "description": "Oпиcaниe",
            "commands": "Кoмaнды",
            "placeholders": "Плeйcxoлдepы",
            "morecommands": "...и eщё {remaining} кoмaнд.",
            "moreplaceholders": "...и eщё {remaining} плeйcxoлдepoв.",
            "list": "Вce нaйдeнныe мoдyли:",
            "search": "Пoиcк пo зaпpocy {query}...",
            "noquery": "Ввeдитe зaпpoc для пoиcкa, пpимep: {prefix}fheta зaпpoc",
            "notfound": "Hичeгo нe нaйдeнo пo зaпpocy {query}.",
            "toolong": "Зaпpoc cлишкoм бoльшoй, coкpaтитe дo 168 cимвoлoв.",
            "added": "✔ Oцeнкa дoбaвлeнa!",
            "changed": "✔ Oцeнкa измeнeнa!",
            "deleted": "✔ Oцeнкa yдaлeнa!",
            "prompt": "Ввeдитe зaпpoc для пoиcкa.",
            "hint": "Haзвaниe, кoмaндa, oпиcaниe, aвтop.",
            "retry": "Пoпpoбyйтe дpyгoй зaпpoc.",
            "install": "Уcтaнoвить",
            "counter": "{idx}/{total}",
            "code": "Кoд",
            "success": "✔ Moдyль ycпeшнo ycтaнoвлeн!",
            "error": "✘ Oшибкa, вoзмoжнo, мoдyль пoлoмaн!",
            "overwrite": "✘ Oшибкa, мoдyль пытaлcя пepeзaпиcaть вcтpoeнный!",
            "dependency": "✘ Oшибкa ycтaнoвки зaвиcимocтeй! {deps}",
            "inline_unavailable": "Инлaйн-бoт нeдocтyпeн.",
            "bot_not_configured": "Инлaйн-бoт нe нacтpoeн.",
            "search_failed": "He yдaлocь выпoлнить пoиcк.",
            "cmd_error": "Oшибкa пpи выпoлнeнии кoмaнды.",
            "installing": "Уcтaнaвливaю...",
        },
        "en": {
            "lang": "en",
            "author": "by",
            "description": "Description",
            "commands": "Commands",
            "placeholders": "Placeholders",
            "morecommands": "...and {remaining} more commands.",
            "moreplaceholders": "...and {remaining} more placeholders.",
            "list": "All found modules:",
            "search": "Searching for {query}...",
            "noquery": "Enter a search query, example: {prefix}fheta query",
            "notfound": "Nothing found for query {query}.",
            "toolong": "Query is too long, shorten to 168 characters.",
            "added": "✔ Rating submitted!",
            "changed": "✔ Rating changed!",
            "deleted": "✔ Rating removed!",
            "prompt": "Enter a query to search.",
            "hint": "Name, command, description, author.",
            "retry": "Try another query.",
            "install": "Install",
            "counter": "{idx}/{total}",
            "code": "Code",
            "success": "✔ Module installed successfully!",
            "error": "✘ Error, the module might be broken!",
            "overwrite": "✘ Error, module tried to overwrite a built-in!",
            "dependency": "✘ Dependency install error! {deps}",
            "inline_unavailable": "Inline bot not available.",
            "bot_not_configured": "Inline bot not configured.",
            "search_failed": "Search failed.",
            "cmd_error": "Error executing command.",
            "installing": "Installing...",
        },
    }

    def _e(text: str) -> str:
        return html.escape(str(text))

    class FHeta:
        def __init__(self):
            self.token = None
            self.uid = None
            self.sync_task = None
            self.config = None
            self.ssl = ssl.create_default_context()
            self.ssl.check_hostname = False
            self.ssl.verify_mode = ssl.CERT_NONE

        def _lang(self) -> str:
            return kernel.config.get("language", "ru")

        def _s(self, key: str, **kw) -> str:
            strings = STRINGS.get(self._lang(), STRINGS["ru"])
            text = strings.get(key, key)
            return text.format(**kw) if kw else text

        def _emoji(self, key: str) -> str:
            theme = (self.config and self.config.get("theme")) or "default"
            return THEMES.get(theme, THEMES["default"]).get(key, "")

        def _localise(self, value) -> str:
            if not value:
                return ""
            if isinstance(value, dict):
                return (
                    value.get(self._lang())
                    or value.get("doc")
                    or next(iter(value.values()), "")
                )
            return str(value)

        async def client_ready(self):
            me = await kernel.client.get_me()
            self.uid = me.id

            default_cfg = {
                "tracking": True,
                "only_official_developers": False,
                "theme": "default",
            }
            cfg_dict = await kernel.get_module_config(__name__, default_cfg)
            config = ModuleConfig(
                ConfigValue(
                    "tracking",
                    True,
                    description="Enable usage tracking",
                    validator=Boolean(default=True),
                ),
                ConfigValue(
                    "only_official_developers",
                    False,
                    description="Show only official developers modules",
                    validator=Boolean(default=False),
                ),
                ConfigValue(
                    "theme",
                    "default",
                    description="UI theme",
                    validator=Choice(
                        choices=["default", "winter", "summer", "spring", "autumn"],
                        default="default",
                    ),
                ),
            )
            config.from_dict(cfg_dict)
            await kernel.save_module_config(__name__, config.to_dict())
            kernel.store_module_config_schema(__name__, config)
            self.config = config

            if not self.token:
                self.token = await kernel.db_get("FHeta", "token")
                if not self.token:
                    try:
                        async with kernel.client.conversation("@FHeta_robot") as conv:
                            await conv.send_message("/token")
                            resp = await conv.get_response(timeout=5)
                            self.token = resp.text.strip()
                            await kernel.db_set("FHeta", "token", self.token)
                    except Exception as e:
                        kernel.logger.error(f"FHeta: token fetch failed: {e}")

            if self.token and (self.sync_task is None or self.sync_task.done()):
                self.sync_task = asyncio.create_task(self._sync_loop())

        async def _sync_loop(self):
            tracked = True
            timeout = aiohttp.ClientTimeout(total=5)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                while True:
                    try:
                        if self.token:
                            if self.config.get("tracking", True) is not False:
                                async with session.post(
                                    "https://api.fixyres.com/dataset",
                                    params={"user_id": self.uid, "lang": self._lang()},
                                    headers={"Authorization": self.token},
                                    ssl=self.ssl,
                                ) as r:
                                    tracked = True
                                    await r.release()
                            elif tracked:
                                async with session.post(
                                    "https://api.fixyres.com/rmd",
                                    params={"user_id": self.uid},
                                    headers={"Authorization": self.token},
                                    ssl=self.ssl,
                                ) as r:
                                    tracked = False
                                    await r.release()
                    except:
                        pass
                    await asyncio.sleep(10)

        async def _get(self, endpoint: str, **params):
            try:
                async with aiohttp.ClientSession() as s:
                    async with s.get(
                        f"https://api.fixyres.com/{endpoint}",
                        params=params,
                        headers={"Authorization": self.token},
                        ssl=self.ssl,
                        timeout=aiohttp.ClientTimeout(total=180),
                    ) as r:
                        return await r.json() if r.status == 200 else {}
            except Exception as e:
                kernel.logger.error(f"FHeta API GET: {e}")
                return {}

        async def _post(self, endpoint: str, payload=None, **params):
            try:
                async with aiohttp.ClientSession() as s:
                    async with s.post(
                        f"https://api.fixyres.com/{endpoint}",
                        json=payload,
                        params=params,
                        headers={"Authorization": self.token},
                        ssl=self.ssl,
                        timeout=aiohttp.ClientTimeout(total=180),
                    ) as r:
                        return await r.json() if r.status == 200 else {}
            except Exception as e:
                kernel.logger.error(f"FHeta API POST: {e}")
                return {}

        def _url(self, install: str) -> str:
            s = unquote(str(install or "")).strip()
            for pfx in ("dlmod ", "dlm ", "loadmod "):
                if s.lower().startswith(pfx):
                    return s[len(pfx) :]
            return s

        def _render(self, items: list, kind: str, char_limit: int) -> str:
            """Port of FHetaUI.render() for commands / placeholders."""
            if not items:
                return ""

            lang = self._lang()
            prefix = kernel.custom_prefix
            title_key = "commands" if kind == "cmd" else "placeholders"
            more_key = "morecommands" if kind == "cmd" else "moreplaceholders"
            emoji_key = "command" if kind == "cmd" else "placeholder"

            lines = []
            for i, item in enumerate(items):
                raw_desc = item.get("description", {})
                if isinstance(raw_desc, dict):
                    raw_desc = raw_desc.get(lang) or raw_desc.get("doc") or ""
                desc = _e(str(raw_desc).split("\n")[0]) if raw_desc else ""
                name = _e(item.get("name", ""))

                if kind == "cmd":
                    bot_user = kernel.config.get("inline_bot_username", "bot")
                    char = f"@{bot_user} " if item.get("inline") else prefix
                    row = f"<code>{char}{name}</code> {desc}".strip()
                else:
                    row = f"<code>{{{name}}}</code> {desc}".strip()

                extra = f"<i>{self._s(more_key, remaining=len(items) - i)}</i>"
                test = "\n".join(lines + [row, extra])
                if len(re.sub(r"<[^>]+>", "", test)) > char_limit and i > 0:
                    lines.append(extra)
                    break
                lines.append(row)

            body = "\n".join(lines)
            return (
                f"\n\n{self._emoji(emoji_key)} "
                f"<b>{self._s(title_key)}:</b>\n"
                f"<blockquote expandable>{body}</blockquote>"
            )

        def _fmt(self, mod: dict, query: str = "", idx: int = 1, total: int = 1) -> str:
            """Port of FHetaUI.format() - identical layout to official FHeta."""
            limit = 3700
            name = _e(mod.get("name", ""))
            author = _e(mod.get("author", "???"))
            version = mod.get("version", "?.?.?")

            text = (
                f"{self._emoji('module')} "
                f"<code>{name}</code> "
                f"<b>{self._s('author')}</b> "
                f"<code>{author}</code>"
            )
            if version not in ("?.?.?", None, ""):
                text += f" (<code>v{_e(str(version))}</code>)"

            desc = self._localise(mod.get("description"))
            if desc:
                text += (
                    f"\n\n{self._emoji('description')} "
                    f"<b>{self._s('description')}:</b>\n"
                    f"<blockquote expandable>{_e(str(desc))}</blockquote>"
                )

            plain_len = len(re.sub(r"<[^>]+>", "", text))
            text += self._render(mod.get("commands", []), "cmd", limit - plain_len)
            plain_len = len(re.sub(r"<[^>]+>", "", text))
            text += self._render(mod.get("placeholders", []), "ph", limit - plain_len)

            return text

        def _mk_btns(
            self, install: str, stats: dict, idx: int, mods=None, query: str = ""
        ) -> list:
            url = self._url(install)
            buttons = []

            if url:
                buttons.append(
                    [
                        make_cb_button(
                            kernel,
                            self._s("install"),
                            self._cb_install,
                            args=[url, idx, mods, query],
                            ttl=3600,
                        ),
                        Button.url(self._s("code"), url),
                    ]
                )

            like_row = [
                make_cb_button(
                    kernel,
                    f"↑ {stats.get('likes', 0)}",
                    self._cb_rate,
                    args=[install, "like", idx, mods, query],
                    ttl=3600,
                ),
                make_cb_button(
                    kernel,
                    f"↓ {stats.get('dislikes', 0)}",
                    self._cb_rate,
                    args=[install, "dislike", idx, mods, query],
                    ttl=3600,
                ),
            ]
            if mods and len(mods) > 1:
                counter_btn = make_cb_button(
                    kernel,
                    self._s("counter", idx=idx + 1, total=len(mods)),
                    self._cb_show,
                    args=[idx, mods, query],
                    ttl=3600,
                )
                like_row.insert(1, counter_btn)  # between ↑ and ↓
            buttons.append(like_row)

            if mods and len(mods) > 1:
                nav = []
                if idx > 0:
                    nav.append(
                        make_cb_button(
                            kernel,
                            "←",
                            self._cb_nav,
                            args=[idx - 1, mods, query],
                            ttl=3600,
                        )
                    )
                if idx < len(mods) - 1:
                    nav.append(
                        make_cb_button(
                            kernel,
                            "→",
                            self._cb_nav,
                            args=[idx + 1, mods, query],
                            ttl=3600,
                        )
                    )
                if nav:
                    buttons.append(nav)

            return buttons

        def _mk_list_btns(
            self, mods: list, query: str, page: int = 0, current: int = 0
        ) -> list:
            buttons = []
            start = page * 8
            end = min(start + 8, len(mods))

            for i in range(start, end):
                m = mods[i]
                buttons.append(
                    [
                        make_cb_button(
                            kernel,
                            f"{i + 1}. {_e(m.get('name', 'Unknown'))} by {_e(m.get('author', '???'))}",
                            self._cb_nav,
                            args=[i, mods, query],
                            ttl=3600,
                        )
                    ]
                )

            total_pages = (len(mods) + 7) // 8
            nav = []
            if page > 0:
                nav.append(
                    make_cb_button(
                        kernel,
                        "←",
                        self._cb_page,
                        args=[page - 1, mods, query, current],
                        ttl=3600,
                    )
                )
            if page < total_pages - 1:
                nav.append(
                    make_cb_button(
                        kernel,
                        "→",
                        self._cb_page,
                        args=[page + 1, mods, query, current],
                        ttl=3600,
                    )
                )
            if nav:
                buttons.append(nav)

            buttons.append(
                [
                    make_cb_button(
                        kernel,
                        "✘",
                        self._cb_nav,
                        args=[current, mods, query],
                        ttl=3600,
                    )
                ]
            )
            return buttons

        @staticmethod
        async def _answer(event, text: str = "", alert: bool = False):
            try:
                await event.answer(text, alert=alert) if text else await event.answer()
            except:
                pass

        async def _cb_rate(self, event, install, action, idx, mods, query=""):
            await self._answer(event)

            result = await self._post(f"rate/{self.uid}/{install}/{action}")
            stats_r = await self._post("get", payload=[install])
            stats = stats_r.get(install, {"likes": 0, "dislikes": 0})

            if mods and 0 <= idx < len(mods):
                mods[idx].update(stats)

            try:
                await event.edit(
                    buttons=self._mk_btns(install, stats, idx, mods, query)
                )
            except:
                pass

            if result and result.get("status"):
                st = result["status"]
                toast = (
                    self._s("added")
                    if st == "added"
                    else (
                        self._s("changed")
                        if st == "changed"
                        else self._s("deleted") if st == "removed" else ""
                    )
                )
                if toast:
                    await self._answer(event, toast, alert=True)

        async def _cb_nav(self, event, idx, mods, query=""):
            await self._answer(event)

            if not mods or not (0 <= idx < len(mods)):
                return

            mod = mods[idx]
            install = mod.get("install", "")
            stats = {
                "likes": mod.get("likes", 0),
                "dislikes": mod.get("dislikes", 0),
            }
            try:
                await event.edit(
                    self._fmt(mod, query, idx + 1, len(mods)),
                    parse_mode="html",
                    buttons=self._mk_btns(install, stats, idx, mods, query),
                )
            except:
                pass

        async def _cb_show(self, event, current_idx, mods, query=""):
            """Counter button → paginated module list."""
            await self._answer(event)
            text = f"{self._emoji('modules_list')} <b>{self._s('list')}</b>"
            try:
                await event.edit(
                    text,
                    parse_mode="html",
                    buttons=self._mk_list_btns(
                        mods, query, page=0, current=current_idx
                    ),
                )
            except:
                pass

        async def _cb_page(self, event, page, mods, query, current):
            """List pagination ← →."""
            await self._answer(event)
            text = f"{self._emoji('modules_list')} <b>{self._s('list')}</b>"
            try:
                await event.edit(
                    text,
                    parse_mode="html",
                    buttons=self._mk_list_btns(mods, query, page=page, current=current),
                )
            except:
                pass

        async def _cb_install(self, event, url, idx, mods, query=""):
            """Install via FHeta using kernel.install_from_url()."""
            try:
                await event.answer(self._s("installing"), alert=False)
            except:
                pass

            try:
                success, msg = await kernel.install_from_url(url)
                toast = (
                    self._s("success")
                    if success
                    else f"{self._s('error')}: {str(msg)[:80]}"
                )
            except Exception as exc:
                toast = f"{self._s('error')}: {str(exc)[:80]}"

            try:
                await event.answer(toast, alert=True)
            except:
                pass

    fheta = FHeta()

    async def _init():
        await fheta.client_ready()

    asyncio.create_task(_init())

    @kernel.register.command("fheta")
    async def fheta_cmd(event):
        """(args) - search heroku/hikka modules"""
        args = event.text.split(maxsplit=1)
        prefix = kernel.custom_prefix

        if len(args) < 2:
            return await event.edit(
                f"{fheta._emoji('error')} <b>{fheta._s('noquery', prefix=prefix)}</b>",
                parse_mode="html",
            )

        query = args[1]

        if len(query) > 168:
            return await event.edit(
                f"{fheta._emoji('warn')} <b>{fheta._s('toolong')}</b>",
                parse_mode="html",
            )

        if not kernel.is_bot_available():
            return await event.edit(
                f"{fheta._emoji('error')} <b>{fheta._s('inline_unavailable')}</b>",
                parse_mode="html",
            )

        bot_username = kernel.config.get("inline_bot_username")
        if not bot_username:
            return await event.edit(
                f"{fheta._emoji('error')} <b>{fheta._s('bot_not_configured')}</b>",
                parse_mode="html",
            )

        try:
            await event.edit(
                f"{fheta._emoji('search')} "
                f"<b>{fheta._s('search', query=_e(query))}</b>",
                parse_mode="html",
            )
            success, _ = await kernel.inline_query_and_click(
                chat_id=event.chat_id,
                query=f"fheta {query}",
                bot_username=bot_username,
                result_index=0,
                silent=False,
                reply_to=event.message.id,
            )
            if success:
                try:
                    await event.delete()
                except:
                    pass
            else:
                await event.edit(
                    f"{fheta._emoji('error')} <b>{fheta._s('search_failed')}</b>",
                    parse_mode="html",
                )
        except Exception as exc:
            await kernel.handle_error(exc, source="fheta_cmd", event=event)
            await event.edit(
                f"{fheta._emoji('error')} <b>{fheta._s('cmd_error')}</b>",
                parse_mode="html",
            )

    async def fheta_inline(event):
        """(query) inline search heroku/hikka modules"""
        raw = event.text.strip()
        query = (
            raw[6:].strip()
            if raw.lower().startswith("fheta ")
            else "" if raw.lower() == "fheta" else raw
        )

        if not query:
            await event.answer(
                [
                    event.builder.article(
                        title=fheta._s("prompt"),
                        text=fheta._s("prompt"),
                        description=fheta._s("hint"),
                    )
                ]
            )
            return

        if len(query) > 168:
            await event.answer(
                [
                    event.builder.article(
                        title=fheta._s("toolong"),
                        text=fheta._s("toolong"),
                        description=fheta._s("retry"),
                    )
                ]
            )
            return

        mods = await fheta._get(
            "search",
            query=query,
            inline="true",
            token=fheta.token,
            user_id=fheta.uid,
            ood=str(fheta.config.get("only_official_developers") or False).lower(),
        )

        if not mods or not isinstance(mods, list):
            await event.answer(
                [
                    event.builder.article(
                        title=fheta._s("retry"),
                        text=fheta._s("notfound", query=query),
                        description=fheta._s("retry"),
                    )
                ]
            )
            return

        results = []
        for idx, mod in enumerate(mods[:50]):
            stats = {"likes": mod.get("likes", 0), "dislikes": mod.get("dislikes", 0)}
            install = mod.get("install", "")
            text = fheta._fmt(mod, query, idx + 1, len(mods))
            buttons = fheta._mk_btns(install, stats, idx, mods, query)
            desc = fheta._localise(mod.get("description", ""))

            results.append(
                event.builder.article(
                    title=_e(mod.get("name", "")),
                    text=text,
                    parse_mode="html",
                    buttons=buttons,
                    description=_e(str(desc))[:100],
                )
            )

        await event.answer(results)

    kernel.register_inline_handler("fheta", fheta_inline)
