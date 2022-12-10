from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
button =ReplyKeyboardMarkup(resize_keyboard=True,
                            keyboard=[
                                [KeyboardButton(text ="💼 Ish kerak"),
                                 KeyboardButton(text ="🏢 Xodim kerak")],
                                [KeyboardButton(text="✍ Talab va taklif"),
                                 KeyboardButton(text="🌍 Boshqa e'lon")],
                                [
                                    KeyboardButton(text="Favqulotda 🆘"),

                                ]
                            ])
checkbtn = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2,
                               keyboard=[
                                   [KeyboardButton(text="✅ Ha"),
                                    KeyboardButton(text="❌ Yo'q")],

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
newbutton = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [KeyboardButton(text="🛑 Bekor qilish")]
                                ])