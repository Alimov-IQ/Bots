from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

gender_keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Мужской"),
        ],
        [
            KeyboardButton(text="Женский"),
        ]
    ],
    resize_keyboard=True
)