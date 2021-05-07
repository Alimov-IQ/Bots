from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_events_keyboard(data: list, mafia: str):
    return InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(data[x]['name'],url=data[x]['link'])] for x in range(len(data)) if data[x]['mafia'] == mafia]
)

async def get_event_button(data: list):
    return InlineKeyboardMarkup(
        inline_keyboard = [
            [
                InlineKeyboardButton("Перейти в беседу", url=data['link'])
            ]
        ]
    )