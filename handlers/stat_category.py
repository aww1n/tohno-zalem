from aiogram import F,Router
from aiogram.filters import Command
from aiogram import types
from keyboards.keyboards import *
from message import *
from db import db_users, sink_db_users
from filtres import *
from pprint import pprint

stat_router = Router()

@stat_router.message(F.text == "По категориям")
async def stat_menu(message):
    await message.answer("Выберите по какой категории ",reply_markup = category_sort)


@stat_router.message(F.text == "За период")
async def stat_menu(message):
    await message.answer("Выберите за какой период ",reply_markup = statistics_sort)