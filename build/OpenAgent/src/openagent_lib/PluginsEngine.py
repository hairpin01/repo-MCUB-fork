# SPDX-License-Identifier: MIT
from __future__ import annotations

from typing import Any
from pathlib import Path
import sys
import contextlib
import asyncio
import json
import importlib
from urllib.parse import quote
import cubkit.lib.aiohttp
import re
import html
import io
import base64
import tempfile
import time
import difflib
import mimetypes
import uuid

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.channels import EditPhotoRequest

from core.lib.types import (
    Kernel,
    Event,
)
from core.lib.loader.module_config import (
    ConfigValue,
    Boolean,
    String,
    Float,
    List,
    Integer,
)

from .TodoService import _WHITESPACE_RE

class OpenAgentPlugin:
    """Base class for OpenAgent plugins."""
    name: str = ""
    version: str = "0.1.0"
    author: str = ""
    description: str = ""
    tool_registry: tuple[str, ...] = ()
    tool_map: dict[str, str] = {}
    tool_docs: dict[str, dict[str, str]] = {}
    dangerous_tools: set[str] = set()
    config_defaults: dict[str, object] = {}

    def __init__(self, agent: "OpenAgent") -> None:
        self._agent = agent
        self.kernel: Kernel = self._agent.kernel
        self.client = self._agent.client

    @property
    def agent(self) -> "OpenAgent":
        return self._agent

    def add_runtime_comment(self, runtime_token: str | None, comment: str) -> bool:
        """Queue a live comment for the current OpenAgent run."""
        return self._agent.add_runtime_comment(runtime_token, comment)

    def create_background_tool_task(
        self,
        *,
        tool_name: str,
        attrs_raw: str = "",
        body: str = "",
        source_event: Any | None = None,
        status_event: Any | None = None,
        runtime_token: str | None = None,
        label: str = "",
    ) -> str:
        """Run an OpenAgent tool in background and comment when it finishes."""
        return self._agent.create_background_tool_task(
            tool_name=tool_name,
            attrs_raw=attrs_raw,
            body=body,
            source_event=source_event,
            status_event=status_event,
            runtime_token=runtime_token,
            label=label,
        )

    async def on_load(self) -> None:
        """Called after plugin is registered."""
        pass

class _OpenAgentPluginSkillMixin:
    """OpenAgent plugin and skill discovery/install helpers."""

    def _resolve_skills_dir(self) -> Path:
        path = Path(self._workspace_dir()) / "openagent_skills"
        path.mkdir(parents=True, exist_ok=True)
        return path

    def _legacy_skills_dir(self) -> Path:
        return Path(self._workspace_dir()) / "openagent_skills"

    def _workspace_dir(self) -> str:
        work_dir = getattr(self.kernel, "WORK_DIR", None)
        if work_dir:
            path = Path(str(work_dir)).expanduser()
            if path.exists() and path.is_dir():
                return str(path)
        return str(Path.cwd())

    def _resolve_plugins_dir(self) -> Path:
        """Directory for installed plugins on the real machine."""
        path = Path(self._workspace_dir()) / "openagent_plugins"
        path.mkdir(parents=True, exist_ok=True)
        return path

    def _disabled_plugins_file(self) -> Path:
        return self._resolve_plugins_dir() / "disabled_plugins.json"

    def _load_disabled_plugins(self) -> set[str]:
        fpath = self._disabled_plugins_file()
        if not fpath.exists():
            return set()
        try:
            data = json.loads(fpath.read_text(encoding="utf-8"))
            raw = data.get("disabled", data) if isinstance(data, dict) else data
            if not isinstance(raw, list):
                return set()
            return {self._safe_plugin_name(item) for item in raw if str(item or "").strip()}
        except Exception as exc:
            self.log.warning(f"OpenAgent: failed to load disabled plugins: {exc}")
            return set()

    def _save_disabled_plugins(self) -> None:
        try:
            data = {"disabled": sorted(getattr(self, "_disabled_plugins", set()))}
            self._disabled_plugins_file().write_text(
                json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
            )
        except Exception as exc:
            self.log.warning(f"OpenAgent: failed to save disabled plugins: {exc}")

    def _builtin_plugins_dir(self) -> Path:
        """Directory with bundled plugins shipped with OpenAgent."""
        return Path(__file__).resolve().parent / "OpenAgent" / "plugins"

    def _is_builtin_plugin_file(self, fpath: Path) -> bool:
        try:
            fpath.resolve().relative_to(self._builtin_plugins_dir().resolve())
            return True
        except Exception:
            return False

    def _plugin_scan_dirs(self) -> list[Path]:
        dirs: list[Path] = []
        for candidate in (self._builtin_plugins_dir(), self._resolve_plugins_dir()):
            if candidate.exists() and candidate.is_dir() and candidate not in dirs:
                dirs.append(candidate)
        return dirs

    async def _load_installed_plugins(self) -> None:
        """Scan bundled + external plugin directories and register all plugins.
        External plugins override bundled ones without warning."""
        for plugins_dir in self._plugin_scan_dirs():
            for fpath in sorted(plugins_dir.glob("*.py")):
                if fpath.name.startswith("_") or fpath.name == "__init__.py":
                    continue
                if self._is_builtin_plugin_file(fpath) and self._safe_plugin_name(fpath.stem) in self._disabled_plugins:
                    self.log.debug(f"Plugin skipped (disabled): {fpath.stem}")
                    continue
                try:
                    await self._register_plugin_from_file(fpath)
                except Exception as exc:
                    self.log.warning(f"Plugin load failed: {fpath.name} - {exc}")
        await self._reload_plugin_config_values()
        self._refresh_live_config_schema()

    async def _reload_plugin_config_values(self) -> None:
        """Reload persisted config after plugins add dynamic ConfigValues."""
        try:
            get_config = getattr(self.kernel, "get_module_config", None)
            if not get_config:
                return
            saved = await get_config(self.name)
            if saved and hasattr(self.config, "from_dict"):
                self.config.from_dict(saved)
        except Exception as exc:
            self.log.warning(f"OpenAgent: failed to reload plugin config values: {exc}")

    def _refresh_live_config_schema(self) -> None:
        """Expose plugin-added ConfigValues to MCUB config UI."""
        with contextlib.suppress(Exception):
            store_schema = getattr(self.kernel, "store_module_config_schema", None)
            if callable(store_schema):
                store_schema(self.name, self.config)
                return
        with contextlib.suppress(Exception):
            if not hasattr(self.kernel, "_live_module_configs"):
                self.kernel._live_module_configs = {}
            self.kernel._live_module_configs[self.name] = self.config

    async def _register_plugin_from_file(self, fpath: Path) -> None:
        """Import a .py file, find *Plugin class, register it."""
        module_name = f"openagent_plugins_{fpath.parent.name}_{fpath.stem}_{uuid.uuid4().hex[:8]}"
        spec = importlib.util.spec_from_file_location(module_name, fpath)
        if not spec or not spec.loader:
            raise ImportError(f"Cannot load {fpath}")
        mod = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = mod
        try:
            spec.loader.exec_module(mod)
        except Exception:
            sys.modules.pop(module_name, None)
            raise
        plugin_cls = None
        for attr_name in dir(mod):
            attr = getattr(mod, attr_name)
            if isinstance(attr, type) and attr_name.endswith("Plugin") and attr is not OpenAgentPlugin:
                plugin_cls = attr
                break
        if not plugin_cls:
            raise ValueError(f"No *Plugin class found in {fpath.name}")
        plugin = plugin_cls(self)
        self._register_plugin(plugin)
        self._plugin_files[str(plugin.name).lower()] = fpath
        if not self._is_builtin_plugin_file(fpath):
            plugin_name = self._safe_plugin_name(plugin.name)
            if plugin_name in self._disabled_plugins:
                self._disabled_plugins.discard(plugin_name)
                self._save_disabled_plugins()
        on_load = getattr(plugin, "on_load", None)
        if callable(on_load):
            maybe_awaitable = on_load()
            if asyncio.iscoroutine(maybe_awaitable):
                await maybe_awaitable

    def _register_plugin(self, plugin: OpenAgentPlugin) -> None:
        """Register plugin: add config_defaults, tools, handlers."""
        name = str(getattr(plugin, "name", "") or "").strip().lower()
        if not name:
            name = plugin.__class__.__name__.replace("Plugin", "").strip().lower()
        plugin.name = name
        if name in self._plugins:
            self.log.debug(f"Plugin {name} already registered, external overrides bundled")
        # Set default config values if not already set
        for key, value in getattr(plugin, "config_defaults", {}).items():
            if key not in self.config.keys():
                self.config._values[key] = self._plugin_config_value(key, value)
        self._refresh_live_config_schema()
        self._plugins[name] = plugin
        self._tool_map_cache = None  # invalidate after plugin list changes
        self._tool_registry_cache = None
        self.log.info(f"Plugin registered: {name} v{plugin.version}")

    def _plugin_config_value(self, key: str, value: object) -> ConfigValue:
        description = f"OpenAgent plugin setting: {key}"
        if isinstance(value, bool):
            validator = Boolean(default=value)
        elif isinstance(value, int):
            validator = Integer(default=value)
        elif isinstance(value, float):
            validator = Float(default=value)
        elif isinstance(value, list):
            validator = List(default=value)
        else:
            validator = String(default=str(value or ""))
        return ConfigValue(key, value, description=description, validator=validator)

    def _effective_tool_registry(self) -> tuple[str, ...]:
        cached = getattr(self, "_tool_registry_cache", None)
        if isinstance(cached, tuple):
            return cached
        names = set(self.TOOL_REGISTRY)
        names.update(self._get_tool_map().keys())
        for plugin in self._plugins.values():
            for tool_name in getattr(plugin, "tool_registry", ()):
                if tool_name:
                    names.add(str(tool_name).strip().lower())
            for tool_name in getattr(plugin, "tool_map", {}).keys():
                if tool_name:
                    names.add(str(tool_name).strip().lower())
        registry = tuple(sorted(names))
        self._tool_registry_cache = registry
        return registry

    def _unregister_plugin(self, name: str) -> None:
        """Remove a plugin by name."""
        name = str(name or "").strip().lower()
        self._plugins.pop(name, None)
        self._plugin_files.pop(name, None)
        self._tool_map_cache = None  # invalidate after plugin list changes
        self._tool_registry_cache = None
        self.log.info(f"Plugin unregistered: {name}")

    def _get_plugin_for_tool(self, tool_name: str) -> OpenAgentPlugin | None:
        """Find which plugin handles a given tool name."""
        tool_name = (tool_name or "").lower().strip()
        plugins = tuple(self._plugins.values())
        for candidate in reversed(plugins):
            tool_map = {
                str(key).lower().strip(): value
                for key, value in getattr(candidate, "tool_map", {}).items()
            }
            if tool_name in tool_map:
                return candidate
        for candidate in reversed(plugins):
            registry = {
                str(item).lower().strip()
                for item in getattr(candidate, "tool_registry", ())
                if item
            }
            if tool_name in registry:
                return candidate
        group = self._tool_group(tool_name)
        plugin = self._plugins.get(group)
        if plugin is not None:
            return plugin
        return None

    def _core_tool_docs(self) -> dict[str, dict[str, str]]:
        return {
            "thinking.note": {"desc": "Record a concise progress/thinking note for the user.", "args": "note/text", "body": "optional note text"},
            "skill": {"desc": "Save an OpenAgent skill from body text.", "args": "name/title", "body": "skill markdown/content"},
            "skill.save": {"desc": "Save an OpenAgent skill from body text.", "args": "name/title", "body": "skill markdown/content"},
            "skills.list": {"desc": "List installed OpenAgent skills."},
            "skills.read": {"desc": "Read an installed OpenAgent skill.", "args": "name", "body": "optional skill name"},
            "skills.activate": {"desc": "Activate/load the best matching installed skill for the current task.", "args": "query/name", "body": "optional query"},
            "skills.import_md": {"desc": "Import a skill from markdown body.", "args": "name/title", "body": "markdown content"},
            "skills.export_md": {"desc": "Export/read an installed skill as markdown.", "args": "name", "body": "optional skill name"},
            "skills.save_from_ai": {"desc": "Persist useful knowledge as an OpenAgent skill.", "args": "name/title", "body": "skill content"},
            "skills.install": {"desc": "Install a skill from the configured skill repository.", "args": "name", "body": "optional skill name"},
            "skills.repo_list": {"desc": "List skills available in the configured skill repository."},
            "code.generate_file": {"desc": "Generate a text/code file and keep it for sending/attaching.", "args": "name/path", "body": "file content"},
            "code.generate_mcub_module": {"desc": "Generate an MCUB module file.", "args": "name", "body": "module code"},
            "code.choose_filename": {"desc": "Choose/sanitize a filename for generated code.", "args": "name/path", "body": "optional filename"},
            "code.attach_result": {"desc": "Attach/send the latest generated code/file result."},
            "code.read_docs": {"desc": "Read bundled/remote MCUB API documentation."},
            "context.remember": {"desc": "Remember a note in the active chat context.", "body": "memory note"},
            "context.clear": {"desc": "Clear the active OpenAgent session context."},
            "context.prune": {"desc": "Prune internal OpenAgent context: history, tools, tool_memory, runtime_comments, or all.", "args": "target/all; keep", "body": "optional target list"},
            "context.discard": {"desc": "Alias for context.prune." , "args": "target/all; keep", "body": "optional target list"},
            "context.regenerate": {"desc": "Explain that regeneration is available via the response button."},
            "context.reply_context": {"desc": "Read context from the replied message."},
            "context.media_context": {"desc": "Read replied media/message context."},
            "todo.add": {"desc": "Add a TODO item.", "args": "text/task"},
            "todo.delete": {"desc": "Delete a TODO item.", "args": "id/index/text"},
            "todo.edit": {"desc": "Edit a TODO item.", "args": "id/index/text/status"},
            "todo.current": {"desc": "Show the current TODO list."},
            "todo.close": {"desc": "Mark a TODO item as closed.", "args": "id/index/text"},
            "todo.closeall": {"desc": "Close all TODO items."},
            "todo.clear": {"desc": "Clear the TODO list."},
            "utility.token_usage": {"desc": "Show token usage from the last provider response."},
            "utility.placeholders": {"desc": "Show available OpenAgent template placeholders."},
            "utility.random_template": {"desc": "Render the current thinking/random template."},
            "utility.agent_log": {"desc": "Explain where the agent log is shown."},
            "utility.error_file": {"desc": "Explain how OpenAgent reports errors."},
            "utility.tool_help": {"desc": "Show normalized documentation for one core/plugin tool.", "args": "tool (str) — exact tool name", "body": "optional tool name"},
            "utility.list_tools": {"desc": "List all available core and plugin tools by category with short descriptions."},
            "utility.plugin_docs": {"desc": "Show activated plugin documentation and each plugin's tools.", "args": "plugin/name (str, optional) — plugin to inspect", "body": "optional plugin name"},
        }

    def _doc_text(self, value: object, *, default: str = "") -> str:
        text = _WHITESPACE_RE.sub(" ", str(value or "")).strip()
        return text or default

    def _plugin_tool_names(self, plugin: object, *, include_aliases: bool = True) -> list[str]:
        names: set[str] = set()
        for tool_name in getattr(plugin, "tool_registry", ()) or ():
            clean = str(tool_name or "").strip().lower()
            if clean:
                names.add(clean)
        if include_aliases:
            for tool_name in (getattr(plugin, "tool_map", {}) or {}).keys():
                clean = str(tool_name or "").strip().lower()
                if clean:
                    names.add(clean)
        return sorted(names)

    def _normalize_tool_doc_entry(
        self,
        tool_name: str,
        raw_doc: object,
        *,
        plugin: object | None = None,
        handler: str = "",
        source: str = "core",
    ) -> dict[str, str]:
        if isinstance(raw_doc, dict):
            entry = {str(key): self._doc_text(value) for key, value in raw_doc.items() if value is not None}
        elif raw_doc:
            entry = {"desc": self._doc_text(raw_doc)}
        else:
            entry = {}

        clean = str(tool_name or "").strip().lower()
        entry.setdefault("desc", f"Tool handled by {handler}" if handler else "No documentation yet")
        entry.setdefault("args", "none")
        entry.setdefault("body", "not used")
        entry["tool"] = clean
        entry["category"] = self._tool_group(clean)
        entry["source"] = source
        if handler:
            entry.setdefault("handler", handler)

        if plugin is not None:
            plugin_name = self._doc_text(getattr(plugin, "name", ""), default=self._tool_group(clean))
            entry["plugin"] = plugin_name
            entry["plugin_version"] = self._doc_text(getattr(plugin, "version", ""), default="?")
            author = self._doc_text(getattr(plugin, "author", ""))
            if author:
                entry["plugin_author"] = author
            plugin_desc = self._doc_text(getattr(plugin, "description", ""))
            if plugin_desc:
                entry["plugin_desc"] = plugin_desc
            dangerous = {str(item).strip().lower() for item in getattr(plugin, "dangerous_tools", set()) or set()}
            if clean in dangerous:
                entry.setdefault("dangerous", "true")
        return entry

    def _plugin_tool_docs(self, plugin: object) -> dict[str, dict[str, str]]:
        plugin_docs = getattr(plugin, "tool_docs", None)
        plugin_docs = plugin_docs if isinstance(plugin_docs, dict) else {}
        tool_map = {
            str(key).strip().lower(): str(value).strip()
            for key, value in (getattr(plugin, "tool_map", {}) or {}).items()
            if str(key or "").strip()
        }
        docs: dict[str, dict[str, str]] = {}
        for tool_name in self._plugin_tool_names(plugin):
            handler = tool_map.get(tool_name, "")
            raw_doc = plugin_docs.get(tool_name)
            if raw_doc is None:
                raw_doc = {
                    "desc": f"Plugin tool from {self._doc_text(getattr(plugin, 'name', ''), default=self._tool_group(tool_name))}",
                    "args": "see plugin implementation or call utility.plugin_docs",
                    "body": "optional, depends on tool",
                }
            docs[tool_name] = self._normalize_tool_doc_entry(
                tool_name,
                raw_doc,
                plugin=plugin,
                handler=handler,
                source="plugin",
            )
        return docs

    def _get_tool_docs(self, tool_name: str | None = None) -> dict:
        docs: dict[str, dict[str, str]] = {}
        core_docs = self._core_tool_docs()
        for tname, handler in self._get_tool_map().items():
            clean = str(tname).lower().strip()
            docs[clean] = self._normalize_tool_doc_entry(
                clean,
                core_docs.get(clean, {"desc": f"Tool handled by {handler}", "args": "see core handler docs"}),
                handler=str(handler or ""),
                source="core",
            )
        for plugin in self._plugins.values():
            docs.update(self._plugin_tool_docs(plugin))
        if tool_name:
            clean = str(tool_name).lower().strip()
            return {clean: docs.get(clean, {"tool": clean, "desc": f"No documentation for {clean}", "args": "unknown", "body": "unknown"})}
        return docs

    def _format_tool_doc(self, tool_name: str, entry: dict[str, str]) -> str:
        clean = str(tool_name or entry.get("tool") or "").strip().lower()
        lines = [f"📘 {clean}"]
        if entry.get("plugin"):
            plugin_label = f"{entry['plugin']} v{entry.get('plugin_version', '?')}"
            if entry.get("plugin_author"):
                plugin_label += f" by {entry['plugin_author']}"
            lines.append(f"   plugin: {plugin_label}")
            if entry.get("plugin_desc"):
                lines.append(f"   plugin docs: {entry['plugin_desc']}")
        elif entry.get("source"):
            lines.append(f"   source: {entry['source']}")
        lines.append(f"   desc: {entry.get('desc', '')}")
        if entry.get("args"):
            lines.append(f"   args: {entry['args']}")
        if entry.get("body"):
            lines.append(f"   body: {entry['body']}")
        if entry.get("returns"):
            lines.append(f"   returns: {entry['returns']}")
        if entry.get("example"):
            lines.append(f"   example: {entry['example']}")
        if entry.get("notes"):
            lines.append(f"   notes: {entry['notes']}")
        if entry.get("handler"):
            lines.append(f"   handler: {entry['handler']}")
        if entry.get("dangerous") == "true":
            lines.append("   ⚠️ requires confirmation")
        return "\n".join(lines)

    def _format_plugin_docs(self, plugin_name: str | None = None, *, max_tools: int | None = None) -> str:
        plugins = getattr(self, "_plugins", {}) or {}
        if not plugins:
            return "No activated plugins."
        selected: list[tuple[str, object]] = []
        query = str(plugin_name or "").strip().lower()
        for name, plugin in sorted(plugins.items(), key=lambda item: str(item[0])):
            aliases = {str(name).strip().lower(), self._doc_text(getattr(plugin, "name", "")).lower()}
            if query and query not in aliases:
                continue
            selected.append((str(name), plugin))
        if query and not selected:
            return f"No activated plugin named '{query}'. Activated plugins: {', '.join(sorted(plugins))}"

        lines = ["🧩 Activated plugin docs:"]
        for name, plugin in selected:
            docs = self._plugin_tool_docs(plugin)
            desc = self._doc_text(getattr(plugin, "description", ""), default="no description")
            version = self._doc_text(getattr(plugin, "version", ""), default="?")
            author = self._doc_text(getattr(plugin, "author", ""))
            header = f"\n{name} v{version} — {desc}"
            if author:
                header += f" (author: {author})"
            lines.append(header)
            tool_items = sorted(docs.items())
            if max_tools is not None and len(tool_items) > max_tools:
                visible = tool_items[:max_tools]
                hidden = len(tool_items) - max_tools
            else:
                visible = tool_items
                hidden = 0
            for tname, entry in visible:
                bits = [f"  · {tname}: {entry.get('desc', '')}"]
                if entry.get("args") and entry.get("args") != "none":
                    bits.append(f"args: {entry['args']}")
                if entry.get("body") and entry.get("body") != "not used":
                    bits.append(f"body: {entry['body']}")
                if entry.get("returns"):
                    bits.append(f"returns: {entry['returns']}")
                if entry.get("dangerous") == "true":
                    bits.append("⚠️ confirmation")
                lines.append(" | ".join(bits))
            if hidden:
                lines.append(f"  · ...(+{hidden} more; call utility.plugin_docs tool={name})")
        return "\n".join(lines)

    async def _fetch_repo_plugins(self) -> list[dict]:
        """Fetch list of available plugins from GitHub repo."""
        url = "https://api.github.com/repos/hairpin01/repo-MCUB-fork/contents/OpenAgent/plugins"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=15)) as resp:
                    if resp.status != 200:
                        return []
                    files = await resp.json()
        except Exception:
            return []

        plugins = []
        for f in files:
            fname = f.get("name", "")
            if not fname.endswith(".py") or fname == "__init__.py":
                continue
            raw_url = f.get("download_url", "")
            meta = await self._parse_plugin_meta(raw_url)
            meta["file_name"] = fname
            meta["plugin_name"] = fname.replace(".py", "")
            meta["download_url"] = raw_url
            plugins.append(meta)
        self._plugins_cache = plugins
        return plugins

    async def _parse_plugin_meta(self, raw_url: str) -> dict:
        """Parse plugin metadata from raw .py file via regex."""
        meta: dict = {"name": "?", "version": "?", "author": "?", "description": "?", "tools": []}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(raw_url, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                    if resp.status != 200:
                        return meta
                    code = await resp.text()
        except Exception:
            return meta

        name_m = re.search(r'name\s*=\s*["](.+?)["]', code) or re.search(r"name\s*=\s*['](.+?)[']", code)
        ver_m = re.search(r'version\s*=\s*["](.+?)["]', code) or re.search(r"version\s*=\s*['](.+?)[']", code)
        author_m = re.search(r'author\s*=\s*["](.+?)["]', code) or re.search(r"author\s*=\s*['](.+?)[']", code)
        desc_m = re.search(r'"ru"\s*:\s*"(.+?)"', code)
        if not desc_m:
            desc_m = re.search(r'"en"\s*:\s*"(.+?)"', code)
        tools_m = re.findall(r'"((?:terminal|web|mcub|message|file|dialog|chat|moderation|profile|contacts|creation|account|code|utility|skills|context|todo|thinking)\.[\w.]+)"', code)

        if name_m:
            meta["name"] = name_m.group(1)
        if ver_m:
            meta["version"] = ver_m.group(1)
        if author_m:
            meta["author"] = author_m.group(1)
        if desc_m:
            meta["description"] = desc_m.group(1)
        if tools_m:
            meta["tools"] = tools_m

        return meta

    async def _install_plugin_from_repo(self, name: str) -> str:
        """Download a plugin from repo and install it."""
        safe_name = self._safe_plugin_name(name)
        raw_url = f"https://raw.githubusercontent.com/hairpin01/repo-MCUB-fork/main/OpenAgent/plugins/{safe_name}.py"
        async with aiohttp.ClientSession() as session:
            async with session.get(raw_url, timeout=aiohttp.ClientTimeout(total=15)) as resp:
                if resp.status != 200:
                    raise ValueError(f"Plugin {safe_name} not found in repo")
                code = await resp.text()

        plugins_dir = self._resolve_plugins_dir()
        fpath = plugins_dir / f"{safe_name}.py"
        fpath.write_text(code, encoding="utf-8")
        try:
            await self._register_plugin_from_file(fpath)
        except Exception:
            with contextlib.suppress(Exception):
                fpath.unlink()
            raise
        return next((pname for pname, path in self._plugin_files.items() if path == fpath), safe_name)

    def _safe_plugin_name(self, name: str) -> str:
        name = re.sub(r"[^a-zA-Z0-9_.-]+", "_", str(name or "").strip()).strip("._")
        if name.endswith("_plugin"):
            name = name[:-7]
        return (name[:64] or "plugin").lower()

    async def _install_plugin_from_code(self, name: str, code: str) -> str:
        """Install a plugin from raw Python code into openagent_plugins/."""
        code = (code or "").strip()
        if not code:
            raise ValueError("Plugin code is empty")
        compile(code, f"<openagent-plugin:{name or 'reply'}>", "exec")
        safe_name = self._safe_plugin_name(name)
        fpath = self._resolve_plugins_dir() / f"{safe_name}.py"
        fpath.write_text(code + "\n", encoding="utf-8")
        try:
            await self._register_plugin_from_file(fpath)
        except Exception:
            with contextlib.suppress(Exception):
                fpath.unlink()
            raise
        return next((pname for pname, path in self._plugin_files.items() if path == fpath), safe_name)

    async def _install_plugin_from_reply(self, event: Event) -> str:
        reply = await event.get_reply_message()
        if not reply:
            raise ValueError("Reply to a .py plugin file or Python plugin code")
        arg_name = self._args_raw(event)
        file_name = getattr(getattr(reply, "file", None), "name", None) or ""
        code = ""
        try:
            data = await reply.download_media(file=bytes)
            if data:
                code = data.decode("utf-8", errors="replace")
        except Exception:
            code = ""
        if not code.strip():
            raise ValueError("Plugin code is empty")
        name = arg_name.strip()
        if not name and file_name.lower().endswith(".py"):
            name = Path(file_name).stem
        if not name:
            class_match = re.search(r"class\s+(\w+Plugin)\b", code)
            name = class_match.group(1).replace("Plugin", "") if class_match else "plugin"
        return await self._install_plugin_from_code(name, code)

    def _repo_context_prompt(self) -> str:
        if not bool(self.config.get("repo_context_enabled", True)):
            return ""
        workspace = Path(self._workspace_dir())
        max_chars = int(self.config.get("repo_context_max_chars", 7000) or 7000)
        lines: list[str] = [f"Workspace: {workspace}"]
        try:
            entries = sorted(
                workspace.iterdir(),
                key=lambda p: (p.is_file(), p.name.lower()),
            )
            top = []
            for item in entries[:80]:
                marker = "/" if item.is_dir() else ""
                top.append(item.name + marker)
            if top:
                lines.append("Top-level:")
                lines.extend(f"- {name}" for name in top)
        except Exception as exc:
            lines.append(f"Top-level unavailable: {exc}")
            return "\n".join(lines)[:max_chars]

        key_files = ["README.md", "pyproject.toml", "requirements.txt", "config.example.json", "modules.ini"]
        for name in key_files:
            file_path = workspace / name
            if not file_path.is_file():
                continue
            try:
                text = file_path.read_text(encoding="utf-8", errors="replace").strip()
            except Exception as exc:
                lines.append(f"{name}: read error: {exc}")
                continue
            if name.endswith(".json"):
                try:
                    obj = json.loads(text)
                    short = json.dumps(obj, ensure_ascii=False, indent=2)[:1200]
                except Exception:
                    short = text[:1200]
            else:
                short = text[:1200]
            lines.append(f"{name}:\n{short}")

        module_dirs = [workspace / "modules", workspace / "modules_loaded"]
        for mdir in module_dirs:
            if not mdir.is_dir():
                continue
            try:
                mod_names = sorted(p.name for p in mdir.iterdir() if p.is_file())[:120]
            except Exception as exc:
                lines.append(f"{mdir.name}: unavailable: {exc}")
                continue
            lines.append(f"{mdir.name} files ({len(mod_names)} shown):")
            lines.extend(f"- {mn}" for mn in mod_names)

        text = "\n".join(lines)
        if len(text) > max_chars:
            text = text[:max_chars] + "\n... [repo context truncated]"
        return "\n\nLocal MCUB workspace snapshot:\n" + text

    def _safe_skill_name(self, name: str) -> str:
        name = re.sub(r"[^a-zA-Z0-9_.-]+", "_", name.strip()).strip("._")
        return name[:64] or "skill"

    def _skill_path(self, name: str) -> Path:
        if not getattr(self, "_skills_dir", None):
            self._skills_dir = self._resolve_skills_dir()
        return self._skills_dir / self._safe_skill_name(name) / "SKILL.md"

    def _skill_name_from_path(self, path: Path) -> str:
        if path.name == "SKILL.md" and path.parent.name:
            return path.parent.name
        return path.stem

    def _find_skill_path(self, name: str) -> Path:
        path = self._skill_path(name)
        if path.exists():
            return path

        legacy_path = self._legacy_skills_dir() / f"{self._safe_skill_name(name)}.md"
        if legacy_path.exists():
            return legacy_path

        return path

    def _list_skills(self) -> list[Path]:
        if not getattr(self, "_skills_dir", None):
            self._skills_dir = self._resolve_skills_dir()
        try:
            self._skills_dir.mkdir(parents=True, exist_ok=True)
            skills = list(self._skills_dir.glob("*/SKILL.md"))

            # Backward compatibility for older OpenAgent exports. OpenCode-style
            # skills in openagent_skills/<name>/SKILL.md win on name conflicts.
            seen = {self._skill_name_from_path(path).lower() for path in skills}
            legacy_dir = self._legacy_skills_dir()
            if legacy_dir.is_dir():
                for path in legacy_dir.glob("*.md"):
                    if path.stem.lower() not in seen:
                        skills.append(path)
                        seen.add(path.stem.lower())

            return sorted(skills, key=lambda p: self._skill_name_from_path(p).lower())
        except Exception as e:
            self.log.warning(f"OpenAgent skills directory unavailable: {e}")
            return []

    def _should_load_skills(self, prompt: str = "") -> bool:
        if not bool(self.config.get("skills_enabled", True)):
            return False

        mode = str(self.config.get("skills_trigger_mode", "auto") or "auto").strip().lower()
        if mode in {"off", "false", "disabled", "disable", "never", "0"}:
            return False
        if mode in {"always", "all", "on", "true", "1"}:
            return True

        text = (prompt or "").lower()
        if not text.strip():
            return False

        return bool(self._matching_skill_paths(prompt))

    def _skill_frontmatter(self, text: str) -> dict[str, str]:
        if not text.startswith("---"):
            return {}
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, flags=re.DOTALL)
        if not match:
            return {}

        data: dict[str, str] = {}
        current_key = ""
        current_lines: list[str] = []
        for line in match.group(1).splitlines():
            key_match = re.match(r"^([a-zA-Z0-9_-]+):\s*(.*)$", line)
            if key_match:
                if current_key:
                    data[current_key] = "\n".join(current_lines).strip()
                current_key = key_match.group(1).strip().lower()
                current_lines = [key_match.group(2).strip()]
            elif current_key:
                current_lines.append(line.strip())
        if current_key:
            data[current_key] = "\n".join(current_lines).strip()
        return data

    def _skill_keywords_from_text(self, text: str, fallback_name: str) -> list[str]:
        frontmatter = self._skill_frontmatter(text)
        raw = frontmatter.get("keywords", "")
        keywords: list[str] = []

        if raw.startswith("[") and raw.endswith("]"):
            keywords.extend(part.strip().strip("'\"") for part in raw.strip("[]").split(","))
        else:
            for line in raw.splitlines():
                cleaned = line.strip().lstrip("-").strip().strip("'\"")
                if cleaned:
                    keywords.append(cleaned)

        if not keywords:
            keywords.append(fallback_name)
            description = frontmatter.get("description", "")
            keywords.extend(re.findall(r"[\wА-Яа-яЁё.-]{4,}", description)[:6])

        return [keyword.lower() for keyword in keywords if keyword.strip()]

    def _skill_matches_prompt(self, path: Path, prompt: str) -> bool:
        text = (prompt or "").lower()
        if not text.strip():
            return False
        try:
            skill_text = path.read_text(encoding="utf-8", errors="replace")[:2000]
        except Exception:
            return False
        keywords = self._skill_keywords_from_text(skill_text, self._skill_name_from_path(path))
        return any(keyword in text for keyword in keywords)

    def _matching_skill_paths(self, prompt: str = "") -> list[Path]:
        mode = str(self.config.get("skills_trigger_mode", "auto") or "auto").strip().lower()
        skills = self._list_skills()
        if mode in {"always", "all", "on", "true", "1"}:
            return skills
        if mode in {"off", "false", "disabled", "disable", "never", "0"}:
            return []
        return [path for path in skills if self._skill_matches_prompt(path, prompt)]

    def _installed_skill_match_score(self, path: Path, query: str) -> int:
        query = (query or "").lower().strip()
        if not query:
            return 0
        name = self._skill_name_from_path(path).lower()
        safe_query = self._safe_skill_name(query).lower()
        safe_name = self._safe_skill_name(name).lower()
        score = 0
        if safe_query == safe_name:
            score = max(score, 100)
        elif safe_name.startswith(safe_query) or safe_query.startswith(safe_name):
            score = max(score, 80)
        elif safe_query in safe_name or safe_name in safe_query:
            score = max(score, 60)
        try:
            skill_text = path.read_text(encoding="utf-8", errors="replace")[:4000]
        except Exception:
            skill_text = ""
        frontmatter = self._skill_frontmatter(skill_text)
        keywords = self._skill_keywords_from_text(skill_text, self._skill_name_from_path(path))
        query_words = set(re.findall(r"[\wА-Яа-яЁё.-]{3,}", query))
        for keyword in keywords:
            keyword = keyword.lower().strip()
            if not keyword:
                continue
            if keyword in query:
                score = max(score, 50)
            if keyword in query_words:
                score = max(score, 70)
        haystack = " ".join(
            [name, frontmatter.get("description", "")]
            + keywords
        ).lower()
        overlap = sum(1 for word in query_words if word in haystack)
        if overlap:
            score = max(score, min(65, 25 + overlap * 10))
        return score

    def _installed_skill_candidates(self, query: str) -> list[Path]:
        ranked = [
            (self._installed_skill_match_score(path, query), path)
            for path in self._list_skills()
        ]
        return [path for score, path in sorted(ranked, key=lambda item: item[0], reverse=True) if score > 0]

    def _activate_skill_text(self, query: str) -> str:
        query = (query or "").strip()
        if not query:
            return "skill name or query is required"
        candidates = self._installed_skill_candidates(query)
        if not candidates:
            installed = ", ".join(self._skill_name_from_path(path) for path in self._list_skills())
            return "No installed skill matched. Installed skills: " + (installed or "none")
        path = candidates[0]
        text = path.read_text(encoding="utf-8", errors="replace")[:16000]
        return f"Activated OpenAgent skill: {self._skill_name_from_path(path)}\n\n{text}"

    def _load_skills_prompt(self, prompt: str = "") -> str:
        if not self._should_load_skills(prompt):
            return ""

        chunks = []
        for path in self._matching_skill_paths(prompt)[:20]:
            try:
                text = path.read_text(encoding="utf-8")[:4000]
            except Exception:
                continue
            chunks.append(f"## Skill: {self._skill_name_from_path(path)}\n{text}")
        if not chunks:
            return ""
        return "\n\nLoaded OpenAgent skills. Use them when relevant:\n" + "\n\n".join(chunks)

    def _normalize_skill_content(self, name: str, content: str) -> str:
        text = content.strip()
        if text.startswith("---"):
            return text + "\n"

        safe_name = self._safe_skill_name(name)
        first_heading = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
        description = first_heading.group(1).strip() if first_heading else safe_name
        frontmatter = (
            "---\n"
            f"name: {safe_name}\n"
            f"description: {description}\n"
            "---\n\n"
        )
        return frontmatter + text + "\n"

    def _save_skill(self, name: str, content: str) -> str:
        safe_name = self._safe_skill_name(name)
        path = self._skill_path(safe_name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self._normalize_skill_content(safe_name, content), encoding="utf-8")
        return safe_name

    def _skill_repo_base_url(self) -> str:
        return str(
            self.config.get(
                "skill_repo_url",
                "https://raw.githubusercontent.com/hairpin01/repo-MCUB-fork/main/OpenAgent/skills",
            )
            or ""
        ).strip().rstrip("/")

    async def _fetch_text_url(self, url: str, *, max_chars: int = 120000) -> str:
        timeout = aiohttp.ClientTimeout(total=int(self.config["timeout"]))
        headers = {"User-Agent": "OpenAgent/skills"}
        async with aiohttp.ClientSession(timeout=timeout, headers=headers) as session:
            async with session.get(url, allow_redirects=True) as resp:
                text = await resp.text(errors="replace")
                if resp.status >= 400:
                    raise RuntimeError(f"HTTP {resp.status}: {text[:500]}")
                return text[:max_chars]

    async def _fetch_skill_repo_index(self) -> list[dict[str, Any]]:
        base_url = self._skill_repo_base_url()
        if not base_url:
            raise RuntimeError("skill_repo_url is not configured")
        raw = await self._fetch_text_url(f"{base_url}/index.json", max_chars=60000)
        data = json.loads(raw)
        if isinstance(data, dict):
            items = data.get("skills") or []
        elif isinstance(data, list):
            items = data
        else:
            items = []
        return [item for item in items if isinstance(item, dict)]

    def _repo_skill_match_score(self, query: str, item: dict[str, Any]) -> int:
        needle = self._safe_skill_name(query).lower()
        names = [
            str(item.get("name") or ""),
            str(item.get("id") or ""),
            Path(str(item.get("path") or "")).parent.name,
        ]
        names.extend(str(alias) for alias in item.get("aliases") or [] if alias)
        normalized = [self._safe_skill_name(name).lower() for name in names if name]
        if needle in normalized:
            return 100
        if any(value.startswith(needle) for value in normalized):
            return 75
        if any(needle in value for value in normalized):
            return 50
        haystack = " ".join(
            [str(item.get("description") or "")]
            + [str(keyword) for keyword in item.get("keywords") or []]
        ).lower()
        return 25 if query.lower() in haystack else 0

    async def _repo_skill_candidates(self, query: str) -> list[dict[str, Any]]:
        index = await self._fetch_skill_repo_index()
        ranked = [
            (self._repo_skill_match_score(query, item), item)
            for item in index
        ]
        return [item for score, item in sorted(ranked, key=lambda pair: pair[0], reverse=True) if score > 0]

    async def _install_repo_skill(self, name: str) -> str:
        query = (name or "").strip()
        if not query:
            raise RuntimeError(self.strings("skill_name_required"))
        base_url = self._skill_repo_base_url()
        candidates = await self._repo_skill_candidates(query)
        if not candidates:
            raise RuntimeError(self.strings("skill_not_found_repo", query=query))
        item = candidates[0]
        path = str(item.get("path") or f"{self._safe_skill_name(str(item.get('name') or query))}/SKILL.md").lstrip("/")
        content = await self._fetch_text_url(f"{base_url}/{quote(path)}", max_chars=200000)
        saved_name = self._save_skill(str(item.get("name") or query), content)
        return saved_name

    async def _format_skill_repo_list(self) -> str:
        items = await self._fetch_skill_repo_index()
        if not items:
            return "No skills in repository"
        lines = []
        for item in items:
            name = str(item.get("name") or item.get("id") or Path(str(item.get("path") or "")).parent.name or "skill")
            description = str(item.get("description") or "").strip()
            lines.append(f"- {name}: {description}" if description else f"- {name}")
        return "\n".join(lines)

class _OpenAgentTelegramMediaMixin:
    """Telegram entities, files, media and reply-context helpers."""

    async def _fetch_mcub_docs(self) -> str:
        timeout = aiohttp.ClientTimeout(total=int(self.config["timeout"]))
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(self.MCUB_DOCS_URL) as resp:
                text = await resp.text()
                if resp.status >= 400:
                    raise RuntimeError(f"Docs HTTP {resp.status}: {text[:500]}")
                return text[:60000]

    def _format_entity_profile(self, entity: Any) -> str:
        username = f"@{entity.username}" if getattr(entity, "username", None) else ""
        name = " ".join(
            p
            for p in (
                getattr(entity, "first_name", None),
                getattr(entity, "last_name", None),
            )
            if p
        ) or getattr(entity, "title", None) or "Unknown"
        return (
            f"Name: {name}\n"
            f"Username: {username}\n"
            f"ID: {getattr(entity, 'id', None)}\n"
            f"Access hash: {getattr(entity, 'access_hash', None)}\n"
            f"Bot: {getattr(entity, 'bot', None)}\n"
            f"Verified: {getattr(entity, 'verified', None)}\n"
            f"Premium: {getattr(entity, 'premium', None)}\n"
            f"Scam: {getattr(entity, 'scam', None)}\n"
            f"Fake: {getattr(entity, 'fake', None)}\n"
            f"Deleted: {getattr(entity, 'deleted', None)}\n"
            f"Contact: {getattr(entity, 'contact', None)}\n"
            f"Mutual contact: {getattr(entity, 'mutual_contact', None)}\n"
            f"Restricted: {getattr(entity, 'restricted', None)}\n"
            f"Support: {getattr(entity, 'support', None)}\n"
            f"Bot chat history: {getattr(entity, 'bot_chat_history', None)}\n"
            f"Bot no chats: {getattr(entity, 'bot_nochats', None)}\n"
            f"Language code: {getattr(entity, 'lang_code', None)}\n"
            f"Phone visible: {'yes' if getattr(entity, 'phone', None) else 'no'}\n"
            f"Photo object: {getattr(entity, 'photo', None)}\n"
            f"Emoji status: {getattr(entity, 'emoji_status', None)}"
        )

    async def _format_full_profile(self, entity: Any) -> str:
        lines = [self._format_entity_profile(entity)]
        try:
            full = await self.client(GetFullUserRequest(entity))
            full_user = getattr(full, "full_user", None)
            if full_user is not None:
                lines.append(
                    "Full profile:\n"
                    f"About: {getattr(full_user, 'about', None)}\n"
                    f"Common chats count: {getattr(full_user, 'common_chats_count', None)}\n"
                    f"Blocked: {getattr(full_user, 'blocked', None)}\n"
                    f"Phone calls available: {getattr(full_user, 'phone_calls_available', None)}\n"
                    f"Video calls available: {getattr(full_user, 'video_calls_available', None)}\n"
                    f"Voice messages forbidden: {getattr(full_user, 'voice_messages_forbidden', None)}\n"
                    f"Stories pinned available: {getattr(full_user, 'stories_pinned_available', None)}\n"
                    f"Profile photo: {getattr(full_user, 'profile_photo', None)}"
                )
        except Exception as exc:
            lines.append(f"Full profile unavailable: {exc}")

        try:
            photos = await self.client.get_profile_photos(entity, limit=1)
            lines.append(f"Profile photos count fetched: {len(photos)}")
        except Exception as exc:
            lines.append(f"Profile photos unavailable: {exc}")

        try:
            directory = Path.cwd() / "openagent_profiles"
            directory.mkdir(parents=True, exist_ok=True)
            path = await self.client.download_profile_photo(
                entity,
                file=str(directory / f"profile_{getattr(entity, 'id', 'unknown')}.jpg"),
            )
            if path:
                lines.append(
                    "Avatar: Telegram does not expose a permanent public avatar URL via client API.\n"
                    f"Avatar local file: {path}"
                )
            else:
                lines.append("Avatar: no accessible profile photo")
        except Exception as exc:
            lines.append(f"Avatar download failed: {exc}")

        try:
            common = await self.client.get_common_chats(entity, limit=10)
            if common:
                formatted = []
                for chat in common:
                    title = getattr(chat, "title", None) or getattr(chat, "first_name", None) or "Unknown"
                    username = f"@{chat.username}" if getattr(chat, "username", None) else ""
                    formatted.append(f"{title} {username} [id={getattr(chat, 'id', None)}]".strip())
                lines.append("Common chats:\n" + "\n".join(formatted))
        except Exception:
            pass

        return "\n\n".join(lines)

    def _safe_generated_filename(self, filename: str) -> str:
        filename = Path(filename.strip() or "generated.py").name
        filename = re.sub(r"[^A-Za-z0-9_.-]+", "_", filename).strip("._")
        if not filename:
            filename = "generated.py"
        if "." not in filename:
            filename += ".py"
        return filename[:96]

    def _extract_generated_file(self, answer: str, fallback_name: str = "generated.py") -> tuple[str, str]:
        match = self.GENERATED_FILE_RE.search(answer or "")
        if match:
            return self._safe_generated_filename(match.group(1)), match.group(2).strip("\n")

        fence = re.search(r"```([A-Za-z0-9_+.-]*)\n(.*?)```", answer or "", re.DOTALL)
        if fence:
            lang = (fence.group(1) or "").lower()
            ext = {
                "python": ".py",
                "py": ".py",
                "javascript": ".js",
                "js": ".js",
                "typescript": ".ts",
                "ts": ".ts",
                "html": ".html",
                "css": ".css",
                "json": ".json",
                "yaml": ".yaml",
                "yml": ".yml",
                "bash": ".sh",
                "sh": ".sh",
                "sql": ".sql",
                "md": ".md",
                "markdown": ".md",
            }.get(lang, Path(fallback_name).suffix or ".txt")
            return self._safe_generated_filename("generated" + ext), fence.group(2).strip("\n")

        return self._safe_generated_filename(fallback_name), (answer or "").strip()

    def _is_text_file(self, mime_type: str, file_name: str) -> bool:
        if mime_type.startswith("text/"):
            return True
        suffix = Path(file_name or "").suffix.lower()
        return suffix in {
            ".txt",
            ".md",
            ".py",
            ".js",
            ".ts",
            ".tsx",
            ".jsx",
            ".json",
            ".yaml",
            ".yml",
            ".toml",
            ".ini",
            ".cfg",
            ".csv",
            ".log",
            ".xml",
            ".html",
            ".css",
            ".sh",
            ".sql",
        }

    async def _extract_video_frame(self, data: bytes, suffix: str) -> bytes | None:
        suffix = suffix if suffix.startswith(".") else ".webm"
        with tempfile.TemporaryDirectory(prefix="openagent_media_") as tmp:
            src = Path(tmp) / f"input{suffix}"
            dst = Path(tmp) / "frame.png"
            src.write_bytes(data)
            proc = await asyncio.create_subprocess_exec(
                "ffmpeg",
                "-y",
                "-i",
                str(src),
                "-frames:v",
                "1",
                "-vf",
                "scale='min(1024,iw)':-1",
                str(dst),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            try:
                await asyncio.wait_for(proc.communicate(), timeout=15)
            except asyncio.TimeoutError:
                proc.kill()
                await proc.communicate()
                return None
            if proc.returncode != 0 or not dst.exists():
                return None
            return dst.read_bytes()

    async def _reply_context(
        self, event: Event
    ) -> tuple[str, list[dict[str, str]]]:
        reply = await event.get_reply_message()
        if not reply:
            return "", []

        parts = []
        attachments: list[dict[str, str]] = []
        try:
            sender = await reply.get_sender()
        except Exception:
            sender = None
        if sender is not None:
            parts.append("Replied sender profile:\n" + self._format_entity_profile(sender))

        reply_text = getattr(reply, "raw_text", None) or getattr(reply, "text", "") or ""
        if reply_text:
            parts.append(f"Replied message text:\n{reply_text[:12000]}")

        if not getattr(reply, "media", None):
            return "\n\n".join(parts), attachments

        file_obj = getattr(reply, "file", None)
        file_name = getattr(file_obj, "name", None) or "attachment"
        mime_type = getattr(file_obj, "mime_type", None) or mimetypes.guess_type(file_name)[0] or "application/octet-stream"
        size = getattr(file_obj, "size", None) or 0
        parts.append(f"Replied media: name={file_name}, mime={mime_type}, size={size}")

        try:
            data = await reply.download_media(file=bytes)
        except Exception as exc:
            parts.append(f"Could not download replied media: {exc}")
            return "\n\n".join(parts), attachments

        if not data:
            return "\n\n".join(parts), attachments

        if self._is_text_file(mime_type, file_name):
            text = data.decode("utf-8", errors="replace")
            parts.append(f"File content ({file_name}):\n{text[:20000]}")
            return "\n\n".join(parts), attachments

        if len(data) > int(self.config["media_max_bytes"]):
            parts.append("Media is too large to send to AI; metadata only was included.")
            return "\n\n".join(parts), attachments

        if mime_type.startswith("video/"):
            frame = await self._extract_video_frame(data, Path(file_name).suffix or ".webm")
            if frame:
                attachments.append(
                    {
                        "name": f"{file_name}_first_frame.png",
                        "mime_type": "image/png",
                        "data": base64.b64encode(frame).decode("ascii"),
                    }
                )
                parts.append("First frame extracted from replied video/sticker and attached as image.")
            else:
                attachments.append(
                    {
                        "name": file_name,
                        "mime_type": mime_type,
                        "data": base64.b64encode(data).decode("ascii"),
                    }
                )
                parts.append("Could not extract video frame; raw video attached only for providers that support it.")
        elif mime_type.startswith(("image/", "audio/")):
            attachments.append(
                {
                    "name": file_name,
                    "mime_type": mime_type,
                    "data": base64.b64encode(data).decode("ascii"),
                }
            )
            parts.append("Media bytes attached to AI request when provider supports it.")
        else:
            parts.append("Unsupported binary media type; metadata only was included.")
        return "\n\n".join(parts), attachments

    def _build_openai_content(
        self, prompt: str, attachments: list[dict[str, str]]
    ) -> str | list[dict[str, Any]]:
        if not attachments:
            return prompt
        content: list[dict[str, Any]] = [{"type": "text", "text": prompt}]
        skipped = []
        for item in attachments:
            mime_type = item["mime_type"]
            if mime_type.startswith("image/"):
                content.append(
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{mime_type};base64,{item['data']}"
                        },
                    }
                )
            else:
                skipped.append(f"{item['name']} ({mime_type})")
        if skipped:
            content[0]["text"] += "\n\nProvider note: non-image media not sent to OpenAI-compatible endpoint: " + ", ".join(skipped)
        return content

    def _build_google_parts(
        self, content: str | list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        if isinstance(content, str):
            return [{"text": content}]
        parts = []
        for item in content:
            if item.get("type") == "text":
                parts.append({"text": item.get("text", "")})
            elif item.get("type") == "media":
                parts.append(
                    {
                        "inline_data": {
                            "mime_type": item["mime_type"],
                            "data": item["data"],
                        }
                    }
                )
        return parts or [{"text": ""}]

    def _build_google_content(
        self, prompt: str, attachments: list[dict[str, str]]
    ) -> str | list[dict[str, Any]]:
        if not attachments:
            return prompt
        content: list[dict[str, Any]] = [{"type": "text", "text": prompt}]
        for item in attachments:
            content.append({"type": "media", **item})
        return content

    def _parse_xml_attrs(self, attrs: str) -> dict[str, str]:
        parsed: dict[str, str] = {}
        for key, value in re.findall(r"([a-zA-Z_][\w.-]*)=[\"']([^\"']*)[\"']", attrs or ""):
            parsed[key.lower()] = html.unescape(value.strip())
        return parsed

    async def _fetch_url_bytes(self, url: str) -> tuple[bytes, str] | None:
        timeout = aiohttp.ClientTimeout(total=int(self.config["timeout"]))
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as resp:
                if resp.status >= 400:
                    return None
                data = await resp.read()
                content_type = resp.headers.get("Content-Type", "image/jpeg").split(";")[0]
                return data, content_type

    async def _set_channel_avatar(
        self,
        channel: Any,
        attrs: dict[str, str],
        source_event: Any | None,
    ) -> str | None:
        data: bytes | None = None
        mime_type = "image/jpeg"
        avatar_url = attrs.get("avatar_url") or attrs.get("avatar") or attrs.get("photo_url")
        if avatar_url:
            fetched = await self._fetch_url_bytes(avatar_url)
            if fetched:
                data, mime_type = fetched
        elif source_event is not None and attrs.get("avatar_reply", "").lower() in {"1", "true", "yes"}:
            reply = await source_event.get_reply_message()
            if reply and getattr(reply, "media", None):
                data = await reply.download_media(file=bytes)
                file_obj = getattr(reply, "file", None)
                mime_type = getattr(file_obj, "mime_type", None) or "image/jpeg"

        if not data:
            return None
        if not mime_type.startswith("image/"):
            return "avatar skipped: media is not an image"
        ext = mimetypes.guess_extension(mime_type) or ".jpg"
        buf = io.BytesIO(data)
        buf.name = f"avatar{ext}"
        uploaded = await self.client.upload_file(buf)
        await self.client(EditPhotoRequest(channel=channel, photo=uploaded))
        return "avatar set"

    async def _resolve_tool_chat(self, chat: str | None, source_event: Any | None) -> Any:
        await asyncio.sleep(0)
        chat = (chat or "").strip()
        if not chat or chat.lower() in {"current", "this", "here"}:
            chat_id = self._event_chat_id(source_event)
            if chat_id is not None:
                return chat_id
            return "me"
        try:
            return int(chat)
        except ValueError:
            return chat

    async def _resolve_tool_user(self, user: str | None, source_event: Any | None) -> Any:
        user = (user or "").strip()
        if user:
            try:
                return int(user)
            except ValueError:
                return user
        if source_event is not None:
            reply = await source_event.get_reply_message()
            if reply:
                sender = await reply.get_sender()
                if sender is not None:
                    return sender
        raise ValueError("user is required or reply to a user's message")

    def _format_sender_short(self, sender: Any) -> str:
        if sender is None:
            return "Unknown"
        username = f"@{sender.username}" if getattr(sender, "username", None) else ""
        name = " ".join(
            p
            for p in (getattr(sender, "first_name", None), getattr(sender, "last_name", None))
            if p
        ) or getattr(sender, "title", None) or "Unknown"
        return f"{name} {username}".strip()

    async def _message_id_from_attrs(
        self, attrs: dict[str, str], body: str, source_event: Any | None
    ) -> int | None:
        raw = attrs.get("id") or attrs.get("message_id") or body.strip()
        if raw and raw.lower() not in {"reply", "replied"}:
            try:
                return int(raw.split(",")[0].strip())
            except ValueError:
                return None
        if source_event is not None:
            reply = await source_event.get_reply_message()
            if reply:
                return getattr(reply, "id", None)
        return None


class _OpenAgentStatusMixin:
    """Inline status UI, confirmations and dangerous-tool gating."""

    async def _show_agent_action(
        self,
        event: Any,
        title: str,
        value: str,
        log: list[str],
        tool_name: str = "",
        elapsed: float | None = None,
        thinking_notes: list[str] | None = None,
        tool_done: bool = False,
    ) -> None:
        text = self._render_tool_display(
            title=title,
            tool_name=tool_name,
            value=value,
            log=log,
            elapsed=elapsed,
            thinking_notes=thinking_notes,
            tool_done=tool_done,
        )
        try:
            buttons = getattr(event, "_openagent_status_buttons", None)
            if buttons is not None and hasattr(event, "edit"):
                self.log.debug(
                    "OA show_action EDIT_FORM: tool=%s has_buttons=%s title_len=%d",
                    tool_name, bool(buttons), len(text),
                )
                await event.edit(text, buttons=buttons, parse_mode="html")
            else:
                self.log.debug(
                    "OA show_action FALLBACK_EDIT: tool=%s has_edit=%s has_buttons=%s",
                    tool_name, hasattr(event, "edit"), buttons is not None,
                )
                await self.edit(event, text, as_html=True)
        except Exception as exc:
            self.log.debug(
                "OA show_action EXCEPTION: tool=%s error=%s", tool_name, exc,
            )
            await self.edit(event, html.escape(title), as_html=True)

    def _dangerous_terminal_command(self, command: str) -> bool:
        command = (command or "").lower().strip()
        if not command:
            return False
        compact = re.sub(r"\s+", " ", command)
        dangerous_patterns = [
            r"\brm\s+-[a-z]*[rf][a-z]*\s+/(?:\s|$|\*)",
            r"\brm\s+-[a-z]*[rf][a-z]*\s+--no-preserve-root\b",
            r"\bsudo\s+rm\s+-[a-z]*[rf][a-z]*\s+/(?:\s|$|\*)",
            r"\bmkfs(?:\.[a-z0-9]+)?\b",
            r"\bdd\b.*\bof=/dev/",
            r"\b(shutdown|reboot|poweroff|halt)\b",
            r">\s*/dev/(sd[a-z]|nvme\d+n\d+|mapper/)",
        ]
        return any(re.search(pattern, compact) for pattern in dangerous_patterns)

    def _requires_tool_confirmation(self, tool_name: str, attrs_raw: str = "", body: str = "") -> bool:
        if not bool(self.config.get("tool_confirmation_enabled", True)):
            return False
        name = (tool_name or "").lower().strip()
        group = self._tool_group(name)

        plugin = self._get_plugin_for_tool(name)
        if plugin is not None:
            plugin_dangerous = getattr(plugin, "dangerous_tools", None)
            if isinstance(plugin_dangerous, set):
                if name in plugin_dangerous:
                    return True
            elif isinstance(plugin_dangerous, dict):
                tool_level = plugin_dangerous.get(name)
                if tool_level is not None:
                    return tool_level != "safe"
        safe_read_tools = {
            "message.get", "message.search", "message.history", "message.typing",
            "dialog.list_private", "dialog.list_groups", "dialog.list_all", "dialog.search",
            "chat.info", "chat.participants", "chat.admins", "chat.permissions", "chat.common_with_user",
            "profile.get", "profile.get_full", "profile.get_me", "profile.get_photos", "profile.common_chats",
            "context.reply_context", "context.media_context", "skills.list", "skills.read", "skills.activate",
            "skills.repo_list", "utility.token_usage", "utility.placeholders", "utility.random_template",
            "todo.add", "todo.delete", "todo.edit", "todo.current", "todo.close", "todo.closeall", "todo.clear",
            "thinking.note",
        }
        if name in safe_read_tools:
            return False

        mode = str(self.config.get("tool_confirmation_mode", "medium") or "medium").lower().strip()
        attrs = self._parse_xml_attrs(attrs_raw)
        command = body.strip() or attrs.get("command") or attrs.get("cmd") or attrs.get("query") or attrs.get("text") or ""
        low_tools = {
            "profile.update_name", "profile.update_bio", "profile.update_username", "profile.set_photo",
            "contacts.add", "contacts.delete", "contacts.block", "contacts.unblock",
        }
        critical_tools = {
            "terminal.run", "terminal.inspect",
            "mcub.command", "mcub.install", "mcub.reload",
            "message.send_current", "message.send_target", "message.edit", "message.delete",
            "message.forward", "message.pin", "message.schedule", "message.draft",
            "file.send", "file.download_media", "file.attach_image", "file.attach_video",
            "moderation.mute", "moderation.unmute", "moderation.ban", "moderation.unban",
            "moderation.kick", "moderation.promote", "moderation.demote", "moderation.pin",
            "moderation.delete_messages",
            "profile.update_name", "profile.update_bio", "profile.update_username", "profile.set_photo",
            "contacts.add", "contacts.delete", "contacts.block", "contacts.unblock",
            "creation.channel", "creation.group", "creation.bot", "creation.channel_avatar", "creation.private_invite",
            "chat.set_title", "chat.set_about", "chat.set_username", "chat.slowmode", "chat.invite_link",
            "dialog.archive", "dialog.unarchive", "dialog.leave", "dialog.set_photo",
            "context.clear",
            "skills.install", "skills.import_md", "skills.save_from_ai",
            "code.generate_file", "code.generate_mcub_module", "code.attach_result",
        }
        medium_groups = {
            "terminal", "mcub", "message", "file", "moderation", "profile",
            "contacts", "creation", "chat", "dialog", "context", "skills", "code",
        }
        if mode == "low":
            return name in low_tools or self._dangerous_terminal_command(command)
        if mode == "high":
            return group not in {"utility", "thinking"}
        return name in critical_tools or group in medium_groups


    async def _confirm_dangerous_tool(
        self,
        event: Any,
        tool_name: str,
        value: str,
        *,
        elapsed: float | None = None,
    ) -> bool:
        token = str(uuid.uuid4())
        loop = asyncio.get_running_loop()
        future: asyncio.Future[bool] = loop.create_future()
        self._tool_confirmation_waiters[token] = future
        safe_tool = html.escape(tool_name or "tool")
        safe_value = html.escape((value or "").strip()[:1800])
        elapsed_value = f"{elapsed:.1f}" if elapsed is not None else "0.0"
        elapsed_line = f"\n⏳ {elapsed_value}s" if elapsed is not None else ""
        template = str(self.config.get("tool_confirmation_template", "") or "").strip()
        if not template:
            template = "<blockquote><a href=\"tg://emoji?id=6010201728773790293\">😈</a> Continue?\n<a href=\"tg://emoji?id=6012317326584583729\">😐</a> Tool: {tool} • {elapsed}s</blockquote>\n<blockquote expandable><a href=\"tg://emoji?id=6010394680179562842\">😶</a> <b>What will be completed</b>\n<a href=\"tg://emoji?id=6010292550152230657\">☀️</a> <code>{value}</code></blockquote>"
        body = template
        for key, item in {
            "tool": safe_tool,
            "value": safe_value,
            "elapsed": html.escape(elapsed_value),
            "elapsed_line": elapsed_line,
        }.items():
            body = body.replace("{" + key + "}", item)
        buttons = [[
            self.Button.inline(
                str(self.config.get("tool_confirmation_yes_text", "") or self.strings("tool_confirmation_yes_text")),
                self._confirm_tool_action,
                args=(token, True),
                style="primary",
            ),
            self.Button.inline(
                str(self.config.get("tool_confirmation_no_text", "") or self.strings("tool_confirmation_no_text")),
                self._confirm_tool_action,
                args=(token, False),
                style="danger",
            ),
        ]]
        try:
            if hasattr(event, "edit"):
                await event.edit(body, buttons=buttons, parse_mode="html")
            else:
                await self.edit(event, body, as_html=True)
            return await asyncio.wait_for(
                future,
                timeout=int(self.config.get("tool_confirmation_timeout", 900) or 900),
            )
        except asyncio.TimeoutError:
            return False
        except Exception:
            return False
        finally:
            self._tool_confirmation_waiters.pop(token, None)


    async def _start_inline_status(
        self,
        event: Any,
        text: str,
        buttons: list[list[Any]],
    ) -> Any:
        async def edit_with_status_buttons(target_event: Any) -> Any:
            result = target_event
            edited_ok = False
            if hasattr(target_event, "edit"):
                with contextlib.suppress(Exception):
                    edited = await target_event.edit(
                        text,
                        buttons=buttons,
                        parse_mode="html",
                    )
                    result = edited or target_event
                    edited_ok = True
            if not edited_ok:
                with contextlib.suppress(Exception):
                    result = await self.edit(target_event, text, as_html=True)
            for candidate in (target_event, result):
                with contextlib.suppress(Exception):
                    setattr(candidate, "_openagent_status_buttons", buttons)
                with contextlib.suppress(Exception):
                    setattr(candidate, "_openagent_source_chat_id", getattr(event, "chat_id", None))
            return result or target_event

        chat_id = getattr(event, "chat_id", None) or getattr(event, "_openagent_source_chat_id", None)
        target = await self._inline_target(event, chat_id)
        if not target:
            return await edit_with_status_buttons(event)

        token = str(uuid.uuid4())
        loop = asyncio.get_running_loop()
        future: asyncio.Future[Any] = loop.create_future()
        self._inline_status_waiters[token] = future
        try:
            _unit, sms = await self.inline(
                target,
                text,
                buttons=[[self.Button.inline(" ", self._activate_inline_status, args=(token,), style="primary")]],
                ttl=900,
                parse_mode="html",
                reply_to=getattr(event, "reply_to", None),
            )
            self.log.debug(
                "OA inline_status: chat_id=%s inline_sms=%s ttl=900", chat_id, bool(sms),
            )
            if sms:
                with contextlib.suppress(Exception):
                    await sms.click(0)
            try:
                call = await asyncio.wait_for(future, timeout=5)
            except asyncio.TimeoutError:
                call = sms or event
            await edit_with_status_buttons(call)
            with contextlib.suppress(Exception):
                await event.delete()
            result = call or sms or event
            self.log.debug(
                "OA inline_status OK: chat_id=%s result_type=%s has_edit=%s has_buttons=%s",
                chat_id, type(result).__name__,
                hasattr(result, "edit"),
                hasattr(result, "_openagent_status_buttons"),
            )
            return result
        except Exception as exc:
            self.log.debug(
                "OA inline_status FALLBACK: chat_id=%s error=%s",
                chat_id, exc,
            )
            return await edit_with_status_buttons(event)
        finally:
            self._inline_status_waiters.pop(token, None)


class _OpenAgentAgentLoopMixin:
    """Agent loop, tool-call parsing and provider HTTP calls."""

    def _is_provider_timeout_error(self, exc: BaseException) -> bool:
        text = str(exc).lower()
        return isinstance(exc, (TimeoutError, asyncio.TimeoutError)) or "timed out" in text or "timeout" in text

    async def _ask_provider_once(
        self,
        provider: str,
        messages: list[dict[str, Any]],
        api_key: str,
        *,
        max_tokens_override: int | None = None,
    ) -> str:
        if provider in ("openai", "openrouter", "groq", "deepseek", "xai", "other"):
            return await self._ask_openai_compatible(
                provider,
                messages,
                api_key,
                max_tokens_override=max_tokens_override,
            )
        if provider == "google":
            return await self._ask_google(
                messages,
                api_key,
                max_tokens_override=max_tokens_override,
            )
        raise RuntimeError(self.strings("bad_provider", providers=", ".join(self.PROVIDERS)))

    async def _ask_provider_with_reconnect(
        self,
        provider: str,
        messages: list[dict[str, Any]],
        api_key: str,
        *,
        status_event: Any | None = None,
        agent_log: list[str] | None = None,
        started_at: float | None = None,
        thinking_notes: list[str] | None = None,
        max_tokens_override: int | None = None,
    ) -> str:
        max_reconnects = max(0, min(int(self.config.get("provider_reconnect_attempts", 5) or 0), 5))
        attempt = 0
        while True:
            try:
                return await self._ask_provider_once(
                    provider,
                    messages,
                    api_key,
                    max_tokens_override=max_tokens_override,
                )
            except Exception as exc:
                if not self._is_provider_timeout_error(exc) or attempt >= max_reconnects:
                    raise
                attempt += 1
                reconnect_label = f"provider.reconnect {attempt}/{max_reconnects}"
                if agent_log is not None:
                    agent_log.append(reconnect_label)
                if status_event is not None:
                    with contextlib.suppress(Exception):
                        await self._show_agent_action(
                            status_event,
                            f"Reconnect {attempt}/{max_reconnects}",
                            str(exc),
                            agent_log or [reconnect_label],
                            tool_name="reconnect",
                            elapsed=(time.monotonic() - started_at) if started_at else None,
                            thinking_notes=thinking_notes,
                        )
                await asyncio.sleep(1)

    async def _ask_agent(
        self,
        prompt: str,
        status_event: Any | None = None,
        source_event: Any | None = None,
        attachments: list[dict[str, str]] | None = None,
        cancel_token: str | None = None,
        system_override: str | None = None,
        started_at: float | None = None,
        flash_mode: bool = False,
    ) -> tuple[str, list[str], list[str], list[dict[str, str]]]:
        provider = self._provider()
        api_key = self._api_key()
        if not api_key:
            raise RuntimeError(self.strings("no_key"))

        attachments = attachments or []
        if provider == "google":
            user_content = self._build_google_content(prompt, attachments)
        else:
            user_content = self._build_openai_content(prompt, attachments)

        chat_id = self._event_chat_id(source_event)
        compacted_context = False if flash_mode else await self._compact_chat_history_if_needed(chat_id, provider, api_key)
        history = self._history_for_chat(chat_id)
        if flash_mode:
            history = history[-2:]
        messages: list[dict[str, Any]] = [
            {"role": "system", "content": system_override or self._system_prompt(prompt, flash_mode=flash_mode)}
        ]
        tool_memory = "" if flash_mode else self._tool_memory_prompt(chat_id)
        if tool_memory:
            messages.append({"role": "system", "content": tool_memory})
        messages.extend(history)
        messages.append({"role": "user", "content": user_content})

        agent_log: list[str] = []
        tool_trace: list[dict[str, str]] = []
        if compacted_context:
            agent_log.append("context.compact")
        thinking_notes: list[str] = []
        max_steps = self.AGENT_MAX_STEPS  # Architectural limit for tool chaining in 0.5.0
        invalid_tool_retries = 0
        answer = ""

        if cancel_token and cancel_token in self._cancelled_generations:
            raise RuntimeError("Generation cancelled")
        think_messages: list[dict[str, Any]] = [
            {"role": "system", "content": self._thinking_system_prompt(flash_mode=flash_mode)}
        ]
        think_messages.extend(history)
        think_messages.append({"role": "user", "content": user_content})
        think_answer = await self._ask_provider_with_reconnect(
            provider,
            think_messages,
            api_key,
            status_event=status_event,
            agent_log=agent_log,
            started_at=started_at,
            thinking_notes=thinking_notes,
        )

        think_calls = [
            call
            for call in self._extract_tool_calls(think_answer or "")
            if (call[0] or "").lower().strip() == "thinking.note"
        ]
        thinking_outputs: list[str] = []
        for tool_name, attrs_raw, body in think_calls[:1]:
            if cancel_token and cancel_token in self._cancelled_generations:
                raise RuntimeError("Generation cancelled")
            output = await self._dispatch_tool(
                tool_name,
                attrs_raw,
                body,
                source_event,
                status_event,
                agent_log,
                started_at=started_at,
                thinking_notes=thinking_notes,
            )
            self._remember_tool_output(chat_id, tool_name, output)
            thinking_outputs.append(
                f"Tool <{tool_name}> call:\n"
                f"attrs: {attrs_raw or '-'}\n"
                f"body: {body or '-'}\n"
                f"output:\n{output}"
            )
        if thinking_outputs:
            think_assistant_msg = {"role": "assistant", "content": think_answer or ""}
            think_output_msg = {
                "role": "user",
                "content": "\n\n".join(thinking_outputs) + "\n\nNow proceed with the actual task.",
            }
            messages.append(think_assistant_msg)
            messages.append(think_output_msg)
            tool_trace.append(
                {
                    "role": "assistant",
                    "content": "OpenAgent tool trace:\n" + "\n\n".join(thinking_outputs),
                }
            )

        if flash_mode:
            if cancel_token and cancel_token in self._cancelled_generations:
                raise RuntimeError("Generation cancelled")
            answer = await self._ask_provider_with_reconnect(
                provider,
                messages,
                api_key,
                status_event=status_event,
                agent_log=agent_log,
                started_at=started_at,
                thinking_notes=thinking_notes,
            )
            return (answer or "").strip(), agent_log, thinking_notes, tool_trace

        for _ in range(max_steps):
            if cancel_token and cancel_token in self._cancelled_generations:
                raise RuntimeError("Generation cancelled")
            runtime_comment = self._runtime_comment_message(cancel_token)
            if runtime_comment:
                messages.append(runtime_comment)
                agent_log.append("user.comment")

            answer = await self._ask_provider_with_reconnect(
                provider,
                messages,
                api_key,
                status_event=status_event,
                agent_log=agent_log,
                started_at=started_at,
                thinking_notes=thinking_notes,
            )

            tool_calls = self._extract_tool_calls(answer or "")
            if not tool_calls:
                tool_error = self._invalid_tool_call_error(answer or "")
                if tool_error:
                    invalid_tool_retries += 1
                    agent_log.append(f"tool_error: {tool_error[:220]}")
                    if invalid_tool_retries > 2:
                        return tool_error, agent_log, thinking_notes, tool_trace
                    messages.append({"role": "assistant", "content": answer or ""})
                    messages.append(
                        {
                            "role": "user",
                            "content": f"{tool_error}\n\n"
                            + self.strings("tool_validation_retry_prompt"),
                        }
                    )
                    continue
                clean_answer = (answer or "").strip()
                runtime_comment = self._runtime_comment_message(cancel_token)
                if runtime_comment:
                    messages.append({"role": "assistant", "content": answer or ""})
                    messages.append(runtime_comment)
                    agent_log.append("user.comment")
                    continue
                if clean_answer or not agent_log:
                    return clean_answer, agent_log, thinking_notes, tool_trace
                break
            invalid_tool_retries = 0

            outputs: list[str] = []
            for tool_name, attrs_raw, body in tool_calls:
                if cancel_token and cancel_token in self._cancelled_generations:
                    raise RuntimeError("Generation cancelled")
                output = await self._dispatch_tool(
                    tool_name,
                    attrs_raw,
                    body,
                    source_event,
                    status_event,
                    agent_log,
                    started_at=started_at,
                    thinking_notes=thinking_notes,
                )
                self._remember_tool_output(chat_id, tool_name, output)
                outputs.append(
                    f"Tool <{tool_name}> call:\n"
                    f"attrs: {attrs_raw or '-'}\n"
                    f"body: {body or '-'}\n"
                    f"output:\n{output}"
                )

            assistant_tool_msg = {"role": "assistant", "content": answer}
            messages.append(assistant_tool_msg)
            followup = "\n\n".join(outputs)
            if any(name != "thinking.note" for name, _attrs, _body in tool_calls):
                followup += (
                    "\n\nProgress reminder: if you need more tools, include a fresh thinking.note "
                    "with the next tool_call batch unless the task is ready for the final answer."
                )
            tool_output_msg = {"role": "user", "content": followup}
            messages.append(tool_output_msg)
            if outputs:
                tool_trace.append(
                    {
                        "role": "assistant",
                        "content": "OpenAgent tool trace:\n" + "\n\n".join(outputs),
                    }
                )
        # Force one final pass without tool calls if tool-chain limit was reached.
        messages.append(
            {
                "role": "user",
                "content": (
                    "Stop using tools. Give the final user-facing answer now, in plain text only. "
                    "Do not output tool_call fenced blocks, XML tags, or tool calls."
                ),
            }
        )
        answer = await self._ask_provider_with_reconnect(
            provider,
            messages,
            api_key,
            status_event=status_event,
            agent_log=agent_log,
            started_at=started_at,
            thinking_notes=thinking_notes,
        )
        clean = (answer or "").strip()
        if not clean and provider in ("openai", "openrouter", "groq", "deepseek", "xai", "other") and self._uses_completion_tokens(provider):
            max_tokens = int(self.config["max_tokens"])
            if int(self._last_token_usage.get("output_tokens", 0) or 0) >= max_tokens:
                messages.append(
                    {
                        "role": "user",
                        "content": (
                            "Your previous final answer was empty because the completion budget was exhausted. "
                            "Answer now in 800 characters or less. Plain text only. No tools."
                        ),
                    }
                )
                answer = await self._ask_provider_with_reconnect(
                    provider,
                    messages,
                    api_key,
                    status_event=status_event,
                    agent_log=agent_log,
                    started_at=started_at,
                    thinking_notes=thinking_notes,
                    max_tokens_override=max(4096, max_tokens * 2),
                )
                clean = (answer or "").strip()
        if clean:
            return clean, agent_log, thinking_notes, tool_trace
        return self.strings("tools_no_final"), agent_log, thinking_notes, tool_trace

    def _tool_names(self) -> set[str]:
        """Single whitelist source for executable tool names and aliases."""
        return set(self._get_tool_map())

    def _json_tool_to_legacy(self, payload: dict[str, Any]) -> tuple[str, str, str] | None:
        """Convert the new JSON tool protocol into legacy attrs/body for handlers."""
        tool_name = str(payload.get("tool") or payload.get("name") or "").lower().strip()
        if tool_name not in self._tool_names():
            return None
        args_raw = payload.get("args") or {}
        if not isinstance(args_raw, dict):
            args_raw = {}
        body_value = payload.get("body")
        if body_value is None:
            for key in ("body", "content", "text", "message", "command", "query", "prompt"):
                if key in args_raw:
                    body_value = args_raw.get(key)
                    break
        body = "" if body_value is None else str(body_value)
        attrs: list[str] = []
        for key, value in args_raw.items():
            if value is None or key == "body":
                continue
            if isinstance(value, (dict, list, tuple)):
                value = json.dumps(value, ensure_ascii=False)
            safe_key = re.sub(r"[^a-zA-Z0-9_.-]", "_", str(key).strip())
            if not safe_key:
                continue
            attrs.append(f'{safe_key}="{html.escape(str(value), quote=True)}"')
        return tool_name, " ".join(attrs), body

    def _iter_json_tool_payloads(self, raw: str) -> list[dict[str, Any]]:
        """Parse one JSON tool payload or a list of payloads without raising."""
        try:
            payload = json.loads((raw or "").strip())
        except Exception:
            return []
        payloads = payload if isinstance(payload, list) else [payload]
        return [item for item in payloads if isinstance(item, dict)]

    def _codex_recipient_tool_name(self, header: str) -> str:
        """Return a registry tool name from a Harmony `to=...` header when possible."""
        match = re.search(r"(?:^|\s)to=([^\s<]+)", header or "")
        if not match:
            return ""
        recipient = match.group(1).strip().strip('"\'').lower()
        aliases = {
            "tool.send_message": "message.send_current",
            "tool.send_current": "message.send_current",
            "tool.thinking_note": "thinking.note",
            "tool.thinking.note": "thinking.note",
        }
        if recipient in aliases:
            return aliases[recipient]
        if recipient.startswith("tool."):
            recipient = recipient[5:]
        return recipient if recipient in self._tool_names() else ""

    def _extract_codex_tool_calls(self, text: str) -> list[tuple[str, str, str]]:
        """Extract Codex/OpenAI Harmony style tool JSON from raw model text.

        Some local OpenAI-compatible models do not follow the fenced `tool_call`
        instruction and instead emit text like:
        `<|start|>assistant<|channel|>commentary ... <|message|>{...}<|call|>`.
        Treat the JSON between `<|message|>` and `<|call|>` as a normal tool
        payload so it is executed instead of being shown to the user.
        """
        calls: list[tuple[str, str, str]] = []
        pattern = r"(?P<header>.*?)<\|message\|>(?P<body>.*?)(?:<\|call\|>|$)"
        for match in re.finditer(pattern, text or "", re.DOTALL):
            fallback_tool = self._codex_recipient_tool_name(match.group("header"))
            raw = match.group("body").strip()
            if not raw:
                continue
            for item in self._iter_json_tool_payloads(raw):
                if fallback_tool and not (item.get("tool") or item.get("name")):
                    item = {**item, "tool": fallback_tool}
                tool_call = self._json_tool_to_legacy(item)
                if tool_call:
                    calls.append(tool_call)
        return calls

    def _extract_json_tool_calls(self, text: str) -> list[tuple[str, str, str]]:
        calls: list[tuple[str, str, str]] = []
        stripped = (text or "").strip()
        if stripped.startswith("{") or stripped.startswith("["):
            for item in self._iter_json_tool_payloads(stripped):
                tool_call = self._json_tool_to_legacy(item)
                if tool_call:
                    calls.append(tool_call)
        for match in self.TOOL_CALL_JSON_RE.finditer(text or ""):
            raw = match.group(1).strip()
            if not raw:
                continue
            for item in self._iter_json_tool_payloads(raw):
                tool_call = self._json_tool_to_legacy(item)
                if tool_call:
                    calls.append(tool_call)
        return calls

    def _invalid_tool_call_error(self, text: str) -> str:
        """Return a user-facing error when the model attempted an invalid tool call."""
        # First check: did the model put a real tool call inside thinking.note?
        for match in self.TOOL_CALL_JSON_RE.finditer(text or ""):
            raw = match.group(1).strip()
            for item in self._iter_json_tool_payloads(raw):
                tool_name = str(item.get("tool") or item.get("name") or "").lower().strip()
                if tool_name == "thinking.note":
                    note_val = ""
                    args = item.get("args") or {}
                    if isinstance(args, dict):
                        note_val = str(args.get("note") or args.get("text") or "").strip()
                    if not note_val:
                        note_val = str(item.get("body") or "").strip()
                    embedded = self._extract_json_tool_calls(note_val)
                    real = [c for c in embedded if c[0] != "thinking.note"]
                    if real:
                        names = ", ".join(c[0] for c in real)
                        return (
                            f"[FORMAT ERROR] You put tool call(s) ({names}) inside thinking.note. "
                            "They were NOT executed. Each tool must be its own separate ```tool_call``` block:\n"
                            "```tool_call\n"
                            "{\"tool\":\"thinking.note\",\"args\":{\"note\":\"your plain-text note\"}}\n"
                            "```\n"
                            "```tool_call\n"
                            f"{{\"tool\":\"{real[0][0]}\",\"args\":{{...}}}}\n"
                            "```\n"
                            "Retry now with separate blocks."
                        )
        raw_items: list[str] = []
        stripped = (text or "").strip()
        if stripped.startswith("{") or stripped.startswith("["):
            raw_items.append(stripped)
        raw_items.extend(match.group(1).strip() for match in self.TOOL_CALL_JSON_RE.finditer(text or ""))
        for raw in raw_items:
            try:
                payload = json.loads(raw)
            except Exception as exc:
                preview = raw.strip().replace("\n", " ")[:500]
                return self.strings("tool_call_bad_json", error=str(exc), preview=preview)
            payloads = payload if isinstance(payload, list) else [payload]
            for item in payloads:
                if not isinstance(item, dict):
                    return self.strings("tool_call_not_object")
                tool_name = str(item.get("tool") or item.get("name") or "").lower().strip()
                if not tool_name:
                    continue
                if tool_name not in self._tool_names():
                    candidates = sorted(self._tool_names())
                    nearest = ", ".join(difflib.get_close_matches(tool_name, candidates, n=5, cutoff=0.45))
                    available = ", ".join(candidates[:30])
                    hint = self.strings("tool_call_nearest", nearest=nearest) if nearest else ""
                    return self.strings(
                        "tool_call_unknown",
                        tool_name=tool_name,
                        hint=hint,
                        available=available,
                    )
                args_raw = item.get("args") or {}
                if not isinstance(args_raw, dict):
                    return self.strings("tool_call_args_not_object", tool_name=tool_name)
        return ""

    def _extract_json_tool_call(self, text: str) -> tuple[str, str, str] | None:
        calls = self._extract_json_tool_calls(text)
        return calls[0] if calls else None

    def _extract_xml_tool_calls(self, text: str) -> list[tuple[str, str, str]]:
        """Return executable XML fallback calls, ignoring ordinary HTML/XML tags."""
        tool_names = self._tool_names()
        calls: list[tuple[str, str, str]] = []
        for match in self.TOOL_CALL_RE.finditer(text or ""):
            if match.group(1):
                tool_name, attrs_raw, body = match.group(1), match.group(2), match.group(3)
            else:
                tool_name, attrs_raw, body = match.group(4), match.group(5), ""
            tool_name = (tool_name or "").lower().strip()
            if tool_name in tool_names:
                calls.append((tool_name, attrs_raw or "", body or ""))
        return calls

    def _extract_xml_tool_call(self, text: str) -> tuple[str, str, str] | None:
        calls = self._extract_xml_tool_calls(text)
        return calls[0] if calls else None

    def _rescue_embedded_tool_calls(
        self, calls: list[tuple[str, str, str]]
    ) -> list[tuple[str, str, str]]:
        """When the model puts a real tool call inside thinking.note body, surface it.

        Models occasionally emit:
            ```tool_call
            {"tool":"thinking.note","args":{"note":"{\"tool\":\"terminal.run\",\"args\":{\"cmd\":\"ls\"}}"}}
            ```
        instead of two separate blocks. This method rescues those embedded calls
        so they are executed in the same step, while preserving the thinking.note
        itself (its handler will return a FORMAT ERROR that teaches the model).
        """
        result: list[tuple[str, str, str]] = []
        for name, attrs_raw, body in calls:
            result.append((name, attrs_raw, body))
            if name == "thinking.note":
                raw = (body or "").strip()
                # Also check the note= arg if body is empty
                if not raw:
                    try:
                        for item in self._iter_json_tool_payloads(attrs_raw):
                            raw = str(item.get("note") or item.get("text") or "").strip()
                            if raw:
                                break
                    except Exception:
                        pass
                embedded = self._extract_json_tool_calls(raw)
                for emb_name, emb_attrs, emb_body in embedded:
                    if emb_name != "thinking.note":
                        result.append((emb_name, emb_attrs, emb_body))
        return result

    def _extract_tool_calls(self, text: str) -> list[tuple[str, str, str]]:
        """Return executable tool calls; JSON/Codex protocols first, XML fallback second."""
        calls = self._extract_json_tool_calls(text)
        if calls:
            return self._rescue_embedded_tool_calls(calls)
        calls = self._extract_codex_tool_calls(text)
        if calls:
            return self._rescue_embedded_tool_calls(calls)
        calls = self._extract_xml_tool_calls(text)
        return self._rescue_embedded_tool_calls(calls) if calls else calls

    def _extract_tool_call(self, text: str) -> tuple[str, str, str] | None:
        """Return the first executable tool call; kept for compatibility."""
        calls = self._extract_tool_calls(text)
        return calls[0] if calls else None

    def _compact_agent_log(self, log: list[str]) -> list[str]:
        if not log:
            return []
        compacted: list[str] = []
        current = str(log[0])
        count = 1
        for raw in log[1:]:
            item = str(raw)
            if item == current:
                count += 1
                continue
            compacted.append(f"{current} * {count}" if count > 1 else current)
            current = item
            count = 1
        compacted.append(f"{current} * {count}" if count > 1 else current)
        return compacted

    def _agent_log_html(self, log: list[str]) -> str:
        if not log:
            return ""
        compacted = self._compact_agent_log(log)
        return (
            f"\n\n<blockquote expandable><b>{html.escape(self.strings('agent_log_label'))}</b>\n"
            f"{html.escape(chr(10).join(compacted))}</blockquote>"
        )

    def _uses_completion_tokens(self, provider: str) -> bool:
        model = self._model(provider).lower()
        return provider == "openai" and (
            model.startswith("gpt-5")
            or model.startswith("o1")
            or model.startswith("o3")
            or model.startswith("o4")
        )

    def _reasoning_effort(self) -> str:
        effort = str(self.config.get("reasoning_effort", "off") or "off").lower().strip()
        return effort if effort in {"low", "medium", "high", "xhigh"} else "off"

    def _set_token_usage(self, usage: dict[str, Any] | None, provider: str) -> None:
        usage = usage or {}
        if provider == "google":
            input_tokens = int(usage.get("promptTokenCount") or 0)
            output_tokens = int(usage.get("candidatesTokenCount") or 0)
            total_tokens = int(usage.get("totalTokenCount") or input_tokens + output_tokens)
        else:
            input_tokens = int(usage.get("prompt_tokens") or usage.get("input_tokens") or 0)
            output_tokens = int(
                usage.get("completion_tokens")
                or usage.get("output_tokens")
                or 0
            )
            total_tokens = int(usage.get("total_tokens") or input_tokens + output_tokens)
        self._last_token_usage = {
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
        }

    async def _ask_openai_compatible(
        self,
        provider: str,
        messages: list[dict[str, str]],
        api_key: str,
        *,
        max_tokens_override: int | None = None,
    ) -> str:
        base_url = self._base_url(provider)
        if not base_url:
            raise RuntimeError("custom_base_url is not configured")
        url = f"{base_url}/chat/completions"
        payload: dict[str, Any] = {
            "model": self._model(provider),
            "messages": messages,
            "temperature": float(self.config["temperature"]),
        }
        reasoning_effort = self._reasoning_effort()
        if reasoning_effort != "off":
            payload["reasoning_effort"] = reasoning_effort
        max_tokens = int(max_tokens_override or self.config["max_tokens"])
        if self._uses_completion_tokens(provider):
            payload["max_completion_tokens"] = max_tokens
        else:
            payload["max_tokens"] = max_tokens

        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        try:
            data = await self._post_json(url, payload, headers=headers)
        except RuntimeError as exc:
            error_text = str(exc).lower()
            if "max_completion_tokens" in error_text and "unsupported" in error_text:
                value = payload.pop("max_completion_tokens", None)
                if value is not None:
                    payload["max_tokens"] = value
                    data = await self._post_json(url, payload, headers=headers)
                else:
                    raise
            elif "max_tokens" in error_text and "unsupported" in error_text:
                value = payload.pop("max_tokens", None)
                if value is not None:
                    payload["max_completion_tokens"] = value
                    data = await self._post_json(url, payload, headers=headers)
                else:
                    raise
            elif "temperature" in error_text and "unsupported" in error_text:
                payload.pop("temperature", None)
                data = await self._post_json(url, payload, headers=headers)
            elif "reasoning_effort" in error_text or "reasoning effort" in error_text:
                payload.pop("reasoning_effort", None)
                data = await self._post_json(url, payload, headers=headers)
            else:
                raise
        try:
            self._set_token_usage(data.get("usage"), provider)
            return str(data["choices"][0]["message"]["content"]).strip()
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError(f"Unexpected {provider} response: {data}") from exc

    async def _ask_google(
        self,
        messages: list[dict[str, str]],
        api_key: str,
        *,
        max_tokens_override: int | None = None,
    ) -> str:
        model = self._model("google")
        url = f"{self._base_url('google')}/models/{model}:generateContent?key={api_key}"
        system_text = "\n\n".join(m["content"] for m in messages if m["role"] == "system")
        contents = []
        for msg in messages:
            if msg["role"] == "system":
                continue
            role = "model" if msg["role"] == "assistant" else "user"
            content = msg["content"]
            parts = self._build_google_parts(content)
            contents.append({"role": role, "parts": parts})
        payload: dict[str, Any] = {
            "contents": contents,
            "generationConfig": {
                "temperature": float(self.config["temperature"]),
                "maxOutputTokens": int(max_tokens_override or self.config["max_tokens"]),
            },
        }
        if system_text:
            payload["systemInstruction"] = {"parts": [{"text": system_text}]}
        data = await self._post_json(url, payload)
        try:
            self._set_token_usage(data.get("usageMetadata"), "google")
            parts = data["candidates"][0]["content"]["parts"]
            return "".join(str(part.get("text", "")) for part in parts).strip()
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError(f"Unexpected google response: {data}") from exc

    async def _post_json(
        self,
        url: str,
        payload: dict[str, Any],
        *,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        timeout_seconds = int(self.config["timeout"])
        timeout = aiohttp.ClientTimeout(total=timeout_seconds)
        try:
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.post(url, json=payload, headers=headers) as resp:
                    text = await resp.text()
                    if resp.status >= 400:
                        raise RuntimeError(f"HTTP {resp.status}: {text[:800]}")
                    try:
                        return await resp.json()
                    except Exception as exc:
                        raise RuntimeError(f"Invalid JSON response: {text[:800]}") from exc
        except TimeoutError as exc:
            raise RuntimeError(
                f"Provider request timed out after {timeout_seconds}s. "
                "Increase OpenAgent timeout or use a faster model for this task."
            ) from exc

__all__ = [
    'OpenAgentPlugin',
    '_OpenAgentPluginSkillMixin',
    '_OpenAgentTelegramMediaMixin',
    '_OpenAgentAgentLoopMixin',
    '_OpenAgentStatusMixin',
]
