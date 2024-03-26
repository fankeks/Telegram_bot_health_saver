from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from Data_base.DataBase import data
from Nutrition.nutrition_states import NutritionStates
from Main.main_keyboard.inline_menu_kb import inline_menu_kb
from Main.main_keyboard.menu_kb import menu_kb
from Nutrition.nutrition_keyboard.inline_activity_kb import inline_activity_kb


def calculate(gender, age, height, weight, activity):
    if gender == 'Мужской':
        return round((weight * 10 + height * 6.25 - age * 5 + 5) * activity)
    return round((weight * 10 + height * 6.25 - age * 5 - 161) * activity)


async def cmd_nutrition(callback: CallbackQuery):
    gender = await data.get_value('gender', callback.from_user.id)
    age = await data.get_value('age', callback.from_user.id)
    height = await data.get_value('height', callback.from_user.id)
    if (gender is None) or (age is None) or (height is None):
        await callback.message.answer('Профиль не заполнен')
    else:
        await callback.message.answer('Введите ваш вес:')
        await NutritionStates.Send_weight.set()


async def cmd_menu(message: Message, state: FSMContext):
    await state.finish()
    await message.answer('Возврат в главное меню без сохранения результатов ввода')
    await message.answer('Выберите функцию', reply_markup=menu_kb)
    await message.answer('Функции:', reply_markup=inline_menu_kb)
    await message.delete()


async def cmd_get_weight(message: Message, state: FSMContext):
    async with state.proxy() as d:
        try:
            value = float(message.text)
            await data.set_value('weight', message.from_user.id, value)
            d['weight'] = value
            await NutritionStates.next()
            await message.answer("Выберите ваш уровень активности:", reply_markup=inline_activity_kb)
        except:
            await message.answer("Введите ваш вес:")
        await message.delete()


async def cmd_get_activity_1(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as d:
        weight = d['weight']
    await state.finish()
    gender = await data.get_value('gender', callback.from_user.id)
    age = await data.get_value('age', callback.from_user.id)
    height = await data.get_value('height', callback.from_user.id)
    activity = 1.2
    await data.set_value('activity', callback.from_user.id, activity)
    cal = calculate(gender, age, height, weight, activity)
    await callback.message.answer(f'КБЖУ: {cal}', reply_markup=menu_kb)


async def cmd_get_activity_2(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as d:
        weight = d['weight']
    await state.finish()
    gender = await data.get_value('gender', callback.from_user.id)
    age = await data.get_value('age', callback.from_user.id)
    height = await data.get_value('height', callback.from_user.id)
    activity = 1.38
    await data.set_value('activity', callback.from_user.id, activity)
    cal = calculate(gender, age, height, weight, activity)
    await callback.message.answer(f'КБЖУ: {cal}', reply_markup=menu_kb)


async def cmd_get_activity_3(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as d:
        weight = d['weight']
    await state.finish()
    gender = await data.get_value('gender', callback.from_user.id)
    age = await data.get_value('age', callback.from_user.id)
    height = await data.get_value('height', callback.from_user.id)
    activity = 1.46
    await data.set_value('activity', callback.from_user.id, activity)
    cal = calculate(gender, age, height, weight, activity)
    await callback.message.answer(f'КБЖУ: {cal}', reply_markup=menu_kb)


async def cmd_get_activity_4(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as d:
        weight = d['weight']
    await state.finish()
    gender = await data.get_value('gender', callback.from_user.id)
    age = await data.get_value('age', callback.from_user.id)
    height = await data.get_value('height', callback.from_user.id)
    activity = 1.55
    await data.set_value('activity', callback.from_user.id, activity)
    cal = calculate(gender, age, height, weight, activity)
    await callback.message.answer(f'КБЖУ: {cal}', reply_markup=menu_kb)


async def cmd_get_activity_5(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as d:
        weight = d['weight']
    await state.finish()
    gender = await data.get_value('gender', callback.from_user.id)
    age = await data.get_value('age', callback.from_user.id)
    height = await data.get_value('height', callback.from_user.id)
    activity = 1.64
    await data.set_value('activity', callback.from_user.id, activity)
    cal = calculate(gender, age, height, weight, activity)
    await callback.message.answer(f'КБЖУ: {cal}', reply_markup=menu_kb)


async def cmd_get_activity_6(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as d:
        weight = d['weight']
    await state.finish()
    gender = await data.get_value('gender', callback.from_user.id)
    age = await data.get_value('age', callback.from_user.id)
    height = await data.get_value('height', callback.from_user.id)
    activity = 1.73
    await data.set_value('activity', callback.from_user.id, activity)
    cal = calculate(gender, age, height, weight, activity)
    await callback.message.answer(f'КБЖУ: {cal}', reply_markup=menu_kb)


async def cmd_get_activity_7(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as d:
        weight = d['weight']
    await state.finish()
    gender = await data.get_value('gender', callback.from_user.id)
    age = await data.get_value('age', callback.from_user.id)
    height = await data.get_value('height', callback.from_user.id)
    activity = 1.9
    await data.set_value('activity', callback.from_user.id, activity)
    cal = calculate(gender, age, height, weight, activity)
    await callback.message.answer(f'КБЖУ: {cal}', reply_markup=menu_kb)


def register_nutrition_router(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_nutrition,
                                       lambda call: call.data == 'nutrition')

    dp.register_message_handler(cmd_menu,
                                commands=['menu'],
                                state=[NutritionStates.Send_activity,
                                       NutritionStates.Send_weight])

    dp.register_message_handler(cmd_get_weight,
                                state=NutritionStates.Send_weight)

    dp.register_callback_query_handler(cmd_get_activity_1,
                                       lambda call: call.data == 'activity_1',
                                       state=NutritionStates.Send_activity)

    dp.register_callback_query_handler(cmd_get_activity_2,
                                       lambda call: call.data == 'activity_2',
                                       state=NutritionStates.Send_activity)

    dp.register_callback_query_handler(cmd_get_activity_3,
                                       lambda call: call.data == 'activity_3',
                                       state=NutritionStates.Send_activity)

    dp.register_callback_query_handler(cmd_get_activity_4,
                                       lambda call: call.data == 'activity_4',
                                       state=NutritionStates.Send_activity)

    dp.register_callback_query_handler(cmd_get_activity_5,
                                       lambda call: call.data == 'activity_5',
                                       state=NutritionStates.Send_activity)

    dp.register_callback_query_handler(cmd_get_activity_6,
                                       lambda call: call.data == 'activity_6',
                                       state=NutritionStates.Send_activity)

    dp.register_callback_query_handler(cmd_get_activity_7,
                                       lambda call: call.data == 'activity_7',
                                       state=NutritionStates.Send_activity)
