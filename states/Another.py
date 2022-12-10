from aiogram.dispatcher.filters.state import State,StatesGroup
class AnotherState(StatesGroup):
    title = State()
    description = State()
    price = State()
    connect = State()
    check = State()

