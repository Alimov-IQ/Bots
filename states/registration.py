from aiogram.dispatcher.filters.state import State, StatesGroup


class StandartMafiaForm(StatesGroup):
    invite_code = State()
    name = State()
    gender = State()
    month = State()
    day = State()
    correct = State()


class PremiumMafiaForm(StatesGroup):
    invite_code = State()
    name = State()
    gender = State()
    month = State()
    day = State()
    instagram = State()
    correct = State()


class OpenGames(StatesGroup):
    invite_code = State()
    name = State()
    gender = State()
    month = State()
    day = State()
    correct = State()


class PremiumMafiaRestart(StatesGroup):
    instagram = State()


class InputInviteCode(StatesGroup):
    invite_code = State()

class Phone(StatesGroup):
    phone = State()