# author: @Hicota
# version: 1.0.0
# description: Удаление сообщений с защитой содержимого

import asyncio

def register(kernel):
    client = kernel.client
    
    @kernel.register_command('del')
    async def del_handler(event):
        try:
            args = event.text.split()
            reply = await event.get_reply_message()
            my_id = (await client.get_me()).id
            
            if reply:
                # Режим 1: удаление сообщения по реплаю
                if reply.sender_id == my_id and not reply.sticker:
                    try:
                        await reply.edit("###")
                    except:
                        pass
                
                try:
                    await reply.delete()
                    
                    await event.delete()
                    
                except Exception as e:
                    await kernel.handle_error(e, source="del_reply", event=event)
                    await event.edit("❌ Не удалось удалить сообщение")
                    
            elif len(args) > 1 and args[1].isdigit():
                # Режим 2: удаление N сообщений
                count = int(args[1])
                if count <= 0:
                    await event.edit("❌ Укажите положительное число")
                    return
                
                await event.edit(f"🪄")
                
                deleted_count = 0
                messages = []
                
                # Получаем сообщения (включая команду)
                async for message in client.iter_messages(
                    event.chat_id,
                    max_id=event.id,
                    limit=count
                ):
                    messages.append(message)
                
                # Удаляем в порядке от старых к новым
                for msg in reversed(messages):
                    # Проверяем, что сообщение не является стикером перед редактированием
                    if msg.sender_id == my_id and not msg.sticker:
                        try:
                            await msg.edit("###")
                        except:
                            pass
                    
                    try:
                        await msg.delete()
                        deleted_count += 1
                    except:
                        pass
                    
                    await asyncio.sleep(0.5)
                
                await event.edit(f"✅ Удалено {deleted_count} сообщений")
                await asyncio.sleep(2)
                await event.delete()
                
            else:
                await event.edit("❌ Используйте: .del [ответ] или .del [число]")
                
        except Exception as e:
            await kernel.handle_error(e, source="del_handler", event=event)
            await event.edit("❌ Ошибка при удалении")