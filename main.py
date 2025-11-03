from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from deep_translator import GoogleTranslator
from num2words import num2words
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()


TOKEN = os.getenv("TOKEN")

db = Dispatcher()

@db.message(CommandStart())
async def starter(message: Message):
    await message.answer(f"Asslomu alaykum {message.from_user.first_name}, Botga xush kelibsiz \nIxtiyoriy raqam yozsangiz men sizga yozma ko'rinishini yuboraman")

@db.message()
async def tarjima(message: Message):
    try:
        a = num2words(int(message.text))
        turn = GoogleTranslator(source='auto', target='uz').translate(a)
        await message.answer(turn)
    except:
        await message.answer("Iltimos raqam yozing")


async def main():
    print("bot ishda")
    bot = Bot(TOKEN)
    await db.start_polling(bot)

asyncio.run(main())


