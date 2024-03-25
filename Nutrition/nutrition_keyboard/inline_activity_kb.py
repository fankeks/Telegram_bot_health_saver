from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_activity_kb = InlineKeyboardMarkup()
inline_activity_kb.add(InlineKeyboardButton('Физическая нагрузка отсутствует или минимальна', callback_data='activity_1'))
inline_activity_kb.add(InlineKeyboardButton('Тренировки средней тяжести 3 раза в неделю', callback_data='activity_2'))
inline_activity_kb.add(InlineKeyboardButton('Тренировки средней тяжести 5 раз в неделю', callback_data='activity_3'))
inline_activity_kb.add(InlineKeyboardButton('Интенсивные тренировки 5 раз в неделю', callback_data='activity_4'))
inline_activity_kb.add(InlineKeyboardButton('Тренировки каждый день', callback_data='activity_5'))
inline_activity_kb.add(InlineKeyboardButton('Интенсивные тренировки каждый день', callback_data='activity_6'))
inline_activity_kb.add(InlineKeyboardButton('Ежедневная нагрузка + физическая работа', callback_data='activity_7'))