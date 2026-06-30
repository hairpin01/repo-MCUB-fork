import ast
import html
import json
from typing import Any

from core.lib.loader.module_base import ModuleBase, callback, command


class DBModMCUB(ModuleBase):
    name = "DBMod"
    version = "1.0.0"
    author = "@codrago_m, ported to MCUB API"
    description = {
        "en": "Interactive MCUB database browser/editor",
        "ru": "Редактор базы данных MCUB",
        "linux": "MCUB /var/lib database browser/editor",
        "rofl": "кринжовый ковырятель базы MCUB",
    }

    strings = {
        "en": {
            "del_text": "<b>Database</b>\n\nSelect a key to view",
            "deleted": "🗑 Key {key} deleted",
            "deleted_all": "🗑 Deleted {count} keys",
            "close_btn": "❌ Close",
            "back_btn": "⬅ Back",
            "del_btn": "🗑 Delete",
            "del_all_btn": "❌ Delete all",
            "edit_btn": "✏ Edit",
            "add_btn": "➕ Add",
            "not_found": "🔍 Key {key} not found",
            "invalid_key": "⚠ Invalid key",
            "saved": "✅ Saved: {path}",
            "added": "✅ Added: {path}",
            "input_key_value": "key value",
            "input_module_key_value": "module key value",
            "input_value": "value",
            "invalid_input": "⚠ Invalid input. Use: {usage}",
            "page": "📄 Page {current}/{total}",
            "module_not_found": "🔍 Module '{module}' not found in database",
            "confirm_delete": "⚠ Are you sure you want to delete this?",
            "view_path": "<b>Path: {path}</b>",
            "root_path": "Root",
            "value_display": "<b>Value:</b> <code>{value}</code>",
            "yes_btn": "✅ Yes",
            "no_btn": "❌ No",
            "list_item_display": "<b>List item [{index}]</b>",
        },
        "ru": {
            "del_text": "<b>База данных</b>\n\nВыберите ключ для просмотра",
            "deleted": "🗑 Ключ {key} удален",
            "deleted_all": "🗑 Удалено {count} ключей",
            "close_btn": "❌ Закрыть",
            "back_btn": "⬅ Назад",
            "del_btn": "🗑 Удалить",
            "del_all_btn": "❌ Удалить все",
            "edit_btn": "✏ Изменить",
            "add_btn": "➕ Добавить",
            "not_found": "🔍 Ключ {key} не найден",
            "invalid_key": "⚠ Некорректный ключ",
            "saved": "✅ Сохранено: {path}",
            "added": "✅ Добавлено: {path}",
            "input_key_value": "ключ значение",
            "input_module_key_value": "модуль ключ значение",
            "input_value": "значение",
            "invalid_input": "⚠ Некорректный ввод. Используйте: {usage}",
            "page": "📄 Страница {current}/{total}",
            "module_not_found": "🔍 Модуль '{module}' не найден в базе данных",
            "confirm_delete": "⚠ Вы уверены, что хотите удалить это?",
            "view_path": "<b>Путь: {path}</b>",
            "root_path": "Корень",
            "value_display": "<b>Значение:</b> <code>{value}</code>",
            "yes_btn": "✅ Да",
            "no_btn": "❌ Нет",
            "list_item_display": "<b>Элемент списка [{index}]</b>",
        },
        "linux": {
            "del_text": "<b>/var/lib/mcub/db</b>\n\nSelect inode to inspect",
            "deleted": "🗑 rm: removed key {key}",
            "deleted_all": "🗑 rm -rf: removed {count} keys",
            "close_btn": "❌ SIGTERM",
            "back_btn": "⬅ cd ..",
            "del_btn": "🗑 rm",
            "del_all_btn": "❌ rm -rf",
            "edit_btn": "✏ nano",
            "add_btn": "➕ touch",
            "not_found": "🔍 ENOENT: key {key} not found",
            "invalid_key": "⚠ EINVAL: invalid key",
            "saved": "✅ fsync: {path}",
            "added": "✅ created: {path}",
            "input_key_value": "key value",
            "input_module_key_value": "module key value",
            "input_value": "value",
            "invalid_input": "⚠ EINVAL. Usage: {usage}",
            "page": "📄 page {current}/{total}",
            "module_not_found": "🔍 module '{module}' not mounted in database",
            "confirm_delete": "⚠ sudo rm -rf this path?",
            "view_path": "<b>pwd: {path}</b>",
            "root_path": "/",
            "value_display": "<b>cat:</b> <code>{value}</code>",
            "yes_btn": "✅ yes",
            "no_btn": "❌ no",
            "list_item_display": "<b>argv[{index}]</b>",
        },
        "rofl": {
            "del_text": "<b>база данных</b>\n\nвыбери ключ, посмотрим чо там",
            "deleted": "🗑 ключ {key} удалён нахуй",
            "deleted_all": "🗑 удалено {count} ключей, чисто",
            "close_btn": "❌ закрыть",
            "back_btn": "⬅ назад в прошлое",
            "del_btn": "🗑 удалить",
            "del_all_btn": "❌ удалить всё нах",
            "edit_btn": "✏ едить",
            "add_btn": "➕ дабавить",
            "not_found": "🔍 ключ {key} куда-то пропал в лес",
            "invalid_key": "⚠ ключ какой-то хуесос",
            "saved": "✅ ок: {path}",
            "added": "✅ добавил: {path}",
            "input_key_value": "ключ значение",
            "input_module_key_value": "модуль ключ значение",
            "input_value": "значение",
            "invalid_input": "⚠ ввод не зашёл. надо так: {usage}",
            "page": "📄 страничка {current}/{total}",
            "module_not_found": "🔍 модуль '{module}' не найден, бывае",
            "confirm_delete": "⚠ точно удалить?\nизменение нельзя будет отменить потом",
            "view_path": "<b>путь бд: {path}</b>",
            "root_path": "рутированый",
            "value_display": "<b>значение:</b> <code>{value}</code>",
            "yes_btn": "✅ до",
            "no_btn": "❌ не",
            "list_item_display": "<b>элемент списка [{index}]</b>",
        },
    }

    def on_load(self) -> None:
        self.page_state: dict[tuple[Any, ...], int] = {}
        self.callback_events: dict[int, Any] = {}

    def s(self, key: str, **kwargs: Any) -> str:
        value = self.strings(key)
        if kwargs:
            return value.format(**kwargs)
        return value

    def _db_api(self):
        return getattr(self, "db", None) or getattr(self.kernel, "db_manager", None)

    async def _db_rows(self) -> list[tuple[str, str, str]]:
        rows = await self._db_api().db_query(
            "SELECT module, key, value FROM module_data ORDER BY module, key", ()
        )
        return [(row[0], row[1], row[2]) for row in rows]

    async def _module_keys(self, module: str) -> list[str]:
        return await self._db_api().db_get_module_keys(module)

    async def _module_exists(self, module: str) -> bool:
        rows = await self._db_api().db_query(
            "SELECT 1 FROM module_data WHERE module = ? LIMIT 1", (module,)
        )
        return bool(rows)

    async def _get_raw_value(self, module: str, key: str) -> str | None:
        return await self._db_api().db_get(module, key)

    async def _set_raw_value(self, module: str, key: str, value: Any) -> None:
        await self._db_api().db_set(module, key, value)

    async def _delete_raw_key(self, module: str, key: str) -> None:
        await self._db_api().db_delete(module, key)

    def _decode_value(self, value: str | None) -> Any:
        if value is None:
            return None
        stripped = value.strip()
        if not stripped:
            return value
        for parser in (ast.literal_eval, json.loads):
            try:
                parsed = parser(stripped)
            except Exception:
                continue
            if isinstance(parsed, (dict, list, tuple, str, int, float, bool, type(None))):
                return list(parsed) if isinstance(parsed, tuple) else parsed
        return value

    async def _root_data(self) -> dict[str, dict[str, Any]]:
        data: dict[str, dict[str, Any]] = {}
        for module, key, value in await self._db_rows():
            data.setdefault(module, {})[key] = self._decode_value(value)
        return data

    async def _get_data_at_path(self, key_path: list[Any]) -> Any:
        if not key_path:
            return await self._root_data()

        module = str(key_path[0])
        if not await self._module_exists(module):
            raise KeyError(module)
        if len(key_path) == 1:
            return {
                key: self._decode_value(await self._get_raw_value(module, key))
                for key in await self._module_keys(module)
            }

        key = str(key_path[1])
        raw_value = await self._get_raw_value(module, key)
        if raw_value is None:
            raise KeyError(key)

        current = self._decode_value(raw_value)
        for item in key_path[2:]:
            if isinstance(current, dict) and item in current:
                current = current[item]
            elif isinstance(current, list) and isinstance(item, int) and 0 <= item < len(current):
                current = current[item]
            else:
                raise KeyError(item)
        return current

    def _make_path_text(self, key_path: list[Any]) -> str:
        path = "/".join(map(str, key_path)) if key_path else self.s("root_path")
        return self.s("view_path", path=html.escape(path))

    def _make_list_item_path_text(self, key_path: list[Any], index: int) -> str:
        return self.s("list_item_display", index=index)

    def _value_text(self, header: str, value: Any) -> str:
        return f"{header}\n\n" + self.s("value_display", value=html.escape(str(value)))

    def _parse_input_value(self, text: str) -> Any:
        text = text.strip()
        if not text:
            return ""
        for parser in (ast.literal_eval, json.loads):
            try:
                return parser(text)
            except Exception:
                continue
        return text

    def _split_key_value(self, text: str) -> tuple[str, Any] | None:
        text = text.strip()
        if "=" in text:
            key, value = text.split("=", 1)
        else:
            parts = text.split(maxsplit=1)
            if len(parts) != 2:
                return None
            key, value = parts
        key = key.strip()
        if not key:
            return None
        return key, self._parse_input_value(value)

    def _display_path(self, key_path: list[Any]) -> str:
        return "/".join(map(str, key_path)) if key_path else self.s("root_path")

    async def _answer_callback(self, call, text: str) -> None:
        try:
            await call.answer(text)
        except Exception:
            pass

    def _event_user_id(self, event) -> int | None:
        for attr in ("sender_id", "user_id"):
            value = getattr(event, attr, None)
            if value is not None:
                try:
                    return int(value)
                except (TypeError, ValueError):
                    return None
        return None

    def _remember_callback_event(self, call) -> None:
        user_id = self._event_user_id(call)
        if user_id is not None and hasattr(call, "edit"):
            self.callback_events[user_id] = call

    def _get_callback_event(self, event):
        user_id = self._event_user_id(event)
        if user_id is None:
            return None
        call = self.callback_events.get(user_id)
        if call is not None and hasattr(call, "edit"):
            return call
        return None

    async def _edit(self, call, text: str, buttons=None) -> None:
        self._remember_callback_event(call)
        await call.edit(text, buttons=buttons, parse_mode="html")

    async def show_menu(self, event, key_path: list[Any] | None = None, page: int = 0) -> None:
        key_path = key_path or []
        self.page_state[tuple(key_path)] = page
        try:
            current_data = await self._get_data_at_path(key_path)
        except KeyError:
            await event.edit(self.s("invalid_key"), parse_mode="html")
            return

        header = self._make_path_text(key_path)
        if isinstance(current_data, (dict, list)) and current_data:
            text = header
            buttons = self.generate_nested_markup(current_data, key_path, page)
        else:
            text = self._value_text(header, current_data)
            buttons = self.generate_value_markup(key_path, current_data)

        success, _message = await self.inline(
            event.chat_id,
            text,
            buttons=buttons,
            parse_mode="html",
            reply_to=getattr(getattr(event, "message", None), "reply_to_msg_id", None),
        )
        if not success:
            await event.edit(text, buttons=buttons, parse_mode="html")

    @callback(ttl=0)
    async def navigate_db(self, call, key_path: list[Any] | None = None, page: int = 0) -> None:
        self._remember_callback_event(call)
        key_path = key_path or []
        self.page_state[tuple(key_path)] = page
        try:
            current_data = await self._get_data_at_path(key_path)
        except KeyError:
            await self._answer_callback(call, self.s("invalid_key"))
            return

        is_list_item = bool(key_path) and isinstance(key_path[-1], int)
        if is_list_item:
            header = self._make_list_item_path_text(key_path[:-1], key_path[-1])
            await self._edit(
                call,
                self._value_text(header, current_data),
                self.generate_list_item_markup(key_path),
            )
        elif isinstance(current_data, (dict, list)) and current_data:
            await self._edit(
                call,
                self._make_path_text(key_path),
                self.generate_nested_markup(current_data, key_path, page),
            )
        else:
            await self._edit(
                call,
                self._value_text(self._make_path_text(key_path), current_data),
                self.generate_value_markup(key_path, current_data),
            )

    def _button(self, text: str, handler, *args: Any, style: str | None = None):
        kwargs = {"args": args, "ttl": 0}
        if style:
            kwargs["style"] = style
        return self.Button.inline(text, handler, **kwargs)

    def _input_button(
        self,
        text: str,
        handler,
        *,
        placeholder: str,
        data: Any,
        style: str | None = None,
    ):
        kwargs = {"placeholder": placeholder, "data": data, "ttl": 0}
        if style:
            kwargs["style"] = style
        return self.Button.input(text, handler, **kwargs)

    def generate_nested_markup(self, data: Any, key_path: list[Any], page: int = 0):
        if isinstance(data, list):
            return self.generate_list_markup(data, key_path, page)

        items = list(data.items()) if isinstance(data, dict) else []
        items_per_page = 9
        total_pages = max(1, (len(items) + items_per_page - 1) // items_per_page)
        start_idx = page * items_per_page
        page_items = items[start_idx : start_idx + items_per_page]

        markup = []
        row = []
        for index, (key, _value) in enumerate(page_items):
            if index % 3 == 0 and row:
                markup.append(row)
                row = []
            row.append(self._button(str(key), self.navigate_db, key_path + [key], 0))
        if row:
            markup.append(row)

        nav_buttons = []
        if key_path:
            parent_page = self.page_state.get(tuple(key_path[:-1]), 0)
            nav_buttons.append(
                self._button(self.s("back_btn"), self.navigate_db, key_path[:-1], parent_page, style="primary")
            )

        if total_pages > 1:
            if page > 0:
                nav_buttons.append(self._button("◀️", self.navigate_db, key_path, page - 1))
            nav_buttons.append(
                self._button(self.s("page", current=page + 1, total=total_pages), self.navigate_db, key_path, page)
            )
            if page < total_pages - 1:
                nav_buttons.append(self._button("▶️", self.navigate_db, key_path, page + 1))
        if nav_buttons:
            markup.append(nav_buttons)

        if key_path:
            markup.append([
                self._input_button(
                    self.s("add_btn"),
                    self.add_value_input,
                    placeholder=self.s("input_key_value"),
                    data={"path": key_path},
                    style="primary",
                ),
                self._button(self.s("del_all_btn"), self.confirm_delete_all, key_path, style="danger"),
            ])
        else:
            markup.append([
                self._input_button(
                    self.s("add_btn"),
                    self.add_value_input,
                    placeholder=self.s("input_module_key_value"),
                    data={"path": key_path},
                    style="primary",
                ),
                self._button(self.s("close_btn"), self.close_form),
            ])
        return markup

    def generate_list_markup(self, data: list[Any], key_path: list[Any], page: int = 0):
        items_per_page = 9
        total_pages = max(1, (len(data) + items_per_page - 1) // items_per_page)
        start_idx = page * items_per_page
        page_items = list(enumerate(data[start_idx : start_idx + items_per_page], start_idx))

        markup = []
        row = []
        for index, (item_index, value) in enumerate(page_items):
            if index % 3 == 0 and row:
                markup.append(row)
                row = []
            if isinstance(value, (dict, list)):
                btn_text = f"[{item_index}]"
            else:
                value_str = str(value)
                btn_text = f"{value_str[:10]}..." if len(value_str) > 10 else value_str
            row.append(self._button(btn_text, self.navigate_db, key_path + [item_index], 0))
        if row:
            markup.append(row)

        nav_buttons = []
        if key_path:
            parent_page = self.page_state.get(tuple(key_path[:-1]), 0)
            nav_buttons.append(
                self._button(self.s("back_btn"), self.navigate_db, key_path[:-1], parent_page, style="primary")
            )
        if total_pages > 1:
            if page > 0:
                nav_buttons.append(self._button("◀️", self.navigate_db, key_path, page - 1))
            nav_buttons.append(
                self._button(self.s("page", current=page + 1, total=total_pages), self.navigate_db, key_path, page)
            )
            if page < total_pages - 1:
                nav_buttons.append(self._button("▶️", self.navigate_db, key_path, page + 1))
        if nav_buttons:
            markup.append(nav_buttons)

        if key_path:
            markup.append([
                self._input_button(
                    self.s("add_btn"),
                    self.add_value_input,
                    placeholder=self.s("input_value"),
                    data={"path": key_path},
                    style="primary",
                ),
                self._button(self.s("del_all_btn"), self.confirm_delete_all, key_path, style="danger"),
            ])
        return markup

    def generate_list_item_markup(self, key_path: list[Any]):
        parent_page = self.page_state.get(tuple(key_path[:-1]), 0)
        return [
            [
                self._input_button(
                    self.s("edit_btn"),
                    self.edit_value_input,
                    placeholder=self.s("input_value"),
                    data={"path": key_path},
                    style="primary",
                )
            ],
            [self._button(self.s("del_btn"), self.delete_key, key_path, style="danger")],
            [self._button(self.s("back_btn"), self.navigate_db, key_path[:-1], parent_page, style="primary")],
        ]

    def generate_value_markup(self, key_path: list[Any], value: Any = None):
        if not key_path:
            return [[self._button(self.s("close_btn"), self.close_form)]]
        parent_page = self.page_state.get(tuple(key_path[:-1]), 0)
        markup = []
        if isinstance(value, (dict, list)):
            markup.append([
                self._input_button(
                    self.s("add_btn"),
                    self.add_value_input,
                    placeholder=self.s("input_key_value") if isinstance(value, dict) else self.s("input_value"),
                    data={"path": key_path},
                    style="primary",
                )
            ])
        markup.extend([
            [
                self._input_button(
                    self.s("edit_btn"),
                    self.edit_value_input,
                    placeholder=self.s("input_value"),
                    data={"path": key_path},
                    style="primary",
                )
            ],
            [self._button(self.s("del_btn"), self.delete_key, key_path, style="danger")],
            [self._button(self.s("back_btn"), self.navigate_db, key_path[:-1], parent_page, style="primary")],
        ])
        return markup

    async def _render_to_event(self, event, key_path: list[Any], page: int | None = None) -> None:
        if page is None:
            page = self.page_state.get(tuple(key_path), 0)
        try:
            current_data = await self._get_data_at_path(key_path)
        except KeyError:
            await event.edit(self.s("invalid_key"), parse_mode="html")
            return

        if key_path and isinstance(key_path[-1], int):
            text = self._value_text(
                self._make_list_item_path_text(key_path[:-1], key_path[-1]), current_data
            )
            buttons = self.generate_list_item_markup(key_path)
        elif isinstance(current_data, (dict, list)) and current_data:
            text = self._make_path_text(key_path)
            buttons = self.generate_nested_markup(current_data, key_path, page)
        else:
            text = self._value_text(self._make_path_text(key_path), current_data)
            buttons = self.generate_value_markup(key_path, current_data)
        await event.edit(text, buttons=buttons, parse_mode="html")

    async def _replace_value_at_path(self, key_path: list[Any], value: Any) -> None:
        if len(key_path) < 2:
            raise KeyError(key_path[-1] if key_path else "")

        module = str(key_path[0])
        key = str(key_path[1])
        if len(key_path) == 2:
            await self._set_raw_value(module, key, value)
            return

        raw_value = await self._get_raw_value(module, key)
        if raw_value is None:
            raise KeyError(key)

        root_value = self._decode_value(raw_value)
        current = root_value
        for item in key_path[2:-1]:
            if isinstance(current, dict) and item in current:
                current = current[item]
            elif isinstance(current, list) and isinstance(item, int) and 0 <= item < len(current):
                current = current[item]
            else:
                raise KeyError(item)

        last = key_path[-1]
        if isinstance(current, dict) and last in current:
            current[last] = value
        elif isinstance(current, list) and isinstance(last, int) and 0 <= last < len(current):
            current[last] = value
        else:
            raise KeyError(last)
        await self._set_raw_value(module, key, root_value)

    def _parse_root_add_input(self, text: str) -> tuple[str, str, Any] | None:
        text = text.strip()
        if not text:
            return None
        if "=" in text:
            left, raw_value = text.split("=", 1)
            left = left.strip()
            if "." in left:
                module, key = left.split(".", 1)
            else:
                parts = left.split(maxsplit=1)
                if len(parts) != 2:
                    return None
                module, key = parts
        else:
            parts = text.split(maxsplit=2)
            if len(parts) != 3:
                return None
            module, key, raw_value = parts
        module = module.strip()
        key = key.strip()
        if not module or not key:
            return None
        return module, key, self._parse_input_value(raw_value)

    async def _add_value_at_path(self, key_path: list[Any], text: str) -> list[Any]:
        if not key_path:
            parsed = self._parse_root_add_input(text)
            if not parsed:
                raise ValueError(self.s("input_module_key_value"))
            module, key, value = parsed
            await self._set_raw_value(module, key, value)
            return [module, key]

        if len(key_path) == 1:
            parsed = self._split_key_value(text)
            if not parsed:
                raise ValueError(self.s("input_key_value"))
            key, value = parsed
            await self._set_raw_value(str(key_path[0]), key, value)
            return [str(key_path[0]), key]

        current_data = await self._get_data_at_path(key_path)
        if isinstance(current_data, dict):
            parsed = self._split_key_value(text)
            if not parsed:
                raise ValueError(self.s("input_key_value"))
            key, value = parsed
            current_data[key] = value
            await self._replace_value_at_path(key_path, current_data)
            return key_path + [key]
        if isinstance(current_data, list):
            current_data.append(self._parse_input_value(text))
            await self._replace_value_at_path(key_path, current_data)
            return key_path + [len(current_data) - 1]
        raise ValueError(self.s("input_value"))

    async def _safe_edit_text(self, event, text: str) -> None:
        try:
            await event.edit(text, parse_mode="html")
        except Exception:
            try:
                await event.reply(text, parse_mode="html")
            except Exception:
                pass

    async def edit_value_input(self, event, text: str, data: Any = None) -> None:
        call = self._get_callback_event(event)
        if call is None:
            return
        key_path = list((data or {}).get("path") or [])
        if len(key_path) < 2:
            await self._safe_edit_text(
                call, self.s("invalid_input", usage=self.s("input_value"))
            )
            return
        try:
            await self._replace_value_at_path(key_path, self._parse_input_value(text))
        except KeyError as error:
            await self._safe_edit_text(
                call, self.s("not_found", key=error.args[0] if error.args else key_path[-1])
            )
            return
        await self._render_to_event(call, key_path)

    async def add_value_input(self, event, text: str, data: Any = None) -> None:
        call = self._get_callback_event(event)
        if call is None:
            return
        key_path = list((data or {}).get("path") or [])
        try:
            added_path = await self._add_value_at_path(key_path, text)
        except ValueError as error:
            await self._safe_edit_text(call, self.s("invalid_input", usage=str(error)))
            return
        except KeyError as error:
            await self._safe_edit_text(
                call, self.s("not_found", key=error.args[0] if error.args else key_path[-1])
            )
            return
        await self._render_to_event(call, added_path)

    @callback(ttl=0)
    async def close_form(self, call) -> None:
        self._remember_callback_event(call)
        try:
            await self.client.delete_messages(call.chat_id, [call.message_id])
        except Exception:
            try:
                await call.delete()
            except Exception:
                await self._answer_callback(call, self.s("close_btn"))

    @callback(ttl=0)
    async def confirm_delete_all(self, call, key_path: list[Any]) -> None:
        self._remember_callback_event(call)
        await self._edit(
            call,
            self.s("confirm_delete"),
            [
                [self._button(self.s("yes_btn"), self.delete_all_keys, key_path, style="danger")],
                [self._button(self.s("no_btn"), self.navigate_db, key_path, self.page_state.get(tuple(key_path), 0))],
            ],
        )

    async def _delete_nested_value(self, key_path: list[Any]) -> tuple[int, str]:
        module = str(key_path[0])
        key = str(key_path[1])
        raw_value = await self._get_raw_value(module, key)
        if raw_value is None:
            raise KeyError(key)

        root_value = self._decode_value(raw_value)
        current = root_value
        for item in key_path[2:-1]:
            if isinstance(current, dict) and item in current:
                current = current[item]
            elif isinstance(current, list) and isinstance(item, int) and 0 <= item < len(current):
                current = current[item]
            else:
                raise KeyError(item)

        last = key_path[-1]
        if isinstance(current, dict) and last in current:
            deleted = current.pop(last)
            count = len(deleted) if isinstance(deleted, (dict, list)) else 1
            display = str(last)
        elif isinstance(current, list) and isinstance(last, int) and 0 <= last < len(current):
            deleted = current.pop(last)
            count = len(deleted) if isinstance(deleted, (dict, list)) else 1
            display = f"[{last}] = {deleted}"
        else:
            raise KeyError(last)

        await self._set_raw_value(module, key, root_value)
        return count, display

    @callback(ttl=0)
    async def delete_all_keys(self, call, key_path: list[Any]) -> None:
        self._remember_callback_event(call)
        try:
            if len(key_path) == 1:
                module = str(key_path[0])
                keys = await self._module_keys(module)
                for key in keys:
                    await self._delete_raw_key(module, key)
                await self._answer_callback(call, self.s("deleted_all", count=len(keys)))
                await self.navigate_db(call, [], self.page_state.get((), 0))
            elif len(key_path) == 2:
                module, key = str(key_path[0]), str(key_path[1])
                value = self._decode_value(await self._get_raw_value(module, key))
                count = len(value) if isinstance(value, (dict, list)) else 1
                await self._delete_raw_key(module, key)
                await self._answer_callback(call, self.s("deleted_all", count=count))
                await self.navigate_db(call, [module], self.page_state.get((module,), 0))
            else:
                count, _display = await self._delete_nested_value(key_path)
                await self._answer_callback(call, self.s("deleted_all", count=count))
                await self.navigate_db(
                    call,
                    key_path[:-1],
                    self.page_state.get(tuple(key_path[:-1]), 0),
                )
        except KeyError as error:
            await self._answer_callback(call, self.s("not_found", key=error.args[0] if error.args else key_path[-1]))

    @callback(ttl=0)
    async def delete_key(self, call, key_path: list[Any]) -> None:
        self._remember_callback_event(call)
        parent_page = self.page_state.get(tuple(key_path[:-1]), 0)
        try:
            if len(key_path) == 1:
                module = str(key_path[0])
                keys = await self._module_keys(module)
                if not keys:
                    raise KeyError(module)
                for key in keys:
                    await self._delete_raw_key(module, key)
                key_display = module
                parent_path: list[Any] = []
            elif len(key_path) == 2:
                module, key = str(key_path[0]), str(key_path[1])
                if await self._get_raw_value(module, key) is None:
                    raise KeyError(key)
                await self._delete_raw_key(module, key)
                key_display = key
                parent_path = [module]
            else:
                _count, key_display = await self._delete_nested_value(key_path)
                parent_path = key_path[:-1]

            await self._answer_callback(call, self.s("deleted", key=key_display))
            await self.navigate_db(call, parent_path, parent_page)
        except KeyError as error:
            await self._answer_callback(call, self.s("not_found", key=error.args[0] if error.args else key_path[-1]))

    async def find_module_key(self, module_name: str) -> str | None:
        module_name_lower = module_name.lower()
        rows = await self._db_api().db_query(
            "SELECT DISTINCT module FROM module_data ORDER BY module", ()
        )
        for row in rows:
            key = row[0]
            if key.lower() == module_name_lower:
                return key
        return None

    def args_raw(self, event) -> str:
        text = (getattr(event, "raw_text", None) or getattr(event, "text", "") or "").strip()
        parts = text.split(maxsplit=1)
        return parts[1].strip() if len(parts) > 1 else ""

    @command("mydb", doc_ru="Просмотр базы данных", doc_en="Viewing the database")
    async def mydb(self, event) -> None:
        args = self.args_raw(event)
        if args:
            module_key = await self.find_module_key(args)
            if module_key:
                await self.show_menu(event, [module_key], self.page_state.get((module_key,), 0))
                return
            await event.edit(self.s("module_not_found", module=html.escape(args)), parse_mode="html")
            return
        await self.show_menu(event, [], self.page_state.get((), 0))
