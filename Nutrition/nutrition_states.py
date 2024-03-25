from aiogram.dispatcher.filters.state import StatesGroup, State


class NutritionStates(StatesGroup):
    Send_weight = State()
    Send_activity = State()