from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_profile_kb = InlineKeyboardMarkup()
inline_profile_kb.add(InlineKeyboardButton('Изменить пол', callback_data='change_gender'))
inline_profile_kb.add(InlineKeyboardButton('Изменить возраст', callback_data='change_age'))
inline_profile_kb.add(InlineKeyboardButton('Изменить рост', callback_data='change_height'))
inline_profile_kb.add(InlineKeyboardButton('Изменить вес', callback_data='change_weight'))
inline_profile_kb.add(InlineKeyboardButton('Изменить цель', callback_data='change_target'))