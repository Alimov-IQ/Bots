from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

choice_month_keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Сентябрь"),
            KeyboardButton(text="Октябрь"),
            KeyboardButton(text="Ноябрь"),
        ],
        [
            KeyboardButton(text="Декабрь"),
            KeyboardButton(text="Январь"),
            KeyboardButton(text="Февраль"),
        ],
        [
            KeyboardButton(text="Март"),
            KeyboardButton(text="Апрель"),
            KeyboardButton(text="Май"),
        ],
        [
            KeyboardButton(text="Июнь"),
            KeyboardButton(text="Июль"),
            KeyboardButton(text="Август"),
        ]
    ],
    resize_keyboard=True
)
days_31_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=kb)] for kb in range(32) if kb > 0])
days_30_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=kb)] for kb in range(31) if kb > 0])
days_28_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=kb)] for kb in range(29) if kb > 0])
