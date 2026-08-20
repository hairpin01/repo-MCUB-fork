from __future__ import annotations

import os
import shutil
import sys
import tempfile
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: copy_release.py <artifact> <destination>", file=sys.stderr)
        return 2

    artifact = Path(sys.argv[1]).resolve()
    destination_value = os.environ.get("OPENAGENT_RELEASE_DESTINATION", sys.argv[2])
    destination_input = Path(destination_value).expanduser()
    if not destination_input.is_absolute():
        destination_input = Path.cwd() / destination_input
    if not artifact.is_file():
        print(f"release artifact does not exist: {artifact}", file=sys.stderr)
        return 1
    if destination_input.is_symlink():
        print(f"release destination must not be a symlink: {destination_input}", file=sys.stderr)
        return 1

    destination_parent = destination_input.parent.resolve()
    if not destination_parent.is_dir():
        print(
            f"release destination directory does not exist: {destination_parent}",
            file=sys.stderr,
        )
        return 1
    destination = destination_parent / destination_input.name
    file_descriptor = -1
    temporary: Path | None = None

    try:
        file_descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{destination.name}.",
            suffix=".tmp",
            dir=destination_parent,
        )
        temporary = Path(temporary_name)
        with artifact.open("rb") as source, os.fdopen(file_descriptor, "wb") as target:
            file_descriptor = -1
            shutil.copyfileobj(source, target)
            target.flush()
            os.fsync(target.fileno())
        os.chmod(temporary, artifact.stat().st_mode & 0o777)
        os.replace(temporary, destination)
    except OSError as exc:
        if file_descriptor >= 0:
            os.close(file_descriptor)
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        print(f"failed to copy release artifact: {exc}", file=sys.stderr)
        return 1
    print(f"release artifact copied to {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
