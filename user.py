from config import API_ID_USER, API_HASH_USER
from utils.database.database import proccess_insert_event
from validation.validation import proccess_validate_date, proccess_validate_new_event

from pyrogram import Client, filters



user = Client("user", api_id=API_ID_USER, api_hash=API_HASH_USER)

@user.on_message(filters.command("new"))
async def proccess_new_event(client, message):
    data = proccess_validate_new_event(message)
    print(data)
    if data == False:
        await user.send_message(message.from_user.id,"Ошибка.")
    else:
        data_date = proccess_validate_date(data[0])
        if data_date == False:
            await user.send_message(message.from_user.id,"Ошибка.")
        else:
                    date = str(int(data_date[0]))+ "." + str(int(data_date[1])) + "." + str(int(data_date[2]))
                    await user.send_message(message.from_user.id,"Мероприятие успешно записано в базу.")
                    chat = await user.create_supergroup(data[1], "")
                    message = await user.send_message(chat.id,f'''
👋🏻Привет, мой друг!

📝Это чат мероприятия "{chat.title}".
Попрошу тебя отправить в этот чат фото, которые ты бы хотел(-а) сохранить на память.

😍А лучшие из них публикуй в instagram с пометкой @mafiavero!    
''')
                    await user.pin_chat_message(chat.id, message.message_id)

                    link = await user.export_chat_invite_link(chat.id)
                    await proccess_insert_event(data[1], "standart", link, date, data[2], chat.id)
        

user.run()