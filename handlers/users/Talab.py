from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import  Text
from keyboards.default.JobButton import talab_taklif,button
@dp.message_handler(Text(startswith="✍ Talab va taklif"))
async def test(message:types.Message):
    await message.answer("✏ Talab va takliflariz biz uchun qadrli!\n"
                         "Kerakli bo'limni tanlang!",reply_markup=talab_taklif)
@dp.message_handler(Text(startswith="🔙 Orqaga"))
async def test(message:types.Message):
    await message.answer("✅ Bo'limni tanlang va biz bilan davom eting!",reply_markup=button)