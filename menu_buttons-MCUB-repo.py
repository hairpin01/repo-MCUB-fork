from telethon import events, Button

def register(kernel):
    client = kernel.client
    @kernel.register_command('menu_button')
    async def menu_cmd(event):
        buttons = [
            {"text": "1 <tg-emoji emoji-id=\"5404728536810398694\">🧊</tg-emoji>", "type": "callback", "data": "menu_page_1"},
            {"text": "2 <tg-emoji emoji-id=\"5404728536810398694\">🧊</tg-emoji>", "type": "callback", "data": "menu_page_2"}
        ]
        success = await kernel.inline_form(
            event.chat_id,
            "мэню",
            buttons=buttons
        )
        if success:
            await event.delete()
    async def menu_callback_handler(event):
        data = event.data
        if data == 'menu_page_1':
            buttons = [
                [
                    Button.inline("назад <tg-emoji emoji-id=\"5404728536810398694\">🧊</tg-emoji>", b"main_menu")
                ]
            ]
            await event.edit(
                "перви меню",
                buttons=buttons
            )
        elif data == 'menu_page_2':
            buttons = [
                [
                    Button.inline("назад <tg-emoji emoji-id=\"5404728536810398694\">🧊</tg-emoji>", b"main_menu")
                ]
            ]
            await event.edit(
                "втарое меню",
                buttons=buttons
            )
        else:
            buttons = [
            [
                Button.inline("1 <tg-emoji emoji-id=\"5404728536810398694\">🧊</tg-emoji>", b"menu_page_1")
            ],
            [
                Button.inline("2 <tg-emoji emoji-id=\"5404728536810398694\">🧊</tg-emoji>", b"menu_page_2")
            ]
            ]
            await event.edit(
                "мэню",
                buttons=buttons
            )

    kernel.register_callback_handler("menu_", menu_callback_handler)
