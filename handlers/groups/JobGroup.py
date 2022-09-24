import io

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command,CallbackQuery

from filters import IsGroup,IsGroupCall
from filters.admins import AdminFilter
from loader import dp, bot
@dp.callback_query_handler(IsGroupCall(), text='send')
async def send(call:CallbackQuery):
    await call.answer(cache_time=60)
    id = call.message.message_id
    await bot.forward_message(chat_id=-1001623898668,from_chat_id=-1001714221854,message_id=id)
    await call.message.delete()
    await call.message.answer("✅ Hurmatli admin xabar yuborildi!")

@dp.callback_query_handler(IsGroupCall(), text='cancel')
async def send(call:CallbackQuery):
    await call.message.delete()
    id = call.message.message_id
    await bot.delete_message(chat_id=call.from_user.id,message_id=id)
    await call.message.answer("🗑 E'lon o'chirildi!")
