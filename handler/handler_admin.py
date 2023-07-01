import logging
import time
import random
import sqlite3

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command

from keyboard.kb_admin import StartAdm, Stat, MenuAdm
from main import dp

#СТАРТ
@dp.message_handler(Command('MonolyteAdmin'))
async def start_adm(message: Message):
    photo = open('media/Фото2.jpg', 'rb')

    await message.answer_photo(photo=photo, caption=f'ПАНЕЛЬ АДМИНИСТРАТОРА', reply_markup=StartAdm)

#КНОПКИ
@dp.callback_query_handler(text_contains='Back')
async def back_hand(call: CallbackQuery):
    
     await call.message.edit_caption(caption=f'Выбери нужную категорию из списка:', reply_markup=MenuAdm)

@dp.callback_query_handler(text_contains='Выход')
async def back_hand(call: CallbackQuery):
    
     await call.message.delete()

@dp.callback_query_handler(text_contains='Статистика заказов')
async def proch(call: CallbackQuery):
    
     await call.message.edit_caption(caption=f'Здесь вы можете посмотреть количество оплаченных заказов у бота!', reply_markup=Stat)

@dp.callback_query_handler(text_contains='Всего заказов')
async def proch(call: CallbackQuery):
     connect = sqlite3.connect('bot.db')
     cursor = connect.cursor()
     count = cursor.execute("SELECT COUNT (*) FROM classific").fetchone()[0]
     sum = cursor.execute("SELECT SUM(price) FROM classific").fetchone()[0]

     connect.commit()
     cursor.close()
     
     await call.message.edit_caption(caption=f'Всего онлайн заказов: {count}\n'
                                     f'На сумму: {sum}', reply_markup=Stat)
     
@dp.callback_query_handler(text_contains='Заказы за последний день')
async def proch(call: CallbackQuery):
     connect = sqlite3.connect('bot.db')
     cursor = connect.cursor()
     cursor.execute("""  """)

     connect.commit()
     cursor.close()
     
     await call.message.edit_caption(caption=f'', reply_markup=Stat)
