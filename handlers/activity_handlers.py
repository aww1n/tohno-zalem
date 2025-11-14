from aiogram import F,Router
from aiogram.filters import Command
from aiogram import types
from keyboards.keyboards import *
from message import *
from db import db_users, sink_db_users
from filtres import *
from pprint import pprint
activite_router = Router()


@activite_router.message(F.text == "Добавить активность")    
async def category_mennu(message):

    cat = "*Вот ваши категории:* \n \n "
    prom_slovar = await db_users.find_one(filter={'id': message.from_user.id})
    for i in prom_slovar['categories']:
        cat += f"`{i['category_name']}`\n "
    cat += '\nВведите категорию, в которую хотите добавить активность'
    await message.answer(cat,parse_mode="Markdown",reply_markup = main_menu_keys)

