from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_target_kb = InlineKeyboardMarkup()
inline_target_kb.add(InlineKeyboardButton('Сброс веса', callback_data='weight_loss'))
inline_target_kb.add(InlineKeyboardButton('Поддержание массы', callback_data='weight_maintaining'))
inline_target_kb.add(InlineKeyboardButton('Набор массы', callback_data='weight_gain'))