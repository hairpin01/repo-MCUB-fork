# author: @Mitrichq 
# version: 1.0.0
# description: имитация действий пользователя

import asyncio
from telethon.tl.functions.messages import SetTypingRequest
from telethon.tl.types import (
    SendMessageTypingAction,
    SendMessageCancelAction,
    SendMessageRecordVideoAction,
    SendMessageRecordAudioAction,
    SendMessageUploadVideoAction,
    SendMessageUploadAudioAction,
    SendMessageUploadPhotoAction,
    SendMessageUploadDocumentAction,
    SendMessageGamePlayAction
)

fake_tasks = {}

ACTIONS = {
    'typing': SendMessageTypingAction,
    'video': SendMessageRecordVideoAction,
    'audio': SendMessageRecordAudioAction,
    'voice': SendMessageRecordAudioAction,
    'uploadvideo': SendMessageUploadVideoAction,
    'uploadaudio': SendMessageUploadAudioAction,
    'photo': SendMessageUploadPhotoAction,
    'document': SendMessageUploadDocumentAction,
    'game': SendMessageGamePlayAction
}

def register(kernel):
    client = kernel.client

    async def fake_action_loop(client, chat_id, action, duration):
        end_time = asyncio.get_event_loop().time() + (duration * 60)

        try:
            while asyncio.get_event_loop().time() < end_time:
                await client(SetTypingRequest(peer=chat_id, action=action()))
                await asyncio.sleep(4)
        except asyncio.CancelledError:
            await client(SetTypingRequest(peer=chat_id, action=SendMessageCancelAction()))
            raise

    @kernel.register_command('fake')
    # имитация действий пользователя
    async def fake_handler(event):
        global fake_tasks

        args = event.text.split()
        if len(args) < 2:
            await event.edit('⛈️ Использование: .fake действие [время_в_минутах] или .fake cancel')
            return

        action_name = args[1].lower()

        if action_name == 'cancel':
            if event.chat_id in fake_tasks:
                fake_tasks[event.chat_id].cancel()
                del fake_tasks[event.chat_id]
                await event.edit('✅ Фейковые действия отменены')
            else:
                await event.edit('⛈️ Нет активных фейковых действий')
            return

        if action_name not in ACTIONS:
            actions_list = ', '.join(ACTIONS.keys())
            await event.edit(f'⛈️ Неизвестное действие\n\nДоступные: {actions_list}, cancel')
            return

        if len(args) < 3:
            await event.edit('⛈️ Укажите время в минутах\n\nПример: .fake typing 5')
            return

        try:
            duration = float(args[2])
            if duration <= 0:
                await event.edit('⛈️ Время должно быть больше 0')
                return
        except ValueError:
            await event.edit('⛈️ Неверный формат времени')
            return

        if event.chat_id in fake_tasks:
            fake_tasks[event.chat_id].cancel()

        action = ACTIONS[action_name]
        task = asyncio.create_task(fake_action_loop(client, event.chat_id, action, duration))
        fake_tasks[event.chat_id] = task

        await event.edit(f'✅ Имитация "{action_name}" запущена на {duration} мин')

        try:
            await task
            if event.chat_id in fake_tasks:
                del fake_tasks[event.chat_id]
        except asyncio.CancelledError:
            pass
