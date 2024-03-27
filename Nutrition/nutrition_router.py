from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from Data_base.DataBase import data
from Main.main_keyboard.menu_kb import menu_kb
from Nutrition.nutrition_keyboard.inline_activity_kb import inline_activity_kb


def calculate(gender, age, height, weight, activity, target):
    if gender == 'Мужской':
        cal = round((weight * 13.75 + height * 5.003 - age * 6.775 + 66.5) * activity + target)
    else:
        cal = round((weight * 9.563 + height * 1.85 - age * 4.676 + 655.1) * activity + target)

    A = 1.8
    if target == 150:
        if gender == 'Мужской':
            A = 2.7
        else:
            A = 2.3

    if target == -250:
        A = 2

    fat = weight
    bel = round(A * weight)
    car = round((cal - 9 * fat - 4 * bel) / 4)

    ans = f'''Параметры рассчитаны по данным из профиля.
Калории: {cal}
Белки: {bel}
Жиры: {fat}
Углеводы: {car}'''
    return ans


async def cmd_nutrition(callback: CallbackQuery):
    for key in data.keys:
        value = await data.get_value(key, callback.from_user.id)
        if value is None:
            await callback.message.answer('Профиль не заполнен')
            return None

    await callback.message.answer("Выберите ваш уровень активности:", reply_markup=inline_activity_kb)


async def cmd_get_activity_1(callback: CallbackQuery):
    gender = await data.get_value('gender', callback.from_user.id)
    age = await data.get_value('age', callback.from_user.id)
    height = await data.get_value('height', callback.from_user.id)
    weight = await data.get_value('weight', callback.from_user.id)
    target = await data.get_value('target', callback.from_user.id)
    activity = 1.2
    ans = calculate(gender, age, height, weight, activity, target)
    await callback.message.answer(ans, reply_markup=menu_kb)


async def cmd_get_activity_2(callback: CallbackQuery):
    gender = await data.get_value('gender', callback.from_user.id)
    age = await data.get_value('age', callback.from_user.id)
    height = await data.get_value('height', callback.from_user.id)
    weight = await data.get_value('weight', callback.from_user.id)
    target = await data.get_value('target', callback.from_user.id)
    activity = 1.275
    ans = calculate(gender, age, height, weight, activity, target)
    await callback.message.answer(ans, reply_markup=menu_kb)


async def cmd_get_activity_3(callback: CallbackQuery):
    gender = await data.get_value('gender', callback.from_user.id)
    age = await data.get_value('age', callback.from_user.id)
    height = await data.get_value('height', callback.from_user.id)
    weight = await data.get_value('weight', callback.from_user.id)
    target = await data.get_value('target', callback.from_user.id)
    activity = 1.45
    ans = calculate(gender, age, height, weight, activity, target)
    await callback.message.answer(ans, reply_markup=menu_kb)


async def cmd_get_activity_4(callback: CallbackQuery):
    gender = await data.get_value('gender', callback.from_user.id)
    age = await data.get_value('age', callback.from_user.id)
    height = await data.get_value('height', callback.from_user.id)
    weight = await data.get_value('weight', callback.from_user.id)
    target = await data.get_value('target', callback.from_user.id)
    activity = 1.5
    ans = calculate(gender, age, height, weight, activity, target)
    await callback.message.answer(ans, reply_markup=menu_kb)


async def cmd_get_activity_5(callback: CallbackQuery):
    gender = await data.get_value('gender', callback.from_user.id)
    age = await data.get_value('age', callback.from_user.id)
    height = await data.get_value('height', callback.from_user.id)
    weight = await data.get_value('weight', callback.from_user.id)
    target = await data.get_value('target', callback.from_user.id)
    activity = 1.7
    ans = calculate(gender, age, height, weight, activity, target)
    await callback.message.answer(ans, reply_markup=menu_kb)


def register_nutrition_router(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_nutrition,
                                       lambda call: call.data == 'nutrition')

    dp.register_callback_query_handler(cmd_get_activity_1,
                                       lambda call: call.data == 'activity_1')

    dp.register_callback_query_handler(cmd_get_activity_2,
                                       lambda call: call.data == 'activity_2')

    dp.register_callback_query_handler(cmd_get_activity_3,
                                       lambda call: call.data == 'activity_3')

    dp.register_callback_query_handler(cmd_get_activity_4,
                                       lambda call: call.data == 'activity_4')

    dp.register_callback_query_handler(cmd_get_activity_5,
                                       lambda call: call.data == 'activity_5')
