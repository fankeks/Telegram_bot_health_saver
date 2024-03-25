from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_genders_kb = InlineKeyboardMarkup(row_width=2)
inline_genders_kb.add(InlineKeyboardButton('Мужской', callback_data='gender_male'),
                      InlineKeyboardButton('Женский', callback_data='gender_female'))