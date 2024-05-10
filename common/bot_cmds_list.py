from aiogram.types import BotCommand

private_chat_commands = [
    BotCommand(command='menu', description="Посмотреть меню"),
    BotCommand(command='about', description="О нас"),
    BotCommand(command='payment', description="Варианты оплаты"),
    BotCommand(command='shipping', description="Варианты доставки")

]