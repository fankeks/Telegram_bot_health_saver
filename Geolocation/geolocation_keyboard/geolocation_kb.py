from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb = [[KeyboardButton(text='/send_location', request_location=True)],
      [KeyboardButton(text='/menu')]]
geolocation_kb = ReplyKeyboardMarkup(keyboard=kb,
                                     resize_keyboard=True)