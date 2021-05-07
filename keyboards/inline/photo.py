from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

photo_keyboard = InlineKeyboardMarkup(
    inline_keyboard= [ 
        [
            InlineKeyboardButton("Еще фотки", callback_data="photos")
        ],
    ]
)