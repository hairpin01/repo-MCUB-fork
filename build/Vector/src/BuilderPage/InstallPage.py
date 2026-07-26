from __future__ import annotations

import logging

# local
from ..Const import _ILog

LOG = logging.getLogger("VectorMonolith")


class VectorInstallPageMixin:
    async def _safe_install(
        self, module_name: str, dl_url: str, notify: bool = True
    ) -> tuple[int, list[dict]]:
        LOG.info("_safe_install: %s from %s", module_name, dl_url)
        try:
            ihandler = _ILog()
            ihandler.setLevel(logging.WARNING)
            root = logging.getLogger()
            root.addHandler(ihandler)
            try:
                success, msg = await self.kernel.install_from_url(dl_url, module_name)
                LOG.info("_safe_install: success=%s msg=%s", success, msg)
                return (
                    (1, [])
                    if success
                    else (0, self._classify_install_errors(ihandler.records))
                )
            finally:
                root.removeHandler(ihandler)
        except Exception as e:
            LOG.error("_safe_install: exception: %r", e)
            return -1, []

    def _classify_install_errors(
        self, records: list[logging.LogRecord]
    ) -> list[dict[str, str]]:
        errors = []
        for rec in records:
            if rec.levelno < logging.WARNING:
                continue
            msg = rec.getMessage()
            for err_type, pattern in self._ierrs:
                m = pattern.search(msg)
                if m:
                    detail = m.group(1).strip() if m.lastindex else ""
                    if err_type == "core_overwrite":
                        detail = f"{m.group(1)}.{m.group(2)}"
                    elif err_type == "heroku_min":
                        detail = f"{m.group(1)} (current: {m.group(2)})"
                    errors.append({"type": err_type, "detail": detail, "raw": msg})
                    break
            else:
                if rec.levelno >= logging.ERROR:
                    errors.append({"type": "unknown", "detail": msg[:200], "raw": msg})
        return errors

    def _fmt_install_errors(self, m_name: str, errors: list[dict[str, str]]) -> str:
        if not errors:
            return f"{self.ICONS['error']} <b>{self.strings('v_dl_err')}</b>"
        lines = [
            f"{self.ICONS['broken']} <b>{self.strings('v_install_log_hdr', name=m_name)}</b>"
        ]
        seen = set()
        for err in errors:
            key = err["type"]
            if key in seen:
                continue
            seen.add(key)
            detail = err["detail"]
            fmt = self.strings.get(f"v_install_fail_{key}")
            if fmt:
                try:
                    lines.append(f"{self.ICONS['warn']} {fmt.format(detail=detail)}")
                except (KeyError, ValueError):
                    lines.append(f"{self.ICONS['warn']} {fmt}")
            else:
                lines.append(f"{self.ICONS['warn']} {key}: {detail}")
        return "\n".join(lines)
