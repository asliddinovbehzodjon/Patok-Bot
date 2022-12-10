from aiogram.dispatcher import  FSMContext
from aiogram import  types
from aiogram.types import  InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardRemove
from loader import  dp,bot
from aiogram.types import ReplyKeyboardRemove
from api import create_worker
from keyboards.default.JobButton import checkbtn,button
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher.filters import  Text
from keyboards.default.JobButton import newbutton
from states.JobState import JobStateClass
@dp.message_handler(Text(startswith="💼 Ish kerak"),state=None)
async def first(message:types.Message):
    await message.answer("Ism va familyangizni kiriting.",reply_markup=newbutton)
    await JobStateClass.name.set()
@dp.message_handler(state=JobStateClass.name)
async def second(message:types.Message,state:FSMContext):
    name = message.text

    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer( "E'lon berish uchun kerakli bo'limni tanlang!",reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            "name": name
        })
        await message.answer("<b>🕑 Yosh: \n\n</b>"
                             "Iltimos yoshingizni kiriting!\n"
                             "Masalan: 27",reply_markup=newbutton)
        await JobStateClass.next()
@dp.message_handler(state=JobStateClass.age)
async def third(message:types.Message,state:FSMContext):
    age = message.text
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer( "E'lon berish uchun kerakli bo'limni tanlang!",reply_markup=button)
        await state.finish()

    else:
        await state.update_data({
            "age": age
        })
        await message.answer("<b>📞 Aloqa:</b>\n\n"
                             "Bog`lanish uchun raqamingizni kiriting?\n"
                             "Masalan, +998 90 123 45 67",reply_markup=newbutton)
        await JobStateClass.next()
@dp.message_handler(state=JobStateClass.tel)
async def forth(message:types.Message,state:FSMContext):
    phone = message.text
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            "phone": phone
        })
        await message.answer("<b>💼 Kasbingiz:</b>\n\n"
                             "Qanday kasb yoki hunar egasiz?\n"
                             "Masalan, Buxgalter,Quruvchi",reply_markup=newbutton)
        await JobStateClass.next()
@dp.message_handler(state=JobStateClass.job)
async def fifth(message:types.Message,state:FSMContext):
    job = message.text
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            "job": job
        })
        await message.answer("<b>💰 Maosh:</b>\n\n"
                             "Qancha maosh so'raysiz?\n"
                             "Masalan: 300$",reply_markup=newbutton)
        await JobStateClass.next()
@dp.message_handler(state=JobStateClass.salary)
async def sixth(message:types.Message,state:FSMContext):
    salary = message.text
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            "salary": salary
        })
        await message.answer("<b>🌐 Hudud:   </b>\n\n"
                             "Qaysi hududdansiz?\n"
                             "Masalan: Toshkent",reply_markup=newbutton)
        await JobStateClass.next()
@dp.message_handler(state=JobStateClass.address)
async def sixth(message:types.Message,state:FSMContext):
    address = message.text
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            "address": address
        })
        await message.answer("<b>ℹ O'zingiz haqingizda ma'lumot: </b>\n\n"
                             "Masalan: Men yaxshi quruvchiman!",reply_markup=newbutton)
        await JobStateClass.next()
@dp.message_handler(state=JobStateClass.about)
async def sixth(message:types.Message,state:FSMContext):
    about = message.text
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            "about":about
        })
        await message.answer("<b>🕰 Murojaat qilish vaqti:  </b>\n\n"
                             "Qaysi vaqtda murojaat qilish mumkin?\n"
                              "Masalan, 9:00 - 18:00",reply_markup=newbutton)
        await JobStateClass.next()
@dp.message_handler(state=JobStateClass.time)
async def sixth(message:types.Message,state:FSMContext):
    time = message.text
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            "time": time
        })
        await message.answer("<b>🎯 Maqsad: :  </b>\n\n"
                             "Maqsadingizni qisqacha yozib bering.\n",reply_markup=newbutton)
        await JobStateClass.next()


@dp.message_handler(state=JobStateClass.goal)
async def sixth(message:types.Message,state:FSMContext):
    goal = message.text
    await state.update_data({
        "goal":goal
    })
    data = await  state.get_data()
    telegram = message.from_user.username
    if telegram:
        result = f"<b>Ish kerak</b>\n\n " \
                 f"👤 Ishchi: <b>{data['name']}</b>\n" \
                 f"🌐 Yosh: <b>{data['age']}</b>\n" \
                 f"📞 Aloqa: <b>{data['phone']}</b>\n" \
                 f"💬 Telegram: <b>@{telegram}</b>\n" \
                 f"💼 Kasb: <b>{data['job']}</b>\n" \
                 f"💰 Maosh: <b>{data['salary']}</b>\n" \
                 f"🌎 Hudud: <b>{data['address']}</b>\n" \
                 f"ℹ Qisqacha malumot: <b>{data['about']}</b>\n" \
                 f"🕰 Murojaat qilish vaqti: : <b>{data['time']}</b>\n" \
                 f"🎯 Maqsad: <b>{data['goal']}</b>"
    else:
        result = f"<b>Ish kerak</b>\n\n " \
                 f"👤 Ishchi: <b>{data['name']}</b>\n" \
                 f"🌐 Yosh: <b>{data['age']}</b>\n" \
                 f"📞 Aloqa: <b>{data['phone']}</b>\n" \
                 f"💼 Kasb: <b>{data['job']}</b>\n" \
                 f"💰 Maosh: <b>{data['salary']}</b>\n" \
                 f"🌎 Hudud: <b>{data['address']}</b>\n" \
                 f"ℹ Qisqacha malumot: <b>{data['about']}</b>\n" \
                 f"🕰 Murojaat qilish vaqti: : <b>{data['time']}</b>\n" \
                 f"🎯 Maqsad: <b>{data['goal']}</b>"
    await message.answer(result)
    await message.answer("Barcha ma'lumotlar to'g'rimi?",reply_markup=checkbtn)
    await JobStateClass.next()
@dp.message_handler(state=JobStateClass.check)
async def sixth(message:types.Message,state:FSMContext):
    mycheck = message.text
    id = message.from_user.id

    if mycheck=="✅ Ha":
        data = await  state.get_data()
        telegram = message.from_user.username
        if telegram:
            result = f"<b>Ish kerak</b>\n\n " \
                 f"👤 Ishchi: <b>{data['name']}</b>\n" \
                 f"🌐 Yosh: <b>{data['age']}</b>\n" \
                 f"📞 Aloqa: <b>{data['phone']}</b>\n" \
                 f"💬 Telegram: <b>@{telegram}</b>\n"\
                 f"💼 Kasb: <b>{data['job']}</b>\n" \
                 f"💰 Maosh: <b>{data['salary']}</b>\n" \
                 f"🌎 Hudud: <b>{data['address']}</b>\n" \
                 f"ℹ Qisqacha malumot: <b>{data['about']}</b>\n" \
                 f"🕰 Murojaat qilish vaqti: : <b>{data['time']}</b>\n" \
                 f"🎯 Maqsad: <b>{data['goal']}</b>"
        else:
            result = f"<b>Ish kerak</b>\n\n " \
                     f"👤 Ishchi: <b>{data['name']}</b>\n" \
                     f"🌐 Yosh: <b>{data['age']}</b>\n" \
                     f"📞 Aloqa: <b>{data['phone']}</b>\n" \
                     f"💼 Kasb: <b>{data['job']}</b>\n" \
                     f"💰 Maosh: <b>{data['salary']}</b>\n" \
                     f"🌎 Hudud: <b>{data['address']}</b>\n" \
                     f"ℹ Qisqacha malumot: <b>{data['about']}</b>\n" \
                     f"🕰 Murojaat qilish vaqti: : <b>{data['time']}</b>\n" \
                     f"🎯 Maqsad: <b>{data['goal']}</b>"
        send = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                        inline_keyboard=[
                                            [InlineKeyboardButton(text="✅ E'lon qilish", callback_data=f'send{id}')],
                                            [InlineKeyboardButton(text="❌ Bekor qilish", callback_data=f'cancel{id}')]
                                        ])
        create_worker(name=data['name'],age=data['age'],salary=data['salary'],phone=data['phone'],contact_time=data['time'],about=data['about'],address=data['address'],job=data['job'],aim=data['goal'])
        await bot.send_message(chat_id=-1001758444864,text=result,reply_markup=send)
        await message.answer(f"<b>📪 So`rovingiz tekshirish uchun adminga jo`natildi!</b>\n"
                             f"E'lon 24-48 soat ichida kanalda chiqariladi.",reply_markup=ReplyKeyboardRemove())

        await state.finish()
    else:
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!",reply_markup=button)
        await state.finish()






