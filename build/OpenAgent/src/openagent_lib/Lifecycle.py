# SPDX-License-Identifier: MIT
from __future__ import annotations

from pathlib import Path
import asyncio
from typing import Any

from .PluginsEngine import OpenAgentPlugin
from .SessionManager import SessionManager

class _OpenAgentLifecycleMixin:
    """Lifecycle/bootstrap logic."""

    async def on_load(self) -> None:
        await super().on_load()
        defaults = {
            "provider": "openai",
            "api_key": "",
            "model": "",
            "custom_base_url": "",
            "system_prompt": (
                "You are OpenAgent inside a Telegram userbot. Help the user directly. "
                "You may inspect the local workspace through terminal commands when needed."
            ),
            "temperature": 0.7,
            "max_tokens": 1200,
            "reasoning_effort": "off",
            "timeout": 180,
            "provider_reconnect_attempts": 5,
            "terminal_enabled": True,
            "terminal_steps": 3,
            "terminal_timeout": 30,
            "web_search_enabled": True,
            "web_search_steps": 3,
            "mcub_use": False,
            "mcub_steps": 3,
            "send_messages_enabled": True,
            "send_message_steps": 3,
            "create_chats_enabled": True,
            "create_chat_steps": 2,
            "create_bots_enabled": True,
            "create_bot_steps": 1,
            "account_tools_enabled": True,
            "account_tool_steps": 5,
            "chat_management_enabled": True,
            "chat_management_steps": 5,
            "media_max_bytes": 8_000_000,
            "context_enabled": True,
            "context_turns": 10,
            "context_compaction_enabled": True,
            "context_compaction_chars": 18000,
            "context_compaction_keep_turns": 2,
            "context_compaction_max_tokens": 900,
            "tool_memory_enabled": False,
            "tool_memory_items": 20,
            "tool_memory_max_chars": 500,
            "response_header": "<blockquote><a href=\"tg://emoji?id=6010179991944305029\">☺️</a> <strong>OpenAgent</strong>: <a href=\"tg://emoji?id=5325872701032635449\">⏳</a>  <em>{elapsed}</em>s\n• <u>{provider}/{model}</u>  •  <code>{reasoning_effort}</code>\n| | | | | | | | | | | | | | | | | | | | | | | | | | |\n<a href=\"tg://emoji?id=5408994848084624514\">💸</a> <strong>in</strong> <em>{input_tokens}</em>, <strong>out</strong> <em>{output_tokens}</em> | <b>total</b>\n<i>{total_tokens}</i> | <strong>tool use:</strong> <em>{tool_count}</em></blockquote>\n<blockquote expandable><i>{thinking}</i></blockquote>",
            "request_label": "<a href=\"tg://emoji?id=6010352868672936598\"><strong>🐈‍⬛</strong></a><strong></strong><strong> Prompt:</strong>",
            "response_label": "<a href=\"tg://emoji?id=6010286885090368072\"><strong>❌</strong></a><strong></strong><strong> Answer:</strong>",
            "thinking_template": "<blockquote><a href=\"tg://emoji?id=6010292571627069263\">😎</a> <u>{provider}/{model}</u> • <em>prepares the response...</em></blockquote >\n<blockquote><a href=\"tg://emoji?id=5404857686477015710\">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>",
            "tool_display_template": "<blockquote expandable><i>{thinking_line}</i></blockquote>\n<blockquote expandable><strong>┌|</strong> {tool_state_emoji_html} {status_emoji_html} <em>{status_text}</em> <code>{tool}</code>\n<strong>└|</strong> <a href=\"tg://emoji?id=6010570945637392851\">🥳</a>  <b>Round:</b> <code>{round}/{round_total}</code> • <b>Reasoning:</b>\n<code>{reasoning_effort}</code>\n</blockquote><blockquote><a href=\"tg://emoji?id=5310041868191407556\">🩸</a> <strong>{activity_line}</strong></blockquote>\n<blockquote expandable><a href=\"tg://emoji?id=6012361831035705571\">😪</a> <strong>Log tools</strong>\n<code>{log_lines}</code></blockquote>",
            "tool_status_emojis": "thinking=❔\nterminal=🖥\nweb=🌐\nfile=📦\nmcub=🧲\nmessage=💬\ndialog=🗂\nchat=🐈‍⬛\nmoderation=🛡\nprofile=👤\ncontacts=👥\ncreation=✨\nskills=🧠\ncode=🧬\ncontext=🧾\nutility=🛠\ndefault=🛠",
            "tool_display_max_chars": 1200,
            "tool_display_log_lines": 8,
            "thinking_display_limit": 3,
            "thinking_empty_text": "Модель ещё не думала.",
            "thinking_bullet": "•",
            "random_strings": ["Thinking...", "Думаю...", "Генерирую..."],
            "todo_status_emojis": "pending=...\nopen=>>>\nclosed=---",
            "placeholders": "",
            "repo_context_enabled": True,
            "repo_context_max_chars": 7000,
            "skills_enabled": True,
            "skills_trigger_mode": "auto",
            "skill_repo_url": "https://raw.githubusercontent.com/hairpin01/repo-MCUB-fork/main/OpenAgent/skills",
            "tool_confirmation_enabled": True,
            "tool_confirmation_mode": "medium",
            "tool_confirmation_template": "<blockquote><a href=\"tg://emoji?id=6010201728773790293\">😈</a> Continue?\n<a href=\"tg://emoji?id=6012317326584583729\">😐</a> Tool: {tool} • {elapsed}s</blockquote>\n<blockquote expandable><a href=\"tg://emoji?id=6010394680179562842\">😶</a> <b>What will be completed</b>\n<a href=\"tg://emoji?id=6010292550152230657\">☀️</a> <code>{value}</code></blockquote>",
            "tool_confirmation_yes_text": "Выполнить",
            "tool_confirmation_no_text": "Не сейчас",
            "tool_confirmation_timeout": 900,
        }
        config_dict = await self.kernel.get_module_config(self.name, defaults)
        if isinstance(config_dict.get("random_strings"), str):
            config_dict["random_strings"] = [
                line.strip()
                for line in config_dict["random_strings"].splitlines()
                if line.strip()
            ] or defaults["random_strings"]
        provider = self._normalize_provider(str(config_dict.get("provider", "openai")))
        config_dict["provider"] = provider if provider in self.PROVIDERS else "openai"
        self._last_request_at = 0.0
        self._skills_dir = self._resolve_skills_dir()
        sessions_path = Path(self._workspace_dir()) / "openagent_sessions" / "sessions.json"
        self.session_manager = SessionManager(
            sessions_path,
            logger=self.log,
            model_getter=self._model,
            default_name_getter=lambda: self.strings("new_session_name"),
            session_limit=self.SESSION_LIMIT,
        )
        self._sessions = self.session_manager.sessions
        self._active_session = self.session_manager.active_session
        self._session_prefs = self.session_manager.session_prefs
        self._tool_memory: dict[int, list[str]] = {}
        self._cancelled_generations: set[str] = set()
        self._regen_payloads: dict[str, dict[str, Any]] = {}
        self._input_events: dict[str, dict[str, Any]] = {}
        self._session_input_events: dict[str, dict[str, Any]] = {}
        self._pending_prompts: dict[str, dict[str, Any]] = {}
        self._runtime_comments: dict[str, list[str]] = {}
        self._background_tool_tasks: dict[str, asyncio.Task[Any]] = {}
        self._inline_status_waiters: dict[str, asyncio.Future[Any]] = {}
        # Per-chat reference to the last inline response form so follow-up
        # Button.input edits it in place instead of posting a new message.
        self._oa_last_loading: dict[int, Any] = {}
        self._tool_confirmation_waiters: dict[str, asyncio.Future[bool]] = {}
        self._last_token_usage = {
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
        }
        self._todo_items_cache: list[dict[str, str]] = []
        self._todo_status_map_raw: str | None = None
        self._todo_status_map_cache: dict[str, str] | None = None
        self._tool_status_emojis_raw: str | None = None
        self._tool_status_emojis_cache: dict[str, str] | None = None
        self._plugins: dict[str, OpenAgentPlugin] = {}
        self._plugin_files: dict[str, Path] = {}
        self._plugins_cache: list[dict] = []
        self._tool_map_cache: dict[str, str] | None = None
        self._tool_registry_cache: tuple[str, ...] | None = None
        self._disabled_plugins: set[str] = self._load_disabled_plugins()
        await self._load_sessions()
        await self._load_todo_items_storage()
        await self._load_installed_plugins()
        self.log.info("OpenAgent loaded")

__all__ = [
    '_OpenAgentLifecycleMixin'
]
