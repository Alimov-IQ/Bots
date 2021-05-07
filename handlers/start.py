from loader import dp
from utils.database.database import proccess_find_user_by_id, process_delete_user_by_id

from aiogram import types
from keyboards.inline import choice_mafia_keyboard

@dp.message_handler(commands=["start"])
async def proccess_start_bot(message: types.Message):
    data = await proccess_find_user_by_id(message.from_user.id)
    if data == None:
        await message.answer('''
👋🏻Привет! Я бот Mafia Vero

📖Не буду говорить о себе, думаю, ты знаешь, зачем мне пишешь.\nВыбери вид мафии, который тебе интересен    
    ''', reply_markup=choice_mafia_keyboard)
    else:
        await message.answer("Ты уже зарегистрирован")
        
        await process_delete_user_by_id(message.from_user.id)