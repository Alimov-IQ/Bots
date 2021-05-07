import asyncio

from loader import bot, client
from config import API_ID_USER, API_HASH_USER
from utils.invitation.invitation import after_day, after_month, today_day, today_month
from utils.database.database import proccess_find_by_day_and_month, proccess_find_by_day_and_month_premium

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tasks = []


async def send_message_manager(manager_id: int, user):
    async with client:
        await client.send_message(manager_id, f'''
Через 3 недели у человека с именем [{user['name']}](tg://user?id={user['user_id']}) день рождения.''')


async def proccess_send_all(user):
    tasks.append(asyncio.create_task(bot.send_message(user['user_id'],
                                         f'''
👋🏻Привет, {user['name']}!

😌Помнишь, мы познакомились с тобой на мафии? Я вот тебя помню.
Заметил, у тебя скоро праздник, а что, если мы организуем тебе суперский день рождения с игрой?

🔥Хочешь удивить друзей, получить гору эмоций? Нажимай кнопку, и передам твой запрос менеджеру!
                                         ''', reply_markup=InlineKeyboardMarkup(
                                             inline_keyboard= [
                                                 [
                                                     InlineKeyboardButton("Продолжить", callback_data="continue_party")
                                                 ]
                                             ]
                                         ))))
    tasks.append(asyncio.create_task(send_message_manager('sergeyiskander', user)))                                
    await asyncio.gather(*tasks)


async def proccess_send_manager_premium(user):
    async with client:
        await client.send_message('sergeyiskander', f'''
Уже совсем скоро у человека с именем [{user['name']}](tg://user?id={user['user_id']}) день рождения, это наш премиум игрок! Не забудьте его поздравить.

Его instagram: https://www.instagram.com/{user['instagram']}
''')




async def main(): 
    
    users = await proccess_find_by_day_and_month(after_day, after_month)
    for function in asyncio.as_completed(map(proccess_send_all, users)):
        await function
    
    users_premium = await proccess_find_by_day_and_month_premium(today_day, today_month)
    for function in asyncio.as_completed(map(proccess_send_manager_premium, users_premium)):
        await function


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

