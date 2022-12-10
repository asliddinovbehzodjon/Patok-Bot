from aiogram import types
from loader import dp,bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from api import create_another
from states.Another import AnotherState
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardRemove
from keyboards.default.JobButton import newbutton,button,checkbtn
@dp.message_handler(Text(startswith="🌍 Boshqa e'lon"),state=None)
async def func1(message:types.Message,state:FSMContext):
    await message.answer("E'lon uchun sarlavha kiriting...",reply_markup=newbutton)
    await AnotherState.title.set()
@dp.message_handler(state=AnotherState.title)
async def func2(message:types.Message,state:FSMContext):

    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
          'title':message.text
        })
        await message.answer("E'lon haqida batafsil tarvirlab bering!",reply_markup=newbutton)
        await AnotherState.next()
@dp.message_handler(state=AnotherState.description)
async def func3(message:types.Message,state:FSMContext):
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            'description': message.text
        })
        await message.answer("Mahsulot yoki xizmat narxini kiriting!", reply_markup=newbutton)
        await AnotherState.next()
@dp.message_handler(state=AnotherState.price)
async def func4(message:types.Message,state:FSMContext):
    if message.text == "🛑 Bekor qilish" or (message.text).startswith('/'):
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()
    else:
        await state.update_data({
            'price': message.text
        })
        await message.answer("Aloqa uchun raqam kiriting!", reply_markup=newbutton)
        await AnotherState.next()
@dp.message_handler(state=AnotherState.connect)
async def func5(message:types.Message,state:FSMContext):
    await state.update_data({
        'connect': message.text
    })
    data = await  state.get_data()
    telegram = message.from_user.username
    if telegram:
        result = f"<b>🔖 E'lon: </b>{data['title']}\n" \
                 f"<b>💬 Batafsil: </b> {data['description']}\n" \
                 f"<b>💲 Narx yoki xizmat haqqi: </b> {data['price']}\n" \
                 f"<b>☎ Aloqa: </b>: {data['connect']}\n" \
                 f"<b>✍ Telegram: </b> @{telegram}"
    else:
        result = f"<b>🔖 E'lon: </b>{data['title']}\n" \
                 f"<b>💬 Batafsil: </b> {data['description']}\n" \
                 f"<b>💲 Narx yoki xizmat haqqi: </b> {data['price']}\n" \
                 f"<b>☎ Aloqa: </b>: {data['connect']}\n"
    await message.answer(result)
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=checkbtn)
    await AnotherState.next()
@dp.message_handler(state=AnotherState.check)
async def func5(message:types.Message,state:FSMContext):
    mycheck = message.text
    id = message.from_user.id

    if mycheck == "✅ Ha":
        data = await  state.get_data()
        telegram = message.from_user.username
        if telegram:
            result = f"<b>🔖 E'lon: </b>{data['title']}\n" \
                     f"<b>💬 Batafsil: </b> {data['description']}\n" \
                     f"<b>💲 Narx yoki xizmat haqqi: </b> {data['price']}\n" \
                     f"<b>☎ Aloqa: </b>: {data['connect']}\n" \
                     f"<b>✍ Telegram: </b>@{telegram}"
        else:
            result = f"<b>🔖 E'lon: </b>{data['title']}\n" \
                     f"<b>💬 Batafsil: </b> {data['description']}\n" \
                     f"<b>💲 Narx yoki xizmat haqqi: </b> {data['price']}\n" \
                     f"<b>☎ Aloqa: </b>: {data['connect']}\n"
        send = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    inline_keyboard=[
                                        [InlineKeyboardButton(text="✅ E'lon qilish", callback_data=f'send{id}')],
                                        [InlineKeyboardButton(text="❌ Bekor qilish", callback_data=f'cancel{id}')]
                                    ])
        create_another(title=data['title'],description=data['description'],price=data['price'],connect=data['connect'])
        await bot.send_message(chat_id=-1001758444864, text=result, reply_markup=send)
        await message.answer(f"<b>📪 So`rovingiz tekshirish uchun adminga jo`natildi!</b>\n"
                             f"E'lon 24-48 soat ichida kanalda chiqariladi.", reply_markup=ReplyKeyboardRemove())

        await state.finish()
    else:
        await message.answer("E'lon berish uchun kerakli bo'limni tanlang!", reply_markup=button)
        await state.finish()



