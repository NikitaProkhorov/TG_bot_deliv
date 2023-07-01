import sqlite3
import asyncio

from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from main import dp, bot
from keyboard.kb_client import cb, Menu
from aiogram import types
from contextlib import suppress
from aiogram.utils.exceptions import MessageNotModified
from handler.handler_delete import self_delete_message

callback_numbers = CallbackData("fabnum", "action", "prod_id", "price")
 
user_data = {}

def get_keyboard_fab(prod_id, price):
    buttons = [
        types.InlineKeyboardButton(text="-1", callback_data=callback_numbers.new(action="decr", prod_id=prod_id, price=price)),
        types.InlineKeyboardButton(text="+1", callback_data=callback_numbers.new(action="incr", prod_id=prod_id, price=price)),
        InlineKeyboardButton(text='◀ Назад', callback_data='Назад'),
        types.InlineKeyboardButton(text="Подтвердить", callback_data=callback_numbers.new(action="finish", prod_id=prod_id, price=price))
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard
 
#ОБНОВЛЕНИЕ ТЕКСТА
async def update_num_text_fab(message: types.Message, new_value: int, prod_id, price):
    with suppress(MessageNotModified):
        await message.edit_caption(caption=f"Укажите количество: {new_value}", reply_markup=get_keyboard_fab(prod_id, price))
 
#НАЖАТИЕ КНОПКИ
@dp.callback_query_handler(cb.filter(prod_id='Флэт Уайт'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Капучино'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Латте'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Мокко'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Американо'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Раф Пряная Тыква'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Раф Сникерс'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Раф Орео'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Раф Халва'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Раф Арахисовый'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Раф Цитрусовый'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Раф Ванильный'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Брусничный Каркаде'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Фруктово-Ягодный Пунш'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Имбирный Пуэр'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Матча'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Глинтвейн'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Облепиха-Маракуйя'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Листовой Чай'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Аффогато'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Молочный Коктейль'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Бамбл Кофе'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Сливочный Щербет'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Апельсиновый'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))

@dp.callback_query_handler(cb.filter(prod_id='Яблочный'))
async def klas(call: CallbackQuery, callback_data: dict):
    price = callback_data.get('price')
    prod_id = callback_data.get('prod_id')
    user_data[call.from_user.id] = 1
    await call.message.edit_caption(caption=f"Укажите количество: 1", reply_markup=get_keyboard_fab(prod_id, price))
 
 
#СЧЕТЧИК
@dp.callback_query_handler(callback_numbers.filter(action=["incr", "decr"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    user_value = user_data.get(call.from_user.id, 0)
    action = callback_data["action"]
    prod_id = callback_data['prod_id']
    price = callback_data['price']
 
    if action == "incr":
        user_data[call.from_user.id] = user_value + 1
        await update_num_text_fab(call.message, user_value + 1, prod_id, price)
 
    elif action == "decr":
        if user_value == 0:
            user_data[call.from_user.id] = user_value
            await update_num_text_fab(call.message, user_value, prod_id, price)
 
        elif user_value != 0:
            user_data[call.from_user.id] = user_value - 1
            await update_num_text_fab(call.message, user_value - 1, prod_id, price)
 
    await call.answer()
 
#ПОДТВЕРДИТЬ
@dp.callback_query_handler(callback_numbers.filter(action=["finish"]))
async def callbacks_num_finish_fab(call: types.CallbackQuery, callback_data: dict):
    user_value = user_data.get(call.from_user.id, 0)
 
    if user_value == 0:
        msg1 = await bot.send_message(call.from_user.id, 'Нажмите (+1), чтобы добавить')
        asyncio.create_task(self_delete_message(msg1, 2))
 
    elif user_value != 0:
        await call.answer(cache_time=2)
            
        price   = callback_data.get('price')
        prod_id = callback_data.get('prod_id')
        user_id = call.message.chat.id
        value_price = int(price) * user_value

        db = sqlite3.connect('bot.db')
        cursor = db.cursor()
        cursor.execute("""INSERT INTO card (user_id, prod_id, price, value) VALUES (?, ?, ?, ?)""", [user_id, prod_id, value_price, user_value])
        cursor.close()
        db.commit()
        db.close()
 
        msg2 = await bot.send_message(call.from_user.id, 'Товар добавлен в корзину!')
        asyncio.create_task(self_delete_message(msg2, 2))
 
        await call.message.edit_caption(caption=f"Выбери понравившийся кофе:", reply_markup=Menu)