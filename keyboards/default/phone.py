from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

phone_keyboard = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton("Отправить свой номер",request_contact=True)
        ]
    ]
)