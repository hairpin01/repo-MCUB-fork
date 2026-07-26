from __future__ import annotations

# local
from ..Const import _esc


class VectorAntiVirusPageMixin:
    def _build_sec_html(self, item: dict, payload: dict | None) -> str:
        name = item.get("name", "?")
        if not payload:
            return f"{self.ICONS['shield']} <b>{_esc(name)}</b>\n\n{self.strings('v_aud_none')}"
        scan = payload.get("check") or payload
        details = scan.get("details", {})
        static = details.get("static", {})
        verdict = scan.get("verdict") or scan.get("threat_level") or "unknown"
        emoji_map = {
            "safe": self.ICONS["safe"],
            "unknown": self.ICONS["warn"],
            "malicious": self.ICONS["error"],
            "critical": self.ICONS["error"],
        }
        lines = [
            f"{emoji_map.get(verdict, self.ICONS['warn'])} <b>{self.strings('v_aud_lvl')}: {_esc(verdict.upper())}</b>"
        ]
        sigs = static.get("signatures") or scan.get("signatures") or []
        if sigs:
            crit = [s for s in sigs if s.get("severity") == "critical"]
            warn_s = [s for s in sigs if s.get("severity") == "warning"]
            info_s = [s for s in sigs if s.get("severity") == "info"]
            lines.append(f"\n{self.ICONS['shield']} {self.strings('v_aud_sigs')}:")
            if crit:
                lines.append(
                    f"  {self.ICONS['error']} {self.strings('v_sig_crit')}: {len(crit)}"
                )
                for s in crit[:3]:
                    lines.append(f"    \u2022 {s.get('name', s.get('rule', '?'))}")
            if warn_s:
                lines.append(
                    f"  {self.ICONS['warn']} {self.strings('v_sig_warn')}: {len(warn_s)}"
                )
                for s in warn_s[:3]:
                    lines.append(f"    \u2022 {s.get('name', s.get('rule', '?'))}")
            if info_s:
                lines.append(
                    f"  {self.ICONS['info']} {self.strings('v_sig_info')}: {len(info_s)}"
                )
        summary = scan.get("summary") or static.get("summary") or ""
        if summary:
            lines.append(
                f"\n{self.ICONS['info']} {self.strings('v_aud_out')}: {_esc(str(summary)[:300])}"
            )
        if not sigs and not summary:
            lines.append(f"\n{self.strings('v_aud_no_txt')}")
        return "\n".join(lines)

    def _build_sec_kbd(
        self, item: dict, i: int, group: list | None, q: str, has_run: bool
    ) -> list:
        name, owner = item.get("name", "?"), item.get("owner", "?")
        gl = len(group) if group else 1
        kbd = []
        if not has_run:
            kbd.append(
                [
                    self.Button.inline(
                        self.strings["v_btn_aud_run"],
                        self.cb_scan_go,
                        data=self._cb_data(
                            "scan_go", owner=owner, name=name, i=i, gl=gl, q=q
                        ),
                    )
                ]
            )
        kbd.append(
            [
                self.Button.inline(
                    self.strings["v_btn_bck"],
                    self.cb_list,
                    data=self._cb_data("list", i=i, gl=gl, q=q),
                )
            ]
        )
        return kbd
