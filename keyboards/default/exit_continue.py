from aiogram.types import   ReplyKeyboardMarkup, KeyboardButton

ec_keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton("Назад"),
            KeyboardButton("Продолжить")
        ],
    ]
)
