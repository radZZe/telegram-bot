from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import categories, menu
from loader import dp


@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await message.answer("Привет у нас в наличии доступно 3 курса \n1️⃣Лайт - сделан для новичков и он бесплатный \n2️⃣Базовый - для более продвинутых и стоит он 2000 руб \n3️⃣Бизнес - для тех кто собирается зарабатывать на телеграмме и стоит он 30000 руб \nКакой выбираешь?🤔", reply_markup=categories)


@dp.message_handler(Text(equals=['Лайт']))
async def get_food(message: Message):
    await message.answer(f"Ты выбрал {message.text}. и уже можешь приступить к обучению", reply_markup=menu)

@dp.message_handler(Text(equals=['Базовый','Бизнес']))
async def get_food(message: Message):
    await message.answer("Эти курсы на оплату пока стоит заглушка", reply_markup=ReplyKeyboardRemove())