from __future__ import annotations

from typing import Any
import html
import re
import io
import contextlib
import time
import uuid
import asyncio

class _OpenAgentResponseMixin:
    """Response formatting, answer delivery, follow-up and regeneration."""

    def _format_inline_markdown(self, text: str) -> str:
        text = html.escape(html.unescape(text or ""))
        text = re.sub(r"`([^`\n]+)`", r"<code>\1</code>", text)
        text = re.sub(r"\*\*([^*\n]+)\*\*", r"<b>\1</b>", text)
        text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<i>\1</i>", text)
        return text

    def _format_agent_markdown(self, text: str) -> str:
        parts: list[str] = []
        pos = 0
        pattern = re.compile(r"```([a-zA-Z0-9_+-]*)\n?(.*?)```", re.DOTALL)
        for match in pattern.finditer(text or ""):
            parts.append(self._format_inline_markdown(text[pos : match.start()]))
            lang = match.group(1).strip()
            code = html.escape(html.unescape(match.group(2).strip("\n")))
            if lang:
                parts.append(f'<pre language="{html.escape(lang)}">{code}</pre>')
            else:
                parts.append(f"<pre>{code}</pre>")
            pos = match.end()
        parts.append(self._format_inline_markdown((text or "")[pos:]))
        return "".join(parts)

    def _sanitize_answer(self, text: str) -> str:
        patterns = [
            r"\s*Use the above message and context to generate a prompt and call the task tool with subagent:\s*\w+\s*",
            r"\s*call the task tool with subagent:\s*\w+\s*",
            r"<(?:terminal|web|mcub|message|file|dialog|chat|moderation|profile|contacts|creation|skills|context|utility|code)\.[^>]+>",
            r"</(?:terminal|web|mcub|message|file|dialog|chat|moderation|profile|contacts|creation|skills|context|utility|code)\.[^>]+>",
        ]
        for pattern in patterns:
            text = re.sub(pattern, " ", text, flags=re.I)
        return text.strip()

    async def _send_answer_file(
        self,
        event: Any,
        title: str,
        prompt: str,
        answer: str,
        agent_log: list[str],
        thinking_notes: list[str] | None = None,
        buttons: list[list[Any]] | None = None,
    ) -> None:
        content = f"{title}\n\n{self.strings('answer_file_request')}:\n{prompt}\n\n{self.strings('answer_file_answer')}:\n{answer}"
        content += "\n\nThinking:\n" + self._format_thinking_notes(thinking_notes)
        if agent_log:
            content += "\n\nAgent Log:\n" + "\n".join(self._compact_agent_log(agent_log))
        data = content.encode("utf-8")

        def make_buf() -> io.BytesIO:
            buf = io.BytesIO(data)
            buf.name = "openagent_answer.txt"
            return buf

        total_len = len(content)
        self.log.debug(
            "OA send_answer_file: chat_id=%s content_len=%d has_edit=%s",
            getattr(event, "chat_id", None), total_len, hasattr(event, "edit"),
        )
        caption = f"{title}\n\n{self.strings('answer_file_too_long')}"
        last_error: Exception | None = None
        if hasattr(event, "edit"):
            try:
                await event.edit(
                    caption,
                    file=make_buf(),
                    buttons=buttons,
                    parse_mode="html",
                )
            except Exception as exc:
                last_error = exc
            else:
                return
        error = f"\n\n<code>{html.escape(str(last_error)[:500])}</code>" if last_error else ""
        fallback = html.escape(content[:3000])
        await self.edit(
            event,
            f"{caption}\n\n{self.strings('answer_file_attach_failed')}{error}\n\n<blockquote expandable>{fallback}</blockquote>",
            as_html=True,
        )

    async def _reply_text(
        self,
        event: Any,
        text: str,
        *,
        title: str = "OpenAgent",
        prompt: str = "",
        agent_log: list[str] | None = None,
        thinking_notes: list[str] | None = None,
        buttons: list[list[Any]] | None = None,
        edit_current: bool = False,
    ) -> None:
        text = self._sanitize_answer(text or "")
        formatted = self._format_agent_markdown(text)
        formatted_prompt = self._format_agent_markdown(prompt or "")
        request_label = self._request_label(thinking_notes=thinking_notes)
        response_label = self._response_label(thinking_notes=thinking_notes)
        agent_log_html = self._agent_log_html(agent_log or [])
        total_formatted_len = len(formatted) + len(formatted_prompt) + len(agent_log_html)
        chat_id = getattr(event, "chat_id", None) or getattr(event, "_openagent_source_chat_id", None)
        if total_formatted_len > 3500:
            self.log.debug(
                "OA reply_text TOO_LONG→FILE: chat_id=%s total_len=%d limit=3500",
                chat_id, total_formatted_len,
            )
            await self._send_answer_file(
                event,
                title,
                prompt,
                text or "",
                agent_log or [],
                thinking_notes,
                buttons,
            )
            return
        chunks = [formatted[i : i + 3500] for i in range(0, len(formatted), 3500)] or [""]
        for index, chunk in enumerate(chunks):
            header = title if index == 0 else f"{title} <i>{html.escape(self.strings('continued'))}</i>"
            if index == 0:
                body = (
                    f"{header}\n\n"
                    f"{request_label}\n<blockquote expandable>{formatted_prompt}</blockquote>\n\n"
                    f"{response_label}\n<blockquote expandable>{chunk}</blockquote>"
                )
            else:
                body = f"{header}\n\n{response_label}\n<blockquote expandable>{chunk}</blockquote>"
            if index == len(chunks) - 1:
                body += self._agent_log_html(agent_log or [])
            if edit_current and hasattr(event, "edit"):
                try:
                    await event.edit(
                        body,
                        parse_mode="html",
                        buttons=buttons if index == len(chunks) - 1 else None,
                    )
                    self.log.debug(
                        "OA reply_text EDIT_OK: index=%d/%d chat_id=%s chunk_len=%d",
                        index, len(chunks) - 1, chat_id, len(chunk),
                    )
                    continue
                except Exception as exc:
                    self.log.debug(
                        "OA reply_text EDIT_FAIL: index=%d/%d chat_id=%s error=%s",
                        index, len(chunks) - 1, chat_id, exc,
                    )
            if chat_id is not None:
                if buttons and index == len(chunks) - 1:
                    try:
                        await self.inline(
                            chat_id,
                            body,
                            buttons=buttons,
                            ttl=900,
                            parse_mode="html",
                            reply_to=getattr(event, "reply_to", None),
                        )
                        self.log.debug(
                            "OA reply_text NEW_INLINE: chat_id=%s chunk_len=%d",
                            chat_id, len(chunk),
                        )
                    except Exception as exc:
                        self.log.debug(
                            "OA reply_text INLINE_FAIL→SEND_MSG: chat_id=%s error=%s",
                            chat_id, exc,
                        )
                        await self.client.send_message(chat_id, body, parse_mode="html")
                else:
                    self.log.debug(
                        "OA reply_text SEND_MSG: chat_id=%s has_buttons=%s index=%d/%d",
                        chat_id, bool(buttons), index, len(chunks) - 1,
                    )
                    await self.client.send_message(
                        chat_id,
                        body,
                        parse_mode="html",
                    )
            else:
                self.log.debug(
                    "OA reply_text SEND_REPLY: no chat_id, has_reply=%s",
                    hasattr(event, "reply"),
                )
                if hasattr(event, "reply"):
                    await self.reply(event, body, as_html=True)

    async def _cancel_generation(self, event: Any, token: str) -> None:
        self._cancelled_generations.add(token)
        try:
            await event.answer(self.strings("cancelled"), alert=False)
        except Exception:
            pass

    async def _reply_error_answer(
        self,
        event: Any,
        exc: BaseException,
        *,
        prompt: str,
        full_prompt: str | None = None,
        attachments: list[dict[str, str]] | None = None,
        source_event: Any | None = None,
        chat_id: int | None = None,
        started_at: float | None = None,
        source: str = "OpenAgent",
    ) -> None:
        """Render an exception as the final OpenAgent answer instead of a raw edit."""
        with contextlib.suppress(Exception):
            await self.kernel.handle_error(exc, source=source, event=source_event or event)
        elapsed = (time.monotonic() - started_at) if started_at else 0.0
        error_text = self.strings("error", error=str(exc))
        await self._reply_text(
            event,
            error_text,
            title=self._response_title(elapsed, tool_count=0, thinking_notes=[]),
            prompt=prompt,
            agent_log=[f"error: {type(exc).__name__}"],
            thinking_notes=[],
            buttons=self._final_buttons(
                chat_id,
                prompt,
                full_prompt or prompt,
                attachments or [],
                source_event=source_event or event,
            ),
            edit_current=True,
        )

    async def _on_runtime_comment_input(self, event: Any, text: str, token: str) -> None:
        """Collect a user comment while an agent run is still active."""
        token = str(token or "").strip()
        comment = (text or "").strip()
        if not token or not comment:
            return
        bucket = self._runtime_comments.setdefault(token, [])
        bucket.append(comment[:4000])
        # Keep memory bounded if a user sends many comments during a long run.
        if len(bucket) > 10:
            del bucket[:-10]
        with contextlib.suppress(Exception):
            await event.answer(self.strings("runtime_comment_saved"), alert=False)

    def add_runtime_comment(self, runtime_token: str | None, comment: str) -> bool:
        """Queue a comment for the active agent loop identified by runtime_token."""
        token = str(runtime_token or "").strip()
        text = str(comment or "").strip()
        if not token or not text:
            return False
        bucket = self._runtime_comments.setdefault(token, [])
        bucket.append(text[:4000])
        if len(bucket) > 10:
            del bucket[:-10]
        return True

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
        """Run a tool asynchronously and add a runtime comment when it finishes."""
        clean_tool = str(tool_name or "").strip().lower()
        if not clean_tool:
            raise ValueError("tool_name is required")
        if clean_tool in {"task.background", "task.run_background", "background.run"}:
            raise ValueError("background task tools cannot run themselves")
        task_id = uuid.uuid4().hex[:10]
        display = (label or clean_tool).strip()[:120]
        token = str(runtime_token or "").strip()

        async def runner() -> None:
            started = time.monotonic()
            local_log: list[str] = []
            local_thinking: list[str] = []
            try:
                result = await self._dispatch_tool(
                    clean_tool,
                    attrs_raw,
                    body,
                    source_event,
                    status_event,
                    local_log,
                    started_at=started,
                    thinking_notes=local_thinking,
                )
                elapsed = time.monotonic() - started
                comment = (
                    f"Background task {task_id} finished: {display}\n"
                    f"tool: {clean_tool}\n"
                    f"elapsed: {elapsed:.1f}s\n"
                    f"result:\n{str(result or '').strip()[:3000]}"
                )
                if not self.add_runtime_comment(token, comment):
                    self.log.info("OpenAgent background task %s finished: %s", task_id, clean_tool)
            except Exception as exc:
                elapsed = time.monotonic() - started
                comment = (
                    f"Background task {task_id} failed: {display}\n"
                    f"tool: {clean_tool}\n"
                    f"elapsed: {elapsed:.1f}s\n"
                    f"error: {type(exc).__name__}: {exc}"
                )
                self.add_runtime_comment(token, comment)
                with contextlib.suppress(Exception):
                    await self.kernel.handle_error(exc, source=f"OpenAgent:bg_tool:{clean_tool}", event=source_event)
            finally:
                self._background_tool_tasks.pop(task_id, None)

        task = asyncio.create_task(runner())
        self._background_tool_tasks[task_id] = task
        return task_id

    def _runtime_control_buttons(self, token: str, source_event: Any | None = None) -> list[list[Any]]:
        """Buttons shown while a generation is running."""
        allow_user = getattr(source_event, "sender_id", None)
        comment_button = self.Button.input(
            self.strings("runtime_comment_button"),
            self._on_runtime_comment_input,
            placeholder=self.strings("runtime_comment_placeholder"),
            allow_user=allow_user,
            style="primary",
            data=str(token),
        )
        cancel_button = self._direct_button(
            self.strings("cancel_button"),
            "cancel",
            {"token": token},
        )
        return [[comment_button, cancel_button]]

    def _drain_runtime_comments(self, token: str | None) -> list[str]:
        if not token:
            return []
        return self._runtime_comments.pop(str(token), [])

    def _runtime_comment_message(self, token: str | None) -> dict[str, str] | None:
        comments = self._drain_runtime_comments(token)
        if not comments:
            return None
        rendered = "\n".join(f"- {item}" for item in comments)
        return {
            "role": "user",
            "content": self.strings("runtime_comment_note", comments=rendered),
        }

    def _cleanup_runtime_run(self, token: str | None) -> None:
        if not token:
            return
        self._cancelled_generations.discard(str(token))
        self._runtime_comments.pop(str(token), None)

    def _store_last_loading(self, chat_id: int | None, loading: Any) -> None:
        """Remember the inline form for this chat so the next follow-up can edit it in place."""
        if not chat_id or not loading or not hasattr(loading, "edit"):
            return
        self._oa_last_loading[int(chat_id)] = loading
        if len(self._oa_last_loading) > 500:
            for old_key in list(self._oa_last_loading)[:100]:
                self._oa_last_loading.pop(old_key, None)

    async def _clear_context(self, event: Any, chat_id: int | None) -> None:
        if chat_id is not None:
            self._get_active_session(int(chat_id)).messages.clear()
            self._touch_session(self._get_active_session(int(chat_id)))
        try:
            await event.answer(self.strings("context_cleared"), alert=True)
        except Exception:
            pass

    def _direct_button(self, text: str, kind: str, payload: dict[str, Any]) -> Any:
        if kind == "cancel":
            return self.Button.inline(text, self._cancel_generation, args=(payload.get("token", ""),), style="danger")
        if kind == "clear":
            return self.Button.inline(text, self._clear_context, args=(payload.get("chat_id"),), style="danger")
        if kind == "regen":
            return self.Button.inline(text, self._regenerate_response, args=(payload.get("token", ""),), style="primary")
        return self.Button.inline(text, self._clear_context, args=(None,), style="danger")

    def _final_buttons(
        self,
        chat_id: int | None,
        prompt: str,
        full_prompt: str,
        attachments: list[dict[str, str]],
        *,
        source_event: Any = None,
    ) -> list[list[Any]]:
        regen_token = str(uuid.uuid4())
        self._regen_payloads[regen_token] = {
            "chat_id": chat_id,
            "prompt": prompt,
            "full_prompt": full_prompt,
            "attachments": attachments,
            "source_event": source_event,
            "created_at": time.time(),
        }
        self.log.debug(
            "OA final_buttons: regen_token=%s chat_id=%s source_event=%s attachments=%d",
            regen_token,
            chat_id,
            type(source_event).__name__ if source_event is not None else None,
            len(attachments or []),
        )
        if len(self._regen_payloads) > 50:
            stale = sorted(
                self._regen_payloads,
                key=lambda key: self._regen_payloads[key].get("created_at", 0),
            )[:-50]
            for key in stale:
                self._regen_payloads.pop(key, None)
        history_button = self.Button.inline(
            self.strings("chat_history_button"),
            self._open_sessions_panel,
            args=(chat_id,),
            style="primary",
        )
        clear_button = self._direct_button(self.strings("clear_button"), "clear", {"chat_id": chat_id})
        regen_button = self._direct_button(self.strings("regenerate_button"), "regen", {"token": regen_token})
        rows: list[list[Any]] = []
        if source_event is not None:
            input_key = str(uuid.uuid4())
            self._input_events[input_key] = {
                "event": source_event,
                "chat_id": chat_id,
                "attachments": attachments,
                "created_at": time.time(),
            }
            if len(self._input_events) > 50:
                stale_inp = sorted(
                    self._input_events,
                    key=lambda k: self._input_events[k].get("created_at", 0),
                )[:-50]
                for k in stale_inp:
                    self._input_events.pop(k, None)
            input_btn = self.Button.input(
                self.strings("follow_up_button"),
                self._on_follow_up_input,
                placeholder=self.strings("follow_up_placeholder"),
                allow_user=getattr(source_event, "sender_id", None),
                style="primary",
                data=input_key,
            )
            regen_prompt_btn = self.Button.input(
                self.strings("regen_prompt_button"),
                self._on_regenerate_prompt_input,
                placeholder=self.strings("regen_prompt_placeholder"),
                allow_user=getattr(source_event, "sender_id", None),
                style="primary",
                data=regen_token,
            )
            rows.append([input_btn, regen_prompt_btn])
        rows.append([regen_button, clear_button, history_button])
        return rows

    async def _on_follow_up_input(self, event: Any, text: str, data: str) -> None:
        """Handle follow-up query typed via Button.input on the final response row."""
        entry = self._input_events.pop(data, None)
        if not entry or not text or not text.strip():
            return

        source_event = entry["event"]
        chat_id = entry.get("chat_id")
        attachments = entry.get("attachments") or []
        prompt = text.strip()

        cancel_token = str(uuid.uuid4())
        self._set_placeholder_context(source_event, cancel_token)
        buttons = self._runtime_control_buttons(cancel_token, source_event)
        # Try to reuse the previous inline response form so the answer edits
        # it in place instead of posting a new message for every follow-up.
        prev_form = self._oa_last_loading.get(int(chat_id)) if chat_id else None
        loading = source_event
        if prev_form and hasattr(prev_form, "edit"):
            try:
                await prev_form.edit(
                    self._thinking_text(),
                    buttons=buttons,
                    parse_mode="html",
                )
                loading = prev_form
                with contextlib.suppress(Exception):
                    setattr(loading, "_openagent_status_buttons", buttons)
                with contextlib.suppress(Exception):
                    setattr(loading, "_openagent_source_chat_id", chat_id)
            except Exception:
                loading = await self._start_inline_status(
                    source_event,
                    self._thinking_text(),
                    buttons,
                )
        else:
            loading = await self._start_inline_status(
                source_event,
                self._thinking_text(),
                buttons,
            )
        started = time.monotonic()
        try:
            answer, agent_log, thinking_notes, tool_trace = await self._ask_agent(
                prompt,
                status_event=loading or source_event,
                source_event=source_event,
                attachments=attachments,
                cancel_token=cancel_token,
                started_at=started,
            )
            self._last_request_at = time.time()
            elapsed = time.monotonic() - started
            self._remember_context(chat_id, prompt, answer, tool_trace, thinking_notes)
            await self._reply_text(
                loading or source_event,
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
                    chat_id,
                    prompt,
                    prompt,
                    attachments,
                    source_event=source_event,
                ),
                edit_current=True,
            )
            self._store_last_loading(chat_id, loading)
            self._cleanup_runtime_run(cancel_token)
        except Exception as exc:
            self._cleanup_runtime_run(cancel_token)
            await self._reply_error_answer(
                loading or source_event,
                exc,
                prompt=prompt,
                full_prompt=prompt,
                attachments=attachments,
                source_event=source_event,
                chat_id=chat_id,
                started_at=started,
                source="OpenAgent:follow_up",
            )

    async def _on_regenerate_prompt_input(self, event: Any, text: str, token: str) -> None:
        """Regenerate the previous answer using a user-provided replacement prompt."""
        # Button.input delivers UpdateBotInlineSend as event — it has no .chat_id / .edit().
        # Extract source_event and chat_id from the payload first so that show_feedback
        # and the loading-status setup both have a real message context to work with.
        payload = self._regen_payloads.get(str(token))
        prompt = (text or "").strip()
        source_event = (payload.get("source_event") if payload else None) or event
        chat_id = payload.get("chat_id") if payload else None

        async def show_feedback(message: str) -> None:
            escaped = html.escape(message)
            if hasattr(source_event, "edit"):
                with contextlib.suppress(Exception):
                    await source_event.edit(f"<blockquote>{escaped}</blockquote>", parse_mode="html")
                    self.log.debug("OA regen_prompt: feedback edit ok token=%s", token)
                    return
            with contextlib.suppress(Exception):
                await self.edit(source_event, escaped, as_html=True)
                self.log.debug("OA regen_prompt: feedback fallback edit ok token=%s", token)

        self.log.debug(
            "OA regen_prompt: input token=%s payload=%s prompt_len=%d event=%s",
            token,
            bool(payload),
            len(prompt),
            type(event).__name__,
        )
        if not payload:
            self.log.debug("OA regen_prompt: stale token=%s", token)
            await show_feedback(self.strings("regen_stale"))
            return
        if not prompt:
            self.log.debug("OA regen_prompt: empty prompt token=%s", token)
            await show_feedback(self.strings("regen_prompt_placeholder"))
            return

        attachments = payload.get("attachments") or []
        cancel_token = str(uuid.uuid4())
        self._set_placeholder_context(source_event, cancel_token)
        buttons = self._runtime_control_buttons(cancel_token, source_event)
        loading = source_event
        if hasattr(source_event, "edit"):
            try:
                edited = await source_event.edit(
                    self._thinking_text(),
                    buttons=buttons,
                    parse_mode="html",
                )
                loading = edited if edited and not isinstance(edited, bool) else source_event
                self.log.debug(
                    "OA regen_prompt: status edit ok token=%s loading=%s",
                    token,
                    type(loading).__name__,
                )
                with contextlib.suppress(Exception):
                    setattr(loading, "_openagent_status_buttons", buttons)
                with contextlib.suppress(Exception):
                    setattr(loading, "_openagent_source_chat_id", chat_id)
            except Exception as exc:
                self.log.debug("OA regen_prompt: status edit failed token=%s error=%s", token, exc)
                loading = await self._start_inline_status(source_event, self._thinking_text(), buttons)
        else:
            self.log.debug("OA regen_prompt: no source_event.edit token=%s, using inline status", token)
            loading = await self._start_inline_status(source_event, self._thinking_text(), buttons)

        started = time.monotonic()
        try:
            self.log.debug(
                "OA regen_prompt: ask start token=%s chat_id=%s prompt_len=%d source_event=%s",
                token,
                chat_id,
                len(prompt),
                type(source_event).__name__ if source_event is not None else None,
            )
            answer, agent_log, thinking_notes, tool_trace = await self._ask_agent(
                prompt,
                status_event=loading or source_event,
                source_event=source_event,
                attachments=attachments,
                cancel_token=cancel_token,
                started_at=started,
            )
            elapsed = time.monotonic() - started
            self.log.debug(
                "OA regen_prompt: ask done token=%s elapsed=%.2f tools=%d answer_len=%d",
                token,
                elapsed,
                len(agent_log),
                len(answer or ""),
            )
            self._remember_context(chat_id, prompt, answer, tool_trace, thinking_notes)
            await self._reply_text(
                loading or source_event,
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
                    chat_id,
                    prompt,
                    prompt,
                    attachments,
                    source_event=source_event,
                ),
                edit_current=True,
            )
            self._cleanup_runtime_run(cancel_token)
        except Exception as exc:
            self._cleanup_runtime_run(cancel_token)
            self.log.debug("OA regen_prompt: exception token=%s error=%s", token, exc)
            await self._reply_error_answer(
                loading or source_event,
                exc,
                prompt=prompt,
                full_prompt=prompt,
                attachments=attachments,
                source_event=source_event,
                chat_id=chat_id,
                started_at=started,
                source="OpenAgent:regenerate_prompt",
            )

    async def _regenerate_response(self, event: Any, token: str) -> None:
        payload = self._regen_payloads.get(token)
        if not payload:
            try:
                await event.answer(self.strings("regen_stale"), alert=True)
            except Exception:
                pass
            return

        try:
            await event.answer(self.strings("regenerating"), alert=False)
        except Exception:
            pass

        cancel_token = str(uuid.uuid4())
        self._set_placeholder_context(event, cancel_token)
        buttons = self._runtime_control_buttons(cancel_token, event)
        try:
            edited = await event.edit(
                self._thinking_text(),
                buttons=buttons,
                parse_mode="html",
            )
            loading = edited if edited and not isinstance(edited, bool) else event
            with contextlib.suppress(Exception):
                setattr(loading, "_openagent_status_buttons", buttons)
            with contextlib.suppress(Exception):
                setattr(loading, "_openagent_source_chat_id", payload.get("chat_id"))
        except Exception:
            loading = event

        started = time.monotonic()
        try:
            answer, agent_log, thinking_notes, tool_trace = await self._ask_agent(
                payload["full_prompt"],
                status_event=loading or event,
                source_event=event,
                attachments=payload.get("attachments") or [],
                cancel_token=cancel_token,
                started_at=started,
            )
            elapsed = time.monotonic() - started
            self._remember_context(payload.get("chat_id"), payload["full_prompt"], answer, tool_trace, thinking_notes)
            await self._reply_text(
                loading or event,
                answer,
                title=self._response_title(
                    elapsed,
                    tool_count=len(agent_log),
                    thinking_notes=thinking_notes,
                ),
                prompt=payload["prompt"],
                agent_log=agent_log,
                thinking_notes=thinking_notes,
                buttons=self._final_buttons(
                    payload.get("chat_id"),
                    payload["prompt"],
                    payload["full_prompt"],
                    payload.get("attachments") or [],
                    source_event=event,
                ),
                edit_current=True,
            )
            self._cleanup_runtime_run(cancel_token)
        except Exception as exc:
            self._cleanup_runtime_run(cancel_token)
            await self._reply_error_answer(
                loading or event,
                exc,
                prompt=payload["prompt"],
                full_prompt=payload["full_prompt"],
                attachments=payload.get("attachments") or [],
                source_event=event,
                chat_id=payload.get("chat_id"),
                started_at=started,
                source="OpenAgent:regenerate",
            )

__all__ = [
    '_OpenAgentResponseMixin',
]
