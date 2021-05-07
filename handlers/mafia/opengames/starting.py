import asyncio

from loader import dp, bot
from states.registration import OpenGames
from keyboards.default.gender import gender_keyboard
from validation.validation import proccess_validate_name
from aiogram.types import Message, CallbackQuery

@dp.callback_query_handler(lambda callback: callback.data == 'open_games')
async def process_mafia_standart_starting(callback_query: CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                message_id=callback_query.message.message_id,
                                text='''
🙂Понял.
Для начала задам тебе пару жизненно-важных вопросов (без них никак), а далее разберемся.
''')
    await asyncio.sleep(3)
    await OpenGames.name.set()
    await bot.send_message(callback_query.from_user.id, "🔎 Как тебя зовут?\nМожно использовать русские и английские буквы, а также тире")

@dp.message_handler(lambda message: proccess_validate_name(message), state=OpenGames.name)
async def process_month_invalid(message: Message):
    if message.text == "/start":
        await message.reply("Введите, пожалуйста, имя: ")
    else:
        await message.reply("🤔 Странное имя.. А ну, не обманывай меня!")