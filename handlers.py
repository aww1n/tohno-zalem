from aiogram import F,Router
from aiogram.filters import Command
from aiogram import types
from keyboards import *
from message import *
from db import db_users, sink_db_users
from filtres import *
router = Router()

@router.message(Command("start"))
async def cmd_start(message):
    await message.answer(first_message, reply_markup = main_menu_keys)
    print(await db_users.find_one(filter={'id': message.from_user.id}))
    if await db_users.find_one(filter={'id': message.from_user.id}) == None:
        await db_users.insert_one({"id": message.from_user.id, "categories": [],"state": ''})

@router.message(F.text == "Категории активностей")    
async def category_mennu(message):
    await message.answer("Выберите, что вы хотите сделать",reply_markup = category_menu_keys)


@router.message(F.text == "Добавить категорию")    
async def wait_category(message):
    await message.answer("Введите название категории для добавления")
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': 'wait new category'}})

@router.message(is_wait_category_user)
async def add_category(message):
    categ = {
        'category_name': message.text,
        'subcategories': []
    }
    current_user = await db_users.find_one({"id": message.from_user.id})

    current_user['categories'].append(categ)
    print(current_user['categories'])
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'categories': list(current_user['categories'])}})
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': ''}})





@router.message(F.text == "Удалить категорию")    
async def wait_category(message):
    await message.answer("Какие категории вы хотите удалить?")
    await db_users.update_one(filter={'id': message.from_user.id},update={'$set':{'state': 'wait delete category'}})




@router.message(is_delet_category_user)
async def add_category(message):
    print("jjfng")
    prom_slovar = await db_users.find_one(filter={'id': message.from_user.id})

    print(type(prom_slovar['categories']))


























@router.message(F.text == "Статистика")
async def stat_menu(message):
    await message.answer("Выберите функцию",reply_markup = statistics_menu_keys)


@router.message(F.text == "За период")
async def stat_menu(message):
    await message.answer("Выберите за какой период ",reply_markup = statistics_sort)


@router.message(F.text == "По категориям")
async def stat_menu(message):
    await message.answer("Выберите по какой категории ",reply_markup = category_sort)

@router.message(F.text == "Добавить активность")    
async def category_mennu(message):
    await message.answer("Выберите, что вы хотите сделать",reply_markup = category_dobv)
@router.message(F.text == "Главное меню")    
async def category_mennu(message):
    await message.answer(first_message, reply_markup = main_menu_keys)