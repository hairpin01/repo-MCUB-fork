from __future__ import annotations

import html
import json
import os
import re
import secrets
import shlex
import subprocess
import sys
import tarfile
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


CHAT_ID = "-1003588062415"
MESSAGE_THREAD_ID = "11"
TOKEN_KEY = "TELEGRAM_BOT_TOKEN"
DRY_RUN_KEY = "OPENAGENT_NOTIFY_DRY_RUN"
TOKEN_RE = re.compile(r"^\d+:[A-Za-z0-9_-]+$")
ENV_KEY_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
SOURCE_EXCLUDES = {".env", ".env_script"}


class BuildNotificationError(RuntimeError):
    pass


def _is_enabled(value: str | None) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "on"}


def _project_dir() -> Path:
    configured = os.environ.get("CUBKIT_PROJECT_DIR")
    if configured:
        return Path(configured).resolve()
    return Path(__file__).resolve().parents[1]


def _read_env_file(path: Path) -> dict[str, str]:
    if not path.is_file():
        raise BuildNotificationError(
            f"{path.name} is missing; copy .env_script.example and set {TOKEN_KEY}"
        )

    values: dict[str, str] = {}
    for line_number, raw_line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line.removeprefix("export ").lstrip()

        key, separator, raw_value = line.partition("=")
        key = key.strip()
        if not separator or not ENV_KEY_RE.fullmatch(key):
            raise BuildNotificationError(
                f"invalid assignment in {path.name} at line {line_number}"
            )

        try:
            parts = shlex.split(raw_value, comments=True, posix=True)
        except ValueError as exc:
            raise BuildNotificationError(
                f"invalid value in {path.name} at line {line_number}: {exc}"
            ) from exc
        if len(parts) != 1:
            raise BuildNotificationError(
                f"value in {path.name} at line {line_number} must be quoted"
            )
        values[key] = parts[0]
    return values


def _bot_token() -> str:
    token = os.environ.get(TOKEN_KEY)
    if token is None:
        token = _read_env_file(_project_dir() / ".env_script").get(TOKEN_KEY)
    if not token:
        raise BuildNotificationError(f"{TOKEN_KEY} is not configured")
    if not TOKEN_RE.fullmatch(token):
        raise BuildNotificationError(f"{TOKEN_KEY} has an invalid format")
    return token

def _format_size(size: int) -> str:
    if size < 1024:
        return f"{size} B"
    if size < 1024 * 1024:
        return f"{size / 1024:.1f} KiB"
    return f"{size / (1024 * 1024):.2f} MiB"


def _build_message() -> str:
    profile = os.environ.get("CUBKIT_PROFILE", "").strip().lower()
    if profile not in {"debug", "release"}:
        raise BuildNotificationError("CUBKIT_PROFILE must be debug or release")

    output_value = os.environ.get("CUBKIT_OUTPUT", "").strip()
    if not output_value:
        raise BuildNotificationError("CUBKIT_OUTPUT is missing")
    output = Path(output_value).resolve()
    if not output.is_file():
        raise BuildNotificationError(f"build artifact does not exist: {output}")

    module_id = os.environ.get("CUBKIT_MODULE_ID", "openagent").strip()
    module_label = html.escape(module_id)
    artifact_name = html.escape(output.name)
    emoji = "0.0" if profile == "release" else ">_"
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    return "\n".join(
        (
            f"{emoji} <b>New {profile.upper()}-build</b> module {module_label}",
            f"<blockquote>👓 {artifact_name}",
            f"📦 {_format_size(output.stat().st_size)}",
            f"🕒 {timestamp}</blockquote>",
            f"<blockquote>#{module_label} #{profile}</blockquote>",
        )
    )


def _telegram_response(
    request: Request, action: str, timeout: int = 15
) -> dict[str, object]:
    try:
        with urlopen(request, timeout=timeout) as response:
            response_data = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        description = f"HTTP {exc.code}"
        try:
            error_data = json.loads(exc.read().decode("utf-8"))
            description = str(error_data.get("description") or description)
        except (json.JSONDecodeError, UnicodeDecodeError):
            pass
        raise BuildNotificationError(
            f"Telegram API rejected {action}: {description}"
        ) from exc
    except URLError as exc:
        raise BuildNotificationError(f"Telegram API is unavailable: {exc.reason}") from exc
    except json.JSONDecodeError as exc:
        raise BuildNotificationError("Telegram API returned invalid JSON") from exc

    if not isinstance(response_data, dict) or response_data.get("ok") is not True:
        description = (
            response_data.get("description", "unknown Telegram API error")
            if isinstance(response_data, dict)
            else "invalid Telegram API response"
        )
        raise BuildNotificationError(str(description))
    return response_data


def _source_files(project_dir: Path) -> list[Path]:
    try:
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            cwd=project_dir,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except FileNotFoundError as exc:
        raise BuildNotificationError("git is required to archive sources") from exc
    except subprocess.CalledProcessError as exc:
        error = exc.stderr.decode("utf-8", errors="replace").strip()
        raise BuildNotificationError(f"git failed to list sources: {error}") from exc

    files: list[Path] = []
    for raw_path in result.stdout.split(b"\0"):
        if not raw_path:
            continue
        relative = Path(os.fsdecode(raw_path))
        if relative.is_absolute() or ".." in relative.parts:
            raise BuildNotificationError(f"unsafe source path reported by git: {relative}")
        if any(part in SOURCE_EXCLUDES for part in relative.parts):
            continue
        source = project_dir / relative
        if source.is_file() or source.is_symlink():
            files.append(relative)

    if not files:
        raise BuildNotificationError("git reported no source files")
    return files


def _create_source_archive(
    project_dir: Path,
    destination_dir: Path,
    module_id: str,
    profile: str,
) -> Path:
    safe_module_id = re.sub(r"[^A-Za-z0-9_.-]+", "_", module_id).strip("._")
    safe_module_id = safe_module_id or "module"
    archive_path = destination_dir / f"{safe_module_id}-{profile}-sources.tar.gz"
    archive_root = f"{safe_module_id}-{profile}-sources"

    with tarfile.open(archive_path, mode="w:gz", dereference=False) as archive:
        for relative in _source_files(project_dir):
            archive.add(
                project_dir / relative,
                arcname=f"{archive_root}/{relative.as_posix()}",
                recursive=False,
            )
    return archive_path


def _multipart_media_group(
    artifact: Path, source_archive: Path, caption: str
) -> tuple[bytes, str]:
    boundary = f"cubkit-{secrets.token_hex(16)}"
    parts: list[bytes] = []
    media = json.dumps(
        [
            {
                "type": "document",
                "media": "attach://artifact",
                "caption": caption,
                "parse_mode": "HTML",
            },
            {
                "type": "document",
                "media": "attach://sources",
            },
        ],
        ensure_ascii=False,
        separators=(",", ":"),
    )

    for name, value in (
        ("chat_id", CHAT_ID),
        ("message_thread_id", MESSAGE_THREAD_ID),
        ("media", media),
    ):
        parts.extend(
            (
                f"--{boundary}\r\n".encode("ascii"),
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode("ascii"),
                value.encode("utf-8"),
                b"\r\n",
            )
        )

    for field_name, file_path in (
        ("artifact", artifact),
        ("sources", source_archive),
    ):
        filename = (
            file_path.name.replace('"', "_").replace("\r", "").replace("\n", "")
        )
        parts.extend(
            (
                f"--{boundary}\r\n".encode("ascii"),
                (
                    f'Content-Disposition: form-data; name="{field_name}"; '
                    f'filename="{filename}"\r\n'
                ).encode("utf-8"),
                b"Content-Type: application/octet-stream\r\n\r\n",
                file_path.read_bytes(),
                b"\r\n",
            )
        )
    parts.append(f"--{boundary}--\r\n".encode("ascii"))
    return b"".join(parts), boundary


def _send_media_group(
    token: str, artifact: Path, source_archive: Path, caption: str
) -> list[int]:
    endpoint = f"https://api.telegram.org/bot{quote(token, safe=':')}/sendMediaGroup"
    body, boundary = _multipart_media_group(artifact, source_archive, caption)
    request = Request(
        endpoint,
        data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST",
    )
    response = _telegram_response(request, "the media group", timeout=60)
    result = response.get("result")
    if not isinstance(result, list) or len(result) != 2:
        raise BuildNotificationError("Telegram API response has no two-item media group")

    message_ids: list[int] = []
    for item in result:
        if not isinstance(item, dict) or not isinstance(item.get("message_id"), int):
            raise BuildNotificationError("Telegram media group item has no message_id")
        message_ids.append(item["message_id"])
    return message_ids


def main() -> int:
    try:
        message = _build_message()
        profile = os.environ.get("CUBKIT_PROFILE", "").strip().lower()
        module_id = os.environ.get("CUBKIT_MODULE_ID", "openagent").strip()
        artifact = Path(os.environ.get("CUBKIT_OUTPUT", "")).resolve()

        with tempfile.TemporaryDirectory(prefix="openagent-sources-") as temp_dir:
            source_archive = _create_source_archive(
                _project_dir(), Path(temp_dir), module_id, profile
            )
            if _is_enabled(os.environ.get(DRY_RUN_KEY)):
                print(
                    "\nTelegram build notification dry run:"
                    f"\n{message}"
                    f"\nArtifact: {artifact} ({_format_size(artifact.stat().st_size)})"
                    f"\nSources: {source_archive.name} "
                    f"({_format_size(source_archive.stat().st_size)})"
                )
                return 0

            token = _bot_token()
            message_ids = _send_media_group(token, artifact, source_archive, message)
    except BuildNotificationError as exc:
        print(f"\nbuild notification failed: {exc}", file=sys.stderr)
        return 1

    print(
        "\nTelegram build media group sent: "
        f"message_ids={','.join(str(item) for item in message_ids)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
