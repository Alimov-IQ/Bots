from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Генератор никнеймов"),
            KeyboardButton(text="Услуги"),
        ],
        [
            KeyboardButton(text="Контакты"),
            KeyboardButton(text="Правила игры"),
        ],
        [
            KeyboardButton(text="Мероприятия"),
            KeyboardButton(text="Сменить мероприятие"),
        ],
        [
            KeyboardButton(text="Фото и Видео")
        ],
    ],
    resize_keyboard=True
)

menu_keyboard_without_events =  ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Генератор никнеймов"),
            KeyboardButton(text="Услуги"),
        ],
        [
            KeyboardButton(text="Контакты"),
            KeyboardButton(text="Правила игры"),
        ],
        [
            KeyboardButton(text="Сменить мероприятие")
        ],
        [
            KeyboardButton(text="Фото и Видео")
        ]
    ],
    resize_keyboard=True
)

