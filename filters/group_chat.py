from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.filters.builtin import CallbackQuery


class IsGroup(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        )

class IsGroupCall(BoundFilter):
    async def check(self, call: CallbackQuery) -> bool:
        return call.message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        )
