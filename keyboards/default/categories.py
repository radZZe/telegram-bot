from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

categories = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Лайт"),
            KeyboardButton(text="Базовый"),
            KeyboardButton(text="Бизнес"),
        ],
    ],
    resize_keyboard=True
)