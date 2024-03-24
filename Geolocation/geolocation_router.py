from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from Geolocation.geolocation_keyboard.geolocation_kb import geolocation_kb
from Geolocation.geolocation_states import GeolocationStates
from Main.main_keyboard.inline_menu_kb import inline_menu_kb
from Main.main_keyboard.menu_kb import menu_kb


async def cmd_geolocation(callback: CallbackQuery):
    await callback.message.answer('Для отправки геолокации нажмите кнопку', reply_markup=geolocation_kb)
    await GeolocationStates.Send_geolocation.set()


async def cmd_menu(message: Message, state: FSMContext):
    await state.finish()
    await message.answer('Возврат в главное меню', reply_markup=menu_kb)
    await message.answer('Выберите функцию', reply_markup=inline_menu_kb)
    await message.delete()


async def cmd_get_geolocation(message: Message, state: FSMContext):
    await state.finish()
    loc1 = message.location.latitude
    loc2 = message.location.longitude
    await message.answer(str(loc1) + ' ' + str(loc2), reply_markup=menu_kb)


def register_geolocation_router(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_geolocation, lambda call: call.data == 'geolocation')
    dp.register_message_handler(cmd_menu,
                                commands=['menu'],
                                state=GeolocationStates.Send_geolocation)
    dp.register_message_handler(cmd_get_geolocation,
                                content_types=['location'],
                                state=GeolocationStates.Send_geolocation)