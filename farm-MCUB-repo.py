# author: @Hicota
# version: 1.1.1
# description: Автоматический фарминг сообщений с отслеживанием ответов

import asyncio
import time
import re
from telethon import events

def register(kernel):
    client = kernel.client

    kernel.config.setdefault('farm_chat', None)
    kernel.config.setdefault('farm_enabled', False)
    kernel.config.setdefault('next_farm_time', 0)
    kernel.config.setdefault('farm_bot_id', None)

    farm_task = None
    last_farm_times = {}

    def parse_wait_time(text):
        """Парсит время ожидания из текста ответа бота"""
        pattern = r'(?:(\d+)\s*час(?:а|ов)?)?\s*(?:(\d+)\s*мин)?'
        match = re.search(pattern, text)
        if match:
            hours = int(match.group(1)) if match.group(1) else 0
            minutes = int(match.group(2)) if match.group(2) else 0
            total_seconds = (hours * 3600) + (minutes * 60)
            if total_seconds > 0:
                return total_seconds
        return 4 * 3600

    async def message_handler(event):
        """Обработчик ответов от бота фарма"""
        try:
            farm_chat = kernel.config.get('farm_chat')
            if not farm_chat or event.chat_id != farm_chat:
                return

            text = event.raw_text
            if not text:
                return

            # Проверяем, что это сообщение от бота или содержит ключевые слова
            if "НЕЗАЧЁТ" not in text and "ЗАЧЁТ" not in text:
                return

            # Проверяем, было ли наше сообщение отправлено недавно (в течение 30 секунд)
            if event.chat_id in last_farm_times:
                sent_time = last_farm_times[event.chat_id]
                if time.time() - sent_time < 30:
                    # Устанавливаем ID бота при первом ответе
                    current_bot_id = kernel.config.get('farm_bot_id')
                    if current_bot_id is None:
                        kernel.config['farm_bot_id'] = event.sender_id
                        kernel.save_config()

                    # Проверяем, что сообщение от бота (если ID уже установлен)
                    if current_bot_id is None or event.sender_id == current_bot_id:
                        wait_seconds = parse_wait_time(text)
                        next_time = time.time() + wait_seconds
                        kernel.config['next_farm_time'] = next_time
                        kernel.save_config()

                        # Удаляем запись, чтобы не обрабатывать повторно
                        last_farm_times.pop(event.chat_id, None)

                        hours = wait_seconds // 3600
                        minutes = (wait_seconds % 3600) // 60
                        await kernel.send_log_message(
                            f"Фарм: получен ответ от бота, следующая отправка через {hours}ч {minutes}м"
                        )
                else:
                    # Удаляем старую запись
                    last_farm_times.pop(event.chat_id, None)
        except Exception as e:
            await kernel.handle_error(e, source="farm_message_handler", event=event)

    client.on(events.NewMessage(incoming=True))(message_handler)

    async def farm_loop():
        """Основной цикл фарминга"""
        nonlocal farm_task
        try:
            while kernel.config.get('farm_enabled', False):
                next_time = kernel.config.get('next_farm_time', 0)
                now = time.time()

                if now < next_time:
                    await asyncio.sleep(1)
                    continue

                farm_chat = kernel.config.get('farm_chat')
                if not farm_chat:
                    await asyncio.sleep(10)
                    continue

                try:
                    await client.send_message(farm_chat, "фарма")
                    # Запоминаем время отправки нашего сообщения
                    last_farm_times[farm_chat] = time.time()

                    # Устанавливаем время следующей отправки по умолчанию (на случай, если не получим ответ)
                    default_next = now + 4 * 3600
                    kernel.config['next_farm_time'] = default_next
                    kernel.save_config()

                    await kernel.send_log_message("Фарм: отправлено сообщение 'фарма'")
                except Exception as e:
                    await kernel.handle_error(e, source="farm_loop", event=None)

                await asyncio.sleep(5)
        except asyncio.CancelledError:
            pass
        except Exception as e:
            await kernel.handle_error(e, source="farm_loop", event=None)

    @kernel.register_command('farm')
    async def farm_handler(event):
        """Управление фармингом"""
        nonlocal farm_task
        try:
            args = event.text.split()

            if len(args) < 2:
                await event.edit("Используйте: .farm id <chat_id> | on | off | status | botid")
                return

            subcmd = args[1]

            if subcmd == 'id':
                if len(args) < 3:
                    await event.edit("Укажите ID чата")
                    return
                try:
                    chat_id = int(args[2])
                    kernel.config['farm_chat'] = chat_id
                    kernel.save_config()
                    await event.edit(f"Чат для фарма установлен: {chat_id}")
                except ValueError:
                    await event.edit("ID чата должен быть числом")

            elif subcmd == 'on':
                if kernel.config.get('farm_enabled', False):
                    await event.edit("Фарм уже включен")
                    return

                if not kernel.config.get('farm_chat'):
                    await event.edit("Сначала установите чат для фарма: .farm id <chat_id>")
                    return

                kernel.config['farm_enabled'] = True
                kernel.save_config()

                farm_task = asyncio.create_task(farm_loop())
                await event.edit("Фарм включен")

            elif subcmd == 'off':
                if not kernel.config.get('farm_enabled', False):
                    await event.edit("Фарм уже выключен")
                    return

                kernel.config['farm_enabled'] = False
                kernel.save_config()

                if farm_task:
                    farm_task.cancel()
                    farm_task = None
                await event.edit("Фарм выключен")

            elif subcmd == 'status':
                status = "✅ Включен" if kernel.config.get('farm_enabled', False) else "❌ Выключен"
                chat_id = kernel.config.get('farm_chat')
                chat_info = f"Чат: {chat_id}" if chat_id else "Чат не установлен"

                bot_id = kernel.config.get('farm_bot_id')
                bot_info = f"ID бота: {bot_id}" if bot_id else "ID бота не определен"

                next_time = kernel.config.get('next_farm_time', 0)
                now = time.time()
                if next_time > now:
                    wait = next_time - now
                    wait_str = f"{int(wait // 3600)}ч {int(wait % 3600 // 60)}м"
                else:
                    wait_str = "сейчас"

                await event.edit(f"{status}\n{chat_info}\n{bot_info}\nСледующая отправка: {wait_str}")

            elif subcmd == 'botid':
                if len(args) < 3:
                    bot_id = kernel.config.get('farm_bot_id')
                    await event.edit(f"Текущий ID бота: {bot_id if bot_id else 'не установлен'}")
                else:
                    try:
                        bot_id = int(args[2])
                        kernel.config['farm_bot_id'] = bot_id
                        kernel.save_config()
                        await event.edit(f"ID бота установлен: {bot_id}")
                    except ValueError:
                        await event.edit("ID бота должен быть числом")

            else:
                await event.edit("Неизвестная подкоманда. Используйте: id, on, off, status, botid")

        except Exception as e:
            await kernel.handle_error(e, source="farm_handler", event=event)
            await event.edit("❌ Ошибка в команде фарма")
