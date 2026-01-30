# requires: aiohttp
# author: @Hairpin01
# version: 1.0.3
# description: пинг в инлайне

import time
import asyncio
from telethon import events, Button

def register(kernel):
    client = kernel.client


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

    @kernel.register_command('cping')
    # cping
    async def inline_cping(event):

        try:
            ping_result = await ping_api_telegram()


            if isinstance(ping_result, (int, float)):
                ping_text = f"<b>📶 Пинг до Telegram API:</b> <code>{ping_result}</code> мс"
            else:
                ping_text = f"<b>❌ Ошибка:</b> {ping_result}"


            buttons = [
                {"text": "Повторить", "type": "callback", "data": "cping"}
            ]

            success = await kernel.inline_form(
                event.chat_id,
                title=ping_text,
                buttons=buttons
            )
            if success:
                await event.delete()


        except Exception as e:
            await kernel.handle_error(e, source="inline_cping", event=event)

    async def callback_cping(event):
        ping_result = await ping_api_telegram()

        if isinstance(ping_result, (int, float)):
            ping_text = f"<b>📶 Пинг до Telegram API:</b> <code>{ping_result}</code> мс"
        else:
            ping_text = f"<b>❌ Ошибка:</b> {ping_result}"

        await event.edit(ping_text, buttons=buttons, parse_mode='html')
        buttons = [
            [
                Button.inline("Повторить", b"cping")
            ]
        ]

    kernel.register_callback_handler("cping", callback_cping)
