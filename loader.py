from aiogram import Bot, Dispatcher, types
from pathlib import Path
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from data import config
# I18N_DOMAIN = 'mybot'
# BASE_DIR = Path(__file__).parent
# LOCALES_DIR = BASE_DIR / 'locales'
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# i18n = I18nMiddleware(I18N_DOMAIN, LOCALES_DIR,default='uz')
# dp.middleware.setup(i18n)
# _ = i18n.gettext