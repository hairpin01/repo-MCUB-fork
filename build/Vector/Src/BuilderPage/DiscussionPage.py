from __future__ import annotations

# local
from ..Const import _esc


class VectorDiscussionPageMixin:
    def _build_discussion_html(
        self, data: dict | None, name: str, emoji: str = "\U0001f4ac"
    ) -> str:
        if not data:
            return f"{emoji} <b>{self.strings('v_talk_hdr', emoji=emoji, name=_esc(name))}</b>\n\n{self.strings('v_talk_err')}"
        posts = data.get("posts") or data.get("messages") or []
        if not posts:
            return f"{emoji} <b>{self.strings('v_talk_hdr', emoji=emoji, name=_esc(name))}</b>\n{self.strings('v_talk_desc')}\n\n{self.strings('v_talk_0')}"
        lines = [
            f"{emoji} <b>{self.strings('v_talk_hdr', emoji=emoji, name=_esc(name))}</b>",
            f"{self.strings('v_talk_desc')}",
            f"{self.strings('v_talk_num', count=len(posts))}",
            "",
        ]
        for p in posts[:20]:
            author = p.get("author") or p.get("user") or "?"
            text = p.get("text") or p.get("content") or "..."
            ts = p.get("timestamp") or p.get("date") or ""
            lines.append(f"<b>{_esc(str(author))}</b>: {_esc(str(text)[:200])}")
            if ts:
                lines.append(f"<i>{ts}</i>")
            lines.append("")
        if len(posts) > 20:
            lines.append(self.strings("v_more_comments"))
        return "\n".join(lines)

    def _build_discussion_kbd(
        self, owner: str, name: str, i: int, gl: int, q: str
    ) -> list:
        uid = self._norm_hash_name(f"{owner}|{name}")
        return [
            [
                self._discussion_reply_input_button(uid),
                self.Button.inline(
                    self.strings["v_btn_bck"],
                    self.cb_list,
                    data=self._cb_data("list", i=i, gl=gl, q=q),
                ),
            ]
        ]
