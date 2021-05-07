from os import environ
import datetime

from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DB_ADDR = "mongodb" #environ['MONGO_DB_ADDR']
MONGO_DB_HOST = "localhost" #environ['MONGO_DB_HOST']
MONGO_DB_PORT = "27017" #environ['MONGO_DB_PORT']

URI = MONGO_DB_ADDR + "://" + MONGO_DB_HOST + ":" + MONGO_DB_PORT
client = AsyncIOMotorClient(URI)

db = client['database']
collection = db['collection']

today = datetime.datetime.today()
day = today.day
month = today.month
year = today.year

async def get_count_documents()->int:
    return await db.collection.count_documents({})


async def proccess_insert_user(user_id: int, name, gender: str,mafia: str, day: int, month: str, instagram = None):
    count = await get_count_documents()
    if instagram == None:
        user = {
            "id": int(count) + 1,
            "user_id": user_id,
            "name": name,
            "gender": gender,
            "mafia": mafia,
            "day": day,
            "month": month,
        }
        await db.collection.insert_one(user)
    else:
        user = {
            "id": int(count) + 1,
            "user_id": user_id,
            "name": name,
            "gender": gender,
            "mafia": mafia,
            "day": day,
            "month": month,
            "instagram": instagram,
        }
        await db.collection.insert_one(user)


async def proccess_find_user_by_id(id: int):
    return await db.collection.find_one({'user_id': id})


async def proccess_update_user_mafia_by_id(id: int,mafia:str, user: list, instagram = "-"):
    coll = db.collection
    old_document = await coll.find_one({'user_id': user["user_id"]})
    id = old_document['id']
    await coll.replace_one({'id': id}, {
            "id": id,
            "user_id": user['user_id'],
            "name": user['name'],
            "gender": user['gender'],
            "mafia": mafia,
            "day": user['day'],
            "month": user['month'],
            "instagram": instagram,
        })
    return old_document['name']



async def process_delete_user_by_id(id: int):
    return await db.collection.delete_one({"user_id": id})


async def proccess_find_by_day_and_month(day: int, month: str):
    collection = db.collection
    users = []
    async for document in collection.find({'day': day, "month": month}):
        users.append(document)
    return users


async def proccess_find_by_day_and_month_premium(day: int, month: str):
    collection = db.collection
    users = []
    async for document in collection.find({'day': day, "month": month, "mafia": "premium"}):
        users.append(document)
    return users


async def proccess_find_admin_by_id(id: int):
    return await db.collection.find_one({'user_id': id, 'status': "admin"})


async def proccess_insert_event(name, mafia, link, date, invite_code: str, chat_id: int = 0):
    count = await get_count_documents()
    event = {
            "id": int(count) + 1,
            "chat_id": chat_id,
            "status": "event",
            "invite_code": invite_code,
            "mafia": mafia,
            "name": name,
            "link": link,
            "date": date
    }
    await db.collection.insert_one(event)


async def get_event_by_invite_code(invite_code):
    date = str(day) + "." + str(month) + "." + str(year)
    return await db.collection.find_one({'status': "event", "invite_code": invite_code, "date": date})


async def get_events(event: str):
    collection = db.collection
    events = []
    date = str(day) + "." + str(month) + "." + str(year)
    async for document in collection.find({"status": "event", "date": date, "mafia": event}):
        events.append(document)
    return events
    

