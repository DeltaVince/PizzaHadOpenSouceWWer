import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, KeyboardButton, WebAppInfo

pizza_component_join = ["7650812272:AAEOtwEnb93SRhuK_JMFJqLqthFqsOXKv-w"]
feature = 0
calories = 0
products = {
    "лук",
    "сыр",
    "колбаса",
    "салат", 
    "ананасы",
    "грибы"
}


TOKEN = getenv("")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    markup = InlineKeyboardMarkup()
    web_app_button = KeyboardButton(
        "Перейти к Созданию пиццы",
        web_app=WebAppInfo(
            url="https://deltavince.github.io/PizzaHadOpenSouceWWer/"
        ),
    )
    markup.add(web_app_button)

    await message.answer( 
        "Конструктор Пицц!",
        reply_markup=markup,
    )

async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
