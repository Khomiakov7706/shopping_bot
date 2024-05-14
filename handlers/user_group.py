
from string import punctuation

from aiogram import F, Bot, types, Router

from filters.chat_types import ChatTypeFilter
from aiogram.filters import Command

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

restricted_words = {'кабан', 'хомяк', 'выхухоль'}

#Проверка на администратора из списка администраторов группы
@user_group_router.message(Command("admin"))
async def get_admins(message: types.Message, bot: Bot):
    chat_id = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)
    #Просмотреть все данные и свойства полученных объектов
    print(admins_list)

    #генератор списка администроаторов группы с чат-ботом по типу x = [i for i in range(10)]
    admins_list = [
        member.user.id
        for member in admins_list
        if member.status == "creator" or member.status == "administrator"
    ]

    bot.my_admins_list = admins_list
    if message.from_user.id in admins_list:
        await message.delete()
    print(admins_list)

def clean_text(text: str):
    return text.translate(str.maketrans('','',punctuation))

@user_group_router.edited_message()
@user_group_router.message()
async def  cleaner(message: types.Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.reply(f"{message.from_user.first_name}, соблюдайте порядок в чате\!")
        await message.delete()

