from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
button =ReplyKeyboardMarkup(resize_keyboard=True,
                            keyboard=[
                                [KeyboardButton(text ="💼 Ish kerak"),
                                 KeyboardButton(text ="🏢 Xodim kerak")],
                                [KeyboardButton(text="✍ Talab va taklif"),
                                 KeyboardButton(text="🌍 Boshqa e'lon")],
                                [
                                    KeyboardButton(text="Favqulotda 🆘"),
                                    KeyboardButton(text="Cv va Rezumi 📝")
                                ]
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
talab_taklif= ReplyKeyboardMarkup(resize_keyboard=True,row_width=2,
                               keyboard=[
                                   [KeyboardButton(text="Biz haqimizda"),
                                    KeyboardButton(text="Platforma haqida")],
                                   [
                                    KeyboardButton(text="Hamkorlik"),
                                    KeyboardButton(text="🔙 Orqaga")
                                   ]
                               ])
favqulotda= ReplyKeyboardMarkup(resize_keyboard=True,row_width=2,
                               keyboard=[
                                   [KeyboardButton(text="Yo'qolgan buyumlar"),
                                    KeyboardButton(text="Yo'qolgan odamlar")],
                                   [
                                    KeyboardButton(text="Sharoitim og'ir"),
                                    KeyboardButton(text="🔙 Orqaga")
                                   ]
                               ])