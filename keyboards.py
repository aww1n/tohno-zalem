from aiogram.types import ReplyKeyboardMarkup, KeyboardButton 


main_menu_keys = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Добавить активность')],
    [KeyboardButton(text='Категории активностей ')],
    [KeyboardButton(text='Статистика'),KeyboardButton(text='📌 Донат')]
])


category_menu_keys = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Добавить категорию')],
    [KeyboardButton(text='Удалить категорию')],
    [KeyboardButton(text='Главное меню')]
])


statistics_menu_keys = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='За период')],
    [KeyboardButton(text='По категориям')],
    [KeyboardButton(text='Главное меню')]
])


statistics_sort = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='За неделю 📅')],
    [KeyboardButton(text='За месяц 📅')],
    [KeyboardButton(text='За год 📅')],
    [KeyboardButton(text='Главное меню')]

])


category_sort = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='За неделю 📅')],
    [KeyboardButton(text='За месяц 📅')],
    [KeyboardButton(text='За год 📅')],
    [KeyboardButton(text='Главное меню')]

])


category_dobv = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Выбор категории')],
    [KeyboardButton(text='Главное меню')]
])