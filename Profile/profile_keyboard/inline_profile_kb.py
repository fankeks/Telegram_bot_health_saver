from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_profile_kb = InlineKeyboardMarkup()
inline_profile_kb.add(InlineKeyboardButton('Изменить пол', callback_data='change_gender'))
inline_profile_kb.add(InlineKeyboardButton('Изменить возраст', callback_data='change_age'))
inline_profile_kb.add(InlineKeyboardButton('Изменить рост', callback_data='change_height'))