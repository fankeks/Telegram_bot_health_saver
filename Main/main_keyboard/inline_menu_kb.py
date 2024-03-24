from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_menu_kb = InlineKeyboardMarkup()
inline_menu_kb.add(InlineKeyboardButton('Тренировки', callback_data='training'))
inline_menu_kb.add(InlineKeyboardButton('Питание', callback_data='nutrition'))
inline_menu_kb.add(InlineKeyboardButton('Места для тренировок', callback_data='geolocation'))
inline_menu_kb.add(InlineKeyboardButton('Медитации', callback_data='meditations'))