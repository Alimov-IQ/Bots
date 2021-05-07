from loader import dp
from states.registration import PremiumMafiaForm
from validation.validation import proccess_validate_day
from keyboards.default import (
    days_31_keyboard,
    days_30_keyboard,
    days_28_keyboard
)

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


@dp.message_handler(state=PremiumMafiaForm.month)
async def process_question_day(message: Message, state: FSMContext):
    async with state.proxy() as data:
        month = message.text
        data['month'] = month
        if  month == 'Январь' or month == 'Март' or month == 'Май' \
        or month == 'Июль' or month == 'Август' or month == 'Октябрь' \
        or month == 'Декабрь':
            await message.answer('''
        📅 Выбери день своего рождения
        ''', reply_markup=days_31_keyboard)
        elif month == 'Февраль':
            await message.answer('''
        📅 Выбери день своего рождения
        ''', reply_markup=days_28_keyboard)
        else:
            await message.answer('''
        📅 Выбери день своего рождения
        ''', reply_markup=days_30_keyboard)
    await PremiumMafiaForm.next()


@dp.message_handler(lambda message: proccess_validate_day(message), state=PremiumMafiaForm.day)
async def process_day_invalid(message: Message):
    await message.reply("Ошибка.\nВведите день заново:")