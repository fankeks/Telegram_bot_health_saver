from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from Geolocation.geolocation_keyboard.geolocation_kb import geolocation_kb
from Main.main_keyboard.menu_kb import menu_kb


async def cmd_geolocation(callback: CallbackQuery):
    await callback.message.answer('Для отправки геолокации нажмите кнопку', reply_markup=geolocation_kb)


async def cmd_get_geolocation(message: Message):
    loc1 = message.location.latitude
    loc2 = message.location.longitude
    await message.answer(str(loc1) + ' ' + str(loc2), reply_markup=menu_kb)


def register_geolocation_router(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_geolocation, lambda call: call.data == 'geolocation')

    dp.register_message_handler(cmd_get_geolocation,
                                content_types=['location'])