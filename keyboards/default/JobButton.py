from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
button =ReplyKeyboardMarkup(resize_keyboard=True,
                            keyboard=[
                                [KeyboardButton(text ="💼 Ish kerak")]
                            ])
checkbtn = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2,
                               keyboard=[
                                   [KeyboardButton(text="✅ Ha"),
                                    KeyboardButton(text="❌ Yo'q")],

                               ])
send= InlineKeyboardMarkup(resize_keyboard=True,row_width=2,
                               inline_keyboard=[
                                   [InlineKeyboardButton(text="✅ E'lon qilish",callback_data='send')],
                                   [InlineKeyboardButton(text="❌ Bekor qilish",callback_data='cancel')]
                               ])