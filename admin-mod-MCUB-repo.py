from __future__ import annotations
import json
import re
from datetime import datetime, timedelta, timezone

UTC = timezone.utc
from typing import Any
from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, PeerUser
from core.lib.loader.module_base import ModuleBase, command


def _parse_duration(s: str) -> timedelta | None:
    m = re.fullmatch(r"(\d+)(min|h|d|w|m)", s.strip())
    if not m:
        return None
    v, u = int(m.group(1)), m.group(2)
    return {
        "min": timedelta(minutes=v),
        "h": timedelta(hours=v),
        "d": timedelta(days=v),
        "w": timedelta(weeks=v),
        "m": timedelta(days=v * 30),
    }[u]


def _fmt_duration(td: timedelta) -> str:
    s = int(td.total_seconds())
    if s < 60:
        return f"{s}s"
    if s < 3600:
        return f"{s // 60}min"
    if s < 86400:
        return f"{s // 3600}h"
    if s < 604800:
        return f"{s // 86400}d"
    return f"{s // 604800}w"


class Admin(ModuleBase):
    name = "AdminMod"
    version = "1.0.0"
    author = "@rich_beluga"
    description = {
        "ru": "Инструменты администратора: мут, бан, варн и др.",
        "en": "Admin tools: mute, ban, warn, and more.",
    }

    MAX_WARNS: int = 3

    strings = {
        "ru": {
            "no_target": '<blockquote><tg-emoji emoji-id="5260342697075416641">❌</tg-emoji> Укажи цель: ответь на сообщение или укажи @username/ID.</blockquote>',
            "no_duration": '<blockquote><tg-emoji emoji-id="5260342697075416641">❌</tg-emoji> Укажи срок (например: <code>1h</code>, <code>30min</code>, <code>2d</code>).</blockquote>',
            "invalid_duration": '<blockquote><tg-emoji emoji-id="5260342697075416641">❌</tg-emoji> Неверный формат времени.\nПримеры: <code>1min</code>, <code>2h</code>, <code>3d</code>, <code>1w</code>, <code>1m</code>.</blockquote>',
            "not_a_group": '<blockquote><tg-emoji emoji-id="5260342697075416641">❌</tg-emoji> Команда работает только в группах/супергруппах.</blockquote>',
            "user_not_found": '<blockquote><tg-emoji emoji-id="5260342697075416641">❌</tg-emoji> Пользователь не найден.</blockquote>',
            "error": '<blockquote><tg-emoji emoji-id="5260342697075416641">❌</tg-emoji> Ошибка: <code>{err}</code></blockquote>',
            "muted": '<blockquote><tg-emoji emoji-id="5258267368877989660">🔇</tg-emoji> <code>{user}</code> замучен на <code>{duration}</code>.\n<tg-emoji emoji-id="6010374833135688013">😵‍💫</tg-emoji> <b>Причина:<b> <code>{reason}</code></blockquote>',
            "muted_perm": '<blockquote><tg-emoji emoji-id="5258267368877989660">🔇</tg-emoji> <code>{user}</code> замучен навсегда.\n<tg-emoji emoji-id="6010374833135688013">😵‍💫</tg-emoji> <b>Причина:<b> <code>{reason}</code></blockquote>',
            "unmuted": '<blockquote><tg-emoji emoji-id="5260325873688518261">🔊</tg-emoji> <code>{user}</code> размучен.</blockquote>',
            "banned": '<blockquote><tg-emoji emoji-id="5275969776668134187">⛔️</tg-emoji> <code>{user}</code> забанен на <code>{duration}</code>.\n<tg-emoji emoji-id="6010374833135688013">😵‍💫</tg-emoji> <b>Причина:<b> <code>{reason}</code></blockquote>',
            "banned_perm": '<blockquote><tg-emoji emoji-id="5275969776668134187">⛔️</tg-emoji> <code>{user}</code> забанен навсегда.\n<tg-emoji emoji-id="6010374833135688013">😵‍💫</tg-emoji> <b>Причина:<b> <code>{reason}</code></blockquote>',
            "unbanned": '<blockquote><tg-emoji emoji-id="5260726538302660868">✅</tg-emoji> <code>{user}</code> разбанен.</blockquote>',
            "warned": '<blockquote><tg-emoji emoji-id="5258474669769497337">❗️</tg-emoji> <code>{user}</code> получает предупреждение ({count}/{max}).\n<tg-emoji emoji-id="6010374833135688013">😵‍💫</tg-emoji> <b>Причина:<b> <code>{reason}</code></blockquote>',
            "warned_autoban": '<blockquote><tg-emoji emoji-id="5275969776668134187">⛔️</tg-emoji> <code>{user}</code> — {count}/{max} предупреждений, выдан перманентный бан!\n<tg-emoji emoji-id="6010374833135688013">😵‍💫</tg-emoji> <b>Причина:<b> <code>{reason}</code></blockquote>',
            "warn_removed": '<blockquote><tg-emoji emoji-id="5260726538302660868">✅</tg-emoji> С <code>{user}</code> снято {removed} предупр. Осталось: <b>{count}</b>/{max}.</blockquote>',
            "no_warns": '<blockquote><tg-emoji emoji-id="5429571366384842791">🔎</tg-emoji> У <code>{user}</code> нет предупреждений.</blockquote>',
            "kicked": '<blockquote><tg-emoji emoji-id="5260726538302660868">👢</tg-emoji> <code>{user}</code> кикнут из чата.\n<tg-emoji emoji-id="6010374833135688013">😵‍💫</tg-emoji> <b>Причина:<b> <code>{reason}</code></blockquote>',
            "clean_start": '<blockquote><tg-emoji emoji-id="5429571366384842791">🔎</tg-emoji> Ищу удалённые аккаунты...</blockquote>',
            "clean_none": '<blockquote><tg-emoji emoji-id="5260726538302660868">✅</tg-emoji> Удалённых аккаунтов не найдено.</blockquote>',
            "clean_done": '<blockquote><tg-emoji emoji-id="5260726538302660868">🧹</tg-emoji> Удалено аккаунтов: <b>{removed}</b> из <b>{total}</b> найденных.</blockquote>',
        },
        "en": {
            "no_target": '<blockquote><tg-emoji emoji-id="5260342697075416641">❌</tg-emoji> Specify a target: reply to a message or provide @username/ID.</blockquote>',
            "no_duration": '<blockquote><tg-emoji emoji-id="5260342697075416641">❌</tg-emoji> Specify a duration (e.g. <code>1h</code>, <code>30min</code>, <code>2d</code>).</blockquote>',
            "invalid_duration": '<blockquote><tg-emoji emoji-id="5260342697075416641">❌</tg-emoji> Invalid time format.\nExamples: <code>1min</code>, <code>2h</code>, <code>3d</code>, <code>1w</code>, <code>1m</code>.</blockquote>',
            "not_a_group": '<blockquote><tg-emoji emoji-id="5260342697075416641">❌</tg-emoji> This command only works in groups/supergroups.</blockquote>',
            "user_not_found": '<blockquote><tg-emoji emoji-id="5260342697075416641">❌</tg-emoji> User not found.</blockquote>',
            "error": '<blockquote><tg-emoji emoji-id="5260342697075416641">❌</tg-emoji> Error: <code>{err}</code></blockquote>',
            "muted": '<blockquote><tg-emoji emoji-id="5258267368877989660">🔇</tg-emoji> <code>{user}</code> muted for <code>{duration}</code>.\n<tg-emoji emoji-id="6010374833135688013">😵‍💫</tg-emoji> <b>Reason:<b> <code>{reason}</code></blockquote>',
            "muted_perm": '<blockquote><tg-emoji emoji-id="5258267368877989660">🔇</tg-emoji> <code>{user}</code> muted permanently.\n<tg-emoji emoji-id="6010374833135688013">😵‍💫</tg-emoji> <b>Reason:<b> <code>{reason}</code></blockquote>',
            "unmuted": '<blockquote><tg-emoji emoji-id="5260325873688518261">🔊</tg-emoji> <code>{user}</code> unmuted.</blockquote>',
            "banned": '<blockquote><tg-emoji emoji-id="5275969776668134187">⛔️</tg-emoji> <code>{user}</code> banned for <code>{duration}</code>.\n<tg-emoji emoji-id="6010374833135688013">😵‍💫</tg-emoji> <b>Reason:<b> <code>{reason}</code></blockquote>',
            "banned_perm": '<blockquote><tg-emoji emoji-id="5275969776668134187">⛔️</tg-emoji> <code>{user}</code> banned permanently.\n<tg-emoji emoji-id="6010374833135688013">😵‍💫</tg-emoji> <b>Reason:<b> <code>{reason}</code></blockquote>',
            "unbanned": '<blockquote><tg-emoji emoji-id="5260726538302660868">✅</tg-emoji> <code>{user}</code> unbanned.</blockquote>',
            "warned": '<blockquote><tg-emoji emoji-id="5258474669769497337">❗️</tg-emoji> <code>{user}</code> warned ({count}/{max}).\n<tg-emoji emoji-id="6010374833135688013">😵‍💫</tg-emoji> <b>Reason:<b> <code>{reason}</code></blockquote>',
            "warned_autoban": '<blockquote><tg-emoji emoji-id="5275969776668134187">⛔️</tg-emoji> <code>{user}</code> — {count}/{max} warnings, permanent ban issued!\n<tg-emoji emoji-id="6010374833135688013">😵‍💫</tg-emoji> <b>Reason:<b> <code>{reason}</code></blockquote>',
            "warn_removed": '<blockquote><tg-emoji emoji-id="5260726538302660868">✅</tg-emoji> Removed {removed} warning(s) from <code>{user}</code>. Left: <b>{count}</b>/{max}.</blockquote>',
            "no_warns": '<blockquote><tg-emoji emoji-id="5429571366384842791">🔎</tg-emoji> <code>{user}</code> has no warnings.</blockquote>',
            "kicked": '<blockquote><tg-emoji emoji-id="5260726538302660868">👢</tg-emoji> <code>{user}</code> kicked from chat.\n<tg-emoji emoji-id="6010374833135688013">😵‍💫</tg-emoji> <b>Reason:<b> <code>{reason}</code></blockquote>',
            "clean_start": '<blockquote><tg-emoji emoji-id="5429571366384842791">🔎</tg-emoji> Searching for deleted accounts...</blockquote>',
            "clean_none": '<blockquote><tg-emoji emoji-id="5260726538302660868">✅</tg-emoji> No deleted accounts found.</blockquote>',
            "clean_done": '<blockquote><tg-emoji emoji-id="5260726538302660868">🧹</tg-emoji> Removed accounts: <b>{removed}</b> of <b>{total}</b> found.</blockquote>',
        },
    }

    async def _resolve_target(
        self,
        event: events.NewMessage.Event,
        args: list[str],
    ) -> tuple[Any | None, list[str]]:
        if event.reply_to_msg_id:
            try:
                reply = await event.get_reply_message()
                if reply and reply.sender:
                    return reply.sender, args
            except Exception:
                pass

        if args:
            first = args[0]
            if first.startswith("@"):
                try:
                    return await self.client.get_entity(first), args[1:]
                except Exception:
                    return None, args
            if first.lstrip("-").isdigit():
                entity = await self._resolve_id(event, int(first))
                return entity, args[1:]

        return None, args

    async def _resolve_id(
        self,
        event: events.NewMessage.Event,
        uid: int,
    ) -> Any | None:
        try:
            return await self.client.get_entity(PeerUser(uid))
        except Exception:
            pass

        try:
            async for p in self.client.iter_participants(event.chat_id):
                if p.id == uid:
                    return p
        except Exception:
            pass

        return None

    def _user_link(self, user: Any) -> str:
        name = (
            getattr(user, "first_name", None)
            or getattr(user, "title", None)
            or str(user.id)
        )
        return f'<a href="tg://user?id={user.id}">{name}</a>'

    async def _get_warns(self, chat_id: int) -> dict[str, int]:
        raw = await self.db.db_get(self.name, f"warns_{chat_id}")
        if raw:
            try:
                return json.loads(raw)
            except Exception:
                pass
        return {}

    async def _save_warns(self, chat_id: int, data: dict[str, int]) -> None:
        await self.db.db_set(self.name, f"warns_{chat_id}", json.dumps(data))

    async def _edit(self, event: events.NewMessage.Event, text: str) -> None:
        await event.edit(text, parse_mode="html")

    @command(
        "mute",
        doc_ru="Замутить. Использование: mute {цель} {срок} {причина}",
        doc_en="Mute user. Usage: mute {target} {duration} {reason}",
    )
    async def cmd_mute(self, event: events.NewMessage.Event) -> None:
        if not event.is_group:
            await self._edit(event, self.strings["not_a_group"])
            return

        raw = self.args_raw(event).split()
        user, rest = await self._resolve_target(event, raw)

        if not user:
            await self._edit(event, self.strings["no_target"])
            return

        td: timedelta | None = None
        until: datetime | None = None
        reason = "—"

        if rest:
            td = _parse_duration(rest[0])
            if td:
                until = datetime.now(tz=timezone.utc) + td
                reason = " ".join(rest[1:]) or "—"
            else:
                reason = " ".join(rest) or "—"

        try:
            await self.client(EditBannedRequest(
                event.chat_id,
                user,
                ChatBannedRights(
                    until_date=until,
                    send_messages=True,
                    send_media=True,
                    send_stickers=True,
                    send_gifs=True,
                    send_games=True,
                    send_inline=True,
                    embed_links=True,
                ),
            ))
            if td:
                await self._edit(
                    event,
                    self.strings("muted",
                        user=self._user_link(user),
                        duration=_fmt_duration(td),
                        reason=reason,
                    ),
                )
            else:
                await self._edit(
                    event,
                    self.strings("muted_perm",
                        user=self._user_link(user),
                        reason=reason,
                    ),
                )
        except Exception as e:
            await self._edit(event, self.strings("error", err=str(e)))

    @command(
        "unmute",
        doc_ru="Размутить. Использование: unmute {цель}",
        doc_en="Unmute user. Usage: unmute {target}",
    )
    async def cmd_unmute(self, event: events.NewMessage.Event) -> None:
        """unmute {ID/@username/reply}"""
        if not event.is_group:
            await self._edit(event, self.strings["not_a_group"])
            return

        user, _ = await self._resolve_target(event, self.args_raw(event).split())
        if not user:
            await self._edit(event, self.strings["no_target"])
            return

        try:
            await self.client(
                EditBannedRequest(
                    event.chat_id,
                    user,
                    ChatBannedRights(until_date=None),
                )
            )
            await self._edit(event, self.strings("unmuted", user=self._user_link(user)))
        except Exception as e:
            await self._edit(event, self.strings("error", err=str(e)))

    @command(
        "ban",
        doc_ru="Забанить. Использование: ban {цель} [{срок}] {причина}",
        doc_en="Ban user. Usage: ban {target} [{duration}] {reason}",
    )
    async def cmd_ban(self, event: events.NewMessage.Event) -> None:
        """
        ban {ID/@username/reply} [{срок}] {причина}

        Если срок не указан — перманентный бан.
        """
        if not event.is_group:
            await self._edit(event, self.strings["not_a_group"])
            return

        raw = self.args_raw(event).split()
        user, rest = await self._resolve_target(event, raw)

        if not user:
            await self._edit(event, self.strings["no_target"])
            return

        td: timedelta | None = None
        until: datetime | None = None
        reason = "—"

        if rest:
            td = _parse_duration(rest[0])
            if td:
                until = datetime.now(tz=UTC) + td
                reason = " ".join(rest[1:]) or "—"
            else:
                reason = " ".join(rest) or "—"

        try:
            await self.client(
                EditBannedRequest(
                    event.chat_id,
                    user,
                    ChatBannedRights(until_date=until, view_messages=True),
                )
            )
            if td:
                await self._edit(
                    event,
                    self.strings(
                        "banned",
                        user=self._user_link(user),
                        duration=_fmt_duration(td),
                        reason=reason,
                    ),
                )
            else:
                await self._edit(
                    event,
                    self.strings(
                        "banned_perm",
                        user=self._user_link(user),
                        reason=reason,
                    ),
                )
        except Exception as e:
            await self._edit(event, self.strings("error", err=str(e)))

    @command(
        "unban",
        doc_ru="Разбанить. Использование: unban {цель}",
        doc_en="Unban user. Usage: unban {target}",
    )
    async def cmd_unban(self, event: events.NewMessage.Event) -> None:
        """unban {ID/@username/reply}"""
        if not event.is_group:
            await self._edit(event, self.strings["not_a_group"])
            return

        user, _ = await self._resolve_target(event, self.args_raw(event).split())
        if not user:
            await self._edit(event, self.strings["no_target"])
            return

        try:
            await self.client(
                EditBannedRequest(
                    event.chat_id,
                    user,
                    ChatBannedRights(until_date=None),
                )
            )
            await self._edit(
                event, self.strings("unbanned", user=self._user_link(user))
            )
        except Exception as e:
            await self._edit(event, self.strings("error", err=str(e)))

    @command(
        "warn",
        doc_ru="Предупредить. Использование: warn {цель} {причина}",
        doc_en="Warn user. Usage: warn {target} {reason}",
    )
    async def cmd_warn(self, event: events.NewMessage.Event) -> None:
        """
        warn {ID/@username/reply} {причина}

        При достижении MAX_WARNS — автоматический перманентный бан.
        """
        if not event.is_group:
            await self._edit(event, self.strings["not_a_group"])
            return

        raw = self.args_raw(event).split()
        user, rest = await self._resolve_target(event, raw)

        if not user:
            await self._edit(event, self.strings["no_target"])
            return

        reason = " ".join(rest) or "—"
        warns = await self._get_warns(event.chat_id)
        uid = str(user.id)
        warns[uid] = warns.get(uid, 0) + 1
        await self._save_warns(event.chat_id, warns)

        count = warns[uid]
        if count >= self.MAX_WARNS:
            # Auto-ban on limit
            try:
                await self.client(
                    EditBannedRequest(
                        event.chat_id,
                        user,
                        ChatBannedRights(until_date=None, view_messages=True),
                    )
                )
            except Exception:
                pass
            await self._edit(
                event,
                self.strings(
                    "warned_autoban",
                    user=self._user_link(user),
                    count=count,
                    max=self.MAX_WARNS,
                    reason=reason,
                ),
            )
        else:
            await self._edit(
                event,
                self.strings(
                    "warned",
                    user=self._user_link(user),
                    count=count,
                    max=self.MAX_WARNS,
                    reason=reason,
                ),
            )

    @command(
        "unwarn",
        doc_ru="Снять варны. Использование: unwarn {цель} [{количество}]",
        doc_en="Remove warns. Usage: unwarn {target} [{count}]",
    )
    async def cmd_unwarn(self, event: events.NewMessage.Event) -> None:
        """
        unwarn {ID/@username/reply} [{количество}]

        Если количество не указано — снимается 1 варн.
        """
        if not event.is_group:
            await self._edit(event, self.strings["not_a_group"])
            return

        raw = self.args_raw(event).split()
        user, rest = await self._resolve_target(event, raw)

        if not user:
            await self._edit(event, self.strings["no_target"])
            return

        to_remove = 1
        if rest and rest[0].isdigit():
            to_remove = max(1, int(rest[0]))

        warns = await self._get_warns(event.chat_id)
        uid = str(user.id)
        current = warns.get(uid, 0)

        if current == 0:
            await self._edit(
                event, self.strings("no_warns", user=self._user_link(user))
            )
            return

        removed = min(to_remove, current)
        warns[uid] = current - removed
        if warns[uid] <= 0:
            del warns[uid]

        await self._save_warns(event.chat_id, warns)
        await self._edit(
            event,
            self.strings(
                "warn_removed",
                user=self._user_link(user),
                removed=removed,
                count=warns.get(uid, 0),
                max=self.MAX_WARNS,
            ),
        )

    @command(
        "kick",
        doc_ru="Кикнуть пользователя. Использование: kick {цель} [причина]",
        doc_en="Kick user. Usage: kick {target} [reason]",
    )
    async def cmd_kick(self, event: events.NewMessage.Event) -> None:
        """
        kick {ID/@username/reply} [причина]

        Кикает пользователя из группы без бана (бан + немедленный разбан).
        """
        if not event.is_group:
            await self._edit(event, self.strings["not_a_group"])
            return

        raw = self.args_raw(event).split()
        user, rest = await self._resolve_target(event, raw)

        if not user:
            await self._edit(event, self.strings["no_target"])
            return

        reason = " ".join(rest) or "—"

        try:
            await self.client(
                EditBannedRequest(
                    event.chat_id,
                    user,
                    ChatBannedRights(until_date=None, view_messages=True),
                )
            )
            await self.client(
                EditBannedRequest(
                    event.chat_id,
                    user,
                    ChatBannedRights(until_date=None),
                )
            )
            await self._edit(
                event,
                self.strings(
                    "kicked",
                    user=self._user_link(user),
                    reason=reason,
                ),
            )
        except Exception as e:
            await self._edit(event, self.strings("error", err=str(e)))

    @command(
        "cleandeleted",
        alias=["cleandel", "cleanup"],
        doc_ru="Удалить из группы все удалённые аккаунты.",
        doc_en="Remove all deleted accounts from the group.",
    )
    async def cmd_cleandeleted(self, event: events.NewMessage.Event) -> None:
        """
        cleandeleted

        Сканирует участников и кикает все удалённые (deleted) аккаунты.
        """
        if not event.is_group:
            await self._edit(event, self.strings["not_a_group"])
            return

        await self._edit(event, self.strings["clean_start"])

        deleted: list[Any] = []
        try:
            async for p in self.client.iter_participants(event.chat_id):
                if getattr(p, "deleted", False):
                    deleted.append(p)
        except Exception as e:
            await self._edit(event, self.strings("error", err=str(e)))
            return

        if not deleted:
            await self._edit(event, self.strings["clean_none"])
            return

        removed = 0
        for user in deleted:
            try:
                await self.client(
                    EditBannedRequest(
                        event.chat_id,
                        user,
                        ChatBannedRights(until_date=None, view_messages=True),
                    )
                )
                await self.client(
                    EditBannedRequest(
                        event.chat_id,
                        user,
                        ChatBannedRights(until_date=None),
                    )
                )
                removed += 1
            except Exception:
                continue

        await self._edit(
            event,
            self.strings("clean_done", removed=removed, total=len(deleted)),
        )

    async def on_load(self) -> None:
        self.log.info(f"{self.name} v{self.version} by {self.author} — loaded")
