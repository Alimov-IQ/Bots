from loader import dp, bot, client
from utils.generator.nickname import (
    get_random_female_nickname,
    get_random_male_nickname,
)
from utils.database.database import  (
    proccess_find_user_by_id, 
    get_event_by_invite_code,
)
from keyboards.inline.photo import photo_keyboard
from keyboards.default.menu import menu_keyboard
from keyboards.inline.events import get_event_button
from keyboards.inline.registration import menu_services_keyboard
from states.registration import InputInviteCode

from aiogram.types import Message, InputFile,CallbackQuery , ParseMode, MediaGroup, InputMedia, InputMediaDocument, InputMediaPhoto
from aiogram.dispatcher import FSMContext


@dp.message_handler(lambda message: message.text == "Контакты")
async def proccess_view_contact(message: Message):
    id = message.from_user.id
    user = await proccess_find_user_by_id(id)
    if user == None:
        await message.answer("Тебе стоит зарегистрироваться")
    else:
        await message.answer('''
💫 Наши контакты:

📢 Менеджер: +37529-5-413-413
📷 Инстаграм - [mafiavero](https://www.instagram.com/mafiavero/)
''', parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(lambda message: message.text == "Правила игры")
async def proccess_view_rules_games(message: Message):
    id = message.from_user.id
    user = await proccess_find_user_by_id(id)
    if user == None:
        await message.answer("Тебе стоит зарегистрироваться")
    else:
        await message.answer('''
📖 Основные правила игры «МАФИЯ»

1. В игре принимают участие десять человек. Случайным образом делятся на две команды:
“Красные” (мирные жители) и “Чёрные” (мафия).
В игре разыгрываются семь “красных” карт, одна из которых — Шериф, и три “чёрные”, одна из которых — Дон.

2. Ведёт игру и регламентирует её этапы Судья. Ведению игры может помогать боковой Судья.

3. Игра имеет две фазы: фаза “день” и фаза “ночь”.

4. Победа команды “красных” наступает в том случае, когда из игры выведены все представители “чёрной” команды.
Победа “чёрной” команды наступает в случае, когда за игровым столом остаётся равное количество игроков обеих команд или количество “черных” игроков больше, чем “красных”.


Подробные правила игры - в файле.
''')    
        doc = await bot.send_document(id, document="BQACAgIAAxkDAAOPYJV7FjKAontD4N_pK722vAobcGUAArMNAAKFMKhIBIe7cyRIk0YfBA")


@dp.message_handler(lambda message: message.text == "Услуги")
async def proccess_view_services(message: Message):
    id = message.from_user.id
    user = await proccess_find_user_by_id(id)
    if user == None:
        await message.answer("Тебе стоит зарегистрироваться")
    else:
        await message.answer('''
С «MAFIA VERO» стильно, необычно,\nа так же полезно для развития личности и командообразования.
Такое веселое, неординарное мероприятие 100% запомнится\nИ на следующий день ещё будет что обсудить!

Готовы организовать для тебя:
🎂 День рождения
👨‍💻 Тимбилдинг
🤝 Мероприятие для клиентов
🥃 Корпоратив
🧸 Детская мафия
🌏 Online-мафия
🧠 Интеллектуальный квиз

✔ под любой концепт
✔ от 7 до 1000 человек
''', reply_markup=menu_services_keyboard)



@dp.callback_query_handler(lambda callback: callback.data == 'quiz')
async def show_quiz(callback: CallbackQuery):
    id = callback.from_user.id
    await bot.send_message(id, '''
💎Квиз Мозика - это интеллектуально-развлекательная игра, в которой нужно отвечать на разные вопросы (в основном на логику и эрудицию, а также про музыку и кино). 

📜Подробные цены и условия по проведению Квиз-игр в Мозайке, ты можешь узнать, просмотрев файл:
''')
    await bot.send_document(id, document="BQACAgIAAxkDAAOTYJV7o9n8PbvO0WPK8NsVR6WHCqcAArYNAAKFMKhIqLD3JaQXGa0fBA")


@dp.message_handler(lambda message: message.text == "photo-upload")
async def photo_save(message: Message):
    id = message.from_user.id
    i = 1
    text = "[\n"
    while i < 21:
        photo = await message.answer_photo(InputFile(f"assets/images/img{i}.jpg"))
        text = text + 'InputMediaPhoto(\"' + photo['photo'][0]['file_id'] + '\"),\n'
        i += 1
    print(text)

@dp.message_handler(lambda message: message.text == 'Фото и Видео')
async def show_photos_videos(callback: CallbackQuery):
    id = callback.from_user.id
    await bot.send_message(id, '''
📸Видео и фото с наших мероприятий

https://youtu.be/YMUi2GlIfbw (Гангстерская вечеринка)
https://youtu.be/h3OI98If13c (Имиджевый ролик)
https://youtu.be/Q2IRXHTeIQE (Peaky Blinders)
https://youtu.be/qJHSZ7qkm74 (День рождения с игрой и каскадерский трюк)
https://youtu.be/Waz914D6reI (Вечеринка на день рождения)
https://youtu.be/gBLjZRwK08w (Вечеринка с игрой)
https://youtu.be/_cuIeew7CmQ (Мафия на день рождения)
https://youtu.be/Y9NujYsyXqM (It-турнир)   
''')
    images = [
InputMediaPhoto("AgACAgIAAxkDAANcYJV5wnUZitDsdFakLfhMZXDLc2sAAmy0MRuFMKhI3tiTFP0tVa1sWDefLgADAQADAgADbQADypQDAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANdYJV5wpO2vcYtCVlCzUU2Mc8yweYAAnG0MRuFMKhIqLXrYtWd8dC3Q6aiLgADAQADAgADbQADMQoCAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANeYJV5wwF3MMuihZ9luilv4m--3sUAAnK0MRuFMKhIk5M04IO6CJLyf1GkLgADAQADAgADbQADB8EAAh8E"),
InputMediaPhoto("AgACAgIAAxkDAANfYJV5w7jIYueqir56-T8FVrra-CwAAnO0MRuFMKhInCxHlcFj9G9qdE6kLgADAQADAgADbQAD7s0AAh8E"),
InputMediaPhoto("AgACAgIAAxkDAANgYJV5xFM9L_lJFXSIz-HAAj317ckAAnS0MRuFMKhImJtAsWZA17PFT4yiLgADAQADAgADbQADtOEBAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANhYJV5xEHzpngDx4RuuyI2lliGE4AAAnW0MRuFMKhIQE1RHKG4EexVN0OeLgADAQADAgADbQADfZ0DAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANiYJV5xX3_Uzh17VqRT-odJk8mvY8AAna0MRuFMKhIsfBq9zEiX6TY0jWfLgADAQADAgADbQAD6O0DAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANjYJV5xiW-OFZpOGyGgcXSNDnrvRkAAne0MRuFMKhIbbLUtR20MawbN0OeLgADAQADAgADbQADd6ADAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANkYJV5x-5x7B9r8A23UfSNQi7nuXQAAni0MRuFMKhIJutXOyAcqv4Dp4OfLgADAQADAgADbQADbqkDAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANlYJV5x9FFRlflli7FYWhK9gsMwwEAAnm0MRuFMKhIivn97gSFO9XA0Q-bLgADAQADAgADbQADvyUGAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANmYJV5yB0kODZ4dcCe51Kw597A7K8AAnq0MRuFMKhInxqQnLNR0EJ68ZOiLgADAQADAgADbQADZt4BAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANnYJV5yHdnuvDNRRBESppYuFKr4a0AAnu0MRuFMKhIQ4rq9qkZbnj4-dCiLgADAQADAgADbQADss8BAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANoYJV5ya0JKXlidgKiRe37j-y7I00AAny0MRuFMKhIKhaFzIAfKgJuMg-iLgADAQADAgADbQADiOUBAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANpYJV5yXcNPuhhnreFfJvNEJZnphwAAn20MRuFMKhILu1bB1NiEoyac06kLgADAQADAgADbQADDdIAAh8E"),
InputMediaPhoto("AgACAgIAAxkDAANqYJV5ynGICeWMByayekk1c3yh4OQAAn60MRuFMKhI9V_uagb7oHIchoedLgADAQADAgADbQADTvYBAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANrYJV5y_gNjejBTr6mSUiXsS226vcAAn-0MRuFMKhIlT9QIZo3GwtYIAOeLgADAQADAgADbQADA5cDAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANsYJV5y5Cg9puFYPZ3DFeSrNUNK2kAAoC0MRuFMKhIPi2rtO5l_JOTzIqiLgADAQADAgADbQADUP4BAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANtYJV5zI4OcRpVX2IxNhfXVGUbT10AAoG0MRuFMKhIBe3teLkUpIy2Z4meLgADAQADAgADbQADQQoGAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANuYJV5zFPv-HXPO2LkJJeqM6tmuBkAAoK0MRuFMKhITmnxNSiAjQWBIAOeLgADAQADAgADbQADt5UDAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANvYJV5zUZa0bDN7R28ZzA1TWSgzIIAAoO0MRuFMKhIqmD7DjhdQW26zg2eLgADAQADAgADbQADdfYFAAEfBA"),
    ]
    await bot.send_media_group(id, images[0:10])
    await bot.send_message(id, "Желаешь еще фото?", reply_markup=photo_keyboard)

@dp.callback_query_handler(lambda callback: callback.data == "photos")
async def get_photos(callback: CallbackQuery ):
    id = callback.from_user.id
    images = [
InputMediaPhoto("AgACAgIAAxkDAANcYJV5wnUZitDsdFakLfhMZXDLc2sAAmy0MRuFMKhI3tiTFP0tVa1sWDefLgADAQADAgADbQADypQDAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANdYJV5wpO2vcYtCVlCzUU2Mc8yweYAAnG0MRuFMKhIqLXrYtWd8dC3Q6aiLgADAQADAgADbQADMQoCAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANeYJV5wwF3MMuihZ9luilv4m--3sUAAnK0MRuFMKhIk5M04IO6CJLyf1GkLgADAQADAgADbQADB8EAAh8E"),
InputMediaPhoto("AgACAgIAAxkDAANfYJV5w7jIYueqir56-T8FVrra-CwAAnO0MRuFMKhInCxHlcFj9G9qdE6kLgADAQADAgADbQAD7s0AAh8E"),
InputMediaPhoto("AgACAgIAAxkDAANgYJV5xFM9L_lJFXSIz-HAAj317ckAAnS0MRuFMKhImJtAsWZA17PFT4yiLgADAQADAgADbQADtOEBAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANhYJV5xEHzpngDx4RuuyI2lliGE4AAAnW0MRuFMKhIQE1RHKG4EexVN0OeLgADAQADAgADbQADfZ0DAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANiYJV5xX3_Uzh17VqRT-odJk8mvY8AAna0MRuFMKhIsfBq9zEiX6TY0jWfLgADAQADAgADbQAD6O0DAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANjYJV5xiW-OFZpOGyGgcXSNDnrvRkAAne0MRuFMKhIbbLUtR20MawbN0OeLgADAQADAgADbQADd6ADAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANkYJV5x-5x7B9r8A23UfSNQi7nuXQAAni0MRuFMKhIJutXOyAcqv4Dp4OfLgADAQADAgADbQADbqkDAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANlYJV5x9FFRlflli7FYWhK9gsMwwEAAnm0MRuFMKhIivn97gSFO9XA0Q-bLgADAQADAgADbQADvyUGAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANmYJV5yB0kODZ4dcCe51Kw597A7K8AAnq0MRuFMKhInxqQnLNR0EJ68ZOiLgADAQADAgADbQADZt4BAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANnYJV5yHdnuvDNRRBESppYuFKr4a0AAnu0MRuFMKhIQ4rq9qkZbnj4-dCiLgADAQADAgADbQADss8BAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANoYJV5ya0JKXlidgKiRe37j-y7I00AAny0MRuFMKhIKhaFzIAfKgJuMg-iLgADAQADAgADbQADiOUBAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANpYJV5yXcNPuhhnreFfJvNEJZnphwAAn20MRuFMKhILu1bB1NiEoyac06kLgADAQADAgADbQADDdIAAh8E"),
InputMediaPhoto("AgACAgIAAxkDAANqYJV5ynGICeWMByayekk1c3yh4OQAAn60MRuFMKhI9V_uagb7oHIchoedLgADAQADAgADbQADTvYBAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANrYJV5y_gNjejBTr6mSUiXsS226vcAAn-0MRuFMKhIlT9QIZo3GwtYIAOeLgADAQADAgADbQADA5cDAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANsYJV5y5Cg9puFYPZ3DFeSrNUNK2kAAoC0MRuFMKhIPi2rtO5l_JOTzIqiLgADAQADAgADbQADUP4BAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANtYJV5zI4OcRpVX2IxNhfXVGUbT10AAoG0MRuFMKhIBe3teLkUpIy2Z4meLgADAQADAgADbQADQQoGAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANuYJV5zFPv-HXPO2LkJJeqM6tmuBkAAoK0MRuFMKhITmnxNSiAjQWBIAOeLgADAQADAgADbQADt5UDAAEfBA"),
InputMediaPhoto("AgACAgIAAxkDAANvYJV5zUZa0bDN7R28ZzA1TWSgzIIAAoO0MRuFMKhIqmD7DjhdQW26zg2eLgADAQADAgADbQADdfYFAAEfBA"),
    ]
    await bot.delete_message(id, callback.message.message_id)
    await bot.send_media_group(id, images[10:20])
    


@dp.callback_query_handler(lambda callback: callback.data == 'price')
async def show_price(callback: CallbackQuery):
    id = callback.from_user.id
    await bot.send_message(id, '''
📜Подробные цены и условия ты можешь узнать, просмотрев файлы: 
''')
    docs = [
       InputMediaDocument("BQACAgIAAxkDAAOpYJV9sQAB_WyhUnB4OaJyz9iYcwWOAALEDQAChTCoSANj-8Xr19WmHwQ"),
       InputMediaDocument("BQACAgIAAxkDAAOqYJV9tav31IcazY5PneMZgaOFv5YAAsUNAAKFMKhIHwP7qz-cVdkfBA"),
       InputMediaDocument("BQACAgIAAxkDAAOrYJV9t83XufW1vXSi8aVILD3XeuAAAsYNAAKFMKhI8C72eBwH0LQfBA"),
    ]

    await bot.send_media_group(id, docs)


@dp.message_handler(lambda message: message.text == "Генератор никнеймов")
async def proccess_generation_nickname(message: Message):
    id = message.from_user.id
    user = await proccess_find_user_by_id(id)
    print(user)
    if user == None:
        await message.answer("Тебе стоит зарегистрироваться")
    else:
        if user['gender'] == 'man':
            nickname = get_random_male_nickname()
            await message.answer(f"✏ {user['name']}, твой никнейм - {nickname}")
        else:
            nickname = get_random_female_nickname()
            await message.answer(f"✏ {user['name']}, твой никнейм - {nickname}")


@dp.message_handler(lambda message: message.text == "Мероприятия")
async def proccess_get_events(message: Message):
    id = message.from_user.id
    user = await proccess_find_user_by_id(id)
    if user == None:
        await message.answer("Тебе стоит зарегистрироваться")
    else:
        await InputInviteCode.invite_code.set()
        await message.answer(f"✏️ {user['name']}, введи код мероприятия,\nкоторый тебе выдали на мафии: ")


@dp.message_handler(state=InputInviteCode.invite_code)
async def proccess_invite_code(message: Message, state=FSMContext):
    async with state.proxy() as _:
        event = await get_event_by_invite_code(message.text)
        user = await proccess_find_user_by_id(message.from_user.id)

        if event == None:
            await message.reply("Некорректный код приглашения...")
        else:
            users = await get_users_chat(event['chat_id'])
            if message.from_user.id not in users:
                button = await get_event_button(event)
                #try:
                await add_user(event['chat_id'], message.from_user.id)
                await message.answer("😌Отлично! Добавил тебя в мероприятие, проверяй чаты.", reply_markup=button)
                #except:
                   # await message.answer("К сожалению, я не смог добавить тебя автоматически.\nЗаходи в чат!", reply_markup=button)
            else:
                await message.answer("Ты уже присутствуешь в этом чате.")
        await state.finish()



async def add_user(chat_id, uid):
    async with client:
        await client.add_chat_members(chat_id, uid)


async def get_users_chat(chat_id: int):
    async with client:
        users = await client.get_chat_members(chat_id)
        users_ids = [int(users[element]['user']['id']) for element in range(len(users)-1)]
        return users_ids
