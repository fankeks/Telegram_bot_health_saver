from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = [[KeyboardButton(text='/menu')]]
menu_kb = ReplyKeyboardMarkup(keyboard=kb,
                              resize_keyboard=True)