from loader import dp, bot
from utils.database.database import proccess_insert_user
from keyboards.default import empty_keyboard
from keyboards.default.exit_continue import ec_keyboard
from keyboards.default.menu import menu_keyboard_without_events
from states.registration import OpenGames

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext



@dp.message_handler(state=OpenGames.day)
async def proccess_mafia_standart_finishing(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['day'] = message.text
       if data['gender'] == "man":
            if data['month'] == 'Март':
                await message.answer(f'''
✏️ Убедись в том, что данные верны
Твое имя: {data['name']}
Твой пол: мужской
Дата рождения: {data['day']} марта
    ''', reply_markup=ec_keyboard)

            elif data['month'] == 'Август':
                await message.answer(f'''
✏️ Убедись в том, что данные верны
Твое имя: {data['name']}
Твой пол: мужской
Дата рождения: {data['day']} августа
    ''', reply_markup=ec_keyboard)
            else:
                await message.answer(f'''
✏️ Убедись в том, что данные верны
Твое имя: {data['name']}
Твой пол: мужской
Дата рождения: {data['day']} {data['month'].lower()[:-1]}я
        ''', reply_markup=ec_keyboard)


        if data['gender'] == "woman":
            if data['month'] == 'Март':
                            await message.answer(f'''
 ✏️ Убедись в том, что данные верны
Твое имя: {data['name']}
Твой пол:  женский
Дата рождения: {data['day']} марта
                ''', reply_markup=ec_keyboard)

                        elif data['month'] == 'Август':
                            await message.answer(f'''
✏️ Убедись в том, что данные верны
Твое имя: {data['name']}
Твой пол:  женский
Дата рождения: {data['day']} августа
                ''', reply_markup=ec_keyboard)
                        else:
                            await message.answer(f'''
✏️ Убедись в том, что данные верны
Твое имя: {data['name']}
Твой пол: женский
Дата рождения: {data['day']} {data['month'].lower()[:-1]}я
                    ''', reply_markup=ec_keyboard)
    await OpenGames.next()


@dp.message_handler(lambda message: message.text == "Назад",state=OpenGames.correct)
async def proccess_mafia_standart_exit(message: Message, state: FSMContext):
    async with state.proxy() as _:
        await state.finish()
        await OpenGames.name.set()
        await message.answer("🔎 Как тебя зовут?", reply_markup=empty_keyboard)


@dp.message_handler(lambda message: message.text == "Продолжить",state=OpenGames.correct)
async def proccess_mafia_standart_continue(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await proccess_insert_user(message.from_user.id,
                                   data['name'],
                                   data['gender'],
                                   "opengames",
                                   data['day'],
                                   data['month'])
        await message.answer(f'''
👋🏻 {data['name']}, добро пожаловать в нашу семью!

😌 Держи меню. Тебе стоит ознакомиться:
''', reply_markup=menu_keyboard_without_events)
    await state.finish()
        
