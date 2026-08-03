# scop: inline
# SPDX-License-Identifier: MIT

from __future__ import annotations

import asyncio
import shlex
import shutil
import subprocess
from pathlib import Path
from typing import Any


class AstGrepPlugin:
    name = "ast_grep"
    version = "0.1.0"
    author = "@hairpin01"
    description = "Structural code search and rewrite tools powered by ast-grep"

    tool_registry = (
        "ast_grep.search",
        "ast_grep.replace",
    )

    dangerous_tools = {"ast_grep.replace", "astgrep.replace"}

    tool_docs = {
        "ast_grep.search": {
            "desc": "Search source code by AST pattern using ast-grep",
            "args": "pattern (str); lang/language (str); path/paths (str, default '.'); glob/globs (str); json (bool|string)",
            "body": "pattern text when pattern attr is omitted",
            "returns": "ast-grep matches, JSON output, or an error message.",
            "example": "{\"tool\": \"ast_grep.search\", \"args\": {\"lang\": \"python\", \"pattern\": \"print($$$)\", \"path\": \".\"}}",
            "notes": "Requires ast-grep CLI (`ast-grep` or compatible `sg`) installed on the server.",
        },
        "ast_grep.replace": {
            "desc": "Preview or apply AST-based rewrites using ast-grep",
            "args": "pattern (str); rewrite/replace (str); lang/language (str); path/paths (str); glob/globs (str); apply/update (bool, default false)",
            "body": "optional 'pattern -> rewrite' format when attrs are omitted",
            "returns": "A rewrite diff/summary, command output, or an error message.",
            "example": "{\"tool\": \"ast_grep.replace\", \"args\": {\"lang\": \"python\", \"pattern\": \"print($X)\", \"rewrite\": \"logger.info($X)\", \"path\": \"src\"}}",
            "notes": "Dry-run preview is the default; pass apply=true to write changes.",
        },
    }

    tool_map = {
        "ast_grep": "cmd_search",
        "ast_grep.search": "cmd_search",
        "astgrep.search": "cmd_search",
        "ast_grep.replace": "cmd_replace",
        "astgrep.replace": "cmd_replace",
    }

    config_defaults = {
        "ast_grep_timeout": 30,
        "ast_grep_output_limit": 12000,
    }

    def __init__(self, agent: Any) -> None:
        self.agent = agent
        self._binary: str | None = None

    def _workspace_dir(self) -> Path:
        workspace = getattr(self.agent, "_workspace_dir", None)
        if callable(workspace):
            return Path(workspace())
        return Path.cwd()

    def _trim(self, text: str) -> str:
        try:
            limit = int(self.agent.config["ast_grep_output_limit"])
        except Exception:
            limit = 12000
        if len(text) <= limit:
            return text
        return text[:limit] + "\n...[truncated]"

    def _bool_attr(self, value: object, default: bool = False) -> bool:
        if value is None:
            return default
        if isinstance(value, bool):
            return value
        return str(value).strip().lower() in {"1", "yes", "true", "on", "apply", "update"}

    def _split_values(self, value: object, default: tuple[str, ...] = ()) -> list[str]:
        if value is None:
            return list(default)
        if isinstance(value, (list, tuple, set)):
            return [str(item).strip() for item in value if str(item).strip()]

        text = str(value).strip()
        if not text:
            return list(default)
        if "," in text or "\n" in text:
            return [part.strip() for part in text.replace("\n", ",").split(",") if part.strip()]

        try:
            parts = shlex.split(text)
        except ValueError:
            parts = []
        return parts or [text]

    def _find_binary(self) -> str | None:
        if self._binary:
            return self._binary

        for name in ("ast-grep", "sg"):
            binary = shutil.which(name)
            if not binary:
                continue
            if name == "sg" and not self._is_ast_grep_binary(binary):
                continue
            self._binary = binary
            return binary
        return None

    def _is_ast_grep_binary(self, binary: str) -> bool:
        try:
            proc = subprocess.run(
                [binary, "--version"],
                capture_output=True,
                check=False,
                text=True,
                timeout=2,
            )
        except Exception:
            return False
        output = f"{proc.stdout}\n{proc.stderr}".lower()
        return "ast-grep" in output

    def _validate_lang(self, lang: str) -> str:
        lang = (lang or "").strip().lower()
        if not lang:
            return ""
        if not lang.replace("-", "").replace("_", "").isalnum():
            return ""
        return lang

    def _resolve_existing_paths(self, raw_paths: object) -> list[str] | str:
        workspace = self._workspace_dir()
        paths = self._split_values(raw_paths, default=(".",))
        resolved: list[str] = []
        for path in paths:
            candidate = Path(path).expanduser()
            if not candidate.is_absolute():
                candidate = workspace / candidate
            if not candidate.exists():
                return f"Path not found: {path}"
            try:
                resolved.append(str(candidate.relative_to(workspace)))
            except ValueError:
                resolved.append(str(candidate))
        return resolved

    def _build_common_args(
        self,
        attrs: dict[str, str],
        body: str,
        rewrite: str | None = None,
        update: bool = False,
    ) -> tuple[list[str], str | None]:
        binary = self._find_binary()
        if not binary:
            return [], "ast-grep CLI not found. Install `ast-grep` or make a compatible `sg` binary available in PATH."

        pattern = attrs.get("pattern") or attrs.get("p") or body.strip()
        lang = self._validate_lang(attrs.get("lang") or attrs.get("language") or "")
        if not pattern:
            return [], "pattern is required"
        if not lang:
            return [], "lang/language attribute is required"

        paths = self._resolve_existing_paths(attrs.get("paths") or attrs.get("path") or ".")
        if isinstance(paths, str):
            return [], paths

        args = [binary, "run", "--pattern", pattern, "--lang", lang]
        for glob in self._split_values(attrs.get("globs") or attrs.get("glob")):
            args.extend(("--globs", glob))

        if rewrite is not None:
            args.extend(("--rewrite", rewrite))
            if update:
                args.append("--update-all")

        json_mode = attrs.get("json") or attrs.get("format")
        if self._bool_attr(json_mode):
            args.append("--json=compact")
        elif str(json_mode or "").strip().lower() in {"compact", "pretty", "stream"}:
            args.append(f"--json={str(json_mode).strip().lower()}")

        args.extend(paths)
        return args, None

    async def _run_ast_grep(self, args: list[str]) -> str:
        try:
            timeout = int(self.agent.config["ast_grep_timeout"])
        except Exception:
            timeout = 30

        proc = await asyncio.create_subprocess_exec(
            *args,
            cwd=str(self._workspace_dir()),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        try:
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        except asyncio.TimeoutError:
            proc.kill()
            await proc.communicate()
            return f"ast-grep timed out after {timeout}s"

        out = stdout.decode("utf-8", errors="replace")
        err = stderr.decode("utf-8", errors="replace")
        result = f"exit_code={proc.returncode}\n"
        if out:
            result += f"stdout:\n{out}\n"
        if err:
            result += f"stderr:\n{err}\n"
        return self._trim(result.rstrip())

    async def cmd_search(self, attrs_raw: str = "", body: str = "") -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        args, error = self._build_common_args(attrs, body)
        if error:
            return error
        return await self._run_ast_grep(args)

    async def cmd_replace(self, attrs_raw: str = "", body: str = "") -> str:
        attrs = self.agent._parse_xml_attrs(attrs_raw)

        if not attrs.get("pattern") and not attrs.get("p") and "->" in body:
            pattern, rewrite = body.split("->", 1)
            attrs["pattern"] = pattern.strip()
            attrs["rewrite"] = rewrite.strip()
            body = ""

        rewrite = attrs.get("rewrite") or attrs.get("replace") or attrs.get("r") or ""
        if not rewrite:
            return "rewrite/replace attribute is required"

        args, error = self._build_common_args(
            attrs,
            body,
            rewrite=rewrite,
            update=self._bool_attr(attrs.get("apply") or attrs.get("update") or attrs.get("write")),
        )
        if error:
            return error

        return await self._run_ast_grep(args)
