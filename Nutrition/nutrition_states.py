from aiogram.dispatcher.filters.state import StatesGroup, State


class NutritionStates(StatesGroup):
    Send_age = State()
    Send_gender = State()
    Send_weight = State()