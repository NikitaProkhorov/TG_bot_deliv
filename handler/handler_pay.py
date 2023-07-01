import sqlite3
import asyncio
import datetime
import os

from main import dp, bot
from aiogram import types
from dotenv import load_dotenv
from keyboard.kb_client import Card
from handler.handler_delete import self_delete_message
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery, ContentType


load_dotenv()
button_user_map = {}

#ОПЛАТА
@dp.callback_query_handler(text_contains='Оплатить')
async def buy(call: CallbackQuery):
     connect = sqlite3.connect('bot.db')
     cursor = connect.cursor()
     data = cursor.execute("""SELECT user_id, prod_id, price FROM card WHERE user_id=(?)""", [call.from_user.id]).fetchall()
     cursor.close()
     connect.commit()
     cursor = connect.cursor()
     new_data = []
     for i in range(len(data)):
          new_data.append(cursor.execute("""SELECT * FROM card WHERE prod_id=(?)""", [data[i][1]]).fetchall())
     cursor.close()
     connect.commit()
     connect.close
     new_data = [new_data[i][0] for i in range(len(new_data))]
     price = [LabeledPrice(label=i[1], amount=i[2]*100) for i in new_data]

     if price == []:
          msg = await bot.send_message(call.from_user.id, 'Добавьте хотя бы один товар!')
          asyncio.create_task(self_delete_message(msg, 2))
     
     elif price != []:
          await bot.send_invoice(call.from_user.id,
               title='Monolyte / Оплата', 
               description='Нажмите кнопку "Заплатить", чтобы подтвердить оплату',
               provider_token=os.environ.get('PAY_TOKEN_MASTER'),
               currency='rub',
               max_tip_amount = 100000,
               suggested_tip_amounts = [5000, 10000, 20000, 30000],
               need_email=True,
               need_phone_number=True,
               prices=price, 
               start_parameter='example', 
               payload='some_invoice')
     

@dp.pre_checkout_query_handler(lambda q: True)
async def checkout_process(pre_checkout_query: PreCheckoutQuery):
     await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def pay(message: Message):
     connect = sqlite3.connect('bot.db')
     cursor = connect.cursor()
     
     #CОЗДАНИЕ КНОПОК ДЛЯ СОТРУДНИКОВ
     Process = types.InlineKeyboardMarkup(row_width=2)
     user_id = message.from_user.id
     button1 = types.InlineKeyboardButton("Принят в работу", callback_data="Принят в работу", one_time=True)
     button2 = types.InlineKeyboardButton("Готов", callback_data="Готов", one_time=True)
     Process.add(button1, button2)
    
     button_user_map[button1.callback_data] = user_id
     button_user_map[button2.callback_data] = user_id


     #ДОБАВЛЕНИЕ ДАННЫХ В ТАБЛИЦУ classific
     cursor.execute(""" SELECT user_id, prod_id, value, price 
                         FROM card 
                         WHERE user_id=(?)""", [message.chat.id])
     rows = cursor.fetchall()

     for row in rows:
          user_id, prod_id, value, price = row
          current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          cursor.execute('''INSERT INTO classific (user_id, prod_id, value, price, data)
                              VALUES (?, ?, ?, ?, ?)''', (user_id, prod_id, value, price, current_time))
     
     #ОТПРАВКА ЧЕКА В РАБ.ГРУППУ
     user_id = message.from_user.url
     user_name = message.chat.first_name
     sum = cursor.execute("""SELECT SUM(price) FROM card WHERE user_id=(?)""", [message.chat.id]).fetchone()[0]
     prod = cursor.execute("""SELECT prod_id, price, value FROM card WHERE user_id=(?)""", [message.chat.id]).fetchall()
     deliv = cursor.execute("""SELECT * FROM deliv WHERE user_id=(?)""", [message.chat.id]).fetchall()
     bon = cursor.execute("""SELECT bon FROM deliv WHERE user_id=(?)""", [message.chat.id]).fetchone()[0]
     address = cursor.execute("""SELECT address FROM deliv WHERE user_id=(?)""", [message.chat.id]).fetchone()[0]

     c = []
     for i in prod:
          c.append(f"{i[0]} × {i[2]}шт = {i[1]}₽")
     res = ("\n├".join(map(str, c)))

     d = []
     for i in deliv:
          d.append(
               f"┌#️⃣ <b>Заказ пользователя:</b>\n├{user_id} - {user_name}\n│\n"
               f"└🛍 <b>ИТОГО:</b> {sum}₽\n\n"
               f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
               f"🚚 <b>ДАННЫЕ ДОСТАВКИ:</b>\n\n"
               f"┌🛒<b>Заказ:</b>\n├{res}\n│\n"
               f"├📦<b>Способ получения:</b> {i[1]}\n│\n"
               f"├📍<b>Кофейня:</b> {i[2]}\n│\n"
               f"├📪<b>Доставка:</b> {i[3]}\n│\n"
               f"├⏰<b>Время:</b> {i[4]}:{i[5]}\n│\n"
               f"└💬<b>Комментарий:</b> {i[6]}")
     r = ("".join(map(str, d)))
     
     match bon:
          case 'Списать':
               bonus = cursor.execute("""SELECT bonus-kolvo FROM users, deliv WHERE users.user_id=(?) AND deliv.user_id=(?)""", (message.chat.id, message.chat.id))
               bon = bonus.fetchone()[0]
               cursor.execute("""UPDATE users SET bonus=? WHERE user_id=?""", (int(bon), message.chat.id))

          case 'Начислить':
               bonus = cursor.execute("""SELECT bonus+kolvo FROM users, deliv WHERE users.user_id=(?) AND deliv.user_id=(?)""", (message.chat.id, message.chat.id))
               bon = bonus.fetchone()[0]
               cursor.execute("""UPDATE users SET bonus=? WHERE user_id=?""", (int(bon), message.chat.id))

     match address:
          case 'Мельникайте 106':
               await bot.send_message(os.environ.get('CHAT_ID_MELNIK'), text=f'{r}', reply_markup=Process)
          case 'ТРЦ "Сити Молл"':
               await bot.send_message(os.environ.get('CHAT_ID_CITY_MOLL'), text=f'{r}', reply_markup=Process)
          case 'ТРЦ "Матрешка"':
               await bot.send_message(os.environ.get('CHAT_ID_MATRESHKA'), text=f'{r}', reply_markup=Process)
          case 'ЖК "Айвазовский"':
               await bot.send_message(os.environ.get('CHAT_ID_AIVA'), text=f'{r}', reply_markup=Process)
               
     cursor.execute("""DELETE FROM card WHERE user_id=(?)""", [message.chat.id])
     cursor.close()
     connect.commit()
     connect.close()


#ПРОСМОТР КОРЗИНЫ
@dp.callback_query_handler(text_contains='Просмотреть Корзину')
async def card(call: CallbackQuery):
     connect = sqlite3.connect('bot.db')
     cursor = connect.cursor()

     cursor.execute("""DELETE FROM card WHERE user_id=(?) AND prod_id=(?)""", ((call.from_user.id), 'Бонусы'))
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
          await call.message.edit_caption(caption=f'🛒 <b>ВАША КОРЗИНА:</b>\n\n'
                                                  f'┌{res}\n│\n└🛍 <b>ИТОГО:</b> {sum}₽', reply_markup=Card)

#ОЧИСТКА КОРЗИНЫ
@dp.callback_query_handler(text_contains='Очистить Корзину')
async def clear(call: CallbackQuery):
     connect = sqlite3.connect('bot.db')
     cursor = connect.cursor()
     cursor.execute("""DELETE FROM card WHERE user_id=(?)""", [call.from_user.id])
     cursor.close()
     connect.commit()
     connect.close()

     await call.message.edit_caption(caption=f'Здесь вы можете просмотреть свои товары в корзине и оплатить их!' 
     '\n\nА также просмотореть свои заказы за всё время', reply_markup=Card)
     
     msg = await bot.send_message(call.from_user.id, 'Ваша корзина успешно очищена!')
     asyncio.create_task(self_delete_message(msg, 2))
