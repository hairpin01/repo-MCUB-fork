# SPDX-License-Identifier: MIT
# -- repo data --
# scop: kernel min v1.4.5
# scope: heroku_min 9.9.9
# хе
# repo: https://github.com/hairpin01/repo-MCUB-fork/
# -- end --
# requires: aiohttp
# scop: inline

from __future__ import annotations

import asyncio
import base64
import contextlib
import difflib
import html
import inspect
import io
import mimetypes
import random
import re
import tempfile
import time
import uuid
import json
import sys
from dataclasses import dataclass, field
import importlib
import importlib.util
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, TYPE_CHECKING
from urllib.parse import quote, urlparse

import aiohttp
from telethon import events
from telethon.tl.functions.account import (
    UpdateProfileRequest,
    UpdateUsernameRequest as UpdateAccountUsernameRequest,
)
from telethon.tl.functions.channels import (
    CreateChannelRequest,
    EditAdminRequest,
    EditPhotoRequest,
    EditTitleRequest,
    JoinChannelRequest,
    ToggleSlowModeRequest,
    UpdateUsernameRequest,
)
from telethon.tl.functions.contacts import (
    AddContactRequest,
    BlockRequest,
    DeleteContactsRequest,
    UnblockRequest,
)
from telethon.tl.functions.messages import (
    EditChatAboutRequest,
    ExportChatInviteRequest,
    ImportChatInviteRequest,
    SaveDraftRequest,
)
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins, ChatAdminRights

from core.lib.loader.module_base import ModuleBase, callback, command
from core.lib.loader.module_config import (
    Boolean,
    Choice,
    ConfigValue,
    Float,
    Group,
    Row,
    Answer,
    Integer,
    List,
    ModuleConfig,
    Secret,
    String,
)

if TYPE_CHECKING:
    from core.lib.types import InlineMessage, Event, Kernel

from openagent_lib.mixins import (
    _WHITESPACE_RE,
    _PLACEHOLDER_RE,
    _TODO_STATUS_ALIASES,
    _DEFAULT_TODO_STATUS_MAP,
    _SESSION_PREFERENCES,
    _TOOL_GROUP_ALIASES,
    _DEFAULT_TOOL_STATUS_EMOJIS,
    OASession,
    SessionManager,
    OpenAgentPlugin,
    _OpenAgentLifecycleMixin,
    OpenAgentProviderService,
    OpenAgentTemplateService,
    _OpenAgentProviderMixin,
    OpenAgentTodoService,
    _OpenAgentTodoMixin,
    OpenAgentToolDisplayService,
    _OpenAgentToolDisplayMixin,
    OpenAgentContextService,
    _OpenAgentContextMixin,
    _OpenAgentSessionsMixin,
    _OpenAgentPluginSkillMixin,
    _OpenAgentRuntimeToolsMixin,
    _OpenAgentTelegramMediaMixin,
    _OpenAgentStatusMixin,
    _OpenAgentAgentLoopMixin,
    _OpenAgentResponseMixin,
    _OpenAgentToolRegistryMixin,
)


class OpenAgent(
    _OpenAgentLifecycleMixin,
    _OpenAgentProviderMixin,
    _OpenAgentTodoMixin,
    _OpenAgentToolDisplayMixin,
    _OpenAgentContextMixin,
    _OpenAgentSessionsMixin,
    _OpenAgentPluginSkillMixin,
    _OpenAgentRuntimeToolsMixin,
    _OpenAgentTelegramMediaMixin,
    _OpenAgentStatusMixin,
    _OpenAgentAgentLoopMixin,
    _OpenAgentResponseMixin,
    _OpenAgentToolRegistryMixin,
    ModuleBase,
):
    name = "OpenAgent"
    version = "0.8.0-main.build:1043"
    author = "@dev_dolbaeb && @Hairpin00"
    description = {
        "ru": "ИИ агент в юзерботе с новой архитектурой инструментов",
        "en": "AI agent in userbot with refreshed tool architecture",
        "rofl": "ИИ агент, который делает вид, что всё контролирует",
        "linux": "AI agent daemon with tool-oriented runtime",
    }
    strings = {
        "ru": {
            "need_text": "Usage: .oa <request>",
            "thinking": "Thinking...",
            "running_terminal": "Running terminal command...",
            "running_search": "Searching the web...",
            "no_key": "API key is not configured. Use .cfg OpenAgent api_key",
            "bad_provider": "Unknown provider. Available: {providers}",
            "provider_saved": "Provider saved: {provider}",
            "key_saved": "Provider and API key saved: {provider}",
            "disabled": "Provider {provider} is not available yet",
            "error": "OpenAgent error: {error}",
            "thinking_empty_text": "Модель ещё не думала.",
            "thinking_template_default": '<blockquote><a href="tg://emoji?id=6010292571627069263">😎</a> <u>{provider}/{model}</u> • <em>prepares the response...</em></blockquote >\n<blockquote><a href="tg://emoji?id=5404857686477015710">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>',
            "request_label_default": '<a href="tg://emoji?id=6010352868672936598"><strong>🐈‍⬛</strong></a><strong></strong><strong> Prompt:</strong>',
            "response_label_default": '<a href="tg://emoji?id=6010286885090368072"><strong>❌</strong></a><strong></strong><strong> Answer:</strong>',
            "agent_log_label": "Agent Log",
            "status_thinking": "Думаю",
            "status_terminal": "Выполняю команду",
            "status_web": "Работаю с web",
            "status_file": "Работаю с файлом",
            "status_mcub": "Выполняю MCUB-команду",
            "status_message": "Работаю с сообщениями",
            "status_chat": "Проверяю чат",
            "status_dialog": "Проверяю диалоги",
            "status_code": "Готовлю код",
            "status_todo": "Обновляю TODO",
            "status_default": "Выполняю {tool}",
            "tool_confirmation_approved": "Выполняю",
            "tool_confirmation_yes_text": "Выполнить",
            "tool_confirmation_no_text": "Не сейчас",
            "tool_validation_retry_prompt": "Это результат валидации твоего tool_call. Исправь tool_call и повтори прямо сейчас. Fix the tool call and try again now. Use only valid OpenAgent tool names, valid JSON, and args as a JSON object. If no tool is needed, answer the user in plain text with no JSON/tool_call.",
            "runtime_comment_button": "💬 Комментировать",
            "runtime_comment_placeholder": "Комментарий агенту...",
            "runtime_comment_saved": "Комментарий добавлен",
            "runtime_comment_note": "Пользователь добавил комментарий во время выполнения. Учти это в следующих шагах:\n{comments}",
            "follow_up_button": "✍️ Продолжить",
            "follow_up_placeholder": "Введи запрос...",
            "regen_prompt_button": "🔁 Реген с промптом",
            "regen_prompt_placeholder": "Новый промпт для регенерации...",
            "regen_stale": "Запрос устарел",
            "regenerating": "Регенерирую...",
            "new_session_name": "Новый чат",
            "chat_history_button": "💬 История чатов",
            "chats_title": "💬 <b>Чаты — этот чат</b>",
            "chat_empty": "Пока нет сообщений",
            "chat_today": "сегодня",
            "chat_yesterday": "вчера",
            "chat_days_ago": "{days} дн назад",
            "new_chat_button": "+ Новый чат",
            "ask_this_chat_button": "✍️ Спросить в этом чате",
            "ask_this_chat_placeholder": "Запрос для этого чата...",
            "return_to_chat_button": "↩️ Вернуться в этот чат",
            "saved_response_missing": "В истории этого чата ещё нет ответа ИИ",
            "rename_chat_button": "✏️ Переименовать",
            "delete_chat_button": "🗑 Удалить",
            "remember_chat_button": "💾 Запомнить выбор",
            "chat_choice_saved": "Выбор запомнен",
            "chat_switched": "Чат активен: {name}",
            "chat_created": "Создан чат: {name}",
            "chat_renamed": "Чат переименован: {name}",
            "chat_deleted": "Чат удалён",
            "chat_delete_last": "Нельзя удалить последний чат",
            "new_chat_placeholder": "Название (или Enter для авто...)",
            "rename_chat_placeholder": "Новое название...",
            "auto_name_prompt": "Придумай короткое название сессии на 3-4 слова. Ответь только названием. Запрос: {prompt}",
            "oa_choose_chat": "Выбери чат для продолжения или создай новый.",
            "fallback_thinking_note": "Понял задачу, начинаю выполнение.",
            "tools_no_final": "Инструменты выполнены, но модель не сформировала финальный текст.",
            "tool_call_bad_json": "Ошибка tool call: модель вернула некорректный JSON ({error}).\nФрагмент: {preview}",
            "tool_call_not_object": "Ошибка tool call: элемент вызова инструмента должен быть JSON-объектом.",
            "tool_call_unknown": "Ошибка tool call: неизвестный инструмент '{tool_name}'.{hint} Доступные примеры: {available}.",
            "tool_call_nearest": " Ближайшие: {nearest}.",
            "tool_call_args_not_object": "Ошибка tool call: args для '{tool_name}' должен быть JSON-объектом.",
            "answer_file_request": "Запрос",
            "answer_file_answer": "Ответ",
            "answer_file_too_long": "<b>Ответ слишком длинный, отправляю файлом.</b>",
            "answer_file_attach_failed": "<b>Не удалось прикрепить файл к форме, показываю начало:</b>",
            "continued": "continued",
            "cancelled": "Отменено",
            "context_cleared": "Контекст очищен",
            "clear_button": "🧹 Очистить",
            "regenerate_button": "🔃 Регенерировать",
            "cancel_button": "Отмена",
            "reply_analyze_prompt": "Проанализируй вложение/сообщение из reply.",
            "skills_empty": "No OpenAgent skills installed",
            "skillinstall_usage": "Usage: .skillinstall <skill_name>",
            "sendss_usage": "Usage: .sendss <skill_name>",
            "skill_not_found": "Skill not found",
            "skill_name_required": "skill name is required",
            "skill_not_found_repo": "Skill not found in repo: {query}",
            "skill_saved": "Skill saved: {name}",
            "unknown_skills_tool": "Unknown skills tool: {tool}",
            "imss_need_reply": "Reply to a .md file or markdown message",
            "skill_empty": "Skill content is empty",
            "delss_usage": "Usage: .delss <skill_name>",
            "skill_installed": "Skill installed: <code>{name}</code>",
            "skill_imported": "Skill imported: <code>{name}</code>",
            "skill_deleted": "Skill deleted: <code>{name}</code>",
            "plugin_install_failed": "Plugin install failed: <code>{error}</code>",
            "plugin_installed": "Plugin installed: <code>{name}</code>",
            "plugins_enabled_title": "<b>🧩 Включёные плагины:</b>\n",
            "plugins_none_installed": "\nНет установленных плагинов\n",
            "plugins_total": "\n<b>Всего плагинов:</b> {count}",
            "plugin_catalog_btn": "📦 Каталог",
            "plugin_manager_btn": "⚙️ Менеджер",
            "close_btn": "❌ Закрыть",
            "plugin_repo_empty": "❌ Нет плагинов в репозитории",
            "plugin_no_description": "Нет описания",
            "plugin_more_tools": " ...и ещё {count}",
            "plugin_tools_label": "Tools",
            "plugin_installed_btn": "✅ Установлен",
            "plugin_install_btn": "📥 Установить",
            "plugin_code_btn": "📄 Код",
            "back_btn": "🔙 Назад",
            "plugin_installing": "⏳ Устанавливаю...",
            "plugin_installed_alert": "✅ {name} установлен!",
            "generic_error": "❌ Ошибка: {error}",
            "plugin_manager_no_installed": "Нет установленных плагинов",
            "plugin_version_label": "Версия",
            "plugin_actions_title": "<b>Действия:</b>",
            "plugin_delete_btn": "🗑 Удалить",
            "plugin_deleted_alert": "🗑 {name} удалён",
            "oa_chat_choice_title": "💬 <b>Куда отправить запрос?</b>",
            "remember_pref_continue": "💾 Всегда сюда",
            "remember_pref_new": "💾 Всегда новый",
            "pref_saved": "Запомнено",
        },
        "en": {
            "need_text": "Usage: .oa <request>",
            "thinking": "Thinking...",
            "running_terminal": "Running terminal command...",
            "running_search": "Searching the web...",
            "no_key": "API key is not configured. Use .cfg OpenAgent api_key",
            "bad_provider": "Unknown provider. Available: {providers}",
            "provider_saved": "Provider saved: {provider}",
            "key_saved": "Provider and API key saved: {provider}",
            "disabled": "Provider {provider} is not available yet",
            "error": "OpenAgent error: {error}",
            "thinking_empty_text": "The model has not thought yet.",
            "thinking_template_default": '<blockquote><a href="tg://emoji?id=6010292571627069263">😎</a> <u>{provider}/{model}</u> • <em>prepares the response...</em></blockquote >\n<blockquote><a href="tg://emoji?id=5404857686477015710">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>',
            "request_label_default": '<a href="tg://emoji?id=6010352868672936598"><strong>🐈‍⬛</strong></a><strong></strong><strong> Prompt:</strong>',
            "response_label_default": '<a href="tg://emoji?id=6010286885090368072"><strong>❌</strong></a><strong></strong><strong> Answer:</strong>',
            "agent_log_label": "Agent Log",
            "status_thinking": "Thinking",
            "status_terminal": "Running command",
            "status_web": "Working with web",
            "status_file": "Working with file",
            "status_mcub": "Running MCUB command",
            "status_message": "Working with messages",
            "status_chat": "Checking chat",
            "status_dialog": "Checking dialogs",
            "status_code": "Preparing code",
            "status_todo": "Updating TODO",
            "status_default": "Running {tool}",
            "tool_confirmation_approved": "Running",
            "tool_confirmation_yes_text": "Run",
            "tool_confirmation_no_text": "Not now",
            "tool_validation_retry_prompt": "This is the validation result for your tool_call. Fix the tool call and try again now. Use only valid OpenAgent tool names, valid JSON, and args as a JSON object. If no tool is needed, answer the user in plain text with no JSON/tool_call.",
            "runtime_comment_button": "💬 Comment",
            "runtime_comment_placeholder": "Comment for agent...",
            "runtime_comment_saved": "Comment added",
            "runtime_comment_note": "The user added a live comment while you were working. Use it in the next steps:\n{comments}",
            "follow_up_button": "✍️ Continue",
            "follow_up_placeholder": "Enter request...",
            "regen_prompt_button": "🔁 Regen with prompt",
            "regen_prompt_placeholder": "New prompt for regeneration...",
            "regen_stale": "Request expired",
            "regenerating": "Regenerating...",
            "new_session_name": "New chat",
            "chat_history_button": "💬 Chat history",
            "chats_title": "💬 <b>Chats — this chat</b>",
            "chat_empty": "No messages yet",
            "chat_today": "today",
            "chat_yesterday": "yesterday",
            "chat_days_ago": "{days} days ago",
            "new_chat_button": "+ New chat",
            "ask_this_chat_button": "✍️ Ask in this chat",
            "ask_this_chat_placeholder": "Request for this chat...",
            "return_to_chat_button": "↩️ Return to this chat",
            "saved_response_missing": "This chat history has no AI answer yet",
            "rename_chat_button": "✏️ Rename",
            "delete_chat_button": "🗑 Delete",
            "remember_chat_button": "💾 Remember choice",
            "chat_choice_saved": "Choice remembered",
            "chat_switched": "Active chat: {name}",
            "chat_created": "Created chat: {name}",
            "chat_renamed": "Chat renamed: {name}",
            "chat_deleted": "Chat deleted",
            "chat_delete_last": "Cannot delete the last chat",
            "new_chat_placeholder": "Name (or Enter for auto...)",
            "rename_chat_placeholder": "New name...",
            "auto_name_prompt": "Create a short 3-4 word session title. Reply with the title only. Request: {prompt}",
            "oa_choose_chat": "Choose a chat to continue or create a new one.",
            "fallback_thinking_note": "Understood the task, starting execution.",
            "tools_no_final": "Tools ran, but the model did not provide final text.",
            "tool_call_bad_json": "Tool call error: model returned invalid JSON ({error}).\nFragment: {preview}",
            "tool_call_not_object": "Tool call error: tool call item must be a JSON object.",
            "tool_call_unknown": "Tool call error: unknown tool '{tool_name}'.{hint} Available examples: {available}.",
            "tool_call_nearest": " Nearest: {nearest}.",
            "tool_call_args_not_object": "Tool call error: args for '{tool_name}' must be a JSON object.",
            "answer_file_request": "Request",
            "answer_file_answer": "Answer",
            "answer_file_too_long": "<b>Answer is too long, sending it as a file.</b>",
            "answer_file_attach_failed": "<b>Failed to attach the file to the form, showing the beginning:</b>",
            "continued": "continued",
            "cancelled": "Cancelled",
            "context_cleared": "Context cleared",
            "clear_button": "🧹 Clear",
            "regenerate_button": "🔃 Regenerate",
            "cancel_button": "Cancel",
            "reply_analyze_prompt": "Analyze the replied attachment/message.",
            "skills_empty": "No OpenAgent skills installed",
            "skillinstall_usage": "Usage: .skillinstall <skill_name>",
            "sendss_usage": "Usage: .sendss <skill_name>",
            "skill_not_found": "Skill not found",
            "skill_name_required": "skill name is required",
            "skill_not_found_repo": "Skill not found in repo: {query}",
            "skill_saved": "Skill saved: {name}",
            "unknown_skills_tool": "Unknown skills tool: {tool}",
            "imss_need_reply": "Reply to a .md file or markdown message",
            "skill_empty": "Skill content is empty",
            "delss_usage": "Usage: .delss <skill_name>",
            "skill_installed": "Skill installed: <code>{name}</code>",
            "skill_imported": "Skill imported: <code>{name}</code>",
            "skill_deleted": "Skill deleted: <code>{name}</code>",
            "plugin_install_failed": "Plugin install failed: <code>{error}</code>",
            "plugin_installed": "Plugin installed: <code>{name}</code>",
            "plugins_enabled_title": "<b>🧩 Enabled plugins:</b>\n",
            "plugins_none_installed": "\nNo installed plugins\n",
            "plugins_total": "\n<b>Total plugins:</b> {count}",
            "plugin_catalog_btn": "📦 Catalog",
            "plugin_manager_btn": "⚙️ Manager",
            "close_btn": "❌ Close",
            "plugin_repo_empty": "❌ No plugins in repository",
            "plugin_no_description": "No description",
            "plugin_more_tools": " ...and {count} more",
            "plugin_tools_label": "Tools",
            "plugin_installed_btn": "✅ Installed",
            "plugin_install_btn": "📥 Install",
            "plugin_code_btn": "📄 Code",
            "back_btn": "🔙 Back",
            "plugin_installing": "⏳ Installing...",
            "plugin_installed_alert": "✅ {name} installed!",
            "generic_error": "❌ Error: {error}",
            "plugin_manager_no_installed": "No installed plugins",
            "plugin_version_label": "Version",
            "plugin_actions_title": "<b>Actions:</b>",
            "plugin_delete_btn": "🗑 Delete",
            "plugin_deleted_alert": "🗑 {name} deleted",
            "oa_chat_choice_title": "💬 <b>Where to send the request?</b>",
            "remember_pref_continue": "💾 Always here",
            "remember_pref_new": "💾 Always new",
            "pref_saved": "Remembered",
        },
        "rofl": {
            "need_text": "кинь промпт: .oa <запрос>",
            "thinking": "мозг греется...",
            "running_terminal": "консоль делает бррр...",
            "running_search": "гуглю мемы...",
            "no_key": "ключика нет, брат. .cfg OpenAgent api_key",
            "bad_provider": "такого провайдера не завезли. Есть: {providers}",
            "provider_saved": "провайдер запомнен: {provider}",
            "key_saved": "провайдер и ключ сохранены: {provider}",
            "disabled": "провайдер {provider} пока в отпуске",
            "error": "OpenAgent словил прикол: {error}",
            "thinking_empty_text": "нейронка пока делает вид, что думает.",
            "thinking_template_default": '<blockquote><a href="tg://emoji?id=6010292571627069263">😎</a> <u>{provider}/{model}</u> • <em>варит ответ...</em></blockquote >\n<blockquote><a href="tg://emoji?id=5404857686477015710">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>',
            "request_label_default": '<a href="tg://emoji?id=6010352868672936598"><strong>🐈‍⬛</strong></a><strong></strong><strong> Промптик:</strong>',
            "response_label_default": '<a href="tg://emoji?id=6010286885090368072"><strong>❌</strong></a><strong></strong><strong> Ответик:</strong>',
            "agent_log_label": "Лог движухи",
            "status_thinking": "Думаю, мамой клянусь",
            "status_terminal": "Терминалю",
            "status_web": "Шарюсь в интернетах",
            "status_file": "Щупаю файл",
            "status_mcub": "Дёргаю MCUB",
            "status_message": "Кручу сообщения",
            "status_chat": "Смотрю чатик",
            "status_dialog": "Листаю диалоги",
            "status_code": "Пишу код без паники",
            "status_todo": "Туда-сюда TODO",
            "status_default": "Делаю {tool}",
            "tool_confirmation_approved": "Ща сделаю",
            "tool_confirmation_yes_text": "Вжухнуть",
            "tool_confirmation_no_text": "Не щас",
            "tool_validation_retry_prompt": "Это результат проверки tool_call. Почини tool_call и повтори прямо сейчас. Используй только валидные OpenAgent tool names, валидный JSON и args как JSON object. Если инструмент не нужен — отвечай текстом без JSON/tool_call.",
            "runtime_comment_button": "💬 Подкинуть мысль",
            "runtime_comment_placeholder": "Вкинь коммент агенту...",
            "runtime_comment_saved": "Коммент долетел",
            "runtime_comment_note": "Юзер подкинул коммент пока ты работал. Учти дальше:\n{comments}",
            "follow_up_button": "✍️ Ещё вопросик",
            "follow_up_placeholder": "Вкидывай запрос...",
            "regen_prompt_button": "🔁 Переварить с промптом",
            "regen_prompt_placeholder": "Новый промпт для переварки...",
            "regen_stale": "Запрос протух",
            "regenerating": "Переварю ещё раз...",
            "new_session_name": "Новый чатик",
            "chat_history_button": "💬 Чатики",
            "chats_title": "💬 <b>Чаты — тут</b>",
            "chat_empty": "пока пусто, как в голове",
            "chat_today": "сегодня",
            "chat_yesterday": "вчерась",
            "chat_days_ago": "{days} дн назад",
            "new_chat_button": "+ Новый чатик",
            "ask_this_chat_button": "✍️ Спросить тут",
            "ask_this_chat_placeholder": "Вкидывай запрос в этот чатик...",
            "return_to_chat_button": "↩️ Вернуться в чатик",
            "saved_response_missing": "В истории чатка ещё нет ответа ИИ",
            "rename_chat_button": "✏️ Переобозвать",
            "delete_chat_button": "🗑 Снести",
            "remember_chat_button": "💾 Запомнить прикол",
            "chat_choice_saved": "Запомнил, начальник",
            "chat_switched": "Теперь активен: {name}",
            "chat_created": "Чатик создан: {name}",
            "chat_renamed": "Чатик переобозван: {name}",
            "chat_deleted": "Чатик снесён",
            "chat_delete_last": "Последний чатик не дам снести",
            "new_chat_placeholder": "Название (или Enter для авто...)",
            "rename_chat_placeholder": "Новое имя чатика...",
            "auto_name_prompt": "Придумай мемное короткое название сессии на 3-4 слова. Ответь только названием. Запрос: {prompt}",
            "oa_choose_chat": "Выбери чатик или создай новый.",
            "fallback_thinking_note": "Задачу понял, погнали.",
            "tools_no_final": "Инструменты отработали, а модель финал зажала.",
            "tool_call_bad_json": "tool call кринжанул JSON ({error}).\nФрагмент: {preview}",
            "tool_call_not_object": "tool call должен быть JSON-объектом, не приколом.",
            "tool_call_unknown": "не знаю инструмент '{tool_name}'.{hint} Примеры: {available}.",
            "tool_call_nearest": " Похоже на: {nearest}.",
            "tool_call_args_not_object": "args для '{tool_name}' должны быть JSON-объектом.",
            "answer_file_request": "Запросик",
            "answer_file_answer": "Ответик",
            "answer_file_too_long": "<b>Ответ жирный, кидаю файлом.</b>",
            "answer_file_attach_failed": "<b>Файл не прилепился, показываю начало:</b>",
            "continued": "продолжение банкета",
            "cancelled": "Отменено, расходимся",
            "context_cleared": "Контекст помыт",
            "clear_button": "🧹 Стереть",
            "regenerate_button": "🔃 Переварить",
            "cancel_button": "Стопэ",
            "reply_analyze_prompt": "Глянь вложение/сообщение из reply.",
            "skills_empty": "Скиллов OpenAgent нет, пустота",
            "skillinstall_usage": "Юзай: .skillinstall <skill_name>",
            "sendss_usage": "Юзай: .sendss <skill_name>",
            "skill_not_found": "Скилл потерялся",
            "skill_name_required": "нужно имя скилла",
            "skill_not_found_repo": "Скилл в репе потерялся: {query}",
            "skill_saved": "Скилл сохранён: {name}",
            "unknown_skills_tool": "Неизвестный скилл-инструмент: {tool}",
            "imss_need_reply": "Ответь на .md файл или markdown сообщение",
            "skill_empty": "Скилл пустой как холодильник",
            "delss_usage": "Юзай: .delss <skill_name>",
            "skill_installed": "Скилл установлен: <code>{name}</code>",
            "skill_imported": "Скилл импортнут: <code>{name}</code>",
            "skill_deleted": "Скилл удалён: <code>{name}</code>",
            "plugin_install_failed": "Плагин не взлетел: <code>{error}</code>",
            "plugin_installed": "Плагин залетел: <code>{name}</code>",
            "plugins_enabled_title": "<b>🧩 Включёные плагины:</b>\n",
            "plugins_none_installed": "\nПлагинов ноль, грустно\n",
            "plugins_total": "\n<b>Всего плагинов:</b> {count}",
            "plugin_catalog_btn": "📦 Склад",
            "plugin_manager_btn": "⚙️ Рулёжка",
            "close_btn": "❌ Закрыть лавочку",
            "plugin_repo_empty": "❌ В репе плагинов кот наплакал",
            "plugin_no_description": "Описание украли",
            "plugin_more_tools": " ...и ещё {count} сверху",
            "plugin_tools_label": "Инструменты",
            "plugin_installed_btn": "✅ Уже стоит",
            "plugin_install_btn": "📥 Вкатить",
            "plugin_code_btn": "📄 Кодец",
            "back_btn": "🔙 Назад",
            "plugin_installing": "⏳ Вкатываю...",
            "plugin_installed_alert": "✅ {name} вкатился!",
            "generic_error": "❌ Ошибочка: {error}",
            "plugin_manager_no_installed": "Плагинов нет",
            "plugin_version_label": "Версия",
            "plugin_actions_title": "<b>Движения:</b>",
            "plugin_delete_btn": "🗑 Снести",
            "plugin_deleted_alert": "🗑 {name} снесён",
            "oa_chat_choice_title": "💬 <b>Куда кидаем запрос?</b>",
            "remember_pref_continue": "💾 Всегда тут",
            "remember_pref_new": "💾 Всегда новый",
            "pref_saved": "Запомнил, бро",
        },
        "linux": {
            "need_text": "usage: .oa <request>",
            "thinking": "forking thoughts...",
            "running_terminal": "execve(command)...",
            "running_search": "resolving web query...",
            "no_key": "api_key: ENOENT. Set .cfg OpenAgent api_key",
            "bad_provider": "provider: EINVAL. Available: {providers}",
            "provider_saved": "provider={provider} written",
            "key_saved": "provider={provider} and api_key written",
            "disabled": "provider {provider}: ENOSYS",
            "error": "openagent: {error}",
            "thinking_empty_text": "no reasoning frames in buffer.",
            "thinking_template_default": '<blockquote><a href="tg://emoji?id=6010292571627069263">😎</a> <u>{provider}/{model}</u> • <em>spawning response...</em></blockquote >\n<blockquote><a href="tg://emoji?id=5404857686477015710">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>',
            "request_label_default": '<a href="tg://emoji?id=6010352868672936598"><strong>🐈‍⬛</strong></a><strong></strong><strong> stdin:</strong>',
            "response_label_default": '<a href="tg://emoji?id=6010286885090368072"><strong>❌</strong></a><strong></strong><strong> stdout:</strong>',
            "agent_log_label": "syslog",
            "status_thinking": "reasoning",
            "status_terminal": "exec command",
            "status_web": "net I/O",
            "status_file": "file I/O",
            "status_mcub": "mcub syscall",
            "status_message": "message I/O",
            "status_chat": "stat chat",
            "status_dialog": "scan dialogs",
            "status_code": "compile code",
            "status_todo": "sync TODO",
            "status_default": "run {tool}",
            "tool_confirmation_approved": "executing",
            "tool_confirmation_yes_text": "exec",
            "tool_confirmation_no_text": "skip",
            "tool_validation_retry_prompt": "tool_call validation output. Fix the tool call and retry now. Use only valid OpenAgent tool names, valid JSON, and args as a JSON object. If no tool is needed, answer the user in plain text with no JSON/tool_call.",
            "runtime_comment_button": "💬 stdin+",
            "runtime_comment_placeholder": "append runtime comment...",
            "runtime_comment_saved": "comment queued",
            "runtime_comment_note": "Runtime user comment received. Apply it in next steps:\n{comments}",
            "follow_up_button": "✍️ stdin",
            "follow_up_placeholder": "type request...",
            "regen_prompt_button": "🔁 rerun stdin",
            "regen_prompt_placeholder": "new rerun prompt...",
            "regen_stale": "request expired",
            "regenerating": "rerunning...",
            "new_session_name": "new-chat",
            "chat_history_button": "💬 sessions",
            "chats_title": "💬 <b>sessions — current tty</b>",
            "chat_empty": "empty buffer",
            "chat_today": "today",
            "chat_yesterday": "yesterday",
            "chat_days_ago": "{days}d ago",
            "new_chat_button": "+ fork session",
            "ask_this_chat_button": "✍️ stdin to this session",
            "ask_this_chat_placeholder": "stdin for this session...",
            "return_to_chat_button": "↩️ return to this session",
            "saved_response_missing": "session history has no assistant stdout yet",
            "rename_chat_button": "✏️ mv session",
            "delete_chat_button": "🗑 rm session",
            "remember_chat_button": "💾 persist choice",
            "chat_choice_saved": "choice persisted",
            "chat_switched": "active session: {name}",
            "chat_created": "session created: {name}",
            "chat_renamed": "session renamed: {name}",
            "chat_deleted": "session removed",
            "chat_delete_last": "cannot remove last session",
            "new_chat_placeholder": "name (or Enter for auto...)",
            "rename_chat_placeholder": "new name...",
            "auto_name_prompt": "Create a short 3-4 word session title. Reply with the title only. Request: {prompt}",
            "oa_choose_chat": "select a session to continue or fork a new one.",
            "fallback_thinking_note": "task accepted; starting worker.",
            "tools_no_final": "tools exited 0, final output is empty.",
            "tool_call_bad_json": "tool_call: JSON parse failed ({error}).\nFragment: {preview}",
            "tool_call_not_object": "tool_call: item must be a JSON object.",
            "tool_call_unknown": "tool_call: unknown executable '{tool_name}'.{hint} Examples: {available}.",
            "tool_call_nearest": " Did you mean: {nearest}.",
            "tool_call_args_not_object": "tool_call: args for '{tool_name}' must be a JSON object.",
            "answer_file_request": "stdin",
            "answer_file_answer": "stdout",
            "answer_file_too_long": "<b>stdout too large, redirecting to file.</b>",
            "answer_file_attach_failed": "<b>attach failed, dumping head:</b>",
            "continued": "continued",
            "cancelled": "SIGTERM sent",
            "context_cleared": "context buffer cleared",
            "clear_button": "🧹 clear",
            "regenerate_button": "🔃 rerun",
            "cancel_button": "SIGTERM",
            "reply_analyze_prompt": "Analyze replied attachment/message.",
            "skills_empty": "No OpenAgent skills installed",
            "skillinstall_usage": "usage: .skillinstall <skill_name>",
            "sendss_usage": "usage: .sendss <skill_name>",
            "skill_not_found": "skill: ENOENT",
            "skill_name_required": "skill name is required",
            "skill_not_found_repo": "skill repo lookup failed: {query}",
            "skill_saved": "skill saved: {name}",
            "unknown_skills_tool": "unknown skills tool: {tool}",
            "imss_need_reply": "reply to a .md file or markdown message",
            "skill_empty": "skill content is empty",
            "delss_usage": "usage: .delss <skill_name>",
            "skill_installed": "skill installed: <code>{name}</code>",
            "skill_imported": "skill imported: <code>{name}</code>",
            "skill_deleted": "skill deleted: <code>{name}</code>",
            "plugin_install_failed": "plugin install failed: <code>{error}</code>",
            "plugin_installed": "plugin installed: <code>{name}</code>",
            "plugins_enabled_title": "<b>🧩 loaded plugins:</b>\n",
            "plugins_none_installed": "\nno loaded plugins\n",
            "plugins_total": "\n<b>plugin count:</b> {count}",
            "plugin_catalog_btn": "📦 catalog",
            "plugin_manager_btn": "⚙️ systemctl",
            "close_btn": "❌ close",
            "plugin_repo_empty": "❌ repository index is empty",
            "plugin_no_description": "no description",
            "plugin_more_tools": " ...and {count} more",
            "plugin_tools_label": "Tools",
            "plugin_installed_btn": "✅ loaded",
            "plugin_install_btn": "📥 install",
            "plugin_code_btn": "📄 source",
            "back_btn": "🔙 back",
            "plugin_installing": "⏳ installing package...",
            "plugin_installed_alert": "✅ {name} installed!",
            "generic_error": "❌ error: {error}",
            "plugin_manager_no_installed": "no loaded plugins",
            "plugin_version_label": "Version",
            "plugin_actions_title": "<b>Actions:</b>",
            "plugin_delete_btn": "🗑 remove",
            "plugin_deleted_alert": "🗑 {name} removed",
            "oa_chat_choice_title": "💬 <b>select target session</b>",
            "remember_pref_continue": "💾 --always-continue",
            "remember_pref_new": "💾 --always-new",
            "pref_saved": "pref written",
        },
    }
    PROVIDERS = (
        "openai",
        "google",
        "openrouter",
        "groq",
        "deepseek",
        "xai",
        "other",
    )
    PROVIDER_LABELS = {
        "openai": "OpenAI",
        "google": "Google",
        "openrouter": "OpenRouter",
        "groq": "Groq",
        "deepseek": "DeepSeek",
        "xai": "xAI",
        "other": "Other",
    }
    DEFAULT_MODELS = {
        "openai": "gpt-5.5",
        "google": "gemini-1.5-flash",
        "openrouter": "openai/gpt-4o-mini",
        "groq": "llama-3.3-70b-versatile",
        "deepseek": "deepseek-chat",
        "xai": "grok-2-latest",
        "other": "gpt-4o-mini",
    }
    BASE_URLS = {
        "openai": "https://api.openai.com/v1",
        "google": "https://generativelanguage.googleapis.com/v1beta",
        "openrouter": "https://openrouter.ai/api/v1",
        "groq": "https://api.groq.com/openai/v1",
        "deepseek": "https://api.deepseek.com/v1",
        "xai": "https://api.x.ai/v1",
    }
    PLACEHOLDER_KEYS = (
        "{agent_version}, {provider}, {provider_key}, {model}, {reasoning_effort}, "
        "{chat_id}, {user_id}, {session_name}, {session_messages}, "
        "{runtime_comments_count}, {runtime_comments}, {tool_count}, {available_tool_count}, "
        "{elapsed}, {input_tokens}, {output_tokens}, {total_tokens}, {thinking}, "
        "{todo}, {random}, {prefix}, {time}, {date}"
    )
    WEB_SEARCH_RE = re.compile(
        r"<web_search>\s*(.*?)\s*</web_search>", re.DOTALL | re.I
    )
    SEND_RE = re.compile(
        r'<send_message(?:\s+chat=["\']([^"\']+)["\'])?\s*>(.*?)</send_message>',
        re.DOTALL | re.I,
    )
    SKILL_RE = re.compile(
        r'<skill\s+name=["\']([^"\']+)["\']\s*>(.*?)</skill>', re.DOTALL | re.I
    )
    CREATE_CHANNEL_RE = re.compile(
        r"<create_channel([^>]*)>(.*?)</create_channel>", re.DOTALL | re.I
    )
    CREATE_GROUP_RE = re.compile(
        r"<create_group([^>]*)>(.*?)</create_group>", re.DOTALL | re.I
    )
    CREATE_BOT_RE = re.compile(
        r"<create_bot([^>]*)>(.*?)</create_bot>", re.DOTALL | re.I
    )
    SEARCH_MESSAGES_RE = re.compile(
        r"<search_messages([^>]*)>(.*?)</search_messages>", re.DOTALL | re.I
    )
    UPDATE_PROFILE_RE = re.compile(
        r"<update_profile([^>]*)>(.*?)</update_profile>", re.DOTALL | re.I
    )
    SET_PROFILE_PHOTO_RE = re.compile(
        r"<set_profile_photo([^>]*)>(.*?)</set_profile_photo>", re.DOTALL | re.I
    )
    DELETE_MESSAGES_RE = re.compile(
        r"<delete_messages([^>]*)>(.*?)</delete_messages>", re.DOTALL | re.I
    )
    FORWARD_MESSAGE_RE = re.compile(
        r"<forward_message([^>]*)>(.*?)</forward_message>", re.DOTALL | re.I
    )
    DOWNLOAD_MEDIA_RE = re.compile(
        r"<download_media([^>]*)>(.*?)</download_media>", re.DOTALL | re.I
    )
    GENERATED_FILE_RE = re.compile(
        r'<file\s+name=["\']([^"\']+)["\']\s*>(.*?)</file>',
        re.DOTALL | re.I,
    )
    MCUB_DOCS_URL = "https://x0.at/y2rb.md"
    TOOL_CALL_RE = re.compile(
        r"<([a-z0-9._]+)([^>]*)>(.*?)</\1>|<([a-z0-9._]+)([^>]*)/?>", re.DOTALL | re.I
    )
    TOOL_CALL_JSON_RE = re.compile(r"```tool_call\s*(.*?)```", re.DOTALL | re.I)
    TOOL_REGISTRY = (
        # Core/module-tied tools. Most tools should come from plugins.
        "thinking.note",
        "skills.list",
        "skills.read",
        "skills.activate",
        "skills.import_md",
        "skills.export_md",
        "skills.save_from_ai",
        "skills.install",
        "skills.repo_list",
        "code.generate_file",
        "code.generate_mcub_module",
        "code.choose_filename",
        "code.attach_result",
        "code.read_docs",
        "context.remember",
        "context.clear",
        "context.regenerate",
        "context.reply_context",
        "context.media_context",
        "todo.add",
        "todo.delete",
        "todo.edit",
        "todo.current",
        "todo.close",
        "todo.closeall",
        "todo.clear",
        "utility.token_usage",
        "utility.placeholders",
        "utility.random_template",
        "utility.agent_log",
        "utility.error_file",
        "utility.tool_help",
        "utility.list_tools",
    )
    AGENT_MAX_STEPS = 15
    PREMIUM_EMOJIS = {
        "claude": '<tg-emoji emoji-id="5368808376694248152">💬</tg-emoji>',
        "start": '<tg-emoji emoji-id="5368434680179758177">🏁</tg-emoji>',
        "workout": '<tg-emoji emoji-id="5368387680352637360">🏋️‍♂️</tg-emoji>',
        "party": '<tg-emoji emoji-id="5368635272332352173">🎉</tg-emoji>',
        "loading_dots": '<tg-emoji emoji-id="5328311576736833844">🔴</tg-emoji>',
        "loading_wait": '<tg-emoji emoji-id="5326015457155620929">😐</tg-emoji>',
        "reconnect": '<tg-emoji emoji-id="5325872701032635449">⏳</tg-emoji>',
        "loading_squares": '<tg-emoji emoji-id="5334960765931626355">🎲</tg-emoji>',
        "loading_lava": '<tg-emoji emoji-id="5310041868191407556">🩸</tg-emoji>',
        "soon": '<tg-emoji emoji-id="5411382892850871522">🔜</tg-emoji>',
        "top": '<tg-emoji emoji-id="5411132595041765682">🔝</tg-emoji>',
        "linux": '<tg-emoji emoji-id="5300957668762987048">👩‍💻</tg-emoji>',
        "js": '<tg-emoji emoji-id="5300896259320586992">👩‍💻</tg-emoji>',
        "ts": '<tg-emoji emoji-id="5301254000031572585">👩‍💻</tg-emoji>',
        "grid": '<tg-emoji emoji-id="5294096239464295059">🔵</tg-emoji>',
        "done": '<tg-emoji emoji-id="4916036072560919511">✅</tg-emoji>',
        "warn": '<tg-emoji emoji-id="4915853119839011973">⚠️</tg-emoji>',
        "link": '<tg-emoji emoji-id="4916086774649848789">🔗</tg-emoji>',
        "web": '<tg-emoji emoji-id="4906943755644306322">🌐</tg-emoji>',
        "telegram": '<tg-emoji emoji-id="4918203446202467778">💙</tg-emoji>',
        "at": '<tg-emoji emoji-id="5082413149873767213">💙</tg-emoji>',
        "lock": '<tg-emoji emoji-id="4904500559203009298">🔒</tg-emoji>',
        "bubble": '<tg-emoji emoji-id="4918408122868958076">🖱️</tg-emoji>',
        "back": '<tg-emoji emoji-id="5352759161945867747">🔙</tg-emoji>',
        "block": '<tg-emoji emoji-id="5408830797513784663">🚫</tg-emoji>',
        "blink": '<tg-emoji emoji-id="5411528341918356895">⚪️</tg-emoji>',
        "terminal": '<tg-emoji emoji-id="5409076727341154520">⚙️</tg-emoji>',
        "num_0": '<tg-emoji emoji-id="5140999334174655345">0️⃣</tg-emoji>',
        "num_1": '<tg-emoji emoji-id="5141109049114232089">1️⃣</tg-emoji>',
        "num_2": '<tg-emoji emoji-id="5140871649091912628">2️⃣</tg-emoji>',
        "num_3": '<tg-emoji emoji-id="5141399818400170896">3️⃣</tg-emoji>',
        "num_4": '<tg-emoji emoji-id="5138822752123225428">4️⃣</tg-emoji>',
        "num_5": '<tg-emoji emoji-id="5141062672057369534">5️⃣</tg-emoji>',
        "num_6": '<tg-emoji emoji-id="5139005588881015916">6️⃣</tg-emoji>',
        "num_7": '<tg-emoji emoji-id="5140999557512954818">7️⃣</tg-emoji>',
        "num_8": '<tg-emoji emoji-id="5141013683660391172">8️⃣</tg-emoji>',
        "num_9": '<tg-emoji emoji-id="5141137309999039199">9️⃣</tg-emoji>',
    }
    config = ModuleConfig(
        Group(
            "Provider & Model 🧠",
            [
                ConfigValue(
                    "provider",
                    "openai",
                    description="Provider: openai, google, openrouter, groq, deepseek, xai, other",
                    validator=Choice(choices=list(PROVIDERS), default="openai"),
                ),
                ConfigValue(
                    "api_key",
                    "",
                    description="API key for the selected provider",
                    validator=Secret(default=""),
                ),
                ConfigValue(
                    "model",
                    "",
                    description="Model name. Empty means provider default",
                    validator=String(default=""),
                ),
                ConfigValue(
                    "custom_base_url",
                    "",
                    description="Endpoint for provider=other, e.g. https://api.deepseek.com/v1",
                    validator=String(default=""),
                ),
                ConfigValue(
                    "system_prompt",
                    "You are OpenAgent inside a Telegram userbot. Help the user directly. You may inspect the local workspace through terminal commands when needed.",
                    description="System prompt for the agent",
                    validator=String(
                        default="You are OpenAgent inside a Telegram userbot. Help the user directly. You may inspect the local workspace through terminal commands when needed."
                    ),
                ),
                ConfigValue(
                    "temperature",
                    0.7,
                    description="Sampling temperature",
                    validator=Float(default=0.7, min=0.0, max=2.0),
                ),
                ConfigValue(
                    "max_tokens",
                    1200,
                    description="Maximum response tokens",
                    validator=Integer(default=1200, min=64, max=32768),
                ),
                ConfigValue(
                    "reasoning_effort",
                    "off",
                    description="Reasoning effort for models/providers that support it: off, low, medium, high, xhigh",
                    validator=Choice(
                        choices=["off", "low", "medium", "high", "xhigh"], default="off"
                    ),
                ),
                ConfigValue(
                    "timeout",
                    180,
                    description="HTTP timeout seconds for each provider request. Increase for slow reasoning/code tasks.",
                    validator=Integer(default=180, min=10, max=600),
                ),
                ConfigValue(
                    "provider_reconnect_attempts",
                    5,
                    description="Maximum reconnect attempts after provider API timeout",
                    validator=Integer(default=5, min=0, max=5),
                ),
            ],
            description="AI provider, credentials, model and request limits",
            button_text="🧠 Provider",
            key="provider_model",
        ),
        Group(
            "Tools & Permissions 🛠",
            [
                ConfigValue(
                    "terminal_enabled",
                    True,
                    description="Allow the agent to execute terminal commands",
                    validator=Boolean(default=True),
                ),
                ConfigValue(
                    "terminal_steps",
                    3,
                    description="Maximum terminal commands per request",
                    validator=Integer(default=3, min=0, max=10),
                ),
                ConfigValue(
                    "terminal_timeout",
                    30,
                    description="Terminal command timeout seconds",
                    validator=Integer(default=30, min=3, max=120),
                ),
                ConfigValue(
                    "web_search_enabled",
                    True,
                    description="Allow the agent to search the web",
                    validator=Boolean(default=True),
                ),
                ConfigValue(
                    "web_search_steps",
                    3,
                    description="Maximum web searches per request",
                    validator=Integer(default=3, min=0, max=10),
                ),
                ConfigValue(
                    "mcub_use",
                    False,
                    description="Allow the agent to execute MCUB userbot commands",
                    validator=Boolean(default=False),
                ),
                ConfigValue(
                    "mcub_steps",
                    3,
                    description="Maximum MCUB commands per request",
                    validator=Integer(default=3, min=0, max=10),
                ),
                ConfigValue(
                    "send_messages_enabled",
                    True,
                    description="Allow the agent to send messages as the userbot",
                    validator=Boolean(default=True),
                ),
                ConfigValue(
                    "send_message_steps",
                    3,
                    description="Maximum userbot messages sent per request",
                    validator=Integer(default=3, min=0, max=10),
                ),
                ConfigValue(
                    "create_chats_enabled",
                    True,
                    description="Allow the agent to create channels/groups",
                    validator=Boolean(default=True),
                ),
                ConfigValue(
                    "create_chat_steps",
                    2,
                    description="Maximum channels/groups created per request",
                    validator=Integer(default=2, min=0, max=5),
                ),
                ConfigValue(
                    "create_bots_enabled",
                    True,
                    description="Allow the agent to create Telegram bots via BotFather",
                    validator=Boolean(default=True),
                ),
                ConfigValue(
                    "create_bot_steps",
                    1,
                    description="Maximum Telegram bots created per request",
                    validator=Integer(default=1, min=0, max=3),
                ),
                ConfigValue(
                    "account_tools_enabled",
                    True,
                    description="Allow the agent to edit profile/join chats/read/search messages",
                    validator=Boolean(default=True),
                ),
                ConfigValue(
                    "account_tool_steps",
                    5,
                    description="Maximum account-level tools per request",
                    validator=Integer(default=5, min=0, max=15),
                ),
                ConfigValue(
                    "chat_management_enabled",
                    True,
                    description="Allow the agent to manage chats: mute, ban, promote, title, slowmode",
                    validator=Boolean(default=True),
                ),
                ConfigValue(
                    "chat_management_steps",
                    5,
                    description="Maximum chat-management tools per request",
                    validator=Integer(default=5, min=0, max=15),
                ),
                ConfigValue(
                    "media_max_bytes",
                    8_000_000,
                    description="Maximum replied media bytes sent to AI",
                    validator=Integer(default=8_000_000, min=1024, max=25_000_000),
                ),
            ],
            description="Terminal, web, MCUB and Telegram action limits",
            button_text="🛠 Tools",
            key="tools_permissions",
        ),
        Group(
            "Context & Memory 🧾",
            [
                ConfigValue(
                    "context_enabled",
                    True,
                    description="Remember chat context between .oa requests",
                    validator=Boolean(default=True),
                ),
                ConfigValue(
                    "context_turns",
                    10,
                    description="How many user/assistant turns to remember per chat",
                    validator=Integer(default=10, min=0, max=50),
                ),
                ConfigValue(
                    "context_compaction_enabled",
                    True,
                    description="Automatically summarize old chat context when it becomes too large",
                    validator=Boolean(default=True),
                ),
                ConfigValue(
                    "context_compaction_chars",
                    18000,
                    description="Compact remembered chat context after this many characters",
                    validator=Integer(default=18000, min=2000, max=200000),
                ),
                ConfigValue(
                    "context_compaction_keep_turns",
                    2,
                    description="Recent user/assistant turns to keep verbatim after compaction",
                    validator=Integer(default=2, min=0, max=10),
                ),
                ConfigValue(
                    "context_compaction_max_tokens",
                    900,
                    description="Maximum tokens used for the compaction summary response",
                    validator=Integer(default=900, min=128, max=4096),
                ),
                ConfigValue(
                    "tool_memory_enabled",
                    False,
                    description="Remember concise notes from tool outputs for next requests",
                    validator=Boolean(default=False),
                ),
                ConfigValue(
                    "tool_memory_items",
                    20,
                    description="Maximum remembered tool notes per chat",
                    validator=Integer(default=20, min=1, max=200),
                ),
                ConfigValue(
                    "tool_memory_max_chars",
                    500,
                    description="Maximum characters per remembered tool note",
                    validator=Integer(default=500, min=80, max=4000),
                ),
            ],
            description="Chat memory, compaction and tool notes",
            button_text="🧾 Context",
            key="context_memory",
        ),
        Row(),
        Group(
            "Templates & Display 🎨",
            [
                ConfigValue(
                    "response_header",
                    '<blockquote><a href="tg://emoji?id=6010179991944305029">☺️</a> <strong>OpenAgent</strong>: <a href="tg://emoji?id=5325872701032635449">⏳</a>  <em>{elapsed}</em>s\n• <u>{provider}/{model}</u>  •  <code>{reasoning_effort}</code>\n| | | | | | | | | | | | | | | | | | | | | | | | | | |\n<a href="tg://emoji?id=5408994848084624514">💸</a> <strong>in</strong> <em>{input_tokens}</em>, <strong>out</strong> <em>{output_tokens}</em> | <b>total</b>\n<i>{total_tokens}</i> | <strong>tool use:</strong> <em>{tool_count}</em></blockquote>\n<blockquote expandable><i>{thinking}</i></blockquote>',
                    description="Final response header template. Placeholders: "
                    + PLACEHOLDER_KEYS,
                    validator=String(
                        default='<blockquote><a href="tg://emoji?id=6010179991944305029">☺️</a> <strong>OpenAgent</strong>: <a href="tg://emoji?id=5325872701032635449">⏳</a>  <em>{elapsed}</em>s\n• <u>{provider}/{model}</u>  •  <code>{reasoning_effort}</code>\n| | | | | | | | | | | | | | | | | | | | | | | | | | |\n<a href="tg://emoji?id=5408994848084624514">💸</a> <strong>in</strong> <em>{input_tokens}</em>, <strong>out</strong> <em>{output_tokens}</em> | <b>total</b>\n<i>{total_tokens}</i> | <strong>tool use:</strong> <em>{tool_count}</em></blockquote>\n<blockquote expandable><i>{thinking}</i></blockquote>'
                    ),
                ),
                ConfigValue(
                    "request_label",
                    '<a href="tg://emoji?id=6010352868672936598"><strong>🐈‍⬛</strong></a><strong></strong><strong> Prompt:</strong>',
                    description="Request block label template. Placeholders: "
                    + PLACEHOLDER_KEYS,
                    validator=String(
                        default='<a href="tg://emoji?id=6010352868672936598"><strong>🐈‍⬛</strong></a><strong></strong><strong> Prompt:</strong>'
                    ),
                ),
                ConfigValue(
                    "response_label",
                    '<a href="tg://emoji?id=6010286885090368072"><strong>❌</strong></a><strong></strong><strong> Answer:</strong>',
                    description="Response block label template. Placeholders: "
                    + PLACEHOLDER_KEYS,
                    validator=String(
                        default='<a href="tg://emoji?id=6010286885090368072"><strong>❌</strong></a><strong></strong><strong> Answer:</strong>'
                    ),
                ),
                ConfigValue(
                    "thinking_template",
                    '<blockquote><a href="tg://emoji?id=6010292571627069263">😎</a> <u>{provider}/{model}</u> • <em>prepares the response...</em></blockquote >\n<blockquote><a href="tg://emoji?id=5404857686477015710">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>',
                    description="Initial loading/thinking message template. Placeholders: "
                    + PLACEHOLDER_KEYS,
                    validator=String(
                        default='<blockquote><a href="tg://emoji?id=6010292571627069263">😎</a> <u>{provider}/{model}</u> • <em>prepares the response...</em></blockquote >\n<blockquote><a href="tg://emoji?id=5404857686477015710">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>'
                    ),
                ),
                ConfigValue(
                    "tool_display_template",
                    '<blockquote expandable><i>{thinking_line}</i></blockquote>\n<blockquote expandable><strong>┌|</strong> {tool_state_emoji_html} {status_emoji_html} <em>{status_text}</em> <code>{tool}</code>\n<strong>└|</strong> <a href="tg://emoji?id=6010570945637392851">🥳</a>  <b>Round:</b> <code>{round}/{round_total}</code> • <b>Reasoning:</b>\n<code>{reasoning_effort}</code>\n</blockquote><blockquote><a href="tg://emoji?id=5310041868191407556">🩸</a> <strong>{activity_line}</strong></blockquote>\n<blockquote expandable><a href="tg://emoji?id=6012361831035705571">😪</a> <strong>Log tools</strong>\n<code>{log_lines}</code></blockquote>',
                    description="Tool execution status template. Raw: {tool}, {title}, {value}, {log}, {step}. Semantic: {round}, {round_total}, {progress_bar}, {progress_percent}, {status_emoji}, {status_icon}, {status_emoji_html}, {status_icon_html}, {status_text}, {tool_state}, {tool_state_emoji}, {tool_state_icon}, {tool_state_emoji_html}, {tool_state_icon_html}, {tool_running_emoji}, {tool_running_icon}, {tool_running_emoji_html}, {tool_running_icon_html}, {tool_done_emoji}, {tool_done_icon}, {tool_done_emoji_html}, {tool_done_icon_html}, {tool_group}, {tool_short}, {tool_input}, {tool_input_block}, {thinking_line}, {thinking_block}, {log_lines}, {log_block}, {log_count}, {elapsed_line}, {token_line}, {model_line}, {activity_line}. General placeholders: "
                    + PLACEHOLDER_KEYS,
                    validator=String(
                        default='<blockquote expandable><i>{thinking_line}</i></blockquote>\n<blockquote expandable><strong>┌|</strong> {tool_state_emoji_html} {status_emoji_html} <em>{status_text}</em> <code>{tool}</code>\n<strong>└|</strong> <a href="tg://emoji?id=6010570945637392851">🥳</a>  <b>Round:</b> <code>{round}/{round_total}</code> • <b>Reasoning:</b>\n<code>{reasoning_effort}</code>\n</blockquote><blockquote><a href="tg://emoji?id=5310041868191407556">🩸</a> <strong>{activity_line}</strong></blockquote>\n<blockquote expandable><a href="tg://emoji?id=6012361831035705571">😪</a> <strong>Log tools</strong>\n<code>{log_lines}</code></blockquote>'
                    ),
                ),
                ConfigValue(
                    "tool_status_emojis",
                    "thinking=❔\nterminal=🖥\nweb=🌐\nfile=📦\nmcub=🧲\nmessage=💬\ndialog=🗂\nchat=🐈‍⬛\nmoderation=🛡\nprofile=👤\ncontacts=👥\ncreation=✨\nskills=🧠\ncode=🧬\ncontext=🧾\nutility=🛠\ndefault=🛠",
                    description="Custom emoji/icon map for {status_emoji}/{status_icon}. Format: group_or_tool=emoji per line. Tool-specific keys like terminal.run or thinking.note override groups like terminal/thinking. Premium emoji HTML is allowed via {status_emoji_html}/{status_icon_html}.",
                    validator=String(
                        default="thinking=❔\nterminal=🖥\nweb=🌐\nfile=📦\nmcub=🧲\nmessage=💬\ndialog=🗂\nchat=🐈‍⬛\nmoderation=🛡\nprofile=👤\ncontacts=👥\ncreation=✨\nskills=🧠\ncode=🧬\ncontext=🧾\nutility=🛠\ndefault=🛠"
                    ),
                ),
                ConfigValue(
                    "tool_display_max_chars",
                    1200,
                    description="Maximum chars from current tool input shown in status form",
                    validator=Integer(default=1200, min=0, max=4000),
                ),
                ConfigValue(
                    "tool_display_log_lines",
                    8,
                    description="How many recent tool names to show in status form",
                    validator=Integer(default=8, min=0, max=30),
                ),
                ConfigValue(
                    "thinking_display_limit",
                    3,
                    description="How many recent thinking.note entries to show in {thinking}",
                    validator=Integer(default=3, min=0, max=20),
                ),
                ConfigValue(
                    "thinking_empty_text",
                    "Модель ещё не думала.",
                    description="Text for {thinking} when no thinking.note entries exist",
                    validator=String(default="Модель ещё не думала."),
                ),
                ConfigValue(
                    "thinking_bullet",
                    "•",
                    description="Prefix marker for each thinking.note line in {thinking}. Empty disables the marker",
                    validator=String(default="•"),
                ),
                ConfigValue(
                    "random_strings",
                    ["Thinking...", "Думаю...", "Генерирую..."],
                    description="Random lines for {random}",
                    validator=List(
                        default=["Thinking...", "Думаю...", "Генерирую..."],
                        item_type=str,
                    ),
                ),
                ConfigValue(
                    "todo_status_emojis",
                    "pending=...\nopen=>>>\nclosed=---",
                    description="State markers for {todo}. Format: pending=..., open=>>>, closed=---",
                    validator=String(default="pending=...\nopen=>>>\nclosed=---"),
                ),
                ConfigValue(
                    "placeholders",
                    "",
                    description="Available OpenAgent placeholders (auto-generated)",
                    validator=String(default=""),
                ),
            ],
            description="Response headers, labels, thinking and tool status templates",
            button_text="🎨 Display",
            key="templates_display",
        ),
        Group(
            "Repo Context & Skills 📚",
            [
                ConfigValue(
                    "repo_context_enabled",
                    True,
                    description="Inject local workspace snapshot into system prompt",
                    validator=Boolean(default=True),
                ),
                ConfigValue(
                    "repo_context_max_chars",
                    7000,
                    description="Maximum chars used for repo context in system prompt",
                    validator=Integer(default=7000, min=500, max=30000),
                ),
                ConfigValue(
                    "skills_enabled",
                    True,
                    description="Enable loading OpenAgent skills into the system prompt",
                    validator=Boolean(default=True),
                ),
                ConfigValue(
                    "skills_trigger_mode",
                    "auto",
                    description="When to load skills: auto = only on keyword match, always = every request, off = never",
                    validator=String(default="auto"),
                ),
                ConfigValue(
                    "skill_repo_url",
                    "https://raw.githubusercontent.com/hairpin01/repo-MCUB-fork/main/OpenAgent/skills",
                    description="Base URL for installable OpenAgent skills repository",
                    validator=String(
                        default="https://raw.githubusercontent.com/hairpin01/repo-MCUB-fork/main/OpenAgent/skills"
                    ),
                ),
            ],
            description="Workspace context and OpenAgent skills loading",
            button_text="📚 Skills",
            key="repo_skills",
        ),
        Group(
            "Tool Confirmations 🛡",
            [
                ConfigValue(
                    "tool_confirmation_enabled",
                    True,
                    description="Ask for confirmation before tools that can change files, chats, account state, or run commands",
                    validator=Boolean(default=True),
                ),
                ConfigValue(
                    "tool_confirmation_mode",
                    "medium",
                    description="How often to ask before tools: low = only critical/destructive, medium = write/actions, high = almost every non-read tool",
                    validator=Choice(
                        choices=["low", "medium", "high"], default="medium"
                    ),
                ),
                ConfigValue(
                    "tool_confirmation_template",
                    '<blockquote><a href="tg://emoji?id=6010201728773790293">😈</a> Continue?\n<a href="tg://emoji?id=6012317326584583729">😐</a> Tool: {tool} • {elapsed}s</blockquote>\n<blockquote expandable><a href="tg://emoji?id=6010394680179562842">😶</a> <b>What will be completed</b>\n<a href="tg://emoji?id=6010292550152230657">☀️</a> <code>{value}</code></blockquote>',
                    description="Confirmation form template. Placeholders: {tool}, {value}, {elapsed}, {elapsed_line}",
                    validator=String(
                        default='<blockquote><a href="tg://emoji?id=6010201728773790293">😈</a> Continue?\n<a href="tg://emoji?id=6012317326584583729">😐</a> Tool: {tool} • {elapsed}s</blockquote>\n<blockquote expandable><a href="tg://emoji?id=6010394680179562842">😶</a> <b>What will be completed</b>\n<a href="tg://emoji?id=6010292550152230657">☀️</a> <code>{value}</code></blockquote>'
                    ),
                ),
                ConfigValue(
                    "tool_confirmation_yes_text",
                    "Выполнить",
                    description="Confirm button text for dangerous tools",
                    validator=String(default="Выполнить"),
                ),
                ConfigValue(
                    "tool_confirmation_no_text",
                    "Не сейчас",
                    description="Cancel button text for dangerous tools",
                    validator=String(default="Не сейчас"),
                ),
                ConfigValue(
                    "tool_confirmation_timeout",
                    900,
                    description="Seconds to wait for dangerous tool confirmation",
                    validator=Integer(default=900, min=10, max=3600),
                ),
            ],
            description="Confirmation policy and prompt/button templates",
            button_text="🛡 Confirm",
            key="confirmations",
        ),
        Row(),
        Answer('❔ About', 'AI agent in userbot with refreshed tool architecture')
    )
    SESSION_LIMIT = 20
    from .mcub_event import _MCUBEvent

    @callback(ttl=900)
    async def _open_sessions_panel(
        self, call: InlineMessage, chat_id: int | None = None
    ) -> None:
        cid = int(
            chat_id
            or getattr(call, "chat_id", 0)
            or getattr(call, "_openagent_source_chat_id", 0)
            or 0
        )
        if not cid:
            await call.answer(
                self.strings("error", error="chat_id is missing"), alert=True
            )
            return
        await self._show_sessions_panel(call, cid)

    @callback(ttl=900)
    async def _return_to_last_response(self, call: InlineMessage, chat_id: int) -> None:
        cid = int(chat_id)
        saved_turn = self._last_saved_assistant_turn(cid)
        if not saved_turn:
            await call.answer(self.strings("saved_response_missing"), alert=True)
            return
        prompt, answer, thinking_notes = saved_turn
        with contextlib.suppress(Exception):
            setattr(call, "_openagent_source_chat_id", cid)
        self._set_placeholder_context(call)
        await self._reply_text(
            call,
            answer,
            title=self._response_title(
                0.0, tool_count=0, thinking_notes=thinking_notes
            ),
            prompt=prompt,
            thinking_notes=thinking_notes,
            buttons=self._final_buttons(
                cid,
                prompt,
                prompt,
                [],
                source_event=call,
            ),
            edit_current=True,
        )
        self._store_last_loading(cid, call)

    @callback(ttl=900)
    async def _switch_session(self, call: InlineMessage, session_id: str) -> None:
        session = self._sessions.get(str(session_id))
        if session is None:
            await call.answer(self.strings("skill_not_found"), alert=True)
            return
        self._set_active_session(session.chat_id, session.id)
        self.session_manager.set_preference(session.chat_id, "continue")
        await self._show_sessions_panel(
            call,
            session.chat_id,
            alert=self.strings("chat_switched", name=session.name),
        )

    @callback(ttl=900)
    async def _remember_session_choice(self, call: InlineMessage, chat_id: int) -> None:
        self.session_manager.set_preference(int(chat_id), "continue")
        await self._save_sessions()
        await call.answer(self.strings("chat_choice_saved"), alert=True)

    @callback(ttl=900)
    async def _delete_active_session(self, call: InlineMessage, chat_id: int) -> None:
        cid = int(chat_id)
        sessions = self._get_chat_sessions(cid)
        if len(sessions) <= 1:
            await call.answer(self.strings("chat_delete_last"), alert=True)
            return
        active = self._get_active_session(cid)
        self._sessions.pop(active.id, None)
        remaining = self._get_chat_sessions(cid)
        self._active_session[cid] = remaining[0].id
        await self._save_sessions()
        await self._show_sessions_panel(call, cid, alert=self.strings("chat_deleted"))

    @callback(ttl=900)
    async def _run_pending_here(self, call: InlineMessage, prompt_token: str) -> None:
        """Run pending prompt in the current active session."""
        chat_id = self._pending_prompts.get(prompt_token, {}).get("chat_id")
        if chat_id:
            self.session_manager.set_preference(int(chat_id), "continue")
        await self._execute_pending(call, prompt_token)

    @callback(ttl=900)
    async def _run_pending_in(
        self,
        call: InlineMessage,
        prompt_token: str,
        session_id: str,
    ) -> None:
        """Switch to another session, then run the pending prompt."""
        session = self._sessions.get(str(session_id))
        if session is None:
            with contextlib.suppress(Exception):
                await call.answer(self.strings("chat_delete_last"), alert=True)
            return
        self._set_active_session(session.chat_id, session.id)
        self.session_manager.set_preference(session.chat_id, "continue")
        await self._execute_pending(call, prompt_token)

    @callback(ttl=900)
    async def _remember_pref_continue(
        self,
        call: InlineMessage,
        prompt_token: str,
        chat_id: int,
    ) -> None:
        """Save 'always continue here' pref then run pending in current session."""
        self.session_manager.set_preference(int(chat_id), "continue")
        with contextlib.suppress(Exception):
            await call.answer(self.strings("pref_saved"), alert=False)
        await self._execute_pending(call, prompt_token)

    @callback(ttl=900)
    async def _remember_pref_new(
        self,
        call: InlineMessage,
        prompt_token: str,
        chat_id: int,
    ) -> None:
        """Save 'always create new' pref, create new session, then run."""
        cid = int(chat_id)
        self.session_manager.set_preference(cid, "new")
        self._fresh_session(cid)
        with contextlib.suppress(Exception):
            await call.answer(self.strings("pref_saved"), alert=False)
        await self._execute_pending(call, prompt_token)

    @callback(ttl=900)
    async def _confirm_tool_action(
        self,
        call: InlineMessage,
        token: str | None = None,
        approved: bool = False,
    ) -> None:
        if token:
            future = self._tool_confirmation_waiters.get(token)
            if future is not None and not future.done():
                future.set_result(bool(approved))
        with contextlib.suppress(Exception):
            await call.answer(
                (
                    self.strings("tool_confirmation_approved")
                    if approved
                    else self.strings("cancelled")
                ),
                alert=False,
            )

    @callback(ttl=900)
    async def _activate_inline_status(
        self, call: InlineMessage, token: str | None = None
    ) -> None:
        if token:
            future = self._inline_status_waiters.get(token)
            if future is not None and not future.done():
                future.set_result(call)
        with contextlib.suppress(Exception):
            await call.answer()

    def _oa_arg_parser(self, event: Event) -> Any | None:
        with contextlib.suppress(Exception):
            return self.args(event)
        return None

    def _oa_prompt_from_parser(self, parser: Any | None) -> str:
        if parser is None:
            return ""
        raw = str(getattr(parser, "raw_args", "") or "")
        raw = re.sub(r"(?<!\S)--test(?:=\S+|\s+\S+)?", "", raw)
        raw = re.sub(
            r"(?<!\S)--new(?:=(?:\{[^}]*\}|\"[^\"]*\"|'[^']*'|\S*))?(?=\s|$)", "", raw
        )
        raw = re.sub(r"(?<!\S)(?:--flash|-f)(?=\s|$)", "", raw)
        return re.sub(r"\s+", " ", raw).strip()

    def _oa_flash_arg(self, parser: Any | None) -> bool:
        if parser is None:
            return False
        with contextlib.suppress(Exception):
            if bool(parser.get_flag("flash")) or bool(parser.get_flag("f")):
                return True
        raw = str(getattr(parser, "raw_args", "") or "")
        return bool(re.search(r"(?<!\S)(?:--flash|-f)(?=\s|$)", raw))

    def _oa_new_chat_arg(self, parser: Any | None) -> tuple[bool, str]:
        if parser is None:
            return False, ""
        raw = str(getattr(parser, "raw_args", "") or "")
        match = re.search(
            r"(?<!\S)--new(?:=(?:\{[^}]*\}|\"[^\"]*\"|'[^']*'|\S*))?(?=\s|$)", raw
        )
        if not match:
            return False, ""
        token = match.group(0)
        if "=" not in token:
            return True, ""
        name = token.split("=", 1)[1].strip()
        if len(name) >= 2 and (
            (name[0] == name[-1] and name[0] in {'"', "'"})
            or (name[0] == "{" and name[-1] == "}")
        ):
            name = name[1:-1]
        return True, name.strip()[:64]

    def _oa_test_name(self, parser: Any | None) -> str:
        if parser is None or not hasattr(parser, "get_kwarg"):
            return ""
        return str(parser.get_kwarg("test", "") or "").strip().lower()

    async def _run_oa_test(self, event: Event, name: str) -> None:
        """Run internal OpenAgent smoke tests without hitting real provider APIs."""
        name = (name or "").strip().lower()
        old_once = self._ask_provider_once
        old_show = self._show_agent_action
        old_sleep = asyncio.sleep
        calls: list[int] = []
        statuses: list[str] = []
        log: list[str] = []

        async def no_sleep(_delay: float) -> None:
            return None

        async def fake_show(
            _event: Any,
            title: str,
            value: str,
            _log: list[str],
            tool_name: str = "",
            **_kwargs: Any,
        ) -> None:
            statuses.append(f"{title}:{tool_name}:{value}")

        try:
            asyncio.sleep = no_sleep
            self._show_agent_action = fake_show  # type: ignore[method-assign]
            if name == "reconnect":

                async def fake_once(
                    _provider: str,
                    _messages: list[dict[str, Any]],
                    _api_key: str,
                    *,
                    max_tokens_override: int | None = None,
                ) -> str:
                    calls.append(1)
                    if len(calls) <= 5:
                        raise RuntimeError("Provider request timed out after 1s")
                    return "ok"

                self._ask_provider_once = fake_once  # type: ignore[method-assign]
                result = await self._ask_provider_with_reconnect(
                    "openai",
                    [],
                    "test-key",
                    status_event=event,
                    agent_log=log,
                    started_at=time.monotonic(),
                    thinking_notes=[],
                )
                text = (
                    "Reconnect test OK\n"
                    f"result={result}\n"
                    f"calls={len(calls)}\n"
                    f"statuses={len(statuses)}\n"
                    f"log={', '.join(log)}"
                )
            elif name == "timeout_provider":
                max_reconnects = max(
                    0,
                    min(int(self.config.get("provider_reconnect_attempts", 5) or 0), 5),
                )

                async def fake_once_timeout(
                    _provider: str,
                    _messages: list[dict[str, Any]],
                    _api_key: str,
                    *,
                    max_tokens_override: int | None = None,
                ) -> str:
                    calls.append(1)
                    raise RuntimeError("Provider request timed out after 1s")

                self._ask_provider_once = fake_once_timeout  # type: ignore[method-assign]
                try:
                    await self._ask_provider_with_reconnect(
                        "openai",
                        [],
                        "test-key",
                        status_event=event,
                        agent_log=log,
                        started_at=time.monotonic(),
                        thinking_notes=[],
                    )
                except Exception as exc:
                    text = (
                        "Timeout provider test OK\n"
                        f"max_reconnects={max_reconnects}\n"
                        f"calls={len(calls)}\n"
                        f"statuses={len(statuses)}\n"
                        f"error={type(exc).__name__}: {exc}\n"
                        f"log={', '.join(log)}"
                    )
                else:
                    text = "Timeout provider test FAILED: expected timeout"
            else:
                text = f"Unknown OpenAgent test: {name}"
        finally:
            self._ask_provider_once = old_once  # type: ignore[method-assign]
            self._show_agent_action = old_show  # type: ignore[method-assign]
            asyncio.sleep = old_sleep
        await self.edit(event, html.escape(text), as_html=True)

    def _config_export_blocked_keys(self) -> set[str]:
        return {"api_key", "provider", "model", "custom_base_url"}

    def _exportable_config(self) -> dict[str, Any]:
        blocked = self._config_export_blocked_keys()
        data = self.config.to_dict()
        return {
            key: value
            for key, value in data.items()
            if key not in blocked and value is not None
        }

    async def _read_import_payload(self, event: Event) -> str:
        raw = self._args_raw(event)
        if raw.strip():
            payload = raw.strip()
            if not payload.startswith("{"):
                raise ValueError(
                    "Pass a JSON object after .oaimport or reply to openagent-settings.json"
                )
            return payload
        reply = await event.get_reply_message()
        if not reply:
            return ""
        file_name = getattr(getattr(reply, "file", None), "name", None) or ""
        if file_name.lower().endswith(".json"):
            data = await reply.download_media(file=bytes)
            if data:
                payload = data.decode("utf-8", errors="replace").strip()
                if payload.startswith("{"):
                    return payload
                raise ValueError("Replied .json file does not contain a JSON object")
        text = getattr(reply, "raw_text", None) or getattr(reply, "text", None) or ""
        if text.strip():
            payload = text.strip()
            if payload.startswith("{"):
                return payload
            raise ValueError(
                "Replied message is not OpenAgent settings JSON. Reply to openagent-settings.json or JSON text."
            )
        data = await reply.download_media(file=bytes)
        if data:
            payload = data.decode("utf-8", errors="replace").strip()
            if payload.startswith("{"):
                return payload
            raise ValueError("Replied file does not contain a JSON object")
        return ""

    def _parse_import_config(self, payload: str) -> dict[str, Any]:
        try:
            data = json.loads(payload)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid OpenAgent settings JSON: {exc.msg}") from exc
        if not isinstance(data, dict):
            raise ValueError("JSON object expected")
        settings = data.get("settings", data)
        if not isinstance(settings, dict):
            raise ValueError("settings object expected")
        return settings

    async def _apply_import_config(
        self, settings: dict[str, Any]
    ) -> tuple[list[str], list[str], list[str]]:
        blocked = self._config_export_blocked_keys()
        known = set(self.config.keys())
        applied: list[str] = []
        skipped: list[str] = []
        failed: list[str] = []
        for key, value in settings.items():
            key = str(key)
            if key in blocked or key not in known:
                skipped.append(key)
                continue
            try:
                self.config[key] = value
                applied.append(key)
            except Exception as exc:
                failed.append(f"{key}: {exc}")
        if applied:
            for key in applied:
                self._invalidate_config_caches(key)
            await self.save_config()
        return applied, skipped, failed

    @command(
        "oa",
        alias=["agent"],
        doc_ru="<запрос> спросить ИИ агента; --flash/-f быстрый режим; --new[=имя] новый чат; --chats меню; --clear очистить",
        doc_en="<prompt> ask AI agent; --flash/-f fast mode; --new[=name] new chat; --chats menu; --clear clear",
    )
    async def cmd_oa(self, event: Event) -> None:
        parser = self._oa_arg_parser(event)
        prompt = (
            self._oa_prompt_from_parser(parser)
            if parser is not None
            else self._args_raw(event)
        )
        new_chat, new_chat_name = self._oa_new_chat_arg(parser)
        test_name = self._oa_test_name(parser)
        flash_mode = self._oa_flash_arg(parser)
        if test_name:
            await self._run_oa_test(event, test_name)
            return
        if prompt.strip() == "--clear" or (
            parser is not None and parser.get_flag("clear")
        ):
            chat_id = getattr(event, "chat_id", None)
            if chat_id is not None:
                session = self._get_active_session(int(chat_id))
                session.messages.clear()
                self._tool_memory.pop(int(chat_id), None)
                self._touch_session(session)
                await self.edit(
                    event, html.escape(self.strings("context_cleared")), as_html=True
                )
            else:
                await self.edit(event, self.strings("need_text"))
            return
        if prompt.strip() == "--chats" or (
            parser is not None and parser.get_flag("chats")
        ):
            chat_id = getattr(event, "chat_id", None)
            if chat_id is not None:
                await self._show_sessions_panel(event, int(chat_id), force_inline=True)
            else:
                await self.edit(event, self.strings("need_text"))
            return
        reply_context, attachments = await self._reply_context(event)
        if not prompt and reply_context:
            prompt = self.strings("reply_analyze_prompt")
        if not prompt:
            chat_id = getattr(event, "chat_id", None)
            if chat_id is not None:
                if new_chat:
                    session = self._new_session(
                        int(chat_id), name=new_chat_name or None
                    )
                    self.session_manager.set_preference(int(chat_id), "continue")
                    await self._show_sessions_panel(
                        event,
                        int(chat_id),
                        force_inline=True,
                        alert=self.strings("chat_created", name=session.name),
                    )
                    return
                await self._show_sessions_panel(event, int(chat_id), force_inline=True)
            else:
                await self.edit(event, self.strings("need_text"))
            return

        full_prompt = prompt
        if reply_context:
            full_prompt += f"\n\nReply context:\n{reply_context}"

        chat_id = getattr(event, "chat_id", None)
        if chat_id is not None:
            if new_chat:
                self._new_session(int(chat_id), name=new_chat_name or None)
                self.session_manager.set_preference(int(chat_id), "continue")
            else:
                pref = self._session_prefs.get(int(chat_id), "ask")
                sessions = self._get_chat_sessions(int(chat_id))
                if pref == "new":
                    self._fresh_session(int(chat_id))
                elif pref == "ask" and len(sessions) > 1:
                    prompt_token = self._store_pending_prompt(
                        int(chat_id),
                        prompt,
                        full_prompt,
                        attachments,
                        source_event=event,
                    )
                    await self._show_oa_choice_panel(event, int(chat_id), prompt_token)
                    return

        cancel_token = str(uuid.uuid4())
        self._set_placeholder_context(event, cancel_token)
        self.log.debug(
            "OA cmd_oa: chat_id=%s prompt_len=%d reply=%s attachments=%d",
            chat_id,
            len(prompt),
            bool(reply_context),
            len(attachments or []),
        )
        loading = await self._start_inline_status(
            event,
            self._thinking_text(),
            self._runtime_control_buttons(cancel_token, event),
        )
        started = time.monotonic()
        self.log.debug(
            "OA cmd_oa: status_event type=%s has_edit=%s has_status_buttons=%s",
            type(loading).__name__,
            hasattr(loading, "edit"),
            hasattr(loading, "_openagent_status_buttons"),
        )
        try:
            answer, agent_log, thinking_notes, tool_trace = await self._ask_agent(
                full_prompt,
                status_event=loading or event,
                source_event=event,
                attachments=attachments,
                cancel_token=cancel_token,
                started_at=started,
                flash_mode=flash_mode,
            )
            self._last_request_at = time.time()
            elapsed = time.monotonic() - started
            self._remember_context(
                getattr(event, "chat_id", None),
                full_prompt,
                answer,
                tool_trace,
                thinking_notes,
            )
            await self._reply_text(
                loading or event,
                answer,
                title=self._response_title(
                    elapsed,
                    tool_count=len(agent_log),
                    thinking_notes=thinking_notes,
                ),
                prompt=prompt,
                agent_log=agent_log,
                thinking_notes=thinking_notes,
                buttons=self._final_buttons(
                    getattr(event, "chat_id", None),
                    prompt,
                    full_prompt,
                    attachments,
                    source_event=event,
                ),
                edit_current=True,
            )
            self._store_last_loading(getattr(event, "chat_id", None), loading)
            self._cleanup_runtime_run(cancel_token)
        except Exception as exc:
            self._cleanup_runtime_run(cancel_token)
            await self._reply_error_answer(
                loading or event,
                exc,
                prompt=prompt,
                full_prompt=full_prompt,
                attachments=attachments,
                source_event=event,
                chat_id=getattr(event, "chat_id", None),
                started_at=started,
                source="OpenAgent",
            )

    @command(
        "oaexport",
        doc_ru="экспорт настроек OpenAgent без секретов",
        doc_en="export OpenAgent settings without secrets",
    )
    async def cmd_oaexport(self, event: Event) -> None:
        payload = {
            "name": "OpenAgent settings",
            "version": 1,
            "blocked_keys": sorted(self._config_export_blocked_keys()),
            "settings": self._exportable_config(),
        }
        text = json.dumps(payload, ensure_ascii=False, indent=2)
        data = io.BytesIO(text.encode("utf-8"))
        data.name = "openagent-settings.json"
        try:
            await self.client.send_file(
                event.chat_id,
                data,
                caption="OpenAgent settings export (without provider/API secrets)",
            )
            with contextlib.suppress(Exception):
                await event.delete()
        except Exception:
            await self.edit(event, f"<pre>{html.escape(text)}</pre>", as_html=True)

    @command(
        "oaimport",
        doc_ru="импорт настроек OpenAgent без секретов из reply/JSON",
        doc_en="import OpenAgent settings without secrets from reply/JSON",
    )
    async def cmd_oaimport(self, event: Event) -> None:
        try:
            payload = await self._read_import_payload(event)
            if not payload:
                await self.edit(
                    event,
                    "Reply to openagent-settings.json or pass JSON after .oaimport",
                )
                return
            settings = self._parse_import_config(payload)
            applied, skipped, failed = await self._apply_import_config(settings)
        except Exception as exc:
            await self.edit(
                event, self.strings("error", error=html.escape(str(exc))), as_html=True
            )
            return
        lines = [
            "OpenAgent settings import complete",
            f"applied: {len(applied)}",
            f"skipped: {len(skipped)}",
            f"failed: {len(failed)}",
        ]
        if skipped:
            lines.append("skipped keys: " + ", ".join(sorted(skipped)[:30]))
        if failed:
            lines.append("failed keys: " + "; ".join(failed[:10]))
        await self.edit(
            event,
            "<blockquote>" + html.escape("\n".join(lines)) + "</blockquote>",
            as_html=True,
        )

    @command(
        "skills", doc_ru="список скиллов OpenAgent", doc_en="list OpenAgent skills"
    )
    async def cmd_skills(self, event: Event) -> None:
        arg = self._args_raw(event)
        if arg in {"-repo", "--repo", "repo"}:
            try:
                text = await self._format_skill_repo_list()
            except Exception as exc:
                await self.edit(
                    event,
                    html.escape(self.strings("error", error=str(exc))),
                    as_html=True,
                )
                return
            await self.edit(event, "<pre>" + html.escape(text) + "</pre>", as_html=True)
            return

        skills = self._list_skills()
        if not skills:
            await self.edit(event, self.strings("skills_empty"))
            return
        lines = []
        for path in skills:
            try:
                text = path.read_text(encoding="utf-8")
                first_line = text.splitlines()[0] if text.splitlines() else ""
                frontmatter_name = re.search(
                    r"^name:\s*(.+)$", text, flags=re.MULTILINE
                )
                frontmatter_description = re.search(
                    r"^description:\s*(.+)$", text, flags=re.MULTILINE
                )
            except Exception:
                first_line = ""
                frontmatter_name = None
                frontmatter_description = None
            name = (
                frontmatter_name.group(1).strip()
                if frontmatter_name
                else self._skill_name_from_path(path)
            )
            title = (
                frontmatter_description.group(1).strip()
                if frontmatter_description
                else (
                    first_line.lstrip("# ").strip()
                    if first_line.startswith("#")
                    else name
                )
            )
            lines.append(f"- {name}: {title}")
        await self.edit(
            event, "<pre>" + html.escape("\n".join(lines)) + "</pre>", as_html=True
        )

    @command(
        "skillinstall",
        alias=["ssinstall"],
        doc_ru="<name> установить OpenAgent skill из repo",
        doc_en="<name> install OpenAgent skill from repo",
    )
    async def cmd_skillinstall(self, event: Event) -> None:
        name = self._args_raw(event)
        if not name:
            await self.edit(event, self.strings("skillinstall_usage"))
            return
        try:
            saved_name = await self._install_repo_skill(name)
        except Exception as exc:
            await self.edit(
                event, html.escape(self.strings("error", error=str(exc))), as_html=True
            )
            return
        await self.edit(
            event,
            self.strings("skill_installed", name=html.escape(saved_name)),
            as_html=True,
        )

    @command(
        "sendss", doc_ru="<name> отправить .md скилл", doc_en="<name> send skill .md"
    )
    async def cmd_sendss(self, event: Event) -> None:
        name = self._args_raw(event)
        if not name:
            await self.edit(event, self.strings("sendss_usage"))
            return
        path = self._find_skill_path(name)
        if not path.exists():
            await self.edit(event, self.strings("skill_not_found"))
            return
        await self.client.send_file(
            event.chat_id,
            str(path),
            caption=f"<b>Skill:</b> <code>{html.escape(self._skill_name_from_path(path))}</code>",
            parse_mode="html",
        )
        try:
            await event.delete()
        except Exception:
            pass

    @command(
        "imss",
        doc_ru="[name] импортировать .md скилл из reply",
        doc_en="[name] import .md skill from reply",
    )
    async def cmd_imss(self, event: Event) -> None:
        reply = await event.get_reply_message()
        if not reply:
            await self.edit(event, self.strings("imss_need_reply"))
            return

        name = self._args_raw(event)
        file_name = getattr(getattr(reply, "file", None), "name", None) or ""
        content = ""
        try:
            data = await reply.download_media(file=bytes)
            if data:
                content = data.decode("utf-8", errors="replace")
        except Exception:
            content = ""

        if not content:
            content = (
                getattr(reply, "raw_text", None) or getattr(reply, "text", "") or ""
            )
        if not content.strip():
            await self.edit(event, self.strings("skill_empty"))
            return

        if not name:
            if file_name.lower().endswith(".md"):
                name = Path(file_name).stem
            else:
                match = re.search(r"^#\s+(.+)$", content, flags=re.MULTILINE)
                name = match.group(1).strip() if match else "skill"

        saved_name = self._save_skill(name, content)
        await self.edit(
            event,
            self.strings("skill_imported", name=html.escape(saved_name)),
            as_html=True,
        )

    @command("delss", doc_ru="<name> удалить скилл", doc_en="<name> delete skill")
    async def cmd_delss(self, event: Event) -> None:
        name = self._args_raw(event)
        if not name:
            await self.edit(event, self.strings("delss_usage"))
            return
        path = self._find_skill_path(name)
        if not path.exists():
            await self.edit(event, self.strings("skill_not_found"))
            return
        path.unlink()
        try:
            if path.name == "SKILL.md" and not any(path.parent.iterdir()):
                path.parent.rmdir()
        except Exception:
            pass
        await self.edit(
            event,
            self.strings(
                "skill_deleted", name=html.escape(self._skill_name_from_path(path))
            ),
            as_html=True,
        )

    @command(
        "oaplugin",
        doc_ru="управление плагинами OpenAgent",
        doc_en="manage OpenAgent plugins",
    )
    async def cmd_oaplugin(self, event: Event) -> None:
        """Show plugin manager or install a plugin from replied .py file."""
        if await event.get_reply_message():
            try:
                saved_name = await self._install_plugin_from_reply(event)
            except Exception as exc:
                await self.edit(
                    event,
                    self.strings("plugin_install_failed", error=html.escape(str(exc))),
                    as_html=True,
                )
                return
            await self.edit(
                event,
                self.strings("plugin_installed", name=html.escape(saved_name)),
                as_html=True,
            )
            return

        installed = self._plugins
        text = self.strings("plugins_enabled_title")
        if not installed:
            text += self.strings("plugins_none_installed")
        else:
            for pname, plugin in installed.items():
                desc = getattr(plugin, "description", "?") or "?"
                author = getattr(plugin, "author", "?") or "?"
                text += f"<blockquote>{pname} - {desc} | by {author}</blockquote>\n"
        text += self.strings("plugins_total", count=len(installed))

        buttons = [
            [
                self.Button.inline(
                    self.strings("plugin_catalog_btn"),
                    self._oaplugin_catalog,
                    args=(0,),
                    style="primary",
                ),
                self.Button.inline(
                    self.strings("plugin_manager_btn"),
                    self._oaplugin_manager,
                    args=(0,),
                    style="primary",
                ),
            ],
            [
                self.Button.inline(
                    self.strings("close_btn"), self._oaplugin_close, style="danger"
                ),
            ],
        ]

        chat_id = getattr(event, "chat_id", None)
        if chat_id:
            try:
                await self.inline(
                    chat_id,
                    text,
                    buttons=buttons,
                    ttl=900,
                    parse_mode="html",
                    reply_to=getattr(event, "reply_to", None),
                )
                await event.delete()
            except Exception:
                await self.edit(event, text, as_html=True)
        else:
            await self.edit(event, text, as_html=True)

    @callback(ttl=900)
    async def _oaplugin_close(self, call: InlineMessage) -> None:
        try:
            await call.delete()
        except Exception:
            await call.answer()

    @callback(ttl=900)
    async def _oaplugin_catalog(self, call: InlineMessage, page: int = 0) -> None:
        """Show available plugins from repo (xheta-style)."""
        plugins = self._plugins_cache
        if not plugins:
            plugins = await self._fetch_repo_plugins()
        if not plugins:
            await call.answer(self.strings("plugin_repo_empty"), alert=True)
            return
        if page < 0 or page >= len(plugins):
            await call.answer()
            return
        m = plugins[page]
        name = m.get("name", "?")
        author = m.get("author", "?")
        version = m.get("version", "?")
        desc = m.get("description", self.strings("plugin_no_description"))
        tools = m.get("tools", [])
        fname = m.get("file_name", "")
        plugin_key = self._safe_plugin_name(
            m.get("plugin_name") or fname.replace(".py", "") or name
        )
        installed = plugin_key in self._plugins

        text = f"📦 <b>{name}</b> v{version} by <code>{author}</code>\n\n"
        text += f"📝 {desc}\n"
        if tools:
            tools_str = ", ".join(f"<code>{t}</code>" for t in tools[:8])
            if len(tools) > 8:
                tools_str += self.strings("plugin_more_tools", count=len(tools) - 8)
            text += f"\n🔧 <b>{html.escape(self.strings('plugin_tools_label'))}:</b> {tools_str}"
        text += f"\n\n🔢 {page + 1}/{len(plugins)}"

        buttons = []
        raw_url = m.get("download_url", "")
        if installed:
            buttons.append(
                [
                    self.Button.inline(
                        self.strings("plugin_installed_btn"),
                        self._oaplugin_noop,
                        style="primary",
                    )
                ]
            )
        else:
            buttons.append(
                [
                    self.Button.inline(
                        self.strings("plugin_install_btn"),
                        self._oaplugin_install,
                        args=(fname.replace(".py", ""), page),
                        style="primary",
                    )
                ]
            )
        if raw_url:
            buttons[0].append(self.Button.url(self.strings("plugin_code_btn"), raw_url))

        nav = []
        if page > 0:
            nav.append(
                self.Button.inline(
                    "⬅️", self._oaplugin_catalog, args=(page - 1,), style="primary"
                )
            )
        nav.append(
            self.Button.inline(
                f"📋 {page + 1}/{len(plugins)}", self._oaplugin_noop, style="primary"
            )
        )
        if page < len(plugins) - 1:
            nav.append(
                self.Button.inline(
                    "➡️", self._oaplugin_catalog, args=(page + 1,), style="primary"
                )
            )
        if nav:
            buttons.append(nav)
        buttons.append(
            [
                self.Button.inline(
                    self.strings("back_btn"), self._oaplugin_main, style="primary"
                )
            ]
        )

        try:
            await call.edit(text, buttons=buttons, parse_mode="html")
        except Exception:
            pass

    @callback(ttl=900)
    async def _oaplugin_noop(self, call: InlineMessage) -> None:
        await call.answer()

    @callback(ttl=900)
    async def _oaplugin_main(self, call: InlineMessage) -> None:
        """Return to main plugin page."""
        installed = self._plugins
        text = self.strings("plugins_enabled_title")
        if not installed:
            text += self.strings("plugins_none_installed")
        else:
            for pname, plugin in installed.items():
                desc = getattr(plugin, "description", "?") or "?"
                author = getattr(plugin, "author", "?") or "?"
                text += f"<blockquote>{pname} - {desc} | by {author}</blockquote>\n"
        text += self.strings("plugins_total", count=len(installed))
        buttons = [
            [
                self.Button.inline(
                    self.strings("plugin_catalog_btn"),
                    self._oaplugin_catalog,
                    args=(0,),
                    style="primary",
                ),
                self.Button.inline(
                    self.strings("plugin_manager_btn"),
                    self._oaplugin_manager,
                    args=(0,),
                    style="primary",
                ),
            ],
            [
                self.Button.inline(
                    self.strings("close_btn"), self._oaplugin_close, style="danger"
                ),
            ],
        ]
        try:
            await call.edit(text, buttons=buttons, parse_mode="html")
        except Exception:
            pass

    @callback(ttl=900)
    async def _oaplugin_install(
        self, call: InlineMessage, name: str, page: int = 0
    ) -> None:
        """Download and install a plugin from repo."""
        await call.answer(self.strings("plugin_installing"), alert=False)
        try:
            saved_name = await self._install_plugin_from_repo(name)
            await call.answer(
                self.strings("plugin_installed_alert", name=saved_name), alert=True
            )
        except Exception as exc:
            await call.answer(self.strings("generic_error", error=str(exc)), alert=True)
            return
        plugins = self._plugins_cache
        if plugins and page < len(plugins):
            await self._oaplugin_catalog(call, page)
        else:
            await self._oaplugin_catalog(call, 0)

    @callback(ttl=900)
    async def _oaplugin_manager(self, call: InlineMessage, page: int = 0) -> None:
        """Show installed plugins with delete option."""
        installed = list(self._plugins.values())
        if not installed:
            await call.answer(self.strings("plugin_manager_no_installed"), alert=True)
            return
        if page < 0 or page >= len(installed):
            await call.answer()
            return
        plugin = installed[page]
        text = f"<b>⚙️ {plugin.name}</b>\n"
        text += f"{html.escape(self.strings('plugin_version_label'))}: {getattr(plugin, 'version', '?')}\n"
        text += f"Tools: {len(getattr(plugin, 'tool_registry', ()))}\n\n"
        text += self.strings("plugin_actions_title")
        row1 = [
            self.Button.inline(
                self.strings("plugin_delete_btn"),
                self._oaplugin_uninstall,
                args=(plugin.name, page),
                style="danger",
            )
        ]
        buttons = [row1]
        if len(installed) > 1:
            nav = []
            if page > 0:
                nav.append(
                    self.Button.inline(
                        "⬅️", self._oaplugin_manager, args=(page - 1,), style="primary"
                    )
                )
            nav.append(
                self.Button.inline(
                    f"{page + 1}/{len(installed)}", self._oaplugin_noop, style="primary"
                )
            )
            if page < len(installed) - 1:
                nav.append(
                    self.Button.inline(
                        "➡️", self._oaplugin_manager, args=(page + 1,), style="primary"
                    )
                )
            buttons.append(nav)
        buttons.append(
            [
                self.Button.inline(
                    self.strings("back_btn"), self._oaplugin_main, style="primary"
                )
            ]
        )
        try:
            await call.edit(text, buttons=buttons, parse_mode="html")
        except Exception:
            pass

    @callback(ttl=900)
    async def _oaplugin_uninstall(
        self, call: InlineMessage, name: str, page: int = 0
    ) -> None:
        """Delete a plugin."""
        try:
            name = self._safe_plugin_name(name)
            fpath = self._plugin_files.get(name)
            is_builtin = bool(fpath and self._is_builtin_plugin_file(fpath))
            if is_builtin:
                self._disabled_plugins.add(name)
                self._save_disabled_plugins()
            self._unregister_plugin(name)
            plugins_dir = self._resolve_plugins_dir()
            if fpath and fpath.exists() and not is_builtin:
                try:
                    fpath.resolve().relative_to(plugins_dir.resolve())
                    fpath.unlink()
                except ValueError:
                    pass
            if not is_builtin:
                for extra in (
                    plugins_dir / f"{name}.py",
                    plugins_dir / f"{name}_plugin.py",
                ):
                    if extra.exists():
                        extra.unlink()
            await call.answer(
                self.strings("plugin_deleted_alert", name=name), alert=True
            )
        except Exception as exc:
            await call.answer(self.strings("generic_error", error=str(exc)), alert=True)
            return
        await self._oaplugin_manager(
            call, min(page, len(self._plugins) - 1) if self._plugins else 0
        )
