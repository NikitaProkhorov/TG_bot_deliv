import math
import asyncio
import sqlite3
import datetime

from main import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery, Message
from handler.handler_delete import self_delete_message
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard.kb_client import deliv, adres, time, hourse, min, pay, Bonus

class Form(StatesGroup):
    bonus = State()
    kolvo = State()
    dostavka = State() 
    comment = State()
    address = State()
    time = State()  
    hourse = State()
    min = State()
    pay = State()

#НАЧАЛО РАБОТЫ 
@dp.callback_query_handler(text_contains='Оформить заказ')
async def dev(call: CallbackQuery):
    now = datetime.datetime.now().time()
    start_time = datetime.time(0, 0)  # Время начала работы бота
    end_time = datetime.time(23, 59)  # Время окончания работы бота

    if start_time <= now <= end_time:
        connect = sqlite3.connect('bot.db')
        cursor = connect.cursor()
        cursor.execute("""DELETE FROM deliv WHERE user_id=(?)""", [call.from_user.id])
        cursor.execute("""DELETE FROM card WHERE user_id=(?) AND prod_id=(?)""", ((call.from_user.id), 'Бонусы'))
        bon = cursor.execute("""SELECT bonus FROM users WHERE user_id=(?)""", [call.from_user.id]).fetchone()[0]
        sum = cursor.execute("""SELECT SUM(price) FROM card WHERE user_id=(?)""", [call.from_user.id]).fetchone()[0]
        prod = cursor.execute("""SELECT prod_id, price, value FROM card WHERE user_id=(?)""", [call.from_user.id]).fetchall()

        card = []
        for i in prod:
            card.append(f"{i[0]} × {i[2]}шт = {i[1]}₽")
        res = ("\n├".join(map(str, card)))

        cursor.close()
        connect.commit()

        if card == []:
            msg = await bot.send_message(call.from_user.id, 'Добавьте хотя бы один товар!')
            asyncio.create_task(self_delete_message(msg, 2))
            
        elif card != []:
            await Form.bonus.set()
            await call.message.answer(f'🛒 <b>ВАШ ЗАКАЗ:</b>\n\n┌{res}\n│\n'
                                    f'└🛍 <b>ИТОГО:</b> {sum}₽\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                    f'🎁 <b>Доступно бонусов для списания:</b> {bon}\n'
                                    f'🎁 <b>Начислить:</b> {math.ceil(sum/100*5)}', reply_markup=Bonus)
    else:
        msg1 = await bot.send_message(call.from_user.id, 'Извините, я работаю только с 09:00 до 20:00.')
        asyncio.create_task(self_delete_message(msg1, 2))

#ОТМЕНА
@dp.callback_query_handler(text_contains="Отмена", state='*')
@dp.message_handler(Text(equals='Отмена', ignore_case=True), state='*')
async def cancel_handler(call: CallbackQuery, state: FSMContext):
    connect = sqlite3.connect('bot.db')
    cursor = connect.cursor()
    cursor.execute("""DELETE FROM deliv WHERE user_id=(?)""", [call.from_user.id])
    connect.commit()
    cursor.close()

    current_state = await state.get_state()
    if current_state is None:
       return
    
    await call.message.delete()
    await state.finish()

#БОНУС
@dp.callback_query_handler(state=Form.bonus)
async def process_bonus(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['bonus'] = call.data
        data['id'] = call.from_user.id

    connect = sqlite3.connect('bot.db')
    cursor = connect.cursor()

    sum = cursor.execute("""SELECT SUM(price) FROM card WHERE user_id=(?)""", [call.from_user.id]).fetchone()[0]
    bon1 = math.ceil(sum/100*5)
    bon = cursor.execute("""SELECT bonus FROM users WHERE user_id=(?)""", [call.from_user.id]).fetchone()[0]
    cursor.execute("""INSERT INTO deliv (user_id) VALUES (?)""", (data['id'],))

    if call.data == "Списать":
        await Form.kolvo.set()
        await call.message.edit_text('Отлично!\n\n'
                                    f'<b>Какое количество бонусов хотите списать?</b>\n'
                                    f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                    f'🎁 <b>Доступно бонусов для списания:</b> {bon}')

    elif call.data == "Начислить":
        cursor.execute("""UPDATE deliv SET kolvo=? WHERE user_id=?""", (bon1, call.from_user.id))
        await Form.dostavka.set()
        await call.message.edit_text('Супер!\n\n'
                                     '<b>Как хотите получить заказ?</b>', reply_markup=deliv)
    
    cursor.close()
    connect.commit()

# #КОЛИЧЕСТВО БОНУСОВ
@dp.message_handler(state=Form.kolvo)
async def process_kolvo(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['kolvo'] = message.text
    
    connect = sqlite3.connect('bot.db')
    cursor = connect.cursor()

    bon = cursor.execute("""SELECT bonus FROM users WHERE user_id=(?)""", [message.from_user.id]).fetchone()[0]

    if message.text.isdigit():
        if int(message.text) <= bon:
            cursor.execute("""UPDATE deliv SET kolvo=?WHERE user_id=?""", (data['kolvo'], message.from_user.id))
            await Form.dostavka.set()
            await message.answer('Отлично!\n\n'
                                '<b>Как хотите получить заказ?</b>', reply_markup=deliv)
        else:
            msg = await bot.send_message(message.from_user.id,'Вы превысили количество имеющихся бонусов!')
            asyncio.create_task(self_delete_message(msg, 2))    
    
    else:
        msg1 = await bot.send_message(message.from_user.id,"Пожалуйста, введите необходимое количество!")
        asyncio.create_task(self_delete_message(msg1, 2))

    cursor.close()
    connect.commit()

#ДОСТАВКА
@dp.callback_query_handler(state=Form.dostavka)
async def process_dostavka(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['dostavka'] = call.data

    if call.data == "Заберу Сам":
        await Form.comment.set()
        await call.message.edit_text("Можете оставить любой комментарий или пожелание к своему заказу:")

    elif call.data == "Доставка":
        await Form.comment.set()
        await call.message.edit_text("Обратите внимание!\n\nДоставка производится, только в пределах помещений:\n\n"
                                        "Мельникайте 106\nТРЦ 'Сити Молл'\nТРЦ 'Матрешка'\nЖК 'Айвазовский'\n\n"
                                        "Отправьте сообщение с названием офиса или описанием вашего местонахождения:\n")
        
#КОММЕНТАРИЙ
@dp.message_handler(state=Form.comment)
async def process_comment(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['comment'] = message.text

    await Form.address.set()
    await message.answer("Выберите кофейню, которая находится ближе всего:", reply_markup=adres)

#АДРЕС
@dp.callback_query_handler(state=Form.address)
async def process_address(call: CallbackQuery, state: FSMContext):
    
    async with state.proxy() as data:
        data['tochka'] = call.data
                         
    await Form.time.set()
    await call.message.edit_text("Когда заказ должен быть готов?", reply_markup=time)

#ВРЕМЯ
@dp.callback_query_handler(state=Form.time)
async def process_time(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
            data['vrem'] = call.data

    connect = sqlite3.connect('bot.db')
    cursor = connect.cursor()

    sum = cursor.execute("""SELECT SUM(price) FROM card WHERE user_id=(?)""", [call.from_user.id]).fetchone()[0]
    bon = cursor.execute("""SELECT kolvo FROM deliv WHERE user_id=(?)""", [call.from_user.id]).fetchone()[0]

    if call.data == "Как можно скорее":       
            prod = cursor.execute("""SELECT prod_id, price, value FROM card WHERE user_id=(?)""", [call.from_user.id]).fetchall()
            cursor.execute("""UPDATE deliv 
                      SET dostavka=?, address=?, time=?, comment=?, bon=?
                      WHERE user_id=?""", 
                      (data['dostavka'], data['tochka'],data['vrem'], data['comment'], data['bonus'], call.from_user.id))

            card = []
            for i in prod:
                card.append(f"{i[0]} × {i[2]}шт = {i[1]}₽")
            res = ("\n├".join(map(str, card)))

            if data['bonus'] == 'Списать':
                cursor.execute("""INSERT INTO card VALUES(?,?,?,?)""", ((call.from_user.id), 'Бонусы', (-bon), 1))
                await call.message.edit_text(
                        f"🛒 <b>ВАШ ЗАКАЗ:</b>\n\n┌{res}\n│\n"
                        f"└🛍 <b>ИТОГО:</b> {sum}₽ - {bon}₽ = {sum-bon}₽\n\n"
                        f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                        f"🚚 <b>ДАННЫЕ ДОСТАВКИ:</b>\n\n"
                        f"┌📦 <b>Способ получения:</b> {data['dostavka']}\n│\n"
                        f"├🎁 <b>Бонусы:</b> {data['bonus']}({bon})\n│\n"
                        f"├⏰ <b>Время:</b> {data['vrem']}\n│\n"
                        f"└📍 <b>Адрес:</b> {data['tochka']}", reply_markup=pay)
                await state.finish()

            elif data['bonus'] == 'Начислить':
                await call.message.edit_text(
                        f"🛒 <b>ВАШ ЗАКАЗ:</b>\n\n┌{res}\n│\n"
                        f"└🛍 <b>ИТОГО:</b> {sum}₽\n\n"
                        f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                        f"🚚 <b>ДАННЫЕ ДОСТАВКИ:</b>\n\n"
                        f"┌📦 <b>Способ получения:</b> {data['dostavka']}\n│\n"
                        f"├🎁 <b>Бонусы:</b> {data['bonus']}({bon})\n│\n"
                        f"├⏰ <b>Время:</b> {data['vrem']}\n│\n"
                        f"└📍 <b>Адрес:</b> {data['tochka']}", reply_markup=pay)
                await state.finish()

    elif call.data == "Указать время":
            if data['bonus'] == 'Списать':
                cursor.execute("""INSERT INTO card VALUES(?,?,?,?)""", ((call.from_user.id), 'Бонусы', (-bon), 1))
                await Form.hourse.set()
                await call.message.edit_text("Выберите час:", reply_markup=hourse)

            elif data['bonus'] == 'Начислить':
                await Form.hourse.set()
                await call.message.edit_text("Выберите час:", reply_markup=hourse)
    
    cursor.close()
    connect.commit()

#ЧАСЫ
@dp.callback_query_handler(state=Form.hourse)
async def process_hourse(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['hourse'] = call.data

    await call.message.edit_text("Выберите минуту:", reply_markup=min) 
    await Form.min.set()

#МИНУТЫ
@dp.callback_query_handler(state=Form.min)
async def process_min(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['min'] = call.data

    connect = sqlite3.connect('bot.db')
    cursor = connect.cursor()
     
    sum = cursor.execute("""SELECT SUM(price) FROM card WHERE user_id=(?)""", [call.from_user.id]).fetchone()[0]
    bon = cursor.execute("""SELECT kolvo FROM deliv WHERE user_id=(?)""", [call.from_user.id]).fetchone()[0]

    prod = cursor.execute("""SELECT prod_id, price, value FROM card WHERE user_id=(?)""", [call.from_user.id]).fetchall()
    cursor.execute("""UPDATE deliv 
                      SET dostavka=?, address=?, time=?, hours=?, min=?, comment=?, bon=?
                      WHERE user_id=?""", 
                      (data['dostavka'], data['tochka'],data['vrem'], data['hourse'], data['min'], data['comment'], data['bonus'], call.from_user.id))

    card = []
    for i in prod:
        card.append(f"{i[0]} × {i[2]}шт = {i[1]}₽")
    res = ("\n├".join(map(str, card)))

    cursor.close()
    connect.commit()
    
    if data['bonus'] == 'Списать':
        await call.message.edit_text(
                        f"🛒 <b>ВАШ ЗАКАЗ:</b>\n\n┌{res}\n│\n"
                        f"└🛍 <b>ИТОГО:</b> {sum}₽ - {bon}₽ = {sum-bon}₽\n\n"
                        f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                        f"🚚 <b>ДАННЫЕ ДОСТАВКИ:</b>\n\n"
                        f"┌📦 <b>Способ получения:</b> {data['dostavka']}\n│\n"
                        f"├🎁 <b>Бонусы:</b> {data['bonus']}({bon})\n│\n"
                        f"├⏰ <b>Время:</b> {data['hourse']}:{data['min']}\n│\n"
                        f"└📍 <b>Адрес:</b> {data['tochka']}", reply_markup=pay)
        await state.finish()
        
    elif data['bonus'] == 'Начислить':
        await call.message.edit_text(
                        f"🛒 <b>ВАШ ЗАКАЗ:</b>\n\n┌{res}\n│\n"
                        f"└🛍 <b>ИТОГО:</b> {sum}₽\n\n"
                        f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                        f"🚚 <b>ДАННЫЕ ДОСТАВКИ:</b>\n\n"
                        f"┌📦 <b>Способ получения:</b> {data['dostavka']}\n│\n"
                        f"├🎁 <b>Бонусы:</b> {data['bonus']}({bon})\n│\n"
                        f"├⏰ <b>Время:</b> {data['hourse']}:{data['min']}\n│\n"
                        f"└📍 <b>Адрес:</b> {data['tochka']}", reply_markup=pay)
        await state.finish()


