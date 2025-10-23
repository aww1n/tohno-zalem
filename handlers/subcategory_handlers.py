from aiogram import F,Router
from aiogram.filters import Command
from aiogram import types
from keyboards.keyboards import *
from message import *
from db import db_users, sink_db_users
from filtres import *
from pprint import pprint

subcategories_router = Router()



@subcategories_router.message(F.text == "Добавить подкатегорию")    
async def wait_category(message):
    prom_slovar = await db_users.find_one(filter={'id': message.from_user.id})
    cat = "*Вот ваши категории, введите в какую категорию вы хотите добавить:* \n \n"
    for i in prom_slovar['categories']:
        cat += f"`{i['category_name']}`\n"
    await message.answer(cat,parse_mode="Markdown")
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': 'wait category_to_subcategiry'}})
    




@subcategories_router.message(is_category_to_subcategory_user)
async def add_category(message):
    prom_slovar = await db_users.find_one(filter={'categories': message.text})
    await message.answer("Введите название подкатегории:")
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': 'wait subcategory','temp': message.text}})
    print(prom_slovar)



@subcategories_router.message(is_subcategory_user)
async def add_subcategory(message):
    subcategory = {
        "name":message.text,
        "data": []
    }
    categor = await db_users.find_one(filter={'id': message.from_user.id})
    await db_users.update_one(filter={'id': message.from_user.id,'categories.category_name': categor['temp']},update={'$push':{'categories.$.subcategories': subcategory}})
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': '','temp': ""}})
    








@subcategories_router.message(F.text == "Удалить подкатегорию")    
async def wait_category(message):
    prom_slovar = await db_users.find_one(filter={'id': message.from_user.id})
    cat = "*Вот ваши категории, введите в какую категорию вы хотите добавить:* \n \n"
    for i in prom_slovar['categories']:
        cat += f"`{i['category_name']}`\n"
    await message.answer(cat,parse_mode="Markdown")
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': 'wait category_to_subcategiry'}})
    




@subcategories_router.message(is_category_to_subcategory_user)
async def add_category(message):
    prom_slovar = await db_users.find_one(filter={'categories': message.text})
    await message.answer("Введите название подкатегории:")
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': 'wait subcategory','temp': message.text}})
    print(prom_slovar)



@subcategories_router.message(is_subcategory_user)
async def add_subcategory(message):
    subcategory = {
        "name":message.text,
        "data": []
    }
    categor = await db_users.find_one(filter={'id': message.from_user.id})
    await db_users.update_one(filter={'id': message.from_user.id,'categories.category_name': categor['temp']},update={'$push':{'categories.$.subcategories': subcategory}})
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': '','temp': ""}})
    

    