from aiogram.dispatcher.filters.state import State,StatesGroup
class JobStateClass(StatesGroup):
    name = State()
    age = State()
    tel = State()
    job = State()
    salary = State()
    address = State()
    about = State()
    time = State()
    goal = State()
    check = State()


