from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Выбери урок из меню ниже", reply_markup=menu)


@dp.message_handler(Text(equals=["Урок 1","Урок 2","Урок 3","Урок 4","Урок 5","Урок 6","Урок 7","Урок 8","Урок 9","Урок 10","Урок 11","Урок 12","Урок 13","Урок 14","Урок 15","Урок 16",]))
async def get_food(message: Message):
    await message.answer(f"Вы выбрали {message.text}. Спасибо", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=['Урок 17']))
async def get_food(message: Message):
    await message.answer("Дружище, ты дошел уже до последнего урока , я очень рад что тебе нравится наш курс , так как ты заинтересован в обучении мы предлагаем тебе скидку на базовый и бизнес курс !!!", reply_markup=ReplyKeyboardRemove())