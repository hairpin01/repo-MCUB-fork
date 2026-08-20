# name: OpenAgent
# version: 0.8.1-main.build:1050
# requires: aiohttp
# scop: inline
# CubKit build info:
# CubKit source sha256: f818e3101cd78eec12331876a3cc1dd77a2d8d797970a0c1b6f856c5a82b1632
# CubKit payload sha256: bd0ad2578157f8d41477eedb471cedda6e289732c3d157f1f45acae0f64a2aaa
# CubKit signature: 85d974980d604e73bbcb32614c39a83311e0d75dd6d7b900af27b4e1df5100ef
# CubKit signature algorithm: sha256(cubkit-sign-v1 + module id + source sha256 + payload sha256)
# CubKit source map:
# - generated line 1971 -> OpenAgentMain.py:1
# - bundled files are extracted from the CubKit payload at import time:
#   - MCUBEvent.py -> MCUBEvent.py:1 (lines: 68, sha256: 373d1dcbb565c2675a6ba5cd7d91ccef359f143c44f1b1e518e45b0eab1448a7)
#   - OpenAgentLib/AgentRuntime.py -> AgentRuntime.py:1 (lines: 237, sha256: ae62ab0280dc595b0e5c2e8e83aedbb46cb704f6edc6a0cefd8f93c22bf8d9f9)
#   - OpenAgentLib/ContextService.py -> ContextService.py:1 (lines: 622, sha256: d304db23ed90c638376f92af62713c7cb8e7b547a0b07af0098a0bb9267f0df9)
#   - OpenAgentLib/HttpClient.py -> HttpClient.py:1 (lines: 66, sha256: c230c52a123893db543e7ec3620328214a28343cd3dcbe826352f32b769a3686)
#   - OpenAgentLib/Lifecycle.py -> Lifecycle.py:1 (lines: 157, sha256: 158cca5d1ff9e46d2ff007d54375e159c47d0b66dec522e0359dc7dacbb9b7d7)
#   - OpenAgentLib/Manager/OASession.py -> OASession.py:1 (lines: 51, sha256: 9653d80b9d11fa73bcf98ea98881e9aee91acda1a4a58ff01c0f9b19f9c3b974)
#   - OpenAgentLib/Manager/Session.py -> Session.py:1 (lines: 971, sha256: 23787d599657409ac5fba9308bbf4c6d4964de43ae1ae447becc85ed3e6e97e3)
#   - OpenAgentLib/Manager/__init__.py -> __init__.py:1 (lines: 7, sha256: aed21d92f18345e69613291b80d87635ced1e2b8b20b7983b1c9b896fd1a5c09)
#   - OpenAgentLib/OpenAgentMixins.py -> OpenAgentMixins.py:1 (lines: 80, sha256: 6a2362dfc3f62e7f10537473f78143c3c0981af93993539eef944a1789102a42)
#   - OpenAgentLib/Placeholders.py -> Placeholders.py:1 (lines: 381, sha256: 34bdfe48356b0ed382a524d6bfe31f2f0d78ccc52d2f8ed91f2ea0b370784d8b)
#   - OpenAgentLib/Plugin/PluginBase.py -> PluginBase.py:1 (lines: 372, sha256: 563cb62e86a733987d7dde758f956fc4aeebbc2124198b0f2dfa37cf0c99a8a7)
#   - OpenAgentLib/Plugin/PluginsEngine.py -> PluginsEngine.py:1 (lines: 3515, sha256: 3563e0a1e4e1b2192487c884c60312f043e2bc154b42685729ff4f25e897eb3b)
#   - OpenAgentLib/ResponseAgent.py -> ResponseAgent.py:1 (lines: 862, sha256: 7850cbb509db87c745ccdbb9928ba9b86772ebc49fdfdbde6642e078ba017b80)
#   - OpenAgentLib/SystemPlugins/Code/attach_result.py -> attach_result.py:1 (lines: 23, sha256: c7b213e2a5ecf5f39369b668f857e46f92d6408015d5ad04425a8c6ce2f76c98)
#   - OpenAgentLib/SystemPlugins/Code/choose_filename.py -> choose_filename.py:1 (lines: 27, sha256: 1d0fd72db20c6607a11085c5f139ecf8648cea366718b8571dd332aca563ad1f)
#   - OpenAgentLib/SystemPlugins/Code/generate_file.py -> generate_file.py:1 (lines: 27, sha256: c06a77d0632df5e2e1963c90563ffebe0c1611648b254ef13283c67255c28318)
#   - OpenAgentLib/SystemPlugins/Code/generate_mcub_module.py -> generate_mcub_module.py:1 (lines: 27, sha256: 34e26981e8eab742bdf2b4df47859cbfbf62904093ee65d5682c3e754192d5b5)
#   - OpenAgentLib/SystemPlugins/Code/read_docs.py -> read_docs.py:1 (lines: 22, sha256: 12b2395393173e2118b782d577723f9f86834204e800abdad4b83730ece0e52a)
#   - OpenAgentLib/SystemPlugins/Context/clear.py -> clear.py:1 (lines: 21, sha256: 8181670618be67bd4d8c40ec86aa35b2d3ffcdf783dd1a91b95c214850e728c7)
#   - OpenAgentLib/SystemPlugins/Context/discard.py -> discard.py:1 (lines: 25, sha256: e1b4e9c4e1c87e0f1ce4b6f90427c783be03653c4f72cc9855256953a20a5b53)
#   - OpenAgentLib/SystemPlugins/Context/media_context.py -> media_context.py:1 (lines: 22, sha256: 02a0ea5898bd55fe7ed276e39cadca1c244f7cca30a4560fe0133311a40f3333)
#   - OpenAgentLib/SystemPlugins/Context/prune.py -> prune.py:1 (lines: 25, sha256: c1e4559a3ae892933677ffd311f23ace83596ce7c36aedfe8421d15ae5e38eb8)
#   - OpenAgentLib/SystemPlugins/Context/regenerate.py -> regenerate.py:1 (lines: 21, sha256: 66c84a43cbe56625735f4e24a2526ec7203371967710857b3d250c4a534e38c5)
#   - OpenAgentLib/SystemPlugins/Context/remember.py -> remember.py:1 (lines: 21, sha256: ac0ae79029328c3facb8dc571e744797afc195620733f3cd1f6c0613c47c861d)
#   - OpenAgentLib/SystemPlugins/Context/reply_context.py -> reply_context.py:1 (lines: 22, sha256: e0c0bd6c75f6546fae8eeee5661f95935592ea7b51cb9e01317dcdbf5d5846fa)
#   - OpenAgentLib/SystemPlugins/Context/tool_output.py -> tool_output.py:1 (lines: 26, sha256: 3dc2d236bc487a51cc228590758fbcc16f0df42e4a2427c98428671a1faac5f7)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/activate.py -> activate.py:1 (lines: 25, sha256: a4c3e863b5741f08e1a2f557f76ad7ae6f96cac562746905e79b0418810e471d)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/export_md.py -> export_md.py:1 (lines: 25, sha256: 6451ec715abe582854f2109e0fec8d2c182135f4c0f3e2f6899b9b919c3f5944)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/import_md.py -> import_md.py:1 (lines: 25, sha256: 9cd3a975968f97cc87c9f51c8fc4f8598685fc750cb873a106fba31b6ff3a495)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/install.py -> install.py:1 (lines: 25, sha256: 1cd800d3f3e96d57d41ff5f0c4727431496b97ff165ec2e9d53f99aeec9d331c)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/list.py -> list.py:1 (lines: 22, sha256: 271b3712c1bbae2766d76f67c60ffbe5318878861f705c81d8dd3cebb2622b49)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/read.py -> read.py:1 (lines: 26, sha256: 4aaab7664cddbc2b2dfdd543e7ef8c07f406dd55144260746e411bad943bd452)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/repo_list.py -> repo_list.py:1 (lines: 22, sha256: e13ccb1d0a85e237a859d0eb959e790348ca213aae59ad47a0eea638a520abea)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/save.py -> save.py:1 (lines: 26, sha256: 6b4d31415f1c057638dd83d1eb0096aedc9d064b2c4099e4bc8f9c3bb5ad96f6)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/save_from_ai.py -> save_from_ai.py:1 (lines: 25, sha256: 8c0ab518ae0e4d7bfa6a68ffa8d161fd732e6330f02ade1914efbd9ca6dc3c25)
#   - OpenAgentLib/SystemPlugins/Thinking/note.py -> note.py:1 (lines: 25, sha256: 048a12265342159472cb928aa0c6b616ef0fc0bc5116b3e0e7415b6beaa7f654)
#   - OpenAgentLib/SystemPlugins/Todo/add.py -> add.py:1 (lines: 21, sha256: 4864d8ee637ece86631f52deb0928e61c8ce268ff7a75047871e4cb8250e304f)
#   - OpenAgentLib/SystemPlugins/Todo/clear.py -> clear.py:1 (lines: 21, sha256: 85c2048926c8a38c8b4559de6c3e1f7d6548b8b8e96ba4a1c8c083c3b8fc0539)
#   - OpenAgentLib/SystemPlugins/Todo/close.py -> close.py:1 (lines: 21, sha256: c757136f3762ff8d5f68a581f010e0547f1c1cd5d6d83539f4262b135ff72b00)
#   - OpenAgentLib/SystemPlugins/Todo/closeall.py -> closeall.py:1 (lines: 21, sha256: c8f405e1dd598362a8053febe8ecdbc538004fc6476cf8b3334254fa33224293)
#   - OpenAgentLib/SystemPlugins/Todo/current.py -> current.py:1 (lines: 21, sha256: 25baecdd26aa92b45401401948273f3d965ec8c823828719676ea1280a7a07e1)
#   - OpenAgentLib/SystemPlugins/Todo/delete.py -> delete.py:1 (lines: 21, sha256: 8ed0a42f3213b328ee9ad23b9068c4d5edc71d1c119c6086a1fbc8b70148505a)
#   - OpenAgentLib/SystemPlugins/Todo/edit.py -> edit.py:1 (lines: 21, sha256: 9ff3664951fce5ced7df06beb78b4954cde94409b59a29ddd9cf2deb20f2872c)
#   - OpenAgentLib/SystemPlugins/Utility/agent_log.py -> agent_log.py:1 (lines: 22, sha256: 1baeb93dee1642ecbc6323b9a0adabd2377de71d873c01b4d23013bb90c76ed9)
#   - OpenAgentLib/SystemPlugins/Utility/error_file.py -> error_file.py:1 (lines: 21, sha256: b416487786cd1eefce2867152f5abf603ff9c5118947c4a60abb41daa9292194)
#   - OpenAgentLib/SystemPlugins/Utility/list_tools.py -> list_tools.py:1 (lines: 24, sha256: 0cb467f94182e120f92b1aaae38b671e12bb51911a19d638c39e0c45aba39b53)
#   - OpenAgentLib/SystemPlugins/Utility/placeholders.py -> placeholders.py:1 (lines: 22, sha256: 19b1f60beac121d7a45d93ef2c703a5398e49ea600a965744b60a11d5e965511)
#   - OpenAgentLib/SystemPlugins/Utility/plugin_docs.py -> plugin_docs.py:1 (lines: 26, sha256: 961e48d90b2754dc2db3a5358f22f447d7b08e07c97a395aef9d0d0e23f4d829)
#   - OpenAgentLib/SystemPlugins/Utility/random_template.py -> random_template.py:1 (lines: 22, sha256: f10893e9397bf1a9bca6ae56a60a6c04b63de1fa5f35997f340d7c74d14900b0)
#   - OpenAgentLib/SystemPlugins/Utility/token_usage.py -> token_usage.py:1 (lines: 22, sha256: b3ba2ca57c2c8f493e60e7c14220fbea20660b111fc10c5b1624c2750b2cd807)
#   - OpenAgentLib/SystemPlugins/Utility/tool_help.py -> tool_help.py:1 (lines: 26, sha256: c11a7a63fa410a6c5a964e77ba7bdb9ef130b849df3f0cca925b35200e76034a)
#   - OpenAgentLib/SystemPlugins/__init__.py -> __init__.py:1 (lines: 16, sha256: 0f7ca2a08fa17665665895689ac20340888a048a537735b0096f9bc7df85636b)
#   - OpenAgentLib/SystemPlugins/base.py -> base.py:1 (lines: 280, sha256: 0653cbcc7f61a51c05bea1996858f576198bd96e9c1df408a3dae17936aac0c9)
#   - OpenAgentLib/TodoService.py -> TodoService.py:1 (lines: 214, sha256: bb335eb0c56249f08ec1560df10b0c3fbe12d9f660affb2caafa52eea9ab8321)
#   - OpenAgentLib/ToolDispatch.py -> ToolDispatch.py:1 (lines: 1269, sha256: 6bd259a0f154ad83fd831bdb21b69257e8cd471587a55cd83d59e5d23ff419c5)
#   - OpenAgentLib/__init__.py -> __init__.py:1 (lines: 14, sha256: 21fca903f07c84058eb38ea9e71b3c2484a99b1b7166d7caf035623588fe2865)
#   - locales/en.yaml -> en.yaml:1 (lines: 122, sha256: c4e8369176d907c3715fcb0d44b35dbf4eef3e6a2df9ed4e375976b5d6ad782a)
#   - locales/ru.yaml -> ru.yaml:1 (lines: 122, sha256: 113c37c8b389bc89e3e8fdf7ff3daf481089fcdac1e019a8f0ee95f1c3d69304)
#   - locales/uk.yaml -> uk.yaml:1 (lines: 122, sha256: 3f3cfc7b51e23d4b55ad24eeb8bdda0c20eed4a9a08484ad8cb940454cdc04db)

from __future__ import annotations
# Generated by CubKit. Do not edit this header by hand.
# CubKit repository: https://github.com/hairpin01/CubKit
# CubKit build notes:
# - Metadata comments above were generated/normalized from cubkit.toml and entrypoint code.
# - Bundled helper files are stored below as a base85-encoded zip payload.
# - On import, CubKit verifies the payload SHA256 and extracts it into CUBKIT_CACHE_DIR or ~/.cache/cubkit.
# - CubKit import-debug comments below explain sys.path/package wiring for private relative imports.
# - Vendored libraries declared in [libs] are exposed as `cubkit.lib.<name>`.
# - `load_strings()` returns project locales in MCUB's native class-level format.
# - Plugin resources and metadata are exposed through `from cubkit import ...`.
__cubkit_module_id__ = 'openagent'
__cubkit_package_dirs__ = ('OpenAgentLib',)
__cubkit_lib_dir__ = '_cubkit_lib'
__cubkit_assets_dir__ = None
__cubkit_locales__ = {'en': {'need_text': 'Usage: .oa <request>', 'no_key': 'API key is not configured. Use .cfg OpenAgent api_key', 'bad_provider': 'Unknown provider. Available: {providers}', 'error': 'OpenAgent error: {error}', 'thinking_empty_text': 'The model has not thought yet.', 'thinking_template_default': '<blockquote><a href="tg://emoji?id=6010292571627069263">😎</a> <u>{provider}/{model}</u> • <em>prepares the response...</em></blockquote >\n<blockquote><a href="tg://emoji?id=5404857686477015710">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>', 'request_label_default': '<a href="tg://emoji?id=6010352868672936598"><strong>🐈\u200d⬛</strong></a><strong></strong><strong> Prompt:</strong>', 'response_label_default': '<a href="tg://emoji?id=6010286885090368072"><strong>❌</strong></a><strong></strong><strong> Answer:</strong>', 'agent_log_label': 'Agent Log', 'status_thinking': 'Thinking', 'status_terminal': 'Running command', 'status_web': 'Working with web', 'status_file': 'Working with file', 'status_mcub': 'Running MCUB command', 'status_message': 'Working with messages', 'status_chat': 'Checking chat', 'status_dialog': 'Checking dialogs', 'status_code': 'Preparing code', 'status_todo': 'Updating TODO', 'status_default': 'Running {tool}', 'tool_confirmation_approved': 'Running', 'tool_confirmation_yes_text': 'Run', 'tool_confirmation_no_text': 'Not now', 'tool_validation_retry_prompt': 'This is the validation result for your tool_call. Fix the tool call and try again now. Use only valid OpenAgent tool names, valid JSON, and args as a JSON object. If no tool is needed, answer the user in plain text with no JSON/tool_call.', 'runtime_comment_button': '💬 Comment', 'runtime_comment_placeholder': 'Comment for agent...', 'runtime_comment_saved': 'Comment added', 'runtime_comment_note': 'The user added a live comment while you were working. Use it in the next steps:\n{comments}', 'follow_up_button': '✍️ Continue', 'follow_up_placeholder': 'Enter request...', 'regen_prompt_button': '🔁 Regen with prompt', 'regen_prompt_placeholder': 'New prompt for regeneration...', 'regen_stale': 'Request expired', 'regenerating': 'Regenerating...', 'new_session_name': 'New chat', 'chat_history_button': '💬 Chat history', 'chats_title': '💬 <b>Chats — this chat</b>', 'chat_empty': 'No messages yet', 'chat_today': 'today', 'chat_yesterday': 'yesterday', 'chat_days_ago': '{days} days ago', 'new_chat_button': '+ New chat', 'ask_this_chat_button': '✍️ Ask in this chat', 'ask_this_chat_placeholder': 'Request for this chat...', 'return_to_chat_button': '↩️ Return to this chat', 'saved_response_missing': 'This chat history has no AI answer yet', 'rename_chat_button': '✏️ Rename', 'delete_chat_button': '🗑 Delete', 'remember_chat_button': '💾 Remember choice', 'chat_choice_saved': 'Choice remembered', 'chat_switched': 'Active chat: {name}', 'chat_created': 'Created chat: {name}', 'chat_renamed': 'Chat renamed: {name}', 'chat_deleted': 'Chat deleted', 'chat_delete_last': 'Cannot delete the last chat', 'new_chat_placeholder': 'Name (or Enter for auto...)', 'rename_chat_placeholder': 'New name...', 'auto_name_prompt': 'Create a short 3-4 word session title. Reply with the title only. Request: {prompt}', 'oa_choose_chat': 'Choose a chat to continue or create a new one.', 'tools_no_final': 'Tools ran, but the model did not provide final text.', 'tool_call_bad_json': 'Tool call error: model returned invalid JSON ({error}).\nFragment: {preview}', 'tool_call_not_object': 'Tool call error: tool call item must be a JSON object.', 'tool_call_unknown': "Tool call error: unknown tool '{tool_name}'.{hint} Available examples: {available}.", 'tool_call_nearest': ' Nearest: {nearest}.', 'tool_call_args_not_object': "Tool call error: args for '{tool_name}' must be a JSON object.", 'answer_file_request': 'Request', 'answer_file_answer': 'Answer', 'answer_file_too_long': '<b>Answer is too long, sending it as a file.</b>', 'answer_file_attach_failed': '<b>Failed to attach the file to the form, showing the beginning:</b>', 'continued': 'continued', 'cancelled': 'Cancelled', 'context_cleared': 'Context cleared', 'clear_button': '🧹 Clear', 'regenerate_button': '🔃 Regenerate', 'cancel_button': 'Cancel', 'reply_analyze_prompt': 'Analyze the replied attachment/message.', 'skills_empty': 'No OpenAgent skills installed', 'skillinstall_usage': 'Usage: .skillinstall <skill_name>', 'sendss_usage': 'Usage: .sendss <skill_name>', 'skill_not_found': 'Skill not found', 'skill_name_required': 'skill name is required', 'skill_not_found_repo': 'Skill not found in repo: {query}', 'skill_saved': 'Skill saved: {name}', 'unknown_skills_tool': 'Unknown skills tool: {tool}', 'imss_need_reply': 'Reply to a .md file or markdown message', 'skill_empty': 'Skill content is empty', 'delss_usage': 'Usage: .delss <skill_name>', 'skill_installed': 'Skill installed: <code>{name}</code>', 'skill_imported': 'Skill imported: <code>{name}</code>', 'skill_deleted': 'Skill deleted: <code>{name}</code>', 'plugin_install_failed': 'Plugin install failed: <code>{error}</code>', 'plugin_installed': 'Plugin installed: <code>{name}</code>', 'plugins_enabled_title': '<b>🧩 Enabled plugins:</b>\n', 'plugins_none_installed': '\nNo installed plugins\n', 'plugins_total': '\n<b>Total plugins:</b> {count}', 'plugin_catalog_btn': '📦 Catalog', 'plugin_manager_btn': '⚙️ Manager', 'close_btn': '❌ Close', 'plugin_repo_empty': '❌ No plugins in repository', 'plugin_no_description': 'No description', 'plugin_more_tools': ' ...and {count} more', 'plugin_tools_label': 'Tools', 'plugin_installed_btn': '✅ Installed', 'plugin_install_btn': '📥 Install', 'plugin_code_btn': '📄 Code', 'back_btn': '🔙 Back', 'plugin_installing': '⏳ Installing...', 'plugin_installed_alert': '✅ {name} installed!', 'generic_error': '❌ Error: {error}', 'plugin_manager_no_installed': 'No installed plugins', 'plugin_version_label': 'Version', 'plugin_id_label': 'ID', 'plugin_author_label': 'Author', 'plugin_permissions_label': 'Permissions', 'plugin_requirements_label': 'Requirements', 'plugin_actions_title': '<b>Actions:</b>', 'plugin_delete_btn': '🗑 Delete', 'plugin_deleted_alert': '🗑 {name} deleted', 'oa_chat_choice_title': '💬 <b>Where to send the request?</b>', 'remember_pref_continue': '💾 Always here', 'remember_pref_new': '💾 Always new', 'pref_saved': 'Remembered'}, 'ru': {'need_text': 'Usage: .oa <request>', 'no_key': 'API key is not configured. Use .cfg OpenAgent api_key', 'bad_provider': 'Unknown provider. Available: {providers}', 'error': 'OpenAgent error: {error}', 'thinking_empty_text': 'Модель ещё не думала.', 'thinking_template_default': '<blockquote><a href="tg://emoji?id=6010292571627069263">😎</a> <u>{provider}/{model}</u> • <em>prepares the response...</em></blockquote >\n<blockquote><a href="tg://emoji?id=5404857686477015710">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>', 'request_label_default': '<a href="tg://emoji?id=6010352868672936598"><strong>🐈\u200d⬛</strong></a><strong></strong><strong> Prompt:</strong>', 'response_label_default': '<a href="tg://emoji?id=6010286885090368072"><strong>❌</strong></a><strong></strong><strong> Answer:</strong>', 'agent_log_label': 'Agent Log', 'status_thinking': 'Думаю', 'status_terminal': 'Выполняю команду', 'status_web': 'Работаю с web', 'status_file': 'Работаю с файлом', 'status_mcub': 'Выполняю MCUB-команду', 'status_message': 'Работаю с сообщениями', 'status_chat': 'Проверяю чат', 'status_dialog': 'Проверяю диалоги', 'status_code': 'Готовлю код', 'status_todo': 'Обновляю TODO', 'status_default': 'Выполняю {tool}', 'tool_confirmation_approved': 'Выполняю', 'tool_confirmation_yes_text': 'Выполнить', 'tool_confirmation_no_text': 'Не сейчас', 'tool_validation_retry_prompt': 'Это результат валидации твоего tool_call. Исправь tool_call и повтори прямо сейчас. Fix the tool call and try again now. Use only valid OpenAgent tool names, valid JSON, and args as a JSON object. If no tool is needed, answer the user in plain text with no JSON/tool_call.', 'runtime_comment_button': '💬 Комментировать', 'runtime_comment_placeholder': 'Комментарий агенту...', 'runtime_comment_saved': 'Комментарий добавлен', 'runtime_comment_note': 'Пользователь добавил комментарий во время выполнения. Учти это в следующих шагах:\n{comments}', 'follow_up_button': '✍️ Продолжить', 'follow_up_placeholder': 'Введи запрос...', 'regen_prompt_button': '🔁 Реген с промптом', 'regen_prompt_placeholder': 'Новый промпт для регенерации...', 'regen_stale': 'Запрос устарел', 'regenerating': 'Регенерирую...', 'new_session_name': 'Новый чат', 'chat_history_button': '💬 История чатов', 'chats_title': '💬 <b>Чаты — этот чат</b>', 'chat_empty': 'Пока нет сообщений', 'chat_today': 'сегодня', 'chat_yesterday': 'вчера', 'chat_days_ago': '{days} дн назад', 'new_chat_button': '+ Новый чат', 'ask_this_chat_button': '✍️ Спросить в этом чате', 'ask_this_chat_placeholder': 'Запрос для этого чата...', 'return_to_chat_button': '↩️ Вернуться в этот чат', 'saved_response_missing': 'В истории этого чата ещё нет ответа ИИ', 'rename_chat_button': '✏️ Переименовать', 'delete_chat_button': '🗑 Удалить', 'remember_chat_button': '💾 Запомнить выбор', 'chat_choice_saved': 'Выбор запомнен', 'chat_switched': 'Чат активен: {name}', 'chat_created': 'Создан чат: {name}', 'chat_renamed': 'Чат переименован: {name}', 'chat_deleted': 'Чат удалён', 'chat_delete_last': 'Нельзя удалить последний чат', 'new_chat_placeholder': 'Название (или Enter для авто...)', 'rename_chat_placeholder': 'Новое название...', 'auto_name_prompt': 'Придумай короткое название сессии на 3-4 слова. Ответь только названием. Запрос: {prompt}', 'oa_choose_chat': 'Выбери чат для продолжения или создай новый.', 'tools_no_final': 'Инструменты выполнены, но модель не сформировала финальный текст.', 'tool_call_bad_json': 'Ошибка tool call: модель вернула некорректный JSON ({error}).\nФрагмент: {preview}', 'tool_call_not_object': 'Ошибка tool call: элемент вызова инструмента должен быть JSON-объектом.', 'tool_call_unknown': "Ошибка tool call: неизвестный инструмент '{tool_name}'.{hint} Доступные примеры: {available}.", 'tool_call_nearest': ' Ближайшие: {nearest}.', 'tool_call_args_not_object': "Ошибка tool call: args для '{tool_name}' должен быть JSON-объектом.", 'answer_file_request': 'Запрос', 'answer_file_answer': 'Ответ', 'answer_file_too_long': '<b>Ответ слишком длинный, отправляю файлом.</b>', 'answer_file_attach_failed': '<b>Не удалось прикрепить файл к форме, показываю начало:</b>', 'continued': 'continued', 'cancelled': 'Отменено', 'context_cleared': 'Контекст очищен', 'clear_button': '🧹 Очистить', 'regenerate_button': '🔃 Регенерировать', 'cancel_button': 'Отмена', 'reply_analyze_prompt': 'Проанализируй вложение/сообщение из reply.', 'skills_empty': 'No OpenAgent skills installed', 'skillinstall_usage': 'Usage: .skillinstall <skill_name>', 'sendss_usage': 'Usage: .sendss <skill_name>', 'skill_not_found': 'Skill not found', 'skill_name_required': 'skill name is required', 'skill_not_found_repo': 'Skill not found in repo: {query}', 'skill_saved': 'Skill saved: {name}', 'unknown_skills_tool': 'Unknown skills tool: {tool}', 'imss_need_reply': 'Reply to a .md file or markdown message', 'skill_empty': 'Skill content is empty', 'delss_usage': 'Usage: .delss <skill_name>', 'skill_installed': 'Skill installed: <code>{name}</code>', 'skill_imported': 'Skill imported: <code>{name}</code>', 'skill_deleted': 'Skill deleted: <code>{name}</code>', 'plugin_install_failed': 'Plugin install failed: <code>{error}</code>', 'plugin_installed': 'Plugin installed: <code>{name}</code>', 'plugins_enabled_title': '<b>🧩 Включёные плагины:</b>\n', 'plugins_none_installed': '\nНет установленных плагинов\n', 'plugins_total': '\n<b>Всего плагинов:</b> {count}', 'plugin_catalog_btn': '📦 Каталог', 'plugin_manager_btn': '⚙️ Менеджер', 'close_btn': '❌ Закрыть', 'plugin_repo_empty': '❌ Нет плагинов в репозитории', 'plugin_no_description': 'Нет описания', 'plugin_more_tools': ' ...и ещё {count}', 'plugin_tools_label': 'Tools', 'plugin_installed_btn': '✅ Установлен', 'plugin_install_btn': '📥 Установить', 'plugin_code_btn': '📄 Код', 'back_btn': '🔙 Назад', 'plugin_installing': '⏳ Устанавливаю...', 'plugin_installed_alert': '✅ {name} установлен!', 'generic_error': '❌ Ошибка: {error}', 'plugin_manager_no_installed': 'Нет установленных плагинов', 'plugin_version_label': 'Версия', 'plugin_id_label': 'ID', 'plugin_author_label': 'Автор', 'plugin_permissions_label': 'Права', 'plugin_requirements_label': 'Зависимости', 'plugin_actions_title': '<b>Действия:</b>', 'plugin_delete_btn': '🗑 Удалить', 'plugin_deleted_alert': '🗑 {name} удалён', 'oa_chat_choice_title': '💬 <b>Куда отправить запрос?</b>', 'remember_pref_continue': '💾 Всегда сюда', 'remember_pref_new': '💾 Всегда новый', 'pref_saved': 'Запомнено'}, 'uk': {'need_text': 'Використання: .oa <request>', 'no_key': 'API-ключ не налаштовано. Використайте .cfg OpenAgent api_key', 'bad_provider': 'Невідомий провайдер. Доступні: {providers}', 'error': 'Помилка OpenAgent: {error}', 'thinking_empty_text': 'Модель ще не думала.', 'thinking_template_default': '<blockquote><a href="tg://emoji?id=6010292571627069263">😎</a> <u>{provider}/{model}</u> • <em>готує відповідь...</em></blockquote >\n<blockquote><a href="tg://emoji?id=5404857686477015710">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>', 'request_label_default': '<a href="tg://emoji?id=6010352868672936598"><strong>🐈\u200d⬛</strong></a><strong></strong><strong> Запит:</strong>', 'response_label_default': '<a href="tg://emoji?id=6010286885090368072"><strong>❌</strong></a><strong></strong><strong> Відповідь:</strong>', 'agent_log_label': 'Журнал агента', 'status_thinking': 'Думаю', 'status_terminal': 'Виконую команду', 'status_web': 'Працюю з інтернетом', 'status_file': 'Працюю з файлом', 'status_mcub': 'Виконую команду MCUB', 'status_message': 'Працюю з повідомленнями', 'status_chat': 'Перевіряю чат', 'status_dialog': 'Перевіряю діалоги', 'status_code': 'Готую код', 'status_todo': 'Оновлюю TODO', 'status_default': 'Виконую {tool}', 'tool_confirmation_approved': 'Виконую', 'tool_confirmation_yes_text': 'Виконати', 'tool_confirmation_no_text': 'Не зараз', 'tool_validation_retry_prompt': 'Це результат перевірки вашого tool_call. Виправте tool_call і повторіть спробу зараз. Використовуйте лише дійсні назви інструментів OpenAgent, дійсний JSON та args у вигляді JSON-об’єкта. Якщо інструмент не потрібен, дайте користувачеві відповідь звичайним текстом без JSON/tool_call.', 'runtime_comment_button': '💬 Коментувати', 'runtime_comment_placeholder': 'Коментар для агента...', 'runtime_comment_saved': 'Коментар додано', 'runtime_comment_note': 'Користувач додав коментар під час виконання. Врахуйте його в наступних кроках:\n{comments}', 'follow_up_button': '✍️ Продовжити', 'follow_up_placeholder': 'Введіть запит...', 'regen_prompt_button': '🔁 Перегенерувати із запитом', 'regen_prompt_placeholder': 'Новий запит для перегенерування...', 'regen_stale': 'Термін дії запиту минув', 'regenerating': 'Перегенеровую...', 'new_session_name': 'Новий чат', 'chat_history_button': '💬 Історія чатів', 'chats_title': '💬 <b>Чати — цей чат</b>', 'chat_empty': 'Повідомлень ще немає', 'chat_today': 'сьогодні', 'chat_yesterday': 'вчора', 'chat_days_ago': '{days} дн. тому', 'new_chat_button': '+ Новий чат', 'ask_this_chat_button': '✍️ Запитати в цьому чаті', 'ask_this_chat_placeholder': 'Запит для цього чату...', 'return_to_chat_button': '↩️ Повернутися до цього чату', 'saved_response_missing': 'В історії цього чату ще немає відповіді ШІ', 'rename_chat_button': '✏️ Перейменувати', 'delete_chat_button': '🗑 Видалити', 'remember_chat_button': '💾 Запам’ятати вибір', 'chat_choice_saved': 'Вибір запам’ятовано', 'chat_switched': 'Активний чат: {name}', 'chat_created': 'Створено чат: {name}', 'chat_renamed': 'Чат перейменовано: {name}', 'chat_deleted': 'Чат видалено', 'chat_delete_last': 'Не можна видалити останній чат', 'new_chat_placeholder': 'Назва (або Enter для автоматичної назви...)', 'rename_chat_placeholder': 'Нова назва...', 'auto_name_prompt': 'Створіть коротку назву сесії з 3–4 слів. Дайте у відповідь лише назву. Запит: {prompt}', 'oa_choose_chat': 'Виберіть чат для продовження або створіть новий.', 'tools_no_final': 'Інструменти виконано, але модель не надала остаточного тексту.', 'tool_call_bad_json': 'Помилка tool call: модель повернула некоректний JSON ({error}).\nФрагмент: {preview}', 'tool_call_not_object': 'Помилка tool call: елемент виклику інструмента має бути JSON-об’єктом.', 'tool_call_unknown': "Помилка tool call: невідомий інструмент '{tool_name}'.{hint} Доступні приклади: {available}.", 'tool_call_nearest': ' Найближчі: {nearest}.', 'tool_call_args_not_object': "Помилка tool call: args для '{tool_name}' має бути JSON-об’єктом.", 'answer_file_request': 'Запит', 'answer_file_answer': 'Відповідь', 'answer_file_too_long': '<b>Відповідь надто довга, надсилаю її файлом.</b>', 'answer_file_attach_failed': '<b>Не вдалося прикріпити файл до форми, показую початок:</b>', 'continued': 'продовження', 'cancelled': 'Скасовано', 'context_cleared': 'Контекст очищено', 'clear_button': '🧹 Очистити', 'regenerate_button': '🔃 Перегенерувати', 'cancel_button': 'Скасувати', 'reply_analyze_prompt': 'Проаналізуйте вкладення/повідомлення у відповіді.', 'skills_empty': 'Навички OpenAgent не встановлено', 'skillinstall_usage': 'Використання: .skillinstall <skill_name>', 'sendss_usage': 'Використання: .sendss <skill_name>', 'skill_not_found': 'Навичку не знайдено', 'skill_name_required': 'Потрібна назва навички', 'skill_not_found_repo': 'Навичку не знайдено в репозиторії: {query}', 'skill_saved': 'Навичку збережено: {name}', 'unknown_skills_tool': 'Невідомий інструмент навичок: {tool}', 'imss_need_reply': 'Дайте відповідь на файл .md або повідомлення у форматі Markdown', 'skill_empty': 'Вміст навички порожній', 'delss_usage': 'Використання: .delss <skill_name>', 'skill_installed': 'Навичку встановлено: <code>{name}</code>', 'skill_imported': 'Навичку імпортовано: <code>{name}</code>', 'skill_deleted': 'Навичку видалено: <code>{name}</code>', 'plugin_install_failed': 'Не вдалося встановити плагін: <code>{error}</code>', 'plugin_installed': 'Плагін встановлено: <code>{name}</code>', 'plugins_enabled_title': '<b>🧩 Увімкнені плагіни:</b>\n', 'plugins_none_installed': '\nНемає встановлених плагінів\n', 'plugins_total': '\n<b>Усього плагінів:</b> {count}', 'plugin_catalog_btn': '📦 Каталог', 'plugin_manager_btn': '⚙️ Менеджер', 'close_btn': '❌ Закрити', 'plugin_repo_empty': '❌ У репозиторії немає плагінів', 'plugin_no_description': 'Немає опису', 'plugin_more_tools': ' ...і ще {count}', 'plugin_tools_label': 'Інструменти', 'plugin_installed_btn': '✅ Встановлено', 'plugin_install_btn': '📥 Встановити', 'plugin_code_btn': '📄 Код', 'back_btn': '🔙 Назад', 'plugin_installing': '⏳ Встановлюю...', 'plugin_installed_alert': '✅ {name} встановлено!', 'generic_error': '❌ Помилка: {error}', 'plugin_manager_no_installed': 'Немає встановлених плагінів', 'plugin_version_label': 'Версія', 'plugin_id_label': 'ID', 'plugin_author_label': 'Автор', 'plugin_permissions_label': 'Дозволи', 'plugin_requirements_label': 'Залежності', 'plugin_actions_title': '<b>Дії:</b>', 'plugin_delete_btn': '🗑 Видалити', 'plugin_deleted_alert': '🗑 {name} видалено', 'oa_chat_choice_title': '💬 <b>Куди надіслати запит?</b>', 'remember_pref_continue': '💾 Завжди сюди', 'remember_pref_new': '💾 Завжди в новий чат', 'pref_saved': 'Запам’ятовано'}}
__cubkit_metadata__ = {'id': 'openagent', 'name': 'OpenAgent', 'version': '0.8.1-main.build:1050', 'author': 'unknown', 'description': '', 'requires': ('aiohttp',), 'banner_url': None, 'scop': 'inline'}
__cubkit_bundle_sha256__ = 'bd0ad2578157f8d41477eedb471cedda6e289732c3d157f1f45acae0f64a2aaa'
__cubkit_bundle_b85__ = """
P)h>@6aWAK2mk;8Aplt)5*kAS002)2000aC002!xRYFB}Wo~pXaCy~M(Q4Z;6n*zs2=~PfiRp7-
W9`yGU@3!jFld7i_I0XNk%Xiy&EM}za-
7JaS!ti@mqfbfo^!B{ZgN3>{+RuqeCIVt3zK;R((#sqnUcl)E^Cci6H42S+Zdpf@U>RP5hkT_%yA`c7BOz8xm@k*S8|u_p>`*0uC
gqv1+$jW#n)fgH-AxPnh|^&Xi<Pm?kFuRh;~fW#(8}t8565ErUnY3A#OQ%#;?|yl1x66TO}bf`NtDfG!T$ak!VmmCPc{bGDUhB1o
)4%VAz(vSX_g(Yz3YfmuamQJc<Ti-EshVWRCKt$3$ba+b)jXmT9L2*?@_?E5O5XridI*U?hk!$**RM`7NE#@^N@;B~hk__GE$ZNC
x|Q>aMZJ4lE?v1CG#qIcPwC*l}kzknU@)p?R@_VbP&6@p335>)ARyW7cZb_(Qr(>rzqHG?bZ@rB3xi-
<Ys)nlUWeDG}VddradJf%nTSz(VLlw4vdyi*=vdF&TM<F3zLT)3#rRNDr?_VB9j^U#7|m09_1U=iXDrw8kSVP^$2v<pE~^FS3l;9
5^+g#qOh6wOaYEk6^X|0S-E^=MAQ_>_65z$q@2^B;G+9j+1udD5wVslsYKzmOL^Wuj|Qh#7ld^lb6$EP;?%m(^HD-)X1y-
`;qq!+rIrRZiDQrO~%Ri4x5qSEk--
(GgiN7qcj+|>wjlsjt_P*$kSne{vaP@Uj0#A7D@Wc3gKL%VwO?LguuT8IPvnst;(0#KTt~p1QY-
O00;m803iT(MM<!83jhF@9smFw0000_aAj^mXJu}5Ole{-L1$%dbW(M0bZKp6E^v9RS?g{bw-
x@sPr*+A%qY8K$*~J(8yR&RH5HQBhNPe^WMM$faCZsKWlM4_tt|tNTQn#N^fCIoNgTxW^%YjH&?o6Rhn(Ba%DJ=#yyB9Fhv)j8L+
&rx{=JX?F#1f!BG+QHn~2=Vi4<zgKHohUOjMDvD4LX}R3eI)%;tqMjOTe_xRFJ!2ZL%(FY;Ix)z^%hSv6L|GBS&~%%>HTTlr$hc8
yT{I2D6Ibg*~p&i?MsorCCi2M70}{exQvU+nMfvuy^OAEJ21e{^m0#*kgx`~W_#UdIm@UEkcqkE{6cK7L$#91Pt4Xm1A?C=td*Hk
YaJm3RLb`QO*?`S+7Y?>`RiAA3Wj*!|?r-MyXLxAu2}!C(-
lTx<4uk%;s*Pt%XeWGc*fz~G<fdAEx)N4<E;=Bjug6QLM4Mr3oN!8!>nX`vnn7V|lerCG2^q1Z&`Je3d0a3OFR5W7T7z{E0_CW?G
5(#epeGLvS^WNrdBy2<Voxv)p$KO_l>0yN9`nZGqeN}r~Jpi5V3kpS6dbCi>ePFllVPFfppZnsWrXz-unQVX^RW{{cKQL0e>#Je?
x@L?GmZ4`sm*fE)niL)6mwE>R)qlV$*z*{Hnd)sWwiu)U|?OZ6cXbGQjuv9*6#0S+I$&`RV&B-
bd6D>=PngfEy7N#iDNP#aC?RO*@*55Xop_$421kR2`jv<?j*)i;I*5e|d$SEXB5`nIBO%809$@@_iCA0{h*|G$ERrmugQ#^-
lcNIZjuZjZOt5E136ZA|YbKjW<8Li431jEXDwEzL;1DZ={a5gt0GUCicrZ|D5^dIoF6l2Wht_~32d-
g~Uww{X|pe0_6CQ67QnhK*3G68ag7}d-}>z-
Ttw|93jxwN<vLqLHzfD}`qS)9TgY=V?36^mzF@fc7<GYA#SE5w){5eMRh;xei0BN7NvB|1W+3#JQpd!b~S%9v8PFf(ANV<j=ElY#
-}5jzbyk{j4jfJl?HIEBa%4GsWXI`CBHNpTuh#uzlBfJ2S4hGPH=o=XErJvf3$dJ(-
z6I{nqMyRqzCS~St5wPG4Sl%f*0j7zMa{>F1ZC$-
#+2=(bbs2yfK5oJ2X{`)aGHGi_XdcEwrhc2l6?QFP@3j_JkGR6N!t4F;$%NME$|{7a@8h~0940b0hhU{42G-
G0FSK?XFI3%FuWO9xI4u*bF`VfP0SIDZ<k&+Q;Tf*Qg*FZR8mMF`K_n$9ShJ!BgVvHYAVB1RQP=uYYxBdg2muFuPZg<vY6Bh*e$I
9Zt=zOZI6n~+XJ?~i*0ynEQP?6}W9w9EvubAxM&NXJyn`?@|2q2GAD;>_XL<n`lGR607GY}S;uLhl#DIj+RQ@145W`wWH6DQgZl>
9X;2O*lOpU%focf1HHZ!dN+w4%{Uvwr7TAoDiIM?z=z_z!UXZL!R(Q%P1ema|9wAnO8MwNNo3j3zgAcHaMnzX4G)@!XILSE=nv-
5uWb~P95c4MVvTU+6VcFn?wa*)($v?kJQWT+E>IMDNc{+}oRJgjs}5RWV1vjQA>O@woW64l*`lW@eY!~gYBPv^7_j!UJioQ}uZZB
FWT6C@vsl{N`LucBicm26k46WWPcE4NK%C-
baXKCG>E1e9)kIL4!oLIrk}bKl}5Dpl`4ok1P30^Vd>lq{DbWMgQ6!kblSbiCWwlx8;AX81u%ssD%M73S3Tk?#Qaj_44SRZEyc5v
NcjwkKk4)<Y7eVLQ7WnpssVkZ`4w(v~>ab*m=XU{~3dEA0KC#(AjE;%r!_w#ds2s*i!zm<|fYtt`=a;N?0ZkE3?4<=WJ!Mx?Irqs
w`rC4zQ7)8RLJJiFdUI6`$0$~L=8tD)S(BNTqv;~(^x$VuDfnk?Q$pY}i0Bjj^z{QP=bm+3KFpiTzsHZ+-
5i`8}bk20WaT^Oj2^y&uE+5ogQ>W4zGT?&-IY9<mNqwaqQmNhQ!`PNlXIK89LjlSu-HvOr-
4^|KUkq)=={UmpHw{)SkQF63R#;GwP1hhx`+W3}Dw;8ftrCvzSiZV?iCH_<bSybJdeCXCQL>zLmn1ElaFB@=$g1i4L!fUL(;!)wn
LEY|rEMn;O0m21c60pfB=GfQR2Z1SEvh@heCG2IG(PbDccnast2>3hgPIDl-
*os3<Nimsty`cRq2ZXD(I%0^&M_wipS!P(XXL35jzh^Xf++%T|O0jw$u_kF>NE~s~urwEjo7?#8QZK+JoDXAs7xAGv@QCDEn*a^y
cLG9*Pz$c&ncoX2e5Uaeaa>N%m6*T<uTbZioB}+b%WR&C3<}lxJmvX02b(Vr^~0m{<@1X#mv1kgEdRCq<{bWfckve(zPNb0d~@;S
+*@<T^40SB@>|?-@mJab^e<uR`*Y&+2EM*-O~C*rg8Qc%-mu3F_3zJi-
j%w`O}N`pbxo3h6pH6sf{IaftBeFav52#H%s%2;?3~4d0<IsMdyR`(k*DtI3GVW6%hwR9a9`qZ`^^i5Hzc_C@(Eq1!P{!l2}`MEt
_{y)fd>zne;_kal!l&rhSiH-*qyyy<hh7ZG@1y4%YzSin-VXgP!hQ@%AVrcX$W7$nqZAEmVla^K6l3y65_HK#nr%vQv-MJG4Tv0o
43O%J}Ky%%L$P6&c%+4R>G+&%DKN41V1Q5TAT`Hff=)hzWSZq<N2aV4%dAHSGTcwTf%E=z1mGD4`1jK1|C|8T3T2$9oHVD$HI57P
w+{tM?nw7%n`1x()*)=mRdW4J_CHbDil`|;<L=_m#7w5H)kkzBS2cd@ZHmwy*MG9$9z5ph%Goe{6@G*DMQ~^b0!f+s0=C()b5yxv
pED{ZX|&EF^^9GjLFa((n^euIX+gp!<w{dJ+r~NL+HM*L+j~ZWg8py!<yX#Jq*MMY7iaVz57}8$==;B?nR&O{PFj9_ddpF??(e??
nHQF=Gy_}$9!RCMUJD1w9g4pIZ8WPz5vvEh9d&Me=lFs>?@qT_%nP9h80)3tU1PZOoc-
O)GlgPuK_*30}TE0;wjBN#}VS`@_EfF0Rt6N;^c-viSIJB;~9V_Lg<_2w<OkA0Jcx-
y`%x|tW=p4DZm|$5~)O73DeQ$EsWnTUsUV~xE;*bjI+2rCdM=XN{CZ+T#!r`|5$zx)#1tVYuM7r;(8*x%Z(9^px>ZfUxE&AmS11|
jShyLRk5i#=o6Wyni$X!2~YCkG!=>E1w3AWJzhFRu(*74@pn+A;$Y*Cr^KWFg7z%3j9WqUOjy?F8;}5t7?r8oYp<wqJ!`lYNnttS
0H_StCq(@{P(A~XeB}&F6|UZQDy$9hFIfV?5J!+&Lgm6Zoxn9NKHkFVSca{0p4<2V8DGOES^9CEv8i~#bG*72X_Rv?xP`5DXJ$Kd
Tx&fI!h(Axac}d@uO;}N{ww!fWy-lF9<neDo0qD6I5>t9$nX~-
Xe{VQ0DF1*HJg;srx7p#LM>b$s#|aI1%d=RqRIHqLp}6j(3I9F^$6<=DiDP3HeG={AqlP^V3UgU)5|LP<3R&<O||H?Yn{?T^+(qL
QcrcN1<eehRbD_(nz(w|hoKM~bM1F-D_E1<zE&+FuC3{cv)yX-fTXf`+Lg|$+VT)v<`&3%rID#Lix6*R6e)V$Duoav#eCi3JT0d(
kCGy;_F7pq#Q~Y~u(_0g?K@_wJXAZmZHQ{IrIy<g>Ny<ldm*I3R&cm^gk;t)#Neo1D=1R^N}j`U^>|@_&^w|E5kadKMYXKn$`6xH
Gw-rXXK%grYF4eiqwlOp)+BASR9E0?>XN%xwS37lH7p+u{tHk`0|XQR000O8001EXt)w)DITZi^cU1rY9smFUPjF>!L1$%dbWCYt
FGFu`bY*ySQ)O~?X=7zBaCzN4Ym?hHlHcc7pm-lF*_1q<TBj0i<T`Kc)Vj{jxIB}s-
IH}JjtI>#Ly=mNnn!f{@7LXUgP<fkN$u9D${q;>8vR0}yV2l(u#1mx{yuu2FL>GT(YuV7ZNAKTJz*c-
U7jrKYQ>UdxoI~wPZE}|)>YlIv@EMOZS$&ZPEKT7&DFOyUvV*Vowhecex-(egrDL;`?$`_Yt{a`d^{2Di>l^h7%_$pyiw2J-
T_v!$N2R%{P?sfaTe8qH}ETMd9vb7lV0;CX{%cxC}wS)uk6<3YLi`a0Cut{(xzeOYhDt>AF8tD5A6l7?|>JR69%6silF(9*A3A+y
2+cisvp@6FV@h=+MBdxS;c@EEaLzvV^zsM{P6Q%SatOaU$o5_K%5Y)<ZrLvzk8E>I)DH6f=wCF@+)$@9c-
iKv1$1#idnR2c#VGnGngtZ+h{iwqklO6@bUEzmv7%BA3weQ@!j761mLz>r;C<nY+duayxLggum)%boPnc6*CY~fF3-
>3C+9z3e*F0|x%l|*{rlvv?|!;OXg_X>g0)puuxit;Hvl2M1JG^7mU+P^iVTU!yYruti+@~PzWo3QK@)-
)P!D3<KdKGPOz45KSZFPfWfHeB`@~b2;fAv%PQI@5s#XZYu#80p;(eXBoTd19kvE*W<>e-
CA6c_mtx^yRiKF0cLm)K|RaegLtNPY~nYTAUEGs$BP#tktwaQy$snVG-
`&e@j%N?IE6c4+u(gGAK<A4S(fY^ozQ#Ea!=4A`*$hQV5F0Xm^yarlhWXcLCYgoN0K|4WlVc|5J0{bsEb&Wi_Jb!cUf~|mm?4KJ{
bD9x(BUB&hyHD#9&<9lC2wlueTrg~zq6V7AMX|}a4K|1Q3VxSLxwO0<vvVQ*bpb>$5(Mz}HmmMS(Cy-JEQSw-
HvDIUR$#H>z{iYQGQMPTnW$wqs4LJP27HNyaLaarOFm{r4$PhaW-VyXi?h?y(;*wZVp+auXVe}3n@=>pgv}Hi2NDhgeTkx>?vXD+
{^bBW4%sUSUq7{A;Gfxqp3m7c7JV+q<MFHop)A0RWOKu$nuF;p*)~Edq6x!4F$o$GfCdD$lk6ay;&G#_>Q!3gzw*TAi=JZv3T0>j
TQISB0Gyher%%n-F89Q<01w&!vY)Dw8&-f>`XmTTVcAu8dB*EelP<Xup3;BhFb-
u)_`+A~_VM`@tXUwv&bcse7V}BZn!Lnyx8MULB_>pct`sCw5wKx2Fjh(z$Bn^C4+PVPBxYk1hhylJuLr|%QQh-;;K-
lA2z^Jsj%~Z^At5HT02_fw_43hCQXfjiQ;7IHP-=ddXwim<hE|PUFmkO-
>3_NSP`RYBOr$)FN;SM#8dU)igXqK>)QxG`+~Yp)G~x!3fCYms5T<O}nX5=jlYle$$5OaZXG6cl4~ESUvktLp=M#u3YQIH`FxNm(
1yL3#T7xHwVm5bKt=C+JBE$*%SD{c+G2u5jp#v$m7I5ZHV$n5D*SPx+OxK}Ly6O@p-
{@d0<>K&Q=qro_y2tF0<0I$ku{82&SkSS%7(mBx;)d+a(P9Vl@L!y-X=5$<J??h2hY~1ue*+sN`YyP=;{FSs0)GI2_+5Gr=)%bT-
8VK4UhMlRI}NV4+5AK|J9;s51r2K8G}ziUzy-Qrg@(=m*`uRN&Mb4^Z1ibbfD+)^GJoh<qf_jvdR|r8BeWRUW<BL~(>jl4rw&fkV
J3_)Km}VVT~%^G<Wpr6=U@!ex^2*@8aU{a8TK7m-NV}&1Yt-
5!Jj)1JG9JROf04l0`UCQGK0KKQ01hS*w08_WyT*+U^O~v19Tp64p43OB4#7{=OGAu!7eizI(N83MyzWjd?cR1cHQX&VEultrrz4
?46=zPe1bi$!1cT}T)O3J>`z3{;E7@KDt*w=67+$e19zD{W#7ciZ#wIEU^oYQU^YA#eTfDBnT?!o1{<aKPlZy%>?wAi@3DH#y2#t
4DzXGLG^sg6wGz$WW&>}*iiHheyIB`}791Uf=~~AN#8>-
VO~nMtG+!g4B4aRP>BCc~f`J<Cf36euZ*1WV56M{LzI}wzGmm4(04lXdZ3}I?U$OEnF#FfPWq*EWE3khthi!zVn|qdjFI#65niSO
4YEyP$Pn5SPcv>dyO<vxDLM9+e@IT$3a#dLoi18WR&`zy%hXCb!Yd71~Sa&Yr1`dfw{y0k?j|f{K6t0`WUc*3S<hFw^2>@4xR4E)
b#27OSd)Cnrn2Ds;SEAOJBO4rp!4g%Y)n);HCdNTK0wMTj5L%;~;5sRKMaG&jyxgpK4G1gnG4q#Vf5?crwDPvB?#pQCny5peosg0
1k|4gye_uwkEn&Kwvn|fGn|v;}a`Z0hc<RyT@^cxDf2s0vK!BX+O|dW$j#VP!9|{t>d{a7x5kzkuZl4q}z)vW0D$^Ao=x-
DQcIU%Kz^9szo6Xgrj%NRpj(&YT`tQ@xcgc7(e}=poMI>eeiy~wE1zeQtFB*-ze8Il6$+xF-GholYF7>Zj=S9IYLBk>~ik@BlsTa
^{BCY7RZR;kf(|fNS-6F3^<U_qiOztI^-
=0uf+m5yQUC!@?8S%XZhra@DVx_fY=CzyEa)1V69r+y788h`g%bWD7aFSWPkp7u9^$@|i@WG?&18)tqpf<d(zZ(g7RL>^Pyz_DG8
*KH_DY{jjWrfbt{#m$4l5KfInE^~EV_=zHRd;+2gJAsy0NQwrT%pa!MF^3O4!guHqf2zkzTaw<+r46_q!S;3WklLHVOy<*DDx+yC
%bM}p^#e&eR?}d741HlZ7KQ+r~P+qtJQcn4-B@sEA@Hnt50{}lgkPO(X9CbWYWgO1NOZP8pgyO2@@xtMj)c-6~nj@ga<;z)-
jsRCmuc@g_O|XN`dXn%tL*qllX@^AM%I13?AvIP$sr)aV(tc6<?uGj*%{OTISd4*vFjdpk+!_Fw}^XBV)Vw9xdTVj(}AHI}mCDjR
m9X!%S306^t!;QGVjU%DKuRao_ab7HV+l>F=!pvHA4jN7*)N>TX)1+3>CAbfA$G=@l>f5|@@C=S8}1AV^@#qDtFP9uhx?9MEp!vV
V)MVZTR5o3GXd`XL?XG~naIIH4`l8L^2JzD3s{)?yr*obtNy1|`6(bW^n6z+vqCl+2mRzwSeqCsX%lY%d^7IL*2$8~*=YIyRNZi^
m@IuaQshQIfDAUvT1PSlxH*=5XD&cEh92Eo{_H<{r#Ok(UsVqz^La(zY`cz+f`!6muZLKXxR!2PlY@()uV!%%ppm$gPY#%OuN{4a
W1(B+mq^tk@NOJ%btbT8ogK!U@1ljvP`bDu0lR#G>n>x=M@A*&@OeBqex4-K>!eL<L|x7l*&;H6^kP!c7E^^z?g)s;kP1C|m-
569(3-VkYgD%PxI(Bf#9l4!c%l-5Q_=a0agf_icIZ(<5Xhr0&4+>J~cyS7EYddRcEko9R>{scz|~m1DwqN=8Y2%cC#mGElIP1-
8%Cn({vF0Dq71zrheZ@fXgK6uL&x&5-#V+@h_9up4bPPP=jYU>#|aQ$<A-
<hBj;0_EkR!j$4P+O*5jx7|pMMuO3+iaYcMjL>CJW~46C0>pveRrJ3lR_pE}<kb3+$-
jm3z7^jbr&fJ4X3bUY9!u)Dh}Kw@c||WC89~vXc^*u`Vn363ZR<z3mkuE`Vm;PC%04!7jtRDPR{F5OV}bLFw{;CjrVY0E4lB%1RM
%r!^)gsSrn<-}UqU3<G6n2F-
L?Q|=k3wX#<urJ7O_+ZvW8hh>+s7tnX^LasoJ(yc{w<Hc}g3Ymd5kv?5umZ+h<A+CqYO)in&w6W~YNz+o}HMc0g^N;(u<l;OkWUi
Nh)|)!*C>4pXMiudst-n{6-^Nm^g`nH0GkUH8R4y76s<^w_N241O$U7G#yLHY?>Pomx-Q2m1*+P)^y6<F|BH%3WG)xU}-
<E)eGAzyOl5!b|7PhMk2mxO`l5S{pI@8v>*6!|*H;T*!@*1PZOB{;?v>@sQB5Zk%18WP5~<)TuZ^FT_jwTK*A4{TRo(L-
a7GcH+Q}K0NuNq2wGXn(?!MfIrVt6P_S7^KP~p2h#Bo&eAy{!qzc)4Pc79$1-
LT=+q*9oi6wxql%N!7dhFuMmKU0J*EAfyiD4m^CrQ?7f7CU%aaU^A%hsIP@<DyJuJpmH7(NBRhBZ51SK3W>x@26o2<|$@ghoeAiB
ELv#Q}2xj4QT*ylg=Yo3B6eRTcPE#XqR>d(=WsKYRgO#lATw^X#J>FDJi_f%-
4<#2VB1_mpKov<2$60PAO9t#F)(bO>1kn{?mZXjCrl#;N7WfaWV9<%Iv7PAO^kR&%cc76$O7N*u%JU3XoXj&|gqhMa~O)obyXAn-
uDoak|fw|#Tm;H8EcntE+Nu38cQ`b^UA7+o84y`sc9cm7}po7CyH=|cea0RZ?#jT1+JRQMSUpJf~hp_|iV{t=;Ax%}c+_PGiadO~
#sgR>AN9^H(30p3Lv4C%^Z4{w5JDnqa3R%(yB7^#;&11PxCMnGvwXXR!s1O~rR=r8D1MWs3CTXfo4L&-
*Q+b%<vR!I9DN{k?6WKbjf!b9M+Sa+kF|J00{PsLy^tDX~)VjSL@@(&86neJ<GNyANZ@vlpDQ&a`Oti~mS-
<cX_r$F;QS>5mbth^;Y5cZF-gKI*hMga8d&$M)48A=CkKL%h(@LtTvY9>Gqmrn0w?fR5J^)(YfD0v7$CIBbeWk-hNy}<eW@E4wO=
F$LFmXxehFf(;F@=pp#8fbK{A5p5C{HzI@&FeaW(E9YL(Di@#%3DTd|kjS(H8}SDnN~Xq%aRJtKeK+I#mE@Oj(ujuCigPEbhJmID
0D1DHaUw;woApu%Nco69^R*`YN`VT1lO1xor4xz(iMo=0dU+K~RQu?M300AvHI6jYHmk5TGVxD<uY`kIvDq5Usow0V97*p^K4FVb
9ls4E9Yp63J(pP_R#AMWf!?oVy%YRfFIx1?ikS2MA;nMcp$d?|XdJ{04|YL=Qw|;a#J<j4lF-NT;pcEYM}uriF9LDvnpXJwE`)p$
js8_h*S1{1#uJMXU;#*9Im~4yTruhH96elCEb{_T+PEuE$JZiV>aah7NV<AQzFF3YCcE57fsPEJ%F~AV~mZQUuy_bJnXD^;S&3!=
vCW;lGQVh+@T8SNyl79RJvx5j5_L&%9g{uH1O(4allV>jXq*q39L}6?{bVkd?H!BW?yNdjpm)!IN*;edHte9K&e2EK{B83w)}S%q
&TL&!aDi<=<FQH$K#@2gBx}kMY>6_}eo{s5a4E=FYRgqL9R@_*|lEMPp74^wd9=GD4va(Y#BIRcGBthjWQTm%%xZon?IJN<=Rst>
lK<gf@#Ctq=0=(CgHIgPm;(o}`<$B458d!mL-Pco3B9Ko)8L&63}1RoIjt5UEussKpA~df;}>QQ{1^l!sQLRvFiKbx_)WUTlt8<N
c-
Y{S~eUj)9%(*$@h{>hzDqAz0XIA6fO(u^x+4e^Ekj(tdyC?9izv`ud{Kkh$%FHtdAMva5(N6~6g0!Q0Vxtp8=ZD_t%1_t$lvxM_K
!>k3T&p%spO`WK~I>M^5(+HmH?^<m{S`{7z#{DLX;6V2M+Ve9o_b@$-
*27<|(s>tNwlY`(3eO{p%u+Pd_go{N*7EhH^h;N~cjO409Th-
9`MnI`QZdDrXV>oKvB?%DOS0xgl$^Zh&&WNhBP=xJHfESF^cI;tGH;y{bhWjc6j<~aA>42Y2Q~2)@gN5!f%*9h=A)rH>pv6ct2pI
XDRFLoN+66V}J}<NCJ|wrZ(?5NCKy+fTrHs0^=Y@ND*WQ%r^$l{uvzOl-m_qh9bDaH2PC;L6g2YM`uM`Op^zy}-
D=s{5(~2JZEE#EBN45|~2q(DA6b8mT^t|t6U~8<0co$q=VjQP5cK;6Mp<o5Y`a++-k>VQ-=AG+l`V9-
#`%uhV7S!VD+s$?^pWUP&el&D()4coK%oRS2Q?FYQHOjp&S{buT=j9{!xeSx(4J6${bON0&TZoAtt4*ygJIAUXT3?(N){d@CHhi7
p&6whm%A~_UA%1q`x$AcGGV>M>jZ@r7?9pumv8~fJEKwbnqqy)}U2R(N5}WI~`X~O)@Gc|gxA^@*b_BZWC~z>UUga`n>3y0@hdxQ
0+eFMFG@#943+_2Gm8f+EjGwUotUl5$=^3imV^ZDmx`s)nrmZ{1&HqxSOtTHMW!F`8jSBe%ED%G&bpHz}^OJD+3A$P`q5GEp;F9^
``X2ReAnWA-M-=#Y+nZtVKz-f+HV@hBYdk$W$e$f+p_KjGXQRIC<xk-
oFp{p>h*Hy&d9O9V&(l8FW`E|uXGkYjMlag0`w>?!C^;cxGNK}UOHCd$=v!)^8@iarA~EWKYzc5kuvS`FSJm~oLpIWO-SJE5H@vh
R6Ym{Gy8oW{6zM+Zh7{h2!jl@Gos_*d?9@3@D?#fQi-
#gOzZBE1tNgM=WjL_1Ic6d%T1?@PN;jcWxJM<nwg@ykQpRU{p~}lX0l4Fax3ZGTiOujf`p_G1?uc4tq+ptGdfPUkJn`n~Q3^#J(F
>J6sH;i_R5#lvk-}uCeRS2e*cn&Xoo17fhB)t8mR35VKYQma(LYo(nDh1nJ1=ZY5n=a>&r*|cNmSHXXwfI}rUvV-
7@ApeQ&Hacbs#OH5!+(rr{{=aeHS*PGero@Mqi;5%zABxolUw*8=h?HLW;{t$OHxDI4QzU3s*hK>uPQYwSmoHr6(1q_I{z2G-
1*6ZmBr|{LAZ$x5>|+-e1fVE^}v$Aug@2seDxuCkrg-ZISyEWqP0}pU|6w0iBn3X+fnxi6Agpq*zWOr&8G~_Y5a&6rnHGDG0*~a?
Gj(%Uw220@C~?Z=zkm1xoCGt8`6u=2N#Gr@u2H>vs>~0y=dRE`Gm5=ydu!7|{?b^$0drv6-q-
Jub(hrj=@E0z9^}{xAeXOX}}ACcPqsF-
8+DryHvXWLMOUlO(}n_C&jKQTU>%bljqz3zhJAe)4}%O9KQH000080000X0Qx3W4+#SR0FDR%02%-
Q08embZb4^dZgfm(VlPN^bZ|p#X=QG7E^v93R!wi)Fbuu>R}k*S8JZx69R>p_P_zZwVrz>whXFxgC^ns_btF%c+ZtW}`zU|Jv6T#
)4zWX0kB`r!>=Sr;xcoW(&SMlB$2SQI!&8nbgdaC^FI932QIr;@P#8tPx4BdXm=Mx1!==z(9b?Lzi*@Ti7p3R5v0QG9$vw}DGp04
%=P1tCl;)bO7a6C!&;we&?>}Op*($?!6BxyWu3+Swzyww$m<@Iqknt4bGR|;9+r0`W!IUU-
!A%qe8nbi+<1@IE0_!|>S@R^)s5R9Pw&^A{ou}FizpG6!t1dM*)1`>34B9Ydj=}S^p8>e8v83udCUGV;Cf!bl9Hl?VE&w=zxLCb#
69Qigsc^C7<Pz&K$-zXCFMFtV#Zta-jGmdAwV;>9c3WOl_FJZcQE$)4sk%wNtNS3gt{nEpxTy=O1?%vs7f=~jC+e(P@HS8(HJ|7Q
4tZ5F9)H-
al6{P0diS#PUD5mGXabVz&)=S7Tl`)`;3%3)ZK7vQn)djd?*0`j3#r>wXUSQaNtT3=@YpP@%MRSK3;5FA8ootY7^*IoBGJ?;!gSs
ZvILdhN1~r)zw_(xO4okELkjOd@TONrLo!ZF&ue>N=upXK1Il~bRXGs2Qt^$O%}!-2XW;ZbX?W@wt?08xOV`^-
Gi$DHKtr>o+YcBKH)>ouy6995-M#p3c4D<*6Kfp|pk35~yAT>8Q)oDw!Pn{3#kET@t`Qy!VToNSB~_66*Yo)Ud<<YdL-
?>c7vZ<*bouGKsU5}Jl`zBH0;)E4QSd#++`v_Jv28-yknKO{--
uV1@dR$4?(aHT2kfDG5fShq1?{YIIvlBT5o2KapH}TW`ez!)Sm1k(v7wg}6ChX5bbmm}<`A=acfLlKru(ZT2c<c{#lcVg2PI!QwJ
N3hRiHLigC=0-jirX{AA`aA)D!R>AgVG}$n^e8ww+tzSCE52%Ctq?$^<h=$!s=sI2xv3CjMX!b`Qn#qKIV~eMHP);UD-
4@R!~nP)h>@6aWAK2mk;8Apl>)C>6*H000Uk000>P002*LWo|)dWo~p#X<{!-
X=Y_(d1Gv4E^v9JTIr4?#S#8LPmyYVFeA<MeQT!Ca*368Va1LwO|MGTRoUIiRAm*FSv%VvR$9Q4vApJ7*+_uEmNB-
)4`hS2HU>+6g6>zC7ch_Dh^(XQ?4E_)A5&HN#gUN_k&%)87`b`l>7O24V+Q4d9$Ymkmu$+YHze1u9`8&&$0nLK^`-
AoO(V>99ZwRSb4TiuIb7@n7+05bi%lZH4S3y&z+%A-<^(voa2cOPuq%8K(pPU-
{*3YP&y%{K5#|M#@+&h?D;Nsl*LAMXs8_v7g#a}oaQGUIhS=w%bf2;qu*mUT5AE#i7?v&s(c-
~tY)XxVVbSaC4&%ce0{<$NO8mJtaU3b6r@O>*X3VI<;EqD6DHD@UiNiI^(al{!t?3>)7?I~4P6Jj7c&0N+gzr*scdr_O_u_G2q5G
B;<cOTdAC(@i=iFu{^(sSBaX@38Rrb>e-DTP-T_7MkWIHCciUtf{NXOPDV1Lc`3L#=4B(*h=Z@UrzyQyIX`I+Mr-
J@$W6UGH7OLTHfEjsgboA`oy6Gv9bbJTK)oKy9Mn9QSwv=&uTDdubI3*_bkN>N#kp<Cq4@lJ)S8x+2Ijz60dNj;l!7&08&*10Lj*
_?91DK)8CO*7xiOcCY>3!<aX!vyQqUe<j29Zfo?5HT>^Xx8hQagXZ4;o#>Qole2u)EZ5vSxZW0Q^&{AMnB6UT3!vz;cyPK)pUt^N
tD^lE;SliL$zRSTtswB5o+x<Fq(z9ej(1Jx@j>^3snPsB)ucGGsaElEMbUlJ!gps>rq(T+jI?XwsY8M#WZl{iA7C79eX}4Lq#)fl
>ye~ZDmEB(TOIg?iusV!V<VLakk-
4G;m!QdRDhYmV+8DqZO2!nhhxntS&Zdl7yD>Gr;jA)r`3=x3EhfV{Tce3Na9*mtzLNm{%j~R)*pD;8@aetS#J<(3oE*D-
spARhGBWVK?iS0hckgsmXK|Ba?-sDmpZ9X|3F?H;WBHkVb;|DB}Vd3Q`yDrk7)wz{Au$5kzUJk_q@aR_m9-
pHk|^`se&3k547WK|aE9No{I7-Xby6qOeIK8KgZWe-
k^D92uiiEEqOwgKCUpVoTu*@)qPP7m6FI%^?%2P4@A_32Zf|FZ+(9qeGp{Jvu$A$l0(~0}WncPcZYSTW{1Gy}@A67_{51dZ*qTR7
Mx?|LcDb-#V=6BXS7Eg2QK{cwaoMg<poGgk`7I?DTuh9&m0oyRA;UjV#~#yW&R<sXaQUmhK8_-
aQ1Wkr?xfdw(E@{^&f~LhjbiRn7;14>UMT4h{G+I?rxY08s;D{tEdX|Hr&+7VUa}FlhJN{d&LMZMHj&c4hS4$L~H&nT7G#9>L5Qc
YPT;R4~2$7z~*`gN83zI4E^E8A+&Bt;5;`rgg|h=jwG0V+s{=LPx<uWSHTt97yG*fH81edjqgtzY%)Jg>nO(d!(ez89xOJD@iG`$
8$dSvQLH7EPbMiv&T1hS*z3Rcl+I5bI|H`2K~w?n!tA-zx~F=z297X{y{tgwDDp596dzSyP@j1^?dVMg^_R>wNR;kr#`5+y8U{ux
mN4qqx+ZC=L#2RaQZ0KC$gu8#gGO2&LhNTbI|Pc8eNE{?f`-
bUGV)k0~aif7Zpvg;;u(ssA+{NIwPZ0tJR!4khDLP=>s9r?ss~yi0vLkH|SMIeIEQGWghh5a}WH<u_MPz4CP%hXD#$wlL@fYqRe7
t9;;!Z%)4#5w?}LJ;QlM?@Hr3najX#3<h8l9t-ItLKlvi{O@&(c9k-S+h{I%sjMfQiE$u-<+J?pN^y-6lr`zha2F-
q_fyVw+rP2R>f=S{<2ySzTSt3r3_ywFn{nb>~h{Ok80Yp*$9ERy-TUt$7@-
kl1f}OhEfUs%|8tr<o)9Iq(e@Q3KbKHJ!Gr5SCERL>Aty`(hnyqf5-
@<Iut9QUdRlxi;CHk5(BdVy2g~nEZGqKV~MAP5ysY#!}ojH#7ql=FojCoYrAAR@nZ$BM#sLtW({@Y_dWfq0U_x?2ISa8GRXMcmop
j?KxcRwF<sO>-_c=_FHV~!=^(K=TG78LYUM*}{8@cS``Y!GsN=Z}DgS_h0Q@D(JhiWjjLAO3mF#VLcs6bk(WktPy-_IW@AUW{+wj
=3+H1xtkN0Tv$Y)m!ddm<-xvp;B<vOkrb-
7aZ*3sE)zRX0qt~6an$DxlnP4E3y1=`R(${<yXtESNF;CtJSYo?~vs;%dg1t%hl`4e=omSe!cvnnwv_*Y~ouMRg55XvZx@z!RmVe
MdeQ_#~~qP*vdXge-
H>+y%~LY4^#p1t9#3bt9z^0gMnK)>zGd7si68Y(Wii7%&~WJG#Y{18kPfP)X~AgK~_JomqF)_1ui0rS|YGDINGJo1Sw>4X?yt^G;
pge$HD*uhMUc(r_T1Mpzcd2*SA5arW6P}J98;r0U__{XVn>#bAN&@7^NMTRVeFgbDeoE<Ml=j=?<<x^`j>bAfcVsY@P91T*lS{H4
6P0*iD&d>)Vevd3ZD(Jec|RcJ|+=B!Ggw+3)pQy#bU5K}qn2%5YDC9T@lN6QxzH%8-p7)a9LiyVGy=u-pgww-
x;{s5cC@zq@L`hzoV`L-TUIHE2VD1xJlex7lwumDGO(d3iGW3FJ0%1`9$a6uVz81RgcR4Qg|7)PX{z*=*IjogN-
s?!^a}Afw;bEuUUKo2S-
hLB%?kyu14K@;{JIzJ?HfxO#1MfBV{UXHEVQq@C5PkO2O<`X%IqS1;iiaW5!!D!m&&DKsWWLz1JYElaIw^^|&?TGbhq=#IWc1I9D
e(XDdbru%W1cHOsSQ^Ew}kb1a5cN5H!(QY>3?d=nI+#9B5ksvzB65IkEPjdZHO#M}axQPyO^bf*T0SM!pSyy3uU{Y-
(1#DnqrDARokP+D;&p5_Lg*Hq=84=bN*2!W&r&=_$3siZt#Xax+xaYmMw^y`=Cu=O)DwYW9ub+7!{>F<h{P^nA&%Ah(P)pF5bIdl
-(b5IBF@qzTj!sgq)-
xDPsG1SnG#nLOG9(O^aIqvE7*_X^xBwC6d6TV;24@h*x=j;9DJpdjA~d|00g`l+9&cv?|JCBgdB9+g)ItNOK5)dQf}f+8>Pt}EuF
aECHAIE|HdHr#CzIABrDr;dp_l>qkzxwZ>A|3h4Nf5=NYK|#qe5TQFiIn^rP~uzABM^XzPVfB^emdJLRT_Z0@0W%ngW40pSgMS>I
=_n*REc_dc0p|j@X3Jx@GJWy^9Q)s_1D%T}GTn6-$PgqSI~S15k!RqQ5pIDykTl`w;&^o`B_UVPu`(%@7%w@u1c-
!QebBsRf!lpiz3{{oA8}1}9kH{g()(0e(O6bcHX9MFwpmdK*0UQAwle{{R+YH5p!rJu0>5bKIM-iE3wsZ#MKqH%@2K*%aHGx;Rad
hxe}4V;DFoS6|(#YCcEHM@(?F3dxJsF6^j=Wj3ZYD3gm6c~;#b7pd|Xxk0@HJd_deL+VkEH+fEQ!3T+#1Tx~j3+`q%5f1#dEa&XN
cN46h^rduoRV^uj%25i!kONU=JYF73s++`tt-uiyZ=-br@lV3zVl^{8M-
Os8+6PbiiAcbi6xlRie{8qP1Zav^NJ&@iO3g<F^LN3?J}F*UX3C*dW3*sA*$_<+=O+f|Db<gMI5*~W82IRVQjxcw+$y3BUBuR14b
B`xM3Yz4jX03tpDje8%(S>I9I{=7%Sz7CJ-YB9v{H+n`7y($h{WzgiWYb64FvfmDO`x~`d&>CvMyjTyMrfhoJxW!rPIa;C|oi{vD
NgEW)Z#g;S>`vfK&Ts1|}2gl)1KlYV%Pcg}E+^D=E$tHrk~(VG_Y1q~k%PZsZvLjAFZNb&Rlz6^*JR$aYg_x3d1h1yaI6dv9lFN7
H~>)6f|zWj}6#>iqvuO9KQH000080000X0K&RvG(Q3W0Qv<003iSX08embZb4^dZgfm(VlPc$ZeeF-axYIoQ)P2=X>V>WaCwDP!H
U~35WV{=2KQov6M7D~Y@wHhc3a3E3LzL_jT2E>3X;;LwEg#vq?H`oS?Yr=&Ac}n&71K%*nj)<ee+rLs4Q+CIVvXxfo2C^9-
oWB=n=YZxVo#st^+Y%v~j?c(vCTym5mV29P1^s7Hz_0Qv(!F@}ejnvaJYj`1)~=)>4>V0rZq*xfkjr5fmGdL$B3OG&URr?re~8co
FU_6fk&3i6_HG=+De;iCTmhg73gO6V^V;wDY*myM=PmKmi@{j=3ESQnP5iUicmBNO`go+8sz?-
GPhV9Vl?)qaTmZ#yeIV2X>XN8(8nO`PF)G9Rp~NG9&|k;7Kbaj{gLwztRu7c}Hc<XZXnf2^`4e0;fBlQe{yNHEceB-
^HT(#~|sa;CD8JY71UcLd4h#-ppOTa>?n}3-
@a&6XJEd1m*H(T(&HrQ_T}}vMiuU2m&5vo=^&31L1J2VbBKriqwt~6A{D!!U|;_Q#}TB6NvRJ+;MrX*DqxkHVeR9!!n8(1li7A^+
fy|6?_QOFrqtao+b5j6-DhO%@Fl%NYaa2=D8_X8WXshB_?=FomBDd30>tiZ)ncydY--
4_!buQC*Tvlgt=J}UL|j7mJ%m5MFa0w=q!92Mk-UL7P-
TkdSK4F>6SaJq;nXNM9E!K1NFt>xa4>}Z|@(~4&X9={H)GNb5+}QH~M&?8CRa$=1fN}`X?p2;!^wOz*}00OZ8^w(jTJeIwmFkx?4
Eh^v$vO2T)4`1QY-O00;m803iS{y)4s79RL8Rj{pE40000_aAj^mXJu}5Ole{-O<`_fXJv9PQ)P2=X>V>WaCz-
L%Z}tma`*lUiVI;_tLoa8v=6&h6jqi;fV_G^BN#SH4T@cr-Ay%%tR-39({2y2@WlroeDuZp1-=+Q`2qN_UoiRweTgF?-
!B%sr=^t_Tfj_Lk@<*-
j8{fRX8tI7_Ss+l&GARonl(K;{&2&Zp*pWvw@g0%@Qb7KuH7a@alRk+9V?2Y+V0wJNXn*ZhjOUeraw9o&pIZ*eciW>{617$^?bjt
HuC%Bu&w3yvcGNCRjaD7?e4s)RkckyFteF;+YIdaP*-
Ohyj?k5!Vd}CXYiB17;bk}b0ME+M+to1Yi{TC<^8g*%d?uzk7h@__~O&|p0U0Mq+}KK;OMA$_Vn4a4?q2+`0VqiA3Xj1=_l_$eU{
`2RQx+6+>qU+Wq*~<lN7<Lnmxns4ZBHSK>J7Qy6pR;_;kmb_b!0MqTT-
E>Uq^H37|AhKPk6t1HC4_cs)<nmn{qp;MlOb2fA+(XkvqC?EvQ8&@Z6g5jC)3=Sd-J7D&OYXZ86kIewRj!n?sw$6z>{1m7-
1g<@Ma<pt{&Rs+0Y8Xw+#-
Ig2Ghi?9pwqd$?faoJA2atAs)enG@tdS6*H&uT{V9N^SO<4_LaInK{=E2dI*K7(LpK%a007FaNC)s(`v16d;@p;=_upzmw%4FR!;
I(3ak(^Bh5FwEO5@;~y5;6h|$FLlVYO_qLW|$`p4DvGRhc5Yhf)}_5{}B9&;VdNHC$N$dsK@$Ci3>5qw!C5qfL5-
D>Y62hi|oyUe{8@_ctu?fq=^*u{K#m1&h|Y^*88plfk;5;hg)j%mq|NZvhJqBw?Wh=;|2rkfF8vVi*hQCpgD>SfguJ$j*&4SbB+v
(E|RA@Pa4KHZ2CY2AQVlzc+g`@Is$0aAQvlz%V`jqx;8`?P${XIdD4S+1hEFzVf}CnqSO!fLc<0yfCX!yyR|~JsH<%?#4z!s{@0A
{l5$A4Er`BU+#h`i22G;_%1I!z>-G(eO1)tY9zg^oY#gQl@I$*_yTT%VEj9N9Ko553w#F-
4Dt`j!DhTKSh^fuWLTIO&h!`W9z07>8RKSmNUk?QepP{y)!4-gX>UDpo9?-
~s!fptubZ$R?`Ma0@`|>}&`KOovm3;G$FaQ0Ue>hm+<$u2XZ?_O|^KqbcPJ*EW7U{Fp(3XTnI@6_J1TaP!?~8Ijv{ZbY8_wFc_Gp
k<&|neC1PdTy4<pjgtRiR^R1xen0m)6%86mODX21>{smQSC)~q31U$V`<W*V1=a5!qcc5u4)X~e59Ewnf}v`OYpBdHU14Hg7^lNP
XBtU+rPeG70|)$4M5wkemY9(Zl&(sIu>;{b(F<75PO_Q+zmBL`?=$($?lT>f&KCOzVnnZjgHP}Zq>ZfRk7AB(8Fs<>je3L5b{o4E
rhUW_(IW})D2Dzs>*RWv0PxcQtDZC<vUgzm5)Q6ufz8ssg>p)K$ny3{Tj=n_bt>FP9ZXa@Al)0vV6uZ=UX(pN6NX2YXMLy_xh1GY
tyP(Cnv((qZTMKcjEkj_QP-0Xd|eCy=oR5vE+2F<N3!0tTEI02VQ+TVg#zIF5*m5?-
oLc#}VoB9^)et*ela|6tnfFj9n_U*uW`nuaU>tRo`K{UGHyCpD1SvbwVuz%huU}z}kX4f21qr$2BHgvZhgD8>%H)UxH^P{rD2Ju_
h?g!rdMc4iY|8BrH=ozD_+H+A5-OY67vlF2Ugf-
m%0_Fw<@1s})n1D7+A~Ub5$qREeNOLJT@Thzaj=~kFp`yKJT?Ym8x8L&GvH6qLCcY>L7j1iibes%3uaJ2VxgGV)Z`0v*_I%BNkDt
;X8vP!h+4ZRBy1iIz*xCLfOVt#3sV6eP_{U_Z&P$kdg06hMhjD?XW@DlzG3?l)-
=Ae&y85#FvN?SNhctozQ2KcpZvUjnr^#1ercZwVZ@>SaZ-4u*-~RS@i}^2?uN@cZEZ*{$y=s--
%~s2w|Mb*TAwpTGP9I4tTedvs&3iAm?S|D#>(H-Ea>~pojc+HolpI{(kfJWnSS{=shGF`l-
0qgiIn2zt`wdiB#szePicW@b7C8S`jb!TEEXq?M!kDIHXgB4p*+bLbfD?c}je!wm2JbnmhZ5doyqRMxh?Q@9b4+=uck<*U2#u}9$
rGmL(wW}~i0qqF8@UDAurAWjJIODmwu9)vNVdSd_%){nbd#bY5C^KABMr0k_08h-?c(*nO--g)*Q{*zJH;GTv)d2R;0r)nvnI3Ip
Q><ot)C%9e-<REX4j!4LFDtz%vUVImTgM|x-I9<AAVhq)LX&(Q{gL6++kDTY#=!?e0-
4n<DZ>qgM_XOdQ9laAg}@D7wl`X180>C0Yym+GGj=`sX}%lvxL~4-
Cb1;_c3vDzQ^e)^|Qo)ryY@@W&(nXeF&ck1GNkM@2A<!)g3{?QRP#p?M&F{HCS{LBxlwo(11d64r#wf#NZ|Vack-
^T9Rg35c66SG8^^?2Ya$W=y*<k)znpk(LszCx}%|~ZI4Wh_Ig;Hz)RoO*BI~ucL)$1(3b**f6IMlf&jm6`^Ax}_XVrjaM?Cb`s70
@0j<DvZn3Vb^%dasn|;-RgIIz+YL0oFjW@bTp0!|7aK?02uC>$4M>W~BWWm_;UE8zdtFHuJUwxHqpuzP}-
y*Yt(XQ(R>tk@0yg#h|#89C~W}?bZ@V}%z`x<H|XABTw$whUI(U<*hVG_dBBcfjd27NrF8b~Gi@j)dhDp*2V4ukLzIp^}3KIcFD%
PHbE$Ojun5B|p%GS0%(niO5LJV48<#GEJb+5&BhqqiZ4fJ2CLS{q6kG;`tOReku3CL>_3#rj9aiw3;kn`*c;7F)m-+U<ak`b-
(;KqZT4-1p=i1ZG+X2sTbQ@sy-WE6)yQ9<0-
=Ahd20iyK<{PXx58jh_5kAuh5DD%dA$p|tr^FW(6F1$k{|v<N@A3btVVy4;BngsRk*Fy1Z5ofvkfVw#3#N61VnI3R;O@p!AlN@aI
N^Vam+fBEOsh%+pZCb>Z%oE)GtY*iP|sg02xgE|yRbHZ2`etV_?GJR9t&wjTN24Uv0`*@f^4dtTT;rd#3p5AeKyhz?Td-o3Ed-
2Xs&fcYx?^N&JK^yR(dN-XiZ?c*W^7+C3qMY)CMw7Jqli7^JG%|~n9`u(@y7;=Snv7sG{g1lr2U=ePLiV_LRyN>)K&3GUL>snYzp
L4bJ0kcWEi+(n_cUzpc#M-z`9ZHX{S8i-hs&w~lYdb(7-
pF9bwji*&icwFwBB~NPSD;Csg13h$T~(8#pM*_+?6e3;ES;5C}CaMT(AuNTosCiNyMA;<e2_B5=J4fT=li0W=>sB_2ONxfk>*62+
Z{5g0n3>M963iZ05v-T_7mNM@>xZFBImJ<N~X4t*OO{7pD?$ja?Tmx$xnsSCj%GqV&`-
p#?A!$Z25`mE^~c7ve|An9I{B37NFhg3G|P+pG@8eswzIJm*QRW9)1zSDfvK0oD8HJYn+WfaI3`gF>g~(oB2PFWuK@0`=H{Yth~m
NPNRHvE~3t+H*?{p1<p$Jh~M-V9b$I3{w}hZe(aM-$U!^yHWG@#5HeEW-
sg}k&aQDunMvo_3#%o%nLpj2wM{cF@>r8Ft62K(SxI>!$I-V;D7bGu_7{`jkG-6)+|qVT?OR24Mdvp<I9sR-ZP8mg0%AKWYY+I=r
D<VUxe6!%aH4)S(OS3<K5Vk$Z+{xU9Q<Bt}AzWq(h@ftXC~fx&9gfa0=PMNh)&@CXB@z)Os$ZFxhG&0H!^XdKACE5ya3oXwv>(!>
B5~(pcJE|KJCdr>VX2fGW)z_ZPw7C?z|?)k^d#Y!?te-
?1XJ2a8)$Aj%X*QPm4wjnIW@@D6McJESZn)&F=jB}}k!h4Ma9CaS!WjG5j3KqV|X!dmn=7LN3V2RtB>{-
dd4VAFDg;lg_ip(t;AP!YOM;d(*w4bBF-
0KuJVk7`Y((x_uwwmk#?bTXAx4aplkbNAKh6z9wdR+rBkkX(KW?PYu82FmQIgZgCzx79OiTA`l)Sbr^R)(wG-
P+fwj(eXi9Qf3nr`Jk+&UX5kQO`6eT)KY~2!eK$L4%jq;no_7P%ifHrrhFRb24Ei)B;|2YYIwn$&8Xiw?>;9QSYTPCvf6WktsGx_
sX}1jp)1;^CF@8G)@YP%D%BKX3&8dThNbc^x;^tPl(UpaupV4v!Vl(gAwEWeSGR94MN_1B*#QPh;L>?rAJA`_l|my}VIk7GMXHxw
-J%!xF2lYr5NFmIt6IFKjf%U@jh|xQR5-
`p_V##;=^ak_um&J9hl37$uAhh9BmBhQD6}U!Q1XN64+jewvu&igMcBi&xn3l?kNHfhvnjS)e!|fk{P;m7dKwv%q0ayO<Rs$2lwH
p#`65qIG$J5%Y**ic+mJh}HmQ6eV<I7)?>$0Kd>aU8<LAL^IQS79yzTi)Vs_$_FenC`5*U&qyp$|R5yc+`Xta#W6;CT^_e1_OzXO
pEBCCGEOFr$oHV~QgJ4R7#yCm#r2_f=wFJtjE^P>}<4OcEVIzM2o@dE=Vjf_zd*CIjHhVs$y!%1nB=ZcwYWT_U!-
?`6_J`@jTkzO#b4LeVc!vwEFkVdZXM=a1Q!C+ca?xzN#v;j*rDRqq_8BJdktMPhA0n&k1!*MY@mc({mHBcfTH6xaYl0~>yG}A@!G
m(eG?8;~V+GPqPSGrzMj5W=HctwUhkY#B1y({}Zj=*>89CambQTpq$-
ZN52e5qG<TJ_1cg28Am92|w0P)v3cVlG11J#b0xSBqJ&3D)a@mdhin%T`==LyYy^sD^Q-
x`)^6&Z<Je;ml7F!lp#J7RDB0y91y?ck9ZwpGSsGxT`3Fcd3QZ96Om^ljBS-qw*`2m1V3!i3NTVY<EWq{8Xz)_;HtDqk9Z<z70>-
vyC^w!dK*YBH7Hh<)&bd&S;(H=h}kvIaeTYQY4tA0#tLoXKXV_B;@r+&joI$v?Fw^&xb73JGs#KhZeb<2tg#n`G?78oLe5kXW<2m
vE0NE%f*5%ufTU|b$tq>@P0(T{DeI=Q+d_&btVoo@4Zlg3Xb{EcB~Nl?!`77d%%OKt785C;Iox8)3jW)aOUhR$d~LnTki)2sWe+A
PF9ltC|Y&|FdXd@V@2$wqk8+gE`o2s;+N~oEi#TsAlOvvLFEda8gw|2reMSeAC$ywBOT9QK9rm+Hfk+{<C+?jfFi~(r<_3-
C};d~%9%ttkW_t-)MzVF-yzH_c{h36Nzot6$&XUl_ax1<{AFZVu1;4bDvq3BD*oFicJPMM@gvFjQQ&wkzN^CgTyU;+OA*;GP_um>
silF$P;^cN5F)J<^y?pK9_Xax%|}cYRkZ(8E~vrm;pDPO_JLa-#}-Ui@X<uHSIaV+lE(HRx&1>5-*=Fv76-
xS?Xy8SO%v7@4rQo`rMrEj^z|j{Mi*2~etV=<)vyqM*N9f5>+2Sp#^^i_#^&1k3J^WDW#)&Ph6iFN$@l**84twO9Mc!eJE0w3{Ls
@Qb{#t})QM-
)5+tlT)A?K~%!e}hW2Mj7cwl<uJ<x{Ye<+L}lpmrUfJaIYiMRxT=!2EO;dtGi(RG(We8)wFVI1vwpY@PGEhqdCmlIw&1?T%)9dIK
wetgc8kMId+pYIzylm#O=?un4e9+`wU%AHYKOT=Rj!M@pBrR)e_Xj*Jb%L9YUDjFzabs{EWOjvbnM3*wdCx%n5!y|S~&y1qXoK0I
gVrW#5!5u2>GN4|xwsDTf6s_n?Ahal!bX863C6H3hV2pA;AnMR3Oi@GX%at@YMq{=?i?&+*d+{6-
u3&2Fx@^|0E~cLmVEIyo5Kd=uW;SYsJ=&6(*;cXuWH;E0<0BZ`Z}@_M++{_8%tA%L0mmpALEE*)+PMK|G;w}rjx!yOnDfBfwuMn@
n`)hn7#6ujjOR_%?S;Do5`MP;($E1>1Bd!hJzvvDLyj)Ra!GZ`wSnS?qtXf+Es1$Fnu#Bivbja(5VRc+*W}{sm`N~pCgAZ04E~mb
91$K0b!K_xt`Ck`axA+Jag53m77XrVD7_AIDD*B@HKy)(kKksGy)cu(u8kp$3kNmGq45nnh8A<#5#R8@<BefASr9RjHixLL+dc9c
Ycj>?5$D#XM(zm16z5(XofhMM1wgK4&ZofrppdQ-CmALBOiLmQ&sQUm<7ZT`3B56~!_Pg$IY3-
AD1|t=mt390!pK*fNF)VkYL{F*2vw6uwn*g+f3vXRn0^}BJsKridIHDLJugJ&_QM4apu0EU8Y7>Na=~OJd=E|#1C~em_K=p={pCg
`o$xzTmx)~OIUezOtQBwYjm?<VQlCE!9jmDBa0y-z@C+SDU_0NIcMTIDa#GP<!meiv@W5fhkS@WSd(-
lxQ72My+V20>1aI025)`=4BIjKO++JfV9+rG)R?mHMdG5b5El$Z7r^kNGPa9T;<9}9{6i)B1@j!f>*eDJnM0Fx2KP8`^Jr6?doRA
M*Bq*;U7Rpe09eDozk`B%fZf^mDfza784?1=agZ%@(l2;6@R;PS{TNgA>+?`Th@;se6ZG=<~93suJ(1%)xQ~l#b7r;O`CEi|bD$M
NdNPm!q2XzGmE!rz*zsJ3&-|=2SN41;mr2WOoi8G}DYSV5Gq`AY7Ce87<2;-
+yGC*`Z70`d`O=k?^Yhv=>VPY;5o!X$!SjPkd=S(ttMM+fSCp7>A1S-hRF`U>>D9^7-
s9VfPmRa;4!LPu%4^ADt20_>P0)FvbH3ut#NV1Nf2b(7+ffAd;MPRVbz+0pv;DNa|s7Fs0KXpp3>$c~UMcOhIYNtX{wHL^dsu-
2~6+8wlG2Cj^fO*^C7Tojd48g-
F2SvX>Kd+u=f!F*^@<x&_&dMwMU`1qmfRb;SQN7RUW)rT00&;$Dxx<rEps5APai4{bUBTB<2!D=3sDZrcDpcSC$g|sl^&XVc!qVG
NNO!v{bm<5qd6Q#8R9*_RpgU5&V0b}G+1-9ng=Qn^%~>GW2pTP?!(I?eu5p6%1_tAlpQnpEDoD%k?qSBnV>F<7x&W*~y-
`pxH?}j%&kQ|Ns1!J}SI`GYf&|Lox03~Elw8n=aL3{()QUZl!4l}s!t9es67;@(&a{gLcQfFbZW0q?*FV{1)peW;AAatfY<rJ!qA
TlG7P`1*SKjgqY(S-H0oR(^P;bsDRi$x<&0jtH^piR5^FY;O9(;(io8+o#Z<^zaw%sILpIAO2orgq(X_A1Nm<z%in#h-
8N|PL?VepKmiDOEn4DIU@<OA-
+8=mNDo<0+N1XQIk1UOtRx_EiIAI^{e%uVJI7*wFO@t_D|J!*7L!w?x*p}EjC_DL4szoz!?+>{+|AGLPx07voYxf)kGV~i6%uqy>
W@?a+pvK>LX_l6<~RCt1Kg33?DMkeblMkL>kwA71batFP=n2_zG&yaGjbrNVz77Wp#y|-
^@i{TQ%6bV?K+=Y&rKG5@_Ye6JI(q*#h5dy3Z^A}qDP&qj2W`%29VFRggvN2Nbia{fHXeF*@%jBBp6V8)s)ryk=glC39Q_kV`DLH
2cTCyCuKttj-kzZj9p<44pG&SiYN$F5A!ic6KI%6tGI4bA}AU)%!lg)Tm(du+k*F<HfYZ^G3cHg&u5`W(R-8kx~e1rqS-
3^;t_)RMK`oL8xq{KG+?XDLo?BYt0vR_w~Fx)Uy;3<@#Df&E1=XezB5>JvRHODfk<g9kzNX{^&PCYX@Ug&iZI*Z-b7QZva_9?^q-
_4d6eQE6-Xo(a!r|HNtg`xJHRu>y)5oGFG>S1kYDnfZzn5_XTlyTr9j6+;8w&T$lc3rjmUh4Bmc+$`A;#w=_>{^C-
?vi$99Yo6mo+{su`^sIZcaCVOvBw)V1(egtgO;qDEreYIL$;uB)UXC!ga`RvdLNIP>e4~~Ttfg1K_9@#Dn!Rn{*-
AWL9=La?n<|Cs%PbaF|c*EITZZO*gzOTGxIthe{dwOqRpAq=#Ow*$a*}4=hM^#P;pzFpf-
J0Ym1(Ej<!!yG+L~~=$c7R5tEomO)Nb^M{4Xb$;eL%r7lCac^>9C4${gU2qYH1vB<P5t1ifR!Hd4IG%Y{cVGK8wICcwy=i1E8?G;
GDB|lbHC%wafv1``#jG}qkR(Tr5k;{;*%7fWM0j;qA>u{XYp22;KYU8zFkjsKyCbNmxrk{y{AaC*~qZI-
7A#~`_sOfeyAfg5&INNhPnwhusVSC4uZ(Bt%Y4=0Ir}<<T_h)srCX~f7{Qbf?ZU2C;p%PC#dpOM<@h^xe=?WHexxku^1as(U<N}=
G9rR$!2QK_|p%Z`{w?10VcG{!GeDjY0i##DYTbYejbXAA0FQzG@wN3S`Yw}r1XnT!V+6?KeXzm=R2fzJRzPaCxP}1j%Om@jz)y@*
1;CiA#5X40zb^)-<^-
io@rdfrYLtQAhBI=_FJ_IkBEjKD3){vp#wWaN%UD>1L&&$WdCBCkdO3IzAheIU()98UGqqy3J@KN~+dppcmxU?|FSRd5;{!*>}g5
_%Pta!4HL%XAJpj^V(@GfyZMXyC_?DZmsHNaS0Z$Xv|GA7Sb2{*vXGmN394LotB*JgBs;xQq&x}=c^?uVfcc?Ly*FQVR>WX|`gCJ
YbdJ&&H}VFBdO#$8FUu(j5l-U%;PMe}?eHD~wjtY!sU_Ot87b*h_UOo91&#1iVhhUso*bm%UcIf>GjI9+}flHg|ovf-hNQF4@;+w
yr9emOTFIj|scfKLRkXs1R>B=>b+ja(dSd3i3Ok6ZI#p3@Dt@}x)Qs@es)m-
^#*qHCygGHDS$7%Z}I81==Vu+egiWCqr6<jI?=7@n=D*N5Lb>oJpYc#5eVAK?*>;pM%kGWeV)V}(?}^b;X5l?Dq3&G$pPj&yI{I2
`L7^JnP%Njw@Ht;yzqYiw)hsCIYC1Qoq^(uykp=E0cwC`*zbCF}j!6{VM4G~h+9#D0@wkuG-
{Vh~%6dB>F?Pn!utoTKe4Dd?OS|D0I+f^y6DzAv+~&SCg2)f5>CgvT={s3Q42F-
FiKaz~8n!FG(QP3~p6+d+Pn@}xG^h7wHNRP)gkI(^nb9z3)GKY9uuFGD#n^1NyzA0`VYtWOB4S!LaL(dew5YOsbMU`rV@p+kM3%z
-0&RN{pb<qI4d<TKd_FNqt7oO^`~zM1o3p^VOk7BBD;R~F<aW3Tv>t>SjX&WNlW4&a6IP*%FOmQ|XRbN7-8$9JNeV98ppQIJw2-
>*&rTH#*&p*hepeX}sOHaD6?2&5&>Y%U>X@yMD;a!-
@+dlhXqnxks4Qb+{{$%Twdn8!@G!fMLFSjvGJJ1XO0bmW9_sA=<1MC52CQs=(~Nmtj#dJbOHNX^Vev=gbu`r(+aK(}Zlfer*kv;N
T9FNvOtU*>saudNY9g_&Y+#!nr(>R76&Vim<~1sI{0H^=-nxc7La`nJ^(43UMXNVa30AlMFkBGOXzhB>sd2J0T0zzINGrB`-
XfP=L>4Y-kt`naJ`s{rrnTh{_0kyK)&;-X-Hmba;gC$iT^Nr$>D+x)HUxNS2XL+Pj~?Yd7fMCKZj-rlKj^KvX4MW85&=0vv?vM8n
(>c;C|Q~VxO4}M<f{Vje>o5##JZ5dQi%OK_Ob!<zlT-y;V5r@}zLJqRM%wr%)t2^Uda8wka$%-
P8cY&s2NJSdE$Pi2m6_OI~`;V*VRij=90Ec&{NB;*<O9KQH000080000X0ID>Z(mMbE09^n803ZMW08embZb4^dZgfm(VlPc$Zee
F-axY(BX>MtBUtcb8c}pwG&sES<$jmLsFDg+8PAx9Z%+KRWLlO0Ngo$&-
$0z3G#K$YxDnxTB0D%%zMo9<4g)0RL#Bu=uP)h>@6aWAK2mk;8ApqLmTg|uv005&10018V002*LWo|)dWo~p#X<{!=aAj^mXJu}5
O=);(ZgVbhd3{yiZ`v>re$QWF(U(mcglc=3kou5<+cJeFio-
T(nj$wCu$sh??Nsf5KLd%uKNt@o@%Mdq=kwk92B38DdmPh}G=hwm8`4O+rG(GGYMBQ&AnGI=R}62+1|%(MqMc#@-
YHs5KuzCiBfyq%u$r&$CrW@=$4fE;dnsEn3&S0i`|f2@vO3&j%3In@Z$nO6Ha;lEO8Oc~PDof|+JrA1tu~={6bfDj!IrZc6veia9
VbNrXx%a{0d5*5v81dKJ!i7Q4c-
wxFc1+!!2pZl)#Oc*XrS~8y<ib7+NS`hUx6S(%jCI8Gxz{A_&kT`%L&mt=!If+$kdnMb8k1Tx*cu$zk4i*4qy<TARk@8Mm>oYizP
&_w5ociCZ3au>^QDhWJ9r+fmBvI;f0Qmn6cK{PtG<B5&ov?$c*dk_RMf1QqZNhJXs_K%A<UZiYQ)2NT+oHAEI@f8;n(y_UNytWe!
mq&0&$jb8Io)lJcXhbYy4G8aley$;KtwvuZ=Qu#%j{%J@?fFJN|bVeByF?2RgsvCE6J*KLI*xsroH?BtbI3o2SH%e@uLITuMh<N~
geA4_C=?rl`~<LUuuhItOk@?(~)Q|lPCFgwkGgWg{+2P7jqDkT4~wl-
&tB=7S7Rb!HD>pf~2&WLDL$C1;ha?X5!Pe&dkDSVC|;d5TZ%lqOd%nlt5?!ag|`97JB4^wG!oJzCX>9?;V0B*n*SJewHUxT11)T^
3Eci_)4w2{}^=oI(JEKt2_7L{K1bb-dM^nu1bgXzMqeX1U_c1aBsJs*b!>(iP-+VYi-
b7f`^Ik?qDu6?7AT={tjxl%obJTkk3d}_0Y93y5ay9O?c*+q?e#ItQ{=(`N3RXtm9ZU#>r=exlL&D+5f!)5FFQ)mneMfn^215ir?
1QY-O00;m803iTL-RzJ34FCXkH~;_~0000_aAj^mXJu}5Ole{-
P;6miWoU0~WMy)5E^v9x8trc5#__+OV!`4NDv@Q~*>^b$mRje|L0s7J^?WJX`V4}WRyJdbR7lF_iz1+J5TL*MuRvd+e}X<vUZ8!1
&g}OtcO^STfzp6Q?##~4%+Aiv%<iwq`J2~&*gna|w5aL!@q`vlHqB@?Ag9Ogwx(4%BS|t{G>eKR3CU*jvT8_L6lIe(Sy|Lu9H;p>
&x&gaKP*0OiPv#iH1xj7vn$zBQT3J<lX51%nrue5wvsm|hp&#lIy-rN^fq~WM23Lh8<(?rmeaV3-
Y?^ebo=|m?LYOm_mj)dI`3CeXKQO~oTqh7&gQf@yao~8ROMYZq18F9?m)D`7J(;<BH6w(D<?EZ=BC*-xuN--RyE0r2?YwM1Hz;_e
f7;3q*@fnS`WH!F*?cN$?@U&(K+z8WDSh?cu_ayEE<rgY;I^3bv392qDfUQ8fYHyPx0j-ZEr%luF6}4-
lv&pUU8l#bV}wzxVWbIv@3)g;AC_atY+UGvOOYoQw<bl2?v>=J?4FT*R+Wv35vR$D;T=d>E-
1I7^%|(>}(!)6rqZOsT7)CHZ|ULdrfFwQ$<h<QIypz&9m=m;)o+Z2gu-B0p#l@9+7TOP9~F8_SB<wG-u3Ye7Xf-
y2zV^A%KD>*|@oYF}uj&<wnlADYo^_+EMAK?tloqZ&^7!T*x6WIs3n<akY+Tw7DrKN}zO}CAairYzWilPU^~GPW0vMAp`KEm|Qca
WGu<kE6}E;nl53DEe!^l;^@xIMX&fm^mv7LbT-
e^hPqxsw!>8A>6qS>Iim#LiPT_>IhmqSHVt|>=_{a#WOa$%CZwTtQyUJ#^kJ`$&R@Mfe)I15>}$tkq{vfp2h_lk;;L4R64_`heYF
e$QMxg%0Us8d921jGmd4}8H9&1u6^<yZO=DCvt;+&LPUsYbZ4mjbY$Kx0z#reFO_EJan%G33$-
r9Fz?+SQO%7H~YZN~z(iuh6!*P?{Q9Y4FAP|P&={SR5P;YH?mR$r0mN58rOJMHj6WDBKFh-ql450A41zo@_=SW6EH}}V$Cu!Y~UG
klWfZ4Sv%Ulol4!&ws%LF~<Sg5I@^&IwFOWgD>&A<e5n%EQ$Wjn$4HmfvG=Rh7&kN7L72bTB5;wmfViv}p)LTI3bVU0vIn%mc+@n
G{-
4|)UfL+)a;Mj!G`R@{QsG3AJN*eGDt5sWQtx|0&ozT_(w1bcV(`V2H*+jGSt4`$NrjmRO;&)`VblA_b>o>?qR9XbWkVh)>eLzOno
z76;U+=K~d-
_{21cbDApB$B&?2^}lCcKd*diGK5v{6M}g3#vKzRKHHL8r<B+B+q79Gk^(gGz=VJ^D#lCa*wP4SBpHSW@Fna^9dP}3)O-
TZX5_vy94u_*n-
9#+Y;bLasmDxf`(Q<MfFm>0h%QY8Ik_L8eQ_lelNCd(KR8AMf@EvtkIyALu_QR9ckq`Y6Cj4cyo42iN`Gp@TSp{W3EVqBZ_W3Sc=
>YFnV7^y>H8`h@l^+v05U7tH@F_<9Y4A%ojvr?0<2Uen@z8AT$8>vN|h(UNNQyI@`57j*1i%BYO4GgZaoHIVixYjo`+Q%&o(~Vl1
=HI8$gb_+eWbwx9|OGQzqn+)G!rg1_-inK9w?Sj;@F!TIb+&(!PnqO~EA)-mqVb=-*X!-x+lU&ie)3_=|zL+VW-ZGj*~kr6hwe!4
NssqB%v<Sxw@)C#{~-
o4>h4Y4NZ+#XWFQSTs`Ac)%MlzSO;fQfcjkD$h1dKG0Filb#jK0`Y2KUzi1s$xc{(~5(6*L4!pI}El&kP@>mX4b+}G9kegicibP8
8Vo<12Kk2fNB?GfItwK!X8xd(YiWB>WU#jO%lbTD)AGR9kD2}E*I69CN>4tN$cZ7*4!95cduT|!7tQxd~`pibIjOV+Gi4g=&>Nq>
{|)}Qlrzu(YTpg<C@~TdzNYD7&NoYDHzIYPiAokZf&^)6IiWQWScD6?5`plrDbe9uM5TC(g+RZ$wVP()elay`>beH4{!uJMrE=b0
d>8jmV!tSbT)uGQORsl^V~ygV|~p6AJN4yD4v8yEvkw1#?r*x&CBrDqDwc(fMY0{i%<tcr@RABLy$$xczILX$?;~bJ*nI^+Vkdi>
$T@n{qMBrFtAyBP6w~{f-F8pdsZPOoZ)+?EAI5H?mb=v=yLQoZ_j>z3=8bsD3c_=w1TsV4-
Z{Wl_oLEG}eg1wS(rA!{1avLJw{86RIM4_~neWC)Lv6>!U9Zzd3oAoSwZtIyu)Io8C!@CJQ#dY#z<tf{BjLL-ESYe`hO#$QpkTcN
`l^P7c2S6?g@gxo^@yut?)AlcbTn@Kkm{rg@n*-
rPs0$t>}KsqP!V4cU~ioKXH_>4pbbYW+HzXspG=D{4x{8=8u0Yt*rQ0$AfG2UmGHzWr_iERGIRasxsCFlw#`J3Dk%ew+O|n+#v{p
Z1@AzQ4c!bboJexBtBVY(E<P{MUc}>!%+NcG3|!fbq-XdZawj!H#GdkO0Z&yU(7#{QTMHKzaAsi{0mYdr0!fe=vIFfX+rsq5ahX^
cvOgi=Y4ecXF^8E#-u-c9v{K0Kx+LAebDCp=GpmOHF{n0Pl+*$S?SNUxcLC>%ZLJ-
+Q_Dvj1}L#k0NVPxqqHzyJ1^pDeXxh0+I?%&dcO@wy7RTr>{0RS4nez|_Ijh*dWZcCJ9IgKV@kD<FWDF)TreRc#iKlRC7u`EtTQO
<Mzy)nA0(&mlI!8qkQ1CTyFHWOe(bYuT8X#-aGNfqML*esxf+MKrWOyWZ99FLH1X{=hZ4VKuhmhfZ%pWu+~OEv8jT7-
IC?TF|Pyg$wI?mqq^lj-
z;0Js8$*Lcp9xkiPE8okpvx+{JiptM+%byE)A9GQ`m9xD+vtggn6FR;L2~IcIB9%rR_AA_1L39($FJZ~1;bWM>QOCiczSqtoMWPL
re4v)>-`BOI0rNIKU3X5=G09S!XxpN6&+-#)+$#o1LtXph-
n@WJZ9KotXmyO4caVruF;kP>U4LsmFIayTh*hoyMz)1TkzS|MoeLs~R-jFomBxLtw7-
aJx|De`3;5c{$kj0D;PfV<S>MINV1PVJ;SGkJ32Y<&3aULf>RoU8G&fgZM9>0lZjlI2S0@jQ!WH5%*S1|OZv+s*QP!)dk-Gy*VnX
5qjC=Mo#R47edubMIDn9GO+^!pif7RBrPaGZC?exiGAe`D{To_F$zzp3L*;*i^QsbO?<5(qCgq3j*MMmMhzp@xGEuyJ!imU8a-
{Ujc?XY?S~a_jq#d?Qyh{6r!{Shap>Snyk?t8ODn1!#OPMy1LK+D{53rMIRqJ+7*jM!`YIt<9i;=ucOM28#hp9IBn`)y8JXUK#&7
9C7x*c$h6Kd0~A|$nz#!xi}nk{7P`t%__k+bDYu}kL|}QCwtNNKMIC^06s;PA?#MPzFI4tMjJ}QHuluzf?4yf}@)@(`Vb&VGXem3
fwQHzy%?p^2hA(%ve8wSa^5Az!+Ci0k+)+fI+MutP@{c0)r?7%Z?JBDI_=)3*g^<EqhW3ctK8b4)g{XKf0=wb>NVs)xP>=|y!m1H
cNHR#)QxG2x(L{noE;k7cGSAZc@H88!PCV~E;H!ptI=h;rOa%j%^TiyGa3@KMJB}O5yN|e>Gqj^S_j$<Fhu5Sdo^%2{VrNY~*5r7
nP<O*iu(L8+C^8Df4{L2&%-h+~j>Xa%Y#sl!xbXVPKwM;c%vMn3h87Oo>mx8sk6rt3hg-
@~u&YwWR^I8h)g&Y_(OPikC@yT9_oy!v9uk~07wDO-
*0}3JNrj`1YihA3I+nX|NnC924lbQl;zl^e6_&1%QlXyAFE?T7`!;^>#hAe6@5Q~e3?Bml*#0SZ?hLJ>*I*abM@Xiey<T3f>Eh{?
Odxwtrz>`#FB;l%MEzbr^2uUd!wJY>;asY9k9_B8Eg;DP7ZZ;)tq$nHd?VX;dICe+NOEj{`69rKO`>Z~DL0fhYu5dt0B07?LzH55
2q{HfMhcB8;W~!&*P854zmStMEF8evLqMx_iNhNe^UF`6SeQeN2)KPU#IbmJAIgdndbhMHXx^1KqZ5S{^+a)~=e2iscPb<`!jLs~
BOB&(iZ5~W<g3Ax)4`K-
FF|(MDnO9Id<6fv{baWNWMUI+WwbWYz)`eQrSe{aFnF3qtT>jib8p5Q0~j?a_p*{0*DA5J$@7vA$e315jUjw226A<y24YYoJj9+C
F9!Yq4858{^$Q)2SA@{eRau<f^+M5Z-O=HF&2yr*sRqum%o|4SqZm#`luIMFf4i5DHk6mw-lyvLj<#FZf<yuQF_(h^%mi;7Sru99
f(#%0;n!p~vEaFWV-5~7`Kmcig|^L)EQVT<l;^Zp7fWrnA6M@(?*jQFaZOJI4L-
5W4tgZ_vQW)W5Fc<|2p`!?7aCeAX2()y&!_KjnR6gT3)DLYQW6Jl)wBlIG?@iTV+n^2PVE}KeREAU|6i2uAAezvJ2G7wTXR%li1x
oeqr(T?#n4&REqB7jvrc-n<Qx1Xzlg{w$Qy{3f0WEIfAD}?2^&w|{h_J%L`xER^tqanRHXjy>6)P_Eo%GXT>TJ%!-t!#D|mR-ElJ
WmPZCugik$nTBHN2Xx4c?#=N^-
U2QJeA_;Tw%P)h>@6aWAK2mk;8Apim>Yiy<r008YS001EX002*LWo|)dWo~p#X<{!>Y;|X8ZZA-
5b!TaALSb`dE^v9pT3M6ZxDkHWuRxR+$)%w;ui8>-9mkGcULWy#bCk<PK_oO{h9a~CIa-
z1|2=&G1VB=nvDZ#it}zKVfJPr*HyZe(`034G|8@0ak*Uh4tLM3@nqph1dMRE$e>d6IdN0y++cs^j(o_`tgRUDPt4cSrDRgBfOq0
t-W~DSn8AsGLEd&f$=1ka}4xZ$tYIZt*2Tk3_qPlipA62J?c=zu&PtwQFo;-
f>{MFwklVTgUEGGhf)H&0&O3GrBL{q#_b*0M5<k{=jFVa`9)3;B4`uWFqVkPwEKPqcx^T{MlWm&@FR^mO4HhpvrQh28I&0}3P>ep
tv;P!Y7*UF1{Bb#jJnqD7NMT5L4+v}oo&HRP~zg4C!yK&!XUB=UWm`o-
=bOM~vU(xT*YoAVGI#h)$MXf+jmAI8<tHf5<;y_)*4*Hm6LiE_*h`l@sSsE?&EhtinW~V@aG`*FK$cq~OD^H2|*(kAIXR^vvxq4T
(YP}YXrqN8J58Sz}Ygn+*2UU}0EWk=~=vEW2t0YON7w~u}WyUkMM%7nanSs)2G^TwhD|1wJ;+DsJ^Ylxx0bzlvo&xtO=(I$0f%aH
OmOvU^ErHh>2;6u-9BSmXIni6Lwqhqu%7e{}Dz|fS^=F!m<;)|IeDQ0-
l%g;Ke4#(>i1vC)?v(cu6tF41^bhDnIZDbZufYYg20LL$G%i{)y&_3k$-
SaQGDXwWupD^|){X5Oou7J5Mz?jQQg!Rb6u*gAx>7)a|5-
iDrZtyoh^e&H*Go|rrg;yOe1Pxd{4)@+1bL;P?MBz96;jOI&~>BoRKmd9Qp;v!=w??`H((_x$Xc0j{2?uiE!D>gQEZ&mJ8eeQwT9
k*kw!iFHB;nZBjfB<BT>;y@Rp1?THu)HmyKleG4tqS&i(C!#D0f?fUWNjjkgYXzb$f<k8AmAM$o{zc6*?3YVwjnh26&@*wxcU-ze
+0BfOkUqxPx31x>+9&XH|FxVv<(kz#-xdu0p=YRD+6@IH)oX8F5E`a<71?-
%#zi=ffefW=>|C<f{toP0f>2qJ6e4$mN}fHyD_gCA^8&JPYqCw8g?RCmD+0wqkL_!}k#74!s?fq<rKuzztZnjHiw9s)5P$x}-
{n?uNgD2g_<VMoHp3w>tv7rOO=7eL&#3j8s~YF!sFk}NOa(N5;6C$pA}p_uiMHN~xp+q<x489W!$fJY}K49RX13LwR%ZPdd(sUZP
jqRb5q4}t(~)~0d86ZE(-
Axp!cNO98g)_n`&sP{zMi8@3}jk+1IEZ~Y(lCVe@+y~`pA6?gZ*HytR@jy*|iW^u~<%QAb5xt_AARajxJ)v+h7!t9%YYe0jp-
><YR-Co|UJ}`P0LCQ2B$(oLWY!Oy>Az44Gc(9f0R38U8MB8pmy)tvK_AHUv(r^sT<^dxF%fh95q@3v3>LxhqTQ55CN_R*bOPPNq-
|MJ&R&uE9CsR~;*lPjn*wH36+Ek+Lv#+{aRc452=cV=l0PNi@h92BWPO~;mC5RYB6A;sWL0dzEJqON<0oE^s`rJ#=>RmF_E0LOf-
DuOW^<b*{L(@aY=hZZG6K?CT>~tFUEM*qmxquoi`AAbqR4e-
LXsgYhtvjuYA?@paM8zh$Yph{Y7HSAyFwpuC>Jf@(Xt7N#<sXlElNit^Ufd`5wni;P#55I4J^F?D_n{1Jocn%Q58*^l2a{$tb~9F
qx3TNkCd~S6_du_ZfGmF6jR>QO^NHSkNq5X$;yI<3kkWgH!p*nLw*|(g8+n!e*fXz)`1502n!1w-!w1>UOqC<)4GK%_g<x$-
tXNg3*lM^Nzg)ALTVfb^uM<XAX>sAZj~b^un2c*9ynmG2)>6LCu598EOu<o{pvE<c{M8C$n54C%&y8)&N-yHnMLAXbZ-
y*W4x*H?ISxI|1sX)`1U)}+ko(Lj_V1}Dri7i$_<)r%oHgOn&Lp*LONdsnxVZPK&uxa0k~7?ai;*PLABsz2F&&@E#6BZk?dF9(;_
11l(6caVggje3jf5-p&nM@OOGtj!YX`;$s!%BVtb4TNd+tV>pujR%6^~1OxcZh;{gVEWx0fMC9Z>{WFe+KAek=67<~3%Q=`H_q-
}7YGqaQnnr<E^5q=uLo=89=paoR+sc!?W*{|0?@GkRoQ&hHl&mqH%b>V6@d*>4ifgNqW`J3Nuji3>%7inFcB!>KeMI;J41p;!p7}
oXX_edmdqf<=4JnARK^`)s(3^GRid)dG)%-
Vy??Wr1IHB4WY;of9{>0qx`FcRNjSctxX#q=$QeAMv;4bWj=K1W$sm~Qz|cvv8}pT;aMgUk<$2s2C5lcH^nApn2dX+OKPyDTdhv6
V%sz!0V*T|W}3&7}WOe@bivg2|_)_y|J#6!!}qQXi`n*OyW;b2eg>U1%U#bJm5n$7zpW;UL*3!~zN4%Gy}t3N{Oz*<($5B&iSb^h
KuuXP@yl0UaG05WQ)_3j@*j_elMrZ^UHTi$QtOiHXgWxHuC~Ly>ijBT<#a+#?HuF-
MNLh7ts_!A>225R9k=Le|M|Cn<noQoY}RH|+G0i^6PAMPqj__*<`e))mbLTX9Ic8puBlq+1fv0TDqPECFz)j*fvDj-Sg`sadfAuU
##h2e!3r4x?3rXCGKcFHe}5;b>Ac3U@-X<`pF2;-ZX%Vk9P-pbC0~Y->85C-
7bzW&`~1y7bIK7Qo*>P#0u<vnl(VUlH4saeI?|IzMmdeFN<#9hm#2jjZL^TEM{3iRGxZD<O<lGTblR<`4G6!!3JAz6ht_NZ5mm3o
B-Uu0oUT<v!GRWrv79QAX5_xfosbs^ju3|Ep**K|bQ1%sIs^*iYw?vnNsZGEd|IxA(RbHJS?a0fh62&w>z}dW;~+AXym0lR^FvWz
82c<*hwHl9mSo6xlX<FPkDG@AYtkb*i>1waf!xc?!PCRSaI5Sx}`0Mud?8ueWWLArd4+>GF_(7^%9^95wWZDL0g)1Ee7kagUg}?}
aSEmGaXSlky^b%7%l`lqEz~A<b1`#!-h)`BtI4LzH3580LA-rlPb6zxR>?H@rWijWel!;0(7LL0EFr1@_VzaX*Yv4g9h#{{PJGv9
4ePQYf^9V~svm^ARgja;&iS2qw2)bF~jwv|gXxmPOv@d-
S9=(A0|5<;92Wd|e;53;ZU6{3nc!yIcy$C^#!NTUNJI&pg;a0N%mt9z3`?;uBTZgCxNbLLi5@h;HX_!5{$8G<Z;;w%thp%o_W4Pf
k1xr~=Qjp|8_7jL%LRd9*v}ju`R&%-
+r&7q9_#qj8}XM+o}P#ugh0uX_$6U_Z<UY7GK~2ZAnWo(BiZq6LOYge$(&auOj%=gBIc**$4ayDgir)6(3tU7s%oMm4jZv)pYHo)
b<T&NBADVZzRqq@)G9Te6)xk$emk6zqU}pIm3u#VNMa#?*cr?D5Wm$|(HWnJkzD3hiUc??dEo2_omvnDJu_Qj;W^Ux4Cs-
6Fw7ZqY~K_#p6HvEcFv9Lm6+WAZtt-
7M)_N@n<y)Xp8S2+H`PB@OlfmaE(qhunGPY_JFL_Z$E?v7#|ja5`5SIdpZ9d2jZS`iw7EjbyJO)UYIqu6{LI8%tO`XVP7_{4;7&<
{rnQh|rE_KITz1pFGp?n$-
pT`|<hH*L<!V=|tazXSMg2z;RcU>cZN6y)QZFaF01^2wk@k3%Iuxbjyh~>VBVZBvwuOh85ISHWe&O%4{Q5*_$oqRAr<|U8R`Vdkx
0*Hbe=VL~on!c$4?ePKlA8=(Kh?2X7zlo`tFiev-EG(>%-zgY`E@q>U-
yHJaUBDvK{5^!ec|hRXI9V(h)3W&eU1@!G#KXmNIoeVZR)t)_qefQF#57BZnA@p{P@2iI%MK+>HQtk;X6xjP@=yA=Kd9uBP69=Wg
zbgT<|8Ifkj<jCDSfS&!;%z`V4;YNTi98Ll7r*pn@Xl{ywT?1J*fU3O#1z9`Ok7rrdJbi)KYl4jGTPT99Rk8$3n`KJn=6icl^P#&
w>E+1$kB7D~#=)dXRbf&4oA6GRA>>@1qFbL}XOKH%UQH}G1>BQ;>jD16HQ>H~iS7%1fN#r%SJ`M+o?*^`R~4~VsJlCK-
8Hf=SwVMmtbhJ;c1=Dv`fR-nIOd8)Ta>u5?AFdSSYQM+y7#KsAHJnp$aeT{65TsvD7W{(Y{dmHvYh4kzfem91QY-
O00;m803iT{k3T06a{vJEA_4#;0000_aAj^mXJu}5Ole{-P;7N)X>Ko2Y;|X8ZgWL$XK8L_E^vA6z1xx-
Ns=h`-d~ZMvug#AD6q(B_Vm;=*kZHUGt~BlMsj8^#Ts-Lkf_QoAQOWGSga|Q+3HPidt}nXnqH1fFETwzW-^n`v%X-
@FYFJT^9c%fkBdiyM*>x3_w=zNST_sEjPUS?@bGZ=aQFB{_VW3cf4~2AH7V=1+<!JL>vc7&%GF`^&9he@%~s7K8;@t3^=4I$$62*
lHmh}3)OE8i)>TutA5oe0<+7?z&HKmo<sf@f%;&|)yrcrlVtqERPE3jC>gPuWTDvx1+soE`oiz2je7jb4T)E47QZ?r14{cMM@AL=
CVq=@tTzwxdi&a~i7XP$q)}<-Gvfs|ui@AkjVV@Lj`N_xT*ScIRXVu)+Syv1DeOk?C49A6frN*MP-PmlZsfAy+%W|?dLsrhq^;uI
7*Yn|QQ%`U>hnu!swFc+kmg}!J^ZD=9vlr!`Hl-
S<j;fP0H817d)_yvz*3ZwHbz|z9ajcrN^?Iq%m^7<$2&08)+q!QQAp`~HO))K3!$mXQ%*(NwpIK#Ry!TP2K2Px3ABy>=9N>d5nr2
=WHT`(GUMU)(?_VikYx??i)#`80)Qq2&tHDQojoWbes+l$~%hel2pQfqt-~H~{tEVrYKYsFb{Nkx8`1n*I{9;qX-
1ta+(@e`b5aSn{>1nB(s@m~-
Rn%>zYK@nx=1rx#HZE7IW<>>7<$85FRyB)DdeELVoB4FSqOlyW&#L;|c1QJWF<z8yTbz~(ax*^BZS@U)FE3j~M$hM)Q$+;^L3;Q~
4bp&pe^H*QAz7&<1QSnH%rgy+9)3|c^2YxEu4&Gn(7G99-!01;pHksLMt`Bqi?ZF!6&-
#wnHO!Fjf0{u&#U?To9b;<A7bzFJhvsXB^FUEV4Ag1POX4;(!42Gm-kf9)@q!yvvR&vR6JDmK0*M~a+ax)Yn%C-
a*Vaw@w8g?+HyYYXZw$k9Z*~F0bY@f@F5l%jxU<kdAlqoC06VAvwK<ID3l67Nkh!N`oqOJ6jdxhm1sw=R*EFE@~s-
gadVD8`?kEA>&>dhY7F0bd0I>^cR*KHzcIS5DZjjJMoqYD1<Jr{H86^@iuIZb4$sS#TJ(b~|GV#A{O$P5XD{+W_H9$M?o~5e*@27
3S-~@<`u$<~cBy6<m{G6q)ltB3cyTD(ULOeopHwtReZLJhK+pt~j0PTF020H=#Z--!Kr=*iowJ~b?aOMV*lV-
8%x29h)6`f_HOaPFQ)lb5QngylvqdpcE4V}&y)E5oxF4GE)PjP2b834Hd(Rf)BXp(VLYza8L)bhy1p;r68fKJOu8-
6#9lLgCda$Tr8D)<ImBc`mEa~`!Vmq>C^%TeROHGS)p;`s>aX)H%1XIoFbPRm2SJsnesu=Sq-
>hf*pXPm^epkhXst;g>Y8mzH$f#8V5Bq>>)gtZGld=cT)SGIu?q_OiEwNCzAfRikj%s3%%~c;emV(zy_Tnn4K?B?tGc&E@x>%IGN
^KT>qI3045j*xwAp?sEAE{S)-XE&p)iP-8+WsovPRga)?(vV3B9xE?&wRuYg?V#2yeL++8rt5>?FWb1tf*j-
t(y!cBr^kQR^4HCr2t;%Vs~jA92vI7o3eupfv+8IC5|gMsfSssHpg<><1AD0%BT%B{fJAye;s!{Mc%`Ul^SUxyJ+5!M5mj@veiVS
1Z)tZi*`~~qpu1@OanD-AaIW!^x?Hnw;sU$k27H~+#M6<=H+Bl&DV<bZpw!*D#avDHuaRV;r6UrF4b>*Y4P$nG2c?hINIZJf2i4;
8hGNaz}am59DZ4j>`+(Rl8?P(rvqY0hu98w<wS{J9Ry~0jX`6j#KU!^NOs-
m4MQ3zhPb#0U{6TSugD~kdRQNI$J$9zLyK(102?}j?lIO4B@WpewPcQt9b;E~L&2F=ifT*XD_uPsbZtBV`%}Eh!u7=m_t?k~{$pa
WH6b1?G<Z5J6h+n3o~;t?u~3RL8kDwgOV4T~_7y&g8|?!zWdu#Fs78syWjj$ER~2t>Nz$IGph+2ZU$#~I_@_9eYM&H`a%EQ`!?n#
&oA6bW>809Vs)>@EE<OB<i=whR_^_Rq<+69su~X}Pi|~Zj6p@e)qv$PGc6wfUpN_iWwpI#}8bc|ew*`bN{ic{B{q%k$j*D9)p8|P
%{7DDz%58b{9vfT~%ke}B$)zd*R3()$NOcs1F{$cV<8P3f#x)hLG>w+i!|ZQhE1s8iv}1FmRgtS}*0sL8NUR31!#a7XSchFBchv+
dd}^g9Xmxk0SwK~`$eRqx8R)x4sJ8H)`n8qjq4eWbH7#ums`(bVNwZmJnr6J^25gv3B(Ogk_=wjBY!)h#a1K>S`eA^Er}O5dm){v
KFY}N?!$)yx+T}pXRKjDiTDO2_FCXXq%)rLC*=VHZMU8T`9*+TD3=KYD$g66$#j&PhvB^<bV&k6qDkT4)O+prz3F{VxW;>LjSQh~
m#>e6Zggq@!Hn7x*cY-
|x1)H7$+*hmHwHz+;tpgPCRNGPH#b)azO0<KdSbFD3?ZnTbt~$P^JByr*7@O@S4E1%kAF(taUtF6STe2dK-+;-mWlYzUov97-Y&-
`UOBZbwr&$!ec*%DG?%E%*BVezBVVq{#u35}rb({5DOs8gJ<VH?^hmWR9u`pvMO&M*Vh-
XlZtT*t{I;Mk{QY?LDucZ5_YMDmgRVEZ*uA)|`3aq2EqIKv}J%uh37ihz|uryfFp)J@$kU!FHy3&(J6sd=rrd-luI>;$aAWz>e8>
RPC8~ch7RMVUU0FQ5;{Qe8m{O_N6M1c~cJIffho8?j=(e~^J1S8q1U8dA%CCP>gd4!{@r08d&Ph)x<zBGyKwIh@PpWK+G1jKjaK5
P2+XwLSPrpxPVn<PJ~HI(Z3lFlwQj%@#rjf_ce1m2Tk!m^$jQQ0$nG?S@)G=qw&PNkON9nEdgP(N^DN9F6w8gJT_gI#qNTP(+#Uz
5&3Y<tXis__+^TMgl#kCkq6R=zzt{Pg(RHOM&ivYe<k?Frm)v##btc<M$$iDMHyF6=Qx^{7NfLIkJ;4f9=}I|YhxQK>~qqxKX|Z4
`@mg2$4yF;Qpu9;8~1(bVW5qR>_k{$YK)Y;}?Lh+z)Ypni7fJ`QcA>8g>S%Fz2XCk#NiriaUB=?`4I!f`yD9a`^!DBgQAIY@`F#)
wo%utl`|)}aVvKB~aLRf~8_EX6TvC{!E3`EVKY4cKTb*r8J3wWvu%FNjN~f@%QiBRIJ7ZDuix@Wut;L?upEWpN%-
q^l+oA#MYP2ET3mC94KpN&GO-Tts3$(|gy5HA0(FBno*PMvL@eDJCelM|j?X4`{Pj6nO#XIY7RMOtkX0%iX~Nl9RBV5*~`)9EFf_
IDn*Bo?!J+xgnfH7AvFf2(;?z%7$iFx~WlxWNTolPf>IIN;+n<o2)Jq4A-
K#JSoR0jzK8}T$hW_*o>V8&Q@1SN33eaJ^bndeUqdYl=B22pNMF4q92FhV%lO)GPOW7))I(nqu9*XYM(+aeV{gU&~^hun4uOmrqS
5KJ2kL5shaHg!q9F=vQWVv2Mu0R-
FS@4Q0b>*qzCn7RW9d+VoZk13_9Ck)T^Mv9}fkOa7B6zl*MSytU`4~+EX!yv#d*I6d5>cgs~&E#*mOYCiq46vRr3+LVU^C44rAHE
!W=ma9&;xs3`O-nxbH?$rLk$6Q{@&p&C-
ajP;hQ2kLQD+76a3qjk3<Ro04Ml6Kc~2;WG5^o#1bJ2LzG(%(=z3}Z0ZRc#E1p5ll`_6+=TPRmw;brS=cB@}Kh(?s*;O4I2Z&|{n
0*L$QvqouEg?hsa@9>2q^Ir*W4vre`2nUcfK4zzU}G&i-2#C{=)niR7-
RhTK*OknhnRk5`J9=8NkpvSQR@k4tL^)#)Gf;ledBG9T14_-M;?PGL9m@{x!>VS&wOgDrnoDg%6;1-
pJ*p}&<<Y#5;0;8qnOe{4z8etR7*3y8_^@x2RxW-
2I8z;ANHd8c2$6}1eosPZUEa&ABlHG7PWG7R&3Z{Y93o4+nSfu@z4KjfmP+PLA0TuD~B|1x3hsNhu-
+lM>_{G!TK70A<#XqQq!4pIcCbzC*?crvLhX=I6!Qx^#hT2((=Ot?FVD5$%fz@`xi9N=89)If(5hJYA^GLxSFW`vvwB;BJ_CsbV^
Dgrsq%Zs2k;tZ&MG@T2fgz=YkA>O+m6oiT&B-O!NQoEtb&DKf<!^78Q00<ztys+7QuHU@GOSE(G$elv9W2-eQKQs-+0-
bAifTo?1-
bcin~=2SoHfn)c)6;YRkgm{LEKclyW{v>(~~L`OO9SkYQY@fdSM5YTHWrwQkp1gYXhda$qeFvyAc4bQX}D65}u?7y<toZd_3MFSA
&ARvfeDpmAK}eFA7`k#x%|rp@ukwH3}SiG%pq>(*iw#4zu3AN2LA~K#`;S$Nd2oJ~}v#w}T^1Kp+c_v8jQjsoJ!C?0Z<~y@t1`d$
j;Z<*5-Ylu7{T_{-dPx&YVfG1X!lLFCM8;e^Xh_rjVk5E6{;7(AuNW3z9-
0%2{j{!E&3H7ULETcN|O?ouo&g`Tz9yI|d^WvM0VR#=f5<!~X#B171YOtx4!9FMSSkGf<ei^!n4srdl3J&z*{>@R;h-
E(dIweyZIb{i|;^PAd`9JUUGXGmDBiz%GD;vp<{4SYJ4k_TS>0C4z`1qH3(alvK<=e8?Vt~ou`CmdDV%nLa2X&X3>wWkPVMMOgof
Ob~xGbN2Wu9dCG*?h<mx8DIDO*Mz9E=#sKx6rgPCSp6GO(9$<%WVrpQx|m7+A9bO@*HaflGe0YO%}MI!-
>b4;!!3UDrl6zq>8|Mnsj2z4J-
+Ypcq!IHE;Adl*EB;&=5D1&_l1*&IhE?F_qYOtRtNnvLuIx;or36_aIhJ*+`NGj=l`X(S!I}bufMr&w)6(c3_Ei()`n#s*oTx6p=
$Fo3{0aXGLokoJ2Y1Y-wV`BXTM%og~4h)x#c@AD9NEZX_Ek>Q>2}+Zq#Jn!W>|WC7DaM~R#bmOs|y*$fi1-
!&On++)V<Pz{Jylxuhb+u1xG1*<A}b@fvQ-
;WKzvr0{8%VMoW+Hj*vNt*+1dd9uW?NC1X>1HHLu*HCymNZh2%j)vtuH7Z|Vy*Y~NQ=fiW=z--+hfO}66}c$Vf-
>;D4w6UtbN?n9^IIl2|GQ#jOGPc#bl#8xp39F>7E{v6RLMEB5jFYA8lo?{g2!b2ty~~zLm#^G!}J9()kiAW*M&t$xk^=p~3cQJ02
fv++zPuIzi2wW(k|QJ}CifixSCz)W`6u7xO8-Zgi9&Dt<EP8#^$hMq@acH*G1P0-
yJr6c5T)Ap}10de_u%{ML*=Vv*^A#4+xWP2khX1mGj1t!XNH7w8~{km9w^KS>%vh~3hj`OK;se4f*AZa!TxEf?)M*a6h24kt>%fZ
!4JNS-pU|FLKWHl)es<h)V}Ms->%oQ@V%t5n9*{RvpjH_PLw5<$Z@TfxfeF=Hwvx)Z@C4twI&Fq$T@Mgk<_P$+-
E1*B9h{<E{2!(uw^!8c(#w6<Tj8^u#~B`v8=Ri_cap=B_y)UTt*_2uyvV)R-!N75Fa+|^D3wso~!mKZM0-
3+=<P|{Kxcn6=equg;m$v;UBGBJ&9VHWV&$}r&5*~Q&lSG~?{WsaTQ+bRj&xPQ7gT>~I;4<P3;5(Ee=C&lEvCsVLLfboG5d~Ux1?
Jj}ddVjl({JQIO-Cl47DZ^O*n-
yB*HT$&ZD$cMO2(Xf+>nm{byEv<q*lmmh=rhr(P588WQ`Qtz6rFO|*1+A*{m_RU`j8`v{nR!jcgW+Nd00!cXOZ$^!B!<4FuRC?fW
@1`4sf-MsZH%P=jCOD-C<y`<c-
U|2o@!^X_+Q{KLih$@ARoQE;n9PZE;TOq_(wN4+}e7lZOR^d6Toon>E3{$)PZ9(J7^9LsKAbFg^z04aVnm)ohm59E8yDkt5Wt=Wh
_3jdeUtXWP-1iKq8{H@JD-U&-u{HNA>mxK*@(Z?_6f+|{l}zFtLGyHEf}NElCJ6NjSy8Nxb9Gol09gJFSeFEnM-
X2K4+z?Ywn?A<rW2*Be?RfWTJLErzHt%;6t;N%<}^As0|Av<>-BF13^zj-TVSkXhk(1JB)M|GfwvCeLAJfHG}3Z&&|Hg+_4s@((!
4Pz_JAo#>UXya%E8~`32*>cXSN@)*^VqX2(&HNbKiT7OBNW5=Cjrg(l0UXJq7h<Z5hy`LAHpP*w5^^HUs+lssPHs#n;P+>YK7yyQ
VEk;G&1zDPa+>=*6cWrg6L74?nkV&8V~U9agfqlJc4uIG^^otVi2)bLFa->HKoHMu7RzF?&LBa{{;ZgQt`5-o8PY=aA2JWzLke-
?<Z~?qG_!RH>|MdY0G9oBeL05{vI&yH6iH0Ub_E7K0$}C@#DX2k-Kd&fA`)j1EaTN&6zA&S@4p{51!4C6_mnh-(8NWoG-Bs<eX?r
KOC=h%O}1Q>vvTEdx~Dq6fHW@9S8#+uNHYk+1X&njao{v?R;^m6<=0KUUoMvG%S`EF^I}DVFQ40q$F7+EBk+7i#8%~Wj97#*7YKH
>5k$|ttfi-HXj8AH=P(Z9^J=ZAT6jT*MX3R#z9dn@M+;<h7|Xja9=Pa|Z+!nj{=rGK8Dz}*pveJ-
2Ew9U7o$88Jqhv(oHQpjDYGN0LQ!{&I7N*b0a!3Xil{>EZUj4#OCe?$2*K?p%^vuaXfHQ1x`ZM*VGi7G_(N0GLaat84~B!&+t%%P
D0dS)yBr!d-
hQ&TVY@l$<<ObPsWFnW*yv`+yJ$2WM{bdCjnOG5<=BC)J$~Y&om@FsK8;;D3Y_%or~sly^7CUuBtn8cFbQZ?4%_9tQi4K$G<aPf=
aHXu0_s+>3bE~&Nmf*Y=aWPp5_X*ZTqJE-)`vFvRAemVWM^6tspv-Q78utEYevq3dOi^<Y&@QKds#~=5}pF+>?E>V1Jpz-CGfkDe
4|rOZG2c1bu}w3<(eZiM!HV=riYA#L2NVtq|+z!E_I;k=en|>M6%x2R?wfQNmkd2yyjUX>c_~40>0jwdN$ldd(FewVxvTu6@24ca
_pzQk<RVVTp@bfFiNpK0tzBX`b`h2LO2TO?gO<DP_dBwW(a}_jqq2X*TZGG!c&0;-
3oKaURkZm1*E3?FRD{|IhaDif>2m<0oz{@Jknt|S)0+FcMf3}Ug#<7CE~NJ<|C<#M!Fevj5U*dLP0?Avt`qq<_N-O_I|zOJ7~J20
S(3+z<cdEx(Yqz6#Vn+s<*y`z6S4;ouwe9q{0}JtCLE+6?b(_D-
M!z!GR%!;o9RuR3cYZtJEWiE1MU=iJ=~VZQ4;RfyhfCkUVyki~NYAuH^+Er#<-
m8$`h1UGxx@DIIv&p$07>B~DUg(OqMW3t`9r!3YJcWIyJ|W0<inB`Jpj6vG(tX9r;m4l{%@x^fl5Ts7det^@L1q%T_&3?V2gAj2S
R!6pZnv}Sgg<=I`PxG(?#^yR8iOk`alZVVImJde;}wC9S61PC9!ZoyIL${Oqi4U#hf@H;v>MtV9rzK%f7s&YQ<rXwr{DVLzA$(ex
Pb$Srg#0~PY<<V=-
P*XtPei<OhbQyo>I5x?_6Hy2Vngi;l>m<V4SVLTqH|KGS&boF&!s^@WCB_s!X+!3=0hPPYQIugXiq(0E;?JGjB#w2I)~B-
{P4*~7C$OIvC*>T2L9bl(>nj3(ound14e1UN=(_;>@XA%#1{6kQC!mn3%2i2#rG;vk6V?{Z8+t*DFns=ImOk>g-x&TzPh-YO`;EY
oXm`%u830(&uYM~>HVv62u+_V>l))BakkAMiq_)1DS;2Iw+gc@Ar?|wF;LiOmMyO7)#mQ!P1frW$rL=qox+gtMXyK6+NzkM_7^%q
*%~ChRdCOtYf`7=i17~#2hLVx=#*?RV$+1<-K0fk@>Jh;P6yb}fuhP-
V7}cM3v4XQ%qr!TCdbxUunk@be4r%c1#t7GmB5IWsi;nkIz1*y~ymq;^5~a4iKWV0Lq)C6px2y@d5D|pd>gj8uOlOg1v)29HQiLI
tELpxS7Rxzq+vaOjMv*<b%Ih!eeSBu>$U-MLH-ZmX85o^tQv<Dth-G+2K+Y!u3U{r^juUB1KGC;B=vW&N!{ttgx0uAJ4h~o2K6-
W>BMmW;)~S<ICV9x_|E|7^=FPaDdJQ8zNBz^>3CpC7m4RQuP0f~mvfqUIu7yW;F7KFO;GUr2`y4YqZkCk-!A}4>W*mw-gmHAv)dA
{}%Sb9pouP;IWirI$eSCkc-9!K<w_(i1-fi8K`9?}PizU1mU~OMdYXd-
h+HD5Px;dkb#XUm<tt`IsakTJu9LDWK84ss;OqQ0<IeNl%3?CFV&#gvsKG180rGBs#WNYaiNTV{DZ>CDxn^#2(`7}?+`^aXiPZ`>
<fi0&to`+dvB@-OkDBXrXAh%vg>G7pp8gLkc1$=Qf7?3nS@H~e6URh5?Kbyx-
$|jPXjFJP=qC}3Jn;y`n5uF~;y((d+Ei}oU&5Ubsb4r45L?f&UCr9tSM{xTnc8;Ww4JN%8nw=|5>|*p0o{5Dm>g`TjeyG0h+UTBZ
Co(@&A3k^7SD!!l@#`!Z06AH?V-@#`WGnjyybN=e6re**3REP8sYoJPwozl4bU-HA<xu|>oM4>x&{0V14;>{)gV<KU$kQF=wwFNF
;86cfyk`xiiW!0a(0xso+EPgC6T1{*h{<JrR$)9J0}c|qiEA=Ri(uU@9Ojcu%Z_V(Ol|_ksXbOYoOUt_h!aH{3uNHnr5U+VfqX!_
D<iS|pK#Mj3p8o4sS_TQHw|}@r;<zphan(ciQUB%<Hg9qKED;qM?ga*qv&(i;HC<4y~}1fdVmv)n?mNPE6wh%a|-##AKFs-
Z37}0G84>uoL!b{$yyS%ZS5PiqRYIipfMqUUb$&K9Z;)kC{V*R;jn~nCu(atZIpcFCX#vT2m6_>LtLC{;8)J54fl^{$-
`S0%WZa07U{Hui@zT@?QgBt1t22eFtFO@#@o_wf41025Ww7JiX3~XL8Fpm<6;t}vfKr0=bvJomOk$~q9iAlbW0Yn_I8QHV|t!60%
(A`Hgt);N;BozAk&zn&tF`cVA-zk<791&?6+5C3Ypc^T(?`Iakfc_QZ$b1jcLS22+-|vlwc=};EY6K;$z?(ZQvxj?X4_Z7-
e;(rsa_=nK01Y$S#wN|1cv?Q5mxSqg4stoyf1qe+37%?oG<Qi>oL}B#a6Z;t^E#e#WK~^D2dkmGpJLc2om=Y$RFM2GRv2dg#1j<s
h<HRN7TbmBQ-uks(MXiK`~rLBvf$gCb4O8#!jg&?Dxr4YLuC>;Q(*F`>gJpD0K}#pf**W`%2tq!gcIyDGRtBY(?fhe^EgRApbU3?
XpR43LS>7EKqDg0SnOe4y@)odW3njy(X$ABjhvg#f!8HM;aaAK9xrcifN+vO9P5t3ace-
)sot?E*eVhPBBtF=z~L*1OuW>+Qj`>~)AEZ0@cTVdqAxW%L2Fp0rt539~J2&btbZYMii&;jQy|23KTM>&qb{Z~2HkktxckrvYkKb
Zv0EFXk`+a57FeG@}_<26*R=JO%JU2TwVY*nDFC$1syv9RK+Ku2*&#u`{uI4}7lUUI+x}aJT_Q@2oh%=SL0uGmA1Iy^b`kN3Ts>p
oz?jMKK+2r$z0Xh1=QO%S@{A4Pd?z%gQ*n3}?l#S#P5c0%-
&LH|<1bud;hwkTP1dV0cQdcd>`K>2q<?Vi{AKf1+Ru>PN8+L^6)}Fm6g?STQC8i%OcUC2GPa%`Y6=PAm3Z`S!Fe5x6LzXy=k7++F
#B!061vfcZ5*Nx(|45oS-dkUfGkj6S%kA`$Y2!!22_BWcw;A#n>VO|W)D>m=IbZRli>&wdPgz>Vjyt1=d|WE0tVV4Sb8`c9Oysn6
@?LJIe^MU8p4yQoA~3H?%LmNQtRj$exGav=K~#h&O%8yqRD!BKCQVQya4=+S#L%m4Gg{~!Owj;$A4$DrzsLcXJjc`1^?V2@tx9mD
Mz4$7WyuTjF;-
sgM$z%@{6*H}Z+*G_TALtrx=9=iJ8anKYFg7eeP+*!;O2OIipix`q`SBzh(4ZQ^hhyoNqGcfeB=CqkGXen;R9158R=(i6$u7y^hj
87S2q$UdHsh=PY^26GO5tMTHz%L&gA0|0wZG#D=98CDt1=IRgZ3C+dI>`D#7jWy8wGFr~=z!}7UBI<J*EY~t%mK!qU0{v9cq?Fg`
e;Dw2VKCO$*hmJ8Kc##qakSL-~Q+S<v;z0e>T3+EnThz4AeJW8duiWwRUAiK>e8QGVMxs%Sg$r=%%qK-ja>+5bi|~GK<F?+GT;-
;Q|6aaPBU=@FG0jSG6S;aPteMRW~9=&O233){vPC-
A33oFxnR@h=KUird*jrHg5OdvTwjXO!768dc2FUjbM!dcmC}O#sG|0Blx}4jvq<8F^M$+R)Wmtt85*2pe2Ar=3*Kra4V#5T1OQfR
p28E?`CogsrPJ`%sBeOo@-R6$fc>3=wc=j22Rm5+q*(Q*L%b4aY#C9DFa)l<>SvF*hAd8k(Csbpzy!_?-
3x{$C%t8Qi#|C$#$DI*<y{VUCxWkEhki|1F6_(*nNJIkTrq>6?Se^H#|12>kvsxKs)q7Jf8ZHCsLTsM6^Nj(T-
k%FFJc~Rugb~{yVCN)=4EO^2*m)kFL4tca7Ou33tAtnEATCLbO4=G`F&4|MpM+Q+6f9nsgkwX^<o~_H?Q2ioS%{c$*c~3_|5xux&
UQJcd{zY#zHB*7c%trOI%K=iqM<L30n!Fb<Ht5)9f5k?pN`rGsYpyPzFp0Jw$VK{)ay)JXNV5@BUGX@0JaymMaGJqNCzJz^Vrg#M
eVttgR(t8#Q`E5ufsvuZjmVFicH?7L<HgQVpCA+?)s>%e=(tX<@>0ns=FFK+0hT5E+b%l_a0C%eLm*J)ut?y)5F<3Ptx|7xVYEM$
Kdz{Saz+Y|%2eNqs@_VrV0UpsH?g2OgNLdGGXP{>W}rc}rc?I24_jpkaOPKeRw6D(aD^ah~f1xLiVg#n1DY0?`GhrPR31m-
$hG^_GA$ukjS=@$0~`0S_@u+-<Xay>ayTy@zbt{Vd@3_E&<OtMggZjWo!Zt|w6FtweP_VGaKx7GT0o0ALxd+B61E3l2^XY2K{J-
m0XSXRT+YJIjj8BUtTJt*GZJ1eTyvZ@d6<L`Y;8K+kF`8|v;R9y0&&3AjxC=#}T_=@zh)zSs!XQ%B15ExJ972Ha%O9cBf4HCvR>H
@MIQ1xh#L7M+&vmO;y1CWPL5b`T}su<$Bn2+v14BUMnm$B081n)Y!#$>5P{9?UnVF5olIOxpnB?WZDrGd8F2oEAHJFfRgWtb8ax+
7o41*dgtFz{B_!s(1fS;Xh!TI0jQ>~i+u@{(+K8p;TADpqy19*^PGj_L*+8xhrMB&N*;<*!yx1!O=}42We}tlE-
`l06MHu6dNhD4-
yR&Ox(CUZhe?%XH=3jnU9Q8MPxHf2gaG5sZ<R13^s(%d^be>mBv)kcF7XA?Jt(#l@#8Y+PDf|FBCjgXd5)Odd&W1DyL+-
;tE;EfLjXsYD-0`dF<!W&(A|P8_MqL~2UZ`aG~@TOC4rr*#7971w2?_vC(c2uV=<7d-
2X@Y+k%;=gCkMn5%E)04O(V>|c}85_*8u+XQa&)HD7yCG*o(DsGS7_u#H55!rxC2De}s5nFX#|H-o-
upS`h@0Co5B(y^SoxQi^}2W~-4m+D4J2#mw-Mbf64GIQr4|^2W(@OgwUGrJv;;-C*&Lj$k&!=s`3mv?!0jHPYP>3O%-
i)4mp&omUmgIA!F0Y*<aJt;qE@S-CIbloXxEGN@wO;T^O-f9db)L9T<KK?&B2C5&5G1T?&Tb(^6fH}8pV>w7$6>Irg-
9d#bDx?UlCLvVD-m1IvqJoG=iDF%oS=5^|Q3=h(l7<!zyV%l`u$?;a1l-
K<|j5CJ)_BF|!GUXdb&lC*YF|pMVc)g@_vlmFihf!V=PFV-*^hZ{>R^cSZ(2dg0MR!qo5-4BnQfuvTzY4OsuBG*JP@z!?aN;SC-G
dQXJk>xwG);QH0^9K&jQtov?oELC57tiLfg)3#jz<FgxL*~WiBVm!dKhM>R(nj7a5w#>F@W4A({z%6NCmNRp6n<D2xc6}}$5$}#T
!W0lUAG|fzjYg3CQo~1a*CxF5jOy>1U6VHuI2yBdewHaU<xH({#zfXd{0+w>J7zFIIbF)mAQ?q(mD|u8fA+@9@@MBxvZvlI&meEt
Pw^==++~Z^Y7oO6V=3Hk4kc}DB`_W;s1mUUZk6cc%VfYf(4fiv;17cduHgNrXZ~4LK+x&54wSn=Gk}PIj7v*&$Y)*FP57ZU_Riue
zDVvQ<9QOz8|7!P_1-&21HaqkR!JJtp@bpmSdsYgg5PO|ZxH;>@(|o88r~idFygfEw|Ti^-Q@IiQz?9Qr&PjnE2Y9G2!s<TR-
?U@Vt*E$FiS<p*n~U;gJ8CC5h(PdGZI8_2VP=-;sqy*jPk#i#cFcaTVbfd>-
Nq_{eP4n_l9>r@2kIigKT2NSy$Sp<(yaD(^dB%nLJb#HW;<{N6l+_;FcH!wRb^+q>cy=dVEVX{K~sv0TNGy1KbRv0353Sa|Dr_)<
ap4ss}C!BFM7d1`<iqRGd}yw3yF>4({c>-sgvF*zN0L{_dhYdAFEs)IUnGC{D|FVE=nJt%`Yb`c5e^>vs#)!U~UU-Yr)Rz6PD7n5
^4(c)=;WDJB!8B&^>7I`8!P$-
DNvn$O#JT7!AFZl=w<^;uP)EAglQdU*8uVt9NPdf{P+Y8V@4Z@h@=LG&l_!&q@gU>B6+6Km$BszZvox$n&a(Xs=|;&_vAd8{wi7a
>~$b--OfZ4!1AbDMy!sl>tNvUgVlK{*XbY(rC22j|1Pm%4bIAxaI+l#QE_P$g0C*d4;-
14b2*MUffGk(bZs_BO{=v%mv4Z7=ulfD5l-
`cfPFv%(n6$xg27<B)6Mp=G=+W~J{KgiqM1Loc|^&7G3i!#T)%Lx*#4`;$I=!*jai3EiTo>iBf--j&7Y8csGGnzt}x?_$EfnfaQX
%Oy<LJDRP@?)nGV-^uK1BlXw-
&`}o{Gbr)xvI#`mq;cD+k^1CjS~*82Rj`@ADaY&`_f%XKYP?2X&3oW^l$aPSKfG8~aB(!WPG+gHR(}=W9Oaw!Z2wb+cyvO+CzK>x
#h>^R03P1Mc6K$}-^vn2J=xTA#qq<~516iS3D=RcTW^UA34>d-
FCPqM7%q&bpT;qV(&@sGj|hXnv(gTGw8v0Z{&2BwWfgj@!%n?9fm?X~SnU7#@%}#^?EiW^+&{hxdc;^?XC&x2=1V>t2X-
RgtTmQHA9U;R=jd?%SI6O?_UO$gA0K1828h+Hc43)7f#Eoi<dNo{&op-om}ha3J-
<|2T1{)Ms@F}{D5g~a(=sdQp2tx2qQrHOibB_-6rvOp8s`g!Eljk58!wGx0}mG_!1AC~H_Jb>*zN0}j4LyVdvIoaxp)1Da-
o(yIrxot0mCLbSjx@W1~|LD2K(Iq&pm#0?y+6$m|yBeRK8K<beKJbKk?$hl6DuuvUpm7&&OI!k7*xYZzKK}2wSbW0?+!*(u5;_HA
;GAF5L=Ygi@?deS!uDxv^T%Jw%aFvhl)T!3X9qBB@pjlrgC}oP#t4>H3E*diCcWZbo>j>UM3_!q7TuEJ~%y^q{%X$>q8X4)8#RR+
S}p7Hkz>4yPsZKfQ9)?7>jBqg;E8<h!ndxF?Kj*^9E@k9+B1H*=NZlUNLI)iiTuBQ*mbAaS#KuGU4*Rt0X%?0c+<FhsOyl^Otd!~
2SDj&EMKcYCid?otQ)uTSz&w`B-OfyEZMRb!k_k3JH@lLWFII#ei`m);i>mRrqYIBQJqlf-
G*2|cm|bo0|JaIDm5HE+(_FTCXk#t$;FQd}-NO`aOVKLexorIR^cL4s-
d6KVEcpDvV|&@PLKokHq~eN4LyKSO$J{V3E%y#*UvTH*7ngM$NH$oRzqL`TTrHk4WZcc%Tr?8@T8{eGhb4-
Tnx5scOeBXY2CfUmExUvZEQiwjyFs@-B(wY0fGG|Z5%ihe5W8qsT(vF`%6*K2f-
4nI8*d@S4*9rto`c>!QTTYl<N4%Mh}FvAMCFz#w#@mX0TI0X6Lwy&Dy{#<eL`C-yASIshc5btN?2AkU;8&dO^X;uizoqE<8-
)B+CHnsI_1vllllh89c;bTjV@<@fubrLcu8js8)4@~~z>EkcIc{*H7L!YwcrCOxm>oQz7i+T8#pK%S>(e=E!UL-
o85`90zB8z6aLAj%@*sC~v2}ag-AUG2O4y?sSx3=$Pk>8_n@-
*cgq3`I(*_CqNL0y$<!$sLM6gP!UQ?zgIL^bdUDCbJY5C8_$luS0s4#w&hO`3G3A&mumnv);YaNvz9AbPZkt3ct?o+-
X%3e)u~s<wRjN>xu4nT;MO;=cdj;2`$%>6SXeCIKl4l6;c4t(H6wuj?zU2*dAo6C`+GYq$<M!J5UO=tO!vhT&BEoWD30U`PSKItM
qh90AosIm=Jqhu&2~l#|TuJG4uXhJm<XTV}^WUBaz3n!w`^L-
5#=ruwbiGTF~GRPDmvy8;g<+w=Z4P{f5&*Mb(}4PsI2?O{>tSsL@~);P-g+UhV+f=wXCG{G{`-c^EEm4-
qT>exT2zQf@#J3@=C7E{#JZfZ!2Iz4uqs@qLo*I&am^ck2{87;PTu~Z#jE6RodGIT5nOh$Ot@qsNyT!fd+L`L`ZY&?ic&Jjf1mPX
_YaRXT}l0U<+aXQO^Rb&*k&@CE`9JW+s%5bmZ3%sMs_qfr74K3;$z#3lu?X$1HhJ8EgCZ6-
4IL<l@Uk|aPqQH&YmyL9=uu(<Acgtc0YIv;F7*GA6P}o6yk7|-
b7mnv{HZ`7!h}HBhNv1#LTP0^lX@3|(EVjBlEhd*^559iJr%fB6(lc|7GvcjZ3%DB}Rxmo+aSw6aKz-
0?1p!kqTJil`KMf@daRNS=;o=-
>5RuSLYHGuWF&Q`K!NqD=A8Q&X<Otg7ygBLRckWqY?FSCwzsSBQCg&H$YKk_^VqKl!sVp+(W)AVj_OwXh0dXGf5Fb5Jy6b+szMPi
<K#h`O=gwqH&+dH&^Z&?VlU+a|VoVtIH?JlNd@w*5N_xe~Ias`Cfb-52tpyL8^?lGa4e==xh&YrHT&)f%fj7-6=t;ogm&Go#7-
8+(j&xop@6W&4oPBd^RMuQCAGH+_g@4@yH8BVj;ja1UJGcg<D8dL!Vcwh$6*bmMEl?7IBRx%2YB-
g))vPW<aVDYqnb<hu{AbN(K1Df^bA~}imX_cSa4@axXm8Pkvy-I-<#kWqjZIap=0j2=YI{FD1y2I7yOK+7qZ4S+R}Ye?KSlm>-
mb9FUe{N7Gn+vRGr$;qcB|HO(0s?V^GX><pWcJ~x}(ct6UF?ZxTGui<{0Zoe!>_qtp46lK*XDeLJ6@)(`XKV!cOWLgu)3ksyIRVs
hfB*2!d;_+gn@RcE2A98fsb8YgI*w`zD(jxFmbQcOBP4YINZ~PtrK|_xB?g!{|atW<JHQN_zaGs`$FS^SbU0?|j~WU7Meu=Y-
K9o6U>UcBHC&`Q59>Uw<8q970O9Y#*bgyz?r`$z}zco4yc(8}aoE$pGkUbx;EJ1>cg}F4fkBwZplkYck?N=^Z(lT8Y$s@S0Ks)c<
QWDgY?j2P`1btCn?5X4x=0N37Jbr`dP|kak@32hd`~#$k(Jtk({VZV2Ong%PU%+dAoiwm0RfAEG}`64ZN*lSyq@7+)W@92G33uuW
UquFwn>tV*>I6fZhaQqkC#vV{xI*y0W(Zoce&3lCk7#oiNpH;4sM#pZFe9QZJT9}wpeM>^94Ja@LL<B)F{*hV9dCKIj^w#1|r%e~
jIKa!-
gTASOq^vk2;T(81jJ_xoV?%^I9k@%WMaLI*?GzRY4cmq2ptl?ZEvClliInv^SB~bEWwd147SQid_4Haj!lOzwXv7B(SiZeTDPdkY
=`~*&6SHfvzKAo%l==H_F{=5Bu{XhQo|J?tN|NO82-
GBTahWp1?9}liELz9KtKRW#6IQEu1(x5%rT0hekXKYzBMl5RiM!52jzmzRM*5VqsCxr<D*pIQvTiB6Sh8XK6Z*H|dI(%@zZJ;{^J
Nqcvq4n8{z`hcQ4>~1uPfv(XFzd@6n`Rt`#ME<vM-
+@YBy33=|C!0dR=w7WA~Px^gyvgHv;_3WmBWuBx344AR%4ABV+<Ji1Z#K6)~mPD^>KGO<@Lrb<fIlBJf{0|>%FR3q@GFm*rPB0a!
)xd5J0KxF1FwIw%Te=aFhU+ESrW>G;ZPBM9tXAE3}Hm^)Q(@&!Pph!q6Bw&;k3>H5bL(9)2HW_xTAsT{d9qa?!zorwfYg&!|uxhg
u8Gek!&~_ye`sp)rk_!%SChYa5@iHa<Kj|M&)++-
r;}HoJ+5u68W`{j}Qvj{Dd(yxu{k_$A5|L^^&bov>?&f)eR6T;53CV!&js9gpgqfC6X;bcLf9)7HZSNdxrYjD;R0p#6$LJ5#&FT1
kUIDJFxN2jhrbgtiNVaEN6F)=g%_P8zj4%rU;L-7I?dacYE)Ko`wpgQLf2HJq)>a-ll($-
_bR;Gx3LG=4`hBH><JsL`>FOq4QHK@^D*CxV?r5+qhdeU3VU@5|Bi{IbN2YUwtoK5bZWY69OyR2B>3-
PQwx=M^DbJ$4p6SzxIzLW*LYo_L^IfJmcKI3U1lWngk1v5kc9*(MwB*f9-
xl)d9Hd4Im~zD!bFX0`ymF|;N;oE;N68nC>ugG^}lLOfi7zz4tpg2gxxS0jA3anhYB13t2+(zgvmhQ@|uujw#*=D*NsN@Fw~0GJi
bYnf<SpX9k=IbvJgd+eF_Kk+tA6Jy|0d+u^G2WI}m?WaB0a0q_|7+v$rR2@|_BY&WAN}7n|TB%Wp&kVHOoARS{6nnO*&xKTcK818
ylR=LRd;z<BthP*5B+S5PyIYXBpHknPPslHRk-gk~>h#3L>l2}Fb5QmDFu><0B%pSf{k|=;^;x;dF3w5_;+mIlirRQ)U{z_A69OV
Zx!a30v!Q4^Dc}WPB>1MDDif<GFw7fR{1F%hZ#c5sQQdGPS*;Y0f(+4+z|VKN{^Kve-
+Fi#?cu>G!8gDE`qi_qpMCq(4{>H@EDks_PD5AyrqPMjVxJJ6gDaWg6hlqvET;)zVK4NUVRT68w)HQ3Pt{-7oP`8K%v--354iU1F
~|KkrG}f%Rm!!)X=Gke<7;vQpMo$x$d~ehd%S{`V1r&vulsRGQF^4^%!igkbRa(|+7d!W6aMhx9s_nGc^7Afq^JNA7Hb)^kjkY#T
p%v-Euo#*Y#pZ?+r`GU(x&ixc|YWDQMO_9)Hh>2$V{?Od&>y<*WoQAqYT_V!H+-
UbQHr2aV8zHy+OplQLd}y$4pJ2^!0e%My?q9Y9Gf8vV2AZ=#CkGtk7i$TlO9(S*y8Fq(Z(4dVTquwhnUEfBl!bb0htiMU2Uz&Uyz
4qmR?^M(_#ZqaTg3kJItdFE%w`Y9ge6_v+R2?21)~H0<O^`A~@y3D1kr(=tJ7Y@LA%^IIXgHJu|rt}pow(}o=c+|Xwgk$_>|Nbyr
%uY>h(lJygjZa^^!5A-
;Z1*>S5Uzvul?_n>sufJPNqfZXJ7#JO_#@xhJD_(b43K}RZrk*i*hcG~m8O_N)&cxC%gAYN38R&q>YKP}}rkG%H#&8!N_hK{l$SJ
9~s*2N*vMf7ob)dClpLk*$b6u9xd3x(jm~)MDx3A5c%Yt|wEb*>JzhE^@6r;#1uPkiMwsfESkxG#vh^9Fb1VDHP5b3D+)r`Hq34v
}1GL(T?Nw9(gXtsScs_bCM_JUJr)N}xacWs}Z1<VF(S`ek(`v;yS91f{4Qxg}K2^ckPul99tWik3!4@0;PCjxRKa1R}t+l_qw6nj
|_^-TNv+Fh!m?S0XStOI5J3G|FQFfmDM#2-
Agw>jB4WL7{D&<`R;&Q|44hPotAN7g8^(rB09+}GIoddB}&WD<x8afZJB<Fg@vyTxP|WvF8&I|C<evRf)q@DTrf50jk`KkhobJ*L
2#?SvE)yIAewoe~F~a#glw+eEeBn(&w)cf(!Vv-
$ZM2PBfanbB|8zBKDGCWFC7%@M~aJm|pbPnpt;+7_xKA#e9y!nF!1H+qk2(ADvMYd`Jxubsa)U-
g0ppjDM_`6aO1F=6KFPn%|4YP*gn&!AG^sF$CHzA2}n&g=B&#5QWI@kX(Xl}7_LmNV&YMMi1XRbH_DX~E@2EXZW*g}Sow>f45S#p
4|+6*w`w*|DB@zNyfYk;EW-QN`Vwkkd=rSxw~<HxfZaEmemY@yA_$PuurGQMC=i(@fZLVDHIIDm2rczS_-
3DMvIFU(NFoW(3H_R_lCK&dbwPvG@k^M|@Mgt+f3#&vWw%;<~GKRki~PmQ#xa3X^{xWTDtMF=uDxe5rN>%xWVmOOS!jU1R^Fs@xw
?d&a6@_!xir-IJH&-@o{J5NgCXQ*}R_YWpSJ+4Mg8Evju?MbX>_C;f7)Ga;IUF8J^e#GZKWz;LA3^eq2xuBhzLJSFlqF-
r7ukmcsJ&59Bx0uVD{$f78GmeCU%v?|-lB8<qS%W;xTXHms@v9+G)!MW^UFADdl9lVLrv=Nrhf3L4sPn#*j-
SAs7JR6&H@b>q5f>a4Rm2s(OU#j;ZrhC<NPopVRc|4h@C8lKa_Drf<;OjBG?f~*dvz98KH0zE^e<)Ygtb(h1<C<^uyN>G5SLLGGE
Tq~?deu?+<)jd6w(5CDwXcfvQmQsn&pWDpsaW`0?&y?WbyR*r$xo%qIxlKR<!?6YO)<|VX&4JEG2Ra9MG1T6B+-
wRecLtan<d2ki33lsx@jzf1hLtflDZmD21SAcv2i`tWwwB;8-&=VK-CSt?tt=jQJ-##(^6-
ri^0rQ0Zi1>MagGywT!vJGP~NlEZaSaP46wC<etZ)_v&U(h6$<e@ctZeiNN~~oSrV4AF7PDF{yqD@5l7sf{9MhW9fOefup9~cQY%
`Y7tu873pWcBZUt%>x&>HeDr=>uD??6fW5v@dZwac1Fatc7z5{JS;pWQ>{RBJxEa9dq^--
YYTc4^LEP(dKsD37J`5+#P2S@ZB?_@wvj_k~hj+<|cQBqbiv^@jgawdcvgHK82^Pd<*N(B^4$!}tH<NRZlW>qH^mYe0v~=JW%{Jp
<oDx)AJYy_7wq<u{;}6xeY<6tp4V1l28%;GSGo5U&1!3ugt{Y7>1I0~lzIJSj@6ggq#TOx&)v~G~^krLzS}H!K;y3EkbE4A>Sxst
AsLa@BM_t#Q-X_x%Up8|3k~HT)%vy<eV3tI$1Fhwc^J-D8NB2AROK*Ji8p}{W!-WC4Na$7nx+Ce|F8vQ$y5R`8P-
)8JHk@2cF*!rdGO1DvZ7$cmX)*$B=Zc5iCR+5yJ?55r9%3y7GBbjCz;z0eOc-
bh*?Dh6()?ckdicZgG(2L782-{rqajX;%-<isDb~g6Fta-Uv?*!JfQ$)hw=eMCoT3I(+j4U<uO_g9Rh>*}!%BoGG8(At@$+ZHjtz
q9%rW^4ZYJ3kAl<q0a9qW-O@3-O(+MSAk@kQWeJ?o;z9&6v^bIj&Geym~X13BYZC1(E%=fZzEyoVrR9ej5fQ~-
XI8UE`O@b^Y)|5dY@}OXf*(c4%P%A*|)JXY<>9V?BtZH{vj#XR!k*hMBM7lR%tpJP?whE2xR!hZpZ0!7WE=EG>3J3L?Y2DdTH62~
~SaB8mI8Vk~%P9G)hs#~g%TU`{Ean{vF@o)@Xxk_ple;bQ+rnLXDaF*`5)QTF!=hzrrp(X8v5<M4v8=5;trQZF1&%3SeXB16!17f
+-
v7s9|IcB*DpNL{(p+aDj02lkGd?=JdOple?vyQ1?kX@|ZR7N(3mhH(`V(&4E8nhHO4|;G+0h}5by2q$<tiCVF5`}Kg4ZNT$skPX0
%Ux@efsUw7mr^({c`-
(v#+0yUpzJbn$)m1mGcovXKrA}O9JiqX$AU&Ow17wt&BX}!5C|wmG#6>iSaW1{`>EHM~+tRDq^|Q*NH0ByW9*Z^$bo<r4$tiIoN*
+^l0tjE8CA$>@a-D;CvN#X^Ba%!Q~8Z{+0@Ky!=7!_H^=qg?^A6{qi5$j+g7pWyv6{<w9-8%d_=jj<4~HP+-
zhb@(fyr~5DDDa8Vpg>C@9NCnJ$`SnTBp5c4-M|j=+@=pXB{tB-bQ+yjGaHW^U>KtSexyUu1VE`o!G;j36_!Y04&8oLZQ<&pbJS^
y5W{w@ewgK^fgN&1Ggz^J_bs0XYmR%gf-
`%v|nL+0B5W6Ef7Fe}(F3b!;i)vAhfj$k(Gbz7Qq5Qy+OdZeD9U$LJ__|}tAM;EPdYEI}qK&UpZZ5hqgjRbE<x-
AbA?a_t#)U;ItU`G7R;VdGi!%XBt4dl*xtNMLNFYqlCbQG{S^Fk>HgDo`Z-q7l#v*YOVGV~1_d2penyr^CHM5lyZ7AUortKf-xn+
b0kM%9!hcWpWQkdy)9yJbgBc%>6%991lkPauD>vFLK!W+I)Uz%01y8P1UroH8=RKP||(Z)01agOJl>qQtmxtbVKR_`c(VpT6U>np
-4Q17OAUoS77<9H00^=Tdg*1r5W4(QeyXzZ(IV$~`f?y4E$b#3KXNpbKR&XM5S5@Da8%@)ftqz!ztFK&bTAq^suklbN45zhPaee7
3z7?LEuyf3!!W+rYAN?|TXdk~U(|KP#LgX*HccepP>KqEuD7O-j8Q@p5350V?5;qzzDpNi$n)oQo${-
lU8Uj7up53nCXq}T)k4Hlcaf`qk@mEIh#^Lw-4qg4(ALwg0_S$NzY0!E*lSoI-X;-;g5n&ZOii;OK$o8IF!6@N9#4l=y-
dkqwx$OGC1)TDh<l`#m8Xg)sDpc_)O*G1~C6())YPKzL!bFak@coB;UbsKmIo*>Us;2Wfr$zpOww=IkK`Nf5-qxBTeMEGqec-
K9?=<TYeS~%WhVDb=rkvurTJ|*>dynv>HKvx38j!u+-)ODmp6~ahcf38e|2EX0#?isvtwFH5{T{sh#(eLv-ypG13ZP#eW7|d*+HN
{Xuve)&Mt4^ua$s;8srw}#VaOBLjf;9nAQJjO(6;s(jyrQ)AT^IED<+YY>4-
Yg9=@uW?s2e~lA13FCL9~TaZXHkn6{z9q2DUT!&TghT3Swdrsim5Y3Eo<IubHgN^}bqHWwDUvxUK%2=qtS8eLe6OwKVx^+78ieXL
MyTye1)gbY*+0o&fC875uy99N<>>9_?h`4Lb1zLZyj;8x!x!?^pLF9lMdExeqtGk?9tIbRGe&)7T+qicEN;Gx3ibUi%~r*jHd#H!
iq6HsAe29VAVe#F9>EH|Z-JOrZdnJqqvXIU;s}m-
8SU<j4IR@oV&d1a7}>nrvRIfPFQ{z2WcUXTQOVSCJB%TJ4q>7=ALDZ>HsR*ySL4i+;+gCF%{4Zi(_`;NvK18c~laKq|W7irE5ul_
BmKSgcl&X%arHW1W`n*h*#R19|Kr*ufo5jp@9=sS2`V9@cjp^)Sn;h1!npZK(kRq6&j+_$MC^Pd@n=1Ai5lUE#=>WrBB>ga>iva~
(a6CCY9>L{z?le(I^!lc_k6xs?~$5m7_Ct|oA)61d{hpu@?!qD<)U@OEcvA8_)_%<VW&j&a?5mXI&}q?6?K3Oz+MCp2xp!I(;VU?
&C{2fCxK8hEu*+y;*0v<n(uu-
t(ghB%76p{FUFvIkBpU=snK*kxAb8QpO<Z!(kbJB!yHTxlmhPev6xG05RDV^68p9p>9GQ)DKmjc13?Ot_FdEb`yi8j5P`q^gV6rF
Nl*A?n^)B%l868wqNOC!1<M9is)OvMCOn$QS048En_du(COO%ie7Zh9fbDLzQ+$LczYV=_VxLpcG!^hOHar1^*suK-
W$ZZqF+<0l{H74@ya*#)WsxP{pX*m$Z}HwO)~lo0vewz9n<@Hnon_4p`U~Qle{4e`mP-
4w)$a8(N5iE9~nYyxvm++x6}EXX1t}nhbUc6E%jRU&q%<cy##m{lh<9HFT)JQB<1G5fQ*K9EOTVd9Ul|W;H8<EWtsf-
p7&A%aD>KDG63F0*s7#wr{QyQR1yaciBMLbry5yyDZz5Ml+QpOOw0CJ6flwO>>GD%qa>AS1C`yl2~?bX>MJVEJ|Gi#^o*R*s$Dad
Fis(JSZ?S>+scOunyOY3y?xm?&DoV)JXR}Y*Aqlto`CTB*IinWLMbI)J+#<1=ly1W4*7X3u0luQ%2k+y_m7CZh@-
dkB%DgN|m2RL`pLYQP+0N^ZfcaMYR7lZZ13RBLS;-(2a5H&K-bpy#tp}Q__~>w~P50Of)7s9lvkCiUTW8yDzoSargt5CV-
_(^~W|hmrjh2k6vG(v%~1<b-s7pJNhI1xzopAxyCOvEk>e}!VMC&o8wME3{K*Po4RZ##j><n5`y~|9JMM4iHJkB=V?2-
p9+ZC$j!+c3`uy<_VWx#gbY4AMj-AQT$nhL2yAZ(5S&Z|2PK+Xjl_h-bTS}fzfY*Z{wp$ZYT@VyIC`_UE&L{r%$V#NjDgokG}mp3
@i%o{&d21J8ZaZr0;m*5eYmH39r^3Sy>6S$YEq8%8H=i^>0}TxEuVPU!LEK69yD-4laGo+3_GJU4*1Iuan`v{Y$-
D2N3WvC=nYF1+`{DC)qxBQPUI&pMwq*`=4!__BkgFOut@O{(M5d?n9l`2o-
sy{U`)_nOd<kL2@*I?ga@fQ+r9tnvgD2cQHFYch{loZJWJDqLbag>H#i0{gLZS<xSh-!9*md|pQK%mGjIps<Q?wgNn3b$EQi-P-
9X_oTC;XmH>!jd{5AO$HCfEuvLpL=c<O?=h>$~D6sT+HoNp_iY-XT0Hp4Gq)SrD9crB>cLmMYecwPBvVAZZfSwSUtae7Ineg%r{6
;X`Y(`mKFcsvtfrkUSJ{~eH1{K&KyZ>@IR%5@ylZ|;d)H_aSf*CV|}Jv(Haagb!Bj*qHmhe4OD1H!y4mp$eVkIw9hE#lwqR4}Fp`
gwCckn5|MP}V!E@ZO8Fa#e;mP+)XtHMJ=}unS}Tw8#4uyX)(!ok4g;@T0OK4KEmhMu%j&5J(~bBRU8B1Bg(9rvz)adxF6aJ)B^8_
FfaL0~>qzH$8*cj)%7BVZz1$YKXogsc~TSp{{3tNbEQtd;<`yCOf-1aD2D8E(G1B;%?<*nh7^dz1&2QntVtwQPkUYlNC5zd#yS3&
--yM32I@Cccp7FoE{}&Z@oT9BTefeiU$cYP!NnnR0qBMIc1=*7~M1jg{}A_XP~g{yl)1ISx(s|Sa3`3d+IVKr0GgAMasiX>Tke^W
cfWiX{IKj;&#Ra$zVeXUT4O1Ql&|E$R0Ta=@m38F)@H;?z9VT$i2#~n5qx>!tG}pzq5DF;k9*2k&3lt`0UOEBY&vB923+Sg%WBtj
YyE=9_KoGi7K$4<mee1?sUF^?Dx+Glpz(^mXh;YoUmz8pO&j;)9%AYn4PLu^{JTTNO8D}G5O2Fr4&t_(n1{>x@Wkmh+6G4G<*cl=
FKU)OOe%wUD^xMVcJSLFP3Nmnki9l?Q5e9#939JLn?o;lY2KdrYb<2Qy>HMkXP^V5;&$82j&zKtW6F)+!hE%rKq>K^f@Gs$O!)p(
h-}kj_fzT0FK)T|Mg#}!5gXn{fByRM*45imNzCN|EGW!jK;`*W66-yvfIgKy#``)$`sNEM4Pb-
$dN?Hx@;=tg8>yP#%D$A0aohIS~{GvS6ENWlg(-3==;0J8BsdYc=q(mXRpRzefQ#<LmYw8-(XfBgDL#PDICwsdh|C^0E-
>F^zky@UaTP|wnK0a!n>z-
+4Z=uD~v^t?glV8>%RlCE#lRDBZ@!T>8$G(gZS0sufP7{@sqzD!)W>g3HZf>db@Fy=^!!YF)i&rv^WMhvbrf6VATZ}#vt^5Cttm7
qZ*Or-#>Z!{MEDXzICICzHRc@b&Q+Bq|4bo(O<M+Yx_0Qe?RQKlauWZGhUagMO9;7q{X6u#K-
ys5PzlOk@RcSh4t6n?i)04CHdOF&JzzrCu<%a`?|%5SU3XJaCrJ})1xI`JyFLArxk#c)j|Q;htq`PJ4dV8F@00d?)5%DeBHkL>vy
m3^n=;zthc{kH~UMaxR$Fo<^HN^)~`>5`t4@gsM5D>esMl)p~UcrB0i7r_CFWfnNDAy4DY-?X=bB))AG$dp-
8Vi+pNK6_ik0HSzW(d!jv_$*}Jo1zU~WPAH8nxAhcdPMU3CoZx-
e2>D^lW|84<?O{;qx?I<ZQWQcb0t9ph8W{&MOQ1BGQ(|9sD@oKfO)pj5zK7~@cFQI6ueXK-RCb2k~J+n6u$`N>&4&PpC&o5Su5E-
jYRNps>OK+Deb&c9*k>0kXFx1fsH&~6LAL&{XTW&euoL03hh{;^=5va>pFSs)WG&HJ{jz%B=cA}UlL9gJVRmWsh8%YU*xd(($L2V
E7>6^*WS<=HQot6hLA`(7f7XKIl;f?_K;Aqbk=LHcotc64oUs<g&XH|E#n6N5;rHB+lQ=PWkUbgFUfn)5=F?$}*FRv7eZtUGKF|J
~SDFn>YU0N{RQBb(iTVZs<lMeHW7)0u=&UKf1y}n#lk;`p9tqRz~@mjg%3a?M=DuOF0iofI~@RDNjwTwMlfUA1eh%dnNp_)|7qK>
0qu|P3Z`?LHCGUQZvNGreBNnYT%LZ@x>3+WIbX+qd5%w*T~ei02Qe@m&DQYCmEny3#HZ#MLz&r*fR9Y0Y>UvUQ0mv{wqn|Nhzdra
2U`LV<In{_pZgtY7CysXvugRL@A1Op$=nmHU`r^>9<(!`r<7pioO&AOR3idLdd;B(5oDZWB^TzX-TDWrGvrj^0r8)1d$mui7TZ?t
|p1pU?vXg1#%w-
0zs$F6GM?0!9Zyo;L~(t)@(3mvm&es}=I)ELo@&CbryPsOn7(AUPwDLn1GmAHLXUNZi{$F~{k>T$w+US`q#9y7{!mcX?a8)zlVEL
;GU*e48c*eu~%0Bv9HEOJss%rz+CjP7!=)^I9`zbFpSN^8r$lh>DhjaeR(Z#Q-L-jV)fRjJ)UX=jO{GTPg4wTaRn*mr9CSeBD`&z
)>ehK4Srclx#r@!hI~6WsJRUQfpf2I7@jL*P@gh{T)BJ9)^>TP4_D6sshDN=`_k1r8vac@pw;Rm>u!GzrDyh%bEq2(bt`^o_|Wpr
Zf=ctofvF1132HC$|jF>$Xq^_BuBMLaOPdiVSDDkgLG8eAHi&gQ4(mIBhm@#;VmHe2WxmhfL6U!nJqssct!`(z~Fqa>Vsd(y<BSO
8f&#wCksX?$GOZz`deAi=`$>BGOoTg>vCe4CmcDxmft+Tlfk9gtFjT^)^}mi9r`uim7TiA~-
8UWr1<cb!B7!mcPtX?Zlkwar_|yrM+*l(35z%h0iBl>G*Rq=qIV(wO|Ux=P^P8)|?BZi)ppPg|AkX3nS3ZGR+cX`L*+`$;=gf`3c
QHO)~Ht2(vhQj{(cm^}4~3702J8q|~kO;YeE%N5P%qS$OiY$uq(O<gFSc36ueJ1lSOtU5iD8za+|J&e{mj&_Mcb%0$<8Xy?RMBp!
g(9|oBUZTTNE!vNLyVQ+NOnrNzeJ-7v-eI7&o`nhqM^qd26+fFzH66k~AM^9|dDDRT&v>ihdH1HS;j9o|F@0dRQ6s1jG)2F{-
$&3O_`XAFlfsCKvbxN==;=mq2%*%~Bg7M+P)%14R5fjs@{T4v^CtXa8Ut3McmTf^dE^HkTStfYKRq}&?uP?yA<XhCGxo##GxEpL4
?L?EdEguj5Ap~Up4J1T*Y&^s^Z%7yc}-lmTR<}ZIjy(r8Qnqobeg_Pmy$eJF@?jl3%1d{&rlk`+s7V#R%B<ZayH7>r-
%3M;SC3$SJTla2lo#i9NhoagHM0;t6%==*9Q-N{mcB(fByIX^51`UuXvO_(YM-
v{<==rfAGuuzxw5aPab~y@xxDl`Kt%N#`^yb>%Ri>&aR-
N*V(`Q)BkG6^1A)(9z#xncfTMVwBj#dOz*<_m%sk_lTQ`qzkc}1gHJzxfUW-
D*y?8|kNyr^F)tLy%uY%?a=?p7RGW{wdZK#&;NioA`wt&H_~pST4}X<E`nP}ir~mXH{+XZxuYGhyMDW=?{N;6G&&~rV=xY4URJb*
1!e2~KPq?|k$~bh(C}8&3w0ST19prj&RS~|9Jo4?!RgmUYJ^qtzD?_|mEle||yNTuqoynt@UqSLA)kz3jgv;*m4oNpM)(gQur}KZ
o2Up7%SbRv4Z}J(pc(t1cq<hI-
mhIR@_$48kjnUqF*a0b#8+jn(kG$6GQwWvLmgV9~d2UBNWWf5IDFJqUIWI>_dQtjiWIj)z^HU9Z-F%=CH-LV!0Y^Jy_lT3Ev3<bZ
d1*%mGR5h4b*hP+O<-AmC})#|`vEl}yIa7=oCM2B`Jz@xnutfv1fc~HaLG+n$Hfh@UmqOcCJKLju#sEH_H=*Z0d9BVH?hhLgz3-
)af`$?Tq@a4(;ywFhJr3esf=}qFu8HvNXmsYYQ8Y5DMmZ!;XfF{%A{96j=~}XBtj=pzCT%yOn=NjHikmO2HGKPpsc)4rK$zBOEu@
l88EeKIE0SHgTaql@tRjBLrA5euxNXBVueZ$5$lY~o1>MIWN+xIlzba5+hoCLIm<<54rvEkcS9|e<dFM4rlF6{*0p46%Y49*wz!7
8$e-da4>0)P{S@Z<Vf2^x>r*oyl0;f_nSyC`i_4{PK>Y9+B#FqOmMr3-
OfJ_tj3_~I@CiLlZH=yo191z{vmX+uE$SktwzSD(4Sbd&c*6$$^!?SDuPve!M5}66Oz#Xf8dR*xVJUI*(EECdrRr#~pVEW?yTEQ1
1aCXqYCVXgpYf)yAa6)`*K|rYrBM{*2a(kp78|P`@R6U|uI(Ttn-
BOdb{3$qGA;-Hpmo>evT0&9*+#bM1Lh;|6!AqrLQ0VJdOlL3R{UazO-ko)ZARhxH7{hQ;bXgt_pUd*hh{~B<F0wLAa`==jDV`HB2
W}M3NAw5@yPqF4R0xj&#k$;UKooOB626^z2GV*F{lUb@QV_fTftn*;a2W`p9I;uC0N6X^TuMu7WM|!{nl?aPFy*n1GZkc&1mTY@d
ed0h477OEc@<nJu;)FFtGc^&i6^u!(6>ub{US*);b=?#f(@?B|BX6qk?IPrIXsd?K`P8-
P#r3A7~Ta;0<?&JAQIBw>ab9XlFK+I@CUKn-
o;ODA)}D`C9G6e!Lkz#{HSxq4$xffeEWk9^E}{=0UvG9dGn>v1aB56H~}2)MFe<lL}r<SN28GmTuX_=NSs*7sccp+%kBwvtnKqcn
zpxPDS0~m3|f@>|-
_4S*0CTY~Udiv8m{=B<vJkv2t9r=dN4>PQMA&*c1v>VdGsO=X7%Aie)uEFE7)lLXbKb=d>L+Zxq56+^g(jLZi^PlTwXR2_9l4X1R
KzW(w@$M@Pp*6=Kkw80>5Z7<3-GbE5(a9DG};*~J@v^V3!HC-
^%p%Vk@Z=kWclF1S8ZWn`~*F8IP=+k}v2&V>+WjZeJ#%xK4N^!N%@;&B}b&x9@88{m=uGsOe=Xu_E%Whj$RJ;RZqvhi^I>^n^%`!
6;%a03e3k6D?u)t=BTrZ`6Vz$K#{u~ddo;rWa2{_yO}r!QVI1!c?nMP9oql?YImlQ12~PqvaZvyMW&qa{pxrXNq6DvL%uxQKZDp<
`(OQj7=MwQ~h(oO<BX%>kris(Yes*Uq^GVK4$i$wRs<pby^!tz4H>ZMypeF3upAJXnQxk9-eTaAG6jpEPg7F-
b0UL_4+I&2Zjo$;0Oc%N{<W(BCbx!ACJic~B?;s=i4eAzR??EmbC;W1P=NqkyVn%o7$w;9xO()nM<AvikxF7`ju`k8wXUOO!+VGP
}}1uJ2v>s0mjNL)tUL61E2e*`g-BV}OyIn}zYF?M>WT@kIRC;^;_BAbmKN-L?z3_+y8m-
ev$H^4eliu~P$yNrS=Ok~h^Q49IQ8El8Q90No=6pB^lf;i6G<+0@mfr&ul9F8X@f^-
uCdiSjIlpDkl?gQNr=)P(l!XV_BAb#*ybx_EKf(^J~#0iQUSN@Y>|PC3Vm8GBNEr>u0mAkKYpR)Wl$6<7(}O6Jw1TF)=DW(mpG>v
aQ!ubtL2NDqNGw|Y894e5pE)t~W{2Z$(&)zt1eQ8-
9<be;w4$(1ZF5gkCXmskh<Xk^J7ZB7`r=M7dL)jTvUdm(*JKH4EbR6r43PoVQ+^rwe{jR5WS`z*W^Ni)7~k_~g@7XzctuR?Z77D0
#f;)Dn_Tns@S3o*Vm(M-
H%UO2%g@E|2z(m5??&06&GuO!yVhGn@iOcB%}Qg#cG+r`Em<V9Cx0z@|_Ny1CF<|I2?%Uf(;>d}J?hir+#bYwV+Y>h!q9UV9irU-
kg1KX*$>fG$CHnozp0znJL{xFk9-RDd52AoDy;}%Q}0=B41$!6?Gcrvb~2+Zu@0?r4<K?<<-N<+RrHr%*Yy$6-
Kk(Qp$)#PdyYY6-
lMAcY1%YSPtWEP5iKN8=>?OO2tWaEBHf|TxetZ;&#Nc5C1h4?Kh7cfwcK_lzv78~q@3(eV8GIC!9OX}{s9y@m1w58px;A{-
i#8@T)cS+r+)UjcjYv%XiZ+6JLEPoqh6eXzsB285_<3WP%qmLCiR&wTjo$^nwF#tDk%%-
nT%ja{yL3Zn+9dC5$J37W1W2uTAU!_CE{(r%xs!*txWxvQKo0IcOt;On8Z4l)VhCbJ)`w$FKZ<g_?l;0DF-BDFf%eTh^MoxlrK<p
}j)dqG9%6hZFKnFg%wo->9mr`+-n{^wVxttatq4e(Hs6<Xlo_+N&LJlh7FhgZIV*;Knx93Ah6D8deYG!0eEFw4+>A-
cMNoZUe{94HY%u~4lXFDYncVOlxxJbxqJ(vx5+Oq{CxdGUEPmiu_I6`0@W+Hoiz|CztseFI25oqg8q=|~DT{%XDWJ_n<=_<RcnQ1
mJ+A}=2O{QK8Z-
Awoh~d}ty|B)ZYT}~x1D>E>GNJibx58?K3$n_cE_zK`&r;XNQhrAJ3v|Qd06ncitCD#9^1G%vf1)qXjcI%2Q=y~85&el?;gF1EyA
r3uQF>G5R6R=XqO6}ITwLrypfGac9PuAP!#-(_g5Q2&M{*<gbs%$xk^SZuxM?;$B%G1^%7i^hBAr!r)t-
fX1wL>aZc(=vk=gl!EEU&x6B9^nL4E+&aw=#<sBLW>BR8fU<^6F4_e}3WS4}&#P|N=CYs}W=YJAq9V<DGFVN2JlDZFiaITghw@`2
w}<ZHpec3Q%`qC+@{C*`EeEEi8h(kPPWK?_>-
(Yc3>XuIk~MH0U4(Nj!o#A?%eB&n0bEZR_%*wU$}wj@Z#J@1L&eBu<82zf=rXPf;=TE8?@_NOs<<N5eDD&vLIWCrOlIn*$*5`U@Z
By#ch%5;$)TjeQYBSP~arbtaF6qA*3<CQeATX2=C1c0Tm0}n=kE>L2SX#}fqmDc0b4w!e<IbK>&y3<N4h**o16G<Ygl;1B4f?dCv
xcNkA*XaEANHoa4=J1OvJH;UyN9#s&QLMnpQ*xv+{v^gmXB)^ilxN$u{x|J!vh%WptXrArR1+g7_ydY>y7ns8`>4<Q#LP~d{v8KQ
nnT@KMe$81{!w<_K&8CTv+JRdrtQHIqVS6NTuPMmS3^>;^wMF6)%Z(MbBSxPmnpp=uH?TLR0E6vZ05l@xc6=p;1?;)<9W5H*7`X3
{vf<*TVJk&0O6F!RRnwTr+DuBDf1YZmc^7@sNmdX+U^9{R8kP{e@bye@K=C}7l1_PFL$G6nbxMdc(R$2SNJ!8JshBaflqqjFo;4X
KWUC_pW|Kq7~m6_IB)6-AR9ba<)Wy7pQ!SDp!TDI3U@nK^RrPV-
4Yfr$eDI&GYz4Aq=d_BP&mo1!kM^k152kS%kf23Pn!$L4*@<84nF=gK{Gx8J%B(upB(5QGy2xS(R9MtWaAG%+0wQK;2MAMv2Gi`b
Tm!0SWYe7070*+h5fByYJ!as^9W9KL+U-
e|6mY~@xJNsE)Jr*h6oC77%6`s{^@qeh(_lYo*6r8*A~_`9hSk}#cB<oTb$Q^NPiN>^oDxo1*Z~0Zr5JsmM<j5_nrLiApMWIEYyk
w;!UF3)WSDso>n3hq&ffx_g{;E-
R5wMOP+MnWHtHD%;ZzL7zODz;Yir_lphVAkkA=d$JK0HBa`hJKWVp&%vzA7TV3Dw&%lFoWxT*k3W8#mMh{g7On*Dte{kp|r0#7nI
%SCO%*|KL94|{HIY*FZb3Ln&cOfAQnU77LqYDxpSaJ|eTfu^G8E^vQ=AvBCIFN$J#4pn4+&L1JG>uDx&5HS>ZHCj`B^wS89}WhFT
`p^3Xw$u(H=#h(2<5BgP4G2$?Q?=?Nu-VtbTclI7FA>dg5{JtgLj-d^sL#aWv*45u_-
S)HH*G<<}MOYTCt(o46dmXxZw`=&p=PAr?FuDXp}t=mL>@mo0S?gHJ!`d<Yd?nu(X<*Pf*(UgbB$=1gmCKPo2QacLMjm^@l4Q^il
XAI+*uRAB7JBGcsnZGR~rcf7OHN3EN%bckkyjFBt38n)Tfc`vYOZ?AXIhg%^S0d_Df{({Epmzj^%k<Cm|VK7T1#xB28qZB+G}VqQ
^p-7&ajRVW@hr&()($^APuKb#B0E!-
E7TDGV`ADsUalQneebNO3ycdsK!t{D`&Iq$Ty>8a^VA244NC2hC43gICYarm9A`Q89|Mpu^9)5k?Nsrjvjc3AIi$`I=p`XH8AA7s
iDE0y{=+hRj}-^&<lN;ASr5UFY*A~v4}qq;HKg5!itxAfQzl-
5a^A;zzWZjF)fV6wmkV9|ONaiqvKjC<T@{opMeYG}7agwpd64NQ&j0UvxQd311`xKIT3CqE5)iZ?;uw1Y+Rs2sgf(k^h|qv8hP=<
xn=wDf)!{&3XIfMfk^JmR{o3LSQYAH(y_gRiAqr3;*xyY^@(o$AP_gI)zu>H(#h4K5)`>pNfVk|5<$a<?#_WUMc?-
hH20$2`JEo=f;pXSRjb__|rR<l<o(Lx3zeiK`v51^cU$0_>YWQ;Yb;wE&h{G%(Yml5njEzIW~Auj|*f4)Y5;6mM&Hsr<Li1qk3^*
rk{hB|B$|@okDZxv1qSVG2H>WF(AKe}@Wg3<CPJhs#OIj7Q8HH8wSJK{kBuKn`OF$g$~l9S0M!;Y$s7+}d?OeY@CUel8rkYjd{S@
{Tfyzkhmr*%<n>f}n|>Rl)i{&k<Qs1<cOOEtA1>dm%2zF+Q8|E5%5Lt0t%*#QsEf7+@bmU7nBo?$aBuOe0(+C8kbU$%M)1kPdl^#
{fm!gr_v)4nzTr>2`Em4wmeMBWmMfY@#^2vz#?RiFfJ8(cyy!2glcmRGAQYBsKgfdytO(ORp@~tlV5$jZJJ|-
qy7n%p}?}pEjRuyPQ|nAvnv~SYIPQ?yP!O%591hKzSc2JdR8YsjE}rb1lA+M`)sxIY%$io1Uq&+Z_qv^Whi|e0E_z@cAi7XDd^K&
sN5EqbY#hgwF!ReSpV`^?Vk=rB@&a7Nc^aH1>0!3#N>Kft~JR97Zw(N>Vz6&U_rF?N)#~T$!=x?gy?r9kzaWB?&$|x=2fEXj<Eb4
@fD!w94H#Y8Hqge^%?aYZ~~xqT6vbq39SN$HX1f@2B{&{&sTi+v<Hd30=CM9gDR72cIoEAbiq#pzEakUNZIha*@?z=+JF9wU3s6x
1JP34uhcP^X3BYoaJhUsLX*qvcAO7HN3Obw=eA$%qCEoMd5DJ)C!nAUp1$Yw*VZBAZ$y?KMJACW|P4&cD86%CAQPTY1d@FnJVovo
2eRSnTKd5@7%f7NozQNw;1af*G)Z#w&6X6WdR<A>K&TK)Kff>(o-^wn-J7ZUmx$V^qT?Nq7nNrqp1@O4i=ei-4{M-
xoT$}7z^*92M0QDTGfS5EF!tC|04UUQF}}V#(0{bC1hBGsa8O#RnjfA=)SLb2?Va;DeFanlMJ`V4K2t{IrP1(Dhb+uxo(!(22;Bs
c@MMSR&Pp1a{zgNR!k`Q8;Tcob1|Tsl%Y51P}0=%%VCQ4zidz((OZh6{aLAYv}uNyV5oKV_uqW2sQ*-
b)AnGKS}vY~lr4vyc!k~xH`D!f2qo92#hf*2V)6DToh45nVwZ2viVb)%=jO&DlRqS(xbJ9lh^77(ZZW`#%Gt3x%5U3c@hI62Ad7W
_k(++7{BIFp+L;xRwPStJ3MS!453-
)%1|PVbSZ_1c+rSIqD0gr3<A`C|(&KpnUK#GrU2<R0yv}+{9_V~gCW8>Y*ly#vEw|gEL2g~yw%|V~K^W2|ys6;Ub-
s}x3j!C1%j~3_D2k<Z@8-eKGnO+nom%F$!N-
<M0JVI2Z~!6{m{iIYo}a;1H_V=g%;VcebD%W%TkvS}L4zB2G1TsYiD0G<W|73M+y4_w$PSaej}LzR$$%5{o$SF*`OVE|_XUq7J8}
)idSDbZeGA5fAY5i1%(H@($UVFi5`(-
{u;wM?Tw9l*$!P5kC8F|eIoYh?z?Ak0%G*LI5~@P+5=;jYpsiZzxpXxouNKRmhuse?G9Qpwn(@3mEhd*i?6=zDFX3v|!_0RV!BSz
MrVYf@-tk@spER|ifwdM2FS7sk<#*pwcND3un@KaL97BW#sSx*2<b@$PQ@x!-
qF3Himt07?zFK4ME<T|<!o0_L^<_VC>?>@u#wLl4n!V0>6VgP>xre+2Q;>@s^dpGS;rPIF!sp7r-
W!^7*^W&00nSR$9)rz*z)0F_-
@G>AP40D(mDSD{aXJNvA*!TMMuOKNn+dOkD;)8;d?%%bCf&=7ujm?X;f1yk2G#^Iyj6G4jHS#ry)iXKaZo*PU$2U1OwuWDbQoeZ>
MZ)uzVpJQR^3hpczc?L==vgGPo@y?+tzaot`9h)Lbh_rKIf<9qI=h}9*`-8Y!8TG^o3zJBMDq-INdCkt*Ni}hz&S8wUeqE(X~?ka
))eI6xFsWhwbL1x5|(HSnU7#@%}#^?EiW^+&>1PY@8!|!r3v4Ts+?}@OJDoUGQ!W751)7_3Kf7#qXAbw)MSo8Qy|NNkFdiy=c>6h
M?T!fW>C|WU}JPry=6ladN%3Tb%(8h}Y(Rll=ZXCjA`l9zX?;v1bB^StSud*38U9r~QFk4@LoxKZi<*0j1}d@C5g!U<Z#BlkO{{7
};CAERzc;Qa>eP?9&Q6(hrZrSvbP02QjsczJt)h_o2dT&5V!P)WEfen0B#RR@TxBv#KZOtSn5{-
8gW}rRFOXKBo%Z)ur42Gq{6Tz4=|SS~T@#_WimU4Tr<;HB3n7r?73>77|K(v$8-
F46T$B?qF7nrT6*aAK$%h`wB?!=#Q`4&yMf*bAw-aK&KZ8!V%}g6Gn93(R&*51>)Vaz56ab9sSK;=X-
ga7ElW~k&gv#=y;>NIWhqy!roC2&voXa@DgBG(G<8zMbCr{HGQ*PSC!$mD&CIo1`b#^je;!4(z_#D;aCJSL_2*8%ax>|VVs@ZO_l
wA^zblR6%4fi&sY@l9sF=nm;+~89PHRxr>r!Wt2vG(CJgiz%2R@wJpq{a&=U5{E)BfRg;ox7HC#EsbkLH44Gx_J`DLRP7p73k2o6
uik2TtCN){e6C6e)oY&+lE?tJfNK{1KdW<q&@>nZ+L>q=>&a0ePFg!Ag0Nm$>1_73Oj-
6LxO{Op~+G5*~nePmWBUZ9qH_Srj4y6+xcso&SCq-y-
#qwk%K?G<DRLnN{HC*}I0RJ`GPR`q*C?0Z`oY(It0GKm8h@>ivuD3%Da0_i5D>sA8^6~KB18E#=C!=~}LkI$Gh-fYVZ>B}`s2vb;
r@&{b&`DetU9u4n&-
v8{i>Cx+VkKi3_l=w!mH}w))Qg7b<b>FoPyqy>#M)D7p3J2G*f%bsy47AD)91ya24Zr;E)#I<f4wlYLK|U!a=jJ+R6DXGA{+tu$)
Pp>bL`Z=53X-5M9x-c{EJ~`P$inwD?WB<qBNR+oMD{yvGN|HK80uW^87W+e+-
iuB;`Dd!(0*#J`1M+ftsl<9YDQktYyGQrSwC!b87VT#@?!!2njOs)DY;<G<s2&S$K-CfOpr*H6rJTLSTvECqTUX1MH45!I|_G>-
HFM-
6A0ihJBuD4z~*0l_ubdyCu*&afo+aoJaxQ*4QLpe6E52OKa=(Pvs@!7zc6WyBt>I>U_)+aDEh*tL;JgqYlHj;wQ=2W=PjOS{EO_X
YNZsM$yqr$2b0&7!GXgZki_+tXaWyfNCe`Ebf5pFsOp0diD*wVAJAZTVes25YUYzBHbNsh7nkV|UV(Xp!tSIJVElkH6N{&4X$ueu
EN-H;ErCYot=|SAJz~%=#Kb+Li@Jp%A^u4ZtHvK#jKOJVtlbciys^!*4L;z}GM$zzOh2*vnYLswxVF?bHle^C%pq$agDoE-
bYfSDIIpelK7i}!w$97$?$|;2wq>X-qe-YHGP&{3EI<0{yBFU)ew96a@#4D|$JswLn{3IC%6n};>s=u#*L{(hY(0K@byi+xYL%7Q
x8J?8;`lIoS}3-
I4J|f`rJa<D_}dIb^0tID$Llit{(GjceE&V2OebCEZHv6xw!(W?T8Im^URr>MS494Y`6V9P!6Df`GD3WOef_%L+ltHwMR>M%Wl_E
Y8c;-W1iru)W7M;*KM-
m!z;zYR4$))AP7OH;be#>l&9%4~qe(Yu3;s!kL5q%&2dvB&V{8I=Jpemybhp`8Ef8PugAEo#7|cL=jfvMCiIz;*RlSls-vfl_)g^
56V4ydaF}TgOP@7M#$O!Gg{iDN&2M0nTZ*%0wjwMCP$(^VLmyQAM3NqdLXzzS6*o^ewExYyyGP#<`2raG2RNb=qwbS=ka3jaDP~g
VR$q(g3az*}`NJTd80<UwC#qbV?=^GzgTA=2-a|{`2z}L4I*Ohn5x-3>@yY_b3BuAT8vl(2e1jp5rc>{MK!xAqOq-;Lyq{N{*$m-
EU^<cAZX0y@3@Z*O&Fw*T$i#J7uH@o?AgKhTc@RtY2a@Dh{j`I-
lPm(ri3{`Xb+erUS3nxG=R3=%(m}PhG`_4QDJ`8`I6tly($Ijqr2iIa4#}WL~;eBjoX=K0c>RiIk&UaK5Zg@CvKDQlB1kTviKpMR
*opq-)+ssv>Cccxyha6)Tssny@U~VM<QC#~lwd{hf7~!{z`3E{f&=v*eYy%#e#`c(L?|-
~o18fb=YFgD`hX38GZ@#`~oH=Fx6gLu_XWrJf*CqYzWKe)i8=jEWVG5A0=#eSa2boHt=gOp9zId5m3T48?9#Z~|PV{*LANL2|?}z
Glz!tsz-
~HHOFZZ_HiXG|;LXBra6Ju4(Aq4h<THo0U?X8jzy{dyH_#TT|ZCR5|IW|f^hw79WM1Jd%!SXj*{(t9N4KZwMCvzW#vSjUMHG`b}6
+cY;hRzF{$)sqN{111U<GG(d|6D)yUhJwoU%keHuk%CorCcq*4{^BK)UWfwYb>kYs4|nq6pPH&@9S&zUx<a%1l?iY`l5-
{((Kh))n<!web!7fnly;!P%@h{*!Z_CwRjA8sW#Y>9~t6+x3D}QYJ8xtoMo4uVTcItyhCvflmO>Vt?>?2I<%T2b1t57+lvAMhoBg
L(7I{v%V&~0k<pDfax$5V5GPIW?P`~U(&7_?T}`4S!1NfSNU9pY$R5wt+@QgmTr<Hf3FIK-
l7@%8;53~QeUk2RqT<YlY&ToA9hVNvtLybv!z*I$6f<jlWeVIb##i`s8%1qnv-A-
0PaJ1zKHW}G`~v|w(aW8!vyuG*KInkFIMKTieADr0@YT?`X(Dm1JF^f3`)yauythm`v55CVsx54WKbE-YVt9Uot`_&u8^yXeLomV
$93VZhl5%hlBaet1%Fbq66<vf(<Y{tq4X$RB5s3VCesT<U5j1veDUd@_a?=NpnH;H5kQtmWN<;%UMJ(5J{-
7O>s(H1(+<`PcjPPah8r!gM-Dm$QvDDqBdNYWk?_(EDn~OGSuQpd$5;s>MkGNH3(roaZOY*^NxKQ~1VVE(E{7L{=#NxnIiLXbdS?
NR`S`_n&h$c7NLzigeN&~;n?qpX8?>eW%yZ{<*yd*lLQa*}qH~`b2rEn}hVB3az3`9mNmPW?l-
<&2C@6>(^iEuJEO)_7qkT|9L4gH;ehGDOtq0EZz)^Ovlk`!UxJ^JkAk?)($Eirqpe|VSqUcZ0+*}aoT;c?E)_wSyZt$Ozl`r0aJ`
apFp5|11R9*UC)3DiM2Iv6W;i#Mq(W~}g+3nq+wYV}}w+2M7FBf4<~$1woSJMuYQuJ<2?$pBYE!RG!>rGB|nsgJ$m8?G}3d7@pM6
(>G=DFzBfshmTQ7|=PJX_*ke?GP)ZhgmlaGLZgOE4@xt2dIm3T5T{>_*r#&hVi5L<ysqPp)J<ew)7%5HFe<kFhI*(NG;HgzdvDZH
7@iwiagqWhd@=kz)>BR%Hm2X=H?Z=eFFR@*Kwu(jPu~r7=|;jZ-KLJ*2UZh6LD+?7mJ4=z3$xgQS*SYAce>VC5%ZIA~Z-
Q_!iM%Z#gjC?F1sJvFvI);yF?KerWJk1a3149`IYtfE?KzM-6yGdFZtixbFL%KJ>AO-27P=4!r^3-
u?JBxNp~9hGAUHJMP|f%h)|m=JZB|h25#EZ}akNv&)WddeM=8pUGhcS2n@MdUSL=z@p+Uy)j=tDcW+pS-IWIJP@McwE$sCY)^|m*
|h6sVL_Ta*Df1A+fxV!wWFKT*Y_Y5&ONt2TDNm2qGDr$!;Q>lLl1W5fQ)Pg@54lFbq-
?<DGn9txxS6qPXWLS9QUQrl5lTxnaHC17WlYF)j*Gj-AN4aI*PZ@V~i^C9}2{$8HPZO_QH_vbO+$WvQv(Q1mXZSW{Jlc&w|jw_&q
psWm}#c|ApA5$D8$8v#S1#+3hf2-
WPD3tF~snjIYB$qbC$wyZ`EPNx5T|%Xu}y`uE7mBjiKyalB~RD9)*I@8Kf#2|GGJ@|S=2ZLxmYz*^=7+3QQK0U5x$r&ghjKsV87?
MVM+S)U?HqY@Sho6f-RoSVEIbDp4g%vj$eWSnFop<0hif_~6O=HP&oop0)Pvs|J>Mesfy8fyZ#m(8-5Xo|S6=t5!xeA9CUpA-
#ab+N`S!)=FCJg|dLoEiqR_H#6Tv~m1#22W-
rf2ncgo5TAKq&I*ZaB2j1?HZvPZ65)?poiHqnOJ5E&Vr8jzKF{gLGZbV_>{f@D^Tm8NfM6ncitZeH{>F8ZSz!23F;i>le4CpC<y{
wR*!7@1ohP<UpS66R?P={e_LK66C7mE>S_5_e}^3fzxGAuDBeH$`?`F)EYW^*We~pxd;C%fQA(`50%Wh1u#b_L3Z^I;ld_qThyRN
gd?lNWQLqK6G!TyWsN`P%`X0rk-
n+uT*M~Z7cBw^z&sFC~PHu3cN%!&SZH*_0^Q}LObja}pR++sX1UyNOD2LNAS_t&bK!Q0$gJ}g{miCkbjeS+xQ>l#|Bd4Gu^pGTR3
7$)|r>!oSi|V5gvJPU0%63Qs*>AOW#(D1+MSRuM)%p_XI7cu18Du$DRX_1B%gMX53St^iFwECLdUToApP+25N(#C6ZmoP+2x_T)h
iddIr+_Cik=|4Rh=7DS^Ach9Y#Ag3c`EVD1##mZer4z7=!y=E4>_#sW3QE6rRAig>}^6_QgTN|z@7G*Z_0H6k6_P<xe*NvQMul5t
Z7c~Id*9r=@Ig$#@hOc*HE6O)tVi=574m*83Vi_S8xUBC*HWI?>E}C+>9jlEU;Pl`%q#LiyM_zdw5xP;27^VDGg50xX#w=<#;m3J
P|@KH0}dwfdqHx(e<?EX6aFsqfi%!_(P!E@vHYf`e-
}`*Vl1o?t^lvPM_oDXj;3?$HDWL=hb}vP4!kP@v5Acr>kP|O*yTKL>c_&>!w*I-oL~|+UDi)NB<vCO9KQH000080000X0L-
DkT}&AO08@kj0384T08embZb4^dZgfm(VlPr<b8v5Nb7etiWo~pXaCz-LYm?hHlHcc7@R&+jvNg&$yIXauvh1=i&Yo)>doS_cOP*
yY37X*zMJjxFteu&v`*c6x>VDz=lIv~&#Df4y&5X0Y+n`coiUb;sMx$S7AYTMO{NbB_J${|6SXQ#*S8JA4$tGdNEcou#yQ58!Z-
Xe>)Ky)uC<>D8E-
$Je&a%9Ut0d3LBVMQ4?~?3Het(|rkHq77wN2%7!Q@kt%coVIRqSJxCQJFIO14eCx=z;eIWG6v3K||At<tzGgXry!WzWw5;qO_w16
0^|$;Tv{9R*OrFqChDO<ru{ssj8bfO&bzieSys<O3`A6Zn{>`Q>rFgHLO~5a6+bhBgHlM+9umHbKOpL`jw=8H=`Yak0)Xvr);?%_
P7f%!0Bi#=-GZ{Fh^a1wRFIqQjJxt9Zvo^jv4+7gfj$KzTg2TNP|t*2_^5{y19v>Bslk>7((F;Up-
+C#!tTp1yzl<STjzIST&v?;pN@2p}F32>ijJED6N2zy0XhlfQfaaBKh>J;PTVP(px`HlTt5>tyt@P0Sc)?*Llv;-
V^NL7J4+0zRAqhKp16H80`CiB`L+81zlUSmoPYk}@Rak3h`$_|MOe|NZ3nx6z~HQy5qFY&3oNYz*IUJZ$>S+jq}jzgEKlgag2Mbs
i*{1U%g&**bwIeF_z_4Z_oS2b{X5;Z1#fgdi3;f*J2;T2|0@G(Ods0!tdhGMkG!XGLD`Mvuo(xkz>+vnDb|C*$cbzLqe;_Zje^2`
Sl7x8~4V!`nP~vMU(XtYKp3;g#Msz8>F%Pp=TIn<rmE)u#{4Zdh8fzCJ?i!vGSRKsXcdp<#>hkrPnoT<G(Ob28H>K`?X}PX8lMvJ
pWYYph+ySyCl`W)T-PLztSl3DI5{LxELWKKvsHu<D!z@iPCwf-Ngcpe@NNAvuF84}{Qy_rVUN@vh<(;xwhURa{;`wLA?jlj=Nx6-
^6o2H@XcK7zmDq}}lyT0a>*o57H_NfxKqmuz{xUDfc1<9@w?Wq7?#;xs?IUY*C)^%f?Ri`;9#o<8H);#E~%uL{P$lov^wme*p?*L
9VoNwvR5Mi{@JF8=iN^wHBcB47RWF*!A4h?Gf6ij*eHn}S!=nFL`VBr9mFG(IcmP~nwR$~LlqK9bTDj0t=%m@>kljhfcPqRlV%0c
RI=xO!J5RmzBe)jQ5<)=LiGeo0~;sH}-
@4fc7GU4U|qz@}h^biWSX<Qd8^{6{rd)>Q?HUDTvMfb6NWJ}o!=si;g7mm!fi;S~++=6&`)yCRW*#LLdg(F2W8QNezySy??8-
^`#MA9r6H{w$jCA2(qOhez`uL_qHZ4WM!uJPHiyWYTA3{!}agLR!(;QUqpaWHSY?bJ-
h;d@jsd!j~h0x)atw)W9D#Pp0ryzt(XT1BFG`Ac=8#jKaFw9RGbNc$4Y@XKv#Q7A@<|h$bt^r!V#}vR7}-
Q9uO%sJ@P{i?Lm0n#Eh>fG`I!&#~mhpH?5M&=e1R%|IiCP6cLd8l?=42KYM?_>YaHGKFzZ*KApznFI^pJ`e0gHVaU&M9F&oWhtqF
@aJEygY&qI7#I-
n$&y@W46N&_7|~LM#V=rh2tZaIo0S`!&DQ|kfPp=QT2nP9(9bB?4p<PN4Pf%KGhlB;Q!vV_h!sT+%m3xa72`mSHK{YJ8$U}J7W=k
A5MRbg#ii5~8@0Js8`Q-45eG3>Z0D{d#LQg$>#hXqzXZzxn0p?gxf8alSw;>~Mk7#M;=A@R6*+-;P-
B3p#5r0Ca?#i%(1v6H_a6)k4Q6_zIvp=&zd1QM9p6X~qiqq&sx8dGIC8Mr1`LX2yt=S#Qn4r&vtONHe@bc4G!qZDXPGmNHLfc$=e
?r20*!tiZDRPb1{S`eQBbQV%QRnI{8WQz1)A@`ii(#h&`IJB)KE2Sdjpm;4s8CesF}XbY(-
qKUAm7@S0AK;r3I;8J#;B(6n>3o96HrCRtdY+vrqSaQe{m;hq;bcbx{xnmS}d)gKuNtDz8EpCKK0Hw)w4@^13000RgsdTDkpE)01
slMZ(7JZY(NUT?<npO5-I<8wkc*OT*873cnEXjTS8Z^-y394-
gACz|7Z5?c=Z(+G6E8NKuGuP;<?qK5c4@!R|0#2%^gOX2)ZPI1xG#y6MrDh^wsP5F$YsDO;h;>te+s6N002kbkZrKMj5bLemt?T^
0itv>KE|2;RMY8@+z}=68SjumAq`)$5mr{m^K7v>wuA3#J41=g>K#QTu}fYqOH6tu!Ir;XjxJZTE??sr{NyxTAWrV%y&=26Qww_`
Chxsm#qWTUvB=US}8NoHtZkB*835fK!qBr{vcq=+PB%cE(006N}X+RBwDrIGYxu(vzl}m}G1Aal-pX$SkY3<l&DvI+mSu&SG#}TP
uzTg2ZpV1^%Tjg1H_rlZAA6V+#gP63b99G%M=wB&$)AqOp)zmO?9%r21_eFw1<scaDPS5?=9flBN!Qbqra0)1lHW$z!Vao-
T9|+tCM2mSr>a*@sTcP7uZ<!9C)k&kOlIoXdja;IRjpM~A8i(T%R(DM~fO55VH|1+WbB2PEQdGakzTQ@#OYx&~e3<BQ3(ar82FzU
@;QvRKOF<u|Y1MQ?vU<Jf?f_zDz-?tmg*LV<J)k4qo#XKRH1ie4?$g5+_*+{BR*r!BXJ`c_!(LgH_qzk2N@GI<kipI$FN8-
Zc;LnsUUE6u5-3_x{S7PeMTvOF%`;UWWzcL8J33=JNQ_fH6x-
hpH3UhY(5h>PFgU#0Wko}6@7IzWhE5sa13Z5vj8aEE;K;$9<IhH^L-
i_71<{Fms}o7b=2m<H%T`GIB74E3#l|M(7C>R9eT3{D7I^k9|$@bb+!(RV-mZg$|B$1;d0-
ZhKGKik?0TBQjpLo(RKUdKpw%~wU6PuqaqmI#(xicTlxFbFD_A^g;2Y6mTQ>4<TIkpSDlTlXP{-
80fN8+RGmJ=icqOwJ*b?3&>3U;g3szs*32G-
IJTrfU8bVq1Y!J#<W6o7|3AvS{69FVgU+o@~Vzh91OghwfH!wqj|dl0?Mzt`@KZ7yE)`YOmMSq+&ybz@*@NC`jcrUav>gSc|LJI#
V}xwGHOR9Sa-KK)fJMSy9a?dZu97qSMY;C`(Vol7yU$s~IEej$EQ#4qn71Yr1rXFrE8}n>tM+J#^^_8}gX$7CM)q#&xoy$m9f@`Q
wcu;-
m2PRTSKeW?$t6hB+HBt1*Duq<QSGNWFUFwGPIigr*F={5TU+DAXSA(Qj~rJ7~bjG^ZphEASVCd=tb$5nqz`MR`pUEN$tl9IR<s?{
?r;mZN5_#x4dVp1WX0#?t9In1U(e+~J4`fi@Gvo%4UhYMJYlM`w{9Jh20o#=DZ@wIfUqn{IP3Qu8cX;hv#J_AyEW^^-
eaCsP&T;5@8HjGL81pTOSYx*T^y0Qa$TL&6!tC-ChEnCj8mw!`4c+=|)K%aIuEgt9K8RbB(NP9|1tYYxt}36U?8xht;Lc;)lOCKP
*gSJi&UXpGY+!fn$ix(Th2TB}R*vsBz74vtJHm3f;JysFI?2-Ma-
@`taQw)A~bL7mmyd}jp&ttr%E7QMSWc@`BgVZf!hZ;oh1Nw%x)y&h9#G<!Rm_UMoV|B!=(U%@gD>JpZ@=qI>5Pg2Yc;?o@f8tBfI
Rg$JbysDB9%vk%>6)po{b^gpZD_YrP5<adzwVl$c21^fJ#|9Ms5KT=PVntY&_3DDD?G%f8C0I@sP&Tg9ilaF(;!3==%<B@37PDWQ
yNO=}zh`V0Y}qz1_Mqx(5T$F%ncyTu>#Pj6G01<}Z?LXWGC&R7>PBi#^`WA1$on1#PlLx+G;_^Tf!Shq{P;vgcW)_hJ2bw{ZDsty
q5Y3IRxsf8+9t6uV&q%Jf<k>wnrUpT8Z@vCmi(uh)tG-Kc?F}`l($BFCpa?A^Iee09OHGc+?$<x+0&@y<3B0Yp}xf808XVf=wMU6
`S?kgm2y69PQ5*A34BpNsp+P)H5TFKHD-E(4?;=>llpu%oW8A$bx}9i8C_s)gH0b_y7rUNkaoQvY-
)i5uj+C@MK8y;YEp#UMyj2QiB=X!&6wvql2ku0z}BeCbWb5KSUqS;@qRVI3w#8t6f|H`p0m>6<5kMyjHuqoT0vBcJ;B?;)!kxK1;
FCZI05VCpX0P<FUj}{6=ab6xDk>RC<=6d8a7E5T!qL8Q^g%%|L|8Z#K?TDe&NUPrVklaU!{<i!HUifkZuC;um#Thz)B58tjf1_G5
3Fpe|`<5IcFaiGo9JjNx4g7+AZSy-
#|+>wuYwA=xeRjV40#gz0vGYKf~#1Yh=N*1<xq34OF9Any+vR*UYsrve;EEX?%57bw*V|p@0B_%DT;p6vMP=B9JF(sv)4;OK+CFC
u7PRo6wiOr-ruX-8CB0c>xHke=Z)~^(>RtB=wMZgYrfEu1MSXRVI`Zt4;XAS}s>&CEQ4<0<Pzk;QAZ?<|K)U;7ZM8M_n-zs4kzTk
2g1^zX9hf%xI+r#JLPs&VvWqf}=dHo4$QcEJD5!d%DaLp+Ln?PdKNEQzh9Z?}|k>&ao|+zAQBoV}wcyp^3I2hQ!f^#-
x9K4x&`IzdrwTc%BI4<7yDw4CR+r!-H*aSq=?)$kG|g7eSGY;>_9djH`K_{2gKNwm&;0+)HkH>d+coO}H$@a=OcRqh?jmj+B-
(jm$Qe=kun*;v@@G>dY~EV5@q0k$^#$oMm~z7TcsOLF69OSnHiqYaMtj1P-
VO@zJ(@#b@m}j^dH5Dso47LY&WOEXYZpovKVnE2YseBVUMp((*jN%%o=?sBkY?Xh0pHfMG4hcpNbzpHyYG8B-
jDB?SVt6gS&b7o(J33ddz?g&`VJdp$`G#g4-
B>G6d*tdLY1uh@B>0=o0=zO<Tlhl(U~^=RQ#?Nc@ncSW*|i@mjE@SwoF337N+;3=+ek_{}Tf~_POx(H`9x6v10Eu_HmMr^_vXT2L
2R)VP)3v)syCc3Am8oRH-
4sXp&IkK5taJ1rLG%gkY>i)6QCtkF?PLDf`azi6MIm52S$;T(R$GXrp<ND&u%w7SdnnX86tc@1wYKhOzK^wWC1+76+;_Cd&COi(V
l8S9_LY~G4kLYGeu&t@RGC2hV6a$V3k-
<Zoi+G+qeC}RIXx4^}62yaI98rxcZ?q{8(zhWH{M$)>liGcZV###(z84rJtGHNed}5uq>1QiVBk{9t6=;}<jwqygyaq~%K{<ADCV
{9zvfj7#vSr&P;~_1cphEfJBFvSP1Q;|2Rmd<9r4E*_aK~m11_b_>ahYhye93$w1xEy=1Xl8=+~X9lJ(+S&vgffuiUo{a<^zmTlZ
y9t2+G+QBT}s#XQTp%?&yN;afB#QJgw1*KRNZ;9#(CdW&zijV|_;!__v6JQRmo=bxgRMk9!lKIEtW>BOcR?N|08#1+0^EJQXsmoD
yc1`_Exic@1v3Y(5O`o%Vz|bvUi`*f8JZmT-n{40A<e=tk?1^CSRgdMzGz@gC=Mrb%uzmuME?!I%VWh6!a-
XFBDuY16oq#oGIAiu|oje8-
+raaPVp0`n=%%}A*02}X$~j=Th6fvhnF+?L&A_YiS5KG6vEMKNe}^2EbEjg9Wn_%vf{uIOORw&^|2pWA|L>FvHj@RQoE$q=ZK;u%
jY(rPxKT4|nbRWoMq(reAfL75c?<We}d3ff*%>m0V%U!pmU^x&)>{B2nSR9j4LxzHM;GP6u7$=EaZ{&UDF0H0mk%b`XjsG|L{>S-
i{dfG3mo=zmR<h-
tX$h~L`XQGRMVIur9GORd*EFFiE4Gx;=)aFT@O){RbPY%DefwVI|H8AD}C!s0iqr+FRAIjO#H{~@I>`R}gGh+6}ztgodj2V-
4xGmF)<EQB9mpMk^d?(^fIBjVH2FpB+x65^mk25#p!k1Gaebr=7f)h(Rfz5RMn-eqYj|P`8wg_RLL1p$x_LOEz$+}>_g1x-
=MGe~G%`z`=zD*dOn86N^5!Ou!SY^!GXW+6?@{bL}C!sYro<!}fy?CuP+DJk}Prz4iNs${z@0{4T?OoGr8VX#IPPA}=w(Oip<d=@
aw#K$m$8t0Ihyprf)OQJGHNU(*0WB9z<F-)7686hLs@5aFsm?&@%i;CPRV+6q9dr?*57H$-
h#a^kv1W%Lag)s*z}3ac%th>rA%X;pOPF9GfzpT*1m3aRV)V_0iY-!zY*cGm4TwWFpqu5u-
RG#@c_fNLCeI>O*%5=p;*UeBrX3MTELs$DXjt|@D-#RFDx0O_vqG^5(N5OLZHa8c=%=$LqeP>F>1}lR`H<Xe%veMR=_<2#77c$-
T9a{V3go7Vt|BIex|&#8__XD7ARt$^p~d{JjCAFf<6wQc>0ucDBW-JGv8$hIR_w`mTL&MKIMBH($TKbZSUO{frxD!(Jc@mz4_l%G
F|wtH2#E2PT7H)PEH|8;@h_)Wg7>H(#D&m3N(!pG1gL`L61yBDv#PFu#@rUQoG;w3YF*AnUGreXP~WFy#;Q?)FJoQkK=tG^z9rSp
T{E}F^w#EXn4VAh4*4Png4g1Px?RCOBzaxR_-LWuzbQkbA~799m!$?wi;U_?>$|+HcnW65E}P5mHauw;`fvDjs*#(0p!*G)VcJ1O
oG~M`rbqu8ccTF)!?1IM5<07@F7@-
w&D+E8Hfox7oM#r1M48M&Oz^W_WMtB&LAh1u)|>975cw+LtzXo^(}l#4K>EwWUO!j=_C+C*n+#Ch5ml3d##I}b10t`b<U{pvL4RJ
=!F<v+@$I8xcNjo7@&gg?xzJ-kT3$PzPBLnu4o%ocFT}x&sz7mN4jl6js9k%wzVi!u=G$D`^ywjw??^-
E0f~91bEFIYxuFGINOxx2x!gmN!t#2KxRP_i{V#Lf9GV~{qaA#guF;Ck2}D8rW@^>^*>mf^|HgOb2g~4T69}~4cbo=tu2p$N$oWw
_He}qT<XQKfS426af$s#5^W+f?x;cHMmQ<SphhcHh(IYIKCu@C}_kHVJPFN0DrVhGx96X{Hjy2%e`EFK$+=O*BbEN^et;j)Hj)wv
zTDI1j`@pFzgV&rh3$KS|wNSsGt%u6h1DHSt<GtKEB+Xf57HWxwjgQ#c*m5|O9xwks53qgTbYZ#<!ab-
<ZuO(<e+)Q$Nbs~4G6hI%%7W#H8Ghy$rgJK;_%DM$?!d)lFY@XYnIk_iJjPLS^n<_r=l`Jd0Y*EXSf5Ha;H!X}-
s7nT{^dv17?tT$(nZ^%75_gW;COhz9X#Wr6j>pd9dZs+uwiVCsf`+31c9vtLmzX40PRn3z?V6gujeryp#lPcpDn#0?fUP_ytp7cS
95~|2I^KoV<P~4AXmCg<E(Zb^s}65bD!1N;v(Nl;?nq5<Mwf1<$=4mrJZnGr!)*Aj|8!N5f3c<QnR&nE2(JMx+X_@cUBzAcWKpKG
mf=hdhWK`gxcj_Pp`zN?E6aFZk`k1pi8Ov<qs<EH47x!dA3u25y(BpP>2OLTq|ek)^xLPj5X&-
P{h9Bp=XdzggZvwTypCpfy22nLp&Y(xMrVR%r)D%Vs+3Xm)hc@NV%J9iGGJ+Pq(HBIF>bncBHtW)3L8>ZRmQoVKH(ilY!dSLKkE4
P1$a460>hCe^=<4V1;8lm~OD3M3#4d7_JQd?xi5TACz6uawq<tNTnfCyJD69M}v|5A-V&^wlgk=6-
h@NB$q$47@fzH<U<ozGr|*^Bgp+piIG?&|A>E?kboF-
{p+N(AB)?GRbdI)vQ&=Af1QvgYC)e+U`bENA+r2q_$87#;B4F7Cz>BtQ<JUkRuj|Ox((kwUH2JU^(<vMR|iE*`zX|=4tORliPO+$
BD^KB>%xcRSQfo|oA(vTJ%m=e@pFqv?ct=vqiWQX;x8@#%`}{>Y`9@G#o~3|y;c+fyWb2s%hdQKrhU&b?c2qu4`$XiPO*}OywmxY
)2}!DLIq@0aVfj^UQW+=y)opzpfP>tks2N$=nqT&5}FslehJOD%il<7{xgWN_j|8Rm)-W)FQI#%*1zx2eJdK@8^U*-
kU8|4(gERP_W@dGe5dz+<K@2BOb^$%Ppo0-&#|DBYx)a2T5|Y_I`#hv&d%<9(JGdEioAS+kc$;-
Y0=6GjdaCC4om6q$3lAIAU?O|mXVHjh~rj{_&o#xK0&{>^Y7k$8OqZdt%+!Na_&Br%fd&vFwS<l?hN&~FhhKo0ZvO_O!l+)WZEXZ
kJR=F(_2r8*Fsk=Lyzs+=^`KQQ2b4L5^}OS=IL{ADuyzjR<~<RMztP3ZFN6rePbCSMgHG7BX{r`ZsRWW&#~b-
43$ZDlIcU{Tly748TzhnM%%wQilP{Z5H<gY`Y>u5elO(Mcge>jgQllP{|it{0|XQR000O8001EX7uuN0FaZDn5&{4KFaQ7mPjF>!
L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z)9aJVRUq1V`yJ;Wpj0GbS`jtU64U*!!Qhm@BS6SyR4A5_do`N?NDgfL2}qm#<P{ykl4ji
R>IhSpW}42n@{qSp5JHPLH+vlw%j^{o^ZLb=-
IUnV+p%WBia~xP^ukxh^Q2}{uCmE_CBy?7d(l1CY;dgLozEGiLqB4LZ|e}{aWfQH%S$uey^M7ooe>`EmSw1djaWWr|C3NB~7p>i!
6KHV<k1SHb)hahK?_tqxQDLSjoA#s5Tg?zNAGmvIO~<jcY=0fsY8CW+aA$j4_oKrl@u6I)wT0mHaNmLI|O0^ad=pm!O$4f3~;+Pk
1E|$5~69kyO;@tfgPd3)V-l<A0695DhB)OixxX!D9-B<-
;^p=7ET5{~q*NJD!tQYT`|MIJh)5=5^0te~5}JNRgw9zhSqR>|Tf;P)h>@6aWAK2mk;8Api=~u~tg~003bE001%o002*LWo|)dWo
~p#X<{!^d2@7SZBT4=XK8M8FGFu+WiMlBZ*OyDUuJ1+Wo}_@WiD`eT~WJk!!Qio^%aD>B!H9b2Hd6X5Flv^*h4!BtW75ZY|)UE25
!-RuOvH<Mw4_r-tnjhDBhmm7aLWPwzOE+q@8LMnGCk;QZ$A;kg_?tqai6lbv+vgs5LuuinSFZhkMev_s!A{)=?)Nb1Sh|=awSErA
LJ*K8o^XE6d$(1Nlv5CcvNAS+!_wo>W{@l15l#M;<sZTat}xDF9RLfVytU<jHuM(3&fo|HNxJNlms&GDx1H#>%2rPJI&~oaLZl13
m>AbW}rdUru6C0nOe9g}`0)=nl8VPp*eh<UTA0TeutYHx+Xs1lmDYP*XEaJ%*0EORxDuUk28h5ku#Ul?G1{^Gi!6(O`OySw5PIBz
<|w{FOC%V^}-}Ru&0{{C8@=6Dl`4FJ;Io4ega@4e|G8muQ!X((52;v`+t<-
9BRXT>Jr0O9KQH000080000X00aAKfmQ(k0B8aL05AXm08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bLvLhdFK1<LWpZJ3WnX4#Y
-KKRd0kOWPs1<_z2{e0<+4fLcCS=UAT()XNbLbmkxASxqD`tKV^oO$PLg#WkdyOlzh^(+LG|+Ry4WZ|+R<VyNqf~OvIT6{HEXQtf
%E3z50*Fw)epvcK&_2OuZ(u=RAUCx*oJ2AM(3&L-k6T#pw2B-g6n`XR=rjA<CfRE-
3H2=%#1;JsZ(_5T$u?YDa#YAv8OT%5@gX6Z&Y{A>`}{(Y?+;c36(~;@;im`Ws;o83do)&20-xi<yTPxB3sx>!Uxd+%0pu;IMPz-
c7@)f*oSC2Q71mMt&4nduGN5kf17+aa*WBuD~$HRnJNF1vpHi7-
KYgfYNqi|yC)0ts|}I70O#!q3zJyKEglmVyvruisP`Xp=3oVJ`V5riv(XfUVR0X;id0}JTvY=eF)W;vmpr<`Eww6Cjp>N9%T||(^
6MaZlFt8%-
F{N{oc#h&O9KQH000080000X0Gdy^$36i707?P?05<>t08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bLvLhdFK1<LWpZJ3WnXP$b
z)y_Z)A0BWiD`eT~Xa?!ypvC_bCqUriG*r5Xdg}!zi@tAQ@~|V)djG5-
n<0!q~e{P1<JlN<Y89qjylfJ$>XGB~Uxe*Alf?jY3<%c3qRknhqFidf!`Q3{-bC)&tktc<z<aj*J|0M9mLD%-
rBScFY^oGJaHNNtNI_poCPPRsFnW^=`L;a(1&I5LQx(mOEEcVI<Nl!J2ni(hz}`dt{yH_pCFrZ_k7;u4Rk1q~m5nr4g?DN!z%nL?
>tg^kp&%v%vQ8{Q*WVXjF@<Nt*=R9$XZ}{5ifia)|h(n>GE-$dVAk-Jk_XY^G-
8bm@_@>!8uL0O#$9aqq2TmY)(9UWZPmG42*~rndqaeh16))o2XCkl#mEkq8#UziHqnuKbw1VzDT*cu;{gq;FbWhPpJ$u0^sGo&67
+ACh`W{s2%*0|XQR000O8001EX?^aH^D**ri*#Q6mEC2uiPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z)9aJa%Ev;Uu17%b1ra
sU6D&`!!Qtp@A?&sdPyKj?*<k6Is}p?)Go9qv6j}2!Iq334WabESC(B`s+0IMqn(kipgcaju6L~><7vIsWJ24t<O<ktE7myMgOp7
S(UFwU_Jef+&=?yqwAOewY3x7--;-
JTix1SxU~MOHXn!na##N$>m2YMBxR=%8umkbuWWgY<>{K0kFSxRr_$p(AJqhjzwbWMmnV!(-j-
24rW~Ku=>^kbC$A(1ZB29cWichY|D_#J9PM1L)N29)W)Z0L?zkj)d+v9fB#y%CwH8=cg#g>dQ^cSN*Q!`JVBIo9--
}GbF0(@{2!w{U84$qmT%6!gQTYdS@yp2wgq>pr^c(Nu%U&8ukR25m^D1C+jJYyTC$s5^FP$$`|Sm(!CEZH|uO9KQH000080000X0
QvyT&Lsf=0PX<*04o3h08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bLvL<$Wq5QiV{Bz%axQRrU68>}!!Qs;@BWIFxwKN!4~P^b1
RN^06e&5t$uiESwUpSEciR#n{vF2&6!6KKo$<W&4OGt$FZsqAbcFf3LC3bW7z)^~YtaVZgHr8@PXUzz+aG;k(9U_*Y`r5fdHfNb-
p8<_ff#$m-
ginL?RTU~avfD6s@JN1+^TxF+d%nivJenYN}5g+mC|^}_|7s*6Q_HOT8BE!%0auP!%)iUGOLX@RDQ??$;bla{TKi~AZWw(jIfKac
Oxti62&cG?pevtOe}>Eng(Z}!FFz#$kKw@6>{V$fH+K=W)7r+z9cPfCTE^E-
wgjX@~2=>;W<88K6!_+81mcERU|{e_~#DvMO&VlS8B#o0rxf<hxE&fAC~NjkfqY>Pt8(%0Z>Z=1QY-
O00;m803iUkHZcD~0RR9v0ssIl0000_aAj^mXJu}5Ole{-Q+acAWo=Mwb!TaAb1y@0ZggdMbT4FSb7Nt0WG--dT~WbK!!QiJ=PRs
o*`#jVi;9E<he;blY7cOVOyZ7+G^vu5Q6c`FH0{{HC+qpy@7cbB>goP@wN-
+Qr`1N1393=#3fOIG);QY&=S?4aN1TIdJL>|VF*aaO)_68?Y)1wUv6=h92Wok+R&(sssijJA9Z|-
rm#Ti)@p`}CLU~bHFo=;lg+}koOjr}>Gh}(H7;LG`r1AotoUu1FQj;sQDVb4eg)hHSIz}eRi>!d`PAl}#SO@dub?16R>$xp)(H;E
A4Kbl`jauKpJ5hJZd9`vFIkp>*fEp$;Xys34zjL-^jG-Tl07=d4blNeUDnG9~ZdQN~Zo)7G=efgU!s3mxdFZJ7AM>_%f;fG|k>#T
`6op}RJF<#Ia1_610FS7`q`c<y`rOeWT6RPF*W%YpezuS&(fp6hlKlWsO9KQH000080000X0E3SF7A^q*00sg805bpp08embZb4^
dZgfm(VlPv9b97~GP;7N)X>M~bLvL<$Wq5QiZDnL>VP9i!ZggdMbS`jtU6C<Q!!QtqcmIl$Sz0MAd!#VIP^qPeWPr&!;!ClV*pbh
nM2P>6>!g(8$$IzB@4NF2lu!3BtF5WYGOae6Y%q-
>pTllbiN?DQlxl`Bcv1>X*E=5ot#tu|ahAp8aXnc)#Ad}K2kKOCu2tBZb4!`zDyl-
1uVwYHQ`LUIh2l?TAt0XAS+~es$lBRJpFw7+VzHw_cBBoe>&iP?-I6clbeYv2J+>{iim{=h@&iq}b~P7YQWMuQ2l-
5>!BgKF(vV)i?T9&!19Qq+erIASgg_o`4Vs!caUxEGXBYSrXAT_vq+tl2mB(Y!;>2?1dvkjHudy3^O^QC^lf|R65qSx#yOS$V22b
%XEZ`AMn3C7$WhhSv6OCiq{^FM<yC7sKG`osfiXTu*0|XQR000O8001EXnJ4r;VgUdEb^-
tZD*ylhPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z*FvDcyupta&>NHE^v8WQ9(|_Fc7@^6{~QeQd;goK|+E<r9zR~1Dq_AY+H
-ij@DZsLj0Yz6DZ(Itl62J$@mO54>ynVm2J>RoG)ASY<Cu^g1hBb?I<|VdUxa_q1IqsABe$tAK0)BKB|!udh}*5VjYLb=ro7WY17
+p$tJ^FL6zD(ZML^}db?h)p#C*ES0E=Vo6f{o7ftYt?_895;*G<)=;`QjLJr2a9a3G4mkDh{6YGzBO{ZuvHbn)+LsEj3mE=taYsq
|_GQ(t3!NEojG?Y0+96#Ej%b2LyI@C>YPE;}u1g7g2lWq1gw2#S)<$`=6<4br!?0<8fLpvl+=u?G~WF$i;?i25`R5PWNiGy#T#oh
F$V?(*<@>EvprGm&bVuqQbCi9jtX}Fk{Cg1;93`c5E<EyN!?}JA%hWS-uRhd92Z|}jp8Ox*dLQj2Z!o5VMA;0$dPnPl&q0FY`ADf
x_0#Hi>1QY-O00;m803iTFowHUm0RR980ssIo0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1y@0ZggdMbT4vcXJu|>a$$63E^v8WQNe1%Fbuu>D};AxA?*hQveSAPwCf-_Y$u~S%4$gLU@L9I*uT$pvUZzK
;^|56J^2C3*QdAD)@ZVUR?jtAHjN>l!|u5fjdvX=)eJm%QVLAhJI{dDIz~3m1~GA5PZmGounJ>f>J&TID(ubANSWX&qC%AKWwqI<
YQNt?@vE~C5MP?qErw7??JU!UWtKV?J1V57s6!r^X84G<ZpjyNDrU5HIuxI>rl4gGa&zfhG#2=X47U|A0hj=ILet`*B{&(36pD<{
$8-dTf!W!${K~{q2!Ua=8ft20)yZ;7p55JFjph*8PZ%=$pgf)v79-
2q<H6PAe=NAcYf^NID~lIrDGI~t@yf~*!BhMU3wTDulk!^4cTzE!iNrCTe{u7Y-
7REEH2Wj76yH!w0|XQR000O8001EX63;MXFaZDn2m$~AE&u=kPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z*FvDcyupvWo>0`V
r6nJaCu#k!A`?45Jd0(ij}#vQrZuQ6i#rc)KWxpfRnX#Hm#+`uIz0~g!p$H$56m0Yj(!-
Y~Mls{P4P18%;LQV%3sm(;4z5Y*vlvyz4=!?#yRTN`dK5&NHC3j**SCK};TZB8&SNR$&NCy<+E%3Qy)cQYX2Isu1;C-
8^nov)!(t`Zbveh$|)a5ksh?c9!X#WsxQpd#a?Tp86g6EFRFdNAi`NHd$?*4%LTjDQH=Oe90L=h~xyu0v`xav$+uH12W{Qr7S@1T
sw@h7;=6{5&2n&xex-wU^TSV<>HAsUA?&BkEA68_LGLpJ}8gZq{TbSj5!wl*Md8HO^Pn@$m+>iip8+FA6;cKc#6Ma0k3FyYF?^Lu
RQHdG!E(gXFn{(4WUS-
#h;qF_ySN%0|XQR000O8001EXJPpX6F984m2?78BGXMYpPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z*FvDcyupvWpHeHUt@1>
bY*ySE^v8WQNd2bFbuutE39zYq;4Njshr?2X=8}?0H??_?iQ&{syJm-
h<_(bJI2T<dVcnM&%T55`Qdf7H8okL)kc#IrZMDm*ljA&c-
Mha%@77pN`dKm=L4X%E?_XuvY0roCyR&Jta#)=oeIvi3VU;DDHB{pREYAetR8o&+V8he{HZJi#Fskj7MTlKI~(XT$ShSXc2r1DeL
Je#$`P$@$rp0^%xI4u+m>3z*icdVfhJtLnu{-
~iEEjId?C~@&x4dE90|@chBS1<9Fwi(cP5rX2;|Y$psATfC(|i=cJ+U@nga(vVHkpE<?)oT7+TI2-<=-
+W9$ZBlcJ9}vUqYfx?aNS{>;h~!Baek1w5e%lk)nq59R4#B5_OySp0g)t`@Q+n%&4O#Sc(R0|XQR000O8001EX2S^MxzySaNB?AB
eF#rGnPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z*FvDcyupxZ*Od0Z*_EVb#yLpd0kRXZ`&{oz57=X-
X#H?_MSik25g4{?J_JrY#0WCwdh2EEEy8r%xL=Grw<26>w_&nKJq=1`UHm`Uw>^Lbw@VP=0TBV-D~n&czS57-
n#*$>?fW)NeOxwoo7I69V2UJLsd9#B#XzGEW;d_2FcDDiKD)z95UQSw5krj5AC-
n+3xp`AZ{Y73gVM9JA)yJx^tH4AJ<KeSR6>yIqoJNrz?I!s|<Njm&1aN=+PK5GGI@l^%E5wjmAJhtghAXJfV{B%EGNmj@Rpwty~w
xYd)r@RusB=3-!;)fqpV3`-hSlAm9rrc%ES&2lOQk2+k+6fQ7~$JAyNY^a}?4k)U@Tv^CliTn#QAWx>b^NpM6y-
S^tiy;i%J$`n{|>~aT#QzTB&(1lT(OPoR^=t1)iT;B)c+j`GV&8eOn(>~EGmP-SWR3I8kLTUVvx6LQI@xN4iYpQisRTyU5fuep{O
Id2Z8_WEeeb|E19sddJ8;GyJaDneGb}aIz5R<cQibk|vM1q@qN0MG*IZ>!<*nCc`Z6<h%S2fP}jGBw;o&31p2po0Hm@~M_hEkKSZ
%r0$-pQ=1|4>T<1QY-O00;m803iUKV6hfb0RR9>0ssIq0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zeCX>4qBL1$%dbT46JbZK^BbY(7Zd0kOWPs1<_z2{e0<-
(*6?vsjy1cym{N!tNVk(at%v@{v93#t(Roir_MA}8zl`91sP0yZyqugeE($TKb1HF>d(rMQB}^;R`8bf9(9OCL#Vu-
!340rWlyiVdFC#0f|8*rs940}FLpLU0<7_IG5H;cY^d+PrPH_m6t}{QLmbS?5wgdU?_~WUdN6Sm(GXbHigtRe?tA2MW#L9)0a7R>
f4zXdMh!U%4D#Q4^bD1;y<=eC-0(AbWxxu|S7n_SUyxJqtQVHDqUKLd-1F$C!=-
K|Wl~9$6S;%cJmnPjR>&H$3m|LOqP#a2&Hj2bnfAzDu=GN+A#4Kuyhj$`nG*vOMK6DzAVgP8f<r))7B5mO?CM(b4fg#-
WdfG<_t=>M3|i#<08@S*uKll)l#kexjAh`ASd8>qxClydnSR<=-
mhX@fF*F4PZDO9KQH000080000X0A7GW^gRIp05Ado05bpp08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bQ)_8#Y;!?pWo~pYWq5
FJa&%v9WG--dT~Rwv!!Quu{VOc9v{G93NMWKwrIsQk15DNtUy4=7j(jd9Li~4ZC(w$Utk2)$9(TNcetcQ&bc>d7wN+???lk(6@3#
%>yz9A?-
8q~+O38IUI3GAz>jDJrEU}5>2DEUDVo4(f>}7DyNEr05q|R^?QO4@my4mbyb2#jHb@Q`eJXTh=28b#_Cv6OgB7a!uu@d;1{A90Y^
c}1+=qoWjW>mSBs;~S^B@|LCN-
j28eeV%eoPujh0gOS#a}o#QJ@}Jy7rUOFvK;)8l03C=i@!NFCfp5a8DM6c8`^ilmW(l=(Y9P+H}^Y@nm1Nlr%t+(Q}7c8A$XD=E*
Xof60>QF{g075`xYgBM9b>QS&YGa^^jO)CU}fTv>Yy=!<4+1(|)DLqmH~WUv2T%N^$L=$eBy_15ir?1QY-
O00;m803iUyOIbBH0RR9h0ssIr0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zeCX>4qBL1$%dbT4UbaBp&SUu|SAaCu!(J5R$f5Z?VOPG)JPwCs_>1Vg2kA|(S%ma#9zYGPMDmnuU1cl-
z~!qe%y?{Rm&gZAa|b+t7LE#YdT(FW5S^fl}@9qYXtL5Thw&K`vTGoG9eAgy&l2IDNT!f_|G@({&>CJH!;;M^eO$^1&%40jP_tbJ
>{r=95b`z<toItvEzWu+P<QN!tIhJkpM8&;0k@Zu*%J)<Ae>H&SjOEII`DQdoQnI6|jir2t5^8%2aA<sTaf7I?`;oa$JJsV_|^ao
0+lzbmdxZ3A#qNnavubd6>1T*KmVoS!Dq{%AK*w2%eCG)MS+rBBG1`57lG6YY;%S*=Mk@#$yGXG=b&R(Iw&uG~^JBu+GRu73)XM)
H0eHP?JnoyG0qFh#ZJebIv@_#L^qg1yEs+_rGKTt~p1QY-O00;m803iVV1m65V0RR9v0ssIp0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zeCX>4qBL1$%dbT4Ucb97;BY%XwlT~WbK!!QiJ=PRsm*`#hCP^p~YFll2*-
2qOKY27X&O{zF!su2H9k`|cA$$Eb8`PsRH`uX8yv)2t-
rp>M;8+511mvGpfMCaWAN_CfT@uU>!VRSwKTI&J^?JSF#<3_UBN3r6G0}U!TXB3Y5M^b0_6j34S*ZTB$P^aT@57kX)B_O`6Yz#72
lHav4EQ{Q*I8Y_E<$%U4*cokW$X9YM7PNH@SD(2|PqxI3EJ5yOEg)oL$kD@@pmDa-ecZ8KI-
W+yIygUV7td^jzUO3=qTJ$duALI@#&i@ki^~n|s}O4;1oC7XXsKJ0&nxH46@S|&T?rigjA00#mB(ww;>qM<n#TUe*j;=>iaw%c_2
ewY!LYectTGck#m}^WSJYviyjAm^m8V`u-jsiD^&6%5OHkyQYw-
<GO9KQH000080000X02wc$xhMeu0O|n%04@Lk08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bQ)_8#Y;!?pWo~pYY-
w|JE^v8WkWFgCFc5|JI>n%F5^!<=gA0Xr5lEVXy=YfrYL8P<Suz^AA(Y;|vg9_UT8VFd-
g|Qc_0#?HX0KbaOq*RtHt1fHFX6CjMDN`IO7&BiJShcw7@ZG**1CW}JIf;XxRETL;;`Zi2O3mx&L|x9&q$qc6R8mOOWiyiRC7G;q
54x<35YLEwg#Ci$?w`2mPIO99H^2;b6CI|+Rl)#Wd1C4M32UhQH(uRjh`s<&b3^9%8s~|CCGi;1KM(!n>#qh0C#f$$eLUERfx3^0
{LQF=%`=hvdNUSxcZ&FmB7Jgh9P)X9?yxzka98i>blE+#%}U0Df);jt4C*}-
!*J*=dLm}c#7w@fM?VpD{obHsXU!x4u47aUj14rt`3T%xfb70O9KQH000080000X0NubUutfm?06GEy04@Lk08embZb4^dZgfm(V
lPv9b97~GP;7N)X>M~bQ)_8#Y;!?pWo~pYa%Ev;E^v8Wkxfp+Fc5|JK7|!Ft(5ivk%EK-
i%Km;BnwzsLp&)KjvaX%st9p+{1a$}SJvnEX6B7=c=L4sve~N+4dG@d(RkG>bQM4BTGl%|a3T81PY#9PY8b8a9E`CZyt0N^*4PmZ
oPt@<Odbc}t<?fX^=oMoZUbekd2QN<gJ_S(J+H4`R*Z*}oSg=ux}XoGH5FxgFfd?UI0U(XcQ8_;tBZVD=m-
w9MlA?>tXnr>=F)alf2C_Yg+%I#iWkqJU`WK3As>yBA48bC7>1|*+of=Ffjd!j#bK`bo0W6qc8qHQovr*z_Fb|yV+?3E9hcZI<LA
(6cjYC2^i`a^%M84CBpjR*3rj1OqOt9NMs{)?3j7Qu>ql!s{x#p+Mpcyr4#RgE4rfq4cixJ;Y2omsf^JU#xB45Uyi8E0o@@34P)h
>@6aWAK2mk;8Apl)6)FV0p000OA001)p002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH>u2Y;1EuXJu}5FLGsYZ(nR_b963nd0k
P#YQr!Lz56SKcWEK*2L!Uyb||##AUSL&qb5pg=Geh<TEf`B&$YXC%qR2or1zfm0QKwB+iI&@vP`Q@M>gnQlP_VnX+-
bc07~^!m^>*3dKjG#fY!QzK|9MLbKFQ4kFi<t%z*|KoHGhX{nJt>xQVC`^?Ths?^LtjZ=w2ASqO+Pb+!hXE6E?)7?wpUSRAO5o<^
sP=5Rw#Xgfo`lKFE(NAze68O7LB)%b}r-no{mPuUT-vIMz}b0CWVo>3b-7y@k}oCsQHdwq<-
yG((rH0$8}yp~^uSPCJKXWK$Y{mn;?kTy}=(_EdGz`<t>L-
4FTUJ@2pAaAY@uABd3>?YrmqH`Qsy*L|#EMfI{WtEBGDIUiHUQmauyjD4q@^p*={hY3`__b2p9TZ7(DZT+vO9KQH000080000X0C
Jng=u80s07n7<04@Lk08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bQ)_8#Y;!?pWo~pYb76L6E^v8WQB7;ZFbuu>SBUJ=LfYO784
R{Vp<M^bVLKTuQ9IMbE|%IZjQ#i7PTGz6V)LZ;A^8r<m&e!H+SFv3W~+v*n4KZNgw3i_JMTKsdUukOC#}JBN9P65S|=#RSyn@jJC
enHAZzYfsMF$HtMO>Alrq6pK$R-
r%IayOtL=6T#h=PVK{$z7x5!*%d@yaB<q5agQ9$raBk+N?X~`Ga@EFm?)m(g~XFOR$TxUzj%0LXkVH=V@#H5hKA;o`pO%Fn!G9Oh
E75$zgH99ZE$ju{FBPUh|nGXG-aTmL&ot2<Ic76{Rwg#EFm|Q2C=4z^xLhfx14eiEZh7F`e=D*8`{!3u-
qnL<i?eUVZu)%CJi;4bY>`uNWP3It4JUdIl7-
sjeYnd86g}=3c7c??B&vgnJENE{+U!Oj6a*LAxCdiZLRQ&)@O9KQH000080000X03Q-
JRY(B<05<{v05$*s08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bQ)_8#Y;!?pWo~pYb76L6UuJS|ZC_z&E^v8WQNe1%Fbuu>D@1l
_A?@yg3<m3=(5{8#u$_#SD4A(u7t3i0WB)$e$=WfW#Cy_vdh!Dl$CtO&PF19tR@<7iQ;i~<!G2qc#+n|aYz8-
2k`h#ZHr4@ZZ5%pfG>fUnoJnKrhb52fsF%)|PU2bpjua6tJt{=;UX+`?EDwhr<bRlj0RQ4-)gg19@JV$YCut-
!_T(YFkPMy@)l7V%t~;`MG8Hpgn~L+VScaF>#8r|(awN-&9Sls((7{QYYe#iUfb4_8!6$hRNg$f9XSFDSw&frZHhFZ)-
Mk|EVd^okaSke@omZI~zEiOjLLiU2f|{Cn=P7YKTzU^5<TGGrCk&mlEG=Fm<}a4aqQUS##%8b;NxFE+{MBgk#;|${U0H0f<o{9wU
QxNpc`c_iOG~Xkj2+|WEpDr%_YKnMxfDN8O9KQH000080000X02o6cQ$PU#04@Rm04o3h08embZb4^dZgfm(VlPv9b97~GP;7N)X
>M~bRA^~#YiVw0FK%yiWiD`eT~SR>!!QiJ=T}(eGNgUnE0q%*CT$GS9^e#()a@eLq_R`Sg!u0yX$KQIS<lb!*)KOxKHa~pc1ELRT
y1N#-ZTa&hyAt^4Y?kqY(_s4N(rVP9C=XII<LHOmc_(z16tLFVaaFq*h}wRC)HpsBV~fCfC^E*mes>vR)@n5imT2-
KzM0VcZ#{l{L$EVW7}+*T2}Q~WWgI};HYffAr;wF%xLX27hkE2FRPJtmP7W8+EEP(w6oeU!a%MiWZqnSAZkP72>cOYWTf@1nS>Oz
9EBol<MGp9H{V=+j!iejU{p70U9rBG;#LTu_-r-
Q*v#8cSEulne*wf(b6`&sro1PXq)rJ7sb#Zhbp4O98%d+Yk04n*I*Y*=R(Fw=Cjw#kPYdd#jGvs>@)CiJYp3s9{F*M4&8_$WP)h>
@6aWAK2mk;8AppPwk((d^007bf001Tc002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH~=2Z!ckFWG--dU64Uf!!Qhm@A(y0xNK5
4?v;v!v>hgG6sbMHDKd>)BGzO|JVu51@1$vAh@6ry&wkIof$DMdwA!17Y@pRnlV#Hy@;MxKwP?NTL8<o4XHQCj=}*oxptX*Xjk7^
a8h0X#T`X2%2u!_V=Z*?b=BK1exQ<ka>ba`72UVBl9*RFd3jy(@%I1h66q22GGE3NEPlZIS=l3gGeI#GV=`vI8noxX7O`(xF$a}2
;p)NNim}s(=8A$Y982^|)_?9ue$*)W-g%B79+kmEa?mfjxQ)Sm=V~!jG`-
vg556a^uu{e&Lle{=R{Aa<PeM5@gW6R>fS&GK6x*Jt_5_pP>wtyEjJUOq`xC7;>Gf_39y)J%(WLN(zIWEOFP)h>@6aWAK2mk;8Ap
o+FMUWK%006@Q001Ze002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH~=2Z!cqPWnpqIaCu#j!A`?442JJ{3M*VTsoMioDi`1|X`
@K(0Zx%g+$~a@Oo_)-A>N%dEew%U^x41v-
@b$9<?(g1x0+m}&CZZx+gS=F9Coeff*(Ms?!uQqN`W2DJ}{tjo{_D0QOrI5Ob(Aptl}7%2F2d@3eWaO(q!BwDn#?vv`+`s*7Y8$K
b4h$^s-X-7-J>b8!wBD9S&4U-4lj|oY0w`LM7+VLXFq4`jm#EmL<rCNdSBzXzRxsdK-BwzY4JyLSP)721DI4YWB}-
6t^goaS4&b%#b-
m74Vu_$}bn=cW=i3Ec#2(r064!te(B2WDJ}8sjJKlfzo9i;1w;;&RaDttpXiW)G+2lu6~0QH~%6#uEjS{O9KQH000080000X0PY_
o1SkOj0OJ7w04M+e08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bRBvQ&FJo+Pb7d}Yd0mh}Ps1<_h41+lR=8|Zx7{n1(>P4pC{lZ
XQ)C)<M6}5iXKWSXzmukgA##d7Kl?rV4yvc^^J;GzvP`R;CL2s^$mej_)uQ#T2c_C`ID1kGOn-7d09xw;2IDM?N#jmr@fe#G4;-
jh!MRT1$^5ib3D=PdQN2|4!$H+$xrgFUWg#HG)Y){%T*%<GlUc$Rdn#npIi{Jsq17GvLQbEVYS(b_DK&8;bC3u0?|@L3+Y(Il0c1
!+^jc;h(I0t~8ND%9({&T*8st|dmO=>R!8V|&ovo&PY0c~wbqtmR2R|_k!L#ysNi6Os=U}f+5C0jvvu{YzM;uu^I!n<QR`;VSPXb
Tz@)q!dCQQz2H6BHII+~~&(xDf>L9&~FmK>Mj8&FFF1QY-O00;m803iS(uMRyI0RRBU0RR9i0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zhHWN$BHY;SXAVQg$JaCu#j!A`?442JJ{3M*VTsoMioDi_9K(ngWm1Dv9exFb><PjSXnA>N%dEew%U^!fk&
+rES5dH1q8ID?*Xv$yD@>l}s>j{8=0fd){jyTnUCrN9km3K6vT6m@juS<D(bqt~ZoRy=aVK}Dio>9hN>G#R&v3emha?c-
6kb$x*9Ph}+_z3eo-
X0Bu;OR~t=>j5iidScXlzrc6xZI7Xn^Jk%!3|F7hA{$wPe3(3tOwiW58eB@_t^6v)S_q+e^ad<;ORsr`yh?E!X9_QYW0;waF|Z2y
npxUGF3E3X$N!A!5)3N*NG+=;@|c2Qb3dudEC`sc>p@?&i*xc;O^d65Czn)XKIZCokm8nK<ixf322e`_1QY-
O00;m803iTov6KuM0RRBZ0RR9h0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zhHWN$BHb#iiLZgehid0mjfYQr!LhVOm~;ayrt`v8IL)Ex@#GDr^F$#}NX8WO9>&Po`2_qk5Cj`?Ih>DT{D
574~qUN;A4&<EV?E&Av>hg`yO--
?cD0HwMyj*Loy8!p5VwD%NsbmW7Wd+35*pORRGDMTDpB<hvExF1QAahs?R&0Etx9aUS`2dMs3Rszz?O4I8QDjCU=EHd_bz)G5tIk
_zCtiA1#D>;7_YRQD^Q(6p0mLQumT_K(k7A>^(u7=))xRqapSPLO^n7jdt-
7;|wlJ_a@nQjS62$5%|W8|P%Uo%UK$i@Gi?DU@n8rh)2k2JD+CXdM&HjlTiGB+@$6MN8C?c(gbRk!UG<0(buDPMH;8>G1V7uj(wz
5!560|XQR000O8001EXe5&>LBLM&a+yMXpDF6TfPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeGZ)9&TWMyn+bY(7Zd0mh(Yr`-
Qg?IgmLtPSZlHK4==@3Zjf<3g8xLW5#U`s)|G%=<By|U~!rJBTd@990=15_{D*VW!MWCN{snk<{vkk8?;t3~Tw4@$KczIaj!On-K
s0j+h6Y@7{Z(zr8OJVvt$LtyF^JJ%^Zn;%P+a2=@-)mv3R9aLSGdno=)76Rf)&Zff<3dv48nI&wor$TD#h-pSAw7Mf-
$mudu?V3=0MrCMZ4sx3ufKZp)5=@L*%M2v?V;ILqZ;aJ++c4c&eq~}QgupP^1~j#E#8fQ(FS~af8|4t#PYjuTP#&*|#gECk(7V&a
e-_-uH>BtzK3P0FOEDN$kE1G20#9+}7VwIOr{uL7x1l^8O;inO!;9Y{**!l?iA(VfP)h>@6aWAK2mk;8AplJurMo8q007?s001Wd
002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH~=2Z!cwJX>=}dd0mh(Yr`-Qg?IgmLtPSZlHK4=$q-2Df<3g8xLW5_5KBQPH!-
FEy|U~!rJBU2cY5#L160r3m({^EWSLfbO*WX;kk8?`uSM%!2THYl=shU~rn@*F0IhWagK?I{q;VIrc#6Y{2M*M!;M`f^#r%v^3D=
PdQN336?x^arJV5d1Wg#G*G})YyxsbtWC$oetc2r2xCd}X+tv-`4<aC*-
b`2MwQWG~a2f2%SK&Z=Y2`1XCWd;)ciN{ByH^yqZZ35lGhGV0i<yR(_LI~u+HlV4UeWq-
wVs?)?hRT71pBRSVS$VuB7Q4wg)tl49f5xu&4JrDFUlvc!QZ$Cu<EYA$z*F411-#<eVRT-raUsgn$wbwVmb~~4lHL8Y<hT^yP)h>
@6aWAK2mk;8AplZB(Pl3J008y@001ul002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FI9ADY-
x0PFJWh8ZggL4Z)YxWd0mmgPQx$^hVOX_D_l0I+XGZ8Cw4&E7*czHQ)F6qjg%%;oKh;pyOX7bA##d7|MvgKxr6fg;bnK!HCd+JV?
#FRR+G=+^jL}3yB?Hk$1r+Q3Uog>9{{a&0fTmy#iDToS-iw%#WM%$RdCKI9Q031nQ#@U5anxG9Zsq`pN~-dscZzqlR9gI%!M3-
Hag5QOBIVf6>_mL?y}MjZDYt6a=EN@K##_dQH(7Wl^<#0jjOr%lnrq$bC8FR!JxJ<b>s;`N07!t91og-
J2%<A{K~{u2!TA?8X9U>&n0ha$ZpZEDRbc97lt8tRvxFs;(O(q@Xa;zf5vX~H7R<JBa0_zW9TjH?yssm2|UH0uz(ZlusHA4x+LZ4
qN8w5yWjj~$!-y{WV#jKP)h>@6aWAK2mk;8Apn*+Sj{8>007?s001xm002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FI9ADY-
x0PFJ*FaZ*pH|X>4UKaCu#j!D_=W42JK13gKN^NcsSQ3<m3=&@O}Iu$_#TD6Ju}gXF9WWA8r4$<{HS%&%YiKj{w2=f{`yXlk^K>7
haEO>2-
cI2|g{lIuaKcJw2mQegVQkq2$9^V%C{Su7qmpw;KltaxINz4Fd=N)P6zrHpbFR3XaOvf7_iRTM|a|5P>t!i$}Cr<rp(dea#{$s|^
+?lG50<Vdxq!&Sa$+jK~|Tt2JXxSI1%*&x?41G)bgI&Cam+!cxd`!K@-;S9$RXYx*dC1NXt&^*~18f@3u3s~GQxiQW-
8L+2C)7}#+($}bk#pFuz=9=lh#%`n<6~2d&`IEC4f+4-
1U0E~`hLc;+S8e=~yi@Bn6yezf;}nm)`DICN2uTdxif>R$0|XQR000O8001EXc=ZyWO921?Edl@lFaQ7mPjF>!L1$%dbWCYtFH?D
QbY*Q&Y;|X8ZgVeHbZKm9ba^jqX>)X6bZ>8Lb1rasT~Wbm!!QiJ`zwTZX(8<g6tdHH7_{r4Icz7RCQ55??I1ZVVeH@MIN3VplX#M
z-g|z4!`svQYHMrqLaUdCe6+14-
oWmqQZ0uI7}NH#XEFxtr3)MZy$=zi4PMkV6FTyEO3OwDiF7eB1ZS|bKP!g}R|!?>@NuY~cc$9!w^07+EEJ@dH*1F?rS7A3HV(ST9
gi0(wX+g4z0B|#edCBrJry(BA)|BTj9^P;#XU`U6KW|xb2&cUkkonudYfn=Z2(@;Iy^dpIxr=#4Ro$QS)Y{&90#Z|(kbu&Hyh6&=
h5KE!?w$ztaax9D%4Ubg);a$_1jtLWHYB#+#QeRHXxBF3}a+5jJJ%XnDp%H7@FZfCZXq=3|$jt`5Jt(x`fr^IJL<GOz8tX;0<k@F
0aj;tzkMP>pbL47r$DHyM!ViU8-
+TO9KQH000080000X09pWo=QaTV00RO505Sjo08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bRdi`=X>@rnaBN{?WoU0~WMy)5E^v
8WQOjz>Fc7@!D;D*VfRhg}s8DDRfjkQKp*@L>yiNqNWF$Gkl>U1a*=<5~T4rZ8GrLbvy}y2}wpx)5wAwUeqi!|%5_X%Kwcd3gWjn
;dla!#l-
uVb<t&147vw=+<*OSFl8kS)UkvbWjGZK6KJ5pu1PAFs5XH~!LWPLbnK|FL84ARS!%3uhB4^bN(M_%NP#f}8;4JtZ2(~u8y<BYa3<
OQFK8ST-dF=S-GmPG9bn()S{Aij7*LGcoJb#_<43u=Q$LvTn*UT#Ssxk_4*;8AhSzYDfxjA0n9f`-
~zeKMbSP~3CeESC_XpD>Kk2kG&eu@s)qUXQLB|6{=oUXi3r`cmwjP4<_tdcLvBOz@P>VgawH<D|Tn^Twp7lTO4jA7b(6rMO!tvgn
fi08mQ<1QY-O00;m803iTV^Hhm+0RRAt0ssIp0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zkNX>4h9c`tBmb!TaAUu17%b1rasT~fhn+%OQm>njHLkX`U5_XYRV9s)^Iun+A?Oy%*eK$eVVoW+DdKcZjQ
FR3JZn-
HDEn>X*xJn0j(-@p7gJXk}X>2TkZ7du#rM|iyN)DXi6S`V|#k+cRoP9X}Q_d!r>@T^u&n8@QPHEUj2Xw(vd(>U2{OIzSBp-Qzs+w
SY5?w+0=pm|r>DM+Vu8i&kHHH&ptmZ~llk0UkJ<mQw0x(|jo{EWVL6q{<jZ0Lj$og=3i2Wq-
F(~9TD=A~Tosd{2l9ieK^;R0yHKBG_%t4(IlW7?~1n-=eZ(44pG4VP*8cC##c7*Cw_R?1x-
8g?wPP9bFxbbI*w`_I)t0$9%z8F?@AEA&eixwc%{S#9IJ)@rYmLSDRqo`x-
kHN^53^;@2~?+AH{wJZ`@N4yj)JwmmKX5Wt(hdCP3^qeG{Z^5S=_i*@}S;s<%l)gs_=Ym#N=UctKoQ`y|iMW&xvHL$u{Wd~fO!w*
^P)h>@6aWAK2mk;8ApiqCa6dHx00095001=r002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FI9ADY-x0PFLGgSWN&R>bY*RDY+-
a|E^v8Wk-<*GFbsz8c?v6BHmMu;O63HHNgG472RKEhb+>3~QaLG8g?M+ev}1^ztj~7--
}W7pFOP4lt**&>T5TG#LARPXhux+UExQhsYKJf|DFwRg9S1;bUBIB7^<t`VJy|@&X5~j8s8hi?qp;W4mNMZgQX$IsvU=L7YQNt?@
h7to5MS!74SHY5A!wt+D6^EY*ij)FZR4T<b-
lqrbM6?aAui+;%(O>FW5_6vEfp0HH1WpOzW9<2`C8^6U&%Ja5RL@(z#PYjv9>2|5BHNCT;<mCI}=MG1p3j|&`>)|Pv+AOvfCUN%Q
^VK6T=YLE5>tTad<f!{cz3rpLsWMO^QC_m&LQQ(fbls50|Pu6)?rKSim#tFe$IqyfMXe(6Mk#hgkf2$!-
?1B)SwoP)h>@6aWAK2mk;8ApnL^XjnD@000C6001!n002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FI9ADY-
x0PFLZBfWo}<}b75y?E^v8WQNd2bFbuutE39zYq;4Njshr?|v@xXi0H-Ll?iSG|mF;e-
5dTh=7KX?vdVcnM&%T55<>7U+b2WO#%~OM3T<ef>*gsXOrO<;h?I<ImG2r?kkbw0*h!qz+tC<r9^!6B=4NolC8wsH^c5pu}WrC}S
DpkIf)#Kh&hr<qvKb4h&_)=%xS>{5I;yNdj&QitO9t$nu1HBnJ$}RZG`ldrF^!!=S!IJGd><rr$i;6~^@g~$<eCh_d);Z|%6fTfv
LYfIFkDL&q1%ZLW*)>Q&$V1GFTm6-(wNlFR<ZEcKUG!)7X$jda$klTWEHq<QgxHY1BrK-ai`)0mO#d+sBh_f|97h(<!N&k=*xX-P
c_I+TyLhk{>tt5mnq_5%@aQ6ON|#vuddY4UvLw1z-%v{f1QY-O00;m803iTdBj4U;0RRAR0ssIn0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zkNX>4h9c`tNtZ){&^Wo&RRaCv1?yH3O~5bXUGtI*s@Ip`yW3W}3>Nl5{fwIrK6OO73_9gcvI_z1p`FTr*K
oWPYeJF~O1_6byX7x$Yh)sS(t*|uc7>J)JS*V|fjY<rNh8~w;6C8&O|>;a9j9=)>0iJ4;uGPnz3=_co?m)=?}aZulqD#3L?g{U5?
`tn-Vx3^bN9#vKX!b!?TqjP08dZm@0vOHA`_Ecu6z9&5_=pIe0iOX!hEa-rYT9cLzJ1T1)X~tXIxbih!<H=fbO;$iw?d<`K<sP+q
p*HfyKIBO$p|cFu5HyzQY|!IQnKb9=;+9$=?_6vZ3$SvY*YNrN0rZTGPwW)nSn+7vDJtv`T~PmHz2#ypgg`f$23qQtu=AqQzVqLm
MO^{GcgE0rc9QXsu(0TCX&PPsV$P1-kff*3vb+gVgE4H*BdbURrtk#}-~pANoloWRI+AIp0&z-
@zWSLZ{~aMurfcy9P)h>@6aWAK2mk;8ApmKbENP?w001Td001Tc002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FJE72ZfSI1UoLQ
YZH~bT!Y~j-@A-;QFAA+6Ab9gqP$;&7AhN`ETNctpvZ>I&H?#z?y0@J-
v$HE%7Kdwgq#6xlmN#fTwS;abPkAL;XL||I4t{V5AgO;^=cO{ndgaL)7PDvjP>d0;g$z@U?6I$`)#+kCV@K@WIO`WiSLmT5^Q||;
wSA!jo`T>*l2fq}0zhdUzS+y$<V-
%NlXR)Xqmlg9Me?^Wz`J+@P)h>@6aWAK2mk;8Apjf7=IlQU004_8001HY002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FJfVHWiD
`e#aeBT+r|<8u3xcXKbSOh4Ej}oiWrHD8n7E9cP&~R40?}RNsK9y-
Cf>Ux!iy6%<MZU$rq<V53nVXGqW?Z&%7=9CwBe*hksqYZEDdearI^+I^Ap=Ay@3(o14W}_6Jr~+fk2FR26FuLoYSsUDs=_o4!*EL
$l$U*DY5{C`aTkEg1-GH%lhP(DGUsj)Cia+uS+o_wdu)(8nPNdDm~oR@}fPf3xX!?(VDZxMbh+w&i!NSlEl^14NgjZd!k}Q-
i3r`>Bqg`Snq0ak%OG_HVq~v_i5qQ(CfLz0BLPESI><hs9#?owq0lU49YW`bLhTSkNUFgsm0~{<18)*0QO=5kl3n8FVk%7XI~}V0
UBF>Z_(>KMtaMwF9R!4V>kISbq|Ae>jM4BR1f=Rv_Df>($EK#y@g~XMPLDn)Tne;|@%94hl*I*6V*?-@JZT-Te6DTd+4!<emcmP@
Re_TW6?4woGn!{2<nu*fe@_V{bgU&dis|-
A!Ms^<#z}$yO|T4g8EVBcEkl?i5}|XyEU=esjd%b>C^QGJ6WbieL{{$F2q^Z|&MSN0%%a*IKGd@`oiuK}+`X<);T+qF5z5!4?}~H
+vE9RioHFZyVTj*ai-
e(Ol|rC>d@mV9;8s7?%Q|t@`#J2wVP3(;gRok2DBX;4HI|eFvXX0VWy+R@VC^Q@!0Rl!??*>>5Df5u62a0D;Etnr=f9#l3**c3~#
KP}v?!2RCCy*tivfdEs^|{IdKjb_)M)-xhAWR-kLGZ-IG<5<UP8g>w!b=VPm@Ew8~{$2F1_#0FmDkO)=`+yya2tl(v2%?-
tdcc6Pe0?i#P4>$hGTP5h;z$HYVXe-
6H;>7)?8%ABJdM^$<Rt}@|8Orse{$2chXe!tS1<8+Giaz_ZahK{xS&ItcyP|{!ndI*n?h~nNytrf#<Y22<lWCM4rTK0aI#BAX{N8
=FFynEEkE$AarK_fEbXDa_wA+GR{e`54km&DzhCEqTl@c052q=?qK{klZ05gbGyjH?5!Mm#QC4^Qe17XTlM6rBfZMz(L;R_2PiK8
r@BQx5`jIeFwM3)()0odF~TC-
)TJ1{;Q1u0kat`<fDhRu=%$aqyGk^7a9uG|Ton}k@<a#>LVK{Mo$gVKa0d7}jTCvQjbTFPGL+w76#ZO67HygaQabW0SAc}$A`jEx
kVEHPxNw#^IVipi43<NHu0Bl?-TRy>-T@TDT3ZHZg;v>lhX*z&^mCYl6x(K=0S#ZO%ECCASUx}^VMguH(zpxzyX-uD~I%DClj=`0
a<5yA6_Os-@$15c_irQ^BMh(}`Z$Sd3a0m7=7+Xw0rDP&;-
0=v?T65Q(Lp2IbnIjia4DQqok<D`(gW<h_C`#_n|Hkct*Qd)!0uzkdB+B?HI(P?IJ4B#(@Unr#PF{tu%2C`B>H{BW0*5pC<gOK{@
&Gi5ZX*#jT%5ZoKdG)D$^x5z!J13r7=_-hy)atMl(Shr3Q)GV#z34emtfnc!P*KY4jNExnpv#bip|{;wSWc}rI3~iVx;-
>{UzrkY!+%zfm$RZurcYb<Xem3g%muEa?}^xT^gYtfwURCcRZ?t)6fXImD8%5eXC)<4H0C1WNIirhbq=skbT87--
TR6P1D$T@MfbF?)<M=C5#-GU08wSv#@@K9IW%EaFDvYg^QmgfnIS=5s6;!H6LZ73WN9Ts)8;Yly!uCE`Nvp+ZzSb_c+qK+_W-dIg
u_Qb#e5e1N{l4F@%QQC1#|}Y;dGCq^9cx{g#<BRKZ!p_@P{G7ns^Bg;OyC~{*xWH{LJnyP*%Gek#U0~`xVV^iWq6eQl%fcOm7{v)
zE+Uy`Ihh1jc!slZr?WB=i9bBV%5X7pkf#EjFM`VUOSGl$W%LCz)U#4m6KXLCd!1n}Dp79IF$;K?)44bq{TEWn56v_1x<|+latC&
w=MM9=e<=nb~ao>Pw1oc>_zUyqFah&*h2>ou>FI_l(YSMnMW?Z#q&s4CUZ``2W!_h#`)8)0HSAWHW(j-
$UdV!_K>n);jRv*&AoK0I9+Z7MDsK4o*o+C;ddCf>CpIp48y%cW$Kd?b;|#4njqXIZX+jupNK%$rxugK3tlOB}T44f0%94d;w34X
Hr^@B0DWKJ-B#=;Dq6_a0Bjd)+~kDb5@}qs_M7SIi9(g)Ck<-TfZ1?DG8gmL`dj!=|7+-
m{Z4DF1<d0d5mxPprJDAJ=g4$5QAbP@O(QElL3bfFFH~Nn4n{{xR_uKx0)W{oXfA49Bi`Ro)=z-
?MqQ$55y+Wx0X4?+Z9WiJ7%Dt#EPGGLoGA>?(_sSg`IqSDo)4H3^Q1f&ko?x#^Yq<xn^_G2Rl2tQaYRECg4b%JDD^9oVTfCO_KIE
=zu{-
!hf?<%@8pTRBcWUyy(2=&AUi>emh)YfIZ2Jxd1x`lZ;DK@c&8s0H#mks7{FZ&H7s$kO`0@sM?%t9WHiA7YZCCg}2bf;0VjoXC6}2
Bjo&h(H?0S>_-jAmz%oB2Pqam#<xDR_`1H1&h_T)A!%E<0U|m$!|Tfv3<VP{G#Ge$5gdd+O-
sD?E0><;%YB^P5!AtpD#d4zlSF_UlSB7~NT6oY^y3giz0_ip2Ptyb_IG*qvK)?CQ6v+FXDm&--
?7KcWn(1ACp9qc<JTt^FGTbuJvULfAt{!#D)dOx<Ho+zO*e*VL7RsF751-
$A2T5Mm6pLDY1VKWU+M?ZqY>G2y2Wkw!#K1}4FMX@1olD8qv-
(W4WGJol@)(2=6gl)a@I<Bh!H~P<ncv3n}zv`4wEJhiyt&x9>tO=%u6x+_8G~EVLYp)!1fkx$>M2T@`uXqspZa#WSF&AZ5YkuM$a
(4To)a2blPR&P>P^tHE>jPoeqRgilFoSz>E)rU9akhlB0%f2R-
AEA*_fN3vv7a#EmL=Gld*pxs6E?F?g{Y`XRS+)3vO~|M^<eXEoMk(Np7>FOj;i&Qnq2b?Ow!L+8nyhl|hVId$|*8c)OnZ1Tdc9tB
DnAN56$PEX!UES*IEnLzR<tWpp%eI5(*H{5|H^&WMj<QZ-mEh!bOSypD{&wbP7KyS4jx7+4(js<kUe3%%u&CWl{FDV^}P5FoyOLr
jo;_Ahcy{KLkc*vWWdO3RifqCKzGC#a)VZ1;xHrR|El|6<rkE;?t&!f)pEhBmJ+GJ>q%LY-yBI#=zC0;eAkg9E8({OMx5n;1}!s7
Ez_+63%<@~7A0Q3zl>=61rz1zaVYa%|k<6<ioAvl|)&xr-
`cAy$L{%2S!(J6ePhQbbqRYPl=s>t29k+~R{=BMcv+@R%rXw8Iv06b>}nhzVCpKCE__L@HM>2=_a_7|f*@o{>DN-
m3`Yc;YEJZD!rl|lFQ8sc8zvoNUhN9S#56aZdSw-HJk-r_FC(LkG^?E4yT{A&{*Kc0`Dj~@YS9UEZkr3$|n>|x)-hItkeHt_lr-
<c*rDE;jL`WqNuVFbQ!WZxZtPL=G&0l~jvqxS%-
w%P6VgTVjUtM_jV7$F=4hcI~9)5#$~qJ_cNz2%|IyFt;DBTBWCmpRafwvJ~#=u5A*#C<e+IZI(UjaDba$H=6Gbw%}LxO%DK?nK}e
vF`2!uI6hQ*}G2OP9ps98nLM=GBZE_o(kdV&Nn<sC|D4!!z8_(pZJ@$A~}$@ct)wYl|faMbfL;>Um+`1v+Fp%5NGKqql3j-
NR@<Ij_#twvW&{$JQ<pITmB1BO9KQH000080000X08V76i_QiB06Q8002=@R08embZb4^dZgfm(VlPy0WN%Yta&~EBWiD`e-
56bO+cxmszk<*nB5jJAKJ3M40(fnP1!&e_aj^leAt(}^u$3uIq?34Q{`>Ao>Vu?gr^EI#y+}G9@B5B-{El2-
z5C<%J<BN<^!TEnT(T9T&6HeT%qOd+T9Y(gZRDn*X-e3-t{O=)&MTQoR&g<z7}#e~@%H;puFLj26I-
6Ms{L)~L{pX9n(^C~;*4)6lXU*!-
G}sgKAV5MPG|2gX4mJ}<di&32s}YmQyxssJJzr)m+YRpP+1j~3*+>`1;J+lA|SZ^G%IB$X)^+U$e0`f-
(>lhvKk|lmzAIeE|{+&+y@sGAA#o8x-O|4rDK--l@;Sm+&O!m!N%{-f1Z7OKeudsIlJoZJTOa=BrUzx`e$cnzH-OM$BKIT`!5&s^
XseG+w=6db0FE!1Vv;e4V&PT_#ucUlSy7?LXZzYaCQsfHV1EA)8-yRaH<Ih!4-rXK?zBnH3Fo0wW^wRCMAXpn40A=VWL7m6-
0&8<=c-xk!AzYyQT?Hm?%;OT|xMQDP)?4f|jd@9G{V2!OWT!J_t@y0r9*M={l>^CVQ9?Asg~lVS*a?+Kr!Q`5m2-
g5`1n+hW|ibT)U=pguHZlCA|ZQbNVVVX34nnUD*c=(3j@cBGO%N?-
shA^ei60n<eZ{IWWXI!v}AkgeT@o`fPpA+tGIEIX)dwl<2AxBxzw;YnF#g$P?>Js0|z(^`^q^@751h>ekofpfu>Jg1@N6Dz%=L)#
5R`64fA#<fWek;t_-79=IGv9~e=8ctan-aWtjtlXg6a7(h`RODGrL$t9nw>GkG<#wB$0*Tn%gaHX+z3y)_dZ^XK^v9EvWiL9%kT2
O^)C8N6UH|NmUN3?iq4~0d0^IjN8=wDJ<xOs>G*sfgDhy0Jw7ZoZkedjcj)pLVxB^4P*Y12luq#fq*g^1g7#L6|6nDb7k-
~~3KkN`GR>|uGonl-;LE#%}EwpKevFC*s#0gSV#tRSxz6S@iaWf{2pOrgV8$%>njs6I|O-
~*KA1%jJG15U6kK<`?1E$i=i@(uL_}E$-
D#M^r>h~cuMkDfNdbS{5&>Ca(0om8&J!RF7o);9<Vae)|PDjrT=!}YCa9IkB9~?UNI>hnHhbZCr{$4%+sg~+gqwhNDBP&-
*28R^nN~>8S>XJ!>iZJqWCpZms{&2PNg;D#3ZsV>%;y%qJ1ZpvP9l5w|Zh7$sYi=R4H@7_0+pD!k2jqZmQb@iA#)=C-
TehV3_6peM7~>u25n9g}7G6Nxi(Odj)+epYET?x>S%BUzFSjZQ29oURZ2Y67EtP%|HR1-
UL8I$hZUg54LQbt42U%&0;^`lJ;z9DcV%*M~Rq)hrQY8juS{!NM5vX_sjp|YKOrG=ty5ea09QcPppJu&zW!3;qXc7zh=oq%Q#U2B
9NYI`(!tDe5<(sP5D(m;4?+2Spi0Bk?be9I`RS71XHyaxF9+DgA_ZN&y<3hKJ8D(@>+GbSZ=?blMb?PvfYKT!BTHm|OH|raip!T6
?N%u1WtNRE+A8dX<r3`4a$L|A8@xWYI61v^^gVER)JA2`)2e<RXazcx;oAqdNY3Hg@mMC|<Qs)j6fbi#rH86M$DfZM7CJJ^7)zz)
u#Un@qkrVc~5K`o|TOUuzn^T4ThLn`6ToWU$k&zP+<DpAD6;=ZsNVS0u8jn$a3lq~*FUhl|jhhS>bxvtfV(l8}?6$S|sN_fK+6q7
+Dro~F<4&E>HJZ997z^DxEn5cumOZ8z^CXIb-d|N44jycW;nbRjFWDpG-
7GvDgJUw7gE1Cs3UDDQG#liOmiX&TzsNTgdcN*Q;N8<VJ_a3Z3<k!8H2qXyQA^u42TpO-UhNs~%$9hRv18Vr`xvt0Wqs0)ilq)91
@gy64eqU^`*=m>Uzp7Y!>MimC~@b1%tF^&-
#oJ(X4n(cW4psq4{=>|9GJ$imnn7yhgMDDjK#$uCN!PB1HbBskYZ$=<wgRV++dLN?g<uVtX7wiT5r6_7)mT;)nvDH|1FWLp`JY*W
B!x5eV+$?dg|pl(HVaZO*>}L(N`!HU$I+rFb`<ab@iDEYlMA~$ac>+l+-
k{I?e|jZ6~p9mj71Fk<Qxna~P=#5P9(<vio7d_=cAJ8*e?@KH3$2c>SUew8O#Lj?67$hBw;n6@4N~O6&0C@Sv?p|F0V7ePJ@LXs4
ciaiNs4K`5MqWD9-
j{P)OsU!JD0oTgZ7bWbpLEVh^OBb`LIG;+z;t?jrh=+>=kO@J;Ze*;iU0|XQR000O8001EXY6W`$Q7`}iK+XUF8~^|SPjF>!L1$%
dbWCYtFH~=DY(!~uaA9;~XfAMh-
F@wn8%c85e?CRK*Ny>}AZBK{+~r~ko@Yt!9q&jEgB;qY7>@dSfW}PU0NuFm28UxTBG$5gI6|k8EN{qiNEatNET65oAF^bJ){=FK&
=YW9fiK{D1m{Opb$xXM!{zzbMg%!PcUD$bR#sM4R#w(K!PCcgzklsPI!dxKxpse?WK}vzlVT7&ynk?IQslEBiYAL{Q6y0mq_cTmR
6(3&c@<Y_o|RV^rn;D?*@=9=mtFLNJMnZHA5W7j;^ApEo67HTd6A9MT>h-mnF33*a-NJT^-}?j)5&C-
9?PFa!Zpw1>J%Q!svpBo2{OvFDtTFHg??D(nV`7;FwWwWr0DPOJx$6I+9FY?2Lf>K1eo$<ks+0Vs(qTgh_foH@_ZU)@hm9?^yBH`
B+bO1PvTM)`Og0S_o7Gp(UW^mpFKF}1^e?PBh(Dq3l0F)ck=w~4wEhLJ-sNaWX3S1#MQYHz=vO9u^#<?Rwe}lK1oi}vMMfmSGrfO
L<jr(529~B*?;yp+Iw(+@9Dj#!7x}-k?=e@j>;r1MyKI`eua!HER$>;L9<F=626jO#p`hzPxF%!-
|$!Y;uI>*iwjQ?u14Z4O^6lHdH3F@d%zl|_vyjj!Lz5)y@&hXy|2+*ou=6th#HoD{gW>w?kXu}X%<iM@h^Y+hkquYV}t0?kAGi2n
xxZ&pZ(kaET7Fr3jz1Dzf{law*T^{fADj&;r#U9{g!+>I*luS_WS?(_2<9)`saVF(B$K!ps~X5|M)-
1H}fK|Y56z*Nuh%7k4IH0o~x#eibSD#{U`rLarG>nP6hDK{<KCi7KnfLa~(0rm3aIM#kzc)3x51WK3i1jG_5WK#R}^<nZ%1}r9Fm
jyE2-
_Wf??Do>3sB06t7#rrCf?hv6rSbXr|Yvj9g8j3I^zPUCDmO^Ooq${2=u2}62x+6VY6R1j(nc$~#mRYZ9a9p~eVPMJ(6y#ODTQ4ya
H0>IS^@Rj)b?pbnC()Vs~?Kb{pLhwVyK&lW)KbprynM5yVTtnGWNV}@QBrgKM2kI#xwCV+ZUc}Qy0@$cr|0Jn80Mj)<(g{PE1@Ti
Ppj<P4+Xo`kd8aNaUUslq0gw=eT?Ioxq)C}YED4chE3vGjFfqH7x)MBUWFM9D@a;TKmHO_N(<GU9cDirQR$z-
FDHsl=IQOT}gwW&_zfs5$LNvK!vRd#ge4d5<ALeP+aahh6s4&$Wp{k8=Ch6dRUFvQ8hTY9|7&yAv6@&!)B0DKNg6=4p&0*NAZ(ot
j^T^XkK|8aV$pl(vv1n?f%5~P)0rN!#bFftdLusNK;**e?guU;Gpr`_7d@9>0z#e`ubBp9hi?m3_p^3AMUnFCsL~E-
cnVU%{I*7vCzrOlJd8n&L#15&F^{fJYo4$yv#NySD773^)gIV;5xpg@f>QqOvKGCbFmOF&Gfm9H~Wi2`}Hc$RcUZO=1&Bo#C8`{w
{kmRtPq+nKX85(bH_X-
m5Ei?{99me<NXvr%WG>gopLlhyz$V6s)lEGXF#fLEIO|IPp&L%~X7v(SnA)Lk|;Mn0{_r0B+oulTyG3t>$gR;k(B~HZ*YJ;#jhn?
qpPZ+#!w1=1Ib?sr5R#Wj*VD$BYE+&`i0$UB@M~-
))e33cz2<Mq+<8e;78pgP{*dja2^7Bm2k=T17&xS+QlkSX)R#fYJs(xAXsyQLn^Q(GZn<+KId{K;&D0u-U)Bu-
I!DqpvJj33^KfQ(-
8O)^bko^=OwL}OQQsWm%QKcm?9IdU>q+V^9wij7hirBY2xeHk|=U+!Mjkl(h;!te`Ap6+?2%(*5b0_2e{Gx7N4M&zRuwocUyGp|;
UW&mXY*73-lLs=qKRV5GU<6V^?J>uRe5}d+B#9J#su&FdtWc8XG{YK9Yy-
t$1DVKhrNoRKsLFeRYSchhu<{KxSzuk8Wt9=HU*5dMUd=BkT&sA(Pg9b5W>{JVa{dYA3IlsL{J+7s@Y@m@6%OVwcf>%+AXrLdtDv
)lZykZBy9!{<Sd`th0;ZUai_{2~lZ#&g&m}}3R{iC93KMfkLgzAn<GLo{5}h#}`2ZI#$!z7y@@2dI;hkrn1k4B4dB5JS*U5RC{SG
QA9-
YGUQ__;#sC){<m#Du$W1;F2i{a4MJecQj{_ygg@iepgQ68L_k`26$U&JYS_JHbusSMvt9NmQ(G=*uhZI?D>X#T2|yN%7#>}^um%#
v?A{9t3pMy5~a2!(ynh}BUbXrEqeBt<$ln9$uS#&Hz`Ghjyl<N|nce_tZ$lj)mugyGxmdW-
f&PpY}W2GZ7VqiISb7+r@5?{+YLSSE-
u5&F%dbllOo#j9)WLC=c@iSxf1#dCC&4Q;OK{0!ZqZu^^hhlSo8=4MYMFGtC|3hvP#^ex9FK5G$xJ;E7GU~Ca$fL>`jLW<urHe_p
KPj`~hvJ%W{c3(#*M0qxqt}?;v0qDp|*p_5Y)(-H`EGY#s7KQv0EQrDv>N!pxn&-
V=F6N*W%d(?*VX5{}imL*ksUzw#`$4pcfNX7NwiguLa@D1wKC-
buOBABUPO#AnyrqU%A#v6l!~}Z*F)tQb5(#d29da%H%cccElWXp>=DF<J;rbC-uXEx8*noK2410!h7oGIDbX^dnk7IoiYS&n*9RS
s%U`)vJ{b_!l6qYLkeRv3jCP9((%lR~|Iz@QcdtM%0#l@d$iX$pI?s}oE4-
2A}j14BwlqvDBznFuPN;*rmDbhoCJ1o%TmuQyE#PfnTm_S%&GhlfcuIj4KU?m0&n8hzUJ3SgI8dvcpBG_TR?sSbF&Q4I9pvUkK8g
v9$4v#bu<Z*9zrRJpaXcK*?b}b!&Qz$K3lWCclilJ*5Jc=caOvE`<Zp_t)-
N6fR$O88Te#XgEV(H6`r^CTDEO6u$K$`t%Y!oolC9y4VHRq~)0hXI6)DeGOV9`DOcn*v6F&NB(Cj*-
5?K)x3KLZ77nJs>rEzAmWmJ2l~TNGNo!qTbr2@OpW)v7>enD<q_sOF2R{Q7-)oWQ6>Ys1R`54TMSlx}bT&B_z+bJP*=j@<kfE-
yT?$nvBRTLvLD3emv)0T@k#vxnBEOFn*Z%PYhkv*6Yn;c%t+>xm!<z+fpl;+nrBR-
jO4`3uL>yO}U@6&s17)Q`5*xsM%r^C%_X#81so0>_+F_4eoa+)#Ht(4L-7@N!Y$7%W94U!Q3bBe0J4n=OVpGl<PK-
wSKv%FmL_bRW|ro?2}Ch}`3+`E;BV(#FwDC8tT@D9%O+C=$ZhvVx=aFu-iqUv{&p({Kn84qun~IbP!~7qbrHM>C-
8Dnp`VHQ}w3c5lm$M>ZM?_$ClXjO<cgS#p*LB7P(w;}cBr*?gK*u=ojstJXXpejJD`Qc<;>&ha}>;UNs3Qw;5y;if!PXwT<{yPWO
Zx3dF%X#@C8>{)l0O*EoU+zWduY@$C-
%TZi7+iad4TaVSRTFDJG+t#u_DJv&&3Exb~)m9#phgPp?+nFZa+G+OfSU;O+Ti0=A3ptUZi)AAVVZ<b}<D{L7tzH^*has$7-
qxNlpQlmQCj~(^3q<N6wHLb#B}`ul`5XI0pkn{#Xi*ese(0na?eADR-
7DX?yLq9hZS`W7jMG@XFrA)gt=Nt&DR{MFum^}%Q7?$tc|!Wk+Wj{m8wRY#76Y6nIOrdGxJ_+n>!ubdk&Z@xWJdT5lp=1Z)quhAq
N-qgEi#x0=^c7uwH>!2Dd%}sYSk;RPwmcOQjw@ZuvD~37m%i9MQqluHO|LjpCGEQnFOVufkse^4&D~gBGDHhfcY$f$#_0(>>{C9M
4%w=@^65f%!O#dF@FYLdR7M>p^IGu_DYG0J(`5ev*cn0eM%<6DwL6AJrOkqgObqn$;8k#KqI9wN>xNrh~COs>fk*N&+-
)ItCr0PhDpLeF3;h?`Dv2LEn_hE7iFs^mGx7Agm3Rp5^#?qC<rA+@)YPetxk)4adJvD(3Z(rQe?0?CuA}NaD&R}>1i^ZTXkRB{e>
SH;A1<Z4Er~qs=Z)eSu{2IyBVM7bxMg{27+&%XP(ZJQ98K@VqRkMhE&o&=?4xMIEF#Y%;b4DsT}8{(wO<FBtEqRjs$t!6tNOTxE7
x^=v#nTpf0D-
)PTZnNW!<4glM(Z5B9YEB3$_e%dK9p#lxc{;pkZ8&0^#q##zF6=vuCIpB|Bo;x_e&?nC;1w840yP(t>6STZ$bRy8ot<lPC#_Z(U`
PDkWx>(yR2bh|ChnG|_camQAGjFuM63t6dB2yO>ZRf;Ggh#qw+cZ0Vk4Wy$I5xgCGLQ5mL+VB*erWyNGFgEyi?0yW6FM<&$;S*ev
hDT28n8><aOoXR36g`iv(cup1&ym{}Fr9vwI^JOUX^0PZ!Tj;!4xAf5?tpmW$sHI^e7OtbjW>6|yz%D_RAW54TWwQ(x&!HtS9h!S
$FI9^-gtHg%p2eCsnm&g_Y&sDzdK-_cz6fKA0MxORy2EvVa7nNEVEZ(*cPgcpGg=5|M1trGFt_&KmQ_FDh+{EWVOd-Yn+rL)U8`x
VP|AG{`ho?jnt)vhI{RNc%Ch3tgV72HA8Me6T0rII{*M`z$)~p4T;C~0zJ<T()j>X$8_2>o!!F!Y2*1eH6t!gXp$+naiad%EIX$Y
FRZ62ZkvA76wq(;GC8Ii(cL{9eAFE4X_~sK-nVIrxEyN?*2Rw%Fh?|bB+VDDyatF3A0JS-0b4CIU$Lq-mCUuhvmz2~-
eg6DBliEXV-I5B%LyFl7qfj!R1kvo<MG&%Hd;6O<VNpH)O%|?JTA}H0wI~}F>!RU52{g^yS_$g{9&%*Awpi!;eTG+8ecS<)`*L-
Yf)pC`v#2Jh1EM53i34l7fHl#Te;03&h|GxmeEY88_`N>^Ma#5NHw|)#ngp=4hJ_tL*Wqsu4o`gUYQ7V*9wJOYjVb}ZLdB&*uT5a
8|NTv$r#jQaMiZ9u|Mji`+BJzP4hBw&!UJPBVwAnj0i$ox*^y~-{@~Zg^v#<yU-dBi6X1x-
;iN@Fc~SPl>uXZOKkIceJ{(icuL`9KHjx8`S7SkKnS;TzOHKrdo1mij9-
ew7UozJff;EwPF^zKg~Ik762NGU@yoTYTdKyDnw}DzBm)Zry?LUiy>SK<7h(=^Y-
0{XG$h|>8vLUn(&LXJaHY_z28e(|z;a{)Q#EfvU|roc3GWD>GWIRZwi*drsByNAR?n@v@v~mQb?CL?K2C6>>Ki2`^`;=JW7?t^zk
C~t*4GU*w3rPT11M_O``~T!oV3+9isen>|MoO?Bj>q_M)`l+yidldtrG={=~xQ8C5_ivavp7B?*W`+evrG_jmaa+&}Y@Roe$IvLX
-x;K!GfuQD}jFTG{P*(L}K4svb26zbPLqMd<;aUa;%hk0y6CM2*WMd7e@5&99d=u1b3RjlcZ3&?tUe!(&~G<TMQs!3NeY+12A{y}
>POY&fl{uv~&7U*x<t`bjo%>}%NB_O(ga*!cFFh8}fuDcc`Em$U!fx%5{$rEnl>vu1mHGrO~n=MLXs5ij@aa95lc@oOTaFTG5EC%
6j}>!=djUZ)8j+exONvPL<WKci}T5zH5W0FPfxdGCc>O=(u9W8U^f>R452XrC^M3GfDVAjP!h8F|TBQ<S;bF2+n3(>$LCqOy{=<A
}jEGH9pNZ{DO25)R`5aCufoyS&6m#45rRH@qc)q?a9uP<OS&ctTf|KOB)UOnVUOF@{AP?i`^#t9<Hx3Ro~)V+JnwBr-WSdn(8X5v
r<;q8p3z;ivmg9_}3k_nti2e{w`QbEuCx6sU!}PpY#tqJ_{biKbOQa0Na*fX+~@XYuO>=Sh(SkM<9O<Yh8i;Nc@*(R(wHx&%*ekj
TU(D3vlm;V<zx7={S^;0HfYeFEQu<7qxR^CC0po-Im_@rZ$AFaR-dkD?v2=>^W7FOnko?$iB8wXiljJqe-GZ02x71#iVD85?Ib<p
89AzxO~O<0?S7^8&cocj6sPK#oYmZ+yW1NKg0Tl6QG+a9OXMw5&Xbf@?ELx3cnDpSvSeV8aQtzsQnu6wed(S~Y><DTT#xrwD)Z^-
sQdUcO5)zrA3yGPkzBr6laOR<ajNrtwKR1i<?)mPwM0Y9&I6m+tI6co3mXMNjVaIcJmQYy)}Va$ZLyzv}ab<gQ0^InkG9Q(W^Q{7
o1#oo@|P`#wV@*Zmf-=ri~SFaL2vgM-fy>(d6qRy}5&$y8A4Elcv%dngLVp*SGBw9N^62`FlC%yvP5w!y-nw}-
)wYmw;GsPBhVVqhrW4axGJ3Y^Cm(>xycf+)$xqM|<b`rQQg(qM+~<IFLpUmaDG*TPOq%DV#H-
ce|A7u;iQ;Rj6Ol8ib6<)MVncqm!><o;?9ytNK$w=ij|!f&zZ^ymY+6_|IU+TH3FywT9jsxXRdR*NCG_Q$`Nlb_~uFZkJ%jh<#UH
02G+wa--ggu1LZI>nqr71a}q5o3Z%kLHa!W@9hAI5LuJJj*a2;y3_!N^zJ^#JLa9F?awv&8nopkg8cyo#x}RA3RJ7Jc}~I0~A-
~b|e%p`?bcoL+3|>cmjokNm{@xf4oSi<BtI!EYwpn*D=CE>}w^3*hCAqgJ_Xi5Boa7x`wbL_GQaKi$eYKWO#G<uo+Qj6h^zZx|qW
(o}R!8DLG`=Yvg9A)f94JVDZ<ChM`CpxiH|ZI&va7r!gtpVI<GbEmuNabY-
B7<0sb?2A1k+2@^eP11UY^a|1FVj2+5_l;hhgM)Tw`KR5lNh->0bD!ctUxT%(GFK>s0*cN4aX0MxMzP#4-
G;cXGjrNL`y53hRN>Mw0SigPOz=453V3!SG>dxcJm-
q%hhEZ7Rry4iPlp_wZQ<@9Wp{`X$CWZ*c9oi{5tpl&vz@f=#g@ZB^kwlwiB-e+vwQT?(`-
gNyz%(tiE*LhSjn}(lsQ>7>lw;Qn)i(!^=#pXm)oP{D8AJ1D4O+97kCa8Hz)m~vdy&Zy0eo9_LIJC#X_B2{SfM&f{qQOJBDHsYK6
vEl2OZ=zE=8)1X8%=a7vciaiN^<KP=mNIo&!#Gn>0Mw1T#_W8gd%&nDlsnHe7I<Es4PlM5Q|sCl+Zvy}BKo!;+VIJmpy{meU>;v=
^lIh;&G-edS_p)ihkyAo5|UUs~xtgnz{;p!r+8x=(0-1+TyJYDA}i_RiIlHne)tpa5-
n^KD%SrWH4Um1ZH$h4olOO^Mk=1Z3mhaT=HK_eILV$XHObW8MjN`@!85{aJiMj0|Kfqd?d$g26RGg0VP-tr^j#0!GM#R>GXc>lZy
<^79e3TE0XWdBlKXK2UFkj>*q6%x`VwUpD6uy@hv9lhK(HXql^)jJ7^lqw%OxoCyebd791x%zKf;qD(_HO-
|y`g<|P6JxhW*|MIq;ad}(hS4PZzZv%`j6)#|{vKe4<*N_qmhyGJntp=}b<)wEQ>RM2qWUA?fdODQH+;X}~+I!7N%+-
K*(K2UY_u~p>H?jHX7LEi_$QQq$>Ku~L{-x7~?NeCn!*0U$V4*>7k3?d1Z8%u`b?UAmH^AR8;2MqRmfCQ#$)_(8*~rc&?bEt^O-
1GsK`XZrGp#f<@Q#*US}3|^o0I3*KA)Fi_zUIXs-4`9Fo?YMC`=J;Fh_ipwiJmk>xz3pHoO537F9l(40rnP-
)IYwD;FoQ%&hoi=Ohg7AnsDAVKk4Ig1l9qECordtuyhXc5Ue7&LA+ScS;Z^eCu`Q$Yo7{o~TI8S~7Ia96(5j+5|WD6{zp68Ln|*`
o_NOS{gjs!>nC3p!QJLcyOYe#ut%H{ms@`Q`3m&9m61TT<r1;ByG}`kyP3+&&()JUWkj`GH-
O4u`F|%Ni|^)jg#ZWiQlUe?(fyc02rfp_8)zE|H;D$w_gSvrTtH^bBwBbARRvhQvgGn{E_qSiU>chepLeL8k*QXxg9gWBWsj2Q?W
_k>9#D-
WE#&)@^<5?`u;2jRC$(;I<QvMmORQoD}J?Rwb_K91}`Ne(brxxQg9JhAs7_`k30<YGfz&wW=Dh+T+;2eC=d|uB6o9e3uZ=R%mPs4
i_-Ees8%;FFPmvKMvePgbkI=zZ6jU=qKG!E6>_5w#6HKPJNF(uxOZ3ef=DQQDQPs8J-
DHZ0tqH@PUP{fFR*rzfiYbw01)8$G##b5;~bY~_MY8Z+V>tmezO11+DK;^ZcqZhs)1lcEu7}(5l;rZCw^H8g2{+RIXYdL<Nbc$Gb
+}|RD*{DKW&a0jZJ=WBm|rJK=7ljdY%24cYu>3#H2pz5*)|aMWE1xxl^VmS&aAan4*%NQ1(2!G^ej%I;N>(iZt#?^YMf9q)$JR3R
W!^O^<QIH2D6*2Vx^N2SNWBBpMG1bK<0YoNRM|(>5M(+oq#h!EpgY0t}GgIDut*-
xQEdw`7e{XXj$e$l4oHS%T<13mPZfGFKTehC>bdNO%Grgo=ob5Z2H~GHnk2a<Ec5+D#A=;E^x(57FozhmFt~1t_k`=d)1gwE?*qd
c6Rl_jx!JYt^~+jaaLoiM5V1L?c>gs7*<h;DTWB(-kdaIBzCjW)a#i@Ox!sB{IbiCq>$%4zolZtLDkZBr=HUX_uT?l=-
}QkEj~`BWLqbQ;!%26Yy)i5h4Pl=wJ#rP&T-
h#+qM9R}tnm$`bds1ImpRuc`GNQhVgCmgk2XDU<l*P;QE*6&H%EsTNlJ$MNW_u{K6x*QLT$yebLRcWb>aFX^B>pU?J%QtA{D_PS?
EH_|DYHdKJ;gf_+=+gDdG>ZT2C2SH2b2Z9mDwF<r-
#?=v=>2xFAz@Td?6;PDz?}}ZW;U<N~lPFSJcqP8Lh(;@oYn3Sk`K5Q$lU_yaHfuOjk2Ul;!#UsD7H4e--
TSnHpd;#|Nz+1*A=MQ{K{%eyT0x5h!w3)(y%?aheTS|$8jk)2uf_@G_v<-X!sW-
lGD0wT6WG~ia4k_ECZM>Hs0ngys4;%T#*thIn#N=2-FKOdwgc8Dk@dYUp(|}xHQF^?jn|gxAFl(X;r0%H*KOiL-jo+cLEkpqP@pm
`V2t?KY!j40TlYZmgW>NrQhOV;ezj(cQ#QJW_fSuLzFBQ-b=XgN4{_7_5!S8$Yi*s1YCJfucmdh3*R-
)J_fqW+Y4^X?%WuD&zuiSSe%z68$)!4e+L!D2X$}yZgwOa0f>_GCN=bgCQJ{x3(rKxd5IAc1B)lV1UA9-
!_0!H>>3`SaL%`2EKLV4u#+N{dHuonOb&sLXhX;kv{n3y)&k%U;Wd)YUr~plLF-
K1~{^=y$e#Do)MF!kBsp6DxX@ucXM^MpBl;!e$Xd};yNDVpfDHg-
=#_nHAI7Qbb^nFKI#Ab#FQd`Ovc#peG!n;fu016U?$KMMcewx1IFjiD=?Bt_+4`O+^L!2R?y}H&cB!(iAXUmdi5XB{(X&!EFG{eY
~B2;AEB%|TA)qeeI^Eeu<Op|tXK;DohZ7MQQHcdtK$-Bmh=$jhBV@QR(n%B6Q_b$6jpC-kNbR<T381evP4ZmF^m@N?fu9%VsgB>b
LH5zBZaT4HtIw0OC@A;zQTz<kQVcppqrCC}<Q5|M$?&FEcN6adiYN(D!w4yQEicrL)9%AZ71lBZZxzc=@VceiW?bvQmM~1G8OTwj
LKa`hIdA71;aI$<W55D&4;Ok+_U6Y>MyuGMBaEA&}jov0iCH2=jQs=jdo9+cxUs-|F*b6mbc$Pp5B=-
bmp_Qe8hE2j@2Pl}n@FwZtqXG)nNl;5HK#)!&ikeVf-7e^sFH7j0xMoZ#MVscLW!%k_Xv!0>91hhL00`n+t-
~<O7UuMz<q{oIIVnp+_YgJSU_HeDTa#2uWd19u1+j<<JEP%N>zYf40C^;_tsDHfXcD|yKj;CNI<2nD$tUH!_X_o8Z}mhH4SMu(P=
oP+fn{lh@n&~K*v?@sFyenI@U~QsksDG^4XL8qJ(4WpossUewA-kdv~l4ZUYbC7)DWIkkoh7vN5nZI4XrD$sJ|Q{Rm?*Xx;5}fW0
rwk=TCU6cXUSsrp$j|{C4PwWpwx6r+Z);u#$dyuy^q6X>{-5{&(*`b?;6PNd#NU_~>^<-
Hc%OCq|>pT{8VXU!Lm<aKGPY$^CT+uA5H72)FT{VKG`G59zDeA#*0$xaWyq)UqcEux2q=!AjS<BU(>Ds`^JfvTl49IY<Q*{;~jMR
!#xImp+;xG6AUop`SKLoqtq9i6<7I%q=RQ=%)ozCn*&`;(?7xWbKrg@TUbLvvEou;ZN=I>pIJ(FZ2O8zlki=(9S?r{o5cua@^T>N
!MnS7>EB93#23VBC3%&FY*(-94|VKk&I+cm-
8XADxQk(=jpgQ<xBg9!S0T4xB+m$*MsefvRVLprQaPk!<@_TM1pB2fm4cNF(9dGF!V6?kADR3GQw?H-r-pI`Vapi1TcZ`Dn9sc_&
^}ICf>C2MaFcPDvM1GR!-KrBBVN^D=`Jv;C)1P7X7XjRkfH;6Q6}jca$2I4+;_{Jf$Dq;MTCNgcoM?;&7mz9${-
SNJSw<Dumgq<r&RS4zJbp9nqyL>UVHE*l}Vs1tk()7l3we?pSAswaVnz!)pZQnEQ2OdkR*YFOpddhUO>|x7svVN7@lCZQ59CJk@n
uFC-!EWA6zv;Yl;kjCl@=ktyvV4V`9#;1~}Esu%3&!wy9$7qWC&vroGlz&`m{17X-
&id*$Cr6yC0K1xespVz}1Tkzfo4~s5kXi^`no!T{{v}sKzG>Z^S{kQ?^Ba4}DGSQc(Ii09Ct%!QkWer;|p1UCM+VzH7U-
>ND8f(w(+n&MIu8maBm!#WQ`bkzK(>9~JhPcZN>y#uyq=-
<1+!WU|!_+jkcQkaiq}Li;9)rpBAENHj391KdO_Gneh?1H(Bu>Ix^x{VgjM+|J&SBMvvUdB{@$IEyId2^=j^PDnu*PKSTiq20q7(
L8+sC(UUo4<To8k7dCSrAKn;rqUs`R$Qq#E9By2etov%Yroa08n(Qv4$3M*h*CV<R8rC!A8hwT((%Hfy2+->`*BU%s_wj`OO-
X1@N(7u1!a0)HcyhQ3}kv`x<<LfT)BLqH(sgZ}PhRkDj&?6Wz0WZ_PKN85v7g-
yO1x7k+XPKtEQefI}nVyo~@B~9UT9(EoM^cXp?(_QrfyTRx?bxZP1nnqEWU+l81VcpX7+$ikrX%zlqk!8qjsT{-
CfAYKk`^(=8O(>irYmi_5^vC}`Y(YcG;v5!k-KtKmF%J6wS~?zvH{N@1XXpJ7K78-
S`yXAu`QFVNJ2%4HOv0^g34eR5iTau@S!Y8nH?H4!Z})?bpt74E?S8nkdo#R^t?<@Cm?=q{YO>7)sXE3=lw2+};`6h|+n!D8AxIB
{)S6<R6eB)_iY`~YSd9(&-JKmU$L*B>nDoX1!eiQ7OIX52$)|bkVr{JQ`-rd!D8_7o>1!Z_!x`0C7fGs`%8Ir^dHa!7LZ9OS+L-
6GS9V3>T{@!sDlS>7?k<(8o1ZmTvN^QK3+^F_j0k5rEoG8ou0Xs(kFbS8(A>qiDbeA;5%T5|f_Ix2FxcjO-
d@?IiyFgA7Bn8VmD1a{aUr*j?wfU$zCrO?-
^g<HlSX*Gfg6CkO|u@iR&?2d9Oi3|1NIAfg#_0X_Nc*UUTB)mB`x%$5sIxR1C}4zC3I^C!S&xwunM>Fz=BqG9{{TF9vF#CefPkOK
!aC8cgtm-%^_)siH1zV*T45y!BRKRR<0V6_LkKJ^$WWeS`qt-fPrQ%rB^VKEeU*OAAbwg8rqM@SYog2Mrg=ZYHL06?X5pdU#6M4v
reK2UDlJgOYp^%*;u-|0=4OGZKCr45dN@|ckSyP^|f33_z|U?1Jj`wc_cSi!-iAT+V-
m`(rcr`PLijHX(?lEH)`jwn~0^gI6ZQFUE;CD(#r$^xM{HL4(T>HGOS9yJL&5-&K;AH=-
}O}`l=q&d%^Lq*kkH=D0jJt&302~IM!ZkYu$zzyZWsS-<0X!{FXOdwA-
^{9C|WEudzI6;*pl@w0U>#&1BTO5onPvy;e0IQHuRoYsqIY(E!|lVbW#XG$jf1ZyAb(ihgo|{Chp==d+z~<T|q!CHA)7K)UG23Fq
1NYqF}<_ME@GeBV%>_w2ky@l``9v61I3M(-NRiQPSKIeOPrPHp-5i;C9`rNus=w<x`9D5o|Dy(PulraF1Y&|fE=*J<ca-
bVEICBAE-RqXFI5$kUM8D@g~ruH3KY$+s08$af9mqyN;ZU%0m2AWpa0=+Y`YYhKC?F%&|5p3Kg0)~GY!_=|C&d4`)>T2pg)m1~*{
{Fe4-rcs61*(o4YWs=?i0s0l{NlVGI??s55%b1+X=vV6V03WD{Mq%ijiTq(H(#biwTHzu?S1>+ql4(--
uI)Y2lpO7HA^@fNkhvRun15t+@b$^aTDHL>xd%e!;V!2t%U?6eYXLOWsd+97p)stK3LtOxy6T?ePhXnvH3M@vMPF-MAyoPmqdm%z
h#}%pl&wTD_<{1sUoda%NY8-4ne@I4<caIQ7dxnD`-
$H*LUa?#`PWl7UX(lwP&Fh+$3B#HH*v>QBWsn^6Mjil!xjULZn4@^gMf7dOrLaAgg3P$@Zp5V4-o{P-
MPHl7Z}G^{Sq&rY*7bwzHj;n%i~Hv!=2@e4d@$e*MLdKfARpeu$e>Y#-(-SUMi&Rd6er-Ck;zK2#1*0&S;MZXf~?s<tn*+HS?cX^
~8ZVRbUt-X`4NO2@+wc6N7ee7N(``!_zg{^9kH-
n)5Y7k5+s?5}QZ$G89CPlH>>x1XTPe}FrDvOd}bSZy!0%>Y?_@cQ%rNQLNl1@LOXTZ6Ksd>kbcQ0<jQwa&>~`gcF!H?HsQ?7Y8w^
MjkaAML)s^WlvfA0XlX^-Cl?kUUr#-
l3IZ$A<mZ$g}sZf3SNKD7X&1yK&<~;@Kblxly&Y0W6*<F0}9ZZaLzQQEb}XrShqs90DOa@{P7{WPuQps$(EFPdL!6K;)+l_;wPby
g6*_w|J2)AM6YLB(RO*&2Hf{U)rsOoKDXyGB7}d8?(WjSby*ii67dn>3I~AYQU0K!Md+eM3mtP0WEsp;vtup$<0^Vgn_pmlZEL47
rG9kBn_R$uMhbZ=P_qAUI^~h7BHFf++dBHK0w?AY<YR{ndcNHukvk=upRf~E67*d4Vt1>JSBJm>J7W`K%?!~?gm%%Z{jmwHA;(@t
=>7b#gfNQqcu-
2*ID#b>w2pmKWi*|0peQs_<5W8wN$&>ta)Gjk{X2aCRlUaHBSEWYrjZn7~;h%!BsjIb2SK8AtQ7HibXMdjjhrjfH6OtSG8l<u>Pd
6c6emaPd5*81~~IBTVa<^CYY4*MPgP37Jaa5HIOQhi7zMNk}$9O@<6p4?OR8+V#%&&W8?{+4MZn@Y3_`0M%jQ{jK?v6s>O&;AZKH
cn^8QKM+<p=wDv|OP}Qlt7^0PN-UR32Z{&+0E|PjD0=Y*>Y1JgJ5{rX_WSX25@r;u99p{yOb62>RmFG#J^80O-
fw=RSa#3R1)p5!<%=LofB26av1sgfXOWRUBCVb%_6-fjaBK(7|_v%qfHoSeLN2%EP0w-
2Icvl_X;p1R>R`Tt2Vx>3^<P`^aj~HKvm(r<Iy3u)xyHV5R1*n+5?rW$SAG0`#i!It&FMvF|PvVV!nTKtI3lRUcV>NB=U2`&nFH}
c6F*Hu(0Ff7RIO1%{$MfuYwueon%mtDbCmc&%D~D`eROu9qNSSAQoR3OuntV(hg~w_!v)>ri__%?`O53^e-D4r8<-ECUblHz-
1pUq^@9=TX`PDU9_LexAtSz(-
LjzZM<R0?T0{F<NSN5H4?RSiTCUky#oc;M^0yC{A;p$!X%i{e!PrrBnG53slvmQx4T}CKGeg*~7YZTO6VNOo$wIVIgF2tRVrT4nN
2k9)W2EhkA0j*K(v;NMe`njLr7W(*}$`Y@99ic<MxKJ@p0p}_9(e)_D+&nQ-
g`SswAPBv=8KJXeoGxaY(u!n)mYOW4Xp&L@3W#V*cbkKnLN2nl%24N!C#{W{yBiXDnx33ClUSsqQ&Pz~rJ#{P`<C4ClrH3DKuK0%
te$Mc0uK5*M~~D%De%*ac@BM0Qb;&z&kQ%bu}yW8SVG#`bbUh!dD-45PELW@W*0Ou6xV=aJgMK@OsI6M3-
@_m0Oci+HI4D+B}!T`o8vVGcavoPG)c|?@M4+}BwBCYcHPfL(*;b9HG8%tceXX2@Z`e6p@i_mowdwZ*~1@~J3<lAB8SyPPdz*&ZE
&<krGv6Yg}6e^ZmV&y28v++(SzTh@ee(Ga*CH;o)3WQBeVmcDHV!TYz{!2H)R9ws9E1sXTzm%VmPTvCf4nl^L(0)@UBwPFed>?_$
eMoOHp=dboT-vC8>C*;VU{b5tBiJPbi|8)X9L9p@Z+Aa}POE)C<lFuwen!1(S9G<`Rx-(OL{d$``<-9*uf6;+qD?r}-
50pR_}$Pp2pkL42IQNF2tX`GZ%l3L?OI$PyUS!6~Tg>Ntrj%Cd|QbZ0LRsf;AP64k!7mk!{&9UtDGhz1$VLSB@>OjsKZoFe*luJ+
5VrC7*Xhb(%0$>Cthm*Wk>TNfyBbWJRESw^w$E9meor#8Qd;Ij-
+DTpV0JZVTbV{UFR7;}Ehb#Q*`LBWp}WtGbpu2XgcTR|1o3_ZDaQFcS)+D6|fpoBbpa~x%5W7}50*g@l3PgSBhm(h)H+Ls1a>lCx
s6kU4rd>D4AtaznarsRMrGgu*?=C!%B{$6guy{qnt1{?xQLPLwXfWN;0ZGl%gpf+Rkz8~x@V1yR~0TI(LFmrL)bQ-
^aK{*;xR`WbqqN`&~k91c&Li0H;PRXKj2G;ZJop<U>oyG0gUJVF?neSaBuQ+7^WHU`0#q@ZF_b`fO66po<pMn8$4{vPd(=KUA&`N
>4@rZ{%#8qvypCuRYhFw&v9w&GnggIr}0`jLh>Rk-t_6~f95VQg)_0&Y^dR{hD9tYucqzlk6IU*$?!5Tzf#D4GzWs%2qJ+AR_uHs
vx?Iq(Qx?4KKrE9EdR^RQ~Za40e@#<TeBC9!l7rM<q4$yWe&Qoj@FQJWlu6?tm3a7+mU1GRFE4MP}!7Y%^Ct`TB#{h4gr@@OL3vG
Qysb&de%bk?NXI@B@^l@5_a%2rZK~B4Cy9o&>np7&EyLV0QTP$K(aoN<~<NKw$OW<U|V-1>5I?E-
R@}$0t9gntOj#I02NF3*t%y0^tA(^Bv`@#1TT<TzIy?29!$j(Q3-
A!Au!I|J)tIU!ZjUHME2otFvuq5G)2eC+q<Xlv4>?;^Ehqa5Klp1L<ym9lImc=BkJxC=E;oz!?Os~bzt8(sXtxei?2m5#TS?h>83
{<tR4v$@OY89CJv<b#Km#Gs4R!j$YP8aRS^2k^DtP^r-RhU~|{oSj-
c=eZG{m!eu!Cznf%U6H%>dRMu`|5A;*BMx?ut>nrt;QyaXoEZ+%M7ey4%aAkXftqGgqq`2C)!;+crrcEb5H6Ddd|s*eQ%0np8K8y
JAU!%zx&>N_1nO>|A~z9l=@#-
>Z^a{fBV(vul~oYzXyoFe)Z*7zxC=DUws}n`j^|;j#SHZZm#FWhW2~goRyA{aeAy>5UZyv7dE2M1Pzg-fM=vq2NI$*?~h<bQzcQk
IL6l)JXV6Hvl8_Rye3md=VKA~f!d^mg=P|sQzxFJti~{J4`qFIMg7P3AK!CelcHD;t65R@of}+TPoQ#|i$BoFa%C55>SIF}Svo==
d$&gkTakDxhT>3Vd5HvszCJYx6gfC${Ra%s*KygRH0tAkwOn;fze}CZfTvWcG#4OUV>Fn=Rn$wJ{4JaOt)o?`UG<eO*sw=V_Qg%{
;i8&cy9r8&G7*-;P;8HATL;W<X8a|Jsmzy?FnI~RgXM-xYA`no9~i4;P+CBly@VkwR}l?U4oZ9pf9#S#NNY)a4<+G`QPRk;dU)-
F9ZJ7(<w}HU?V||yZU{DPN#`WAO6W=9CttOkolvD4kEXZ~&K`{)iM-cZf*f7>KTt~p1QY-
O00;m803iSX{BTpr0000a0ssIQ0000_aAj^mXJu}5Ole{-Utei%X>?y-E^v8`kv$8-
Kn#ZW{)$jHK@oIv^AkjiVmr8=*R%%Cq~4vP|K0;Xz~$<aK=LHK$=iW^H$U_?q>&x=Rwc5hiqMWBTNO!~rrQR2Qin1aIzlBDX4m7I
d}t*}W#tV0ow?S;?=)2ofzFLs4_$x`uw2v_mZQP&jej?0bSHLkI8&@@wEgWQN9Ra5ju%o&j`kMriGx3y-
GW1GnfNIAOUH&P)DLZ1RVa-oF(ulTKNKQnPOed2pW@^mT_eHFmuXRSChYO<TORfVP)h>@6aWAK2mk;8AppF~87MRf006re000jF0
03-
nV_|G%b1!9XE_q>XY?T<vZX?I_uCJ)*VjEE?jWk+8)1WmTK!H6Y$eQ>fpi%5Dl0E9KqPwcakqH70;siO^nZy|&abjbD07+oLw_K7
-K1M%~`GmZss=B#&yO7;)tGB;bt(D3Wr=GbJvH8Txkvb6_BSp7TAJ)pc-
sXlj$+fx#bpQNJz>~<W(8h_>=wUvpE0uM`6RSig9gf7~iPHU%(oV=pj(nRN1DPe0%G~6cs_+nft<6-60P2YTjm!%<DB$Q>fZF-yh
N>!q9F0s5nbAK`xN)wpb3IB_IdQkajLWeSrO8ww#*$TaV^fdDPTVTjX>mDVE2L9NriQXEkheQ1OnUucZJg?Lr5IOg_~zB78=Y)#t
I|Bp-^#N$4|eYD>>ls#AKp9IJ={4s-
aXj6+U&i0`RCttw`EUs>s~ZtzC9yN=H2bOC+<G}o9L>tH>uP_R?322O2GfbXsbG%P8ZJTb+;Q8MDI%f5RLZl@7zDyKRh@(xPN%Ka
}PAzA&p*qf*N(LtBfA?@Mtlsq|Qt^_h+?GE2l&3eHJ7T9#yp6^c}9*+uuC`O%8XD_YU@tk3f;2z^j+P|Lxt!pWS`)*XH21ei7*Z#
d&2QuqP3L3bD6-lt!q}(f-cy&fdY%&f#uLqr0y@{ei0VwVgu#wp5Xrl1X7ktP2(hCF#3nw7FrObhS-Fs!>+*V}nywnQMuR7q!-
af|4pr2u~!LssUg>FcmV2Y3{}XKoLF6v1S(W2#W+|S`S*{-#dNs_R1NhvRw9yay-
~Zx^yhj&!=OR5*5BjWR^>CL>tYJ7CV#y;Lj=b+19L4)S1j+Z<u7#A@cI^gU5~V8028c%o$T){li~EeW)sd(da}@u=G^c5U-
=URW>vWpjt-(P0tfNg8l&w%M;zmBF~tlQm(qi&W0&U@wM0*v8Ed;EN{?V3{53&O<f5-N)|;&Jj|aFHG%|!1jI#vP$5S$*LW&-R-
=nsmf7mB#HA&~Y0Kk&{{G`fTO>nPBP*cyNrDM8c&bv@5obe?$&A>;q4TQ@88EX+liI=qoD5wNe$fG(48Vngwj1T45^L@9QYDyASO
|mKIitZ5uU>xsjW}iKDjA4Q)z}m~3_KaRhw2Hs;3|)m9MM26Gf;e$3_88??Vk)GGVno>-
zedU#B>Y=f}wy)s+5>=&a<C$hsL8LG@5Rmn%I*oJ@dRclZK`!%rvPdjlFkYe)hkAKL?9J8(ph5&7!gIXefE%TPho>z-
FI9Z3n*irMN&8d!O-
3)Qh4Ysi`L;R}!VFC<9vuK|N8!xL_58dN#=`@?@l^R&~*OC3dZ*iG_whl>sT|PvjPWzX>G2Gf)moSpX>EQA`MRmpf8|2)ctF(pVU
cFTnATl}H3bsORO<V5cgK9SNtn$3okXh^2oIgW3i+Gdw<f96Z@Xj<D6t@Oduq7c$SVjYJep_^D`&l=d2%xm_ahvG3b!&Kz&RGW}w
(g8MO2k;R9})s+UbmXG<(*LchYp`n1=CsA=EaW0lQgeeRhrU?=7>yYT5g_<W%RtiJ9V%T#&5pkOvu)-
*}O!MmHpZ*{o5C)}`svM|lh351Bf)vJqHYQJ%4+g(9#Z9jw$icKEG7B}3j)|n7Ix1zFL^ITE9%NMt_Bay5PwR--P(BO15?>dH*wR
SkUl))t?=6i&sd2evAhiud_^`xuS}IgHO1ut%=Vm~CuXYBa|Hfh@R_hyalqJYOW!MZKwi<e!9h=IDy`SC3&Xx&Zw1SGR1A&;pB%!
84g9o8BT@Xb{$tySr1%DWcF)~&)vmf8!6v`?{!_@aY0cNB@1+W}sst!*~i=%Yt_nb=v2-
rZk1Y`*5z>9hY;|qQ1_hvy1G=Mr`I>XdS@G9}tQes`kq3JILEQl)z;-
BkgD2mtpjp2>Xm3~;s5q5L3RNdriI&U8VS|mI#*B#P~>KrZ)qO2j_1GO|~+u~}z?W~jKQ7rQ{T4^Y%^Vd2v*cIKpxfnsGmT*;37L
=9&IA1tOE4)#l($Ka1<IDpWDRDXY9y4iwz}#F=>s!s`ZbIv5QiVJUZEg|G&sfX!u!w}SV4tSu1%rVpXr(enAbbn*S!cKa!lb742H
841E*4I4PNw5z2%e%+25ArJ8IzWglzd3c?Np(;<rdb@6c0eiK#g)*Ay523^4X3O<1>JzPF2ANorY(ohWt&^0)xQo3qgd300};{d*
wg>BTf<4n#gKlFZh*+vss0c8v;HZnW4<V)v~z#sMRF;4Dh$kNs;4rM9#o^*!J@k;%Tq*0t&Y^dz-bBaZp~kOpu`j@$X6P?-
JotLK`W%^hVhP?!;JHyUIb}Wm<lLq#c@Cqch(}2=xqtL=tR^n1ea{+%g$<T}Y&WSP=*;6SFE6hdN_skjvHWJTQi##q|Cy%n@JMiF
YGbQ0u#gcOXN<MJ6x76S$Bk6g#ROY}J^qqElv^sZfxmtgbT@<D(T63bA5^DEA;(U@{?SfUog2LD#xE#y84rLArQ%>#@1rZF-
4(<pc&$n=JyqgR2?3%oN|(@=S^v3NxtKRQWl<gQ6n9y$qfJ-y&oU|MwgZ<)N_)XK|s0CIc1xHB5Gb3r|PQ<4QMt8iwP-xmOx0ECK
>wo5dMN^Ao=Y^)B&cLArn&3fzU}(W+EBynQDF$9?0E{}87PiX<hphY|EkCb|2|7r5@d$3W~%IQBj6t52aT!F%Mzl870HXwcv56Dr
2$yz_ew*a0$S(<-0fm4tgr3(#m~DjEZY#X$z!4&G+Hbpnx*l6Q;n<%JfD)u09ozWlW~YZ}&4{zNDJJrFg1gorozPvDM+-
z)|)y^hcqUx>HieOW56;CIje6=a61)QXC5C99lQk~6Kzg`aG0P`A(1Bzz1-cfYgr8FVS6;OusKtxK-RbE7J{)dffXg5MiGvxqu-
5TUSv!k*cD_oCN`o#2Np+B=&7oj0&n8c{c<t92y2XaSq^Qb*ESrPgPVAI+Z5@8=;lt?S7GLF06y@m`OsKJC5D1!eid`oS1K96)Er
N#%zrZ8~qUF7YM=>*X*Bi$b^y^@}N9IZ?(kDJ;%QQ~&|h5f=u|MeBO>e^5&U1QY-
O00;m803iUgxWsJW3jhEq9smFj0001NZ)0I>WpgibbuM{fZETfU>uwZR68_Iqob{h1S{OS9Y-
3F(VmDcd)owtW@DHigo;e;j?&+R%_uzOfOPEW5HJ9KZL0E{B&F-Q|S!pnyFg70Z3f-
^Z7g!!)zp8WTo(n8Uh?zO3s!pA{d{uQENLh0d`BgG2#?HoWUCxS9=!$YAzii1ksf-
;8LT6DfWBcTpQv%<F7mFZFL^TZNy?QH>wURg+OHr!M*Tw0k3{KW%kO;Tw5#QLMIk)CCqws=PlMx*fEC%6HAk0!poV?(AzB}jR=oP
aXuZ|s(Q4|tKE>o|p@Fyse1ut0ig1RFc&1BhJBYl+ar`u^KeUaT1X(zjp-4$ss?TB<cyPWQ&?es<3E)}>Fu={Qzotm6?TRzDs&-
r0>@yk}2$V%B23z3}v=-
gORpB*2Ujqtqpu~++OYU0C*$rF>ur$3yUoSv9EF*$Yg+*sw+=7ZbiaknDMt%|+Q>i9|{tVw^hJl?8^gNy$VW!b1SBiVE#8H;2=3V
b%hAeN<4sf;r!<?&nvQ8^d9jYh|hO&ps!K0P%vb!>Wi;zMXQ!5ZDWLK>ChBnpFig^m_0ksH*)#;QK6ur+i#Vn9cO12;*(Xr?!q=I
HUs8E7&+dE)5Q@e?yp#3=A;^PB4j7jGT>^7s7UqJDN!e~L3v2nWyF4N^#1>zy<reP)hNoR~N|H8U|iS<vX<@y)kX<zx^qA&v{GxD
=X>AJ&yFlqejme+uhkhvLLdTCrn7jiU3O3c~DmzAK}K7r4ZlZe;7}OT_Psw3pq<Zi{pmKPYB<6up*ZNzM`V57>B`?q`=sp2*e&)-
BDvM=3ReD7%7{9UKA4mby`G&5csv&%ZzWyCbjBq9J1i8KVwa1IvE;G`oRJ?4{l84g_>9YjwfpT;0qrf@%wCdXbOIu0g;hOIGt-Sa
uX4GQ7*Fyq`WR%0-
$H`M0bKF}yHV+|CUi)<Pos9xC@V5y|}G^e3nDqiswL*<>XNL!a;m9}eSS)Nm6o3>>#fDKBdyxJHpL%h;k;fgIMll-
(S~05CT6kAY|~awpwko2_Z`3$E|g6mcYzXqm8=k_R0BA&Usuv6DVW5CR_AU6%w5K$h&nrtR!&e0BwPwxCQ0#@!c657+lgB7J}}Uq
VJZ-2%MY9RVIze~S*mKK&$D!Rz~ddX~f=yssGYh*>Z*ut-
2x;nrO*Ky_JCB_#~}Wx*FJ6c*+RT*TgCz4yn@Pk(lpWw=p27B2qrnh594%W6^*r{*D3F;ekD$&)o=pj2i}S~0%hWRwB?PZkzSUa~
-3BxpQ00HCK8Bwj<pFO3Fe{#+|b!T|PtwYl+&NFQ>h>`~Ce5?vj&ZROBGUYu8z3!$${;{b1)teEZynEIJo$}Xci3`>b!9dWPW-
=;hyhr!3#8Ww<Z&PlUL;g{V^pBtS`5zQrZ(-#JlhR#92;6IM9z3dKs%_CZ400QWz>>3$HWVbjR(=Cb)QVhtF-
3DBAv#TPz&bMx7S7*-
!D_T!#3g$!K50{))Gq?M}qg(&&;y8s6+kD`!CWUhP0b6enmJo;tT(`|3y^r8z`$`0w&YPlp@2v^oTt|6>Fivs75HA^P_6Ar7PJGP
Su}+pM@R4zWJ}NC)GC`cl!-
775C57krb9Dtwwx(SGS7}liA^%me`JqoJqLFOOLIb(v#K3Px6=YMth6aWSrkw>ZPC_8bK%_t5qdC_}f94<oiVMKzC9E)0m**<!6H
bG5^gs8s_i=s2hkm1?Pvc(BMB{GS=H8762MS8MqZxqaE-
^63JmU}m;Ob2vEXu1Qz}>DX<LXT;$BtX4TChUjSIHSYI<U<_v8~L+wD$796(j8A#*0+s;{jR|nm-zcsj%drzolZv7_KuYWFUHqUN
<45L=Zx2A#EKmNh=CqmqBg5{+YGeU?cPp3eW{kyp!u=9fC4QsN&d0tKlJ5R8VaI>~r7SRPIxx*mzTr?{h)vsI3R-
1JaVhZpdJFR4%iM9Y|-
CDPkzvXqgQ1z1qBwvworiMukkHt!&7~oQ#HOHvl_qPfo&~bqZWcJ<LTN9@T}=tI8Z+H_X0<49(4u$_z1zMs-
0EKT(yno$eCaG1&Aly3n0hjr>Sr>R{?0A?rD7-
_s@>pjFl?N`5)YL_=pNYZdrV_}NI=U8}aXsPD$6u~1cjLhN$Uq+H<*TB{ti;bIeI2=yqJST)dh#QRi25Hp_!$V(H++)W^a5WXMuN
5&`&rM|=@sTItT@3s*1%$#>Un;fKO^xNU;#d&mz>)5a)?p6@rYaH9OD~=vHrm7Sh8Aa@S6V5OS$37Wsm&)0Iuyn5^in*(1T&M;Ig
)W6y7)#p?s|aJL)`qnfdf8XqbU78;n2e1oes+Y41%juN>Iq|N8|Tf0@c@~R<fT$zN;oiiuvlm7hgp!I{w<%Tdu$#I5M;u=yuG23n
&yfw-=B=pQ}{?N#4epzGVLt7D2Ltz&c~dMFy(cyJ!Po39pUW2xmyOZ_#jr1-
N+e08K#couJ3*QKJY>5T#){gTh(XgrfhzB!IMj?MSai!IjUKFgGSjc4ty<1Sxk3I<cA@v(sIFH0;Ox61BSFb!lmqQT6+LVpM6^Dk
>pM0>2c~mXUnWv1B}u`yvOqj=f&!Kr4`Jg2`b$^3P<WG;dWx~s2F270sA^k<(ik7)jsV4Nv{@UDv{phx#3p|JXW+r_@nmwnW!~?J
3Dg|ufx7i^>;L<>hF0BcJu?rKq2j?QQwtfI=lM`pbF-Eu7T9fSSke#UEGEnW7eHBfqimV6+b;Q=}EIVf|peD)2B+3xYY$`9_DB4r
sH_tGjL3<yJ;M@%USSJW3&+spc6JxJBQVDwoB*)t+sefr(`9VA%U~H1q(461T8+*e#f#KRHd(!;ft%9!*xe7VP<lwK6&1bBE3BO$
p+V;;0;|ZiLh9apX?B(UekSrt>3ztm3>|KWii~=78?YmYtB;8w@pHu{xW>+`pbVEEED^T+G-SjuDWG4*N~qy=%$_Vp-
!|zdG}nfXaruo==lI$)5v}n7N%FVhgp-_d7n(nEBd$7((fteDYm#N%KVFy0iKFwP>bVX4qhIlRX>n@^I<C>2YpT}{Eo{jmV|02C5
xy07%MWY(&TJ5h6IA884gROky`DnApN4{Rl{gnDn+k<nZ8AXpQFu408n^0)&^9o<{`#wz!EgqJM06H|Ajt5C0tQz)C6Uf2qV#Oqs
1DD(N9-
KA>%8h5XUo|g)8$0H=QGF&8s6#ZT)Ly7FNpiNL5kSEsygL%hzazQBq{H3vb}cn>@v2e~;v8`mMSb7!`AnIm7ElQDN4#3{_KKBV+{
s|2ZD%5m05R*)b6q2ORjB#*<xow9Bqhi>eC~m3?~WqXkB)b3raC2m{%t3F`i11<ZOpHm`h~uMm-
4?UPBHMS)3}aIZwK?iDm;daxYgVNJwJ6|qkJoVH2TP3Y0mnM)L4efw{E72>H#Jy%-
F24JWT%vY2L55MEt=aGiiZGs#gMttfKHPPdns-
N7Y8m$0NOQTG)fy{Ku2!mSlw5KY@KEs?H<g6(4i!~WnBd<vhiFznt6z4Ltrn*}ivdvAxi0h*tQ&)gqoH}PU0S=l+b)@F4{0sUu98
Tu8kFL^#(U1>^g4o*nUxW1BJ{wUC=EPUjbKN%mk*d0A*YABN^w`2r0R2a)8TjDNv*JPOZLO=yDo-Lq7jk_WCHhJ#BSuE&Z^jOB(e
tW~`TG~Uvd}9P{s1-*M{rv)4c<Koti%g4;+G-gCiP~(?-
#k#y_(%W^@&}@47LzPIp;U#N!U^}>F*u<@|4E`*IzPYyAaP@ZTRIcr@OD7A$dC6Q!Q*EaNTOcVhf;xMwi~6*SK4Q`nu8440`r8t{
?G=&_|g2k!h_Xi!(Kkb@}tb&@<RWMc&^Q>iN3x6#22z(>`KgZkcyXOJ<)j3^<WM-
0?Pj8Dzp}K9W8k6md%;v@adS#}VD*{SQz}0|XQR000O8001EXh(x=GB@6%nmmvTE4*&oFY;R*>Y-MvVb!#qpVQp-cSzB-
1))9X9uQ=6964Y5KvURbr*&uEDkOHX-
w0#pmP`gJGEiSnsxmHy{fF#?J11OR!3sUV`5gNB~0|e+=7wfvae}Vi9`UCM#=**l854n^hzpPfvnK^Uj^38=F=QS(he~rdiU%VNg
#Ak6QS&UDTrDQp7#qGGAY>cszZ?kg1zi#p{s`TCPd~1f!0mtWm{PJVqI8WA-
RR+XI_|b~b<5uz*_&f1F$>@|=f$UTGJYuEl<P^Kx;NIs`+>4mqa8P#NjS0JEH3I*>Q{w^Zwi_SC`^k2E2vRRV)+vj-
AWR%_3O^qui*U>q90B5!2XPlv-yUQ0N=UfScY_CkPtx|JlylIjl^ze|L;|GIwByY<-
jv1bjc87r=mjvsS#aewmV6^F3?GMZ;Dxw($>5EE*|j5X)%c{{bWuWi!u6{&UpM`TSIRb<4*2A!<9*T8SbsmS`}dsBoZ6?u1D^~G-
WePk`DA!-WMKHt;P9>SzRKIZf2^1L?FuV5EBaOo{quFd#@&T-
f3w0a7r$p^Ua!OlU<NQkvc;s)x@al<maLUZr81mVDfg$Uu*$f19nFSr58NId8W|oPzCAKB@Cj%*K$>kmM9s=!6!_j$1yx}4f$i1&
`hq;mc+_(`gp>>}%e5!CYntmFCb~5=I0~AK4BojlJalIi6j2Ji-Fx!*a`D^CpZ=L1Z0e_flz&;g1J3J0XfBWGhp1H8@V$_~msY6L
=+MBOfm_3)10#cmR+qbL*HvdT?=({_8$;D{{VAarhUGT+dQs#agO3A<&^9Jn-;FS`qh@HSkVN7w5v<92`jiKC$Fp4n1c3iRvd-
x11!XbBxMrB;6O=}9Xe(KP^asjg2CCwzN2JOT0l<Z3nRHxU#Pg8y_dG*euQn%sNf-
9jZ~yX}l!J#M*rnir)QZG?j;29W!~ECm)oD8txPZzN(j<$?21rO&LD;e;tT{FqzL*rW+9nL>fCCKKke|r#ROY0-$YE-Izvd&scL<
e$XXm8)pYMKgH$7H|Ud|@-k?*?*SMUc;@+O_2Zby#qS#|?4g4cR@iiqcUn6CmDP2j?lB627Iih38}?-
)qI=<%^6zHhruO^^mW3g!^W0Y;Jj2cRdr9YYiXiei)|%jhM;oN)dLLu5}LlQBC?=wQ39EG1n!Z=Xtteg*-
k+`WvY21G3*PA|z)@fxBg)wQ4~A?E{Gn81%GaQu;Q>nR9nqj=1*V^HlxL_5}+Man12IQVTpEhje(UMg9?|I^(+FuXCdgQ<|AIv@!
ycn<Lhq(tyBYI?c&EZK_BkQVg(AAI`;tWb2MtUz6gF1T|18h^*5b&WOe2#jdgRblFa^1#IPFzz8QQSS>>`3O`HCc0pB#4#z`pE?H
cvgt)mokOhD>j+U3%_#Cc@cP@m&7WBOoDxvjNoYagmFI$rS>@BdD+|BDg`UHEfweLy2NkVXOlZsCFA&fn<3P6cvUyOCBv;;KDd)b
zB138y%_rbuNw`%ek$@YFHUg$cX@s51;6{0vZMt!Rb05JG6tri^GdAwcOAWD)ne<)PpS7Be)WnxBzWw<G%(6#JhXf>Vu%MxdQ~I2
7H-YL1BaadVb3;@?VNni2EK}F?<rdsep&$7Gzo#C>C_Of031rU*%W1Jo+EP!axwN0V#V1Ltrg{QWiURXJF<fA-
Q2r%5hFDBFZ2a0NMY8e$pvudDx;{)mLb6T=d3@Fiq0kTn+I61QT~!LKCDybPMm_*vE(KOZ4iPkMNDjmd!37xXM05$FE>BeASJI}J
i(4#N0j<<I&_7k=S=6Dbt~OWc%r=#Z{+48dqGKZyD6}TR5ZD0W<YOoZ&=d#~khx0P(2@_~=g_jJuxQQW_XTuTyTpXAu}wfr5vjia
uUUbq>~ID<lQ2iCVp%t3(g=_zP}kSQA=-L*F}dK{$w!nFfr%$YJdj}&H3JU}lh<bDN0C{iJ~cNG5zB-P8-
xi(BB69609m?+tUC}mBFZ))MT|h$DdNw&trw{Qy#E`opxzjZJto|cN{fI#m0)GyE=&zP%JaS5+xfewi-
*+8NB{|Vo!2LL&_li1QEqC*7g)453~zyy*I3SF*i@%|r^-`c-c-
+3ei|b5=qP!^StqJa3%(~*7f*nqZA25yZfJ)Eby&b*@FMzu0rfrwFeY`Um|j?s=wD?!5^1_rr5vZQqsh6i&39y6LE783!?ba_0I6
>f`%R`3VZM$rgKry2qjReVMMY=QVjse{*KpC_d62_K!Q2-KD*OZDKsN+O-O@lBe3Xr+LZEJ?ETZ(<O-
LGIO8Y!*bX8kK4+2dJc<+IhfPuaQhF+35&2C*TKD~{<og*&NM6cQyYL|N372T(4ktK7UqYVHk1@7`~j6px-
y5FY|q@p5Q#Z}=!ReLhUR1OYIT9@3Dxnf%ZTuJo7AvVgBYOq@A?cG$Cq@6<NCKG`pVneMO(%p&(k(Le*LJ@MMfDhfNff-cm4&9lB
`;>bjWo>Tzfiw(h#&TzNO~4a}A{?E`RKg@Q+S(80>g1!+xEKGMTI>ULPjUjk@9^0LQzz)PEPvu2uSW0I>WDH)_q)Pk=lF@?Q_vHm
suDF{3#=~ctl_wfiJIPw=g<Cvh1xxPsKTcF0~*XIDHc8`&BOE^E%a=sM1YCQpl46OPWFA<fwA7@3mM%!ZbKzOJ26W1QwTw{z?)>1
wp{XgmI;T9>l&E`5*hay<*#o^+Y4u*MBt!r$$d_y0B0%0cS^#1PG<>07t8gja$-l+LoM?H)nGDL58~EM_45+lwuPho4whPD-
%t`wR7R^Pva8e9BshT}9Zw{r-j|uz5mjG0js~u-
L~JEm_5=?pPr%qWMJk;kJc;?gOF2uq8=sBIR?de(#A}K|QV2XiV|!KZy0Wa%Xt0zil^_G=a;xfMIOyr8ouUGxlTWa@kSs`QR`gfU
g?~phOH?Lg{g-_*&kO<&-Z=;;eNz^tb7uVG4R;Qr!FK2VW)=`J$h5>#3rC7{ZraxwBQ4W^)sm;MW^6;OhBJ-
}_^exJ%qcPT;_4yYM+@NH*QJ>DGs<=(#PM+Q0Q6A%r>nQ<COs?Df0Sh4{g8XLFuax!qRg|4e<0N-{iavT-AL41+S9bvw%oXZDBYN
`jtrVTW0}y-)O+z&TdL<|5YzClc|7&=7(3{iV=*d<h8O@1;3Jq@Q1W%pm=k*}syE0GSz`2N63s2?X+*T*_Xt-lRn$S4qI%Ef)WJ(
0r^X)Qme#51o~58WLGx)~DAjAKdw5sGYUrT(hJ9rRGc~x1GKLP?O`LK?R%g5-
0A^A2me@N|vwywtBErJxl7U<3hr$FIV`bcZR)j~&{q&EPR&V%0R3r=(z7Q8M=YV$#Gg|PxV%b*w3Mmb@IpuijhAH|NLVxzIvRUsE
ARS;V=`%z>bj2Ym(KOrp8BquW0Q0a{sOiN4)GL7SA6fj8g6jgj+@_G;&gclO23DPMFO}r^9?vKTZQQOoefBCxTPi~;cI>9e$d9P?
#dk}U_+`3k=;0!5*nAZr1RHf}s;V8~w%wYDM7??X11=F;qz7%;HDw*@#}w3XL3#Q784bTLL`?$sy+M?~Vu#JYB-
&jQW5O9_0o5WY4KYk-8PUDG0;n<rdhSkI91H<99##XVfg5oJLXxRN?ZXl-
4AfoxfSMjR#BL7;EbtvI1M=n(BZhtlR5)MshMl_pi$}PTEUas}bkOGiPo5)dHVn;__@P+%9^$Lq>Wuz<>lu@iY73ubj}rTl%Z-
B`)$o-F&6+*ev0WZS@<Jj>uE?Zc_1&N*#;IEBJuvw;(-
IqRfODY*Ud$ojd*_Chd7lTgMAW|9q|OP4;EnW(HU0d{FZ8c4Yft+@%K1dS?9dbqe3?f}N+US7C~{$1#i_vvbgKEZR!(VmBwoIu1;
LWov8m&$5eYW%Cf=fwExK4qCU+gm>4iI`3~A~|qSlVgZ&GN4Pj^W@`_ktS{D%n0qWRy(MS|K#=_T-ILRY=ig4uM^QvG*kt%cn;iU
TXG<Ci>>$7c)a#YR8B?j#o7%Ji(wj7I+dP)h*<6ay3h000O8001EXSsxM_LjnK*PY3`23;+NC0000000000qyYc`002!xRYFB}Wo
~pXaCuNm0Rj{Q6aWAK2mk;8ApmzpNw9MZ005UB000~S0000000000005)`Z2|xQPjF>!L1$%dbWCYtFF|KzZgf(0ZggpFWiD`eP)
h*<6ay3h000O8001EXt)w)DITZi^cU1rY9smFU0000000000qyZWZ002*LWo|)dWo~p#X<{!!Z*FvDcyv=`a&~EBWiD`eP)h*<6a
y3h000O8001EX`X*El2?GECjtBq%8UO$Q0000000000qydj3002*LWo|)dWo~p#X<{!(baZe-Y-wd~bS`jtP)h*<6ay3h000O800
1EXU&AOB$O`}f3M2pk82|tP0000000000qyf+-002*LWo|)dWo~p#X<{!-
X=Y_(d1Gv4E^v8JO928D0~7!N00;m803iUvx@I&#0ssK|1pojc00000000000001_0nai308embZb4^dZgfm(VlPc$ZeeF-axYIo
Q)P2=X>V>WaCuNm0Rj{Q6aWAK2mk;8ApkJFEYnFH005|u0018V0000000000005)`O*H@jPjF>!L1$%dbWCYtFHK=?VP|D>FH>c6
b7^mGE^v8JO928D0~7!N00;m803iUXG?~&n000180000W00000000000001_0n<_d08embZb4^dZgfm(VlPc$ZeeF-
axY(BX>MtBUtcb8c~DCM0u%!j000080000X0NUPL&A0*p0HX*103QGV00000000000Hgs-Qvd)@aAj^mXJu}5Ole{-
PjF>!L1$%dbWLe^X>M~aaCuNm0Rj{Q6aWAK2mk;8Apl9;?2r8o004G4000~S0000000000005)`K~?|&PjF>!L1$%dbWCYtFHme@
V`XS>Y-D9}b1rasP)h*<6ay3h000O8001EX0w`;2rVIc8?JfWSApigX0000000000qyczj002*LWo|)dWo~p#X<{!>Y;|X8ZZA-
5b!TaALSb`dE^v8JO928D0~7!N00;m803iT{k3T06a{vJEA_4#;00000000000001_0bOwb08embZb4^dZgfm(VlPl^b!TaAFHmf
CXK8M8MQ&$lZe=cTc~DCM0u%!j000080000X0L-DkT}&AO08@kj0384T00000000000Hgu0<NyFqaAj^mXJu}5Ole{-
Qe|^+Z*FsCL1$%dbS`jtP)h*<6ay3h000O8001EX7uuN0FaZDn5&{4KFaQ7m0000000000qyaYm002*LWo|)dWo~p#X<{!^d2@7S
ZBT4=XK8M8FGFu+WiMfLbYWv?Uvg!0b!>DlaCuNm0Rj{Q6aWAK2mk;8Api=~u~tg~003bE001%o0000000000005)`wEqAAPjF>!
L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z)9aJV`y)0b7fy<X>4U~VQpnDaCuNm0Rj{Q6aWAK2mk;8ApisWYJpY(003wL001xm00000
00000005)`PXPe{PjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z)9aJXJu|>a$$63UuJ1+WiD`eP)h*<6ay3h000O8001EXnoqgM
J^=s#N&)}?Hvj+t0000000000qyh5+0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FGFu+WiMxCZe?;|bY)*{V|8L*ZEs|CY-KKR
c~DCM0u%!j000080000X0Pj{#xhnwx0NDWm04x9i00000000000Hgti1OWg~aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1y@0WMwaMWnpArWN%}0E^v8JO928D0~7!N00;m803iVS0L;!M0RRB*0RR9i00000000000001_0s93308emb
Zb4^dZgfm(VlPv9b97~GP;7N)X>M~bLvL<$Wq5QiV{Bz%axQRrP)h*<6ay3h000O8001EXw>B{ULjeE)I066wEdT%j0000000000
qycFM0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FGFu`bY*ySFJx(RV_|Y+E^v8JO928D0~7!N00;m803iT_j{Fub0RR970ssIr
00000000000001_0rv<208embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bLvL<$Wq5QiZDnL>VP9i!ZggdMbS`jtP)h*<6ay3h000O8
001EXnJ4r;VgUdEb^-
tZD*ylh0000000000qycsc0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FGFu`bY*ySFK}{oZe=cTc~DCM0u%!j000080000X07I
R#Rx<$r00#m905AXm00000000000HgsS3;_U7aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1y@0ZggdMbT4vcXJu|>a$$63E^v8JO928D0~7!N00;m803iSp&oE>#0RR990ssIm00000000000001_0iq27
08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bLvL<$Wq5Qia%F90ZDM6|E^v8JO928D0~7!N00;m803iT84alA^0RR9A0ssIr00000
000000001_0Ui$l08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bLvL<$Wq5Qia%FIAd0%61ZggdMbS`jtP)h*<6ay3h000O8001EX
2S^MxzySaNB?ABeF#rGn0000000000qye4~0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FGFu`bY*ySFLZBjY+rA6bZ~WaE^v8J
O928D0~7!N00;m803iUKV6hfb0RR9>0ssIq00000000000001_0j&}N08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bQ)_8#Y;!?p
Wo~pYVPkY@c42g7E^v8JO928D0~7!N00;m803iTgfI;*<0RR9n0ssIr00000000000001_0Z$YG08embZb4^dZgfm(VlPv9b97~G
P;7N)X>M~bQ)_8#Y;!?pWo~pYWq5FJa&%v9WG--dP)h*<6ay3h000O8001EX#Y<T=Hvs?uDgpoiGXMYp0000000000qygO(0RT^M
Wo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH>u2Y;1EuXJu}5FKKOXZ*p{BZDcNRc~DCM0u%!j000080000X0R05s{67Hz05}2w05Jdn
00000000000HgtB7XbiIaAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zeCX>4qBL1$%dbT4Ucb97;BY%XwlP)h*<6ay3h000O8001EX884!_C;<Qf>Hz=%E&u=k0000000000qyh67
0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH>u2Y;1EuXJu}5FKlUZbS`jtP)h*<6ay3h000O8001EX-
M}iaMF9W+IsyOyE&u=k0000000000qyc9d0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH>u2Y;1EuXJu}5FLGsJWG--dP)h*<6
ay3h000O8001EXT{6@oIspIx2m$~AGXMYp0000000000qyhLF0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH>u2Y;1EuXJu}5F
LGsYZ(nR_b963nc~DCM0u%!j000080000X0CJng=u80s07n7<04@Lk00000000000Hgtf9RUDOaAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zeCX>4qBL1$%dbT4yZc4aPbc~DCM0u%!j000080000X03Q-
JRY(B<05<{v05$*s00000000000HgsM9{~VQaAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zeCX>4qBL1$%dbT4yZc4c2?a&K*4VQDUKc~DCM0u%!j000080000X02o6cQ$PU#04@Rm04o3h0000000000
0Hgu8AOQeRaAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zhAX>Mz2Zf7rUZ**lYaCuNm0Rj{Q6aWAK2mk;8AppPwk((d^007bf001Tc0000000000005)`Kq3JEPjF>!
L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeGZ)9&TVPs@3aCuNm0Rj{Q6aWAK2mk;8Apo+FMUWK%006@Q001Ze0000000000005)`q$2?U
PjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeGZ)9&TV{Bz%axQRrP)h*<6ay3h000O8001EX?jIxsC;<Qf;{gBwC;$Ke0000000000
qyhgV0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH~=2Z!cqPZ*yfXaCuNm0Rj{Q6aWAK2mk;8Apjz;4m}qE0074U001ih00000
00000005)`Z6*N#PjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeGZ)9&TV{C78WnpY=E^v8JO928D0~7!N00;m803iTov6KuM0RRBZ
0RR9h00000000000001_0nH}?08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bRBvQ&FJpCba%FCGE^v8JO928D0~7!N00;m803iT;
s`d9H0RRBp0RR9g00000000000001_0WK*408embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bRBvQ&FJxtGWprgOaCuNm0Rj{Q6aWAK
2mk;8AplJurMo8q007?s001Wd0000000000005)`m?{APPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeGZ)9&TWn^h|E^v8JO928D
0~7!N00;m803iTULeXX~0RRB@0RR9m00000000000001_0R$`o08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bRdi`=X>@rnVP|D-
bYE<5XD)DgP)h*<6ay3h000O8001EXmN{6>Bmn>b-
vIysFaQ7m0000000000qyc~}0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FI9ADY-
x0PFJ*FaZ*pH|X>4UKaCuNm0Rj{Q6aWAK2mk;8Apm&w5}!)}001ol001xm0000000000005)`@-
6`YPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeHbZKm9ba^jqX>)X6bZ>8Lb1rasP)h*<6ay3h000O8001EXS^$FQHUR(t0|Ed5G5
`Po0000000000qydXC0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FI9ADY-x0PFK}#OV`XS>Y-
D9}b1rasP)h*<6ay3h000O8001EXQ}a}bbO8VWivj=uF#rGn0000000000qyZ5!0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FI
9ADY-
x0PFK}#iXK8L<WN%}0E^v8JO928D0~7!N00;m803iSaJ#arY0RR940ssIt00000000000001_0n{@A08embZb4^dZgfm(VlPv9b9
7~GP;7N)X>M~bRdi`=X>@rna$#;{Z*5<6Wo>Y5VRU6KaCuNm0Rj{Q6aWAK2mk;8ApnL^XjnD@000C6001!n0000000000005)`Tr
~jzPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeHbZKm9ba^jyZ);_4Uv+a~XJsyMc~DCM0u%!j000080000X09zy9-ev&+0B-
^S051Rl00000000000HguoHUR)naAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zkNX>4h9c`tNtZ){&^Wo&RRaCuNm0Rj{Q6aWAK2mk;8ApmKbENP?w001Td001Tc0000000000005)`lsEwZ
PjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeRUukY>bYEXCaCuNm0Rj{Q6aWAK2mk;8Apjf7=IlQU004_8001HY0000000000005)`
d^rICPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeUVRL0JaCuNm0Rj{Q6aWAK2mk;8AplNfsEf`900280000{R0000000000005)`
`$Pc%PjF>!L1$%dbWCYtFH~=2Z&PJ*c4=c}E^v8JO928D0~7!N00;m803iTs1$zKdFaQ8R&Hw-
$00000000000001_0Rl_`08embZb4^dZgfm(VlPy0Z)`+qb8umFV`wgLc~DCM0u%!j000080000X008`OQ^^1T03-
qc02lxO00000000000Hgtpd;tJYaAj^mXJu}5Ole{-Utei%X>?y-
E^v8JO928D0~7!N00;m803iUp%NZy%2><}Q7XSbc00000000000001_0gQbC0Bmn#VQgh{FJ*2nd0}mAP)h*<6ay3h000O8001EX
v$(`;;0pi%DINd-
4*&oF0000000000qyg=Q0RU`oV_|G%b1!mrE_q>XY*0%90u%!j000080000X0Ek4phb0UE0GA;E01p5F00000000000Hgu>k^um0
Z)0I>WpgieYc6?VZER3W1qJ{B0027xI{?ZP002y%0RR91
"""

def __cubkit_bootstrap__():
    # CubKit import-debug: this function is generated by CubKit.
    # It prepares bundled files before the real MCUB module code below runs.
    import base64
    import hashlib
    import json
    import os
    import sys
    import types
    import zipfile
    from pathlib import Path
    from types import MappingProxyType

    # CubKit import-debug: decode and verify the embedded zip payload.
    data = base64.b85decode("".join(__cubkit_bundle_b85__.split()).encode("ascii"))
    digest = hashlib.sha256(data).hexdigest()
    if digest != __cubkit_bundle_sha256__:
        raise RuntimeError("CubKit embedded bundle checksum mismatch")

    # CubKit import-debug: cache extraction avoids rewriting files on every import.
    cache_root = Path(os.environ.get("CUBKIT_CACHE_DIR", Path.home() / ".cache" / "cubkit"))
    bundle_dir = cache_root / __cubkit_module_id__ / digest
    marker = bundle_dir / ".cubkit-extracted"
    if not marker.exists():
        bundle_dir.mkdir(parents=True, exist_ok=True)
        archive_path = bundle_dir / "bundle.zip"
        archive_path.write_bytes(data)
        with zipfile.ZipFile(archive_path) as archive:
            resolved_bundle_dir = bundle_dir.resolve()
            for member in archive.infolist():
                destination = (bundle_dir / member.filename).resolve()
                if destination != resolved_bundle_dir and resolved_bundle_dir not in destination.parents:
                    raise RuntimeError("unsafe path in CubKit embedded bundle")
            archive.extractall(bundle_dir)
        marker.write_text(digest, encoding="utf-8")

    # CubKit import-debug: expose extracted top-level files for normal absolute imports.
    bundle_path = str(bundle_dir)
    if bundle_path not in sys.path:
        sys.path.insert(0, bundle_path)

    # CubKit import-debug: build private package search paths for relative imports.
    relative_import_paths = [bundle_path]
    for package_dir in reversed(__cubkit_package_dirs__):
        package_path = bundle_dir / package_dir
        if package_path.is_dir():
            relative_import_paths.insert(0, str(package_path))

    module_globals = globals()
    module_globals["__path__"] = relative_import_paths
    module_globals["__package__"] = module_globals.get("__name__", __cubkit_module_id__)
    module_spec = module_globals.get("__spec__")
    if module_spec is not None:
        module_spec.submodule_search_locations = relative_import_paths

    def load_strings():
        import copy

        return copy.deepcopy(__cubkit_locales__)

    # Public build-runtime API used by generated source modules.
    cubkit_pkg = sys.modules.get("cubkit")
    if cubkit_pkg is None:
        cubkit_pkg = types.ModuleType("cubkit")
        sys.modules["cubkit"] = cubkit_pkg
    if not hasattr(cubkit_pkg, "__path__"):
        cubkit_pkg.__path__ = []
    cubkit_pkg.load_strings = load_strings

    # CubKit import-debug: expose vendored libraries through `from cubkit.lib import name`.
    lib_path = bundle_dir / __cubkit_lib_dir__
    if lib_path.is_dir():
        lib_path_str = str(lib_path)
        if lib_path_str not in sys.path:
            sys.path.insert(0, lib_path_str)

        lib_pkg = sys.modules.get("cubkit.lib")
        if lib_pkg is None:
            lib_pkg = types.ModuleType("cubkit.lib")
            sys.modules["cubkit.lib"] = lib_pkg
        lib_pkg.__path__ = [lib_path_str]
        lib_pkg.__package__ = "cubkit"
        setattr(cubkit_pkg, "lib", lib_pkg)

    class Assets:
        def __init__(self, root):
            self.root = root

        @property
        def available(self):
            return self.root is not None and self.root.is_dir()

        def _resolve(self, relative_path):
            if not self.available:
                raise FileNotFoundError("this CubKit module has no assets directory")
            root = self.root.resolve()
            candidate = (root / relative_path).resolve()
            if candidate != root and root not in candidate.parents:
                raise ValueError("asset path must stay inside the assets directory")
            return candidate

        def get(self, relative_path):
            path = self._resolve(relative_path)
            if not path.exists():
                raise FileNotFoundError(path)
            return path

        def exists(self, relative_path):
            try:
                return self._resolve(relative_path).exists()
            except (FileNotFoundError, ValueError):
                return False

        def read_bytes(self, relative_path):
            return self.get(relative_path).read_bytes()

        def read_text(self, relative_path, encoding="utf-8"):
            return self.get(relative_path).read_text(encoding=encoding)

        def read_json(self, relative_path, encoding="utf-8"):
            return json.loads(self.read_text(relative_path, encoding=encoding))

        def __bool__(self):
            return self.available

        def __truediv__(self, relative_path):
            return self.get(relative_path)

    assets_root = bundle_dir / __cubkit_assets_dir__ if __cubkit_assets_dir__ else None
    assets = Assets(assets_root)
    metadata = MappingProxyType(dict(__cubkit_metadata__))

    def resource(relative_path):
        return assets.get(relative_path)

    environment = MappingProxyType({
        "root": bundle_dir,
        "assets": assets,
        "locales": __cubkit_locales__,
        "metadata": metadata,
    })

    def get_environment():
        return environment

    public_runtime = {
        "assets": assets,
        "get_environment": get_environment,
        "load_strings": load_strings,
        "metadata": metadata,
        "resource": resource,
        "root": bundle_dir,
    }
    for public_name, public_value in public_runtime.items():
        setattr(cubkit_pkg, public_name, public_value)
    current_exports = list(getattr(cubkit_pkg, "__all__", ()))
    cubkit_pkg.__all__ = current_exports + [
        name for name in public_runtime if name not in current_exports
    ]

    runtime_package = module_globals["__package__"]
    runtime_name = f"{runtime_package}._cubkit"
    runtime_module = types.ModuleType(runtime_name)
    runtime_module.__package__ = runtime_package
    runtime_module.__file__ = str(bundle_dir / "_cubkit.py")
    runtime_module.__all__ = (
        "Assets", "assets", "environment", "get_environment", "load_strings",
        "locales", "metadata", "resource", "root",
    )
    runtime_module.Assets = Assets
    runtime_module.assets = assets
    runtime_module.environment = environment
    runtime_module.get_environment = get_environment
    runtime_module.load_strings = load_strings
    runtime_module.locales = __cubkit_locales__
    runtime_module.metadata = metadata
    runtime_module.resource = resource
    runtime_module.root = bundle_dir
    sys.modules[runtime_name] = runtime_module
    parent_module = sys.modules.get(runtime_package)
    if parent_module is not None:
        setattr(parent_module, "_cubkit", runtime_module)

__cubkit_bootstrap__()
del __cubkit_bootstrap__

# ---- CubKit entrypoint: OpenAgentMain.py ----
# SPDX-License-Identifier: MIT
# scope: heroku_min 9.9.9
# -- repo data --
# repo: https://github.com/hairpin01/repo-MCUB-fork/
# source: https://github.com/hairpin01/OpenAgent-old/
# -- end --
# scop: kernel min v1.4.6


import asyncio
import contextlib
import html
import io
import re
import time
import uuid
import json
from pathlib import Path
from typing import Any, TYPE_CHECKING

from cubkit import load_strings

from core.lib.loader.module_base import ModuleBase, bot_command, callback, command
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
    from core.lib.types import InlineMessage, Event

try:
    from OpenAgentLib.OpenAgentMixins import (
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
    )
except Exception as e:
    raise RuntimeError(e) from e  # debug


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
    version = "0.8.1-main.build:1050"
    author = "@dev_dolbaeb && @Hairpin00"
    description = {
        "ru": "ИИ агент в юзерботе с новой архитектурой инструментов",
        "en": "AI agent in userbot with refreshed tool architecture",
        "rofl": "ИИ агент, который делает вид, что всё контролирует",
        "linux": "AI agent daemon with tool-oriented runtime",
    }
    strings = load_strings()
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

    async def on_unload(self) -> None:
        tasks = set(getattr(self, "_background_tool_tasks", {}).values())
        tasks.update(getattr(self, "_plugin_unload_tasks", set()))
        for task in tasks:
            task.cancel()
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)

        for waiters_name in (
            "_inline_status_waiters",
            "_tool_confirmation_waiters",
        ):
            for waiter in getattr(self, waiters_name, {}).values():
                if not waiter.done():
                    waiter.cancel()

        session_manager = getattr(self, "session_manager", None)
        if session_manager is not None:
            await session_manager.close()
        http_client = getattr(self, "_http_client", None)
        if http_client is not None:
            await http_client.close()

        await super().on_unload()

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
    TOOL_REGISTRY = ()
    # Built-in tools are now discovered dynamically from
    # OpenAgentLib/SystemPlugins/<group>/<tool>.py.
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
                    validator=Choice(choices=list(PROVIDERS)),
                ),
                ConfigValue(
                    "api_key",
                    "",
                    description="API key for the selected provider",
                    validator=Secret(),
                ),
                ConfigValue(
                    "model",
                    "",
                    description="Model name. Empty means provider default",
                    validator=String(),
                ),
                ConfigValue(
                    "custom_base_url",
                    "",
                    description="Endpoint for provider=other, e.g. https://api.deepseek.com/v1",
                    validator=String(),
                ),
                ConfigValue(
                    "system_prompt",
                    "You are OpenAgent inside a Telegram userbot. Help the user directly. You may inspect the local workspace through terminal commands when needed.",
                    description="System prompt for the agent",
                    validator=String(),
                ),
                ConfigValue(
                    "temperature",
                    0.7,
                    description="Sampling temperature",
                    validator=Float(min=0.0, max=2.0),
                ),
                ConfigValue(
                    "max_tokens",
                    1200,
                    description="Maximum response tokens",
                    validator=Integer(min=64, max=32768),
                ),
                ConfigValue(
                    "reasoning_effort",
                    "off",
                    description="Reasoning effort for models/providers that support it: off, low, medium, high, xhigh",
                    validator=Choice(choices=["off", "low", "medium", "high", "xhigh"]),
                ),
                ConfigValue(
                    "timeout",
                    180,
                    description="HTTP timeout seconds for each provider request. Increase for slow reasoning/code tasks.",
                    validator=Integer(min=10, max=600),
                ),
                ConfigValue(
                    "provider_reconnect_attempts",
                    2,
                    description="Maximum retries for transient provider failures",
                    validator=Integer(min=0, max=5),
                ),
                ConfigValue(
                    "agent_max_steps",
                    6,
                    description="Maximum tool-call rounds per request",
                    validator=Integer(min=1, max=15),
                ),
                ConfigValue(
                    "agent_max_model_calls",
                    8,
                    description="Maximum provider attempts in the main agent loop, including retries",
                    validator=Integer(min=1, max=20),
                ),
                ConfigValue(
                    "agent_deadline",
                    180,
                    description="Overall agent request deadline in seconds",
                    validator=Integer(min=15, max=900),
                ),
                ConfigValue(
                    "context_window_tokens",
                    16000,
                    description="Estimated provider context-window budget",
                    validator=Integer(min=2048, max=1000000),
                ),
                ConfigValue(
                    "context_reserve_tokens",
                    2400,
                    description="Tokens reserved for output and tool follow-ups",
                    validator=Integer(min=256, max=65536),
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
                    validator=Boolean(),
                ),
                ConfigValue(
                    "terminal_steps",
                    3,
                    description="Maximum terminal commands per request",
                    validator=Integer(min=0, max=10),
                ),
                ConfigValue(
                    "terminal_timeout",
                    30,
                    description="Terminal command timeout seconds",
                    validator=Integer(min=3, max=120),
                ),
                ConfigValue(
                    "web_search_enabled",
                    True,
                    description="Allow the agent to search the web",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "web_search_steps",
                    3,
                    description="Maximum web searches per request",
                    validator=Integer(min=0, max=10),
                ),
                ConfigValue(
                    "mcub_use",
                    False,
                    description="Allow the agent to execute MCUB userbot commands",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "mcub_steps",
                    3,
                    description="Maximum MCUB commands per request",
                    validator=Integer(min=0, max=10),
                ),
                ConfigValue(
                    "send_messages_enabled",
                    True,
                    description="Allow the agent to send messages as the userbot",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "send_message_steps",
                    3,
                    description="Maximum userbot messages sent per request",
                    validator=Integer(min=0, max=10),
                ),
                ConfigValue(
                    "create_chats_enabled",
                    True,
                    description="Allow the agent to create channels/groups",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "create_chat_steps",
                    2,
                    description="Maximum channels/groups created per request",
                    validator=Integer(min=0, max=5),
                ),
                ConfigValue(
                    "create_bots_enabled",
                    True,
                    description="Allow the agent to create Telegram bots via BotFather",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "create_bot_steps",
                    1,
                    description="Maximum Telegram bots created per request",
                    validator=Integer(min=0, max=3),
                ),
                ConfigValue(
                    "account_tools_enabled",
                    True,
                    description="Allow the agent to edit profile/join chats/read/search messages",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "account_tool_steps",
                    5,
                    description="Maximum account-level tools per request",
                    validator=Integer(min=0, max=15),
                ),
                ConfigValue(
                    "chat_management_enabled",
                    True,
                    description="Allow the agent to manage chats: mute, ban, promote, title, slowmode",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "chat_management_steps",
                    5,
                    description="Maximum chat-management tools per request",
                    validator=Integer(min=0, max=15),
                ),
                ConfigValue(
                    "media_max_bytes",
                    8_000_000,
                    description="Maximum replied media bytes sent to AI",
                    validator=Integer(min=1024, max=25_000_000),
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
                    validator=Boolean(),
                ),
                ConfigValue(
                    "context_turns",
                    10,
                    description="How many user/assistant turns to remember per chat",
                    validator=Integer(min=0, max=50),
                ),
                ConfigValue(
                    "context_compaction_enabled",
                    True,
                    description="Automatically summarize old chat context when it becomes too large",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "context_compaction_chars",
                    18000,
                    description="Legacy character threshold used by older configurations",
                    validator=Integer(min=2000, max=200000),
                ),
                ConfigValue(
                    "context_compaction_tokens",
                    10000,
                    description="Compact remembered chat context after this estimated token count",
                    validator=Integer(min=1000, max=500000),
                ),
                ConfigValue(
                    "context_compaction_keep_turns",
                    2,
                    description="Recent user/assistant turns to keep verbatim after compaction",
                    validator=Integer(min=0, max=10),
                ),
                ConfigValue(
                    "context_compaction_max_tokens",
                    900,
                    description="Maximum tokens used for the compaction summary response",
                    validator=Integer(min=128, max=4096),
                ),
                ConfigValue(
                    "tool_memory_enabled",
                    False,
                    description="Remember concise notes from tool outputs for next requests",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "tool_memory_items",
                    20,
                    description="Maximum remembered tool notes per chat",
                    validator=Integer(min=1, max=200),
                ),
                ConfigValue(
                    "tool_memory_max_chars",
                    500,
                    description="Maximum characters per remembered tool note",
                    validator=Integer(min=80, max=4000),
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
                    validator=String(),
                ),
                ConfigValue(
                    "request_label",
                    '<a href="tg://emoji?id=6010352868672936598"><strong>🐈‍⬛</strong></a><strong></strong><strong> Prompt:</strong>',
                    description="Request block label template. Placeholders: "
                    + PLACEHOLDER_KEYS,
                    validator=String(),
                ),
                ConfigValue(
                    "response_label",
                    '<a href="tg://emoji?id=6010286885090368072"><strong>❌</strong></a><strong></strong><strong> Answer:</strong>',
                    description="Response block label template. Placeholders: "
                    + PLACEHOLDER_KEYS,
                    validator=String(),
                ),
                ConfigValue(
                    "thinking_template",
                    '<blockquote><a href="tg://emoji?id=6010292571627069263">😎</a> <u>{provider}/{model}</u> • <em>prepares the response...</em></blockquote >\n<blockquote><a href="tg://emoji?id=5404857686477015710">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>',
                    description="Initial loading/thinking message template. Placeholders: "
                    + PLACEHOLDER_KEYS,
                    validator=String(),
                ),
                ConfigValue(
                    "tool_display_template",
                    '<blockquote expandable><i>{thinking_line}</i></blockquote>\n<blockquote expandable><strong>┌|</strong> {tool_state_emoji_html} {status_emoji_html} <em>{status_text}</em> <code>{tool}</code>\n<strong>└|</strong> <a href="tg://emoji?id=6010570945637392851">🥳</a>  <b>Round:</b> <code>{round}/{round_total}</code> • <b>Reasoning:</b>\n<code>{reasoning_effort}</code>\n</blockquote><blockquote><a href="tg://emoji?id=5310041868191407556">🩸</a> <strong>{activity_line}</strong></blockquote>\n<blockquote expandable><a href="tg://emoji?id=6012361831035705571">😪</a> <strong>Log tools</strong>\n<code>{log_lines}</code></blockquote>',
                    description="Tool execution status template. Raw: {tool}, {title}, {value}, {log}, {step}. Semantic: {round}, {round_total}, {progress_bar}, {progress_percent}, {status_emoji}, {status_icon}, {status_emoji_html}, {status_icon_html}, {status_text}, {tool_state}, {tool_state_emoji}, {tool_state_icon}, {tool_state_emoji_html}, {tool_state_icon_html}, {tool_running_emoji}, {tool_running_icon}, {tool_running_emoji_html}, {tool_running_icon_html}, {tool_done_emoji}, {tool_done_icon}, {tool_done_emoji_html}, {tool_done_icon_html}, {tool_group}, {tool_short}, {tool_input}, {tool_input_block}, {thinking_line}, {thinking_block}, {log_lines}, {log_block}, {log_count}, {elapsed_line}, {token_line}, {model_line}, {activity_line}. General placeholders: "
                    + PLACEHOLDER_KEYS,
                    validator=String(),
                ),
                ConfigValue(
                    "tool_status_emojis",
                    "thinking=❔\nterminal=🖥\nweb=🌐\nfile=📦\nmcub=🧲\nmessage=💬\ndialog=🗂\nchat=🐈‍⬛\nmoderation=🛡\nprofile=👤\ncontacts=👥\ncreation=✨\nskills=🧠\ncode=🧬\ncontext=🧾\nutility=🛠\ndefault=🛠",
                    description="Custom emoji/icon map for {status_emoji}/{status_icon}. Format: group_or_tool=emoji per line. Tool-specific keys like terminal.run or thinking.note override groups like terminal/thinking. Premium emoji HTML is allowed via {status_emoji_html}/{status_icon_html}.",
                    validator=String(),
                ),
                ConfigValue(
                    "tool_display_max_chars",
                    1200,
                    description="Maximum chars from current tool input shown in status form",
                    validator=Integer(min=0, max=4000),
                ),
                ConfigValue(
                    "tool_trace_inline_max_chars",
                    6000,
                    description="Maximum chars of a tool call kept inline before the full output is saved to openagent_tool_outputs and replaced by a file path plus preview",
                    validator=Integer(min=0, max=50000),
                ),
                ConfigValue(
                    "tool_display_log_lines",
                    8,
                    description="How many recent tool names to show in status form",
                    validator=Integer(min=0, max=30),
                ),
                ConfigValue(
                    "thinking_display_limit",
                    3,
                    description="How many recent thinking.note entries to show in {thinking}",
                    validator=Integer(min=0, max=20),
                ),
                ConfigValue(
                    "thinking_empty_text",
                    "Модель ещё не думала.",
                    description="Text for {thinking} when no thinking.note entries exist",
                    validator=String(),
                ),
                ConfigValue(
                    "thinking_bullet",
                    "•",
                    description="Prefix marker for each thinking.note line in {thinking}. Empty disables the marker",
                    validator=String(),
                ),
                ConfigValue(
                    "random_strings",
                    ["Thinking...", "Думаю...", "Генерирую..."],
                    description="Random lines for {random}",
                    validator=List(
                        item_type=str,
                    ),
                ),
                ConfigValue(
                    "todo_status_emojis",
                    "pending=...\nopen=>>>\nclosed=---",
                    description="State markers for {todo}. Format: pending=..., open=>>>, closed=---",
                    validator=String(),
                ),
                ConfigValue(
                    "placeholders",
                    "",
                    description="Available OpenAgent placeholders (auto-generated)",
                    validator=String(),
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
                    validator=Boolean(),
                ),
                ConfigValue(
                    "repo_context_max_chars",
                    7000,
                    description="Maximum chars used for repo context in system prompt",
                    validator=Integer(min=500, max=30000),
                ),
                ConfigValue(
                    "skills_enabled",
                    True,
                    description="Enable loading OpenAgent skills into the system prompt",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "skills_trigger_mode",
                    "auto",
                    description="When to load skills: auto = only on keyword match, always = every request, off = never",
                    validator=String(),
                ),
                ConfigValue(
                    "skill_repo_url",
                    "https://raw.githubusercontent.com/hairpin01/repo-MCUB-fork/main/OpenAgent/skills",
                    description="Base URL for installable OpenAgent skills repository",
                    validator=String(),
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
                    validator=Boolean(),
                ),
                ConfigValue(
                    "tool_confirmation_mode",
                    "medium",
                    description="How often to ask before tools: low = only critical/destructive, medium = write/actions, high = almost every non-read tool",
                    validator=Choice(choices=["low", "medium", "high"]),
                ),
                ConfigValue(
                    "tool_confirmation_template",
                    '<blockquote><a href="tg://emoji?id=6010201728773790293">😈</a> Continue?\n<a href="tg://emoji?id=6012317326584583729">😐</a> Tool: {tool} • {elapsed}s</blockquote>\n<blockquote expandable><a href="tg://emoji?id=6010394680179562842">😶</a> <b>What will be completed</b>\n<a href="tg://emoji?id=6010292550152230657">☀️</a> <code>{value}</code></blockquote>',
                    description="Confirmation form template. Placeholders: {tool}, {value}, {elapsed}, {elapsed_line}",
                    validator=String(),
                ),
                ConfigValue(
                    "tool_confirmation_yes_text",
                    "Выполнить",
                    description="Confirm button text for dangerous tools",
                    validator=String(),
                ),
                ConfigValue(
                    "tool_confirmation_no_text",
                    "Не сейчас",
                    description="Cancel button text for dangerous tools",
                    validator=String(),
                ),
                ConfigValue(
                    "tool_confirmation_timeout",
                    900,
                    description="Seconds to wait for dangerous tool confirmation",
                    validator=Integer(min=10, max=3600),
                ),
            ],
            description="Confirmation policy and prompt/button templates",
            button_text="🛡 Confirm",
            key="confirmations",
        ),
        Row(),
        Answer("❔ About", "AI agent in userbot with refreshed tool architecture"),
    )
    SESSION_LIMIT = 20
    from .MCUBEvent import _MCUBEvent

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

    @staticmethod
    def _rich_text_html(text: str, *, limit: int = 30000) -> str:
        text = str(text or "")
        if len(text) > limit:
            text = text[:limit] + "\n… [truncated]"
        escaped = html.escape(text)
        paragraphs = []
        for part in re.split(r"\n{2,}", escaped):
            part = part.strip()
            if part:
                paragraphs.append(f"<p>{part.replace(chr(10), '<br>')}</p>")
        return "".join(paragraphs) or "<p></p>"

    def _rich_bot_system_prompt(self, prompt: str) -> str:
        return (
            self._system_prompt(prompt) + "\n\n## Bot command final answer format\n"
            "For this bot command, the final answer is sent as Telegram Rich Message HTML. "
            "Use BlockRich/Rich HTML block formatting directly in the final answer: "
            '<p>, <blockquote>, <pre><code class="language-python">, <details><summary>, '
            "<ul>/<ol>/<li>, <table>/<caption>/<tr>/<th>/<td>, <footer>, <tg-math>, "
            "<tg-math-block>, <tg-emoji>, <tg-reference>, <tg-time>, and media block tags when useful. "
            "Return only the answer body. Do not wrap it in Markdown fences. "
            "The earlier no-XML rule applies only to tool-call syntax; final Rich HTML tags are allowed here."
        )

    @bot_command(
        "oa",
        doc_ru="<запрос> спросить OpenAgent через rich draft streaming",
        doc_en="<prompt> ask OpenAgent using rich draft streaming",
    )
    async def bot_oa(self, event: Event) -> None:
        if event.sender_id != self.kernel.ADMIN_ID:
            return None

        prompt = self.args_raw(event).strip()
        if not prompt:
            await event.reply("Usage: oa <prompt>")
            return

        bot = self.subinline.bot
        if bot is None or not hasattr(bot, "send_draft_message"):
            await event.reply("Rich draft bot client is unavailable")
            return

        target = getattr(event, "chat_id", None) or getattr(event, "sender_id", None)
        if target is None:
            await event.reply("Can't resolve target chat for rich draft")
            return

        draft_id = int.from_bytes(uuid.uuid4().bytes[:8], "big", signed=True)
        started = time.monotonic()

        async def push_draft(label: str) -> None:
            safe_label = html.escape(label)
            with contextlib.suppress(Exception):
                await bot.send_draft_message(
                    target,
                    html=f"<tg-thinking>{safe_label}</tg-thinking>",
                    draft_id=draft_id,
                    noautolink=True,
                )

        await push_draft("OpenAgent думает…")
        task = asyncio.create_task(
            self._ask_agent(
                prompt,
                status_event=None,
                source_event=event,
                attachments=[],
                started_at=started,
                system_override=self._rich_bot_system_prompt(prompt),
            )
        )
        task_id = f"bot_oa:{draft_id}"
        self._background_tool_tasks[task_id] = task

        tick = 0
        try:
            while not task.done():
                await asyncio.sleep(1.5)
                tick += 1
                elapsed = time.monotonic() - started
                await push_draft(f"OpenAgent генерирует ответ… {elapsed:.1f}s")

            answer, agent_log, thinking_notes, tool_trace = await task
            elapsed = time.monotonic() - started
            self._remember_context(
                getattr(event, "chat_id", None),
                prompt,
                answer,
                tool_trace,
                thinking_notes,
            )
            final_html = answer.strip() if answer.strip() else "<p></p>"
            if "<" not in final_html or ">" not in final_html:
                final_html = self._rich_text_html(final_html)
            await bot.send_rich_message(
                target,
                html=final_html,
                message=answer[:4096] if answer else "",
            )
        except Exception as exc:
            await push_draft("OpenAgent словил ошибку")
            error_html = (
                "<p><b>OpenAgent error</b></p>"
                f"<blockquote><code>{html.escape(str(exc))}</code></blockquote>"
            )
            with contextlib.suppress(Exception):
                if bot is not None and hasattr(bot, "send_rich_message"):
                    await bot.send_rich_message(target, html=error_html, fallback=True)
                    return
            await event.reply(f"OpenAgent error: {exc}")
        finally:
            self._background_tool_tasks.pop(task_id, None)
            if not task.done():
                task.cancel()
                with contextlib.suppress(asyncio.CancelledError):
                    await task

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

    def _format_oaplugin_overview(self) -> str:
        installed = self._plugins
        text = self.strings("plugins_enabled_title")
        if not installed:
            text += self.strings("plugins_none_installed")
        else:
            for pname, plugin in sorted(installed.items()):
                display_name = self._plugin_meta_text(plugin, "name", default=pname)
                version = self._plugin_meta_text(plugin, "version", default="?")
                desc = self._plugin_meta_text(
                    plugin,
                    "description",
                    default=self.strings("plugin_no_description"),
                )
                author = self._plugin_meta_text(plugin, "author")
                tools = self._plugin_tool_names(plugin)[:5]
                item_lines = [
                    f"<b>{html.escape(display_name)}</b> <code>v{html.escape(version)}</code>"
                ]
                if display_name.lower() != str(pname).lower():
                    item_lines.append(
                        f"{html.escape(self.strings('plugin_id_label'))}: "
                        f"<code>{html.escape(str(pname))}</code>"
                    )
                if desc:
                    item_lines.append(html.escape(desc))
                if author:
                    item_lines.append(
                        f"{html.escape(self.strings('plugin_author_label'))}: {html.escape(author)}"
                    )
                if tools:
                    tools_text = ", ".join(
                        f"<code>{html.escape(tool)}</code>" for tool in tools
                    )
                    item_lines.append(
                        f"{html.escape(self.strings('plugin_tools_label'))}: {tools_text}"
                    )
                text += "<blockquote>" + "\n".join(item_lines) + "</blockquote>\n"
        text += self.strings("plugins_total", count=len(installed))
        return text

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

        text = self._format_oaplugin_overview()

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
        name = self._doc_text(m.get("name", "?"), default="?")
        author = self._doc_text(m.get("author", "?"), default="?")
        version = self._doc_text(m.get("version", "?"), default="?")
        desc = self._doc_text(
            m.get("description", self.strings("plugin_no_description")),
            default=self.strings("plugin_no_description"),
        )
        tools = self._string_list(m.get("tools", []))
        permissions = self._string_list(m.get("permissions", []))
        requirements = self._string_list(m.get("requirements", []))
        fname = m.get("file_name", "")
        plugin_key = self._safe_plugin_name(
            m.get("plugin_name") or fname.replace(".py", "") or name
        )
        installed = plugin_key in self._plugins

        text = (
            f"📦 <b>{html.escape(name)}</b> "
            f"<code>v{html.escape(version)}</code> "
            f"by <code>{html.escape(author)}</code>\n\n"
        )
        text += f"📝 {html.escape(desc)}\n"
        if tools:
            tools_str = ", ".join(f"<code>{html.escape(t)}</code>" for t in tools[:8])
            if len(tools) > 8:
                tools_str += self.strings("plugin_more_tools", count=len(tools) - 8)
            text += f"\n🔧 <b>{html.escape(self.strings('plugin_tools_label'))}:</b> {tools_str}"
        if permissions:
            perms_str = ", ".join(
                f"<code>{html.escape(item)}</code>" for item in permissions
            )
            text += f"\n🔐 <b>{html.escape(self.strings('plugin_permissions_label'))}:</b> {perms_str}"
        if requirements:
            reqs_str = ", ".join(
                f"<code>{html.escape(item)}</code>" for item in requirements
            )
            text += f"\n📦 <b>{html.escape(self.strings('plugin_requirements_label'))}:</b> {reqs_str}"
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
        text = self._format_oaplugin_overview()
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
        installed = list(self._plugins.items())
        if not installed:
            await call.answer(self.strings("plugin_manager_no_installed"), alert=True)
            return
        if page < 0 or page >= len(installed):
            await call.answer()
            return
        plugin_id, plugin = installed[page]
        plugin_id = str(plugin_id or getattr(plugin, "name", "") or "?")
        display_name = self._plugin_meta_text(plugin, "name", default=plugin_id)
        version = self._plugin_meta_text(plugin, "version", default="?")
        desc = self._plugin_meta_text(
            plugin, "description", default=self.strings("plugin_no_description")
        )
        author = self._plugin_meta_text(plugin, "author")
        tools = self._plugin_tool_names(plugin)
        permissions = self._plugin_permissions(plugin)
        requirements = self._plugin_requirements(plugin)

        text = f"<b>⚙️ {html.escape(display_name)}</b>\n"
        if display_name.lower() != plugin_id.lower():
            text += f"{html.escape(self.strings('plugin_id_label'))}: <code>{html.escape(plugin_id)}</code>\n"
        text += f"{html.escape(self.strings('plugin_version_label'))}: <code>{html.escape(version)}</code>\n"
        if author:
            text += f"{html.escape(self.strings('plugin_author_label'))}: {html.escape(author)}\n"
        if desc:
            text += f"\n{html.escape(desc)}\n"
        if tools:
            tools_str = ", ".join(
                f"<code>{html.escape(tool)}</code>" for tool in tools[:8]
            )
            if len(tools) > 8:
                tools_str += self.strings("plugin_more_tools", count=len(tools) - 8)
            text += (
                f"\n{html.escape(self.strings('plugin_tools_label'))}: {tools_str}\n"
            )
        if permissions:
            perms_str = ", ".join(
                f"<code>{html.escape(item)}</code>" for item in permissions
            )
            text += f"{html.escape(self.strings('plugin_permissions_label'))}: {perms_str}\n"
        if requirements:
            reqs_str = ", ".join(
                f"<code>{html.escape(item)}</code>" for item in requirements
            )
            text += f"{html.escape(self.strings('plugin_requirements_label'))}: {reqs_str}\n"
        text += "\n"
        text += self.strings("plugin_actions_title")
        row1 = [
            self.Button.inline(
                self.strings("plugin_delete_btn"),
                self._oaplugin_uninstall,
                args=(plugin_id, page),
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
