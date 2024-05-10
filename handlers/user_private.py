
from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command

user_private_router=Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я виртуальный помощник')

@user_private_router.message(Command('menu'))
async def echo(message: types.Message):
    #await message.answer(message.text)
    await message.reply("Вот меню")

@user_private_router.message(Command('about'))
async def echo(message: types.Message):
    #await message.answer(message.text)
    await message.reply("О нас")

@user_private_router.message(Command('payment'))
async def echo(message: types.Message):
    #await message.answer(message.text)
    await message.reply("Варианты оплаты")

@user_private_router.message(Command('shipping'))
async def echo(message: types.Message):
    #await message.answer(message.text)
    await message.reply("Варианты доставки")

@user_private_router.message(F.text.lower()=='варианты доставки')
async def echo(message: types.Message):
    #await message.answer(message.text)
    await message.reply(str("Это магический фильтр для " + message.text))

@user_private_router.message(F.text.lower().contains('варианты доставки'))
async def echo(message: types.Message):
    #await message.answer(message.text)
    await message.reply(str("Это магический фильтр для любого вхождения вариантов доставки, в том числе " + message.text))
 

@user_private_router.message(F.text)
async def echo(message: types.Message):
    #await message.answer(message.text)
    await message.reply(str("Это магический фильтр, " + message.text))

