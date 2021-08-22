from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Урок 1"),
            KeyboardButton(text="Урок 2"),
            KeyboardButton(text="Урок 3"),
            KeyboardButton(text="Урок 4"),
        ],
        [
            KeyboardButton(text="Урок 5"),
            KeyboardButton(text="Урок 6"),
            KeyboardButton(text="Урок 7"),
            KeyboardButton(text="Урок 8"),
        ],
        [
            KeyboardButton(text="Урок 9"),
            KeyboardButton(text="Урок 10"),
            KeyboardButton(text="Урок 11"),
            KeyboardButton(text="Урок 12"),
        ],
        [
            KeyboardButton(text="Урок 13"),
            KeyboardButton(text="Урок 14"),
            KeyboardButton(text="Урок 15"),
            KeyboardButton(text="Урок 16"),
            KeyboardButton(text="Урок 17"),
        ],

    ],
    resize_keyboard=True
)