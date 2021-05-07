from loader import dp
from states.registration import StandartMafiaForm
from keyboards.default import choice_month_keyboard
from validation.validation import proccess_validate_month

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


@dp.message_handler(state=StandartMafiaForm.gender)
async def proccess_question_month(message: Message, state=FSMContext):
    async with state.proxy() as data:
        if message.text == "Мужской":
            data['gender'] = "man"
        if message.text == "Женский":
            data['gender'] = "woman"
    await StandartMafiaForm.next()
    await message.answer("📅 Выбери месяц своего рождения", reply_markup=choice_month_keyboard)


@dp.message_handler(lambda message: proccess_validate_month(message), state=StandartMafiaForm.month)
async def process_month_invalid(message: Message):
    await message.reply("🤔 Что-то я не слышал о таком месяце")