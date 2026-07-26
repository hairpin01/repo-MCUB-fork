from __future__ import annotations

from contextlib import suppress
from typing import Any


class VectorInputButtonHandlerMixin:

    def _discussion_reply_input_button(self, uid: str):
        return self.Button.input(
            self.strings["v_btn_wrt"],
            self._on_discussion_reply_input,
            placeholder=self.strings("v_rep_ask"),
            data=str(uid),
            style="primary",
        )

    def _find_discussion_target(self, uid: str) -> tuple[str, str]:
        uid = str(uid or "").strip()
        if not uid:
            return "", ""
        for group in self._cached_groups.values():
            for mod in group:
                mod_uid = self._norm_hash_name(
                    f"{mod.get('owner', '')}|{mod.get('name', '')}"
                )
                if mod_uid == uid:
                    return mod.get("owner", ""), mod.get("name", "")
        return "", ""

    async def _answer_discussion_input(self, event: Any, text: str, *, alert: bool = False) -> None:
        with suppress(Exception):
            await event.answer(text, alert=alert)

    async def _on_discussion_reply_input(self, event: Any, text: str, uid: str) -> None:
        reply = (text or "").strip()
        if len(reply) < 2:
            await self._answer_discussion_input(event, self.strings("v_rep_min"), alert=True)
            return
        if len(reply) > 1800:
            await self._answer_discussion_input(event, self.strings("v_rep_max"), alert=True)
            return

        owner, name = self._find_discussion_target(uid)
        if not owner or not name:
            await self._answer_discussion_input(event, self.strings("v_rep_err"), alert=True)
            return

        ok = await self._post_discussion(owner, name, reply)
        await self._answer_discussion_input(
            event,
            self.strings("v_rep_ok" if ok else "v_rep_err"),
            alert=not ok,
        )
