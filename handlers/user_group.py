
from string import punctuation

from aiogram import F, types, Router

user_group_router = Router()

restricted_words = {'кабан', 'хомяк', 'выхухоль'}

#def clean_text(text: str):
#    return text.translate(str.meketrans('','',punctuation))

@user_group_router.message()
async def  cleaner(message: types.Message):
    if restricted_words.intersection(message.text.lower().split()):
        await message.reply(f"{message.from_user.first_name}, соблюдайте порядок в чате!")
        await message.delete()

