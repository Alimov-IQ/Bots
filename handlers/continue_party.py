from loader import dp, bot, client
from utils.database.database import proccess_find_user_by_id
from states.registration import Phone
from validation.validation import  proccess_validate_phone
from keyboards.default import phone_keyboard
from keyboards.default.menu import menu_keyboard

from aiogram.types import CallbackQuery, Message, ParseMode
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(lambda callback: callback.data == "continue_party")
async def continue_party(callback: CallbackQuery):
    await Phone.phone.set()
    await bot.edit_message_text(message_id=callback.message.message_id,chat_id=callback.from_user.id,text= "Введи свой номер телефона\nПример: +375250000000")
    await bot.send_message(callback.from_user.id, "Или нажми на кнопку", reply_markup=phone_keyboard)


@dp.message_handler(content_types="contact", state=Phone.phone)
async def phone_get(message: Message, state=FSMContext):
    match = proccess_validate_phone("+" + str(message.contact.phone_number))
    if match == False:
        id = message.from_user.id
        user = await proccess_find_user_by_id(id)
        await message.answer(f'''
😎Отлично, {user['name']}!

📝Я передал твои контакты нашему менеджеру, скоро с тобой свяжутся.

🔎А пока, можешь посмотреть список услуг и цены, для этого, нажми кнопку "Услуги"   
''',reply_markup=menu_keyboard)    
        await want_party_user(id, user, "+" + message.contact.phone_number)
        await state.finish()
    else:
         await message.reply("🤔 Странный номер..\nПроверь на корректность.\nПример: +375250000000")


@dp.message_handler(lambda message: proccess_validate_phone(message.text), state=Phone.phone)
async def process_phone_invalid(message: Message):
        await message.reply("🤔 Странный номер..\nПроверь на корректность.\nПример: +375250000000")

@dp.message_handler(state=Phone.phone)
async def proccess_phone_set(message: Message, state=FSMContext):
    async with state.proxy() as _:
        id = message.from_user.id
        user = await proccess_find_user_by_id(id)
        await bot.send_message(id,f'''
😎Отлично, {user['name']}!

📝Я передал твои контакты нашему менеджеру, скоро с тобой свяжутся.

🔎А пока, можешь посмотреть список услуг и цены, для этого, нажми кнопку "Услуги"   
        ''', reply_markup=menu_keyboard)
        await want_party_user(id, user, message.text)
    await state.finish()

async def want_party_user(id, user, phone):
    async with client:
        await client.send_message('sergeyiskander', f'''
[{user['name']}](tg://user?id={user['user_id']}) заинтересовался нашими услугами.
Его номер телефона:  {phone}
''', parse_mode="markdown")