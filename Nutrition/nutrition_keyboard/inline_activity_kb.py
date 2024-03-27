from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_activity_kb = InlineKeyboardMarkup()
inline_activity_kb.add(InlineKeyboardButton('Минимальный (сидячая работа, отсутствие физических нагрузок)', callback_data='activity_1'))
inline_activity_kb.add(InlineKeyboardButton('Низкий (тренировки не менее 20 мин 1-3 раза в неделю)', callback_data='activity_2'))
inline_activity_kb.add(InlineKeyboardButton('Умеренный (тренировки 30-60 мин 3-4 раза в неделю)', callback_data='activity_3'))
inline_activity_kb.add(InlineKeyboardButton('Высокий (тренировки 30-60 мин 5-7 раза в неделю; тяжелая физическая работа)', callback_data='activity_4'))
inline_activity_kb.add(InlineKeyboardButton('Экстремальный (несколько интенсивных тренировок в день 6-7 раз в неделю; очень трудоемкая работа)', callback_data='activity_5'))