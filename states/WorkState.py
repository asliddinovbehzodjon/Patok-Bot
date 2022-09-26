from aiogram.dispatcher.filters.state import State,StatesGroup
class WorkStateClass(StatesGroup):
    place = State()
    job = State()
    tel = State()
    address = State()
    operator = State()
    connect = State()
    time = State()
    salary = State()
    requirements = State()
    check = State()


