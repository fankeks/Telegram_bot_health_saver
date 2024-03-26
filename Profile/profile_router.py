from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from Data_base.DataBase import data
from Profile.profile_keyboard.inline_profile_kb import inline_profile_kb
from Profile.profile_keyboard.inline_genders_kb import inline_genders_kb
from Profile.profile_states import ProfileStates
from Main.main_keyboard.inline_menu_kb import inline_menu_kb
from Main.main_keyboard.menu_kb import menu_kb


async def cmd_profile(callback: CallbackQuery):
    await data.add_user(callback.from_user.id)
    gender = await data.get_value('gender', callback.from_user.id)
    if gender is None:
        gender = 'Не заполнено'

    age = await data.get_value('age', callback.from_user.id)
    if age is None:
        age = 'Не заполнено'

    height = await data.get_value('height', callback.from_user.id)
    if height is None:
        height = 'Не заполнено'

    mes = f"""Ваш профиль:
Пол: {str(gender)}
Возраст: {str(age)}
Рост: {str(height)}"""
    await callback.message.answer(mes, reply_markup=inline_profile_kb)


async def cmd_change_gender(callback: CallbackQuery):
    await callback.message.answer('Введите ваш пол:', reply_markup=inline_genders_kb)


async def cmd_change_gender_male(callback: CallbackQuery):
    await data.set_value('gender', callback.from_user.id, 'Мужской')
    await callback.message.answer('Ваш пол: Мужской')


async def cmd_change_gender_female(callback: CallbackQuery):
    await data.set_value('gender', callback.from_user.id, 'Женский')
    await callback.message.answer('Ваш пол: Женский')


async def cmd_change_age(callback: CallbackQuery):
    await callback.message.answer('Введите ваш возраст:')
    await ProfileStates.Send_age.set()


async def cmd_set_age(message: Message, state: FSMContext):
    try:
        value = float(message.text)
        await data.set_value('age', message.from_user.id, value)
        await message.answer(f"Ваш возраст: {value}")
        await state.finish()
    except:
        await message.answer("Введите ваш возраст:")
    await message.delete()


async def cmd_change_height(callback: CallbackQuery):
    await callback.message.answer('Введите ваш рост:')
    await ProfileStates.Send_height.set()


async def cmd_set_height(message: Message, state: FSMContext):
    try:
        value = float(message.text)
        await data.set_value('height', message.from_user.id, value)
        await message.answer(f"Ваш рост: {value}")
        await state.finish()
    except:
        await message.answer("Введите ваш рост:")
    await message.delete()


async def cmd_menu(message: Message, state: FSMContext):
    await state.finish()
    await message.answer('Возврат в главное меню без сохранения результатов ввода')
    await message.answer('Выберите функцию', reply_markup=menu_kb)
    await message.answer('Функции:', reply_markup=inline_menu_kb)
    await message.delete()


def register_profile_router(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_profile,
                                       lambda call: call.data == 'profile')

    dp.register_message_handler(cmd_menu,
                                commands=['menu'],
                                state=[ProfileStates.Send_age,
                                       ProfileStates.Send_height])

    dp.register_callback_query_handler(cmd_change_gender,
                                       lambda call: call.data == 'change_gender')

    dp.register_callback_query_handler(cmd_change_gender_male,
                                       lambda call: call.data == 'gender_male')

    dp.register_callback_query_handler(cmd_change_gender_female,
                                       lambda call: call.data == 'gender_female')

    dp.register_callback_query_handler(cmd_change_age,
                                       lambda call: call.data == 'change_age')

    dp.register_message_handler(cmd_set_age,
                                state=ProfileStates.Send_age)

    dp.register_callback_query_handler(cmd_change_height,
                                       lambda call: call.data == 'change_height')

    dp.register_message_handler(cmd_set_height,
                                state=ProfileStates.Send_height)