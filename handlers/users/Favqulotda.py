from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import  Text
from keyboards.default.JobButton import talab_taklif,button,favqulotda
@dp.message_handler(Text(startswith="Favqulotda 🆘"))
async def test(message:types.Message):
    await message.answer("🆘 Qanday yordam kerak?!\n"
                         "Kerakli bo'limni tanlang!",reply_markup=favqulotda)
