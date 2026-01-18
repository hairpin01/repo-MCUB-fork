# requires: aiohttp, telethon
# author: TypeFrag (Ported by MCUB Assistant)
# version: 1.1.0
# description: VirusTotal file scanning module for MCUB

import aiohttp
import asyncio
import hashlib
import time
from telethon import Button

def register(kernel):
    
    async def get_config():
        return await kernel.get_module_config(__name__, {
            'virustotal_api_key': ''
        })

    def format_size(size_bytes):
        for unit in ["B", "KB", "MB", "GB"]:
            if size_bytes < 1024:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.2f} TB"

    def create_progress_bar(detections, total):
        if total == 0:
            return "▓" * 20
        percentage = detections / total
        filled = int(percentage * 20)
        empty = 20 - filled
        bar_char = "🟢" if percentage == 0 else "🟡" if percentage < 0.1 else "🟠" if percentage < 0.3 else "🔴"
        return f"{'▓' * filled}{'░' * empty} {bar_char}"

    async def vt_api_request(method, endpoint, api_key, data=None, json_data=False):
        url = f"https://www.virustotal.com/api/v3/{endpoint}"
        headers = {"x-apikey": api_key}
        async with aiohttp.ClientSession() as session:
            if method == 'GET':
                async with session.get(url, headers=headers) as resp:
                    if resp.status == 200:
                        return await resp.json()
                    return None
            elif method == 'POST':
                if json_data:
                    async with session.post(url, headers=headers, json=data) as resp:
                        return await resp.json() if resp.status == 200 else None
                else:
                    async with session.post(url, headers=headers, data=data) as resp:
                        return await resp.json() if resp.status == 200 else None

    @kernel.register_command('setvtkey')
    async def setvtkey_command(event):
        """Установить API ключ VirusTotal"""
        args = event.text.split(maxsplit=1)
        if len(args) < 2:
            await event.edit(
                "❌ <b>Использование:</b> <code>.setvtkey &lt;api_key&gt;</code>",
                parse_mode='html'
            )
            return
        
        api_key = args[1].strip()
        config = await get_config()
        config['virustotal_api_key'] = api_key
        await kernel.save_module_config(__name__, config)
        await event.edit(
            f"✅ <b>API ключ установлен!</b>\n"
            f"<code>{api_key[:10]}...{api_key[-10:] if len(api_key) > 20 else ''}</code>",
            parse_mode='html'
        )

    @kernel.register_command('vtscan')
    async def vtscan_command(event):
        """Просканировать файл через VirusTotal"""
        config = await get_config()
        if not config['virustotal_api_key']:
            await event.edit(
                "🔑 <b>API ключ не установлен!</b>\n"
                "Установите ключ командой: <code>.setvtkey &lt;ваш_api_ключ&gt;</code>\n\n"
                "📝 <i>Получить ключ можно на: https://www.virustotal.com/gui/join-us</i>",
                parse_mode='html'
            )
            return

        reply = await event.get_reply_message()
        if not reply or not reply.file:
            await event.edit(
                "📎 <b>Ответьте на файл для сканирования!</b>",
                parse_mode='html'
            )
            return

        if reply.file.size > 32 * 1024 * 1024:
            await event.edit(
                "📦 <b>Файл слишком большой!</b> (Максимум 32 МБ)",
                parse_mode='html'
            )
            return

        message = await event.edit(
            "📥 <b>Скачиваю файл...</b>",
            parse_mode='html'
        )
        
        try:
            file_data = await reply.download_media(bytes)
            file_hash = hashlib.sha256(file_data).hexdigest()
            file_name = reply.file.name or "unknown_file"
            
            await message.edit(
                "🔍 <b>Проверяю хеш...</b>",
                parse_mode='html'
            )
            
            report = await vt_api_request('GET', f"files/{file_hash}", config['virustotal_api_key'])
            
            if not report:
                await message.edit(
                    "📤 <b>Загружаю на VirusTotal...</b>",
                    parse_mode='html'
                )
                form = aiohttp.FormData()
                form.add_field("file", file_data, filename=file_name)
                upload = await vt_api_request('POST', "files", config['virustotal_api_key'], data=form)
                
                if not upload:
                    await message.edit(
                        "❌ <b>Ошибка загрузки!</b>",
                        parse_mode='html'
                    )
                    return
                
                analysis_id = upload["data"]["id"]
                await message.edit(
                    "🔬 <b>Анализирую...</b>\n<i>Это может занять до 60 секунд</i>",
                    parse_mode='html'
                )
                
                for i in range(60):
                    await asyncio.sleep(5)
                    analysis = await vt_api_request('GET', f"analyses/{analysis_id}", config['virustotal_api_key'])
                    if analysis and analysis["data"]["attributes"]["status"] == "completed":
                        report = await vt_api_request('GET', f"files/{file_hash}", config['virustotal_api_key'])
                        break
                    
                    if i % 5 == 0:  # Каждые 25 секунд обновляем статус
                        await message.edit(
                            f"🔬 <b>Анализирую...</b>\n<i>Прошло {(i+1)*5} секунд</i>",
                            parse_mode='html'
                        )
                else:
                    await message.edit(
                        "❌ <b>Таймаут анализа!</b>",
                        parse_mode='html'
                    )
                    return

            attr = report["data"]["attributes"]
            stats = attr["last_analysis_stats"]
            malicious = stats.get("malicious", 0)
            suspicious = stats.get("suspicious", 0)
            total = sum(stats.values())
            
            detections = malicious + suspicious
            status_text = "🚨 <b>Вредоносный</b>" if malicious > 0 else "⚠️ <b>Подозрительный</b>" if suspicious > 0 else "✅ <b>Безопасный</b>"
            
            result_text = (
                f"🛡 <b>VirusTotal Сканирование</b>\n"
                f"{'━' * 25}\n"
                f"📄 <b>Файл:</b> <code>{file_name}</code>\n"
                f"🔢 <b>Хеш:</b> <code>{file_hash}</code>\n"
                f"📊 <b>Размер:</b> <code>{format_size(reply.file.size)}</code>\n\n"
                f"🔍 <b>Обнаружения:</b> <code>{detections}/{total}</code>\n"
                f"{create_progress_bar(detections, total)}\n\n"
                f"<b>Статус:</b> {status_text}\n"
                f"{'━' * 25}"
            )
            
            vt_link = f"https://www.virustotal.com/gui/file/{file_hash}"
            
            cache_key = f"vt_res_{file_hash}"
            kernel.cache.set(cache_key, {'text': result_text, 'link': vt_link}, ttl=300)
            
            await message.delete()
            
            # Отправляем результат через inline
            success, result_message = await kernel.inline_query_and_click(
                chat_id=event.chat_id,
                query=f"vt_result {file_hash}"
            )
            
            if not success:
                # Если inline не сработал, отправляем обычное сообщение
                await event.client.send_message(
                    event.chat_id,
                    result_text,
                    parse_mode='html',
                    buttons=[[Button.url("🔎 Полный отчет", vt_link)]]
                )

        except Exception as e:
            await kernel.handle_error(e, source="vtscan", event=event)
            await message.edit(
                "❌ <b>Произошла ошибка при сканировании!</b>",
                parse_mode='html'
            )

    async def inline_vt_handler(event):
        """Inline обработчик для результатов VirusTotal"""
        query = event.text.strip()
        if not query.startswith("vt_result "):
            return
            
        file_hash = query.split(" ", 1)[1]
        cache_key = f"vt_res_{file_hash}"
        data = kernel.cache.get(cache_key)
        
        if not data:
            builder = event.builder.article(
                title="VirusTotal Result",
                text="❌ <b>Результат устарел или не найден!</b>\nЗапустите сканирование заново.",
                parse_mode='html'
            )
            await event.answer([builder])
            return

        builder = event.builder.article(
            title="VirusTotal Результат",
            text=data['text'],
            buttons=[[Button.url("🔎 Полный отчет", data['link'])]],
            parse_mode='html'
        )
        await event.answer([builder])

    kernel.register_inline_handler('vt_result', inline_vt_handler)