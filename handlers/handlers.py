from aiogram import F,Router
from aiogram.filters import Command
from aiogram import types
from keyboards.keyboards import *
from message import *
from db import db_users, sink_db_users
from filtres import *
from pprint import pprint
router = Router()

@router.message(Command("start"))
async def cmd_start(message):
    await message.answer(first_message, reply_markup = main_menu_keys)
    print(await db_users.find_one(filter={'id': message.from_user.id}))
    if await db_users.find_one(filter={'id': message.from_user.id}) == None:
        await db_users.insert_one({"id": message.from_user.id, "categories": [],"state": '',"temp": ""})

@router.message(F.text == "Категории активностей")    
async def category_mennu(message):
    cat = "*Вот ваши категории:* \n \n"
    await message.answer("Выберите, что вы хотите сделать",reply_markup = category_menu_keys)
    prom_slovar = await db_users.find_one(filter={'id': message.from_user.id})
    for i in prom_slovar['categories']:
        cat += f"`{i['category_name']}`\n"
    await message.answer(cat,parse_mode="Markdown")




router.message(F.text == "Донат")    
async def wait_category(message):
    await message.answer("Помогите сюда")



@router.message(F.text == "Статистика")
async def stat_menu(message):
    await message.answer("Выберите функцию",reply_markup = statistics_menu_keys)



@router.message(F.text == "Добавить активность")    
async def category_mennu(message):
    await message.answer("Выберите, что вы хотите сделать",reply_markup = category_dobv)

@router.message(F.text == "Главное меню")    
async def category_mennu(message):
    await message.answer(first_message, reply_markup = main_menu_keys)