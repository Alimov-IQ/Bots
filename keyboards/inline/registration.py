from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice_mafia_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton("Корпоратив или День рождения", callback_data="standart")
        ],
        [
            InlineKeyboardButton("Premium mafia", callback_data="premium")
        ],
        [
            InlineKeyboardButton("Открытые игры", callback_data="open_games")
        ],
    ]
)

choice_mafia_restart_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton("Корпоратив или День рождения", callback_data="standart_restart")
        ],
        [
            InlineKeyboardButton("Premium mafia", callback_data="premium_restart")
        ],
        [
            InlineKeyboardButton("Открытые игры", callback_data="open_games_restart")
        ],
    ]
)

menu_services_keyboard = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton("Цена мафия", callback_data="price"),
            InlineKeyboardButton("Цена квиз", callback_data="quiz"),
        ],
    ]
)