from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.types import Message
import os

from Training.Processing_video.ProcessAcync import ProcessAsync


from create_bot import ans
if ans:
    bot = ans[0]
    dp = ans[1]
    storage = ans[2]


async def cmd_training(callback: CallbackQuery):
    await callback.message.answer("Отправьте видео")


async def video_handler(message: Message):
    file_id = message.video.file_id  # Get file id
    file = await bot.get_file(file_id)  # Get file path
    path = os.path.join('Temp', str(message.from_user.id) + '.mp4')
    await bot.download_file(file.file_path, path)

    p = ProcessAsync(path)
    await p.start()
    await message.answer_chat_action("typing")
    await p.join()
    os.remove(path)
    path = path.split('.')[0] + '_out' + ".mp4"
    await bot.send_video(message.chat.id, open(path, 'rb'))
    os.remove(path)


def register_training_router(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_training,
                                       lambda call: call.data == 'training')

    dp.register_message_handler(video_handler,
                                content_types=["video"])