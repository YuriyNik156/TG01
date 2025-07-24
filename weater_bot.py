import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN, WEATHER_API_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer("Привет! Я бот, который передает прогноз погоды. Напиши /help, чтобы узнать что я умею.")

@dp.message(Command('help'))
async def help(message:Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help \n /weather')

