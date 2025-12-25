import html
from telethon.tl.types import MessageEntityCustomEmoji

def register(kernel):
    client = kernel.client

    async def get_formatted_html(message):
        if not message.text:
            return "❌ <i>Нет текста для преобразования</i>"

        text = message.text
        entities = message.entities or []
        parts = []
        last_offset = 0

        for entity in sorted(entities, key=lambda e: e.offset):
            # Текст до сущности
            if entity.offset > last_offset:
                plain_text = text[last_offset:entity.offset]
                parts.append(html.escape(plain_text))

            entity_text = text[entity.offset:entity.offset + entity.length]

            if isinstance(entity, MessageEntityCustomEmoji):
                parts.append(f'[Кастомный эмодзи: document_id={entity.document_id}]')
            elif hasattr(entity, 'url'):
                # Ссылка
                parts.append(f'<a href="{html.escape(entity.url)}">{html.escape(entity_text)}</a>')
            elif hasattr(entity, 'bold') and entity.bold:
                parts.append(f'<b>{html.escape(entity_text)}</b>')
            elif hasattr(entity, 'italic') and entity.italic:
                parts.append(f'<i>{html.escape(entity_text)}</i>')
            elif hasattr(entity, 'code') and entity.code:
                parts.append(f'<code>{html.escape(entity_text)}</code>')
            elif hasattr(entity, 'pre') and entity.pre:
                parts.append(f'<pre>{html.escape(entity_text)}</pre>')
            else:
                parts.append(html.escape(entity_text))

            last_offset = entity.offset + entity.length

        if last_offset < len(text):
            parts.append(html.escape(text[last_offset:]))

        html_result = ''.join(parts)
        html_result = html_result.replace('\n', '<br>')

        return html_result

    @kernel.register_command('html_code')
    async def html_code_handler(event):
        try:
            if event.is_reply:
                source_message = await event.get_reply_message()
                message = source_message
            else:
                message = event

            if not message.text:
                await event.edit("❌ <i>Нет текста для преобразования</i>", parse_mode='html')
                return


            html_content = await get_formatted_html(message)


            html_output = f"""🔮 <b>HTML-разметка сообщения:</b>

<code>{html_content}</code>

"""

            custom_emojis = []
            for entity in (message.entities or []):
                if isinstance(entity, MessageEntityCustomEmoji):
                    custom_emojis.append(str(entity.document_id))

            if custom_emojis:
                html_output += f"\n🎨 <b>прем эмодзи (document_id):</b> {', '.join(custom_emojis)}"

            await event.edit(html_output, parse_mode='html')

        except Exception as e:
            await event.edit("<i>❌ Ошибка, смотри логи</i>", parse_mode='html')
            await log_error_to_bot(f"❌ {module_name}: {str(e)}")

    kernel.cprint(f'{kernel.Colors.GREEN}✅ Модуль html_code обновлён{kernel.Colors.RESET}')
