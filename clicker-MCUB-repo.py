# requires: 
# author: 
# version: 1.0.0
# description: Clicker game module

import json
from telethon import Button

def register(kernel):
    async def get_user_data(user_id):
        data_json = await kernel.db_get('clicker', f'user_{user_id}')
        if data_json:
            return json.loads(data_json)
        return {'score': 0, 'level': 1, 'click_power': 1, 'upgrade_cost': 10}

    async def save_user_data(user_id, data):
        await kernel.db_set('clicker', f'user_{user_id}', json.dumps(data))

    async def clicker_inline_handler(event):
        user_id = event.sender_id
        user_data = await get_user_data(user_id)
        
        text = f"🔢 <b>Clicker Game</b>\n\n"
        text += f"💰 <b>Score:</b> {user_data['score']}\n"
        text += f"⚡ <b>Click Power:</b> {user_data['click_power']}\n"
        text += f"📈 <b>Level:</b> {user_data['level']}\n"
        text += f"🛒 <b>Upgrade Cost:</b> {user_data['upgrade_cost']}"
        
        buttons = [
            [Button.inline(f"🖱️ Click (+{user_data['click_power']})", f"clicker_click:{user_id}".encode())],
            [Button.inline(f"⚡ Upgrade ({user_data['upgrade_cost']} points)", f"clicker_upgrade:{user_id}".encode())],
            [Button.inline("🔄 Refresh", f"clicker_refresh:{user_id}".encode())]
        ]
        
        builder = event.builder.article(
            title="Clicker Game",
            text=text,
            buttons=buttons,
            parse_mode='html'
        )
        await event.answer([builder])

    kernel.register_inline_handler('clicker', clicker_inline_handler)

    @kernel.register_command('clicker')
    async def clicker_command_handler(event):
        try:
            bot_username = kernel.config.get('inline_bot_username')
            if bot_username:
                results = await kernel.client.inline_query(bot_username, 'clicker')
                if results:
                    await results[0].click(event.chat_id, reply_to=event.reply_to_msg_id)
                    await event.delete()
                else:
                    await event.edit("❌ Не удалось запустить инлайн-режим")
            else:
                await event.edit("❌ Инлайн-бот не настроен")
        except Exception as e:
            await kernel.handle_error(e, source="clicker_command", event=event)

    async def clicker_callback_handler(event):
        data = event.data.decode()
        if not data.startswith('clicker_'):
            return
            
        parts = data.split(':')
        if len(parts) != 2:
            return
            
        action, callback_user_id = parts
        user_id = event.sender_id
        
        if str(user_id) != callback_user_id:
            await event.answer("❌ Это не ваша игра!", alert=True)
            return
            
        user_data = await get_user_data(user_id)
        
        if action == 'clicker_click':
            user_data['score'] += user_data['click_power']
            await save_user_data(user_id, user_data)
            
        elif action == 'clicker_upgrade':
            if user_data['score'] >= user_data['upgrade_cost']:
                user_data['score'] -= user_data['upgrade_cost']
                user_data['level'] += 1
                user_data['click_power'] = user_data['level']
                user_data['upgrade_cost'] = user_data['level'] * 10
                await save_user_data(user_id, user_data)
            else:
                await event.answer(f"❌ Не хватает {user_data['upgrade_cost'] - user_data['score']} очков!", alert=True)
                return
        
        text = f"🔢 <b>Clicker Game</b>\n\n"
        text += f"💰 <b>Score:</b> {user_data['score']}\n"
        text += f"⚡ <b>Click Power:</b> {user_data['click_power']}\n"
        text += f"📈 <b>Level:</b> {user_data['level']}\n"
        text += f"🛒 <b>Upgrade Cost:</b> {user_data['upgrade_cost']}"
        
        buttons = [
            [Button.inline(f"🖱️ Click (+{user_data['click_power']})", f"clicker_click:{user_id}".encode())],
            [Button.inline(f"⚡ Upgrade ({user_data['upgrade_cost']} points)", f"clicker_upgrade:{user_id}".encode())],
            [Button.inline("🔄 Refresh", f"clicker_refresh:{user_id}".encode())]
        ]
        
        try:
            await event.edit(text, buttons=buttons, parse_mode='html')
        except:
            await event.answer("✅ Обновлено!", alert=False)
    
    kernel.register_callback_handler('clicker_', clicker_callback_handler)