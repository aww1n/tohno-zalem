from dotenv import load_dotenv
import os 
import asyncio
from aiogram import Bot, Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram import types
import logging  
from handlers import *
from keyboards import *
from motor.motor_asyncio import AsyncIOMotorClient
from handlers.subcategory_handlers import subcategories_router
from handlers.handlers import router
from handlers.category_handlers import categories_router
client = AsyncIOMotorClient('localhost',port = 27017)
db = client['activite_bot']
db_users = db['users']

load_dotenv()
token =  os.getenv("TOKEN")
bot = Bot(token=token) 
dispatcher = Dispatcher()



async def main():
    dispatcher.include_router(router)
    dispatcher.include_router(subcategories_router)
    dispatcher.include_router(categories_router)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

