import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from handlers.admin_private import admin_router
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router

from common.bot_cmds_list import private_chat_commands

ALLOWED_UPDATES=['message, edited message']

bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.MARKDOWN_V2) #достаем переменную из окружения .env
bot.my_admins_list = []

dp = Dispatcher()

dp.include_router(admin_router)
dp.include_router(user_private_router)
dp.include_router(user_group_router)

async def main():
    print('bot started\n')
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats) #this string deletes all the commands
    await bot.set_my_commands(commands=private_chat_commands, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    print('bot stopped')

asyncio.run(main())