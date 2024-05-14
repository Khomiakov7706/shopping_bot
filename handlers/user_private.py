
from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter
from aiogram.utils.formatting import as_list, as_marked_section, Bold


from input_keyboards import reply

user_private_router=Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я виртуальный помощник', 
                         reply_markup=reply.start_kb3.as_markup(
                             resize_keyboard = True,
                             input_field_placeholder='Что вас интересует?'
                         ))

@user_private_router.message(or_f(Command('menu'),(F.text.lower() == "меню")))
async def echo(message: types.Message):
    #await message.answer(message.text)
    await message.reply("Вот меню", reply_markup=reply.remove_keyboard)

@user_private_router.message(or_f(Command('about'),(F.text.lower() == "о магазине")))
async def echo(message: types.Message):
    #await message.answer(message.text)
    await message.reply("О магазине", reply_markup=reply.remove_keyboard)

@user_private_router.message(or_f(Command('payment'),(F.text.lower() == "варианты оплаты")))
async def echo(message: types.Message):
    #await message.answer(message.text)
    await message.reply("Варианты оплаты", reply_markup=reply.remove_keyboard)

@user_private_router.message(or_f(Command('shipping'),(F.text.lower()=="варианты доставки")))
async def echo(message: types.Message):
    #await message.answer(message.text)
    await message.reply("Варианты доставки", reply_markup=reply.remove_keyboard)


#@user_private_router.message(F.text.lower().contains('варианты доставки'))
#async def echo(message: types.Message):
#    #await message.answer(message.text)
#    await message.reply(str("Это магический фильтр для любого вхождения вариантов доставки, в том числе " + message.text))


#Пробуем markdown
@user_private_router.message(F.text.lower()=='markdown')   
async def echo(message: types.Message):
    #await message.answer(message.text)
    await message.reply(str(f"*bold \*text* \n _italic \*text_ \n __underline__ \n ~strikethrough~ \n ||spoiler|| \n *bold _italic bold ~italic bold strikethrough ||italic bold strikethrough spoiler||~ __underline italic bold___ bold* \n [inline URL](http://www.example.com/) \n [inline mention of a user](tg://user?id={message.from_user.id}) \n  ![👍](tg://emoji?id=5368324170671202286)"), 
                        reply_markup=reply.remove_keyboard)


#Пробуем класс marked section
@user_private_router.message(F.text.lower()=='marked section')   
async def echo(message: types.Message):
    text = as_marked_section(
        Bold("Варианты оплаты"),
        "Картой в боте",
        "При получении карта/кеш",
        "В заведении",
        marker='✅ '
    )
    await message.answer(text.as_markdown())


@user_private_router.message(F.text)
async def echo(message: types.Message):
    #await message.answer(message.text)
    await message.answer(str("Это магический фильтр, " + message.text), reply_markup=reply.remove_keyboard)



