import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
import asyncio

TOKEN = "7987718226:AAHjF8XozKueiCWOj7p0250KMiyGNeB9tYY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

def safe_eval(expression):
    allowed_chars = "0123456789+-*/(). "
    if all(char in allowed_chars for char in expression):
        try:
            return eval(expression, {"__builtins__": {}})
        except:
            return "Xato! Iltimos, to‘g‘ri misol kiriting."
    else:
        return "Xato! Noto‘g‘ri belgilar ishlatildi."

@dp.message(F.text == "/start")
async def start_cmd(message: Message):
    await message.answer("Salom! Men kalkulyator botman. Misol kiriting (masalan: 5+3):")

@dp.message()
async def calculate(message: Message):
    expression = message.text.replace(" ", "")
    result = safe_eval(expression)
    await message.answer(f"Natija: {result}")

async def main():
    logging.info("✅ Bot ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
