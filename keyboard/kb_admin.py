from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters import Command

StartAdm = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Авторизация', callback_data='Авторизация')
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='Отмена')
        ]
    ]
)

MenuAdm = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Статистика заказов', callback_data='Статистика заказов')
        ],
        [
            InlineKeyboardButton(text='Добавить товар', callback_data='Добавить товар')
        ],
        [
            InlineKeyboardButton(text='Выход', callback_data='Выход')
        ]
    ]
)

Stat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Всего заказов', callback_data='Всего заказов')
        ],
        [
            InlineKeyboardButton(text='Заказы за последний день', callback_data='Заказы за последний день')
        ],
        [
            InlineKeyboardButton(text='Заказы за последний месяц', callback_data='Заказы за последний месяц')
        ],
        [
            InlineKeyboardButton(text='◀ Назад', callback_data='Back')
        ]
    ]
)