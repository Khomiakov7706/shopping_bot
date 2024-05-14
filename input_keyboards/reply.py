from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_keyboard(
        *btns: str,
        placeholder: str = None,
        request_contact: int = None,
        request_location: int = None,
        sizes: tuple[int] = (2,),):

        keyboard = ReplyKeyboardBuilder()
        
        for index, text in enumerate(btns, start=0):
             if request_contact and request_contact == index: keyboard.add(KeyboardButton(text=text, request_contact=True))
             elif request_location and request_location ==  index: keyboard.add(KeyboardButton(text=text, request_location=True))
             else: keyboard.add(KeyboardButton(text=text))
        return keyboard.adjust(*sizes).as_markup(
               resize_keyboard = True, 
               input_field_placeholder = placeholder)
'''
Parameters request_contact and request_location must be as indexes of btns args for buttons you need.

Example:

get_keyboard(
    "Меню",
    "О магазине"
    "Варианты оплаты"
    "Варианты доставки"
    "Отправить номер телефона" placeholder="Что вас интересует?",
    request_contact=4, 
    sizes=(2, 2, 1)
    )
'''
    



start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Меню"),
            KeyboardButton(text="О магазине"),
        ],                                                  # 1st string of buttons
        [
            KeyboardButton(text="Варианты доставки"),
            KeyboardButton(text="Варианты оплаты"),
        ]
    ],                                                  # 2nd string of buttons
    resize_keyboard=True,
    input_field_placeholder="Что вас интересует?"
)

remove_keyboard = ReplyKeyboardRemove()

start_kb2 = ReplyKeyboardBuilder() # ReplyKeyboardBuilder – второй способ задавать кнопки меню в телеграмм боте
start_kb2.add(
    KeyboardButton(text="Меню"),
    KeyboardButton(text="О магазине"),
    KeyboardButton(text="Варианты доставки"),
    KeyboardButton(text="Варианты оплаты")
)
start_kb2.adjust(2,1,1)            # 2 кнопки в первой строке, 1 кнопка во второй строке, 1 кнопка в третей строке


start_kb3 = ReplyKeyboardBuilder() # ReplyKeyboardBuilder – второй способ задавать кнопки меню в телеграмм боте
start_kb3.attach(start_kb2)
start_kb3.row(
    KeyboardButton(text="Оставить отзыв")
)


