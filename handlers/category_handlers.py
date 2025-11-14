from aiogram import F,Router
from aiogram.filters import Command
from aiogram import types
from keyboards.keyboards import *
from message import *
from db import db_users, sink_db_users
from filtres import *
from pprint import pprint
categories_router = Router()

#//////////////////////////////////////////////////////////////////////////////////
#добавление

@categories_router.message(F.text == "Добавить категорию")    
async def wait_new_category(message):
    await message.answer("Введите название категории для добавления")
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': 'wait new category'}})


@categories_router.message(is_wait_new_category_user)
async def add_category(message):
    categ = {
        'category_name': message.text,
        'subcategories': []
    }
    current_user = await db_users.find_one({"id": message.from_user.id})

    current_user['categories'].append(categ)
    cat = "*Вот ваши категории:* \n \n"
    for i in current_user['categories']:
        cat += f"`{i['category_name']}`\n"
    await message.answer(cat,parse_mode="Markdown")
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'categories': list(current_user['categories'])}})
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': ''}})


#//////////////////////////////////////////////////////////////////////////////////
#удаление

@categories_router.message(F.text == "Удалить категорию")    
async def wait_delete_category(message):
    await message.answer("Какие категории вы хотите удалить?")
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': 'wait delete category'}})
    

@categories_router.message(is_delete_category_user)
async def delete_category(message):
    cat = "*Вот ваши категории:* \n \n"
    prom_slovar = await db_users.find_one(filter={'id': message.from_user.id})
    for i in prom_slovar['categories']:
        if message.text == i['category_name']:
            prom_slovar['categories'].remove(i)
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'categories': prom_slovar['categories'],'state': ""}})
    prom_slovar = await db_users.find_one(filter={'id': message.from_user.id})
    for i in prom_slovar['categories']:
        cat += f"`{i['category_name']}`\n"
    await message.answer(cat,parse_mode="Markdown")
    
