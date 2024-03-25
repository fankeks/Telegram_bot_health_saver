from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from Nutrition.nutrition_states import NutritionStates
from Main.main_keyboard.inline_menu_kb import inline_menu_kb
from Main.main_keyboard.menu_kb import menu_kb


async def cmd_nutrition(callback: CallbackQuery):
    await callback.message.answer('Введите ваш возраст:')
    await NutritionStates.Send_age.set()


async def cmd_menu(message: Message, state: FSMContext):
    await state.finish()
    await message.answer('Возврат в главное меню без сохранения результатов ввода')
    await message.answer('Выберите функцию', reply_markup=menu_kb)
    await message.answer('Функции:', reply_markup=inline_menu_kb)
    await message.delete()


async def cmd_get_age(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await NutritionStates.next()
    await message.answer("Введите ваш пол")


async def cmd_get_gender(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
    await NutritionStates.next()
    await message.answer("Введите ваш вес")


async def cmd_get_weight(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['weight'] = message.text
    await state.finish()
    ans = f'Ваш возраст: {data["age"]}\nВаш пол: {data["gender"]}\nВаш вес: {data["weight"]}\nНужна формула для расчёта КБЖУ'
    await message.answer(ans, reply_markup=menu_kb)


def register_nutrition_router(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_nutrition,
                                       lambda call: call.data == 'nutrition')

    dp.register_message_handler(cmd_menu,
                                commands=['menu'],
                                state=[NutritionStates.Send_age,
                                       NutritionStates.Send_gender,
                                       NutritionStates.Send_weight])

    dp.register_message_handler(cmd_get_age,
                                state=NutritionStates.Send_age)

    dp.register_message_handler(cmd_get_gender,
                                state=NutritionStates.Send_gender)

    dp.register_message_handler(cmd_get_weight,
                                state=NutritionStates.Send_weight)
