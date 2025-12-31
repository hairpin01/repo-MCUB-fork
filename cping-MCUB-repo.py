# requires: aiohttp
# author: @hajfiajsiodjsijdsiirpin
# version: 1.0.3
# description: Инлайн команда, [@youbot cping]

import time
import asyncio
from telethon import events, Button

def register(kernel):
    client = kernel.client


    if not hasattr(kernel, 'ADMIN_ID'):
        kernel.send_log_message("Модуль cping: ADMIN_ID не установлен в ядре")
        return

    async def ping_api_telegram():

        try:
            import aiohttp
            start = time.time()
            timeout = aiohttp.ClientTimeout(total=5)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get('https://api.telegram.org') as resp:
                    end = time.time()
                    return round((end - start) * 1000, 2)  # мс
        except ImportError:
            return "Установите aiohttp"
        except Exception as e:
            return f"Ошибка: {str(e)}"

    async def inline_cping(event):

        try:

            if event.query.user_id != kernel.ADMIN_ID:
                await event.answer([])
                return


            ping_result = await ping_api_telegram()


            if isinstance(ping_result, (int, float)):
                ping_text = f"**📶 Пинг до Telegram API:** `{ping_result}` мс"
                title = f"Пинг: {ping_result} мс"
            else:
                ping_text = f"**❌ Ошибка:** {ping_result}"
                title = "Ошибка пинга"


            buttons = [[
                Button.switch_inline("🔄 Повторить", query="cping", same_peer=False)
            ]]


            result = event.builder.article(
                title=title,
                description="Нажмите, чтобы отправить в чат",
                text=ping_text,
                buttons=buttons,
                parse_mode='markdown'
            )

            await event.answer([result], cache_time=0)

        except Exception as e:
            await kernel.handle_error(e, source="inline_cping", event=None)

    kernel.register_inline_handler('cping', inline_cping)
