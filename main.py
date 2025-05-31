import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardButton

dp = Dispatcher()
TOKEN = '7650812272:AAEOtwEnb93SRhuK_JMFJqLqthFqsOXKv-w'

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Конструктор пицц")

@dp.message(Command('pizza'))
async def command_pizza_handler(message: Message) -> None:
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
          [
              InlineKeyboardButton(
                  text="pizza_constarkt",
                  web_app=WebAppInfo(url=f'https://deltavince.github.io/PizzaHadOpenSouceWWer/'),
              )
          ]  
        ]  
    )
    await message.answer(text='Перейти к созданию пиццы', reply_markup=markup)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
