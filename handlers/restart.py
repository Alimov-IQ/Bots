from loader import dp, bot
from utils.database.database import proccess_find_user_by_id, proccess_update_user_mafia_by_id
from keyboards.inline.registration import choice_mafia_restart_keyboard
from keyboards.default.menu import menu_keyboard, menu_keyboard_without_events
from keyboards.default import empty_keyboard
from states.registration import PremiumMafiaRestart

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(lambda message: message.text == "Сменить мероприятие" or message.text == "/restart")
async def proccess_restart_bot(message: types.Message):
    id = message.from_user.id
    user = await proccess_find_user_by_id(id)
    if user == None:
        await message.answer("Вы еще не зарегистрированы.")
    else:
        await message.answer("🌀Выберите необходимое мероприятие", reply_markup=choice_mafia_restart_keyboard)


@dp.callback_query_handler(lambda callback: callback.data == 'standart_restart')
async def process_mafia_standart_restart(callback_query: types.CallbackQuery):
    id = callback_query.from_user.id
    user = await proccess_find_user_by_id(id)
    if user == None:
        await bot.send_message(id, "Тебе стоит зарегистрироваться")
    else:
        if user['mafia'] == "standart":
            await bot.edit_message_text(chat_id=id, message_id=callback_query.message.message_id,text= '''
❗️Вы, похоже, ошиблись. 

Вы уже находитесь в данном виде мероприятия.
''',reply_markup=choice_mafia_restart_keyboard)
        else:
            await proccess_update_user_mafia_by_id(id, "standart", user)
            await bot.delete_message(chat_id=id, message_id=callback_query.message.message_id)
            await bot.send_message(id, f"😌 Хорошо, {user['name']}. Вид мероприятия изменен.", reply_markup=menu_keyboard)

@dp.callback_query_handler(lambda callback: callback.data == 'open_games_restart')
async def process_mafia_open_games_restart(callback_query: types.CallbackQuery):
    id = callback_query.from_user.id
    user = await proccess_find_user_by_id(id)
    if user == None:
        await bot.send_message(id, "Тебе стоит зарегистрироваться")
    else:
        if user['mafia'] == "opengames":
            await bot.edit_message_text(chat_id=id, message_id=callback_query.message.message_id,text= '''
❗️Вы, похоже, ошиблись. 

Вы уже находитесь в данном виде мероприятия.
''',reply_markup=choice_mafia_restart_keyboard)
        else:
            await proccess_update_user_mafia_by_id(id, "opengames", user)
            await bot.delete_message(chat_id=id, message_id=callback_query.message.message_id)
            await bot.send_message(id, f"😌 Хорошо, {user['name']}. Вид мероприятия изменен.", reply_markup=menu_keyboard_without_events)

@dp.callback_query_handler(lambda callback: callback.data == 'premium_restart')
async def process_mafia_premium_restart(callback_query: types.CallbackQuery):
    id = callback_query.from_user.id
    user = await proccess_find_user_by_id(id)
    if user == None:
        await bot.send_message(id, "Тебе стоит зарегистрироваться")
    else:
        if user['mafia'] == "premium":
            await bot.edit_message_text(chat_id=id, message_id=callback_query.message.message_id,text= '''
❗️Вы, похоже, ошиблись. 

Вы уже находитесь в данном виде мероприятия.
''',reply_markup=choice_mafia_restart_keyboard)
        else:
            await PremiumMafiaRestart.instagram.set()
            await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                message_id=callback_query.message.message_id,
                                text="Введи свой instagram: ")

@dp.message_handler(state=PremiumMafiaRestart.instagram)
async def process_write_instagram(message: types.Message, state=FSMContext): 
    id = message.from_user.id
    user = await proccess_find_user_by_id(id)
    async with state.proxy() as _:
        name = await proccess_update_user_mafia_by_id(id, "premium", user, message.text)
        await bot.send_message(id, f"😌 Хорошо, {name}. Вид мероприятия изменен.",
                                    reply_markup=menu_keyboard_without_events)
    await state.finish()