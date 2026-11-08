# name: OpenAgent
# version: 1.0.0
# requires: aiohttp
# scop: inline
# CubKit build info:
# CubKit source sha256: 1a451610e2e2947d68be888be56ed3e2c4f988e3727c97fa03478e701bd5e9af
# CubKit payload sha256: e67eaf98f15136029482cefd68b743cfaa01868ae83ee48fbc673f85d707fd0c
# CubKit signature: d89524f96b8d8110bd67d46c2a21ff1271eec45504349d35707d755bfcaf6a8d
# CubKit signature algorithm: sha256(cubkit-sign-v1 + module id + source sha256 + payload sha256)
# CubKit source map:
# - generated line 1186 -> OpenAgentMain.py:1
# - bundled files are extracted from the CubKit payload at import time:
#   - Locales/en.yaml -> en.yaml:1 (lines: 57, sha256: e0dea5960b65c0a608685177d0ba92eadb49ba7867b9cd1de8e926c72496692d)
#   - Locales/ru.yaml -> ru.yaml:1 (lines: 58, sha256: 5ac23016c9ba1e944a5820b5b29acc31742fcc6b790bf3fffc64055ed65ba685)
#   - Locales/uk.yaml -> uk.yaml:1 (lines: 57, sha256: 903687b346ff47f666c4f5196f0a6ad9cc64e36d183e01850082882740b73f56)
#   - OpenAgentLib/Format/RichBoby.py -> RichBoby.py:1 (lines: 151, sha256: e46e2060ef5c526d67d4e69e7ee53f04a900956280ef2bde7df01c02169bd57f)
#   - OpenAgentLib/Format/TextRender.py -> TextRender.py:1 (lines: 633, sha256: 09270e8c030350504e1cc7b1af6d3abfca15ace5ec989140bf538209dcbded0a)
#   - OpenAgentLib/Tools/Builtin/__init__.py -> __init__.py:1 (lines: 1, sha256: 5384bfdb2df380b6557cc7a71d16891415bccaa87699406e236f752c6415389f)
#   - OpenAgentLib/Tools/Builtin/context_manager.py -> context_manager.py:1 (lines: 304, sha256: 705179f6214453b18e7a7efea8c8c2d2eca1c5bd49cf9fc616008a238255e2c8)
#   - OpenAgentLib/Tools/Builtin/diff.py -> diff.py:1 (lines: 37, sha256: e436d74075d4c9c16749d70a0d5121216080aa2eb199af363d906c888a2475d9)
#   - OpenAgentLib/Tools/Builtin/edit.py -> edit.py:1 (lines: 74, sha256: 30cb0ece0c2bbd1d905841ab9a2a961ea28a734a9502636d305d052ccbf2f902)
#   - OpenAgentLib/Tools/Builtin/get_reply_media.py -> get_reply_media.py:1 (lines: 131, sha256: 1d69601f2523db9d9166aa9d519a1abfb0bf886a6dfde0b35a6a6887ac0c08ff)
#   - OpenAgentLib/Tools/Builtin/get_reply_message.py -> get_reply_message.py:1 (lines: 116, sha256: 39730efb138cd1dd814fa128d3de66086d0476d488ef305df9ad796cff0d8401)
#   - OpenAgentLib/Tools/Builtin/help_tool.py -> help_tool.py:1 (lines: 77, sha256: f77fbb84208280d147f3bf70bda7d4d147cbe767a2d49b549985c1d9b59e33f5)
#   - OpenAgentLib/Tools/Builtin/python_telegram_exec.py -> python_telegram_exec.py:1 (lines: 141, sha256: 04a7c3db984305b6350d110f425d33317ce6ad368c62eef5d64391c0a91ac03f)
#   - OpenAgentLib/Tools/Builtin/read_file.py -> read_file.py:1 (lines: 35, sha256: cf03fe946fadc1e8e3417294b32b8375e4fca7a9bc2a4697111a854039930698)
#   - OpenAgentLib/Tools/Builtin/recall.py -> recall.py:1 (lines: 125, sha256: 664e1522ae330758872c2b46397e799d1e76efa9c44e051c13a3f677176c86ad)
#   - OpenAgentLib/Tools/Builtin/remember.py -> remember.py:1 (lines: 89, sha256: e8f484ffb831c4ba3391b58e0e70c0f5eb3a1f4c972c9f4ebb71a58d4575f902)
#   - OpenAgentLib/Tools/Builtin/run_python.py -> run_python.py:1 (lines: 65, sha256: 445bf34e5fd77fa952375439d03c051a71d5e6aa3f2d68d0f3ebf86c1a3248b8)
#   - OpenAgentLib/Tools/Builtin/shell.py -> shell.py:1 (lines: 57, sha256: 5f40547f33cc5963eeec7c40fac7a544281d3304794d3b6c35f6b3b1f63f24fe)
#   - OpenAgentLib/Tools/Builtin/tg_get_messages.py -> tg_get_messages.py:1 (lines: 86, sha256: aa35408443a4d20ec2c3c63190e1506e85c2a4fdbe0311633e851f9f8bbb1941)
#   - OpenAgentLib/Tools/Builtin/tg_search_messages.py -> tg_search_messages.py:1 (lines: 106, sha256: 27289605abb5d66ec36260de8eeff7eba068482aab81216c896fa0b6e201d667)
#   - OpenAgentLib/Tools/Builtin/thinking.py -> thinking.py:1 (lines: 78, sha256: f208b9cb11d9688f2d6eeaaf211b95b8e7bc27326c9321df3a6fb88b05e2ec3e)
#   - OpenAgentLib/Tools/Builtin/time_now.py -> time_now.py:1 (lines: 23, sha256: ce0868daf1ec19066eca1177783a39c81b7d63149919ccd44a1428371d0a5876)
#   - OpenAgentLib/Tools/Builtin/todo.py -> todo.py:1 (lines: 92, sha256: 51d0207af233279b475789b02b16bcf58dd2018232a2806afbcd2477db653cce)
#   - OpenAgentLib/Tools/Builtin/web_fetch.py -> web_fetch.py:1 (lines: 99, sha256: 1d69a03b783e08c6f9edad7690e3f4886252c36b6f546c6c81e8ed898df693ff)
#   - OpenAgentLib/Tools/Builtin/web_search.py -> web_search.py:1 (lines: 138, sha256: 1e9465f1955446be1190f4555bbfd5eee5c4720bc1a7463b0a00cb02042ebaee)
#   - OpenAgentLib/Tools/Builtin/write.py -> write.py:1 (lines: 45, sha256: 69327edfb2a38bf3c7a9a5baeed217fc705231c87523abd484bce50be9f1b83f)
#   - OpenAgentLib/Tools/Custom/__init__.py -> __init__.py:1 (lines: 1, sha256: 5384bfdb2df380b6557cc7a71d16891415bccaa87699406e236f752c6415389f)
#   - OpenAgentLib/Tools/Custom/_example.py -> _example.py:1 (lines: 24, sha256: 9cb9290290d317a0028e05cb6f2c654f751817751fc9a4d52a25fc2711f69ed6)
#   - OpenAgentLib/Tools/__init__.py -> __init__.py:1 (lines: 21, sha256: b804bd2624ac13033c9229eb6559dfe9e96f5dcbb7d14153432467929dd1e536)
#   - OpenAgentLib/Tools/checks.py -> checks.py:1 (lines: 142, sha256: deb8f3dd5c89af97614fe671792c58f785a0ab6f34535a7e85dc8009112fd3cc)
#   - OpenAgentLib/Tools/core.py -> core.py:1 (lines: 314, sha256: 4f9359a431301537b6abdc7fcab71fd1c0be89d79452c068f5d6a6f01755b9fa)
#   - OpenAgentLib/Tools/workspace.py -> workspace.py:1 (lines: 51, sha256: 94718847bc2521cd5a4cf047b6b12021ceabf7131714d3ec30897528c5e9af34)
#   - OpenAgentLib/context.py -> context.py:1 (lines: 204, sha256: 956e6073d1d46205810a3e30fc48fea36b97a3ae54014140eb295653a2ad6ab8)
#   - OpenAgentLib/harness.py -> harness.py:1 (lines: 324, sha256: 927457f611b2392fd5df8f394d7803b4d1e7edb315e25871dfb285f8333e82b5)
#   - OpenAgentLib/providers/__init__.py -> __init__.py:1 (lines: 5, sha256: ab0ca84f83bd391a270d95f8ea007ed9a2265594cad8d2e02b2d9626c9234ff1)
#   - OpenAgentLib/providers/openai.py -> openai.py:1 (lines: 299, sha256: e2ccba959e5e56cd6f43992ab8c68f29b7168d7bdd099d11a71c6bc3016e9674)
#   - Settings.py -> Settings.py:1 (lines: 267, sha256: bb64915ca3c153fd3523416fd7d10415c502192084cdeeb9e311e94ba0c7a2a1)

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
__cubkit_locales__ = {'en': {'usage': 'Usage: {mention} agent <prompt> | {mention} agent models | {mention} agent reset', 'thinking': 'Thinking...', 'todo_title': 'Plan', 'thinking_title': 'Thinking', 'models_title': 'Available models:', 'prompt': 'Prompt', 'tool_calls_title': 'Tool calls', 'tool_info_title': 'Help', 'tool_in': 'In', 'tool_out': 'Out', 'tool_time': 'Time', 'tool_ok': 'OK', 'tool_failed': 'Failed', 'models_empty': 'The provider returned no models.', 'status_done': 'Done', 'status_error': 'Error', 'status_cancelled': 'Cancelled', 'cancelled_body': 'Generation stopped.', 'cancelling': 'Stopping...', 'already_finished': 'This request has already finished.', 'btn_cancel': 'Cancel', 'btn_supplement': 'Add', 'btn_copy_prompt': 'Copy command', 'btn_copy': 'Copy', 'btn_back': 'Back', 'btn_again': 'Again', 'btn_next': 'Next', 'repeat_empty': 'There is no request to repeat.', 'history_title': 'History', 'history_first': 'This is the oldest saved message.', 'history_last': 'This is the latest message.', 'models_first': 'This is the first page of models.', 'models_last': 'This is the last page of models.', 'model_changed': 'Model changed: {model}', 'err_context_no_chat': 'Cannot determine chat id for context.', 'err_no_key': 'API key is not set. Set api_key in the module config.', 'err_http': 'Provider error {status}: {detail}', 'err_timeout': 'Request timed out.', 'err_network': 'Network error: {error}', 'err_bad_reply': 'Provider returned an unexpected response.', 'err_tool_limit': 'Tool call limit exceeded.', 'err_unexpected': 'Unexpected error: {error}', 'error_detail_title': 'Provider error details', 'err_config_save': 'Could not save the config: {error}', 'cfg_api_key': 'API key of the LLM provider', 'cfg_model': 'Model name', 'cfg_base_url': 'Provider base URL (OpenAI compatible)', 'cfg_temperature': 'Sampling temperature (0 to 2)', 'cfg_timeout': 'Request timeout in seconds', 'cfg_system_prompt': 'System prompt', 'cfg_context_enabled': 'Keep chat history in context', 'cfg_context_size': 'Message pairs kept in context (0-200, 0 = unlimited)', 'cfg_tool_rules': 'Add tool usage rules to the system prompt', 'cfg_context_window': 'Model context window in tokens shown next to the prompt size in the token stats (0 = no limit shown)', 'cfg_stream': 'Stream the answer while it is being generated', 'context_cleared': 'Context cleared: {count} messages removed.', 'context_empty': 'Context is already empty.'}, 'ru': {'usage': 'Использование: {mention} agent <запрос> | {mention} agent models | {mention} agent reset', 'thinking': 'Думаю...', 'todo_title': 'План', 'thinking_title': 'Думаю', 'models_title': 'Доступные модели:', 'prompt': 'Промпт', 'tool_calls_title': 'Вызовы инструментов', 'tool_info_title': 'Справка', 'tool_in': 'Вход', 'tool_out': 'Выход', 'tool_time': 'Время', 'tool_ok': 'OK', 'tool_failed': 'Ошибка', 'models_empty': 'Провайдер не вернул ни одной модели.', 'status_done': 'Готово', 'status_error': 'Ошибка', 'status_cancelled': 'Остановлено', 'cancelled_body': 'Генерация остановлена.', 'cancelling': 'Останавливаю...', 'already_finished': 'Этот запрос уже завершён.', 'btn_cancel': 'Отмена', 'btn_supplement': 'Дополнить', 'btn_copy_prompt': 'Скопировать команду', 'btn_copy': 'Скопировать', 'btn_back': 'Назад', 'btn_again': 'Повторить', 'btn_next': 'Вперёд', 'repeat_empty': 'Нет запроса для повтора.', 'history_title': 'История', 'history_first': 'Это самое старое сохранённое сообщение.', 'history_last': 'Это последнее сообщение.', 'models_first': 'Это первая страница моделей.', 'models_last': 'Это последняя страница моделей.', 'model_changed': 'Модель изменена: {model}', 'err_context_no_chat': 'Не удалось определить chat_id для контекста.', 'err_no_key': 'API ключ не задан. Укажите api_key в конфиге модуля.', 'err_http': 'Ошибка провайдера {status}: {detail}', 'err_timeout': 'Время ожидания запроса истекло.', 'err_network': 'Ошибка сети: {error}', 'err_bad_reply': 'Провайдер вернул неожиданный ответ.', 'err_tool_limit': 'Превышен лимит вызовов инструментов.', 'err_unexpected': 'Неожиданная ошибка: {error}', 'error_detail_title': 'Детали ошибки провайдера', 'err_config_save': 'Не удалось сохранить конфиг: {error}', 'cfg_api_key': 'API ключ провайдера LLM', 'cfg_model': 'Название модели', 'cfg_base_url': 'Базовый URL провайдера (OpenAI-совместимый)', 'cfg_temperature': 'Температура генерации (от 0 до 2)', 'cfg_timeout': 'Таймаут запроса в секундах', 'cfg_system_prompt': 'Системный промпт', 'cfg_context_enabled': 'Хранить историю чата в контексте', 'cfg_context_size': 'Сколько пар сообщений хранить в контексте (0-200, 0 = без лимита)', 'cfg_tool_rules': 'Добавлять правила использования инструментов в системный промпт', 'cfg_context_window': 'Размер контекстного окна модели в токенах для статистики токенов, показывается рядом с размером промпта (0 = не показывать)', 'cfg_stream': 'Показывать ответ по мере генерации (стриминг)', 'context_cleared': 'Контекст очищен: удалено {count} сообщений.', 'context_empty': 'Контекст уже пуст.'}, 'uk': {'usage': 'Використання: {mention} agent <запит> | {mention} agent models | {mention} agent reset', 'thinking': 'Думаю...', 'todo_title': 'План', 'thinking_title': 'Думаю', 'models_title': 'Доступні моделі:', 'prompt': 'Промпт', 'tool_calls_title': 'Виклики інструментів', 'tool_info_title': 'Довідка', 'tool_in': 'Вхід', 'tool_out': 'Вихід', 'tool_time': 'Час', 'tool_ok': 'OK', 'tool_failed': 'Помилка', 'models_empty': 'Провайдер не повернув жодної моделі.', 'status_done': 'Готово', 'status_error': 'Помилка', 'status_cancelled': 'Зупинено', 'cancelled_body': 'Генерацію зупинено.', 'cancelling': 'Зупиняю...', 'already_finished': 'Цей запит уже завершено.', 'btn_cancel': 'Скасувати', 'btn_supplement': 'Доповнити', 'btn_copy_prompt': 'Скопіювати команду', 'btn_copy': 'Скопіювати', 'btn_back': 'Назад', 'btn_again': 'Повторити', 'btn_next': 'Далі', 'repeat_empty': 'Немає запиту для повтору.', 'history_title': 'Історія', 'history_first': 'Це найстаріше збережене повідомлення.', 'history_last': 'Це останнє повідомлення.', 'models_first': 'Це перша сторінка моделей.', 'models_last': 'Це остання сторінка моделей.', 'model_changed': 'Модель змінено: {model}', 'err_context_no_chat': 'Не вдалося визначити chat_id для контексту.', 'err_no_key': 'API ключ не задано. Вкажіть api_key у конфігу модуля.', 'err_http': 'Помилка провайдера {status}: {detail}', 'err_timeout': 'Час очікування запиту вичерпано.', 'err_network': 'Помилка мережі: {error}', 'err_bad_reply': 'Провайдер повернув неочікувану відповідь.', 'err_tool_limit': 'Перевищено ліміт викликів інструментів.', 'err_unexpected': 'Неочікувана помилка: {error}', 'error_detail_title': 'Деталі помилки провайдера', 'err_config_save': 'Не вдалося зберегти конфіг: {error}', 'cfg_api_key': 'API ключ провайдера LLM', 'cfg_model': 'Назва моделі', 'cfg_base_url': 'Базовий URL провайдера (сумісний з OpenAI)', 'cfg_temperature': 'Температура генерації (від 0 до 2)', 'cfg_timeout': 'Таймаут запиту в секундах', 'cfg_system_prompt': 'Системний промпт', 'cfg_context_enabled': 'Зберігати історію чату в контексті', 'cfg_context_size': 'Скільки пар повідомлень зберігати в контексті (0-200, 0 = без ліміту)', 'cfg_tool_rules': 'Додавати правила використання інструментів у системний промпт', 'cfg_context_window': 'Розмір контекстного вікна моделі в токенах для статистики токенів, показується поруч із розміром промпту (0 = не показувати)', 'cfg_stream': 'Показувати відповідь під час генерації (стрімінг)', 'context_cleared': 'Контекст очищено: видалено {count} повідомлень.', 'context_empty': 'Контекст уже порожній.'}}
__cubkit_metadata__ = {'id': 'openagent', 'name': 'OpenAgent', 'version': '1.0.0', 'author': 'unknown', 'description': '', 'requires': ('aiohttp',), 'banner_url': None, 'scop': 'inline'}
__cubkit_bundle_sha256__ = 'e67eaf98f15136029482cefd68b743cfaa01868ae83ee48fbc673f85d707fd0c'
__cubkit_bundle_b85__ = """
P)h>@6aWAK2mk;8Apm2ut1Yqv007Mh000jF002yHV_|G%b1!9XE_q>XY;{%JjvF@&efL)oeoBGXSmZHi3T)G)U1YZjvdQy69?`a7
jigGPbzFD<y`(NP6T|@q(CCOakv!Cx)E-~K`b$|a13EI^Jp*qY!LK3uA<%E|-*-oY*J#s~gNO-fy`qD0N8|Qv{B!-
?Y&ML0?K?7L#qCF{+$=i5O<}z%UZ#WFCuOYKTCDD0tyd*Nv6X+sfwx_+>_Y7`Ly)0*Y}{@R;xDve!g+t^>dud1_rutXk{Pl!UYf*
F1m4%(j)OzZ$h-
VAMUNcUIbREb!+kOuBd3YR=um_6^)j5CM2g1LY460*AG}N$#^@u1Z)Kg(Ub!A^@%pCyuU8Y?ZM_!Pf1<;vq)d>=hk$xBNtGf!3fz
jMY(%Bc-Of0Z4%s@_ByrIHjF<=xDnXTjCc|o5ay6nUoC2mX1dGxrQbet*s1N6Es^1&lLGOn_xy5-
sD8N?rlJMVoDS+CmT(VnP3*_*tSo@oo^(taOMau$21ilC7yj_LlSEM+8z9RW}o;#!L=YySziCQxFBd(~oTI?kC#Kjyi36mDKtoly
FDiV!Zw)V+2>luT<a^QD!qg0Kn#(yZ^^#|qlxtb5MhiQMw=g;dEcNwSM5ofP+UKFU5(s=@ngmEwqMUlX0*!c)md{dNJ>4=i++mCm
^e<j<T9;6LCB7q8~%ec$ovg48I%tm%*Uu_(SLLqdaN^X6)l$L+yXgLsOSPfTLS(y5%m6Q<;jJ24MPCg!USL8paWV+<F+Sw}IaVOa
G()Gkr<zVF23fL3xc*X_q5>^M9{niYImcs@z0{FE@)R`Y5J6n;lJDa=`l8;@v={zsLO-VUTQ`tC$o%CTQ&1iMWJOeq^MPT8g-
|f3vjzz(^ZAAM1{$UzcMKt%w)H_be6cl``5_V&>%lHI?FQ4w=#fO0I_D+Z$c>eI{{;6mYlTt>~7$w|CH3S(%uz=ykjj;1&Q@C1ZM
x>Pz^6hjglIfh-%sg2h^BzKdAVj3~I68Svq!jNFL+R_vTrpe4zST+QUkUl4(3iQ!6y?kXT4-
?Wzr4J;`5A8DH8)P~1k~*&(k_wPK9y+*0>GH9Wmv8)HAp`W{A8T=r<uvsZGkhn{1IJ(bnqt!G8CK9Vh!XLjf7bigkMRL{#xc^Y2K
_}!%oBlf5=aT{A5k#(uvD`I`D%BEYED;qSSF;9-RCb)sTCODwdb3Mmr&w-
j9x++enm$X7Eqtk!qEyGrZ}V`31^HEc!oCO9KQH000080000X03FhQwqykW0HX~601p5F08DRVVQgh{FLHG*d0}mAjaEx*BS#Rv>
sK^7Ij}3t9!(P1;}VArft-ht)RG5}X2eV@j^Y?(DULU+vG68`CB)h6h8zRq$HZgn^%uJTQL3tYo|eL5usz-NuCKo8L1=gR4y((z>
R7JiQqI(wyo0~jGLj3K$asex_P8e;-
#cO;>k0NL2t;zFMslf+KW9HY66pDD?uKhF0v>WvuZca!+jqP!`u$Z+<XlGTywPaDjo<by;Ru&vdM9TXMXr!vWoq@B_ExyUu+$g?R
&t?U%b0=WQr^lK%q2VZT0ii6eL)T|2e@6SG5Ypht7W@ITW>(0s-
a#pD8_;ekH~inUt_#7nvT~gg#MoD6G0gtWRyv0lP4IBIr9g?_$eI=r)T_+z|mYyQ}KN`effp?>e!CU+bH*kdIjNKX=kP&9FiR7Sz
<%)u?lL$ptDewYy2Own8+EPB#f%GfZz9}l0jcWVT(a%wSAAm`UOf%xyxmC$AiER9>roVTejEYZWb(5k>G_EW>`tIlgU_3zdh7$@C
t*B)K4-|Q>I&6(Ty6JvH?}@AtI>+vo{d4-
GJNeq1ACbC*0E!{e#)4F)IR_L0$gEGTo68h(f(m7jgk6n!+;~X=h^%2h10*!a=|9a)iEtqaG|QF`(zn===Sll_T*zlndpOv{xv}=
x|Pn+^R{gxKTrkH0>7RL|%d>Mt`f1?XImM_>K^bDUXUFdHg#KMzD(MUZ7&Y``i{em@eU}TqqeaK*|ievnm+IuIxFX@PlDK7H_FB+
V3>K?>IpyvPLkpNdSzQZX~6MAE0_dbG5)$5DN4${9LJ@sSCha1=p@!w2TpgIN}D89&ge%BUFh?*M(|5Wts{!O9DEh;>g7EJ~#4z5
vb|MTe4bvw%65w{XG>xkR;Fz4L|}R5;n>o)oU=5fEQ0dV=d1|1H$wW(R~XpXEae~IQlE%8Z+|*Ka{tecGg}59FkrvA9P<D+69>2=
ZKEyU%f!7nL1aehGYnTm|KI%zmOAPs1mfn?7o9)z(c9!A0d^SjIWWG)YQ1x6QW-
s7p4JNBsMra)QockRcLbo1Zm2EjGB?HAyv#8qS5hbeyQL(p*&;ENiNfDxj68H{c1Fz0Fwa=h8+?W8oy1uZNUt=o0zyl!f`1iTwnK
$$QI?sCITXV*XcRg5{q#|K`;OSMtnENA~QTS+kA;--mt-
p*#QthpSOgD*kv^qLOsNirCiR`4=i2q;wFxXhG(=}GR0(V=Q6Z*oURqx-|`JeEs}u2X%Rk!pjw@-
WkB`_o9m#nyZfb9qVdTIG<yn_wxSko+99_F0ZCtwG(8reYu|jmyWY*#%Rcv>zj#W-bB%o<kU`H-?-
OlT0O9fgkQ`7QJ|JKX{UFg#$Px}qaX~_5w`h-
T<H#=Av(#9Q{SOohzMLj&X#AQ`4AVWqjRQg_+CVrAA)wN_N+)BUf^=1UOQBLqJlwOJX7m4DZd+2=2IowjVrn{!M^qD+ZHCVGJYRz
NW_{4y3ajEVqu;YCVAgqHTiZ{cZErt;>V3ulsIj~&%#w`KV&d=x1DA*CcE8fE4B&FIoj&{$e7#bV>mJrPOB=?~^x@+xeBgL({{X}
JlOQ<P)Kbk5x8)6%X$e=0@}5b^>6or)i>Q;7_RR_&n}8CU;DRVb{6w#QWcNFW6;p)C2XW9IsVRa{&KbU`MtOjAR!j<KgKAHUqhb(
iYdR1Lc)|73hfGDLz?Ni#8E5g@X)&vpdJK0r=)n}V<#IdFu>GxENOW-
u)gXB7<ora%V23S#;EAI(C~V}$v*%RRbo%IA!F(PQ;n)5HP)h>@6aWAK2mk;8Apite5BFUK006HI000jF002yHV_|G%b1!vkE_q>
XY>ie+Ya>SxzUx;sIytZrW{)Nb>~V?1hCt54NNP!gM>Ark6-RLlwv=6OV6jMIWC$^v>>;@-
vTVziE&YY=f0U}~nwK77F9XwE@A~Si?#6CY?uoMgRnPQ;UYHX-GpDAn$NEV>nc<!|YRf=*VQ?%!GEm|(eFv9I5bJ*-
eq6h5hjr=48!jRlOI0qZmKPj&K@)vmn1O!OV{=}qRNyA8hmP`;Pw~9hbBrNV$gWbga>;tjT|ovAJqRoz`jG&+g`VmgJvXDha;X!A
?T#Yzkmv$#m!^-NL*J>ne%_L;$DF=1VMbsM4WE$j8~E$P*@Shypb-
{=&=a_wg6cSxAfx6rp7UAQRqUy7th_dv`3F)wO+*ji<kgq_*Kj>w)@_wAi5bL6uDBc$lI&$!PN0zYSOs$;psP0mii4-
{4|xpqMCe;8(-TzhvQRT<ORQYgjh%WJP*lHxOrO*j>79(CFxn6fU)S8ACVh_hl6o`4IM83Yl-@eku-
>yS@Cu_Fn>S`;&V{}!YE@D-MpA0k3>i(XA4#{~a~fXY#VzamZ_vIM8GZ$5-C{lPgz915rVgqq;K)(+FU$xKFu-
a;0cKVp?shu9M5HH;x21hT^NCO`?DU)rdT0vdFtNm#prc0`x~UmtYFp&3K-
H}wEc6xVVFpus>^5DCw)cd?J`Z)O7Rc{8+A+4cT#95zx++7>71RLd>mpYwGZ27@xfwEetXVUFLbbeDg;6iV{~IC@ydIfhcHi)#Sa
BN=hX6{;G$i=e_TgXZ`wg}w2UQv-EYO^eq02eHzMC_<$dT8@|7r866oXna2F4;w0W_fXxv4-9Wd^o-
AAYP2r`B?VrbXx<>FB+~YCMuEArgrgrH{)c7&ib%prDUV5Td%`wg~{p6x&LX4DojcW}w#Q%tAn*wByy&ZX&jT%)rTmWzLFq0EQ1F
!r{f&FHvf4&dnLq2Z4>!TvP<`7v!dIp@)5l+U<C#C=f8#_D_(+HU3ieFhO%_06J+Y)mh^WXu~RP!Qqi5lVhkuT`C|zE(EeA6DbiU
HsK6BKG;#^Ruq8@Re^e--6dziIZJgIMh6=rdQ4ymYeXCo-?9IyTX$f9{B3-
@Mzz?_l@KW=LTQRu^NwR8!uP$lXV(_Tff@X4fgx~+5h=iD)NkHexSqD|EjHc-
F6hXbvf#T~kBqvJFGVr?Fmh}&^2_grMqrNHH?KO|*w+-
z4X^3M?ssw<k~3<!&KQ%yl?$rYXgUnRHSBJJ)&BlhR*8lyW7A1tT#+SFsOrYj=|&{?3&}00<oDv+Z}vAk*rBC??K#D*K>J6$>d4^
5%TKIP1;i^O0Cz;me<1c<^8N$7k{NxyvJ@}Hjzx;t#aUj6=ZU#&AU;qeNaX_rM{x##o@nR?xN|_{wN;OMF$7dtSN1`OQE>vx{No9
g5;l^7TTS-7?H9I(cN~@=-
3#XeCUBgDvc^KAqTSg0LGmgDgFudqC)^zyN#4@uY6KfSiJjd~pYQHIgF1dLPzCyvjg%QAWyLv+y1tB)O+Tea16#(Dj0p>K?AB!SY
kKQEB3(j1KEBe2UQiDYF_b?+fHnn|VkJA|2grV5>E*%Ba}L!61ANUr5V`;a$zI^i+~<(^6`YD<%+GA)k^JF#W-
gHa?W`{C+W=+`<n9FJz#(Ebg|r~?9jbh~?b%>bTdses;62w)sCh+Z1AU?soDPE7>BjltMvQpPUZW>2Z_Sr(WP$v9v81$LGWOlGy|
z?k`S_?7b^~?11(%h~N&4Vgb&)(vsg7`WO9jUV!+%gq0|XQR000O8001EXge+m@Oa}k}UlRZT9{>OVPjF>!L1$%dbWCYtFGg>2ZD
DjTQfXsoLT_SuE^v9hSL<%u$`Ssrr<g+*0hvg&gZ`>2DaeVH)1XQm<QOelTcuaz%G_khWp`I`RG$ESnm$;cq%*rqiMmuxfP)IKCG
KUe-+VJ%YE?m&EmwA>d6t2w8l^3;x>lB1p=#6Xg|*UFvi+@jZ%H?4Ep3=KT(?*MaQ$}n-mUcfnV-
3}qP{onfw%|wc{!V1{dszsUBCS4=e}F{)76{q<BzkeSATTR+3TwhKfbxVoW9H6yvtrqXEQvK^m@HqGGie7Ao9{{jJL{@Vb6&v_!9
jSwXj(h8!nf)0pW87xvD>NZL_>&TJxnDLi9x1-
$#It;xjkE3`C;{L=7dY3(2#BS%%>$K$wmk%?I4%tl<UNl4}m}zU1+1CJhH8B(JSpL!nhe$MH#6!A-J}W>yV)lB64}4@6z-
74Mu!r&42C{%HtO7<*%^p2HY!=DSDK%AP(T>MZ9{4$)hS+ZWpa2H#PMwwB$yIQ9X5^?_NdO(&*eN$Y^{p`dlMygk!3DP<Ujx`-
W;d<>oV^q$*|!p!n7Hcmikh@vFf5u`anx9;s5fXYuI$mOu>Hca5+|8C+2^SheQU{vY}oWn>|_Y-
&!wnRICfkDKVn2ygJBaGN7NYD^!jsO9LRucTGlU|&%d>M@%apmhII_<y~a;;Rnl^nqBdsQ9@&|_qas1K1XqpwG@)8_8k7@i-
8E9(C?#C{iAzr~~TZWK8d|F4LyeOLFr{GaYQ_=oilf$UiLP$F6V*IoKp)gV!H(9ozRP7aQp!Ar=cGS~&2&Wf$68Ay=}qC(o@KzTF
{!^n!FHlpAl?13zD2eqDr#!-
ljQSF!bqQAR3faizy?xzMbdj5!759*?0(0J@h@u(dO&Dp086n+hk^fvjzIm82XselIh*@43;nRK)de_tufeY@&Pc3H}pl)j6?U;@
}jy3O>pTp>9TQi+8ij0MIDjB}}EVPJt6ftaWFDRP<BOh|%6^x?^6w8tJ!TL(&~v3N9L`>@=}o@X>Hru3r{b=(S|slrVRR*Nd5*u>
<|kX-F!^Q?q*?Qz%rD2iSoJujGKb&lx0yQ52YcL)sp?QY=%wQu9<&IA6TWIj+i-
j#f59r#le)(g18QNgKCU^EWO_Z^^ZpQFX9K*oS@kbvz56NMAl5@~}JA>c)0!r<Z~8gA|MKC)-
*B;O4E{=Ca3VIHDW&KV55UJ8slZX_tFvw#ubO_Udn|8ItS7w22{55O7kOm@lMcDm%eh;vHWrp(&-
kJ~d_%qFSEbO~ao&3T1Q)09fNpkb)n`w2Y5;0=5ryPj_^U_SPSg^-Vp4bLF@_dov?b;{$KQoUtCghEl^!NodUqV+-
)juw`LGYS@GS_%xtV%?F%zp$K$(-
MNJRbE0|D_x<VYb*t8B@V92jRH6sU^O;4CU?T*Q$84P{poc}!kOLc5or@kA$Hu1x_0)sL0B#!K$j*EwWPtsBF9xU{<?C(j3P6S7E
vGNU@<PFduCAL06V^oN=wgA+&@-DDe59vEtQn&!3PCpHZ13)zYzC`XvFOqG?EFA`Y?pMa8=CaB`?w*lIWWm&Umk`-
oBqrucw$<&C^^}4T3$^QT$>!!oQoBgTJ!DKhA%c-
~4SfnLkZl{PN`NMOeKU{BHhu(f{r9ugPy{C^>_v<Q2wXGl$_oj&p_WLtwIxD`N+tbB$JVGLm94I(Pr@DTQmckfFh$G^C{U5UmGZH
5k>AEhgj#gU?K2`so-tGJX60`Y+jZHhnvNcfIR|&sKzv{D8jL;ul*cH@9XoPvYRh{O0yyfNtUTt!Z7H+?uDO^V{c>sJEfHMz3m|9
>|cmV*1mnaa4CeZ<qMC671zZ7^aUVHJn*qAnM|p8%u99cm!W&FhWwY21!ohWGX40?nkm=H_txwBC{<cZ$KX}uiOjBZVXbhTGVlbk
n!h|Ze<b(+_j@c=`RGIHDZ?QY@v$vac=L!(>@W16%5~n7E00V;M?JTSUxyeP^ki)q<2qxUu0Vn(8ymvno`d?cXvUqdxgWEfO#i!W
^LDG1oO}`7n~U39#N$!%0oKk>d}chU6UxJ<g)M$7sDbXxC#QokmQ#4Jq3|QCyr_EgGh{7z#0jHmcpa(WP;dlP+yyDh2PlXRMMwf^
i~CM_<rUAvj{{*^1@qh+6K^lJKx9PvJocSv?c3KeqFK-
8@P|`8C>#Q6wWGVt7Z@G2F`oREl9Se+AS3Kobhp0H3&oh%7lcA{UJzl4X(|CsN0aa-IAHi!wD@8ozV5*U}%e*jh(@{ePSXsJ21Qc
zHLr>nBMjIh~MGd)~o}~I14qC$L^TtRDK<uH<KX5>h<>8cXVGT=-
b+_N5_|(Hx{PuOQ?Ehc*J84tyB*Stv>Pkd{sL^jy<WmhTuJL8GFEyl6xl&TXMNRX2>@<e=KPo2|E<InGm`SvokBU`+-i9-
hTj4O9KQH000080000X0Jrl59%B~(0Gw6;03iSX08embZb4^dZgfm(VlPH-
a&2LBFH~iCbW&w*WMy(LaCzlCO>ZMdc6a`Y+BOoBF-1uW7)WGMh&-
0#iDxWB(gthDM61azQf)Q6x!ujtD2x`l<O9jU2sQzdL$W@tFS!KBVFTpX%pb`9guIWc>Z<;rC~15MB4CDOb=9l)s$RYCYR~gtr{O
9NGLc2o>zzWrEkq`hP-amwA9gy&f|_P&wg?Il<suNFoI?Mgh~7vMM|mOAnaCGG9E$~llKD`ayph?R`U&8s68h$ytE*lxmq{@Y)8c
La>PiGj2v3VumH^yDe17rzm6%?yk{gj`;_B+lG?7<VL-83+4qY-Sf;^XtNi4(8ZB$%~MBc_xB1JBjh*Fy61Cgg92tz<0aGk{Il%P
$ogJh0v5dcavpihLU%tewGolO2>6#?ubT}`jCPjM~9LgqPOyE9ouF#%i1;yMjsa6-
?Cl3~a5yiRA9r3>NvvlWmceP2Y2WttU05<rJ_N|U_PQEk`7BG%uFXd!uQ7!(04D$the!KP^-
W|53T?pWL{i3sj<oZJn>3t0I8R%9S9zW(aOfARUri!WY&`6mjib6FHH!hn78v-6A7*Z#@t(?5MV5U-
Da?w_4}_3CRFc6@dYSk7E12OR-_1nG1slVc?Mbr2;QoM}|k4bOm!K1nBcx&!l)KS{$o)nj;(rg1*JO|zSP8BC?_xd?8gA4ap8?l-
LB-Xml_e+d+veeHjF{Ad2f#j61|A|aoiTpYiA#gwSl(@#%cox43RPETL?pB$h0IOMCBuU?&3+TETm(0-@W`D3#)9r|CK5s5F-
1WyVt7;pt0fr8jc9SdMq83L0DVkuxw#bN>%XGn~MV{f7)JP>)2i4njN;sfDjt0VzHp7;ylg>We7i_Ee#qi@q7naUW>ghv1f4F|vi
cMNBtXVfVN#*_yljHbmUbR8fsjR6>*IT%MDFfy3ZF~<`k;iS_j8V_)?pf-NQyxI%pELg>bKZEgUb~nOqeZnLSWehA097~_D%LHzk
F7Nz0;@Di`OoPe}uoo96Kfmx{mw)!^<lII^pNY#$&v2+WaCd4vAV^H|7;#_UGr-SI&t4y2H~@>)5}?snKw0<hbbwI8&*wevCBZ@x
hJC{bXL1fg668%#3RW!|SNIzw9S#FYXLta?f|yN7r1fTrf<|0vk$j2cXw?(*oaHIDbgZ8Sn2j?F^%CcS_yfhNOoG@sqQz+<MJa@U
1UJc3;BBo96m<wVFNw0()?ltCRA})6v6eUx&ff8azJ)9(kpp*231fI>A*>eI8Vz~}#M8HFghvYGf3hPN%fe_Y(mxi~pg7?0jKn3a
(|{JFkJu1-0-
o7)4d=4xS(6P!uiqaNpbx}rB?mw|!D0at1xiAK1%e_srz}n4JJHLf6eubcZ9^EPxU65EKtQb5gM}E<$wWoBzV8zf-YW9?c0&~_mh
8|Wn8B6~1V5N1ND`lJ!&9`8xCT)n7ngfu8iwDoFD=m6^abf9-$GyBeEQX+8T#Twu`fWu&@UXxU_lOm9U+q*0qPq-^b-
K&GAnun2hi3?0{YYuw0;5Hij0S+6FKT~Y$)U9@@>ipYDt;ebUZ=0R`%hdMYAB3m_>%eVbjV3Vi1Q7i;|VJC_$4(^SW&V*&wNx3yG
*321_^wVUM2o?L+N-lXyd9<Q{b-<zx#Z51C?>``0pnQ{eUKh^b$VXRQ51DKU9a>JFgC@Lfldzz=GRqR_=g-
ZdEq%N&jXEJ^UThi1@lDYKbBO;<2$)`M9Y)+LgV6&}dyz2P1cPbvh4q9rwy`7~I{9$?s01L(0gR{Xup(l-
%`fY$!H2My7LAZ4hB#b{J&-
;$t75YG8PINLSz4vYEDG6G9DFYaPF>gKEI6qJ1TXiaF{AMUCSN8aFpq01~<1lb)7)fhI99;+42tp%@AKsJNRS~QE&!>COaroaSj*
un~-
>1B9`K$QF{<LVr2j%=PJ1RESyx@`^yVNa6FX8|k?qyFRfZcU%}umLvb(A52>ZR7?X7&GgkLIBhZd$J_QR+i<SA_QB2x;REcqNJ$y
=4U)c9UIs$d{Sj%EnPO?{kvcP;}61F1O())fzn8^nuMo+@>C@VcMjIa#aosWb;_qKv-
q(?JPyjEKbL9@a|?8zMRRv3cB+ju?Dp<&|IJf}OMx4SJyu}4sq;vBfB0Uk4N3RAYcpR1=^ubSa3jH2&H-
*g1_U^wx7R6|Edkoj!5eZhiXaAUi%+#p0jdw=$UK8HuFaalFBn{XA<KvUB*@K*08H#@_SG7q=24^60P1Mi&w|><8rvSF-
~IYme<#-dY@q@6EZ`1j8i;BQx89m}-
~ESJD@AoM{ORmIukpJ!wY|gT(Yh<Ttc!UDL}Gd5HL2tz3}TR`6}4P@@JJ19Y~FM5mVqG{h`=aGy24mQ)tBp$xW#yh%-
%%chv(Bw;_{L0i@-GBqnsy;khhwe9}?pIj*-`O2-
FM^wEW(z*zMC=)$eKxO2(nhc%mp5US|v5tBG;mXvJfd?OvgSU)gE9?Ma*b<1Li2R}4Dud3DY&UcUIk|LpAe^~pK<F5bKE{~j6P-
S_{(AOFQ4zvYkr=8ym6kKgde5B%{r{P7(us|D3RKY4Nb<);XIZ@B-F@+<Qqn%?-
c49xhRKGR|rr$Lj;NDCG4n4NqXB?+7(8cR;a)s=z(j${sQbrM?MqV|4JOrmY8y0ZByc0~iGeerwb{@6?7?3w-Gk|r28h!rF-NMIK
*-dGA1r}?QOMY+)!6XJCMAD@&9g*U;Arg?;!r(6#*-
*KaxeN?vYnc5`1g^mr*K*eRiemlH*JsRIvu17}k=_D;UdPQm(I#)z>E91JSsm3pTSFLpP0%tN<_&Bz=DWq0gQjTdC6f^;$93=Uz%
sv*=V0w-066B(|O-<x5$ZwR-Ensa_n8e8G2R$#Z3=EQWX|%RNA0KD~ldS_nqp>eN@=B%7J=M$<X{Q#968vN&%8;l7wukKlJ2<RbD
go&Mxxi5nk1n#6?3Y%&@eVDV(D~;X>@8R5>^Gem99$k1{Pi5S7`Ef$T5l!pph|p%n30$TnT}!Mrpq@n0n07I7y_|vluT39+pyYtT
NMEgkC|gcyTu-Lg)EFY-=M#$2-ClxLmF6~Kp7)~1|~96ROB)S&bv-;fmy-
);<O3rCLjpo`!K8KlNKtPg9K!JL<zZREs{f1<x{_sAL*xMUSiODgpm>xD*+i0RZn}?!*O)Pqa%-
w8l{!MY9@gFDw;J*l@d+ASfzzLI-ExEzcYhtDs>I=MO4JHOY_noK(YdOjTFFR3%+gBwyAa-oypO<SrKpy3V~OYd$bkyUA0~f$kh!
YcE$b4swhhJ<TSq5h!pdR;@$Jr5>D0veWqTNELQ-
7rxbHc0nVZ<$F(425Y$}`rZ4+UtmRmT@EA9AV9Q4{i$5uV#6eRhO>x;_T!pPrLmpILF?pk&1Bdh1v1WMnq;`;4)$!9EAOSoS?V#`
orO&J$j@YRqT?BJh5*2ISeq7skWM94AB<G)Ef&iJQ)^T1}p_H^*EVzkx!8-wuHuN*OjPIC%Ys{;F+R91KTvJeWg315!Ls<k-
tO>W<o~dEZg4;5vNpJ-t7NN~LO=GlHq6z2~PJMHR3E9|W8P$rK=-
p2mqIXqk%($!2REtP<DOcetTKZ+LZ|@^_X`ie~pz)ae=rCU`&|rILmklPijMZbkHc|PY<ZgpplimP$3aZcr#^b0zK67~Qa95MKS%
k(i^zB3Cwm#{2J^B>6b2c2KW;fVIyKH%y3k=;rj{!q6YW|#}PpY}Mm15jPA)(hD=y^u!6DTdW*xOF=VP?Cc_R6N`>{rjiq)Ct~ip
?V|9s!TXq}sbAIYwP)9q?$I9{u}n%}=snW3+N;MJsupqh`HQUm7k3s6<Dc#wRV$5^E~h1+Qo-eBwlRu_15otKyjZWoJwz+599nq-
_w555@ldE`4=k*(eEl?jy0!o~ox;sf}}&M{B!y=dwEq;=DV)cTKm+Mz&UqYYDCiBbwcBiejl@m}RYO6E;0PhLzVtgWS&RemS<a20
wX*?pG*Nw!cYcA<*e6%Vbh0Mb{iqd(h&{&?BlQqR}f#YD9nwC8q_aLOH58(l}V=BL`7Uj*c9DJ&>6Pyp)@g4}b%2h*dq14ZwpA-
+1W_xXN`9!eS&PFtl|2gnkaOLU0%*=n=X8525bn!FXVr_*8f&{e~`BM>XQ8$$&xh-41-
DIOpd)z)ePblcECUBg;#J9Vlb`YhI6gv1YpNO)hEM-L}%mO5f-
fPS*5vHAPy~M8u{rt1EgLn<qr1Z73SCep?LIIy+?n!Daas*RDUPo+~EJIWxF8Es`P$-c$qyv^>-
D{UiW$c2|5!6{_j2Dw~lgN24S_KIRjIBFWgfn~v#^r6-
JRKOBku4OI}pz_|&r<+4ykbM_)4lVeUEZ0xcy4BC1(@=jGjl|^w_&nA}#h@>lP@$Uoi$tsGmwrDC3F#MF=DGx{7rmHv<DXe978|9
cFGF4uQycL*;oxs`~P(U9{Pcj)jWWdl((qqdd^cZg~KT3h2g*E491}(intf)20ry00B^?r_Q!DVTH#mC4~$H=R9D2jO0R6=V1wTL
48s|AhB!gOq(zp;8r@er5?dsZ-u2WY{DeBj~EU?OBvB)<B-v)^|ZQ5-
6M+_BlQ30Q)0U<FKlw_xFhw?!MOzFRH&AcU16)d2`0>ZW2<q9C{UlS~FTTB4LK&#|7p!|QC9T(;_rAVI-
I(6jNcC(ZPMI2PBiw<(;pHxV4AC0BSC6iZF9Vv?alOO~$Y*QGI}wGKY4*+>e(L0fFpJomhQB~$G+dD0a-
iHCP>hxy&V|JDEe_B+vFUHQ`(+<P8EHkI*WJ(DDv1Q~bZ0^fA<E!Z6(xuQi>G>9wAj>H%yPsG&~4!OF*s%cCwP*4_c4NO-UfX3#l
D}n=kz|zQaBl%|lLMe9InIVRJf+_4T>^Urrs3h^B`{e<F8iU2;z5C1Gke!8@IegZKqexHLTEZqxo>hhLCWu#3Q&`W;U(*eM)gnj)
m#}CZM#IHz6vF-;i2aX-AKeVZAN}DT<_$GLiPAqbhg;Z_h$B!n{@&gm{%bIi*9mCOvcqtHcJB={4$XLbUf+BldRXM)z4lzto1kt5
@TL-5%z8=Pc%W6lLWm+a$&0e-
xv3diV)E;C`V#gK3n7eg$Ldp^x(JC=IT?&JU=hVGm)4jqVQB3+3ab`I*&IrY(!h2hdK)DnWkWX?D{(i+P~j$j$ywK#x9b$i@YDW1
akiSoc0L;d3ypb)nfLCm|G}-
lA&Lk+B|p>ybhOqMR`+;e!2$HERzT(ITfi#gf7v#ecFG#}*tiW9p@HNoIgx)qlMO$^J0QS+t0fAr`ehV>275k0%L{pvauXk8y?vB
KIVMl>Ih&8^e2%$cywIeCu3=09(pna+E4MQ=19NGWUA2XF%f(>7ynne<NBw|juyT4-
AwQz|E<OC=S#{zwYBzNN#R?5wEVhM7RM~B%oOGMAVFzZ0dxMo1R{600qa|vrJ7dOb_qLjf1MaO_F_4A1#iJ!iM}1OBd1Iv-
^P~N%R#6U%=c$;Yw!@Kdce$Q#@((NU(5i-qSr!4`Y3mv%?qiA@MJhP^VJxu-
AW;meF8S@KnuQ9)V-T#c1F)%zg;m-j%E5A)U&rtdJ-Z+mYW-aR4ih0DuYXWmcoRR-mVSk)szt`m7(3>|e5`nNOiY^IcuIn*QZ^So
8lX1naqbY^S!j2E=s*V9Ja2P-%sEyY)aL#)L|5<+U7z}mIQwra$HzHj?rJ!01<R`~oC-
T(LPeLqKL_!s{0f4?g_pH_1j%rfx2f5pHB0S;&S;1>=MLGNOOTal!Gq*BHmNq=9L}v)Z`eoPHG~KC3x@p`HKb;6RFP_XraC%JD)>
`<kx@2OkB-uyEbv(6SP4dF*3e2LAJ#WpDi`M-
14*~a5f=*PV|0fRp;hICwy3S3O6E;(jP9zQ`OUFe7}zWmbU|&Ua+VeVC5b(j8fUOE&g}(tK>(feUQhWCl=@|7j4za775<RP<9k?r
b#2Xn34tTQJXa|+95u9?R2jcx8{%K7fVupx+ywPR*`laxt;o{_c{pjjLpYIArHkY`ErqP5GS}oCM|tH;y~ill&}J@AP2)ePOPLKS
-TyyIbj-^+0dD-
`>=dn0*IgqwKc)IUtvb65V!IecGn<{=Z6j<yL`UeG<Zy!52L2Vi4O<OZLpdGhm7J^dI92>N=h$c?qeQ3I>g01>fP;lONL}QB?m%=
^Spjyf-!R$&0dQBJh(RXvRb0Fe9MD2<N1~n<vF~0`xXCf8E1Xch0f&FAhuSWaJg!8KcX5_(Q=^A$b`Kn;BZ}=4f0L}chm-
86Yvo#Sq+1E{aIs&Ru3?((a?p#@Pfx)sJNp8Q;Mbn6D-Auc5-
#74QBy{VuWtiU>o2JlSB)+@LW>xC_YKBKn3hIJn7)r{Ssc{`^F9WTp@%?8RrKj*xtLzd=?z*H9~%V`>asjAQi52&L&2CL2w_v%C_
eTa+mo6$q-k)E9yDz#Kvbo5waApU2!(H8sm6Urh&5Om*48;ZrN9Gg<wtA$fuY(XTTeH`bGE$&;>19lSP&}-
)sn?%Sy}S)RNXO14q%@y`osiDXIn#lwM4#J^!DqE_uvw!n~%X9%`Gbn*?M1BnJ;BmA>S_XlGP-ZE%7d(e+@I-
ZzUi?OEx$$sWno1zq`iRG0|qpj)vpERX9rJ5vq5&oz|yb@A#arih*wv=)6QPjWLG|E5`YID)UbCl|!A>pvsXl=#;jlNK^MJD&J3R
>`ITE&f8sFvTg?c(?2)mDa^j<C9}l(BeU&DC)f25wp-
o=)AL%XajWV5<i?NZ0fntij+{(u&XMLO$wcWVx+n^g2qS=060SFO$cObL#23@3s$+cd5}VoN6UTSr_F9q@&gjxfo-X7q{U}m3-
9SZz2$%}AJIs`eZ&%QUnC~*)7$`#AkoD*-
7}9#Wi!`zE?oopW7%e5f7K(}hIB2f|`>K)x@C>6IG|L?pxv0s9dd=u_Q+<Hua_1I|YIF*eG(Y2cSI_%mcUSzB)lA}-
kmxMXdnnvY-
=?E8XqeyU2R!o*zgL5QkkH%fmuXvSE~PzBg#pyPfmmSFB+V^A<$Du0r5=fT3oDZ{b@VEN#7(6L5A}FTHH39a9$5~df{_Dqpay)9%
QxG!mPhavt2F+<TqmJPZ}uf=Js$5qHokewne|62hA5c{`FB%QM0JT9OC*fft(i*;EgjU}+3ycjRb7dBSyfSC=7&(IEtD6a2-
CB3aJdu{Y`0LChN={zqwS#~jD@4GE_>HIn&`cmwt<UUYGWE!#ND66Ql30wpBk!99^9vm+w`1*6%oYIJQ;PT5>rdvt!~d$RX)DV&I
E1g$9ss@+E+XfrV7~dD<D9>h1y7?HVOz<;<T;@!!JitiW!5nEuIti$jf(1p|PI#tb7Y$Gb-QX*Rw%idZ5<vJwEy;h)g@!icuUG<4
VX4{yd@IP|Wfv0uc?FHd>FSD<B41_i&kEXdn$?E%D8MBM+R?`3m-I2XXT%mpP!xy2^oLyY&-Pz1HC}=@#C+{iZe#I69irn-l8qk-
(F~7cA@{%sR&F<AYpzG1S0xqOu|WWfx<ZCUF1FcNMg^f9pJjnT0Oc>K^)Ds`~BT2*h_Q*74?8)FZH_6;R)u`$&x>G*I|3Rkk5t#o
CyM15x$Z2EwY#Vl+j?DR3Z_?=BkDC>Qm+K+agEykwEh3^NebOKT1=s;R(E&butkZw<n|=i)$6HT}@Zz41{t(9MGKCojkU0#Hi>1Q
Y-O00;m803iV82KW9Y0000Z0000c0000_aAj^mXJu}5Ole{-
RBvx=b1y=5X>4?9ZZBV7X>MtBUtcb8c}pwG&sB(zPb)1cElQ1#SIEpQ$S*2UNX*O2FG(!P%+D+40sv4;0|XQR000O8001EXUNym;
ehdHrY%Kr)EdT%jPjF>!L1$%dbWCYtFH~=DY;!L{b!lvLX>KoLZ*FvDcywQFVQyh(WpXZXdCgkukJ~m9|L(tnP;j@_#nE~XX>st?
1%mW};F{ecNznr~hN_iln_WrN>9LRVxqti33?CBp*raI^)E|<SI2_K4zZs6`dERTDZlAo2@@U5s_FU#QzpGi1Han5Ctt{C^!SiQ3
p4Y)__8pJvrsUOX_JqC2tAfWhi<`29Q5Nf|mH01bQJyef)gp^(;9ARTo>u`(y2u&7;pIKNk|~R$G-
Y#GN9JL)t$7*Jo4u6R{%XeH_k7Re>xzjji{e_`aJ$N_$P;<X_+89-Qn7kZLtC)}@e-DbOw?=+(pS-
z!zjqSmucb$#P!8iQ;14);K_nTO)WuQfim2)r~tizv!j;Cw~}-
#c`UOG2!LMZ6>$}LElCj6?WAI|sf(tDCw3c^IgMm8;VChwn%xczWZ7rrfD8>;)x02My>7BBDskOYpvwwSqGEed)v~--
<~gZ|<o*OGP7Fz?NlwUSGDit2%L;4)YbM|i_&ZH_$r2Hza>u~2T}2`!iv>{WHP}@u<Ld>x=DZO34o!g4(lnd`i=ogzmQAiqP=Qc2
JjD<LMr<t-sONd!Y_=_B#=>yhU{r-66Imh48Vr=nT3dFe-~C$2T+!F}w7!1-EWg)$f*_V9x9>4zf21&8us0x%4(-
`&mhdeLO>~ATIOjOF0^659d-65vqbv+!zLL#uZ=xAwTCv}rvUner6)V7eG(SLfkiO(-
5OC++{A|Heo)crAou0C%zF8Y0EN)V@cparigbbVqK~SwAI;;9J5pjJ90xeL-
&Bm3BCbBhK(i85}3<jBHL9g*g0S10rvn<&0dhY2Lo^MHDcZo{mRUPFqpX>1j*`npsF8X*qw4R>S@_fXe#j$K)VU!KSf%dlA%HT39
9=)`}wS?31;pl=))DsU^iqQ&0;*QZc#3C#etEKP>-
Rb$bCl1E}c~tIDGBCp&Y1J%v+2Ag%)HJUnrupSj#s~B8<@A(k!{R)jJsu9AbbdGFhzCSioJIf>i0T^Db>OSLFz@UO--ft)W<@D)M
1q@ZG%3VU5nYK?)Ph$O@UxD(o<gut1De_m39sT(6of)+Hn)0viuJ<6+JZn)0%e9Ebt}tj6vLn+4(iZ0ND?rwW%n#i<t?HRrKIjmg
zW_bop~A2fJQ<N_`G!hu;B!h(GA!6YSCSx03gHZDcGH}BC2YY!W77B`IAx>giZ3Qk|_t+BXkTDALXqgD#2io>oB$s?E-
*m+*>hEUi}Ixc#H1R5^x5M4&w(Wc02{AgZB<c2t<&n!_iXkyvcy#5=bDgR~~4r!5;ral`-
4^$??%Zxk)eHW`twM;lOx4AW+`2X$ka#O`EMCk&y%^`0_^ZTgQL@>^Q<<)TTd}W;5h4t4(CIX}%rR2fQ7>Bii(Wb((A6g2WnQhD3
&lI(MWFhJ1Y2<VW|>I4`6P_<=F;ULL%lae%D20ZlSnB9O~Ksgf6I6mx4g01@RC<&IlX?}I5bL2(AzUt<x~WdI}Fs7bLhDx0{b3eT
(vn-~i#a#&)#4OLsovGV-=CdBF{1O%-
^;`Oi<A*}e0mmh4#?;su67+x{hjaOhJP$`oT4Z6T`0(st4ygUVf7nluetX}s~4hi3%GADQgbz%^DtuyAvqJQ`QkckKzKD~*$+i}W
F&aN~{tFm;;G+isO3yM#fLt==aiqsLDP^_{mNElm2Z}t?(AFw%bqkq((Qnnd@O4mRdS4`?uF{D8!@FwN${OOhaKaGGLM|nc08;$(
OnNIRh(uN`zbr{YoC>*F#JqJ^^C0Nw})X)9E(m6|G39-
hR0siHR)zMjzbY8fWZDv)3?Q=`#E0Lq>9!fzJoZs=dsX56F<w$+E>K+yrR0OV=TZ)r@@YJfO4_a#?*M*`o6{b{`T-
&Pe;W{5H)cP*KS-fR+!$UJom64a5S+_to60GfdBc*$&PAzLh&pDn=utx143v`X@4-
XZ7k0X@oS+xsQnXj0h4QHWrdW{l_B3J;0#M!+<m=mI4<ps>%bw+Zhs%}824)tr?_Vb<%b#e|BrP6Zg&m1ngkj9f{kTh9Q4KZoBZ}
I2JYuFxd%7za&EsZM`tOHkcFtn;nPLj?X*WeSAY|}*>4Cb|VotWd=Mp+T&bsr~YiYm-`REDw)O&?_v%JJv;>1(z$eIn!cuh%Zg-
`Fzv$0)aHquDqoli8;s{c-pTWWYv5RK-H9zl+kU=TLug&*`$+-E@!O=rmH4Hry>sO)aB+?XaLUrXsq<mVS}4fDGo3P19`%d~(NC-
4>dayTIiXk-
Z&)3Z*G_{lH5iR);8EpxFIBhfqkH1j_9Ds^%GsYTRjEHfly_c&ypwz!PG4dWRh=5LikqcuaT2Zld9#8gWODUW$!_K)_}0VJU_9Y^
$jr9&P%%zf!3X6-
qgt0LjXa*;$)dO^r3{34)@!TKnv)H8B|WDc%Ez@HdV{_<I)~5skJD782)BZ}XhmT&7RgJ@inR>agfn4Gv4)3bs|wh}Pq?N46sV-n
AX^H;B-eCJwu8&lPJ5rrWc)ao8_t`d@5-
I6SH%g&IX9cMzGb_?J&`+NPHW!?wG+ZbR;DW%=|XNvIP}cjBKS2pB+lDgdUkF%wRC{^R)$?Be3m&?*L;+OFofS+?G#=~}&RPl`rA
iqFmJZGLdqJB}3fZixbFObeBYT%p-
!6uhV^df4gsLx^e{q6Am~QcZrH%iDaUcZk2%91m1<qcg$gYC%(zjSFQK5qZN$2_CW6du+R78BiAWcu1%*befj!a&`8_asv?R1wnw
gtdP=llc7X_ak9Emag?#+fIxk@nQy%(?0~ujaa0JX1Hj^Q{|IL<Eyr=hB)=oRI&pQNK7Yrv{&BFEFx<w^p`bks1;0uG1$kE!w9aN
I;{fqqP!9wW(`^KY*W4~`vb)a1<`h_p-M(h@z0C|2C15?Ab~0Y>_^IjM2-n*9>1rI^x>SZD5IN-
68uRo)MKQLWXgQ2$6P&BQ$&Wqta(?@vr-Dyc&s#?)wm?@^xlVdcEKKkyc@_!mDgWMcLBGTg0T^IvYp73K>UP`0E?B&)R@I&42Wr*
jSglIuo(F41RU0l8!eUb!oBg~s<O4_0Ud89G8<MWDW><vEl_~;|DT$8f7=oxSmD`!1?xZ~^FWqV*y1_AhGGDsUPl`byqA~~Z83J?
<{cX()Tk}0L!6@#IX97}EfAbkx$_~>fgW(~6OzX#Mcl9UiY`Gkr<t#W11oN{Bk5XWV1@QY|MLpV2^}3gq*e^l0r!N6D1$Mj-
T~UwfJMd<FA;;~Y<k{zHH|T}?4TP>dQ^3}`#eQ)_jBa0lL^S)Ds5JOG<wh@kW$8mxrz5*yXFXKXGc+pU({Q|iNa=6qN9<n+3Ql6h
J1z;ogJZDnNV{b(9W>6|hSpv{QHCR5xmIkyGs4<m(O<)TYIATQi#aeEZb8H0b4I0Jvl}4#)t@G&-l6<K>8N-
>A}&i=!t>VqNmb`MAfd!me;mEzVr2PQZ{@ZdE%We-
1LkwO1JN$7y3>eNbVX&nEj?^s(|qbyyOivI$OZm&oAg?Hd^sXmdqJxwmwjsGv#&<w>?~L{Y2BML=)v2Ohx_J>R$HexZyUjvgGTzM
lf$~Wf~WK0O`490l;CaLs77B?b9)=EclnJG=vw*@Y<2(fHuod;jsE7f1xH>*@pXGSj?UlCeEgESTruDsu(L0(^}Pt>`Q_7VmHI5_
eN@>VFv#WxI!PSjmm9n(;yEDR?+LpG2ZHJT@DTZWQXm=)XdGd--l64xJUw*TAC1Cu%MuEczu<|_y@u$!`Jbl)snJ!#&h{7nXVakM
QM?C^2b82E+iAby4jTH$hjkowK^~#MRX8a=G2YvREJl$(2q`vi=%$X?3ZD2qPCw&iNid)>9z@=92~&Ri@+tmLQRhDtBWl7&vFvYM
(^^~Z;Q(!|(^Pbk$$Uy~cT>Azd^g~`a=23BJyA+`)o!%&u=U>NZ}ZFN7w2!j{r4O8^RrjyFV4Sbe`T+}eSY!s<+tbGJbUxv;(RmK
X~1^K^UkFjNK&n`$Eg{w+<UGo_8c$hp160tPSi(omGjo`zLeA0OI(YQPxD(3@Wt?Y=pqg;dsndVLQ%<Yx|fmV4KKH;yzPCiAMFz;
P-l<3ZWxpX2Ki?{{_xZHFV4YDlQ-
@B*_(@tAAmxU&i)TjO9KQH000080000X01FaGmm~rJ05${w03rYY08embZb4^dZgfm(VlPy0Z)|ffLUn0ubZKrcWNBt*E^v8OQ^A
g#Fc7`-6(gUBMEL-uRH~|WRVnI5>b5;(BjkkvybCt9hi0QF|K72k0QCWE{N~M@H$!910A<-
sG+8W5P{U{}fz;ZNBxSTqlE!25yfPN=_n%tSwC|@@=?tEX>ErXW(S+}Gk2o3o=0;h~VS{|bvQ|x#fkkKfzgUivx+F=YJL?K+Y@n0
6?lG<Cy;yT*AZ_aks8vN9`0x=N*&+d66-
Tt_U<(|RJC==ki<FAnh1h_xaJdGsY64FL_}pR>S^O$9&~iX#TB}Qaz#)Q<n;FbZ0nA2$(svaLnO{~ahww}G6MnJQ*t8Ma%z`blr8
U;j7+b)_vt7lKV5uuy755JZe>z^10Q6>h$YBnfJx)C?14TF-gz0N>ydN~4xDuZh7R;)M+@D<<r5wZ4A`gfL@vNV<$X|`psm~EO!i
J-x7WTz&g6XSj1vh!W`}y$gJF8udPa5dGjIHo-
B8zpQtE?LR1a8y0Hu0k~C!h{t(yCExUC3=%hw9m?n5%}Da{ytj{3zFOvRn}mPm=?&u(4+9lyAhJ2_5C|TTy2wjsf583>>F(Ap3r1
4tes(v58VgX<0p?b=%9rP3I9s0m8hzVnw&A!p&&Sh?W$4!d?GwUgD7P*EyW0T<KP1AXbj}i=7&{IA3M3fD9OoL0&GdOSaWk$eR7&
aM|zI628jbVT9e#@fWn)_|B3|k~}>=?znNWgULToO9KQH000080000X0C+&r`y&JZ0Nx4!03rYY08embZb4^dZgfm(VlPy0Z)|ff
LUn0ubZKrcWn^h|E^v9hR!xuFHW0n*S4`E51TY42HQ)k^ViN?|Y!<<`mmm;mX=F1?kt#{;S~dLNJ0xX`+8EtKf%;&Z)Xd|2ym?e>
bO%+{4sI}5RUo=v8wXq|?YI+K*({s(eps!tto077RlUdh$)3&cZtg!;4>w<LJ~QBbFUQKD9i(IMj7GHM#Y-
DJ``qkMxd%DygktchwT$1tYvu6Z&K@t?JlUSt7dL~vsk{ZFzl7IR^`5I8`lZ$K8LOVVJ%bk`90tQI%eWm?4Gp$HwvEK1c87I(9EE
Lmb`6cFT?y}g1MAE>1NuZX#XE$};)ud~taj*%+%Izmd0v*mN6V%n0HJo4oMyXZKaZ9QU#?mv`;(<;fm#B>3S}KvH5LgP11T&8uFY
$s1ZXmfY59-g!Xo_1<$$-wXtM~AD9|jz>jvv!ixi~cV-
l4_m4;HnFPpHJ`2M#u_xu^b?GdbR0zvPn+GTdGbZE=OiDK?njL&b90hxtmO9c|D!2^S0i?kxz@YbOzX&X=t9UAVi_*?YL@}|io*(
@;V95R`3OBNOp{9-
>fF`CRUR}0gomHBoIVV}NJZvngBjrojP>p}S}eX^^tI0um)9IdE1@839h@ibKJdL*Ga9e4E}@W5*)N6<t$MpYiDkH>J}DPO?N5lx
*5F&pe9jrg)94Bk&o{uS=E+tcAbc|X?<6%0zErCN}{j4%Ooq$psAx<+iU32gGbiCRRHY%SWb6Vz)O?@?;*Np#HhQ%<5_28tk#^g1
w!Rug_hJFn?}3NWeY6;bmNeUKzjdC4X;@@64#+L?}zWtk-
_;qhb|3>JdtHSA}|$&S=q1;Ji5L)Y74I)@R*trvQ3YauotxU@u)EPJ^7<Kw4$DncU4kp~`slVc-
X&ca56wl<>oSHoteN`6Zgz@Zfq{V0WUt<QY{<U|rbtFdbEBHTVSg68VHHxni2Zl3qRwiVolJ|_@?eY&m(vtZvU#rZnZg0zLM9^WQ
G%%BLVkTkNMB1pmbzfzvL6LnNA!5(KO5e?}=as2Qu5Q!YNBlspylTDF7`xuLUbbC$Lo9_fm!A9QEedly1%Mb&H*i_1!lHZb`Jw>L
*f?7KH2i6XoRRk&7#9l)+qG7R{;|%V`9*L>B-
g=*@Z{bOAbdSafwDkPAn9MWdk3Wt71us@U!Mj)_r0|9xe9#^b3WJhfBfNm?kk6Ln&)@03JdH5E(tJyo>fo?ky@Eb1my7H3Ujq$S)
U`NizPjN1I;YdyN!@yuL2LLf@`(~^iJWf*o!;dCf6(a!usBdN@#9qr+@>!qZ{-
uTY@NRGWmil|G5;Eb35xmc@_v*ykS$B|J@MrYi3ugZ<wMHXpjOdrIw`))nN9p<8A;jWmoImuV^Pque*jQR0|XQR000O8001EXKWC
9n0|o#9ju8L=EdT%jPjF>!L1$%dbWCYtFH~=DY;!L{b!lvLX>KoPWprP1WpHeHUu|V%X<;sKd97IAZ`?Kve!ss$(38Dg-
837z;;<{Q{u+ulZGmNbNdi}~<%=4hWJq$7Taf>Kq-5FB-
Q~Ig%R^$z<VW%&MNy%Yo+{N6d&MlN)vat5s|{hYCM#|Y5wcN)U8>%aHLnGO1(4-L^R5-Veqt4@8^cz-pp?#LjaF+?mQ8Pa&C8OAb
*HoiJgF?RLP;~54QtATC(GAeBU<jY?WPlQ6*Pa7n*p^bDy8|jzT(n;Y5SFsbAloG-
>;Rl{LTiATcxi}$Es0HbEDcDUUtl0&1N%ZHnJi$Z^#vd-
14llcZ(QkPMBVq1*t`4&y3Y`bm$@{PhJvuTg(Xj@EdT2ED7iq?%AzYz|Ximyoe@wGXz*6pOoZ;w}vC*%vzl}kU61Vj?SG(?obh7)
OMPfD(}It;+?`D%><zS#oC^~)mrI{N<~h2%U7DM1CG)`9Wx6Um5-
d}GY4dW0B*~*S(T!OaFCAzRx&yy9+qjoB?@xr$}IStf<%E&&Q@4~F+46fY;@7l<`?jFhp9m}rYg{dxI5H5N)L)JNXLvJkv-
i@<cE2*iJ<`HLuR*3*n!u=#p@X|8LG{RsLfJHn<Z@IiMI%}-&qbjN|J`2cuaDipgcH68`aCYpfO-z3dDdXw}%5usevSU@O%7-
rFlTq2My0IV(bf>5O?N7O98;AN6Pj4CHq*RrfJwNj=`G{_E_<;OIOT9H0?w}50Q14f!!^zXQTS$(of1Y)=lWCV?qN6COL#R0Y0AC
Lse5?)j-
?;I`npcWz`iQ4MNxNdRu}<vN5rD(y<*)LX%mPDAnb+IVnLi?z!0{p42@w)A&=tWo>Q+$Y=B^ghkKKY3?!?pbKHjTIg&mG2`d;HGb
`whD4j?sqXol@H=5_sjl5?p6G?6udKPjHiZ5Jto*=M80~pW|G(MPB%YKQHi#-
ypk(n)37Lfx6cdEcjv1g$bzCw$DNA1<lXXyEvujw?CJU&Ky1MOVQ1E49*bT2;cDH-rsOPLF6^q_36Wly5@(2@>jw>Nv=c36bf!%V
a?--!h1csAfVW@C77K{VS9`}P4c4=I>MrNEax?LLaH;-g-P=b~HvXZT1*-
K_PE+xVt@Cp1^^6cpN=P58;ETK36siF6y+yi+<hbq~lPJZ}zDCDV^E1oqE<im&<*WKfqS!5|+6vqH@@@imqEnMuOVeM^PwW|7cH0
59~1GN&SK<wDGm)8<<7^aa{NNxc0Y;+A;8)h~n8q#k1s)7_ZecNsdIv*vcF8Kb<V!IP2a_=BOf@uP=F^j3lADBP4{Xu3*<{lg*3S
|ZgA4nD_@N#3h$x|=ipS;B>7`2d#fO)a6P?qGU<6oY?h+2f+q%8{DD8WV$)f^D3fn6>uRl~5oq`hsPyns;)j)Nvu#~*jnx?#2{G-
q{|b}^Tff^}e{&UTdP>p{EI{6_HG#ku_Y_3OE$JCZ*JLuZTQqobpXJpvg$mqk%fWTAzS28EowB&g!&XiD=vs?^y{twyc=uHu~~Z`
~ibr);-*V?6tz#eo05^}67pI%i)#{`vd+Pry-hHSug<^(>R2!X4J`8+5)(3ukgUaYx^TzJ=pG*wg|>7Iz!dYj=-
IE@k21#*VjjJDcLA;}{jDiws(;>3Ag?5GK<&pBDtn+c+$&HP=anxpv+}h@Ol{&es-
J=A4XWJa=l!#mL~Q2{T)$g<)3BJr{6n0#lZ2v%H^-
xK6Nuv+VL4uWYnaXs4m9wH4gJ_xmJaen{C~P4HkZLg`0%qePSw6#N`K$5Tp3PyZM$o=<QTf@?}|kSN?`j*)O-
wyGd+c*FV@F4UMIj(1U}H-
p5eU2Hk?kiNzju7i<*NxtIxzl63PJEPl!Oh~+g<IM*v7N6}fC8n`dy~a_;i+#`ka7#Pn{MqFFn4*jC2lCq8@@jX58d<_Y8*1c6z^
PD>5bGT8`#S-
kZwLI39x1D9;i1071^A9Z@9|=TwEv%iUi!a&%|b(mjk|n)G@n7&IQ{(jBeV?PJ7)g?P)h>@6aWAK2mk;8Apljo)>8Wf002V|001u
l002*LWo|)dWo~p#X<{!_Z*OdKFG6)`Y;<XEFK1<RUvgz|Y<XX8Wpi_3XJsyMd7W2VZ`(E$e)q2+2n3NZMJup310Gf+T~{D&gCq+
ubcMi5l*3jc1&VIt8vgG)=a9PDRuD`NmUS*4&*dX^#5un=ref|<IHq*l$lSH?B$<^>rDSp8469|^inRniY3^ku*H+Xl2d9*CzF3s
j)GW)&joVn6WlYtLv5pC?jT258-3A-
CZIoVj`qz3J<Y}54D|`7`YIjp@)=DP~<MY3lMmzcB7K?>ww>oEqEZL*bMJ1!$JuSyJ2@`hRE?J>+_o;O@!L>fe?BaI@Ps;^^OMZt
{*ouK~O8-fkL)N`GJg9Q=)G|nmeK1-wS+$a_B_!!=L?8*{-
i{|^5)&#S^xotNafb+k#0Q0!6$(%vM75D`tTi^`+Kj61ag6QUu`7U)`^<T~ARz4D7ScfIMHj>WT5xU|^sL)8tZ`U?K$xxqeXLy=k
D?`e@CIw}&M4Zf^NUBJg*3zup&Txk9+^jRpP#or&QAg_HH&%yUi^az_8q@Vvw@~W`NmqzxTn4EH`yY2VMhqvd&Md5VM8E=a1ug}r
b(nIPJw-;Q?-ov**_O&^~G7i&i-
1Sy<eW)g_4F;x|)(NR0+K&lp+cv{rE<I)8>cvad>4bbs=r0MU9bgJ{GEC)Upn~*Ui(mCp}Vkz#3_WiaWbqPO80WrS043F{zVqS8f
~iaPh<o)+fi4YjoE%*Df*igS-H}nh-HM^2e*>J9J1(Wn1T=!1nxn&%C@6Q!&RzswRq0qKzmX!WeM*X&34wU`7Y=<Bi;sq0jL##Ia
;Vp<^hj#&IPNtNF_c3d5p5d<{DPeLOH;KIO7;><!)EoS$M&JA>IB^ck}rT%Iw<vJd(DZC1-diA?Fzfc2-(9bpfd-
8>p+j&mNoQ_(cAPQ-7>GM)qat_t}wpa-&i9w-
AspJ>Giv|Bos$cd5DJg`yu%P=3%lJ)299H7_~>SZavCd*l%!sMHJ^imwKKm+XyCuFc1D-ZWIh-g1mG8>bb2-
2@IM5<0WqcDR>WV)#a8mgbiJ}3n9SMf7NDEU<gfJM75^nJp1xFFsUWY4~AoowUzTD4B)-
=sY*RZ#Th3eUY>RBjY^&|()WtUKq=$9@;kqaE189>>rS(Z6GYc0TIHRMpFN85+*Q;CLbO6FfPAbQx@C!PYO_uh%B0DYZLUaKM?oz
z=~>3^<1-G$f758D7u*i-R63rDco9SHD!rZzn^^yQ?MJ`F^Wn&y$hiB@XSRKUn-6Cv!M8&*5+2_jx?^y@GK99C50cD(>jW1=Z*@-
m{37>5pTehxeI1b^V0qOa>#{XsQ_6K$#EhyB$qeI8=_(K7iT}{T^C5i~Al;018Wyel<!*gHzl=O?>!0bZ&V{L$rWp>F&2hB<sd)z
2sLP4>P*j#={s+qbL7YbH6+xf^u<l{rB5<AE5W6uN}`gEcxohSnNw)$TkNCAzxPmL-|{YGkR%kO;n~Kjl!aV9X}XK`g-
elMPGa<=*HdL)HON{hbM=zYdrNvK;!Pya7$w_!w*JPs=R~6H+#x%Dd{%6&?&5BjEk&GLbdQ5Zj(OTFipok*G9kxh;-
7ntKHyENB5F(^X03=qhioB)-=*OC0o$%_9Klb3WaqM)y>%EPXTT8X2IHjP}-Hhdl?SwX5&`By-
F6)y8DkGuc2?gfs6kDP)h>@6aWAK2mk;8Apo-}!dk-
u007<x001Wd002*LWo|)dWo~p#X<{!_Z*OdKFG6)`Y;<XEFKA_Ka9?z9Z)`4bd8Jj`YTPgoefL)kda}Xw2N+x^ftEr@0!^QmWl?N
-SBWjTlH4SO{rApDzV4+j@x!h>b7nMijz+GHZeh2pd)FJW+ktF5Z5(i=wBt@{Wus`YJzK4!sHT7{E42|L_}gA6_t5lvsZw~<x(UB
GS~>CNqA23_U6oLY8V+1ljfhM4mM<|WaI?2LRI+pleEAC2nLGk~9D*zqfDu_(YXh6D_bJ{AbRjmT@N6$!%*e<RLNS(P=#yQXL>@0
|z^;5)NKTIt*tzn}WmVsHHlAGce5~H+Vfuw(@unB)xzCq~?#-
FYCkxf(Af0G4TBpD&VM{EMxE?(V)A3@W8rvfzNEH}5Lv7c^9oMfyS(2OEQp(~xZ|tI%fh<ak<SJArj{RO|n-
ZZ@Cr}ig*(8NKtwb_1?(<0Njh|-yq}0hNjL`=DHS5)j(yyVw96qR`BfAj6|8m*zr-szn%uSs2_-
P(HqdQ@o6m*IyW!7<nTRCBd6FVcqx%~*58}X-
?MpSgd5q2?j#Du`jHn5Jv(6=~}wBwMB`g#%XDcDYw)ZDyjM*Z42nZ@y#Vt}H=Rx0bbDn(4DbeK|s-
Hz#3yKZo!Ep5G`in;fW$fgvbcyCD7gw7r1R4-LJT26rLv6-
_j?J3;>bKEf+h`oCDPD;Kq>Ejf8N&FQ5uQZQZm`=d9JcyQ$xLM#6*u*X(r}d(>d3o(j;(3f7Zh!yyd5798uIzZaOAB@oO}C>$hLK
s6UCb=8UkCjP?jRr(k6(*wDry;nmvs$1bOvmWzu`>-uhJcK?-r-
kX=tQH3wo#d3}cvu=t0bxrD9fWJYY;eJ&V#UhJHC=`KiW(mKScEF&}+H)c(>XvKE@r2h9_i!F?;;s-
K~YtGCHw$#_*s%E_CDW#J1g2Xy$Fnj-wC5lZ}ce}9Ym2BD*WP)h>@6aWAK2mk;8ApogT_wI!T001cw001%o002*LWo|)dWo~p#X<
{!_Z*OdKFG6)`Y;<XEFK~HuXm4&`bY*O1XL4a}UuAe@V=i!ctyf=j+cpe;*QemPhe(^Fu6^{T-
sQS<*K4oIt=anE<YYynZMG7rkyILAF5i6sL0MFjc3W?Huq6TnK;VZz<eXn<-7>eU95aKm?0oNbT0OZCt-
u#n>qaoCtb{+e6Rg?_<&G>vhOMbOU{Frnx}0;KBpahUR+gK=4MvnDlU=WkW0g|cRZePUlVn`8ZhGCTTI%uhgVkz$H)4E4C7(>ylM
c7<g&oDe02?o0VUjKN&bdC=ljpTIVq`wS1Dv<RR;mTV!_)5zI!2Ntjo7dfHKlm=C9}?C?D#ozL*I(ksB3}iSIdOK14n<MyI!_}4O
STMvjuaeQns%QsB8Dk4n3-uYRjDNk6UpgTDD$SpDO9r>pby-eiz_32*P^pb(i}3gQ(qtb-Ec^QL3sF88EX~8y^egfl##IO0cGKq6
1w_TJX0QCvJNqtOd6(m~@uiRP7*;URON^sDZ#b4cf{Q_=eV%<$BFhZP>M_bq5XxEnX73qlc4i232DiL96k$lFTe0{owz<XBTD<)}
c%MfrG6O=wr~nkp^OqjLz)IgY+Q;D-ahsc+Cp$f-
D@Q7QJKd_R3Yar^aaWVB1@*1UXR&(b&>s3f4Utlp>wM$ttx^4|}BrWV=e$B2_+SDQZ8#m@K>@Cn)7*IP|Y#6R&C$eZ7}%mt_aR8_
=XEb3D(ds{NRvDa4YIrE&vIE;e{N7SNDCzt+tjjBa9E4}{h6(<?IK6hfU%yYZoD7n7L0*L|AhetpI{abT2Hlg_C4&^fK#s)sZ$p)
y<HY_USdw*b>rHU*zx#TTr0w*^w)IY`Dd%dQrWO7hkf{`Vn6mVEgOWpCtd*-5ZdZOc~IRB<A|;}dX8=p<h*82_dBb+2@xtd-
(c)X%|ejxRhLUy=au_mB{jJp{BdF@9!MYc=aDSMPkz#c4u8R}Ew-
<X&+oX*sQVz~_(~MnarGBeL^smVgD@aMI|@R0)WvKRzqVG+SP(yHWQ2rQ*pL*;!5nIV5y6ItIz=r>ha0Bl%Gb&WK;c;fTQ*_oFzR
b3BH_uVL{2!QU6LH=!r{j|NjkPf7AW8}~+64cPXWzJG)7Z^kwr2C$t>(Aq(~K?E4KjQb-
**=+5SHL`ZTD*{?6+`hmU_?;q44)I7iE}|lyWqH7LT={&1oiekMR<J+ORldg4b}Zha>)k$N0yIu&as|39_wS=XB7{=^HK|HZ(@WT
-phsa}q(ky-
O!IRiHjs7Lz_7Dlqs^_vEi{F|I`!r!AB9oS(e+JWmkL^+V6cO{L%YcA@Buc*U)H<C_bJhW$=<X;B^fZJl@bfbgflN7tdH`>&(8%y
L@Ed2@q!^Jff3?^JY#3V-
_92eY=gmYjAjYIC9(ym`&vXSWGHeFAr0>9jl^QKWUaJrh2s)zSzQs)m#;8~l%6yF!Dk78YaDy5=>7Nw+c*?Lgxfr}LBp7Rz@LB6Q
l$t&8ccjA4s%ba!Zr)`33VflRyZ^fph3^wK{lt8^JQ?sR1vs8Fc8R*(T?EI<ru1n)(KedqPoJ#S+Ghk5yc-
12y_2L3}IjfmhcwSX!b=Ky+t&ftbu@k(W*hyOl(@|M@^_qOE89thX73wUl@WpG2SPKw2$XhM9wrlPlFDTicoW=5aQ>2*p0#xcWtb
dAUmQ`iHYiHC=h`4Z<ik+J@Ksg)MfeAh;2Q%en5T>t(HI+z<4NdL1dJMv+0f`%ty8$^+yt$JY3#zlDcGf^zxm#=W*!|tN?m`_L{*
|8&)!`?&oj*`0dqOFgm&eQ7OT27yPk45u)7)TSNKAhEq({ho1t+;6%7Jes)=u(Jj%^JtSu*H<fIwYq%<HTYU|~5<u+poMY)&Y^Q6
eCqS#Bf}Pfb!Hd<z;McL0JxIp|mb1f#QL?|N5hSw3SkVq#^gS0xNqES(LwZp<K>%`Sl;h2gU<4ir_dY06>;l?CB+p;l;wxGJP>9$
9gLriI`Us^^bWzCZZPmd&lv-yj?vl?6Hl6?~wzY6!PeUsi{c*IDN7*IMX?I2uhWQXc;DoV7R0Q#!ja7g=#b-
rI!yxITut2|?!I;`UtRA*w?^j!#1R@|IAqEZ%(}M7n^ZQBD{j5~|HAuL)!qydOxr$3)(?}Ftwdb*MF9Bttx&>J@+?ay?Y0b$_fai
;+&wg4YkmVO=XKx@?C})zt0Z>Z=1QY-O00;m803iU(a08?J0RR9r1ONah0000_aAj^mXJu}5Ole{-
RBvx=b1y=5X>4?9ZZC3WVPs!sX>4UKaCwbW!D`z;5WVXwhCNB32y!*3PznhJ)0mQ;(jeB-NZxe4tIm#6o6>*p?8<Ru_fmmvY2KTs
nSIYa`8_mEKk-D^G+_3lCkE}DXU)dDkY#=3R8{K<-
|&wEI^Ni6Fs_70@9q5k$vegazjgfb^dpSAJ+~3+u8E9NZiBb4*o>NYS(fQ=bS-q)!%n--V&1fTSS>|M&@_Y<bf)D3ZazR@T4f+tl
qkXJJwkn<o5zl7K+aWsR3#`?6sgA=hau5V6XowJMHNPCI8pK<OZ>oE=C5I|54mx?P)<k_$*KTPa9fn}NloZFX}P3JZ9%r^^7Nk5S
cKw(1NGgh>cyKA_%y%$25w;$MW1D;Y_tA$|M`pPFTBW;NZg@TX|vu~RAs7m7+Nx8^t4uA1q2OoafqA}d_uIfN2!x`1A_18W2#OHq
b5;iq)`7(g?K4Gj;L0k{PqP~K2Z}gk{^-SU=aMhW5%K%*VPL>vDdg^p?791Hi^VLnLlL!azZPieMMjoyhGS}h8RK-lH5={alMs%O
e`i}N&mTgT>2_=p2re5aX^Y$`ezOboK8#vaI@6`yGmWFp6&lX&9y#D8rRw>$Z{8=i(7I0=VS;wX?&Uw_<4cqt~0a6o24&z+6J6yC
$0GpNcH?%W)il?hljN!ZH`>_7f?$B1QY-O00;m803iUwq$6$l1pok_4*&op0000_aAj^mXJu}5Ole{-
RBvx=b1y=5X>4?9ZZC3WV_|G;E^v8`S8Z?GHW2>qU%?RwA_20R?9<@Q8-
l`Zvn6rRxI+uiFc^up*+`^H(n&nS`|Z0UC5uX0C;H$Q^6ufiJa;@%N-vaL_AS>XDS4^%h8WItwi=K-
zIjkOe`DE_Xr8g6AnKlLVyx0UCsJ8%Qc7vBx6rC2^Z8<J*P74gM3j}%mM{r2%nBt<uUD^qHA*(WmGPQ6v)qc3H+s$ggy84DN^&n(
F}o_nZ6kIKfBlBtR6;JB^~sm((fsX)(c8byuin?jrD+C6Hxg${F70)(UJ99ziBg6Ce5<78j}~lQbU_9^0#C&Z_;ES99Dn>WzdoCM
AVX(Eq)dvYrTnpCGG806Bl_Q)R8?FuJn4-
OY>K`YG>&_hXP@VztI5an(G6gno}9Rq$>{S0jy(H_i$9;hYOj~`1t}EE=K!MxH&IObzmq~3JIzIAXWlZf7a~mp(^6sP3sLYW_7eD
L4(X9(I&&*E;2;2lW9!X@(y%TeV6ua%IhcYminz>F4nZH%wO#aop>b-eLReHX;h_#?=)O_|Cst9s->c2Wy;cFA3=$#an(r5_-
gG5|<t4ykL{p59i4diQ=8qY#Ecu%iYd+Fi=@$+FQ-l%HSSB+bA$meECUIA<4qD18$ZhWA{F!xZ>-
{=$^F?VR3n2!_UEbi^<8}P0bsN^FNLXPM<e+4zA7kJaxE0Z(Fa4vkf0UD>4}+si>JLBQY>jQvBxW`;BWTzPXbRkzXZCRrGCv_qFT
q~tdB@;yYYv@Zhzk+Qq)Toi>Q-q&D3H3zE~MiD3cy<it-
~OzP|ZFQaWu2Yu>ccQXiQ*dI*TzcU0u)5LX^S+u#h%Tb*o<Y^d#;Gmh3S)O-LzZ<dzZ=)F4!3SVk=%v^;==V7YZ4gXSOF8N`_h!-
EV&w9@Kc<lJi|PCP-&pgj=49a_ESv_80|4c1Ag)<dhBdVQK&dg;5iFoc(t-
K69S8#8#pn@;^8?26bG2Nmc<x6r~Z<UFN^yl&5_uK}0GJD0LMOquh`7k%XNbT<oBD*OG$f)7HVHyea`=9Z%kaIq$v6Rep5s}0#gl
7+>&nLnZ2GpdDv0o7*R_OfW*ZW0b*i8?~gQ-pNpHgTbZre78CtTiWYqt>8yfSxoNe4aI^+A8N=W03(TJpOM(_a`{=m5`XJrkgqKp
oQ*9i9(*Ig$X)!D^UNM_FZiaW*t_i2Cm!)93K{}yv-Tm1E1MC38v0z0`!FO!tmh)O5;`BU(hSnOf8Ky&@;0Yi5xwLTle*o-
uVI?Zt-&$H`F&P^&kWL2hRSc#YpGdbV1*#HAH+{aGz9=jCYMr;y`fvaQhB1-VJDbkM61N_F5laCVAcRri1QuFzaMs&-
fn@yFHIB=M~d<=7N&x_BbKOo~gc6o|K5E(QZaD3Bf_g0Why~!S64`1?`iqyY{+n9b1FP{c#+}@ow8#vKx>s`n#i@OO*a2>k@L<&?
9@-
7oXmrUxDSp<mQV}vXT#}A5UrGmU3<~2prCx!?t4SjT>uSA9PdMv4L*;Wb}>xycu6z_|dlMp3IWg+aJ$$aY{xE@O`>h46adYNOXQP
c2g`&7G(t-51{;w>w+3#uLOiMn6dpevu{7;+SrEF88f^OQwo<xSaHvv!C}f>-ryGC549gJ-vs0n=Cp-
s?kCuFUEHaZ3VuMK!NGlLd!0C`=VJ}YfN(;c1!iq3P6vdl+pj#cb&A{$+>jO57I0vH+i6SnWbt&l1BlfjmjU2jA|L<?-
c&5(eZ$c{3qfc?`zyBeAigOXI~@jBV;6PT{p;)Npm9uVw)viII5Iljr+(~Sc4RDzw$H8DJ$4=UR<^(dK?>2X*L#5#bI^%f;09;%6
(K%fN_@S7Hx5j{yPyv9=CEackUMA_On!XH^($<<WRLrx0iWw86P@<qy(?~`mEdH|)`f-
H@qm57Pv|<|)&j~3PMOYvb(ZJCgI<Ref5)J8da)YC&*6ILzmp!cy2*Haf$x>B;r0FpP)h>@6aWAK2mk;8AppqnJxIy~0006D001T
c002*LWo|)dWo~p#X<{!_Z*OdKFG6)`Y;<XEFLGsVWo=?*axQRrg;r5-
+cpq>*RMEmFA}C`X!jDhaDkx6+5t@ywCT_x3mir|*=%G|BdIuUkpI4ql<Y`pkm<n^$>Yc4ci-Jv2=USA<$-6rrZumP-
O|P?&oh#3%eo??nY8gtekDC!U0E(=(_CFqDK*s!7LCO2LI{y0wKZ#6Eb7j8mKO_B>(*FLQUgJHWwc9@VeY##y0@>e-
>Wt6tasy_!tW0_FaQ@tY3$zYXvx~2HQiF_oX(AD`rmg(d%p9-
j^5kdmXo7zi}T}e=ZkkAjy`|M>E!t2^z+|~v!nA5IW<OB3qV@M@G_bnz5haUI@}HVZJ7D}b&@2~ZFNZ%*R+zlYB*h#{%$t*Atz~<
Zbp?VeMSdw$$2|V2+uEc3R-
J0M~%`Td+@WhN_$7LXWZz>ez1tU0wzuuB#Q4w=@f8jIH6dwPeoW285v7LWQA)R<<l&S8&w?u<Np5q@K~uF(_gab_}E%wdjwLBc-
{J~*l%rEr(r3hw@(;+0c^h#o?68F0NNV^qV<x}`#tOfaPOzU57`@XD};<SDKGY5S<(|B1Fem6{sJ6af|HBOxKQKvR&GdX8W98Qo|
ucvM~^Z4luPV<B(7-8hHaW%%qG#l+yj7_fPvV@cOV$YM%N~n4>LudOewyz{S9z@c<m1Wc3c}Yh~=>)(|tUo-agVhxd4xpkOvw3d>
xw4qYifCJy4*I!wq&R5cwWOn32;urfpGm>()&}d@sz6fckBRycJH~a)sd^vT<Q-
Sz;e1u(BTNiEJ=iZHey?M<*Wg2_9<~N{Do&Qu7|>sS1LlTd;KhNCt3b`}$F6vq^U)r09H^70Mahb1i+GcP*E5;kY!qf<p2UPGE2r
i5kxaA<bgY`q_v0JE|f@D=pkA);E>1X+LoDo|Jgcg}I5tY$yXqD51?zTN~pbA*4U5s%%K}CS*QsOxIMjL}roSn8=+&oV=M9hiCvn
i=9lyZYj42=OFw+uHzMlx|~8Le&N&)ehl|U`PIbGK)|W6*T^IZ7gtk}*Q>%Y-
=qhxa(bOjmiCSXr(hSNp1z7gycYjxL5$#1_)1<lSVGXOOH(PmoQuxa2Zuj<0`%Ct(s<^tW3fiD<j=?|gIzd$5Y-
DZe_rClaL5`=gt|720`{wi=T1!q9VcfWzrO$T6Zjdmv;IhpOqnBd(3P**ie7OQyV9yQw9@&g2z-
Gvbo%MIFPcNY?knx2wWqb|b{(6pw?o^>3VJND;$3W*9_nhgB<o=5S4^G5hg@3bDnN(p!>WLS<7rNA9c_Y)M^Is3Yt45q{cqm1sze
LOVa1jsrsaljrS>ri(Dp2t3<9mVR4)8m7=xicAyIF^Qe25CgG`2hT)lx4ghWR4aDX0qOk+@adxRmmk&$2(TikqHHMT8>+GMVSr(%
@xaK2^h`@r5$WWB2q)7c3gN;1?c@}Dh6VT55V&R2a=%&BVwyHDF8l`Cm+mnqbflDVr-FL)%amD}eWLei|`-
lxt#{IB=;1Bp&jN+j_OZ#TwP2mv}#F@(4^QOX5<jaNH-;TEG$2>;(s*_dJ%J=d3`RasRkoG+WRafn8ZV!-
PEo7s8)&J*O^`RVCLBwU|)$$wBw0|XQR000O8001EXo9i#pCj$Tg00#g7C;$KePjF>!L1$%dbWCYtFH~=DY;!L{b!lvLX>Koab#7
m9d30!RZZ2?nl~loQ6EP6I?^g^y?MmB)6GD}OgrJ~`s*O;~rBspYoun>a+t^-6R8`_5_(HyfvAvt!AV4CAB(`VX%)FU-jIm2&6of
k-!1db0au@E524PwRseyy<Z>=)|y@yg8xI~2;$2+pn0k@%Q7-L1TcBX^XYTbw4;c5l4v&IGBTARRwG};%%c;|OoNHZSqz0u=;zw-
lB(+J~mgn6|=9hR!!NL@orIDfy+DHKJKFrmdY+;QD1ELS3IkLN};aJTWt&`J?1IC=>_xZ?uolS*C0a~VyV4Th4%OI8D8Rn^dov}K
iy<r=7><dePQ$8qTqK62ILiF3wfcaR>ivth@oBAG@SDG>k0<(`E`IOG9W6U!^yqA2&+L`f5G`oM1$*86*Qbjs!@F+0WR)5(Wc>ct
pu3e>zg`FMVHc6MNC`tT>y<>~U|zz&`Jw_T<yxZOk(Vb?&8dk&%(^||YMEd{YKaEx1lHb6Pzzvfz?QrISPsr9l$!b+!Vf~VFbK!-
GgdhEct(X&pCZD>AArG{|(4(2Y!VWA8uK+|GGDOn%ZM=w~)-8jEs4z1z>+2LrUSMsFa|Maxn1y7#WH{*=OB&Mv>d&8|o-
Ii(TM!SUj7sEBX&W*bHq#u&uBilRv&eW3yJo`HiZsjoZ@bH`G<IMn?uYi5hthqN*mkFc-
;)GqiPufA8+CEey7sc}I>fPx%)jV76JoK7(NJRB|Ws?*QbKRmB#8{M)#k3vlL$CiJSxB*Io({B2dZXyBtzoWWY=RO>QYyf|a;f63
Ris|+SeB#)<@I=)Np0YYc79FOSyH?M9Me&iN%U%HdEhYQAoZqBm|uD+K0~g@H>6VbNa0sh!&=O+;s9S<QXMwxAhz)H`w#f$xXt=8
)jX^U(N>Zo=MAjK;UY!@()c}0z+q>R9RoAB_b9?#Nhn#1E=ctB{&284SrzGa?;fXEZ=z7n`V$}KJqZS~f?>lRr%1EEv=_vQ!<JmH
bCjFeD{osFfw@}FlY7gRA9QZO%Hr=9`8VH%tQL#s&+3AN`10c7jK(g{U-
1i2O9KQH000080000X08YXyy5a%=05=8z03!eZ08embZb4^dZgfm(VlPy0Z)|ffLUn0ubZKrcb7*C3Y%XwljZ{r<+b|5h`&SU!#R
gpO<1_^DfT8V%U_leCX?NHLL$zr~t0Q@mj3fy9-$z-
F?X*42KoUnJAIZljmRfBg%gWZa8nX<<wo%#wmr_}7g_0%+PG{yIbD>Uul{vi`QAu70LFurPBv%?wIG-
z&c2&2PkTI;4s{Qw+k{0(i2!ak23M^s6Wl>|8<#s=tI>o?sWoA%_+(vNm35?aV0O-lpc1uB!x}(r}B^BC`_2(=G#-
b=8qiDjY3lSwyW2Z<D;~ve0LAd92i`QB!J%E5PfZN6%SQK>LjaE5j<U1|~N|Ib7x0sps!I{yR%xti(!vViXi-
!Ya3n9}}{1}*AUEkl_Ef!~<s<p4VuI8)jGe6Y&HNV^S)$(pVdgi+#ov^hlSOiMLjgmNp<Jx8tcbOp!5<<GxZEyEnT74J^q!OE!W|
a-xxa^7RyOkm*cKQjFg0xakBHzGTY?0z!4LO%N)-!k%bq#idu-m8_q3;ALt=cB;MyO<c=sY^62Q(URmsleSTIQ-iH$m6hnDIsNLl
Y)(iJL0yFd9+By||Ox`PXmr#UeV3!F`U6g_W;vq10pBbn<x#-Ed>h4kskJx3HI&Q#?`V=}ZcA9fYj4<;6$RGdggSGL22mb7a08-
z$_1_rhtrz!@B$vGDXu9v$`*qf571+<l$jP@2j0^jejCiz(|UWq#HLnw;*BTLtN;XZF37z&-
cFJ#?SG7GdeyoT}*z<n$mU7QjXjFYUKpxd~i)97AK}7BpqBN<pn;MJoV1O<<Au_{dk+a7`6kBvOteu01r!X28_LAIvQqMa_tn2DK
Gv$bLK<$gnoZFd(?yAuG2@COkO9?OEqmxpEWs6hDL9{U_WHr60*cOHNb8N*@wfc1Duk6m{}SBKX^qyUXx%DE{}vfft4F7^`X9UwC
c$i`>Kc)vHtg>(8vel<E5q@8W>Oxn3?8q!=%q;2%&+0|XQR000O8001EX?l`WSWCQ>JG7A6zEdT%jPjF>!L1$%dbWCYtFH~=DY;!
L{b!lvLX>KocXJ2P!bYE>{b8}&5WpgfYd5u<WZ`(Ey{;pqf;9ykRWWhnvFD_hQ=(=t|n*>8PU`PUkmMEL8L<%IG*l_*dcSlN=6bH
%t!4k=PdG5L6ofu;`T36sU+<_6iu=t+~<={qCVr_U0wXl}2g@p&nQBJ_t3bWEd!fmvIyppJqF~*{(G`fc6vfR3@5z8gWy3xh~S4u
nXq*k_-$+BD<(VhRgMhn-
~b}dy3ged%f)XIsSi=v3zy~?2wC2Y7VDiP;yHy_HRz|Gpup^&*tVEO^9GxG@W7vRAHP$dfszc0(~NLskmN(6EG87{4We|WVOpN!E
aW=i*rbXp4OK-
D||U`gcle}dmc$+wjQr#)Z!))<n{k>mFuc1<O78J0^~fPN6h$N~wL0T&%0S_&sy3m3Cik|m%`2qJ8pq9BF;7XyjTq2bo{{taamcr
YU#5Na1nC2L7gq;hc&$L|I(7qes}So2+ckwPt1?6*>QH%o#DC4E^76k1`@2IkrWmb6Zdut=Uo!Q1=5hu-
@1&HO49LW$1X!lXR36)2rB%dTEyiYE=w76IVT@HXiQLgqS9SW=z2Om97zzw^ot*bG3FlWHrXeuI$xvVe=B(Xjg=cph6=;T8LS+9|
jrK03#=%&=-pCu<S2$-mP{J)IOV`C~r$%94|s6{^5E758l7rRxry*^k}PO+}G-
wCPEF<WzxyHO#^ipVIB)4od4n7Ri|^26!fQCM1wMUyh@bu`x8{@gdjP8=e&J^RXgQ?wpB9F9n8>E5TB)>dWywQ2LeZKnhtYjdkAC
5yDQzyA4Lf%O*aLw}ralcIdjd#hzF344}>U31)hDHF{Uym3~w#IXBVoh+Qrk2cP@{`{$UWF+b$*EIC9B8=$0KMMcpGcGoC~o$-
LNQ+h~i?7Fp6vfEk|lF#ALTf{Zld(%ev=6K&%X?wpj-ZTg?F4=TCh1#xreOVmg2OQ`=_?JPD$2)Z($H%TkweVV_gYGAA04ZRXx*u
RAUd$q6(eV6E-
6@uR)7Y_E8)!JX{_^+dKQA%5!CVT(MIaW;t(SCbI?F8eXV}AYB#*MR=u44(7S7Ls3gfYE0EfmPAB+|1zp<_glJW(XWYF`*uDoSl%
}=d6F4{@67!8>uJvFvit7_l799Z+-2je_xTP4I7(|5BJI@8$VGx*E1WkK+KbLzVTV~^5pKo+TQX=z)PzN=EQ-
h;1*=@^UM=tm5{sdz3n6t!tnlLR&!j-&|e=yq}FJ-K}&*c_N%eG|EBiT5Xs(Ty-pVmh!EN2Pk2pid8mCT|&zIk6Uot|r|AwPyF}x
%eQ<1mvS1z6A|?`hN1vXVB&9#G@sFVUjX7wtXBgPh;^V$c#p*;EKHt^J>gJp;+xlpL5b#QI)U33d8?JP$wE+1@)EhdQ6@`e<^(hC
eM(F#rOig!7JlMA%pVuuq^yg4`Qu!_?k3}@C<u2fAK3|@phI**bQ#3uD;+63q2wF4^T@31QY-
O00;m803iSewDYI(1ONc_4FCWz0000_aAj^mXJu}5Ole{-
RBvx=b1y=5X>4?9ZZC9aUvp()a${&;ZDn(FVP|D?E^v9ZS6gq}HWYsMuOK)Cl>k{tF!aTPhYel34QP{~%LWWdV9*j}vy(`bq!JsR
|NG7%DT|7|Bzu@1BJ1#6zH?_Nr8i2|#IBhohBIBPxgj^a<}1w_(r{zg3MdbP0S_mg;d-
g8<FIQbNl^<fZB8kjOe(D!vRG7|?KEF3h-g}+En!kB%dAk+1fD!El;-{Uk1Nn{U3V)XGlFRR-*-
w{zOj?Zgqf`@NXaX*X0oh#QrOKb=E(@tD>EadC~Qim-xFi?Y(n7q+Ht)lb0j3lldrf<sH4)1P@1MW9Emnb9lNLqVD(a70X~`u!^t
14?)ZDHl@1DsFoZX)-O_a8czrCu8sN+QN3S&;fyAYf{5jQ94dL&lB*Y#>3-
4`j?i=zGuUJ=GVwFoy(P@qR1tjx3!Z&R#3gJH&q9p2pYb{F1rtrA%0MHI`37j+~N_!_f;ot=dyv_$?ospIqGuYQyK7@HS`~jf$u7
K_V1(wL7;WQmg^l7Zz;jH0g=SX|{FXD#Fl521T&|*f%i2Z4B{dOdAe_#To!U$<BlLb%waR#}73WF+iT2GuWp(-
QbC&2GK>wfG4KD;*kKZ-i;S~LO^3D}|{cT}Isi}Q5E*sx7<k&#Bo#E~-
c_B;)#(A+>t8Q{A0vGCnjftoN4upUF(3(NJQ9}>v{Iwm-aqK#u^?jR3TXL#<-
J7N^Il39*0z2Y1{u}v#08lKRzKc{ES^sFRjzs$})(ez1L7m_t7O^3kRxSR38F$OHji0GVsWY{s@I|$<f-
okE^9!fAF%JfJS>g9;*hzV2dig9!@RtAb3zLTYU+E+lzEQ~mmgRusXYYy`bMO^_LJBm+5cPNloLL2K;L1j5g&3XbI&BqfyubGKW5
4z}S5f=d*$4@Zh%ZcG{`Il6W5~lN!ih;s61#c~R?_RK6#xWYl2kjjt2LnSRlsH?lD0;@e+&$Y-9Kx<Zsj=yxr=qtFF9n;C-
JlV^QQw>3;hX*aP^F>sa@Mv0F{$WuIwg%+4f3MglfTIh`@#K)oZR2Z9U9(8BNgEVrO~wJu$?8KyHvw^uT%#k4SIYwo=Sn4-
pM;j^DhbpMo<V=Cf6T-|M}NTa5dWCzS0oUoZ8jG_x@o-P~YmXg9-
>HW^F!{CjHGZpSXR%zzJKUgNeHuZXZ=w*Hag7Zzv~2IEN*z`PWWpUgqS=*<|(Xu#}QA?9lmWeWqEgDQqN?C|Pf#sNr2Ex)p&?v`R
?gyV%#+psX)++}f3>VS<w77DWAUPA;Zz&ok1ag2|ne&n^pwbS=t6s=UYn&!ezwu$Q^{ne|%^mlcL6_kyWULCYY*9E_X!Zcu2qEvG
X=)$$83EFGpbZMAB-wgPepH8QIAaGiQe9x24;k*i4Ifg`E~WW2#-
f|ov@ZtXz!`&L}45)kB1^z6r<hilAph;AutOTL1QpB>QMzYOo4y8)FELLrB;I^@kDLtIZULGJH7&ju0i7M#gfMDYsiGypu5he0sQ
?dTpatl@R_Ds<t3^gjgkL*E6VWM?GmoFDpr8N&P$Tz~U<Hk1dPFM|8THbV#@t6?O%K21-g9$NMpe9=$Zk0lp4-
$PNbC@V|hbzjH5_kqCz^=v_z|EEaL{oB*<rldMM|Monaz^J~ty7~wc&JXO#KTt~p1QY-
O00;m803iUX0C&rc1ONai3IG5m0000_aAj^mXJu}5Ole{-
RBvx=b1y=5X>4?9ZZC9bX>Mz2Zf7oVd5u<0Z`(K!z3W#D)I+4g(H{2Z#sP{T?H1c6LF+Dd(FP7JjcqnGsghJ(Bb)!eGbAO;O;M~7
#4<nLJkGp%RG#Pajnwy2ufZFmrXboDbpvi=tcTW`wMFMZ8;_1wfZrh4PHWz<r5UltD$nyQTUoP(#bVX@&f;PLa@#V3(6m)}X|&6-
G`8_u71#TH%Rp&-{?E<j;^L3Xi$C97y-
tW#RU3=_ikEBD{zi3csV6WezVZKs(H_5h3a~l`nPxzr0CY{q3ftcase8O(@UX6`s#nHtg|FrW`JQrtwqG894bk4c{Cn~C&DG@xn8
EJ=&%kK44;j+9L+4Z01o5YI?ufEcjAnEi^;T}T*koDO;0hLD`C@CDPGKRK))exAVm^V|f2WZn7I_J$=it1Bf8mON<B4-
FD}oY4!uRz}Z0L{9?}d^zES0J6zjibMJLxwdpq4%slwp))rZXrgaOJ3s2*$$0V_B`y7kQ7o2<!4P?4c4+ptv=X;g3a<g$@kE*wQq
60?t3{&pNNZ7^#a@ekRW!SQ{0(TC`ZusS3s^%g3|d<arJ&ip~Q-
6$}Al$Y=0@Sg4TpFfCS|(#(b6<Gi3_EtSysac?Nn^CkKnqJAFB#hIzH5z%5`PP7hLIzMB;W0s*%lpRYPTyZia#Y?a7BybO#=%6Fe
2hIRZjj-c%Noo*ouWMjUY=mw|459ENrB6scYd3{P*1i|OH09!2W9nW$)(coE;XP`q`o2$)17}DAv`g$s4&Y+?cq)K!2(AvK(r_U-
U@AMyZbBL>%gVJ%`l384J<pFSFQh~GOQ;Sntu;382k8K}t>2Ss`n^j!-
zW_E4wAgf15_`^L5)9`A#3#0?eVUvRw!%{d7^UoD^!Y0xfh*!3O*s^^3WSqbjyN|6o(sBaq83bbnu5;uFE}Q`_vp*jajPP{HeEsP
!<LCiVaQg;O_32(cK+kTGOpJjGcg%omBpmnq;7#L$s9%S6(zt@cUl*{6uaf*6fTs)2U$py9CC|f=a>fWQ`RGEV<lDYM}<E8nFr9L
b<Ra#fweFsimO3wQ*@FxvZh#Fo6h-9GT!GcJeIeX6coZIy4`QBRN5q-
Mszy`pp%Ua&%3^M%H4BvqLf_sZ_4EvgNyJcIfx~Wz%p=3?0<pdMEuwd6Lo*JiVXo968QzBdLw{rh`MP=R0HXp&+eRG%tLZX7g`|`
<hM&8(G&~%TF!2R9V5;Cx&DPFMk*$^*Fj*zDXySoUNZ<FJr*`LMX+ppZqUe`cTuLtKcIwYUsL|w_P|l^#kAGbTgvc#A8><reY3TV
JWp#BR6|E1fgpkbGoU_@(b2Jr8~^f3q_08ORDu04m;v5_LUz;kMN?&j_`&RqgwL9d6IT?vce3O=tvl-Yb>iDP#%weCinRz8}=&{`
hU>5VDq7uDf}i)*S}1yq;;OUDXbFoCX+k|R)YNL7yL$#MDuGWEjAS8Q%vCPXqFp2qTh`3{)z*{WeF=@Gj<lgCmD6q{QCMWwNmV<>
_1RT0|XQR000O8001EX7%L1~F984m{Q&>~CIA2cPjF>!L1$%dbWCYtFH~=DY;!L{b!lvLX>KocX>Da+Zf|!kaCuFTL2JV>42AFh6
(Xk;vanso2xKq{8-
=o#tvv_NR$7n54zj}9mHqcQaa!Vojjd05&#xxeLRHm0_k>jirtKUtNNXKSHqLq>>VeUckxh$N;(E_u*ngeH3Cwfl=!U%<(DJtF55
{J&bFPW|(pkn63n8RGTLl_xI7+J<Oe@8wVh&|cNjmrfv{Af(yJzrBg@CXKgKc~Bl3VwaUhU*Pt3__Ss~xqH(?t;5uJ>=NcPQt!(s
7cNEtbj9TZJJ>Ha=?ficB}eP$nNyi;oDZCkp+r-z`V&5SNA+j)m3d2A&@8A0X=H)2vQXkYFTVUdD%EC4BBMDIjrQ-
>7&($4W=8Lt=wI)GvRtiqzT+mSnS?Gq1Ao7_o_tfl?XIOoRk>o6S0WKjt9*0Z>Z=1QY-
O00;m803iUVPLchQ1ONbV3;+Nk0000_aAj^mXJu}5Ole{-
RBvx=b1y=5X>4?9ZZC9iWN$8Td97A$Z`(Ey{_bCK;66kKQ~|}ld2j(EO}7GR6V%Q&zz7URI>$^TQX{D*hT;F-
J5q`zFG<^B0uoE)@ww;TDTG*<!hkoXoPggT$XnF@#KBkP)J=&{mr}#pSddUPrB`p9#~QqJ_n8o4G+J9z!D_W`d}DF70#((<dXQQh
FTFC_jYjR-oin;UFh}o|zIC1W;^O_q>f_?<)9Un(*_U}57e3AY4vX{lRF>t&Vs~c7OfSpkR%wza1LFTvqdh+Q(P+MyEw1KgbC^OR
YSaZO6e$R$SG6^_7M<hI+*Eam9t$xZjYiUKbq)otVIy@>Vv_sENgp=_X>Z*G3YGgYym<%C+sO#%vGRdb@osjDJ`tWA>j;$h)EdYi
Kt9#ZOPymv(kYb6`EfiQ5tKvtQ<e>$S!-
;IL5_DGZYVaI;H}&qKugq&G=_Ia9(x6JEu@Fa5ae!nW)I3^#grpFe@p_$C0n~BOH(%Y`kL%qUI!u045bTvOo5_dxAZ|TO@&ta*2u
R#3yE^i2jN73?1}Ibp{B5-
=#ba77n8WQ?;{;~v_%Vn8Nxl|0yYkIf%$&Ycd)s+!`!zX=BH&qYy^nx&M2J_;ixSJy5l$oa)uD&%+;mx$#{HBwiWzIavcHX0IS+>
d)&x!-#DUn#3-
(}gu2uxUf!xY8E2(=K${HcwMfCG8oJW?4%5MI$c7{8Eo$dpqv>xAyOR`7q9;2=<GmPw^|)~sX0m20l72q4Z_CM1@3^L#Ztd>~?Aw
g~1-=jpS}fpZ8@gR6FaccHR1!r)4Uf#{9ouM4UZa#K!uMKfSwclkgF0kDqt1{qJ}%o*=duWNqqe-
UHYScH_#{!WSXe=j3dOMOxYFV2us4lU_)H!fAAxmmg!SXNPdU)Xv`9T$hqjy*O;x)?KzD;^2y;)qT-XNF;d((>?B%9P-
u?iKUaLI<@-!?;LgIcFjvouOR&(6r+wv(Du31&*6)Y)5*~G*7{oxh0<0&OwuGI8{B-yyfo&WOu>i3VI$-
%w35*?yth0~ZRQM^ExQzh|qn;v{7{<1`!<I>axr3GwFWBc=yhbHI$uPjsXB;#4?ehc~4IHX!VfH_3+Aq`STC-
V*F_uPmxn3WH5>!6m-
g>xUS&d)=Sp0Kn<(wAf0>Y>#ZzbZqeNS?`H9)g0@+}pfJp_h1&bn}5TCGEpJ1u%nCS(dEP8|pY4;{KrgCaC4CBqCHTe5-
(*1XEi4I<!xgfyzwBrWQ<qyhLdudG=ct<=b4SrKLc4v~GGxPvN&Ur=V#2cG|bu)M&jzZUnpIeB**WULF9(Nt^y#pcj3XTM*fYjcK
n+X&8Wym^Zvnfu?qoJ%<uU?Q;xXH)|mEiirccL)Uy+XrPuS1>crlmp<~u1+{m#;j0<v^>bEt&;I4DL+}1ysq&pf#LLWK==_{{?{O
{Z2He%mf3WX`WnuB3M$uFvExoq(g0L(K#gt@u*^hp&o4ulP|7=?v5@?56Z~OZyTd;U%w$u2Vj;OCLE-ucgsmAU)`UX%-
0|XQR000O8001EX6y)NQX9WNNNDKe~CjbBdPjF>!L1$%dbWCYtFH~=DY;!L{b!lvLX>KofWny1uWpra`E^v8$R?BwVHW1zOE2iio
WGvBk+Ge3f&Pg2S(K@k@Ew>9>;ejYfLQH`S0LE4&ozt)BhxJQ315hL-yU{`<fjf5|m<JeRe~J+ld@5ifY&rv*=UETN`JKvgJ~qJN
>f#i*8iN+L)XLzKkNGGQV8y+S8Dl{((fJ&bWKtqRBnilQk!y=mD!1IqT$v!K*0k{GnVn}FT&aXfc_C^Lm-)=vq9TstG}mGSel-
=!o@eD$styd$TK|8XE3zjDlJ_UC-ke-
qLLZjw$_U+c608U8<MGw&E~l^k!}tKgJ26TcuOqe&lEH_;=}B^Ng3?-`-gzN25o-3rN}Gx6&qu?jM`8T*W%Od-tsJoq0WV=ij}K9
hygofU{yiDIdUv_a5di*>X#Ztctj6-
&YNS`0Tv@%ET_1Lz4_8K{6si^1R;HO)%`nbFuO@kJ@iEHs^!96s?~%8Hbvz?#?F6Xz&BfXIV}^$&)v~ZFV;2?aO67j7VnTOb?B5(
dbOoJwjFF`Fj#v}~!B|Wnp`%P}o>2Tl`s;zQI)d&IJ$uefT1KLcm9Z&DAp_J%8&MmAx@Z&i{Lt;9Y27XvR%1Ib$@tXt$<i&kR^UD
Rje3l}a_Tz<Y_c(Ic7BB8Jj-}t1n3e=AfJFKcq;Hsft?93d@dl9N_6N`!6@VE)-5=JNBz70d~<oDhI?)A9*@M0x-
n1PA7Sxj+cRI7z8o>&vIyyDxLK$a=zwNey?An|z3;V4r2||~4c59$?e<}nIz#pN84@C%3L7$9BjqfLY8?cX6TliL30%g^HFwg^!j
Mt<_V)KlgkBB3N0Fy@Hgk!={DWtuIMF)SP65nIW5MwN@j%4_xrT<tab$8XDMnJ+mXULQpQJOc4U0(T*#Z8x@rVe2IXLLRT&mD5cH
p^#VazIrFi<h618Lw>uEh7Ob~q!9!OA5(1%rR%GNTU3Do%eC&Z7;tv$y6&-
#hh(uY1$qG_q#L%DKo(+ppSVe4I(_Wdpw&TI{u1|EGh<3q+_EQ^OS4eOoT1bok09c2NkIV;&G!T74XkJ*YcCkU#ZWp5oJ@XrDThb
8N17LXEaodQRB2+wZ}$O|TxaHn)qPT7+8+w-U#XRNJ;s@PIcPA)|zL+4jZcR2}So?(+2u9)@prEgyCa9OdH$hJxR5X`6u1m<yx-
@nj?w*NcroJ1$Y`Jt@_#!Xf%({VOapp+Zs;tzopV!n9m=llOsc*GUCsnCUYuiVS<rCYjvWK@sLj=A7mi^|fkp#YS+Q&O&0YYt*57
twi!1b*p>O6`epl)p=Qjhf%BOH;jzBKHEK&Mnx6W?cvbaBr@|5OxwHNrH&mO`67NGMUU&A+Z)EZ5{Ert|Ni|C^Y;4WMl2rPvW_yQ
t}V@a2ul}_HMUjK=z~KBJ`P7%yX{uod(IB*yXU7@?>>A&U9F3XPiKWgqR;9}M>W95!sjP8kbaZ)?5(?(?B2dWTC)kbukY4f44SlJ
;rqeIQ));E{wA~)W4z-4CX!Uu82#<??9+a;Kv=H>p~x&v6t@XqZ)H58bCoSngf3+$GFpJkeX`ZazeMb1t7cSijm}$YYs-
d{1n6FtkG|mDhc%6k6*@1_YAFovFSm-&O(I;ZrRl`gl#0C-O4^_v8Jft25S@2HkJ-
AjP1nqfT}@jy;-C>zp;_l4WJm2seh);*Q}UPY3UyrFh;Bu-rZ{ub9PhF?uz8tTKf9<7@BMs=cQm)$XuV>y_*zOW#%Rd3i`1~S$;V
^q^_;ik`<7#_dss!~Zw$KcpPj1j_~G;O0bMtP!P(g<Cb`e{;6G4H0|XQR000O8001EXFoG$g@&*6^wh#aSC;$KePjF>!L1$%dbWC
YtFH~=DY;!L{b!lvLX>KofWny1*Wnpq-XfAMhjaTn(+cpsY?x!F)ppjZdPCE39VY$eXGzpfbS>kLMT-Ts2+Eyb`3PmjmJOg`(J>i
~YcO)fIZaOT0V~afg?%(h3C`##Xd`?Qv<YG-!o~HwHQZ4TBbCwhDeEji}a1j@IB2+*`PL8fG$UT21g7cWien=_p^_DWv$ZWQ(R3-
UrMv|<^r6Np-Trrj8qU`nT+FE64{abQ#64&Z8mEh%q6?R8G7l~Nad*k1)PiM#Hr^i2ET%B31VYtX8uO*IFT&U}`S|uVNV{pg(KhA
~XPYR4!c0mR`0)HClQ^AEk{*fi3#%mT^xiAbr<T7I_90TMH1c%F7+&nefX1AwDH^=9*yPHcA5xQ2YC<pyMx*Nt2Vf?Iea3IrbecG
FypB|l@-rR!thTfH2?rZIIK<LNgyPx(MKJ^d71L8gM`OL|iPq(1(=JfXNatvPpAUPrzNy<IBw@6u8MpW{$O4V$}=;X_2`g$$-
GNRt(3!T34&C<vVU%&T<eKy()5aQMcH?A(OuTTF6Y$=kW;OhHG<D;{0QRoom-;5{-
+?|}fBr$paYFfqdDgs+yp{;(e*Ngd*%oZtU!ozqENU5Yx_DA?_5-
T|nQZ$_Mtp2d9<{l+9Ab8IALpYEWUW2(zo@SLyJq*tasE~UIdPHhtLz4zA?rRC4nHDng4RruBP3B?2WXW5;KUBHmy+*RJS+9E<Ct
S(AD!fC#fk$0nHj}D+Ow`(={XX>vyC9Zwl)TXg+?eQR>#sJ*D}Y?u+km7=mOwnA=C$W(QmTonij+_EcKvTUH5yf-QeI+28vcdLM8
qsjHL9`Nk^|)?Hf?svC(B&c`=FILjOzkTtqVxEa_}F9p%NopaxTCvu22Nm;iqRTLal(#p8}$j7Z^``G=YmM<B~xJjCW3OA&uy(%M
!oYgxo;WLzzx`FcH)zpb$?3zBa2lg?|fZ8;PiRvxp)gi(?Ot_)coI^C5#^iP-Bvcy&2wHv-fZG;yD3SEp#9{zZl)<xLJspYRlDNo
lL9;}yzU-
98ybmLnbYbIIAgOEN28^UOZZvOKP!taUSk&ek+pD9D9+f|X7mrFHd@Kgm@txX}r7=Y%Vkq$QcB`Qn~noQYcVdYD;d;Qu;*6c}>cG
^?0-?BF=O5G-
bjK}tQ)j#*P26Sdj;;R?7y+fG}1K$|+mT;u6)N)Ij7YY!Ed&j7BwzU@QcjEAQTzLqfLfan`&nLpP2wzRc$M$YQ=cC(BAwTOx0S!o
a_)7G?<%{fw6Q_y4-sYQknd3#{e56_dq+k+`|3<{HuHfQIRQn|n&byB{hL$%tsn=q|;v<DD-
h!gE?T%WbIx~D~BS#f{6H=;XG9eHi6za91)d`G@zW(?xcyz!C&#sP*7&X)Z1*WYAggR`aRZXGG@r<Q7S2GM@8puoLiv@z<zlw$N*
3^m=fBcqPNjwNWeBerX|<&DnqcX?x<TYJEk*f4%HEUPSI@_F<NQfELmnnIwoUU!ZBEL#1LRd@`)!gbC=^?rA!WA(6Kt25_uJhJjx
EC?3!nu!={Sl6p_#R>?MD`0M%EL3-D)^&i~M;Vv<fhK-4hMgGceJ4mPf#m(l(u$u-
nM(^ml9KSOP|vn77kMQV=z;;}=+djED&BSFGWO&h1|);1=%s)h9zY@1hG1L3299dl4)n4;TCU_}iG&1sbb|c>VPx}^Q;TWBs5@4T
txarjottAoU_7&|j5hQE?tv!L0a<efEwYU28>2}PAY+Rw;KuD(iK7#|WREOS&31_C@~lC&ui;p0F9U&zPnWZH^zPDjNw4w-
1$tD&Noo}QKyIN8J1w}ZJ2K37mXZu2hE{rPso*}18}mGVCT3LlZYE5FwxR8&quHLk)U>DiR&5w(0|~@4y>d{Swe5hx^sT3rz2qWS
U%(D_ryCRkdJ<7|qt1Jp2z^g-dU<{Sc%i57+(VjycIeziG-BPlp!;dKZAfez{46$rxTT#*ZsEJLdj|+s+V1JQ4XJG)`UrM~>&v^d
i!1QUdHph67A)hD6E7N=dE2(is3kqUwXZXfd^iHHk8!Qk+`$3@^-$_{80v6&uJ0}(X<Hn1-
e2de<Z<V<Rq}@_kvz7O%{TVw3gZgvY10DXIKwxueEyX$lr>%N6f!TkR0&7oY&vml__b-yV_Op|B#z@ZZdiZyiI8rCE|6(gyZ9Z;p
uh1Imo)fRWJlFimCd29@?}$g-
r+tpxe#7)QHBBSpsh2!9K8#703FMmpR|r8;7_dEQ)e4$Co$01Zn!=$n7>BMf|*ewBl8{DSBi}1m5P2m2zo%V@uyGt3T=qi`xj740
|XQR000O8001EXIi#Zfq5=Q_uLS@ABLDyZPjF>!L1$%dbWCYtFH~=DY;!L{b!lvLX>Kofa%psBE^v8mRKaTFFc7`_D+ZlxaQy*+E
QCT!A=`$fds-HwSmQ*kB6%e_sVV*U9Z7cLw9O%j<Tr0--n?;Z%>nAV?R{^tu0b9;V?A)Kjptq(?XqmVdvQi*SsMbXs@Y@n>L&Pl^
>|-zR=-w1OW<9nhT5X*l`r9lR<^@A%2=FYRy)*wqxzlHB|ICW()X>=9^d>FaWeMRb-
X!;S>&P)h?4#ipQxKX*E<YHXVekvj{AKHCo4ThV3uXv4Y~n=Ef7{H%p3o<n5Uz%?anPg$i^3N^8=i>iwx+K*fc*NEU!}JA)?x$&s
jLK5*RCr7}Eq&?J0n0X1MWw4mC<d-m$6tlCA*R#_W}Jbt|dp0#G@GN24(tYa5i|f#98)S4JJ#o`gvCEFue?8e;b-
=prPOE)sl1g88iSG^$y-igaZ~Ir30&Idw*tWA4<&MeJDv7j(p2O)CuGTjCK)Zq(6mmFN$h%g1abpmxEi+%-}z?>OmE(0n)R-
}euXq{GZqd87&{mMqrC%6KEtHCA@P+slLrA9fp60uDiHFcu8y5#vC5I7z<;zem`~BkHNz3ZCg|nl>rRE_~!T&);t1o}hs306|XJV
jFhA@uQ?u-
VJ_l$p4|$5(a*tE%4@`3fe$1r?dEi4NWnag6a_l9ngx>7_7r80gG~Ug{7uFTDN?^5cr`(vH&yNKs0I*pLEuAXuU*7&o2?_S#r|#?
G+z6oI08Doe?vk1Mn{B8u%c$sOa5tL~1pPx}`?Kq6bNYv_XBorA_NS7S$)}kL%-
kr>Mv;HGQq2R|+(q(vYVqvd^5+_>1{lE&C=t&E#J%ZQQIs=XbzV&)*r43n4=ZTy5rBNBbt&NSoeHcA0+5jJ*B)^t2{pCx>VM0Z>Z
=1QY-O00;m803iV82KW9Y0000Z0000b0000_aAj^mXJu}5Ole{-
RBvx=b1y@6b98TQFJE72ZfSI1UoLQYODoFHRfvyID=jH4N{x?K$jmLsFDg+;%*)F!Ni50C&nxBv08mQ<1QY-
O00;m803iTPTu}fs0RR9M0ssId0000_aAj^mXJu}5Ole{-
RBvx=b1y@6b98TQFJEPNVQp}1WiD`eO;F8lgD?!f^Awg(ATb^QiCrq~G^x|n+cZI%7@CPDSz@N5Y45%S*oqHH?C-
~R5b<E$41Cc6dOZ@bg{~ucv6Y*<E~R9|IRXOY6xd#4$&M8wW?AoJ+P3|~lc%-
?eRb9|2xBY@*4BiLQ&rM>`omArpj^&_HB2|ovP^{8NKn+nMHn?w-
b%jJdr}F)51|I7B^U7U2!VZ_K@3l^ze#zXDAhomW0GJAh(!_YPsigkG>cunXpFd0gK1AJmx7`oy>@Bp247c4z7RNXzqBF+$q*(Z<
9q|DYLhwPqZ5-
4&G%ABfjm3H8ql6UNb*KqkZ9+~v!)R7yJA(Pkz@5=9yiivz@NK*_e4*hllG({^KI3>?@*zXPRoe#W#95ijDc3#=C%H}Z`QlaitHC
qO9KQH000080000X05p9mv84b208Ie^03HAU08embZb4^dZgfm(VlPy0Z)|ffUtei%X>?y-
E^v8ujzJE>AP`0OoPu<viSY(5j2Cd>&X@_QLrbJH4Gf9L7uwQxBdeMBKk#heK?B$%DIkD$!^lCjA!0G&n4(g)bj~dYtnoqVe6Agm
+<odCohI;L_S<x068y>xTH`&)ntL|yX^rz95`lGOJOqqm{uQBT{w!%JLTq~+OeROA0LpWqFZwwZnw?5B-
)V}%eqMAcT7@dulq&frRr9@8W-
s*vP)h>@6aWAK2mk;8ApiuGNKeWJ004p!000~S002*LWo|)dWo~p#X<{!_Z*OdKFJowBV{3CRaCxOzTW{Mo6n@vQVA&TLQw0=z^W
b7emTp<oq=?gDLl)SyMA>X)QV=OSUY7s9a}KGCb7`|J53zl8c&^{MP@MDGUOREivbD@^EGtaS+*-
0im6ADQN}I4sWj8Ws%RMWFUNvGR(<oXjWUky|!GzA)VzH~0lkm%l8wn(4DyNJVB|O4I$XBnLjnt0CxhzCex-
l{9sHn}R*C}tE)E3T;Qg#VMEq5$4+TlrMy_sl?1WP4TM6_Zn^MqLw319$qVES4(wydQ9pE}vVTFWmob07fC?jBet_Leo;nFbW(X*
A7&qjMKsM+cQ&F%e9tNkXYCQPB<!z8?K@eDvY?VzyYM5$8Pe&dujV<C<E|=S*!XQ#&}TjT0Cm8$~V6y7ucAYeHOd;Y3ynYo%?^cB
BxweMJ`dhex6;#j=!9^qNgOQ)>z8wPj~UOSW4}O|CnLHO8b+S|&`E7Ba`|8pX)E1|V#twcvhq6vRwA@mE*Y)ev!4Unh*i2m70Z^J
`Rm+Qw}w%0^nB47*b<Ta#iki<zQ`W*<&If!I5awr~(tl|pI!qEQ-
r)?&x+qiA}1GMydIh_~AFF>vnP+7PS%_WdDozbTQh7w~x>%|5?>fAYIOA2Imj>7kU4sGgu=I*?4CEs-R*8am<=G-
o`KK9dNXiJ$`5+$)LE^D(1vYO#^@b;RDhV|`S|UJ~b@L=8z&fK#lo>FhGWcxot+O+^5Q>dFL!8G<g;RT>h{OyjJ|F}+2jGe^~h@I
<k$-
h27}hm;T_fMQyqF0wA6B0=LO_;1v42emPt^43G(<*m#h0Xfv{T<Nuhx|v+oO*kfRGg&$2o6a$zOjxA$HUK_rG@{@o0F&Lp!xX=1b
Dx09(o+CER=Ru6RKa=<k7C~F8*O%)A(3~2N!*0R$WGV?<(!XF2(+r=-
mMU{g5QxT_hYYdV^^T=I~EuGPyLSFp*XLf1bfZ=z|HtKEC6ydVHYxMYV2(Ed(`^P*lVVnvV<n%By?M7x-
6Hng3d?1<)K+%EqdVf1R8>*g%yJI<)AvqJ|0a=BXUau4qTyUzs}Cjev+BV<<qI_BKNh-
!51J5gZi8+SVsTRmCz1R!qAHoB9rlttfuCO$uNwt5AJP+qINe1I0GFfN@<{TVGqOU_gL*~stIG|92#XiQ;{8vZ8Dqz4BFrt>X9uQ
Rp!{a%@RkFrTI0G(^!YyU92pNUtP!|VXwA0HUT&w1&wKES$7JD_Z$Zix}6Rz@#*Z%#J>tB$RIRy=8x&e)32tMV>>iT$1My~Tb0Vi
qi6AmZSVgj5havr`ET<0L}&9to`ZM$`11VY=?f74l_G3c0KkmOoS&0nfL{0GCrp@eI|jnA2$P12IFQ1ep<)Q6Fi|M9{XnUuHRV>$
achb3-
#9?)1%u^Cz`Ru%>}%c5gE;NCodla@zdiu`)`(r$7Me0=b)&m^awGTPCI$#aJ?OCz{++BtuZ7Nu%z#&11D?+#@FCoRx971<QK(x`#
8d3a=wMoVC;}y6Z%0>e-d?xrPy{l9D&%Z?btlc++%5^}O1ju9NV<;hS;87Z96(8sd;kJ+sPn7Ef>#&-
@?*Ea#jwErB{hvlDF4zp8%8BP_OQ8-
7MEpG;<MW44=ifCR+l$gwsxXhm6Mhe`kG(7YN0*!seGOm=fdhub22xuPhbkVo>9TXzxBKCm@VO&07u^obTXVZfC_(B<=s&x0aLOL
c-_KkQ0$*WYJwt$#wBP^58_9$K@^jFiv=()7C+#M<o8$#$zlNl@g7pbtsvjCwa9zN`o8Y(4-e4%sI<JHhcLE-k{TdlU}(U-
H)_(M;|h*n$6)jWsh;m8a?zwo2gPM=;9fNkSELE$LU}(ay?Ajs)D0X#_mDCAhPK38IFWw88DL^^V8SRQTvS!LpVwXpL2*2k3lhX0
+q3VSl;wjabs>};TwlUXZv%r8u7lk)Y;Q8Tzu&>Ag+YjSSwKKg0JpO?zYu1!B=y0@(4hOCHbi+JezKxp?Bau|3QMCui$S^%1y{ft
frfSWO)Sr|^UL4@ID9uS;=b=oqbF?aEeYOS@tvqO*vN6dywDt2H<qx399Yy=hELu%jFM$%7FF<Lt3v-
Ft9nMj!s+zv=lQ4U#q?u858)Oo@sfmd0z3(WE|)fgxq%lJc-XtfyBnq{dLP<%7k2PQqkU0e#g=-
NpSG;`hR3w*!3+tvnNdQ!ZbA!DLW@Dl&co}B@XmrAzOxue>t0`^?6VD5Y=EA<QB{BSP5prp&hCEzP)h>@6aWAK2mk;8Apk^0dkGi
}001^B000^Q002*LWo|)dWo~p#X<{!_Z*OdKFJo_VWiD`ey&BtY+_?39zJjYDsHPn&yY1VcQ`E^iO#nLyYNuGhFl1SxJX~ueRixq
!Tm$`@eptVx=NytEb+aeiZs)-
siHC>he&gg#wPSIdx2kP;95b=2t46V;EGv~LQI&GBu<zu)OhsiM)2iOv@A_XMZtRPnWmVemMRj{C%3J$b-`%!K6pI{BPOGBeDV-
A~H>o}T_&yOTxheRHy-A7!ziId^QAt`PQgUfwyH_ig3tnUzQ0;3tv%^>J7yA7<R|*!o-9MhZJ^p-
p5np`#cp6{4KRfyO`C`S+j(^f`;OW!ni}=mE<G-
FS78g}jyi3Zg;0@b!lwDp1xbUVb75}P&70X1bE~RQ#c<$BJ%CUoQudWu01rf}SZ+WRc6)lKoy<qSOg5Y%`In&E|)v%gYB`73g3Qh
sSOZKtmCGCwCwC&h{u{0@J#&c0}mJm2o+eER`(=$nHDUi&<n>~|S46ICcAmfb7v=KF`VMPe*q=5y+8+|ays^B{~kMXZOZ53bQ>sL
r#Q+*K`XNAalx=#zvwpDdUq-&0j*r$dc>1}`>s0XYmr?c2ACbyu3qf|6$D-
;W>GQQ!km&Zuy(qgEjnnQu)o%13;I!nsrmS@bUfp8@`K=x3*6=hPehRYf(jx*IHrG)c#Wa_jhM~K)$EUj9!pix|F21*3=!#jNC$!
@UXgt#7<1i(B5V4*x%v!J^989V^YCIDg9yitNnc>nPDNLZBE@v2p8mKPPM@*nI&1=`)vzlEV72M-
pdP;ng68~jKR%Bp*Eg!d3QfDs!ra8EEbvtz3rX3c!>nSp(ZSq-
&hM}MNnb+<|6#2yopLC_j3T2Vv<vLQ%+r^oj*2z<zmzt2bKInLAAJiv{&%g1Ge@eCphwXyI%3M2bxP{i9VrkQUY3@_v}JDeSwGdp
Sb_rXfod(qd-cN_N*71cd&!sQ4Y0uHj_0EJ9sD#Rh64X=wN<zWz`s|8EkTa@i?dT+Py^7|`*%*3rw1IXoiw6RG91eL!fMaxf`rfR
}G5apMo5IS}nFMQ~bf7d()%b}DyvON=vz{^A(9(JU||F|C7cf<eQiiT&?#|jClMkOVPX<(!}sr`cUJv-mEQn4G%Oo(et!QjZ~ma9
-l$t9YH4V3>I8cL?oF_~`pE}5Zb!UZYg^cMfPVc&l{QFgbbsIH_?;tMdVy@{$VitQ%nl1f%ARbO=|HHmJ;lIC_4j44dQlcNiA*oj
62H38T5m{8>v1twwnoX5|Gj)p_Y2niT#oBo~<Xw+mmscLb2sMLE~OYls~rH3>RbUEZX3A!U%0r9_#;uv4X@gvJBu4x;UC*jgDG!k
dO#uy|_mnf&@I+nl7N~3h>(r8Z&@1R1WN(`zMO$pf4UTdVQav~Q~-+-
}dVLLQO8ZFe%CDd^(2RT3y)7$Srk+3y00T7C=T??f>NB&xrngj=df*NB~XBz%?G^0VG=87@&24e|oO94i<1*&AnGXbX*`^e|r*@N
EWvPVxru5f#{pmDDz_2nIigblWgoT*#caVepm1cZf<>T+1pJFO3$%-
1fl@w9S}3rKcyvV>hjr7LTQQLlDYCh|SIwnSaCkVm%>RNpNGq^igmh+b9A-s7y=)xfgUCqtmATP3@)-
6GUNxqebb8fHRC{YrUGQD~uHWdC2mS0!08Q3ym!fmuzty5G1R81+4NL16f;<V`fey&)f3wioPmlHT1XO-
90nj^RcWLhTvk_e4@}2<4F1(!riTcg<-ii%QAOMbko0q1!u;ea#3q%2+6yhB-
Q=XIk1SRj*M5w&KE<{0j+o@HT~xFBTbEkLm@X9#A0$dl`E{Lb!o|s#lqAq(P2gE-kcnAqHD~7G;4gCV=VyPmQTjm?wa%iGxi)dl<
09I5p8cQJ)`z875$vaSmw=Y=1))3bKJ|?F*+`heL8DEUr~bvMkmN&6%uj2;+$mqxTJ7=Fl;9vw$dyR-VjfyQ1HEaSNlwY|}N-
@PL^fXBl?**ytMNfDK<?dz4>a)BFI{m9|a8$^5lIsuH7ehYq%t01d&rqB=1t*6d!WEfqe>Hvj-
p$sI4XWn7&6bP=C@{PFYY$+?Rl7d>!FIW`bpU(^5V>lNnoM5E@AK&o83D^WikjDY?I8e?YK1k!0FxiUr&2Caa){^4=yzx2ehVwYF
08i6VYqH-t{-(CIy7PYY?qsZ_rPFc*6%c-(wNLQ59HE<G!#No=ITY+sXp#WK+-
9bm2#pEgBw4?X6PkJ9YNjD~Xug6!fTTws(@ahdzk)RTNtRC8!(HcrtpzJ@Le*Vk*51{A@pK!W`-
>C?eUE~9b;CxLV0$K{87S}|Ew*Fc^=gu3Dxb|Ysai+k@hp$M3*h|qG8B%12afX`})9e@!95X@Wg`|L52?s!)dMx*F0$}4=zqB-
S$4FplVL(HJ7^+GL=v&}w#qRiiQzW~aEFnu+)8D8!H(2_i0*J~hq|D$PwY|8mdr+|2MoIK7Y(poyDO=7hdMg@nY$h1cM>wiYEgU^
`hdc(oy{g%dk1@u+adX>9f3tznJF(vw@vk^|V<%s``J2Rd<0HUuBFL2`7*80O>7+UKrDXC>fWJVFdMSgI&)*8MjXUybxfrw?2G*G
<)r8jT0&VMnT6+>GX#|1}U;&=#h4ncrKetcl?rDy<3HB;X6NUtt^JgX9V|zfK#;&^~banq3P9=wXlD^R*euAv63z1@LV90+-
(`KhHpw~O9NBjump-SwtGbS6Ei6Cc(9@KKe47w1kA5DBQRh$7akr;z;towc$&ebk1{tik|O`_TEq8ue#tN}q{8fR}niIo%fRbwVc
N~UoIVh#sz^*+itukj0!?F~ytCOla0J8=Oe@WBJ<zB28Mvp=5M%#CLdV>jWHy@c%@Mu~gKK>+<^c?Z@SXn!mXGJ6x!%?%yk*m`Ko
rGuc+`?U32ap0&8AXhU!;^t`xe2#4~#4M<DN_~d_waoo?&-PUd4JoIFgjx)2j>$ek%<<GtgKcATk%A{-CsNu59Lw-
!G(mw=h%rBF^F7Ehe;sdmThhp90=HXR&q)Xc4y&E;4-yeUk1m)-
o1CczW?&~L`0u|O+NW`LBOBxFF*GxEsQYP9ZNGH{Gb?yWt4o~YP2T%CtFnU*JNEIOFV~ZMucF3`ZrSfx@b7>AD*&=w7me0IHDUN<
AEntI^dsH)W_sq4+9ATI%QmgY;I3seeHBWePxs`*uB9(xZ|-
QWB(eS(OyS6>dvhOskJ#0v(89!)3OK0y3JP@Jy&)}yIEc)&`33tS8Xkz~p;2rqXvB#C-
80%mf!o~m>qJZ+)m4ZPhao_n9*LTKH5fPQ#M$X?W%V=)e_s7zQBz|%QF**z=QGo}Bi6L#K(LUs?s-
v+u)qPazQ5EiV^19?auUphO#IJe-
8nwWh$@<y`AvOB5;WL4QLcK{GK*`>7k&;daP7w&8tI<t=?cq!g0ZQyJP|m#qI%2J#dXw`#NWV$2})XtMmC38*US}<n-
gz3D|h|xA@Vv@M!}SmP6@^@LWj~Zm7mh{xDw6{snPHC_U5M)xohsQhN0Th?+HvHg`uTCf-yqIpSeU?yQ}3O1qam~<gvF2gdwP_I9
_zXa~`ziU8ysDRY0EA4cj9yQA+&%4c%sLXxn1I&kOeZh@B-km$2@wJ9e=Xbo+~Ww!5#&2hYRM=-(ChT(wE=V>83I-
f4dK6X8Rg4{vPf9DDDQdUsOVW<Z?gtPN2*NZH1G>=73llrDy5X!>T6>z}~@;ta>&W)$^6#5~GiP*RNbu$rcL-r#49UDE-
*l(uJM$rC;A9JezJf_I0wf6|D$E(p<?kn7>^2LiXC6OFbM#P3!*WBfxjk+0_yDhsD>IF|oaZpXdfmZN)e7-
s3G^3PPxF_;cXJIh}$Tpp4}4v3b+q+ys__NrB=B?gy1F;!{dGowJSAnjcQ&6lXpT>_0t%ujfs(p~iYMw+W1_d~C3Q?<9-
@wL^U&g|QhWoh1`3{w;4G`JlzfS$Ej9)CsSm|*o67>H*d_BQN4P)h>@6aWAK2mk;8Apo&kFi6(|001Ng0018V002*LWo|)dWo~p#
X<{!_Z*OdKFL!TpYjbd6V`VOId5u&}Yuqppz57=TI@#bl*Rrs^gwU2k2yG~oG#ITl+ErJUj3g(!r1|fik-
Z<GO<NyqYc%ub&C`s85MMSjpn?tB0Ye1s1EdXtHWndyZ{q?6nKrS8ZX?~Aj6rr=<JL7OqjhYA5JjPb@1bq=n8tu@3#K1@NFbf_Nh
af6EQ;C2QP!-c5Qe73!T*Mq(?;44l;dE({dRNJUVgZ`{PgkqJt66rmPG;d<hZ8u0gqwC|I)jJyHpf~LJa|<w-4BI-jZJnh$&R?<{
hMQuz1G|YPQ`^pj6#wq@r9_MXo4(Oqh97bqY+1R8btP+=G)nLK)Cf#Sg3=bdThr!MJD?R#_?rO){)8!7|rdQnE~?YUs}lWmPq}8w
h-i7|N=dIhWNG8}<`3e!@&G<JI%GIWTCGFF8X)G#FLJcJR^cW+dEoI3)Ng?TA+)`0y{>v-
pFWQnjq^EafB~%W#sFz7sC#K+TYqYfNmp!OH3^r8E)G$dp>-
9^@G9N2eC>#K_NLVn0*Na3>z<I<Kg4mSRl$&0BF``WQ^Yzfh$bY461P+B=-M<pcxGh)YesRff-
s7jbzTMyyFi6I1KAd0Cx8&NA|g9ABXpkXlx?({z<x+AYre_60|8RsMsYnIP@q<DWR^rtPs`;bE9VOyGlA8z*h<TQ*adAlW<4<Y-
@m%yWP2(}`20MkQL*o#fv{OvGA_HkD%D7d1RRSI0x<DKPF3d^+LTaK{e!cY?T!dxEC#)Q&ddE6(KgB&c|?U<qo-
u?voTo_G>FsZ`s0HBwgzni%3ov_!t5=tt^=VJTK#?T^Cua*HiHl>aU9v6-
!LS(o`TYer|ZK{df0izo?=WT*3>*&eJ(IjpSeqX(hCvctC-AI4H#D15kZqqTzNWk?e<xhxrIAus01I7KI)W3^cQzQ?IZjeaR+<BN
e3-
<@cFc;m`UsVaT}P)h>@6aWAK2mk;8Api~BPF!&a002%M000*N002*LWo|)dWo~p#X<{#9Z*FvDcyumsd9_(<Z{s!={qA2us3;<D9
4DQRZjx=92Au+(2{6el3b=+$OSG*<mb@aJ#K`);@3|!Ppd>pplQuy7AbB4=_uR`%+4H>XC08uWQYD_%i2d^O$&7~&B4W!}sx03!d
KHYP5nJckV;qT`t%Q_(A=qpaCsCX(hP~c&dTmtP(emk(JqWRuOf3cTH&WyS#-
)Tto~k}u^Ej6*o3ktxWcpF$lB+mNS)BGrB;3p%Vg+Y@WYej(5?GrOs?{b>CF3MHj~DE?boH2AT&)$<s7xy=JWa4dJ5%l<7omtBg&
eYvBF0P(uX4p6((DPkXW2%t?<tXpMb203^KUH6wTdOrQ>bN0maT_9&+~e{In1&km~Y^k2m%(b))|!XG|iOWnC$h6F{z4=f5|L0qH
4PajD^@$y0t3rgi@H0#f;x$_`AOScz^T9eQ<w!`+M-
|=KA*2FTwTut50_WJ^kV8kDyrc;pXn{>em}P^Xa$i_rd%750Lu&dogIVnD2dKc6gs<Nokb6^m@H8K?GSn$|Efg0B##$Jd#C728KQ
n+oS~gbQ-
GX;3Wj*f;ieur$Y@NsfolK2*zowg20y|nGaYr8xa-*1WnB2=Mi*)M@hEO!+myg$v%QX#tr%-v0)I+*ac)8qecg2%!kG-
lwu06#+jcag)LkOwalW@y(C`2yMl<mb^uJP>|-+@>@4`Nd01rDkL=8TBg(D>2ZJ}M)(CWba4KRUU-va2g}z)6)jI>q{>9$afO`;I
3!24tM4qw#5oFp=ypNiC=bjUddLTBmiEq_vgqwP~+@_(yG2@Z3a9Dd2+xzT605-W6ST@@-o+L2(-
;Iz;R}%%&X<balX()8Eg0u>Yq)-
mBD&JPBwe$Q51mI5`Wv8IgFq#Dmq5L|526nar$U5KeyZQ_mEB@?b8$PK=`8ewj@Lw(z&mpnIzu&IKO`d09_kVb@F`xURE`?`J;T!
!%wUbL4bEQgl4+ZJ;y<32HwIBdDrZ6HFY|i6E0RHc#Hy|CITRCfnkw>pZaln)gnI7s4=~Wb=D411L*)tt99YclEndo!JIzTh2crp
`iH1$#^d^L_00mAW6gu@tggVCZyn+)=c$uKZJwL<;IXi5Gk4n(T}icEJU-QjejGjbfop&IMZp~OxmqrWd>x^v~NxY+Xg6+9kKdgX
9D*V{nZa1WCG%VU%l>S97cIX%$eHJk-
1m>OaxUi+>KP=JnrNms(PRv&GFUI9<dgJ!w(rEA1OT2+#^icY<iZq&?Sf`cjNNgy71(zH;s;#Xz{>~5PX{@hi)N^lNDQa$5DL=z_
YED;D|jv&IH@#x*z*`)1&i&{NK1aUJ?MDFg2S{K&mF#s?nq;cGrtI!*cI<p0mwE)gh@B!kA&VBeW>S998O<Ibc2O2xDBbvwQMz|Z
u5&@GWIHaueXuxxk()p1pXPF)ITHMqM;jQmc%MSRxvT67Fx)j&^wOULH=t(=$_8x;E9COivOE1Rbkv0r#g=3>a)vl$=O~GnUiaJ)
W-
x+Afjj>%iv5=JCTOtVakgvhd$k&n%0U(Xn@rfqMXi}$NB2pi7efB+j=Q>i!{V<v^_MN^YF~a(^1lnGXcoHvC5j9IYWSfPZ&V&Oeu
x-
R!gvHBb($Pb|;TUueKx_E#FZFv4!3Hd0B6$84{bg~7Y;_UkmTIwBWsm6EFLbC|`=mrNEA|4ZV`lXZP&59qE~MRTzOe(*t@P_Hhy|
e4GMaR9E?<N4TL*p1Idicexr4YwJ&C+AsM9&X^*+m^Zq`FLaUSubHzWBbLKr`SSIb<joI2Ic$nWY5a(3YoqGqgK%<2-
&O%!#k@}wy6l@kWxU4Nf!-
EOt$%T7#N6^m41mqyOrSOvKK)UK{wx>{AXTh~`t+`Z}AN_fk8$E(v*x}W!m^mZ&zSq06$s;t|HSGsZBe6IDw7F9f4DJmnyCKi&eQ
O##{a%ggq9_BDZ5~(X`gpFtELSiwfW!c4ePK`hk0}%Z%4M!!_3$As9APNt0L(8!`M3+lVfVsJ?vPdNM+20B^03pD|{An47OG8j}L
a8YVXc(UKJ#Q(t7D5pXiyi9sFKD#tO;!QwfnIQLlhtalUTdzttg$MZs*4Moa^KiR)q0UbIb5_&wW^=gU8w5MK|fsEmO<ZA*gD&|k
SB?Ba3f{}dbr(_)_tTEw!<?}(Lg)-
t;6HGUUFA|a_?7~l1*0*d!bj<z0d<~FDQ9P_qekcoqOY#csF4$z|%)QYU@WSUx}kWJt;c+_fdZbVD|{SVqnL5qpaXje>~dzgm|*s
qmj~RK!t%4Nu-
+<E`O@r><``7uf}~?gf_KWi`&gLRdE8SyHl?!3jp*xm(ZX0XL?Q^o)`e+<)5j?j%nB%{*}e4uTAvL(D|vev>S)+eU^kOm_0e@R#6
&`>-
)fli*b=iQJd;~Qqb*CtqfS7%zXWJpwArlHxuKk+)B_qXmwILOY%*EV6YiJSEJHaUph1<X87R2WtKPwUO&sOq!cUM_}!mpoF8t8oz
$?|hrQ*qKeHq1K9CL0_WBN}-?96p`L#-
&&}E$VievAIZzZ*)$rerQqeyWc3G<kdDr@;$653?EZw=5|^a2@pu0LMBG=5Xrou8Ts<Du>30&B8eEoguA)6YeXwR7);z0kTL)dN%
k^Cc37FX-KOp2mcRDPOhDT0f$V9g~+uf>>v(-+G3SUvXs;{K9(C-`ON-
Y{5V~Y8!z5&jghXgpE9m5`ZV>>m{Y6U4TS9KXv9zS5gpl|7l+xHAa<t&S-~r6Gzt&9T6qUf%eNjhb$$&wo5J^@>}`d{{c`-
0|XQR000O8001EXLcVMY%nkqmOfLWc7XSbNPjF>!L1$%dbWCYtFKA(MZe??GE^v9J8ryE;#`RraG3BBtmC$U8zA05(ch?Er?%E5l
od$3XiWWx_V~S)s<az~1KtG~i*e~h1%nXM&+i3;tTH?%{`+ewn-t|t3cq{W-
WJOUfL|GM|(?nKc9cP&mUyHgZG9kanbyKHB9?oW~Rn_FHl}MG{d?MmJ5jW>2@is41ovs%mt;J)UJt$EFg7q%0#UD=o$iP%BOC^fU
tjMLP<Ubp!Y62klX|2R+g}WkE$5jnzerp~iupNHO&p<33&w-F4kLc%W6$)hJ=3MwP+=hg-
mYLjE@m}nUq{-wQP$gCTh(}?)P*Q`MA?iwQDyepo>6KYrDw&+r>0XMRj8PtN3aKj|bMd%KGYRaab((L(ndf=4*`_M?B8oOm-BdD)
M7l4F3fanwI!4K<*~~mshkTtD=I2iec+uYxA%jZdI$me7Qb3Ykw2yd4eJBCFSv<`TfjC8);`>Yn;w`8TziG-
o$r_2Zu>6^T&)dt3>$4xPqwCAd_tDka+smtW(fjic=hp!(zdQTO&G+W(cc(Y+_0H?_4`-
J*deeu~ANlF|_1V?w_4(z+Ctmn?b@~0(*{4s@&Bu4A*Jsf=;JW(Z^nEa!Gfm+&sI^DYDVpNPtl6eHL%}`mx3@)J%P%!QKnsm(yAD
<vZPGl>BG6<B0+-RQC>|8AvQ4dbavv+CU^XLBGQzW}Dk}f%%UYJGs`-
MBfL=cuZz#YaihPr9n~Jn4BpwluX}uFMSWlcBM5DkHHt`y@f>eU9AehxEk#(GAV7u$Ms#0xZV2Z7?F*H0RHuwc?@Jk7XDHDRh>-
Sl)eh_I+>wBpbIBsZ2Wn_umfEA{BT1SzuWVQ(i>H?gu3Ir2EKg7@C0{w4Ee>BJVQB5f;e;!&Wcz)h41I&=&z*+tR!u)e<oGjO?CO
^;1rnaIy`z)(Ny+h%c2$D;gC}P-
&1fk_cbEp;~OI3ZFr0e>Y*Z^C<yA$G#PzQ)5dk9iH*icjl_y!`~mvtcSn>4G%{ej~TSc<Hy9T<p?vE8*svSu4wxCTe75Rq!R5M4T
u3<x{4CVT>LAHy1Q`hd)W|4S8!Fbr9UM&}DWj;BM6j=o_wU<v~eNtDQ}j^_g6rdcNB0azM*|Ctm=FtcL2)etqM6*~LEMuA%-
_%6T&=F~*a-j<-p-
JKItZV?~Ly$#S1o^5b8fQdR6@T*{g)tz8w0C*2FXBJzfU|=l3n#3k6AeSsh0}^e2Bi^T<A*bc)QEHd+WovttTuWF_get@)uIAse8
ziYhdK5}X#(UUlxZwvwQ4V<MI25=9g?V<!8217X>j#<mX%1=DxCf{^Ru2o46T)lw6$q^wKt$RHsaZGrJ3u0rfvgC7SF3>1X3c)3v
!Nh{CnGSq7{cR3c3m~H_5Zp$v_B}M06T$*fH7jjl8Qh4CnVw+2(6#x6v{S$NQ$x+%G)?!OYqKwVsIBT!VcH8!Jl_lsyJ2BK1nx3W
cP3-Art2e0}?`$)ea2i1T+yENAT(YKs+7W+z@>t-G7g6Z{+_@uEBdza_gNa(F2MNWB|4jiG@U&9k4c1J1iA4ur-
|rPW4)i#Sl4<;{4$~d3Ye^>Ih?%c&tFB;03V~fBkfMLDdm#$x*ND;RyX(czzHCM7XNOTVl<SV7UT^QC*O7K7(QV7ziJCMJCxP*!}
};=GtP)6x?I}a!x^$d)Xz(crQAdq4W{qaj+-+(_10ZmO|TS`yA!C5cepcj-
R2w69$a4Kq)FG5eHc_>8%fLAlGQ(DXg~MHAWzj@%56ox^~u5gR;IDSREFNKw1kW%rF?2J^KYnNH6a0o^LI;^VmVVv?oJ0BD5hNY-
m1CXBR#jeyat)rF7mG8F-
E44I^?wSE!1T(ks!$krsba6qi`LP_1H&T453O2u2BYIA$&zg?=f?o`)_<R*AK9#913L_>{XbbW%C&=6X!#Y>;Ecgmv%hmf9E_2Z_
E2862G{W?wAsf0FCklwsPZ+j8#)7_UGxd4jFXlb1tS@D`Z=1L4Khw%KFT0Z*Rb(eVhu+K)4E#?=a<3GA)mG(>gw%L-
f`#F>Z&p~9X`ldrM<T&?C56c9tpKR~?&sCP$fh%R#=46#$Mh2S1?3`ryvsAd}scYruHA%+ts@PvgdFbv6xG7T_u0Pb_WrHu}bC8s
LQk?FNGItbXokOf%R53M)!ZMRjqj@!4oB6G75)|g=bsPquZfW+#XO<!l0AL6W$y=>9~bp){#PbiBJWyEDSDqowdIx>4uUn(qg0d=
?qcW|XWNA4ZYaT8Zib7&!<!Mre4(NIbRI3Qzmm^bKd5tJsDa81;}OCu*F9}gq>1Z3g5)(CD*XV=wGoN3;)nbnvZAi_f|0rRjMae6
q+rcpdSuy&0!v9!yKjvVMYRJg&hHiSVta@O+;ELxWwAa0#C=&iJ#>QTk;9Ca27lh})G4stT<q}i9sJtK341BF<v({%YAL<-
p=Bg+WmvV>skci=t^l8Tom5FIuiHO&+@pE8;I1Y&;lg5iPsP-
5U})jhJuu0c36k&e~T33c}Su?yp9e=$?qO^GNI;uEO#pbBrwGLr<uf4(ma#{0Bh3WM<Vp@6IfEoXz_6(gR51B|CGC>ADZ4Bb^j34
nGP>^6O&^s)M0GGew62bQ*7Z5euZKQy%s=56O}&&4Upf?*G!SgN!&Jb4vVdZ<1m8m!dQp%NY;kmFo8OMjD+leo+MXRu!=<4lg@o|
?xGE}{IKX!QP(d*M$-n)@hn-
;spgM7{}`I}l%K;_omCaB1W=OI4G1TO`sP?6iu5g^{TujxPm|^0@Ga9W)MdTS2QdBQK0V&;^*EhP$ecz&l_OeZ(xzQC^!Ak~^G9<
QJ^`p{Z1ucy@8VmA}CX{ZVv*@yH24xf3YlFr+jyZw0Dpq3<)Ra;m045fx(aN2YB~NO{Itv|F^n<Bge^K1dwL>H#PkvNP%Qp{J7-
jXFudbKNq6a2-H)jHM-=qW?gro^E$-eZOT6ou10q{TKI6oJ`#(y&USOO;12<ONz$~5j;-
mgc(N$dH`srD@!CR#O46e6OBWxo$$_>u^9tz9yS1-
&XV@}^nWjE1L<afH>@f^>)Pj?z`<oeH<xKhgEF`S+BiPAUeD?r3?tAT$ziGV)mK*dPAu^-
v~&tk`g<Iup4@XPNOqCG5ocfODn^PM)59jM@pU~Ln+j`ieK-
#s;Nsd^XWk3!K$KpJx8Oe9lslcNYeJ*h7C&vkh5kFm++TO2?zm1kDjqxF2Flsm0fhTuOC$T`POW=xQ0N#f6T?H0&wzWz0-
2A#HCy(^n%>v83OYHA^v5{-
aR>JtHEHDOd$Ovc`#6cHG4tm0o;kdQY!pNLR>^fyC1WAnX;{rHe(g+wEfoY{P=nwk#7Wxb<JRZKmTqmLS=<e|e70;C8XSw8EN?D;
wPaWHhQLM*!ok$SB46f`TPz7+QoI0=Cc;=IWY8mmEX_DPAO;?bO5c%?z*Sb%Lygkfq;KJ8Skan~sXMXm80Q0h>`xH?ra?fOgE%t)
(sR=Z2*<(GuF>gg$(R@gYOd^<@7u-XJzUR-
=yt31xt^!=EFH@v4wL3SOwfJUvmiMNOkJf7Rbw+s&;`}z8gri#bnBvVQR&*P18O!|<i6DMj6~$&rq@O2vHoa~^`@H}r&v1sQsUh+
#2}oS**X;44M$pB1ya~3>4Hk>n{B-=_Hhp9_ICK;Dx(YJ)?-
|e!9}KLmC^S47*nvW4R{6(kxJ&!wpCcFai2KZ#p7~+IDmqC>iUN6@6pM|dVK9=U5khxqt~?PeE8|;jk%tqsynK(Yqvw`*IwVu#n<
9@vksu{pr=FBSYMBy!9|Ms44QtPWp#kg2PgG(%fE)UoYG$4Ou9zU_c3)US^@}l?nqVP9O+OrkjM0#V`SokAHId@PCCY8y;nSdPtm
jkYACw=Mn9&^+!DBNpcA{7-
MOrH91qgNIm&R~Q0QzWPz^z68sim`XKr|*xVwc8_Ww&+G%A_i1*|Hale)(7%o(J(!BZ%<k+5YqvNm8Ne|cu7ej5h1eiMH4zoo!&T
Qhg$=GMnD7?wo|qSnhG>h`MJ{csE0?&H!8@6Pb08QsFt{X36Em4F1CWU~5p1QZR#>D7%L4nEM9pyL3>o1{1~lpzMFXqpUKh9u#+3
FvSH9HJHVW4hLFXt*D6o^gwz_()}(VQJj0^Q0@g$z6_rb`EgN8Y*p~(92{D{iS)M0q7HY*wX<TsxnKVZy3VWOn2do<HApt<}{fZ@
jio(wy+OA55{<C7x(lbyz!xfw~LeC-_6D&0%sJ;CHa{8!BVONHqE1GUiN<D`L7-
cPk?EI0aSDo!N8*~1jmBuUWTQtHW9f3z63NpF?96ThDeghQ0^l)@m~9S369rYaUF*Mz^>>$wQ+Mo!2EVhn8^EP%fPw7`L$ZWKS03
~>t}K=zk(902MkjB#f5bxfpK~|?#%Y}wDDy_9aqnjTb@r5tyR2;!`9)GJIy;B_Jn>geZmxxOFLm3-
8vFzri%kMh`}o}L8}Baal%D!q)<XbyEXZZ+bsM#wb7(E+&SU{;>2uZi@ckHqn(YW;ZVPzVe(9_c<`A5eJe<r`NhEE4Y#}zr(zSUn
)BQ~K0rSEOmlE(D>)n4H(((>!K2vbiHQ_77ytR!zeU+7oOr>LN5~8*q>HWsbYG_M5=0gBYRL#Zdg&IOBvtf24h_-@9N+0al-zrm4
o5=3c%-
s#n)Sm%;DoxKHpVKGUpUztC&o0Fq_Bz5YCDUFZr|E234T(mq3`3KaL9j*o~ZpAyNqk0y_`GRhIXp5>yI1h=gU(y!k?x4w8pWTzMk
t^c>7ijzN%wyY);u?H*uQL6jx$3ri}_7Q29<%*VT$k{|#of)yiJiyzm-;b}!oT+CE8-
8t~<}ne!XF8h_$WA1kW%MF1dlj;5|JW&aCMO9KQH000080000X0A&VGK2QJv0A&CG03rYY08embZb4^dZgfm(VlQxVZ+2;9WpZ;b
Utei%X>?y-E^v8EE6UGRh>uSzEh#NZjgMEz%q_?-Dp5$x%gZlGEXmBzE9T-#1F6x=FG$Tx%!DcM2l5;}1B&v?GE-
8ExVYlu6LWHa`fU}Wl~CoBVz~fNO9KQH000080000X0QL}h3+)U504*;703ZMW08embZb4^dZgfm(VlQxVZ+2;9WpZ;bZ*XO9VQD
UKdF5K&ZrjQczV}lsm>Ut16{Bc@LV*G}vCm1`BsOgIw16N`YjI_7Opz?PjIHAu=+pGU`Xrs1-
6eNPN|sMt^rF15spahK?EHK)vt$qiXSqm^KOHW!b<UN%N(9S`?7NIbF=opfuHN92L@1f1C40@*SuB#0C9+g9y&eTYaB#3HvNemMR
i&yzL=ltgJS!CAX__fc6AupTSh-
1;GP6Iwm07B%t4$94?9}6QGi1kiTq+I{4cP~tBzV{Gk=cz>xmo*CD3qqO(+39(t`8rNr_uTG^y83zo}9k_%g_4u%kkf$lhf((r_T
`(U0gP!U(QZWKVL?lKV42wPnzNLi?d%oot$1orxzDz7v3a2K`#?(aYmyXUZkR|<vG3<sX8r+tT;G0h{cLUSt_DLredJPy&ALZ>YG
@qkR85br7Fh68C3gI!j%#!TP%=lv0y4=Fq7d-Hdti^%Vm-rmhx8-
GlBeBS*_Q+kfIF9Hpr+DV3(8yEEs*uWIBKqXxVU7=805;Ff>vThbR_`%Vcns#hbA<M8WUIC>NW6P#qyp?^VH<im98%b&N2$3L}+p
kfO}N69hxXqXU}#r^~ai_#4D!ir)(2u?EHQYoX^Y7Q|^}20;aH>=@n?m&Kxf`WBpSqi)cXz)OJ#_)W>K`0^H2humQ=jVLJJkd+y+
Nwf5j1k$qSz_4Vz5b!{;Br6pY5;zniyK(wYTSUFkFS%l}lxeAWx)h|sA&VtgR%;6{;12YpglnM&0j(Acoe{Ge7z1sG^+caHOzW_A
<Ut#I<7R1pg^*=MGpY^WJ6P&bvrBt5vWY~J`)rj3o@r{L?C1zcLNHxST4<OU1~_Qdi^iasX%jUe1ttz%+u*+utRVA2=mrFi&&J!r
dk#UdOgIFwM#yuEiq`y>x!|`YIhCehcM`k>qH@gvg4)<QG|;Kzl9&(@L^72siW+N`B3TXVUx;#J3wNUri3B9M1oHt)_7C<IHr>!J
vveh|P0+Ge>`N9`iTGef3&CSRj_&}cYra8jPa(=c)S^n2T#H5kP!)jbxJKRCXfz@l&6~B7%q&DB1PUn3*xSY^LaD(7gw_5NEi63K
H?5~e2JJm~*Ln`i!!!8nXfiKE4)Ho51w#C)o3VB*kWE!!hZ+3RL8I?*NApHvu*)wzkug^qh>V2jmd0ZSRgnzY4Jc9+Wr(H*@WF)^
iyCe5;<=1&#m4x)yWd%0o(1#J^GV0O4TT>|1(yI=O(Ge1dLkH!(u_F!nBmw#mMt6Y%~+_rthfb4BD9(WX$E}B330WWAE>8y&sV$@
5j@0A7kbyh8-SG8WTkq#(K0FdAvmtoO;*TXse%Z`Y!$p0VBUf~7zI5BkB;?mhmojvfY#-
z0xy=S(&*aCX5<&mzCAy9U&$mUC#XtM9Ip71QVJyov^r1O$LaLktij$**zb>yJQvWo3EJo+Rg$1FQF((Ef{S08)-
z%vAZ;UI$li6T7vG+iAN|+x<`U1X0Z{wFzyJBKz;hOy)DPlauRx6lR?idtZ)i3?(b75zq7*N}7gA#FLSq($ZRc?uS!Z`M&)5TOha
q5mma0+hK85&uB}&zTVJJqx31jjX2U75MlVltoG-
v|OH8+q9`@(+>G{Q5_zb*xU3THo`PEn%sv&$(n0@ymGuB06J!Ro|wG8c|&U0N7KX&dz*!e<p~+|MObJw8xSswWeOl~(AQc@VjtLs
Bu_ay$#nqgY&3*Mn8?ptbkN9zf8?zyS(XwBSu!;tmQd2e3vRqu5I`9%=<(6EQIcsnszt|A%(x6Z7A%U|?Y?2gjWyOlVK&@ksyb5W
Qj-
m{oy^E_Efi=D4<9Nr{%H<sI0O_QvZfvxikvcMi$w=mx}gU4dU<X1Ef%5QW^2n}+gMCeU(qcwvz{VFQj0l$IZpKNR|4nk7^rgP>BY
!#`q$3C@!6rEmgitBvecV=1hGVvJDn<-
kKVdx`s{$Q6UUT8S3SwpqGC<4iRj<H$H_50iZ|n04bY)O|(YN&`PKh}X~&oty<|e>{IuMSQ;uJ!w1~cJoT#dQFhnoM&LNC&L)@pe
nirdsw7yt2|AU02vgU{h1GRP9><aEP0YBOCbd&iaSN+j0(!8%b%eZ<}C<y%1d3s`6~?j@z*cv&VU<klr`1(TceZ`j1FZC_9Dt|7*
GZOg`>tIf5q5cEbJz*5r^0`fh|jm-GY#SV}=lXO))IKi(*4jTr<n1SPGn#!_qJX0AHe;)8C?i0=;~zTU8PfC~QXzb4mpbf1`S;Qf
X5H4+gN8WlK;nVh_~!af0nO$d0XtZdFRY7VM61My`e$*|wy$348FIFrZ#0828kA`pG;Twk8;Ff;slKMWMtx7X`;NB&_y8j!rIeDB
J}e-O$nQ=&?4t0tWaj!0pi8cA{u`lSx2DBn^0_vcL;Z>j-EO#N}>PU31gEK#ZnEC3X=-
Sx%iI5kCYnT_#lwbu+c<W19ZxLxB!#4f94-;OCKMH>gvh71v3?(ByEe1)Qli*#=mS08}-{XI9V-
q?m$(7f{|e!8JhUq1%|X30g%K(o;ftfnYzE%Ud>Rg)+m+CtI2HtJMQ>)kvgIU))G|#V)h8a8mhQ!E+7Y5UHSa_Pe8_=48S+hF_^T
#~iptb6(@uJ%AB`cD6DgUjp7p+@T^C?vW9l$TWlXnNG7n>u9LICDD=vtpZ@5taioY2+IfPIJcJBmS3ls(0c}9aQ#`Wg8A%d?$KH7
o0u7`&31D5pT))`?oVkf?#=yllbam={N(Lyv#)qCO}k_3+WC5p=bpP@Q|cQnGzPEC5uSgZ<~W)@0`-
J7aqEXii$moI@33e$OfJ&2;(1FJ89t*5cnKuHuF583KiUVEm#6x?ag~`qe|b}-
w;0)wj=5FP{>@emmQG_2rFI%4>8`HI0i2)kV8Ip-
RQ#KsP3qL0Wa%|_h^0&f7z(-pbtgn>L?1hxIMLby1)C5$U0-Jfo@{Y^p<twgQU(Brn!mkUMZb-wzVWLmK9;w*#Z)ZS#4KP&vH!3`
4L&`)qa>SBH^~NCQK8#bf+>_OMbWQd3$q4JurMl(Q_`VO>m(4f?xP=YPxSZC?Pv3>ubKTXHnE^rr+w}1C+zhiJ!7vf-
0L~LBVK#<kCt`2hx9kt+c-J;@w%rzT?Salzk!-
QRi=ulb2hOt=F<55Axjk!V(!uJa{6U|#is6gkGxJHOk;xs69rY@n1Q}wjaI$#KQv=qvAw(*UmzvBS1Z*`cGs+Z9G2RSFx6%SGOro
lqCG#Q8d~Q)ml@fv25mr_FfE7v#d@=P*MT)A;qf)tiH@3U$K5FoQBLYfI~=L=M#H_JqP~?myGl4@E0{G7*sT!xA;))8=-
X?Mpd{^N_@0$Pl4dI@lDK>BW>idXW>F;2Gax_0?I0lE+!kzj;bvu8_4^AYQ+%}qY-fKM&v$M~t}H#YiL;Zlucz~12S7n2-
u|{&^TUkR{NX^`sfKP<>lBuI@Z83<+r*%~ajE8s?FDwM^PE=3y*l8sl@hPt)bniRxDQZts{1E3?)C*UGi%<jexp~fiKumr;?L&0e
8El!!j@~8C(yd>?;w2-
^_hz8^pKzZ1_8#kh!2nZx+~84L4P%`sEF0`LEn5_ViDi}XrX;k<vQYdF49<koU?Cc(8Rse2=!8lHJvFmo6rYbSPWaUZ<nj9SY-
I5Uh&##YT}IzI<`l^QA<W6JHod|8k{l24(kbNUO{l`6~}lCB<`5R8Vl79zfl`Qop$aJA>if-ZW{OP9!-
PB>D|oksdm@9p$9K~=}TtPJ$|F5I53U*n%`>*#G)0i5;Zy6u06cAKLxigu$&`)qf#itakrdC{|_kC7@!y6H-&E7-
t*$RqO?u}{js}Stj^ANo0)boL&CZF5&>uHf$fW|s&q+Zwd;&_a3}B>5iPBrNg8M}n~{k|cZ8ZFz9uyru)OW?Ze2B@;mg!mBGjO?m
mtloIeR@}jVR88_7U9w-
wQiac=x?E35qPCXsBN^VOZESf<d9b$t3&_y%!n!xT5bcbml@h9ddMR`Os@!9i?uJ;P)&6GKwB3lplj(|4fBlEXZ3&#TL5y`FM*AL
}f6-bN7CRMDD^!k7weSi4WT(f9wu-LzyzAhBA$VkTJ`wP$Jg&Izm_|2caK(jqC5|z?vgd{rw-
g8=Y*{$5h_2C4Lh^pTQzE(YT+0=r@J>I6%gw|H;vgcRIio9MAb!**SZ|t$9Tu-
U0P&{^a4ZQ!z?9>NHC8)YSC@i_0~tw?1|C%wh@{60`46roT2JrTLk|o80(7=dBj(M1MEseGEQ7_zzG^0|XQR000O8001EX7*D0l`
w##C;3NP53jhEBQ)P5?X>Mn8E^v9hTFq`7$#&lJDGHp$NB~92k|ld&Spg+-
Y~Cx03Q5h}34#zsc9HC1v%9CNTQu*$KsMP0L6%trxbKih$`jm2$oHM9Zc-lK$tH*wVs~}bsZ;0oJEz=iHgC!}iPS7h=kY?#Gph!<
NjnRZ7MDsViCQGtR41I^3Y`{CCGoRSOJhyD*=#l%bDOQzWHK*{(wfOc#p^t?h0<x76}pJAtkL*J`CZo9u8eJ~q1o8DC`_uRTQ!>5
I4|6>XMsefoIJ^GHjfk2&bL^95SeMYP{+!e#As&@+v<<T<jQ=~vm)85EH%oNvn9C0Q=F<|89OEG8{OW`(+BlleXkQ|$joh)7Uol-
W=mZ(Za;R$lYST9oBpUxPU)JtE|Wq%>!dVJ<Wek+DxI;FtPbw8s7%bQyd7ef?>kR-<H=2D)SEmF??`Z26uG-RKGu2M&LCDDw`bY<
`1w_{o_;^*_GIoNFOFVkN9#C^cVEZ7`^Vm}GkzNOFz2NGX7{Ck-y1xQF?w-Q4~~8sVa4QeIJkf0r-
O#VzvfR_skAja&9;<QGo9;cVw83+7R};-x=@?Ut{epD;>f5mguSqO-Tue4=}8Su4rz;gjY@R7DD}dqY+g&}Tc_5>IgIWW-
5APj7CUpPpuI?K;$kT)tZ|Ss*oh()nL@`2G>Hv1OV~zSDCjUXCNj~ESU0Pcz7dAC!x>g4dZ(gH!RUlonOgG;G*_5N&5fpQx)!#ZV
`XNY3dAyMbG?R0wB7FZ=+6UpLV{fA^%S<5l@twxx6xZKE|^fdfPuU?j9ZC424ZeWe-
KLW28y<z3?Q=w#$22(+Ret!e#V2r-DLQ5*BecG51pI49!+y>OS9ARc-
ZUQhf$@zQP^Q49O%?-V4#~N>^_KZYOsNV(v8&+222}fYs8<$2R3mUVKp_HtxO6bky;9|<71HtS$N_)FO-Y_Y%0~uWDtYpAS4`|fS
V*<W6LsKrC7f^&+Xu0-22mb@?-y@JNS`SO#gbc*)uH6Dw9Te79*}uI|%~DGl{Dye0);cL>-9H_Nk^EUtzI_-en&<<B#;4V|wv1KP
N`QO|v0BHQLQs^Tba4`i@Mx#(n2clVR`i?xzW84M+5%(~}b!4vX*la3zZV{A5S(LvJ$b|3l9^9Vd5t<4*ssCQ{LW1OCwO_J)(*a5
xy&pS?T2IzKs~*4FwH%?HL9+{fw-MIGc~En^O~;1v=CADjyYgVT(&Eb)gCtLcv!EBb>6Zg&3N?gIkF<I}k2<L$}G$xD0NMU&H$hK
$^FhLiD_k?HKh^Xm+3CUQajSppqdH7$z*GN&DE)hvl;D+ZMv36Vzs?oK!&l^3h&Sa44hUBccrbhSKA62@)o;7D0QNx+qyifooQK0
+sh;ZKu?&JVxC8v;LEe5-EsY<2uV0sajpgIa%|nzx<*otT{X3v=-
LzWAEDDFJO44jC;gi@YrG5E&<_kWr%6xsQqt`W_Fu1Cb}xeDAG|bmPLTB`PuG6d7V*0s;8hoVjnDzu}`^Ln^eWQ8@b46dQvWY~$J
TDA*j0bAce|7)SBDgkF58(fgs&mT8KZ(|{9v81_b^$<t%EGwx0Lhy%kPIu!INchYOqs@J>18Vp2L2%}|K8$UC69jut?uivXzmvu%
`CPJ{0kmC*;J|cc)qgQQ-HluQS#5k|h$cJr;$nBghC|S~yRv&uf>O7T=bcO^F&AmYKXw5n<!N)rLId0rO!7}eBz5Br*`k45ukNm(
O>8g3DzP&0IM>5e*KZ>LG&GWPK)3+DrZ{MDses^|y@#ggPdGq?OfBConx;n0AUw_*QY3lc=oSdJZzB+w<`u5e?#oLPuQ2Fow{Fko
~0km<y%gouy>o?!Mee>q+>$8jVH)Q5t|NSMM&pi1MCIKZU#x;ih+mDlv<NJ`XC?Y_@PEcX0_(`x+tu|SF@9oL8)q{D)OyCA}4`_%
)l(rjBcoPr+_rqhM7w)ogq#m`^AdxTKrMk+m+wJz%aej>tACXOACLCVA^5ghbc)-
9#7`WifeoAzRdDH8bx{CRy<R8aBGw7DT#Hcb@PW?~LA4tI=PbJ2Z&>i&3{j^%b72el44|_GQ8MCjBHRt_(nH7c;r%5(j{lYilX9j
n>?vw?P!PT+6TpjOCQ3nv&-WmX&9Hz@SbA1T1w_ue*uvka75r%-`-
Zv{ec9d^HI&J#1%fTQk%of&R`B+>g*H=mGXW;kh7z2viW?z250M>n<ff0*^b9wOJ!*feTu{aV{V2?R{OlG-HAs};_S$u|j!_VW~M
1Hw^yM}f41#V(CKq<qYNPG#s%EL5^w(?;8xcmhPEW9;L7lmFCm<aTzxp?zA*i&<*TwQBe`B(rD8?R7JfL7O|N5<kS(K#j7dZD|P$
gL7ng_37vf)qLhA_;;Z0`n|O%5{p-
Bh{n#T&l0Ro!HA?|MDOIyys@>AfBr&5PLwggj2$3wX9WrVGTu?N0S)GYvcDQ@B|bVfAZw%ersL4Z*IEdU=U%F*Q#BYFdn}Y^Oo12
{^?Yv$V;QUgVa~cVjT`I8fmM6&s<31a7}_}5q!HLb)iQmK2QJ?=YVm*@fD<WTcF@|g)9Z`Gbc`DI-
@^|B^XE4X29V}8jr+hSWw%a3B?2iU{Rb-t)5}ox`gnj2J$KW+8ve-
p^25yQa^hLg7`Bg?2;{~CV`w;CDBA@APzRS@I3ennU)+x&eL)|B`TRWB#GOsWWL1Ww(236ZT*O%omYpIw829;*&}7S&HS@Q`h~a}
w|IjxIzZS&v2`*%2+2^_)k7;396oU)y)0VHxAGbi+#w8+4&l_v(U}JtGfe|koq0iGQveS2)(?tE`R>bvS&}({-w_BhZ2(E-
!Z2%^x&W4PBct+WhGIr!^(H&hX<dT^!dh5peSNrHIUNKS&$rl+^_de|IsqbxwqpN~(Ty%<Jg<cD$cQz;;QT2T05B;y8a(vCG8A>-
m{?#LyYnke^PI7BAX$f}BNc)VlWSH-L3LRw<#CdP5-%$g1g<4*Lx(9IDS-2(vEt*R`FgXO`58fsA<FetAV!_kfN)zE00IuxBo-
{`L3@EHaA5YQ$qr1YV54BTW4ZoL5@_tb&)26(21(Hl+^WTcOIYIRRSqTOOH@~6TRhawmS)W&n&%6AFHnZjBdLkDx+Nz|ljIZGU$)
WSn1oBw8**a=Gn#2K18B(uR;NM$NF~!Zf2NCq#ThtgLak4}TtuN`*G_zZPna&~P*11UJjdFbehRGZ$6<Ltn_0n<G0zy0bh=fd3<@
M7*Wf9HNef83NTvB8BE>s@M1>IAP4D}`uty5wPYM9fsDr72lnsb%%yi<6wzDNGV?_EE_p2&*7}F?NTDgCcOH~=5-
wlMk5r!(x;TU46)WVO9el&TM6xMfOybY#;h{IvIEsxuJaSG9CIEuqAUOr#$0{7(x))!U^J_dmXzYT=uF~b-
wT7pWDot*Ph>}w|oF~A%lHlFzy<QOVM{2Pe*Wvr0K+=~tfwEmb#pnzA+vfO}=8xgmx+Gi1(hR*$2NJA<_ExjWcb(Dq13(Z_Y30{K
Lhh|pQ8<Ne!;b4{G!*S8}1}FWRxjLhS*O~Pq!>N6Kl?Dj;^-
U`lOBDKVg^ZoG+dBe0DXB#5o0U69G*WPZ#H6aJ+UhBfwBHYuSfG4Wjgo>`hwhQDyh~g^#4zuG0;m<xm|ID`_v+}>pH3}I0fESQD2
5TM*??!HlLYcrU&4#`mWhYrBljLhGggEdmh{+e#cl@`dJnxj-
;=e>TZf_usofxcs_bDf_H?A_8*l;Q#ciKHBfV9;5rUCA9&=RUEJl&*;yDZgLn!{b_dPt&KpfS`_Fuw&7jv(aDhgu>YuD;TQesLj#
K_tQk<fMV4JoRNpODu-
Y3AiipL}Bpt(6qK(1#3bm7|JX`pEN38CxUgqvUQOrmS6L>xA1SaHiA~V?v$rqnCoKx^5&#?SzcLOz$UzqqfKb0*;)SjYW7e-
}a6wPUw9gW6tAPz!0p}W48jxNwabhoJxR&s1qxY8D=7=8JT6r6;8-d^UhOB1Nf-ajck`m8z*3qJ>JEj*>1IZlb~Ke*eNo}jmR=hS
`XiFn5Y@xAVol5$MzCgDRe6k0}xLF6MMdUAxV5CH?w$-z(i}2XvjrwyPhI(h1M$q(D$?@FgK*-
X+PPAd@)WcD<=NhGhGi#DX0oTK(9VTXy%D!mKaZnyddGP8CJcheFP=twg=rx$~KP#{lyCz!g--JR&f*xryu(b4tzn^Qa?NX-RgD1
kV{K?$19X5+*W|+d6ocVR&gj{?N}K2b(S6mxGP<1L8IHW(4US($tD85AOWYP?IN(RvK6rnBxAkWBTWM`v{8ei#AS8DEvc(~J7H6n
^F$tiSTx0AX~ozimwFVj(KbT-LoU+6;)o_--1GQTWw9PrFxinUYYMx4Cz5*aTcoQvcfqznfKrwq!^uHM0ol~O@+h9qD}YWX2{1>7
cXtpTNidFat}|7RN{KDGGt;Uw$y^;!?Z!unfQ~8*Kvvv-jcLu1-LpLAegQ@siz*Z5d5>DpZug-9c8uN9V*?-
N1M;b%5TR_y@nmifZxa?1?S6R=v43Y%wGM!8=5v5?Z-
S1ck|xV0#LAe(5QwdX!+MSso&L%IPkRxw+0A^6yduM>8Am&kOqe^Ofn@7%(EPimk0s0(Au(4=D!bi<J7iQ-7d%qO$xth-
+?R)(?Lcml_JS@<o4rXBsPfYBnO9`qO_3adkPv9-
R?f#&_%R@}TtIkdL4jJZYCWvlio}aj+<|LWkc3?=_A3@<cOyo}2`n&p)ddn0mR@M8zRFo17t{>zutLR+b-
KcNdsHM+va?DH_PD@$Td(kuHKmiT4dIhyDHeH+p#%=+GdS}k1L#8l9z1&}>OzF6f~2p9{1*{S?CONzi^oSsy}DE&$kFN#qrrp9rg
Ah{wIA1tUD;CI1qLu%b5NAzTK)Q~@14$h_51m=gp`19s_i7Gi0cC7c_~7G;reAiJk-
9M8@;ChIbWIjI4S2D8o2=%o03X)R+N~8Fdcg!T7TiduKb0JJI{!GB7132TsD4{-_KP`MH;HUVL?5zn|hN?w~fx--QdSwcQWpL814
Gcc{8+rm#^xl)B5SGetKO$o!3tn)zhy1RgJJ=Sv}{re)P@2nn3+jCe>3`KP7SX6z(^wS62c!*lqQy2}o;B>Pdw~eOtZNq|CbBvi_
FtDDSO~S7x_=%@lKT^~@gOj;GzuWi8WPN4REo?~^p^_TCx7_Fmast9e}4N0EkT&5rMd*5B9<tzX!It6wPj`o-
=R)K6UZxzYGx(BGMeXvpu5Pd9gi+ds;;3CiJ{ez)6unDieew>^J%_kU?o|DQJVLZW-JiC#$Q^WOgo`OU@k7q{@=AYR4(_UwRxp|$
%T6o=LAED)>7eV@Y<eW!Rs4p`0$D`2fJ_XxMjCv<V3A^zu#OCToh!^=!WGQ)-p2sUdXP3bGDgYFG#zD>A(M-
sQuq1^mdwC{VPQRhRix}OexS%$6SaP`Oz2_P6lTcWqvOqyxc{}4D}%gB840q(F-k@daR-tA!6o!s^B`@B4U&HrBT+xtcKjQmdFFd
<o0JNW&-
O1Zkce9bHCYQnHL>Wz6PCzq^E<Qr4amZeJJ17ag8isoVCe*jQR0Rj{Q6aWAK2mk;8Apm2ut1Yqv007Mh000jF0000000000005)`
00000OmAahY-MvVWo|BcVQp+sO928D0~7!N00;m803iS!(toyO1pok}4FCWS00000000000001_0p9}v08DRVVQgh{FLHG*d0}mA
P)h*<6ay3h000O8001EX1XvIET?GIDuMGeI4*&oF0000000000qycaV002yHV_|G%b1!vkE_q>XY*0%90u%!j000080000X0E8@I
<xB?v0ACXT03QGV00000000000Hgu>4gdg8aAj^mXJu}5Ole{-MsIR$VRSE2X=7+YZ(?~aaCuNm0Rj{Q6aWAK2mk;8App1Y1Ri4-
005j;001EX0000000000005)`gBAb)PjF>!L1$%dbWCYtFGg>2ZDDjTRAqQ{Qe|#rWpXZXc~DCM0u%!j000080000X0Okhw{v`ka
03!eZ044wc00000000000HgsWE&u>eaAj^mXJu}5Ole{-
RBvx=b1y=5X>4?9ZZBV7X>MtBUtcb8c~DCM0u%!j000080000X0A4l0oqh}e0BkJ)04)Fj00000000000HgtqE&u>eaAj^mXJu}5
Ole{-RBvx=b1y=5X>4?9ZZBhRZggdMbYE>@ZeeF-axQRrP)h*<6ay3h000O8001EX3ld0|Bmw{cHUt0wA^-
pY0000000000qybku002*LWo|)dWo~p#X<{!_Z*OdKFG6)`Y;<XEFJx(EW-f4fP)h*<6ay3h000O8001EXctFwnBLn~d-U<K!A^-
pY0000000000qyf7<002*LWo|)dWo~p#X<{!_Z*OdKFG6)`Y;<XEFJ)wDbS`jtP)h*<6ay3h000O8001EXKWC9n0|o#9ju8L=EdT
%j0000000000qyZj6002*LWo|)dWo~p#X<{!_Z*OdKFG6)`Y;<XEFK1<RUvgz|Y<XX8Wn^h#E^v8JO928D0~7!N00;m803iTXyVg
?s1ONa-
4*&o!00000000000001_0c=PB08embZb4^dZgfm(VlPy0Z)|ffLUn0ubZKrcXJvF>a%FIAd0%a1b8}&5WiD`eP)h*<6ay3h000O8
001EXvnj$_!vX*R-Uk2xCjbBd0000000000qye-
|002*LWo|)dWo~p#X<{!_Z*OdKFG6)`Y;<XEFKA_Ka9?z9Z)`4bc~DCM0u%!j000080000X0I5><?u7;b04Wgw05Sjo000000000
00HguDPyhf=aAj^mXJu}5Ole{-
RBvx=b1y=5X>4?9ZZB|obZBpGUvy<`WoL3>ZC_=0Wn(UIc~DCM0u%!j000080000X0L*X$qx%5>05k*u04D$d00000000000Hgtt
R{#J{aAj^mXJu}5Ole{-
RBvx=b1y=5X>4?9ZZC3WVPs!sX>4UKaCuNm0Rj{Q6aWAK2mk;8AppaqBW?Kw005s4001Na0000000000005)`(OCchPjF>!L1$%d
bWCYtFH~=DY;!L{b!lvLX>KoaWn*D%Y%XwlP)h*<6ay3h000O8001EX$niZ$$^-
xa0t)~DCIA2c0000000000qyY?I002*LWo|)dWo~p#X<{!_Z*OdKFG6)`Y;<XEFLGsVWo=?*axQRrP)h*<6ay3h000O8001EXo9i
#pCj$Tg00#g7C;$Ke0000000000qyZXb002*LWo|)dWo~p#X<{!_Z*OdKFG6)`Y;<XEFLHHmUvPPJXm4&VaCuNm0Rj{Q6aWAK2mk
;8AplOoE4tzW001`z001KZ0000000000005)`hiCu*PjF>!L1$%dbWCYtFH~=DY;!L{b!lvLX>KobXk~0{E^v8JO928D0~7!N00;
m803iVGIIf#y1ONas3jhEu00000000000001_0jg^N08embZb4^dZgfm(VlPy0Z)|ffLUn0ubZKrcbZ1{@WprO{Wpi_3XJvCPaCu
Nm0Rj{Q6aWAK2mk;8Api%o^QZCz008w3001xm0000000000005)`S#SUVPjF>!L1$%dbWCYtFH~=DY;!L{b!lvLX>KocXJ2z=VRB
<=Uu|V`b75y?b1rasP)h*<6ay3h000O8001EXssMM(jRXJyC<*`oCIA2c0000000000qyd?A002*LWo|)dWo~p#X<{!_Z*OdKFG6
)`Y;<XEFLY>WZfj|7XD)DgP)h*<6ay3h000O8001EX7%L1~F984m{Q&>~CIA2c0000000000qycJr002*LWo|)dWo~p#X<{!_Z*O
dKFG6)`Y;<XEFLY^bWnXS@cP?;wP)h*<6ay3h000O8001EXs7{gnkput$a0~zdA^-
pY0000000000qygP~002*LWo|)dWo~p#X<{!_Z*OdKFG6)`Y;<XEFLZBYZ!U0oP)h*<6ay3h000O8001EX6y)NQX9WNNNDKe~Cjb
Bd0000000000qyesg002*LWo|)dWo~p#X<{!_Z*OdKFG6)`Y;<XEFLz~PUuI==V`wgLc~DCM0u%!j000080000X05F0nqw)p-
0JabS04M+e00000000000Hgt0h5!IhaAj^mXJu}5Ole{-
RBvx=b1y=5X>4?9ZZCIbVqbG*VRB<=E^v8JO928D0~7!N00;m803iT5q@w+z0ssK71poje00000000000001_0g{aX08embZb4^d
Zgfm(VlPy0Z)|ffLUn0ubZKrccXDZTWiD`eP)h*<6ay3h000O8001EX<_7ovB>(^bBLDyZB>(^b0000000000qycr1002*LWo|)d
Wo~p#X<{!_Z*OdKFGF>6bZ>1hUtei%X>?y-E^v8JO928D0~7!N00;m803iTPTu}fs0RR9M0ssId00000000000001_0o{-
Q08embZb4^dZgfm(VlPy0Z)|ffLv?d>Z*4DMWq4t2aBO8RaCuNm0Rj{Q6aWAK2mk;8ApkUeDY2yh002z^0015U0000000000005)
`Q<4AxPjF>!L1$%dbWCYtFH~=DY;!MPUukY>bYEXCaCuNm0Rj{Q6aWAK2mk;8ApiuGNKeWJ004p!000~S0000000000005)`G?M@
TPjF>!L1$%dbWCYtFH~=DY;!MTXk}w-
b1rasP)h*<6ay3h000O8001EXL`8cE7z_XaHYxxB8UO$Q0000000000qyadZ002*LWo|)dWo~p#X<{!_Z*OdKFJo_VWiD`eP)h*<
6ay3h000O8001EXv0E@m*8%_lBnAKg9{>OV0000000000qydPg002*LWo|)dWo~p#X<{!_Z*OdKFL!TpYjbd6V`VOIc~DCM0u%!j
000080000X01ezuTyY2h08SkM02crN00000000000Hgt&sQ>^^aAj^mXJu}5Ole{-
V{dMBWq5QhaCuNm0Rj{Q6aWAK2mk;8Apk<YYzoW{002xc000*N0000000000005)`Lb3n=PjF>!L1$%dbWCYtFKA(MZe??GE^v8J
O928D0~7!N00;m803iTn22Vav0001G0000Y00000000000001_0Ykw608embZb4^dZgfm(VlQxVZ+2;9WpZ;bUtei%X>?y-
E^v8JO928D0~7!N00;m803iVO5P1vj3;+NvF8}}_00000000000001_0n@<%08embZb4^dZgfm(VlQxVZ+2;9WpZ;bZ*XO9VQDUK
c~DCM0u%!j000080000X02oiD%=-`k0N^A501E&B00000000000Hgu_&Hw;YWps3DZfA2YaCuNm1qJ{B001QbB><2M001K300000
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
# Standard library
import asyncio
import html
import time
import uuid
from typing import Any
from urllib.parse import urlparse

# Third-party dependencies
import aiohttp

# SDK
import core.lib.loader.module_base as loader
import core.lib.loader.module_config as cfg
import core.lib.types as typ
from cubkit import load_strings
from utils.tg_emoji import tg_emoji_to_link

# Build config
from .Settings import (
    DEFAULT_BASE_URL,
    DEFAULT_MODEL,
    DEFAULT_STREAM,
    DEFAULT_SYSTEM_PROMPT,
    DEFAULT_TEMPERATURE,
    DEFAULT_TIMEOUT,
    DEFAULT_TOOL_RULES_ENABLED,
    DEFAULT_TOOL_TIMEOUT,
    MAX_DETAIL_CHARS,
    MAX_MODELS_LISTED,
    MAX_REPLY_CHARS,
    MODELS_ARG,
    MODELS_PAGE_SIZE,
    PROGRESS_UPDATE_INTERVAL,
    STREAM_UPDATE_INTERVAL,
    CUSTOM_EMOJI,
    DEFAULT_CONTEXT_ENABLED,
    DEFAULT_CONTEXT_SIZE,
    DEFAULT_CONTEXT_WINDOW,
    MAX_CONTEXT_MESSAGES,
    CONTEXT_RESET_ARGS,
    CHAT_ID,
)

# Tools / Plugins
from .OpenAgentLib.Tools import AgentPlugin, Tool, ToolContext, load_tools

# Harness: the agent loop and the provider (UI-agnostic)
from .OpenAgentLib.harness import AgentError, RunInput, run as harness_run
from .OpenAgentLib.providers import OpenAIProvider

# Chat context: DB history store + provider message building
from .OpenAgentLib.context import ContextStore, build_messages

# Text rendering
from .OpenAgentLib.Format.TextRender import RenderContext, render as render_text


class OpenAgent(loader.ModuleBase):
    name = "OpenAgent"
    version = "1.0.0"
    author = "@hairpin00"
    description: dict[str, str] = {
        "ru": "mini клиент LLM (OpenAI-совместимый API)",
        "en": "mini LLM client (OpenAI compatible API)",
    }

    strings = load_strings()

    # User config
    config = cfg.ModuleConfig(
        cfg.ConfigValue(
            "api_key",
            "",
            description=lambda self: self.strings("cfg_api_key"),
            validator=cfg.Secret(),
        ),
        cfg.ConfigValue(
            "model",
            DEFAULT_MODEL,
            description=lambda self: self.strings("cfg_model"),
            validator=cfg.String(),
        ),
        cfg.ConfigValue(
            "base_url",
            DEFAULT_BASE_URL,
            description=lambda self: self.strings("cfg_base_url"),
            validator=cfg.Link(),
        ),
        cfg.ConfigValue(
            "temperature",
            DEFAULT_TEMPERATURE,
            description=lambda self: self.strings("cfg_temperature"),
            validator=cfg.Float(min=0.0, max=2.0),
        ),
        cfg.ConfigValue(
            "timeout",
            DEFAULT_TIMEOUT,
            description=lambda self: self.strings("cfg_timeout"),
            validator=cfg.Integer(min=1, max=600),
        ),
        cfg.ConfigValue(
            "system_prompt",
            DEFAULT_SYSTEM_PROMPT,
            description=lambda self: self.strings("cfg_system_prompt"),
            validator=cfg.String(),
        ),
        cfg.ConfigValue(
            "context_enabled",
            DEFAULT_CONTEXT_ENABLED,
            description=lambda self: self.strings("cfg_context_enabled"),
            validator=cfg.Boolean(),
        ),
        cfg.ConfigValue(
            "context_size",
            DEFAULT_CONTEXT_SIZE,
            description=lambda self: self.strings("cfg_context_size"),
            validator=cfg.Integer(min=0, max=MAX_CONTEXT_MESSAGES),
        ),
        cfg.ConfigValue(
            "context_window",
            DEFAULT_CONTEXT_WINDOW,
            description=lambda self: self.strings("cfg_context_window"),
            validator=cfg.Integer(min=0, max=100_000_000),
        ),
        cfg.ConfigValue(
            "tool_rules",
            DEFAULT_TOOL_RULES_ENABLED,
            description=lambda self: self.strings("cfg_tool_rules"),
            validator=cfg.Boolean(),
        ),
        cfg.ConfigValue(
            "stream",
            DEFAULT_STREAM,
            description=lambda self: self.strings("cfg_stream"),
            validator=cfg.Boolean(),
        ),
    )

    _http: aiohttp.ClientSession | None = None
    _active_requests: dict[str, dict[str, Any]] = {}
    _models_cache: tuple[str, ...] = ()
    _tools: list[Tool] = []
    _provider: OpenAIProvider | None = None
    _context_store: ContextStore | None = None

    async def on_load(self) -> None:
        await super().on_load()

        self._active_requests = {}
        self._models_cache = ()
        self._tools = load_tools(self.log)
        self._context_store = ContextStore(self.db, self.name.lower(), self.log)
        self.log.debug("OpenAgent tools loaded: %s", len(self._tools))

        me = await self.client.get_me()
        if me.premium is False:
            for key, html_emoji in CUSTOM_EMOJI.items():
                CUSTOM_EMOJI[key] = tg_emoji_to_link(html_emoji)

        # One shared session for all requests, closed in on_unload
        self._http = aiohttp.ClientSession()

    async def on_unload(self) -> None:
        for state in self._active_requests.values():
            state["task"].cancel()
        self._active_requests.clear()
        self._tools = []
        self._provider = None
        self._context_store = None

        if self._http is not None:
            await self._http.close()
            self._http = None
        await super().on_unload()

    @property
    def provider(self) -> OpenAIProvider:
        """The active provider; built once the http session exists."""
        if self._provider is None:
            self._provider = OpenAIProvider(
                self._http, self.config, self.strings, self.log
            )
        return self._provider

    async def _chat_with_tools(
        self,
        prompt: str,
        history: list[dict[str, str]],
        state: dict[str, Any],
        message: Any,
        event: typ.Event,
        chat_id: int | str,
    ) -> str:
        """Thin UI adapter over the provider-agnostic harness loop.

        The harness drives the chat <-> tool steps; this method only
        translates its events into rich-message updates.
        """

        async def on_event(name: str, payload: dict[str, Any]) -> None:
            # Any harness event (tool_start / tool_done) re-renders the
            # progress message with the current state (RUN timer, pills).
            await self._edit_rich(message, self._build_progress_text(state))

        async def on_usage(usage: dict[str, Any]) -> None:
            # Latest provider step's token counts for the token_stats widget
            state["tokens"] = usage
            # Tokens billed by this step; the header pill adds them to the
            # chat total saved by the earlier requests
            total = int(usage.get("total_tokens") or 0) or (
                int(usage.get("prompt_tokens") or 0)
                + int(usage.get("completion_tokens") or 0)
            )
            state["request_tokens"] = int(state.get("request_tokens") or 0) + total

        async def on_stream(text: str) -> None:
            # Picked up by the refresh loop (_wait_for_reply); no edit here,
            # so a fast stream cannot flood Telegram with message edits
            state["stream_text"] = text

        tool_context = ToolContext(
            logger=self.log,
            http=self._http,
            event=event,
            chat_id=chat_id,
            client=self.client,
            tools=self._tools,
            state=state,
        )
        return await harness_run(
            RunInput(
                messages=build_messages(
                    self.config["system_prompt"],
                    self.config["tool_rules"],
                    self._tools,
                    history,
                    prompt,
                ),
                tools=self._tools,
                tool_context=tool_context,
                state=state,
                provider=self.provider,
                logger=self.log,
                strings=self.strings,
                on_event=on_event,
                on_usage=on_usage,
                tool_timeout=DEFAULT_TOOL_TIMEOUT,
                on_stream=on_stream if self.config["stream"] else None,
            )
        )

    @staticmethod
    def _clip(text: str) -> str:
        text = str(text)
        if len(text) <= MAX_REPLY_CHARS:
            return text
        return text[:MAX_REPLY_CHARS].rstrip() + "…"

    def _provider_label(self) -> str:
        raw = str(self.config["base_url"]).strip()
        parsed = urlparse(raw)
        label = parsed.netloc or parsed.path or raw or "provider"
        if len(label) > 40:
            label = label[:39] + "…"
        return label

    def _header(self, state: dict[str, Any], kind: str) -> str:
        return render_text(self, "status_header", RenderContext(state=state, kind=kind))

    def _guest_mention(self) -> str:
        username = (
            str(self.kernel.config.get("inline_bot_username") or "").strip().lstrip("@")
        )
        return f"@{username}" if username else "@bot"

    def _build_progress_text(self, state: dict[str, Any]) -> str:
        return render_text(
            self,
            "progress",
            RenderContext(kind="running", state=state),
        )

    def _build_result_text(
        self,
        state: dict[str, Any],
        kind: str,
        text: str = "",
        message: typ.Message = None,
    ) -> str:
        fmt = "cancelled" if kind == "cancelled" else "result"
        # Kept so a tool button can re-render the final message on click
        state["last_result"] = {"kind": kind, "text": text, "message": message}
        return render_text(
            self,
            fmt,
            RenderContext(
                kind=kind,
                text=text,
                copy_text=text,
                state=state,
                extra={"message": message},
            ),
        )

    def _build_error_text(self, text: str, detail: str | None = None) -> str:
        state = {"error_detail": detail} if detail else None
        return render_text(
            self,
            "error_standalone",
            RenderContext(kind="error", text=text, state=state),
        )

    def _build_usage_text(self) -> str:
        mention = self._guest_mention()
        command = html.escape(f"{mention} agent ", quote=True)
        return render_text(
            self,
            "usage",
            RenderContext(copy_text=command, label=self.strings("btn_copy_prompt")),
        )

    def _render_models(self, state: dict[str, Any]) -> str:
        """Render one page of the model list; ``state`` keeps the full list."""
        models = list(state.get("models") or [])
        pages = max((len(models) + MODELS_PAGE_SIZE - 1) // MODELS_PAGE_SIZE, 1)
        page = max(0, min(int(state.get("page") or 0), pages - 1))
        state["page"] = page
        start = page * MODELS_PAGE_SIZE
        return render_text(
            self,
            "models",
            RenderContext(
                state=state,
                extra={
                    "models": models[start : start + MODELS_PAGE_SIZE],
                    "page": page,
                    "pages": pages,
                },
            ),
        )

    async def _build_models_text(self) -> str:
        try:
            list_models = await self.provider.models()
        except AgentError as exc:
            return self._build_error_text(str(exc), detail=exc.detail)
        except Exception as exc:
            return self._build_error_text(
                self.strings("err_unexpected", error=str(exc))
            )

        self._models_cache = tuple(list_models)
        return self._render_models({"models": list(list_models), "page": 0})

    async def _edit_rich(self, message: Any, text: str) -> bool:
        try:
            await message.edit_rich(text)
            return True
        except Exception as exc:
            self.log.warning("OpenAgent rich message edit failed: %s", exc)
            # Fallback: if edit failed because of invalid Rich HTML syntax, try fallback formatting
            try:
                # Replace content inside body or render clean escaped text
                plain_escaped = f"<blockquote><b>⚠️ HTML Error:</b> <code>{html.escape(str(exc))}</code></blockquote>\n<pre><code>{html.escape(text)}</code></pre>"
                await message.edit_rich(plain_escaped)
                return True
            except Exception as fallback_exc:
                self.log.debug(
                    "OpenAgent message update fallback failed: %s", fallback_exc
                )
                return False

    async def _wait_for_reply(
        self, task: asyncio.Task[str], message: Any, state: dict[str, Any]
    ) -> str:
        """Wait for the provider while refreshing the header and the live answer."""
        last_len = -1
        last_edit = 0.0
        while True:
            streaming = bool(state.get("stream_text"))
            interval = STREAM_UPDATE_INTERVAL if streaming else PROGRESS_UPDATE_INTERVAL
            timeout = interval if state["ui_alive"] else None
            done, _ = await asyncio.wait({task}, timeout=timeout)
            if done:
                return task.result()

            if streaming:
                # Nothing new in the answer: the header timer alone can wait
                # for the normal (slower) refresh
                length = len(state["stream_text"])
                now = time.perf_counter()
                if length == last_len and now - last_edit < PROGRESS_UPDATE_INTERVAL:
                    continue
                last_len, last_edit = length, now

            try:
                progress_text = self._build_progress_text(state)
                await message.edit_rich(progress_text)
                state["ui_errors"] = 0
            except Exception as exc:
                # If rich rendering or HTML in stream fails, fallback to escaped preview or report
                state["ui_errors"] = int(state.get("ui_errors") or 0) + 1
                self.log.debug("OpenAgent progress update failed: %s", exc)
                # If error is due to bad markup in live stream, don't let UI freeze
                if streaming:
                    try:
                        # Clean stream text in state if it's breaking HTML
                        fallback_text = self._build_progress_text(state)
                        await message.edit_rich(fallback_text)
                    except Exception:
                        pass
                if not streaming or state["ui_errors"] >= 3:
                    state["ui_alive"] = False

    def _build_notice_text(
        self, text: str, style: str = "primary", label: str | None = None
    ) -> str:
        return render_text(
            self,
            "notice",
            RenderContext(
                kind="notice",
                text=text,
                extra={"label": label or self.strings("status_done"), "style": style},
            ),
        )

    async def _handle_context_reset(self, event: typ.Message) -> str:
        chat_id = "global"
        if chat_id is None:
            return self._build_notice_text(
                self.strings("err_context_no_chat"),
                style="danger",
                label=self.strings("status_error"),
            )
        removed = await self._context_store.clear(chat_id)
        text = (
            self.strings("context_cleared", count=removed)
            if removed
            else self.strings("context_empty")
        )
        return self._build_notice_text(text)

    @loader.callback()
    async def on_cancel_request(self, call: typ.InlineMessage, data=None) -> None:
        if not call.sender_id == self.kernel.ADMIN_ID:
            return

        state = self._active_requests.get(data) if data else None
        if state is None or state["task"].done():
            await call.answer(self.strings("already_finished"))
            return
        state["cancelled"] = True
        state["task"].cancel()
        await call.answer(self.strings("cancelling"))

    async def on_supplement(self, event: typ.InlineMessage, text, data=None) -> None:
        """Queue extra user text for a running request (Supplement input button)."""
        if getattr(event, "user_id", None) != self.kernel.ADMIN_ID:
            return

        text = str(text or "").strip()
        state = self._active_requests.get(data) if data else None
        if not text or state is None or state["task"].done():
            return
        # The harness drains this queue before the next provider step
        state.setdefault("supplements", []).append(text)

    @loader.callback()
    async def on_tool_args(self, call: typ.InlineMessage, data=None) -> None:
        """Toggle the details block (tool, description, args, output, time)."""
        if not call.sender_id == self.kernel.ADMIN_ID:
            return
        if not data:
            return

        state, entry = data
        entry["open"] = not entry.get("open")
        # Drop the cached buttons so they are rebuilt with the new style
        entry.pop("button", None)
        entry.pop("details_button", None)
        await call.answer()

        last = state.get("last_result")
        if last is None:
            # Still running: the next progress refresh renders the block
            return
        await self._edit_rich(
            call,
            self._build_result_text(state, last["kind"], last["text"], last["message"]),
        )

    @staticmethod
    def _repeat_prompt(state: dict[str, Any], from_history: bool) -> str:
        """Prompt shown by the current view, used by the Again button."""
        if from_history:
            history = state.get("history") or []
            total = len(history) // 2
            pos = int(state.get("history_pos", total - 1))
            if 0 <= pos < total:
                return str(history[2 * pos]["content"])
        return str(state.get("prompt") or "")

    @loader.callback()
    async def on_repeat_request(self, call: typ.InlineMessage, data=None) -> None:
        """Repeat the prompt of the exchange currently shown in the message."""
        if not call.sender_id == self.kernel.ADMIN_ID:
            return
        if not data:
            return

        state, from_history = data
        prompt = self._repeat_prompt(state, bool(from_history))
        if not prompt:
            await call.answer(self.strings("repeat_empty"))
            return

        await call.answer()
        # Re-run through the normal guest flow, editing the same message
        call.guest_args = prompt
        call.reply_rich = call.edit_rich
        call.reply = call.edit
        try:
            await self.guest_cmd_agent(call)
        except Exception as exc:
            await self.kernel.handle_error(
                exc, message="OpenAgent repeat request failed"
            )

    def _build_history_text(self, state: dict[str, Any]) -> str:
        """Render the exchange at ``state['history_pos']`` (the latest one is the normal result)."""
        history = state["history"]
        pos = state["history_pos"]
        total = len(history) // 2
        last = state.get("last_result")
        if pos == total - 1 and last is not None:
            return self._build_result_text(
                state, last["kind"], last["text"], last["message"]
            )
        return render_text(
            self,
            "history",
            RenderContext(
                kind="done",
                text=history[2 * pos + 1]["content"],
                state=state,
                extra={
                    "prompt": history[2 * pos]["content"],
                    "pos": pos,
                    "total": total,
                },
            ),
        )

    @loader.callback()
    async def on_history_scroll(self, call: typ.InlineMessage, data=None) -> None:
        """Back / Next through the saved exchanges, editing the message in place."""
        if not call.sender_id == self.kernel.ADMIN_ID:
            return
        if not data:
            return

        state, step = data
        total = len(state.get("history") or []) // 2
        pos = int(state.get("history_pos", total - 1)) + step
        if pos < 0:
            await call.answer(self.strings("history_first"))
            return
        if pos >= total:
            await call.answer(self.strings("history_last"))
            return

        state["history_pos"] = pos
        await call.answer()
        await self._edit_rich(call, self._build_history_text(state))

    @loader.callback()
    async def on_change_model(self, call: typ.InlineMessage, data=None) -> None:
        if not call.sender_id == self.kernel.ADMIN_ID:
            return

        if not data:
            return

        if isinstance(data, tuple) and len(data) == 2:
            state, model = data
            model = str(model)
        else:
            state, model = None, str(data)
        old_model = str(self.config["model"])
        self.config["model"] = model
        try:
            await self.kernel.save_module_config(self.name, self.config.to_dict())
        except Exception as exc:
            self.config["model"] = old_model
            self.log.error("OpenAgent config save failed: %s", exc)
            await call.answer(
                self.strings("err_config_save", error=str(exc)[:MAX_DETAIL_CHARS])
            )
            return

        self.kernel.store_module_config_schema(self.name, self.config)
        await call.answer(self.strings("model_changed", model=model))
        if state is not None:
            await self._edit_rich(call, self._render_models(state))
        elif self._models_cache:
            await self._edit_rich(
                call,
                self._render_models({"models": list(self._models_cache), "page": 0}),
            )

    @loader.callback()
    async def on_models_scroll(self, call: typ.InlineMessage, data=None) -> None:
        """Back / Next through the paginated model list."""
        if not call.sender_id == self.kernel.ADMIN_ID:
            return
        if not data:
            return

        state, step = data
        models = state.get("models") or []
        pages = max((len(models) + MODELS_PAGE_SIZE - 1) // MODELS_PAGE_SIZE, 1)
        page = int(state.get("page") or 0) + step
        if page < 0:
            await call.answer(self.strings("models_first"))
            return
        if page >= pages:
            await call.answer(self.strings("models_last"))
            return

        state["page"] = page
        await call.answer()
        await self._edit_rich(call, self._render_models(state))

    @loader.guest_command(
        "agent",
        doc_ru="<запрос> | models | reset - спросить LLM, показать модели, очистить контекст",
        doc_en="<prompt> | models | reset - ask the LLM, list models, clear context",
    )
    async def guest_cmd_agent(self, event: typ.Event) -> None:
        raw = event.guest_args or ""
        r = getattr(event, "message", None) or event
        try:
            reply = await r.get_reply_message()
        except AttributeError:
            reply = None

        msg = None
        if reply is not None:
            msg = reply.message

        file_text_parts: list[str] = []
        if msg is not None:
            # Handle document (file)
            if getattr(msg, "document", None):
                doc = msg.document
                # Only process text-based files (by mime type or extension)
                mime = getattr(doc, "mime_type", "") or ""
                name = getattr(doc, "file_name", "") or "file"
                is_text = (
                    mime.startswith("text/")
                    or mime
                    in (
                        "application/json",
                        "application/xml",
                        "application/javascript",
                        "application/x-python-code",
                    )
                    or name.lower().endswith(
                        (
                            ".txt",
                            ".md",
                            ".py",
                            ".js",
                            ".json",
                            ".xml",
                            ".html",
                            ".css",
                            ".csv",
                            ".log",
                            ".ini",
                            ".cfg",
                            ".yaml",
                            ".yml",
                            ".toml",
                            ".sh",
                            ".sql",
                        )
                    )
                )
                if is_text:
                    try:
                        file_bytes = await self.client.download_file(doc, bytes)
                        content = file_bytes.decode("utf-8", errors="replace")
                        file_text_parts.append(
                            f"\n\n--- Attached file: {name} ({len(content)} chars) ---\n{content}\n--- End of {name} ---"
                        )
                    except Exception as exc:
                        self.log.debug(
                            "OpenAgent failed to read attached document: %s", exc
                        )
                        file_text_parts.append(
                            f"\n\n[Attached file: {name} - could not read: {exc}]"
                        )
                else:
                    file_text_parts.append(
                        f"\n\n[Attached file: {name} (type: {mime or 'unknown'}) - binary file, not processed]"
                    )

            # Handle photo (image)
            elif getattr(msg, "photo", None):
                file_text_parts.append(
                    "\n\n[Attached image - vision support depends on the model/provider]"
                )

        # Combine prompt with file content
        if file_text_parts:
            raw = (raw + "".join(file_text_parts)).strip()

        if not raw:
            await event.reply_rich(self._build_usage_text())
            return

        if raw == MODELS_ARG:
            await event.reply_rich(await self._build_models_text())
            return

        if raw.strip().lower() in CONTEXT_RESET_ARGS:
            await event.reply_rich(await self._handle_context_reset(event))
            return

        if reply is not None:
            raw = raw + f"\n[reply context]:\n{reply.html_text}"

        start = time.perf_counter()
        request_id = uuid.uuid4().hex
        ttl = int(self.config["timeout"]) + 60
        state: dict[str, Any] = {
            "start": start,
            "model": str(self.config["model"]),
            "provider": self._provider_label(),
            "cancelled": False,
            "ui_alive": True,
            "prompt": raw,
            "tool": "",
            "tool_calls": 0,
            "context_window": int(self.config.get("context_window") or 0),
            "user_id": getattr(event, "sender_id", None)
            or getattr(getattr(event, "message", None), "sender_id", None),
        }
        try:
            cancel_button = self.Button.rich.inline(
                self.strings("btn_cancel"),
                self.on_cancel_request,
                data=request_id,
                style="danger",
                ttl=ttl,
                html_tag=True,
            )
            # TextRender's cancel_button module joins both into one row
            state["cancel_btn"] = cancel_button
            state["supplement_btn"] = self.Button.rich.input(
                self.strings("btn_supplement"),
                self.on_supplement,
                data=request_id,
                style="primary",
                ttl=ttl,
                html_tag=True,
            )

            message = await event.reply_rich(self._build_progress_text(state))

            chat_id = CHAT_ID
            context_enabled = chat_id is not None and bool(
                self.config["context_enabled"]
            )

            history = await self._context_store.load(chat_id) if context_enabled else []
            state["context_count"] = len(history) // 2
            # Tokens of the earlier requests in this chat (the pill adds the live one)
            state["chat_tokens_base"] = (
                await self._context_store.load_usage(chat_id) if context_enabled else 0
            )
            if context_enabled:
                # Snapshot for the pager: errors can still scroll back
                state["history"] = history
                state["history_pos"] = max(len(history) // 2 - 1, 0)
            task = asyncio.create_task(
                self._chat_with_tools(raw, history, state, message, event, chat_id)
            )
            state["task"] = task
            self._active_requests[request_id] = state

        except BaseException:
            task.cancel()
            self._active_requests.pop(request_id, None)
            raise

        if message is None:
            task.cancel()
            self._active_requests.pop(request_id, None)
            return

        try:
            text = await self._wait_for_reply(task, message, state)
        except asyncio.CancelledError:
            if not state["cancelled"]:
                raise
            await self._edit_rich(message, self._build_result_text(state, "cancelled"))
        except AgentError as exc:
            state["error_detail"] = exc.detail
            await self._edit_rich(
                message,
                self._build_result_text(state, "error", str(exc), message=message),
            )
        except Exception as exc:
            await self._edit_rich(
                message,
                self._build_result_text(
                    state,
                    "error",
                    self.strings("err_unexpected", error=str(exc)),
                ),
            )
        else:
            if context_enabled:
                state["context_count"] = await self._context_store.append(
                    chat_id, raw, text, state.get("exchange_tools") or None
                )
                # Snapshot for the history pager: stable even if later requests
                # append to the stored context
                state["history"] = await self._context_store.load(chat_id)
                state["history_pos"] = len(state["history"]) // 2 - 1
            await self._edit_rich(
                message, self._build_result_text(state, "done", text, message=message)
            )
        finally:
            self._active_requests.pop(request_id, None)
            if not task.done():
                task.cancel()
            # Spent tokens count even when the request failed or was cancelled
            spent = int(state.get("request_tokens") or 0)
            if context_enabled and spent:
                await self._context_store.add_usage(chat_id, spent)
