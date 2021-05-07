from config import API_TOKEN_BOT, API_ID_USER, API_HASH_USER
from pyrogram import Client
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(API_TOKEN_BOT)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
client = Client("client", api_id=API_ID_USER, api_hash=API_HASH_USER)
