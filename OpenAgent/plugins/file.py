# scop: inline
# SPDX-License-Identifier: MIT

from __future__ import annotations

from pathlib import Path
from typing import Any


class FilePlugin:
    name = "file"
    version = "0.3.0"
    author = "@dev_dolbaeb"
    description = "File send/read/download/edit/write/patch tools"

    tool_registry = (
        "file.send",
        "file.download_media",
        "file.read_text",
        "file.write",
        "file.edit",
        "file.patch",
    )

    dangerous_tools = {"file.send", "file.download_media", "file.write", "file.edit", "file.patch"}

    tool_docs = {
        "file.send": {"desc": "Send a file from disk to a Telegram chat", "args": "path (str) or file (str); chat (str) — target; caption (str)", "body": "file path"},
        "file.download_media": {"desc": "Download media from a Telegram message", "args": "message (str) or msg (str) — message ID; chat (str) or from (str)", "body": "not used"},
        "file.read_text": {"desc": "Read a text file (UTF-8, first 12k chars)", "args": "path (str) or file (str) or name (str)", "body": "file path"},
        "file.write": {"desc": "Write or append content to a file", "args": "path (str) — file; mode (str) — 'overwrite' or 'append'", "body": "content to write"},
        "file.edit": {"desc": "Search and replace text in a file", "args": "path (str); search (str); replace (str); count (int)", "body": "'search -> replace' format"},
        "file.patch": {"desc": "Apply a unified diff to a file", "args": "path (str); reverse (str) — 'true' to reverse", "body": "unified diff content"},
    }

    tool_map = {
        "send_file": "cmd_send",
        "file.send": "cmd_send",
        "download_media": "cmd_download",
        "file.download": "cmd_download",
        "file.download_media": "cmd_download",
        "file.read_text": "cmd_read_text",
        "file.write": "cmd_write",
        "file.edit": "cmd_edit",
        "file.patch": "cmd_patch",
    }

    def __init__(self, agent: Any) -> None:
        self.agent = agent

    def _resolve_path(self, path_str: str) -> Path:
        fpath = Path(path_str).expanduser()
        if not fpath.is_absolute():
            fpath = Path.cwd() / fpath
        return fpath

    async def cmd_send(self, attrs_raw: str, body: str, source_event: Any) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        path_str = attrs.get("path") or attrs.get("file") or body.strip()
        caption = attrs.get("caption") or ""
        chat = await self.agent._resolve_tool_chat(attrs.get("chat") or attrs.get("to"), source_event)
        if not path_str:
            return "File path is required"
        fpath = self._resolve_path(path_str)
        if not fpath.is_file():
            return f"File not found: {fpath}"
        try:
            await self.agent.client.send_file(chat, str(fpath), caption=caption or None)
            return f"File sent: {fpath.name}"
        except Exception as exc:
            return f"Send failed: {exc}"

    async def cmd_download(self, attrs_raw: str, body: str, source_event: Any) -> str:
        import io
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        msg_id = attrs.get("message") or attrs.get("msg") or body.strip()
        chat = await self.agent._resolve_tool_chat(attrs.get("chat") or attrs.get("from"), source_event)
        try:
            if msg_id and msg_id.isdigit():
                msg = await self.agent.client.get_messages(chat, ids=int(msg_id))
            else:
                msg = await source_event.get_reply_message() if source_event else None
            if not msg or not msg.media:
                return "No media found"
            data = await msg.download_media(file=bytes)
            if data is None:
                return "Download returned no data"
            size_mb = len(data) / (1024 * 1024)
            return f"Downloaded: {size_mb:.2f} MB. Format: {type(data).__name__}"
        except Exception as exc:
            return f"Download failed: {exc}"

    async def cmd_read_text(self, attrs_raw: str, body: str) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        path_raw = body.strip() or attrs.get("path") or attrs.get("file") or attrs.get("name") or ""
        if not path_raw:
            return "File path is required"
        fpath = self._resolve_path(path_raw)
        try:
            if not fpath.is_file():
                return f"File not found: {fpath}"
            return fpath.read_text(encoding="utf-8", errors="replace")[:12000]
        except Exception as exc:
            return f"Read failed: {exc}"

    async def cmd_write(self, attrs_raw: str, body: str) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        path_raw = attrs.get("path") or attrs.get("file") or ""
        content = body.strip()
        mode = (attrs.get("mode") or "overwrite").lower().strip()
        if not path_raw:
            return "path attribute is required"
        if not content:
            return "content body is required"
        fpath = self._resolve_path(path_raw)
        try:
            fpath.parent.mkdir(parents=True, exist_ok=True)
            if mode == "append":
                with fpath.open("a", encoding="utf-8") as f:
                    f.write(content + "\n")
                return f"Appended {len(content)} chars to {fpath.name}"
            if mode == "overwrite":
                fpath.write_text(content, encoding="utf-8")
                return f"Written {len(content)} chars to {fpath.name}"
            return f"Unknown mode: {mode}. Use 'overwrite' or 'append'"
        except Exception as exc:
            return f"Write failed: {exc}"

    async def cmd_edit(self, attrs_raw: str, body: str) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        path_raw = attrs.get("path") or attrs.get("file") or ""
        search = attrs.get("search") or ""
        replace = attrs.get("replace") or ""
        count_str = attrs.get("count") or "0"
        body_text = body.strip()

        if not path_raw:
            return "path attribute is required"
        if not search and body_text and "->" in body_text:
            parts = body_text.split("->", 1)
            search = parts[0].strip()
            replace = parts[1].strip() if len(parts) > 1 else ""
        if not search:
            return "search text is required (attr or body with 'search -> replace' format)"
        try:
            count = int(count_str) if count_str.isdigit() else 0
        except ValueError:
            count = 0

        fpath = self._resolve_path(path_raw)
        if not fpath.is_file():
            return f"File not found: {fpath}"
        try:
            original = fpath.read_text(encoding="utf-8", errors="replace")
            if count > 0:
                new_text = original.replace(search, replace, count)
            else:
                new_text = original.replace(search, replace)
            if original == new_text:
                return f"No changes: '{search}' not found in {fpath.name}"
            fpath.write_text(new_text, encoding="utf-8")
            replacements = original.count(search)
            return f"Replaced {replacements} occurrence(s) in {fpath.name}"
        except Exception as exc:
            return f"Edit failed: {exc}"

    async def cmd_patch(self, attrs_raw: str, body: str) -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        path_raw = attrs.get("path") or attrs.get("file") or ""
        patch_content = body
        reverse = attrs.get("reverse", "").lower().strip() in ("true", "yes", "1")

        if not path_raw:
            return "path attribute is required"
        fpath = self._resolve_path(path_raw)
        if not fpath.is_file() and not patch_content.startswith("---"):
            return f"File not found: {fpath}"

        try:
            import subprocess
            import tempfile

            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".diff", encoding="utf-8", delete=False
            ) as tf:
                tf.write(patch_content)
                patch_path = tf.name

            try:
                cmd = ["patch", "-f"]
                if reverse:
                    cmd.append("-R")
                cmd.extend([str(fpath), patch_path])
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
                if result.returncode == 0:
                    return f"Patch applied: {result.stdout.strip() or 'OK'}"
                return f"Patch failed (exit={result.returncode}): {result.stderr.strip()[:1000] or result.stdout.strip()[:1000]}"
            finally:
                Path(patch_path).unlink(missing_ok=True)
        except Exception as exc:
            return f"Patch error: {exc}"
