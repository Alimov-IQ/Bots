from loader import dp
from states.registration import OpenGames
from keyboards.default import empty_keyboard
from keyboards.default.gender import gender_keyboard
from validation.validation import proccess_validate_name

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


@dp.message_handler(state=OpenGames.name)
async def proccess_question_month(message: Message, state=FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await OpenGames.next()
    await message.answer("🌀 Выбери свой пол:", reply_markup=gender_keyboard)


@dp.message_handler(lambda message: message.text not in ['Мужской', 'Женский'], state=OpenGames.gender)
async def process_gender_invalid(message: Message):
    await message.reply("🤔 Странный пол.. А ну, не обманывай меня!")