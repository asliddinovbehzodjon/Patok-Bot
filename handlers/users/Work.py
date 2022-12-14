from aiogram.dispatcher import  FSMContext
from aiogram import  types
from loader import  dp,bot
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.JobButton import checkbtn,button,newbutton
from aiogram.types import  InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import Command
from api import create_work
from aiogram.dispatcher.filters import  Text
from states.WorkState import WorkStateClass
@dp.message_handler(Text(startswith="🏢 Xodim kerak"),state=None)
async def first(message:types.Message,state:FSMContext):
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await message.answer("Idora nomini kiriting.",reply_markup=newbutton)
        await WorkStateClass.place.set()
@dp.message_handler(state=WorkStateClass.place)
async def second(message:types.Message,state:FSMContext):
    place = message.text
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            "place":place
        })
        await message.answer("<b>💻 Lavozim: \n\n</b>"
                             "Qanday mutaxassis kerak!\n"
                             "Masalan: Buxgalter",reply_markup=newbutton)
        await WorkStateClass.next()
@dp.message_handler(state=WorkStateClass.job)
async def third(message:types.Message,state:FSMContext):
    job = message.text
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            "job":job
        })
        await message.answer("<b>📞 Aloqa:</b>\n\n"
                             "Bog`lanish uchun raqamingizni kiriting?\n"
                             "Masalan, +998 90 123 45 67",reply_markup=newbutton)
        await WorkStateClass.next()
@dp.message_handler(state=WorkStateClass.tel)
async def sixth(message:types.Message,state:FSMContext):
    tel = message.text
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            "tel":tel
        })
        await message.answer("<b>🌐 Hudud:   </b>\n\n"
                             "Qaysi hududdansiz?\n"
                             "Masalan: Toshkent",reply_markup=newbutton)
        await WorkStateClass.next()
@dp.message_handler(state=WorkStateClass.address)
async def fifth(message:types.Message,state:FSMContext):
    address= message.text
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            "address":address
        })
        await message.answer("<b>✍ Mas'ul:</b>\n\n",reply_markup=newbutton)
        await WorkStateClass.next()
@dp.message_handler(state=WorkStateClass.operator)
async def sixth(message:types.Message,state:FSMContext):
    operator = message.text
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            "operator":operator
        })
        await message.answer("<b>🕰 Murojaat qilish vaqti:  </b>\n\n"
                             "Qaysi vaqtda murojaat qilish mumkin?\n"
                              "Masalan, 9:00 - 18:00",reply_markup=newbutton)
        await WorkStateClass.next()
@dp.message_handler(state=WorkStateClass.connect)
async def sixth(message:types.Message,state:FSMContext):
    connect = message.text
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            "connect":connect
        })
        await message.answer("<b>🕰 Ish vaqti::  </b>\n\n"
                              "Masalan, 9:00 - 18:00",reply_markup=newbutton)
        await WorkStateClass.next()
@dp.message_handler(state=WorkStateClass.time)
async def sixth(message:types.Message,state:FSMContext):
    time = message.text
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            "time":time
        })
        await message.answer("<b>💰 Maosh:</b>\n\n"  
                             "Masalan: 300$",reply_markup=newbutton)
        await WorkStateClass.next()
@dp.message_handler(state=WorkStateClass.salary)
async def sixth(message:types.Message,state:FSMContext):
    salary = message.text
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            "salary":salary
        })
        await message.answer("<b>🔢 Talablar: </b>\n\n"
                             "Masalan:Rus tilini yaxshi bilishi kerak!",reply_markup=newbutton)
        await WorkStateClass.next()
@dp.message_handler(state=WorkStateClass.requirements)
async def sixth(message:types.Message,state:FSMContext):
    requirements= message.text
    await state.update_data({
        "requirements":requirements
    })
    data = await  state.get_data()
    telegram = message.from_user.username
    if telegram:
        result = f"<b>Xodim kerak</b>\n\n " \
                 f"🏢 Idora: <b>{data['place']}</b>\n" \
                 f"💻 Lavozim: <b>{data['job']}</b>\n" \
                 f"📞 Aloqa: <b>{data['tel']}</b>\n" \
                 f"💬 Telegram: <b>@{telegram}</b>\n" \
                 f"💰 Maosh: <b>{data['salary']}</b>\n" \
                 f"🌎 Hudud: <b>{data['address']}</b>\n" \
                 f"🕰 Murojaat qilish vaqti: : <b>{data['connect']}</b>\n" \
                 f"🕰 Ish vaqti: : <b>{data['time']}</b>\n" \
                 f"🔢 Talablar: <b>{data['requirements']}</b>"
    else:
        result = f"<b>Xodim kerak</b>\n\n " \
                 f"🏢 Idora: <b>{data['place']}</b>\n" \
                 f"💻 Lavozim: <b>{data['job']}</b>\n" \
                 f"📞 Aloqa: <b>{data['tel']}</b>\n" \
                 f"💰 Maosh: <b>{data['salary']}</b>\n" \
                 f"🌎 Hudud: <b>{data['address']}</b>\n" \
                 f"🕰 Murojaat qilish vaqti: : <b>{data['connect']}</b>\n" \
                 f"🕰 Ish vaqti: : <b>{data['time']}</b>\n" \
                 f"🔢 Talablar: <b>{data['requirements']}</b>"
    await message.answer(result)
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=checkbtn)
    await WorkStateClass.next()

@dp.message_handler(state=WorkStateClass.check)
async def sixth(message:types.Message,state:FSMContext):
    mycheck = message.text
    id=message.from_user.id

    if mycheck=="✅ Ha":
        data = await  state.get_data()
        telegram = message.from_user.username
        if telegram:
            result = f"<b>Xodim kerak</b>\n\n " \
                     f"🏢 Idora: <b>{data['place']}</b>\n" \
                     f"💻 Lavozim: <b>{data['job']}</b>\n" \
                     f"📞 Aloqa: <b>{data['tel']}</b>\n" \
                     f"💬 Telegram: <b>@{telegram}</b>\n" \
                     f"💰 Maosh: <b>{data['salary']}</b>\n" \
                     f"🌎 Hudud: <b>{data['address']}</b>\n" \
                     f"🕰 Murojaat qilish vaqti: : <b>{data['connect']}</b>\n" \
                     f"🕰 Ish vaqti: : <b>{data['time']}</b>\n" \
                     f"🔢 Talablar: <b>{data['requirements']}</b>"
        else:
            result = f"<b>Xodim kerak</b>\n\n " \
                     f"🏢 Idora: <b>{data['place']}</b>\n" \
                     f"💻 Lavozim: <b>{data['job']}</b>\n" \
                     f"📞 Aloqa: <b>{data['tel']}</b>\n" \
                     f"💰 Maosh: <b>{data['salary']}</b>\n" \
                     f"🌎 Hudud: <b>{data['address']}</b>\n" \
                     f"🕰 Murojaat qilish vaqti: : <b>{data['connect']}</b>\n" \
                     f"🕰 Ish vaqti: : <b>{data['time']}</b>\n" \
                     f"🔢 Talablar: <b>{data['requirements']}</b>"
        send = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    inline_keyboard=[
                                        [InlineKeyboardButton(text="✅ E'lon qilish", callback_data=f'send{id}')],
                                        [InlineKeyboardButton(text="❌ Bekor qilish", callback_data=f'cancel{id}')]
                                    ])
        create_work(company=data['place'],job=data['job'],phone=data['tel'],salary=data['salary'],address=data['address'],contact_time=data['connect'],requirements=data['requirements'],work_time=data['time'])
        await bot.send_message(chat_id=-1001758444864,text=result,reply_markup=send)
        await message.answer(f"<b>📪 So`rovingiz tekshirish uchun adminga jo`natildi!</b>\n"
                             f"E'lon 24-48 soat ichida kanalda chiqariladi.",reply_markup=ReplyKeyboardRemove())

        await state.finish()
    else:
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!",reply_markup=button)
        await state.finish()






