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
@dp.message_handler(Text(startswith="Biz haqimizda"))
async def test(message:types.Message):
    await message.answer(f"<b>👥 Birmiz</b> - bu milliy loyiha bo'lib,musofir hamyurtlarimizga yordam berish uchun tayyorlandi!")
@dp.message_handler(Text(startswith="Platforma haqida"))
async def test(message:types.Message):
    await message.answer("<b>Birmiz</b> - chet eldagi hamyurtlarimizga ish, ishchi e'lonlari ulashishga yordam beruvchi platforma hisoblanadi! ")
@dp.message_handler(Text(startswith="Hamkorlik"))
async def test(message:types.Message):
    await message.answer("❓ Biz bilan hamkorlik qilishni istaysizmi?!\n"
                         "Unda biz bilan hoziroq bog'laning!\n\n"
                         "<b>📞 Telefon raqam: </b> <i>+99899 975-44-44</i>\n"
                         "<b>🧑‍💻 Telegram : </b> <i>@birmizadmin</i>\n"
                         "<b>📨 Email : </b> <i>info@birmiz.com</i>")
