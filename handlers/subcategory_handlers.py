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
async def wait_new_subcategory(message):
    prom_slovar = await db_users.find_one(filter={'id': message.from_user.id})
    cat = "*Вот ваши категории, введите в какую категорию вы хотите добавить:* \n \n"
    for i in prom_slovar['categories']:
        cat += f"`{i['category_name']}`\n"
    await message.answer(cat,parse_mode="Markdown")
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': 'wait category for new subcategory'}})
    

@subcategories_router.message(is_wait_category_for_new_subcategory_user)
async def add_subcategory(message):
    await message.answer("Введите название подкатегории:")
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': 'wait new subcategory','temp': message.text}})



@subcategories_router.message(is_wait_new_subcategory_user)
async def add_subcategory(message):
    subcategory = {
        "name":message.text,
        "data": []
    }
    user = await db_users.find_one(filter={'id': message.from_user.id})
    await db_users.update_one(filter={'id': message.from_user.id,'categories.category_name': user['temp']},update={'$push':{'categories.$.subcategories': subcategory}})
    user = await db_users.find_one(filter={'id': message.from_user.id})
    cat = "*Ваши подкатегории:* \n \n"
    for category in user['categories']:
        if category['category_name'] == user["temp"]:
                current_category = category 
                break
    for subcategory in current_category['subcategories']:
        cat += f"`{subcategory['name']}`\n"
    await message.answer(cat,parse_mode="Markdown")
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': '','temp': ""}})


#/////////////////////////////////////////////////////////////////////////////////


@subcategories_router.message(F.text == "Удалить подкатегорию")    
async def wait_delete_subcategory(message):
    prom_slovar = await db_users.find_one(filter={'id': message.from_user.id})
    cat = "*Вот ваши категории, введите категорию из которой хотите удалить:* \n \n"
    for i in prom_slovar['categories']:
        cat += f"`{i['category_name']}`\n"
    await message.answer(cat,parse_mode="Markdown")
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': 'wait category for delete subcategory'}})
    




@subcategories_router.message(is_wait_category_for_delete_subcategory_user)
async def delete_subcategory(message):
    user = await db_users.find_one(filter={'id': message.from_user.id})
    cat = "*Введите название подкатегории:* \n \n"

    for category in user['categories']:
        if category['category_name'] == message.text:
                current_category = category 
                break
    for subcategory in current_category['subcategories']:
        cat += f"`{subcategory['name']}`\n"
    await message.answer(cat,parse_mode="Markdown")
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': 'wait delete subcategory','temp': message.text}})



#NE DODELANO
# temp name_category  message name_podcategory
@subcategories_router.message(is_wait_subcategory_for_delete_subcategory_user)
async def delet_subcategory(message):
    subcategory = {
        "name":message.text,
        "data": []
    }
    user = await db_users.find_one(filter={'id': message.from_user.id})
    await db_users.update_one(filter={'id': message.from_user.id,'categories.category_name': user['temp']},update={'$pull':{'categories.$.subcategories': {'name':message.text}}})
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': '','temp': ""}})
    

    