from loader import dp
from states.registration import PremiumMafiaForm
from validation.validation import proccess_validate_day
from keyboards.default import empty_keyboard

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


@dp.message_handler(state=PremiumMafiaForm.day)
async def process_question_instagram(message: Message, state: FSMContext):
    async with state.proxy() as data:
        print(data)
        data['day'] = message.text
        await message.answer("Введите свой instagram:", reply_markup=empty_keyboard)
    await PremiumMafiaForm.next()


'''
@dp.message_handler(lambda message: proccess_validate_day(message), state=PremiumMafiaForm.day)
async def process_day_invalid(message: Message):
    await message.reply("Ошибка.\nВведите день заново:")
'''