from aiogram import Dispatcher
from aiogram.types import Message


from Main.main_keyboard.menu_kb import menu_kb
from Main.main_keyboard.inline_menu_kb import inline_menu_kb
from Data_base.DataBase import data


async def cmd_start(message: Message):
    await data.add_user(message.from_user.id)
    await message.answer('Добро пожаловать!')
    await message.answer('Заполните профиль для корректной работы.')
    await message.answer('Выберите функцию', reply_markup=menu_kb)
    await message.answer('Функции:', reply_markup=inline_menu_kb)
    await message.delete()


async def cmd_menu(message: Message):
    await message.answer('Выберите функцию', reply_markup=menu_kb)
    await message.answer('Функции:', reply_markup=inline_menu_kb)
    await message.delete()


def register_main_router(dp: Dispatcher):
    dp.register_message_handler(cmd_start,
                                commands=['start'])
    dp.register_message_handler(cmd_menu,
                                commands=['menu'])
