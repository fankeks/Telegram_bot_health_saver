from aiogram.dispatcher.filters.state import StatesGroup, State


class ProfileStates(StatesGroup):
    Send_age = State()
    Send_height = State()