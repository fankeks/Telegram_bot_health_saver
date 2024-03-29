from aiogram.utils import executor
from aiogram.types import BotCommand
import os

from create_bot import ans
from Data_base.DataBase import data
from Main.main_router import register_main_router
from Nutrition.nutrition_router import register_nutrition_router
from Geolocation.geolocation_router import register_geolocation_router
from Profile.profile_router import register_profile_router
from Training.training_router import register_training_router


if ans:
    bot = ans[0]
    dp = ans[1]
    storage = ans[2]


async def on_startup(_):
    await data.start()
    bot_commands = [
        BotCommand(command="/menu", description="Меню"),
    ]
    await bot.set_my_commands(bot_commands)
    await bot.set_webhook(url='', allowed_updates=["message", "inline_query", "callback_query"])
    print('Бот запущен')


async def on_shutdown(_):
    await storage.close()
    await (await bot.get_session()).close()


if __name__ == '__main__':
    try:
        os.mkdir('Temp')
    except:
        pass
    register_main_router(dp)
    register_nutrition_router(dp)
    register_geolocation_router(dp)
    register_profile_router(dp)
    register_training_router(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)