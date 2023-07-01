# # import matplotlib
# # import datetime
# # import numpy as np
# # import pandas as pd
# # from matplotlib import colors
# # import matplotlib.pyplot as plt
# # import matplotlib.pyplot as plt, numpy as np
# # import sys
# # import warnings
# # import pandas as pd
# # import sqlite3
# # import aiogram
# # from aiogram.types import Message, CallbackQuery
# # from main import dp

# # @dp.callback_query_handler(text_contains='X')
# # async def skl_hand(call: CallbackQuery):

# #     con = sqlite3.connect("bot.db")
# #     df = pd.read_sql_query("SELECT * FROM classific", con)
# #     print(df.head())

# #     # skl = []
# #     # for i in df:
# #     #     skl.append(f"{i[0]} — {i[1]} — {i[2]}")
# #     # res = ("\n    ".join(map(str, skl)))
    
# #     con.close()
# #     await call.message.answer(f'Заказы: \n\n{df}')


# # # # Read sqlite query results into a pandas DataFrame
# # # con = sqlite3.connect("bot.db")
# # # df = pd.read_sql_query("SELECT * FROM classific", con)

# # # # Verify that result of SQL query is stored in the dataframe
# # # print(df.head())


# # # con.close()


# # import sqlite3
# # import pandas as pd
# # from sklearn.cluster import KMeans

# # # Подключаемся к базе данных SQLite
# # conn = sqlite3.connect('bot.db')

# # # Получаем данные из таблицы в виде DataFrame
# # df = pd.read_sql_query("SELECT user_id, prod_id, value FROM classific", conn)

# # # Группируем данные по пользователю и товару, чтобы получить количество каждого товара, купленного каждым пользователем
# # grouped_df = df.groupby(['user_id', 'prod_id'])['value'].sum().unstack().fillna(0)

# # # Используем KMeans для кластеризации данных
# # kmeans = KMeans(n_clusters=3).fit(grouped_df)

# # # Получаем метки кластеров
# # labels = kmeans.labels_

# # # Выводим метки кластеров для каждого пользователя
# # for i, label in enumerate(labels):
# #     print(f"User {i+1} belongs to cluster {label}")




# # ____________________________________________________________________________________#
# # import sqlite3
# # import pandas as pd
# # from sklearn.preprocessing import StandardScaler
# # from sklearn.cluster import KMeans
# # import matplotlib.pyplot as plt

# # # Подключение к базе данных SQLite
# # conn = sqlite3.connect('mydatabase.db')
# # cursor = conn.cursor()

# # # Запрос на получение данных из таблицы
# # cursor.execute("SELECT user_id, prod_id, value FROM classific")
# # data = cursor.fetchall()

# # # Создание DataFrame из полученных данных
# # df = pd.DataFrame(data, columns=['user_id', 'prod_id', 'value'])

# # # Создание таблицы сводных данных (pivot table)
# # pivot_table = pd.pivot_table(df, values='value', index=['user_id'], columns=['prod_id'], fill_value=0)

# # # Применение стандартизации к данным
# # scaler = StandardScaler()
# # scaled_data = scaler.fit_transform(pivot_table)

# # # Определение оптимального количества кластеров методом "локтя" (Elbow Method)
# # sse = []
# # for k in range(1, 11):
# #     kmeans = KMeans(n_clusters=k, random_state=0)
# #     kmeans.fit(scaled_data)
# #     sse.append(kmeans.inertia_)
# # plt.plot(range(1, 11), sse)
# # plt.xlabel('Количество кластеров')
# # plt.ylabel('SSE')
# # plt.show()

# # # Создание объекта KMeans с оптимальным количеством кластеров
# # kmeans = KMeans(n_clusters=4, random_state=0)

# # # Применение кластеризации к данным
# # clusters = kmeans.fit_predict(scaled_data)

# # # Добавление столбца с номерами кластеров в таблицу сводных данных
# # pivot_table['cluster'] = clusters

# # # Вывод результатов кластеризации
# # print(pivot_table)



# # import sqlite3
# # from sklearn.cluster import KMeans
# # import numpy as np
# # import pandas as pd
# # from aiogram import Bot, Dispatcher, types
# # from aiogram.types import CallbackQuery
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# # from aiogram.utils import executor

# # Start = InlineKeyboardMarkup(
# #     inline_keyboard=[
# #         [
# #             InlineKeyboardButton(text='Профиль 👤', callback_data='Профиль')
# #         ],
# #         [
# #             InlineKeyboardButton(text='Меню 📄', callback_data='Меню')
# #         ],
# #         [
# #             InlineKeyboardButton(text='Корзина 🗑', callback_data='Корзина')
# #         ],
# #         [
# #             InlineKeyboardButton(text='Помощь 🛠', callback_data='Помощь')
# #         ],
# #         [
# #             InlineKeyboardButton(text='Наш сайт 💻', url='http://monolyte.tilda.ws/')
# #         ],
# #         [
# #             InlineKeyboardButton(text='Рассказать анекдот 💭', callback_data='Рассказать анекдот')
# #         ]
# #     ]
# # )

# # # Подключаемся к базе данных SQLite
# # conn = sqlite3.connect('bot.db')

# # # Определяем переменные для бота и диспетчера
# # bot = Bot(token='5441561569:AAGVI_7jAklHrEUF95QJKBj8ME5o9TNeBvY')
# # dp = Dispatcher(bot)

# # # Определяем функцию для кластеризации данных из таблицы
# # def cluster_data():
# #     # Загружаем данные из таблицы в DataFrame
# #     df = pd.read_sql_query('SELECT user_id, prod_id, value FROM classific', conn)
# #     # Группируем данные по пользователям и суммируем количество товаров
# #     df = df.groupby(['user_id', 'prod_id']).sum().reset_index()
# #     # Трансформируем данные в матрицу для использования алгоритма KMeans
# #     X = df.pivot(index='user_id', columns='prod_id', values='value').fillna(0)
# #     X = np.array(X)
# #     # Применяем алгоритм KMeans для кластеризации данных
# #     kmeans = KMeans(n_clusters=3)
# #     kmeans.fit(X)
# #     labels = kmeans.predict(X)
# #     # Возвращаем метки кластеров
# #     return labels

# # # Определяем хэндлер для команды /start
# # @dp.message_handler(commands=['start'])
# # async def process_start_command(message: types.Message):
# #     # Отправляем приветственное сообщение с кнопкой
# #     await bot.send_message(chat_id=message.from_user.id, text="Привет! Нажми на кнопку для теста.", reply_markup=Start)

# # # Определяем хэндлер для обработки кнопки с calldata='test'
# # @dp.callback_query_handler(text_contains='Меню')
# # async def process_test_callback(call: CallbackQuery):
# #     # Вызываем функцию для кластеризации данных
# #     labels = cluster_data()
# #     # Отправляем сообщение с результатами кластеризации
# #     message_text = f"Результаты кластеризации:\nКластер 0: {labels(0)} пользователей\nКластер 1: {labels(1)} пользователей\nКластер 2: {labels(2)} пользователей"
# #     await bot.send_message(chat_id=call.from_user.id, text=message_text)

# # # Запускаем бота
# # if __name__ == '__main__':
# #     executor.start_polling(dp)




# import sqlite3
# from sklearn.cluster import KMeans
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import CallbackQuery
# from aiogram.utils import executor
# from aiogram.dispatcher.filters import Command

# # Подключаемся к базе данных SQLite
# conn = sqlite3.connect('bot.db')
# cursor = conn.cursor()

# # Создаем объект бота и диспетчера
# bot = Bot(token='5441561569:AAGVI_7jAklHrEUF95QJKBj8ME5o9TNeBvY')
# dp = Dispatcher(bot)

# Start = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Профиль 👤', callback_data='Профиль')
#         ],
#         [
#             InlineKeyboardButton(text='Меню 📄', callback_data='Меню')
#         ],
#         [
#             InlineKeyboardButton(text='Корзина 🗑', callback_data='Корзина')
#         ],
#         [
#             InlineKeyboardButton(text='Помощь 🛠', callback_data='Помощь')
#         ],
#         [
#             InlineKeyboardButton(text='Наш сайт 💻', url='http://monolyte.tilda.ws/')
#         ],
#         [
#             InlineKeyboardButton(text='Рассказать анекдот 💭', callback_data='Рассказать анекдот')
#         ]
#     ]
# )

# # Определяем хэндлер для команды /start
# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     # Отправляем приветственное сообщение с кнопкой
#     await bot.send_message(chat_id=message.from_user.id, text="Привет! Нажми на кнопку для теста.", reply_markup=Start)

# # Обработчик кнопки с calldata='test'
# @dp.callback_query_handler(text_contains='Меню')
# async def back_hand(call: CallbackQuery):
#     # Получаем данные из базы данных SQLite
#     cursor.execute("SELECT user_id, prod_id, value FROM classific")
#     rows = cursor.fetchall()

#     # Формируем список покупок для каждого пользователя
#     user_purchases = {}
#     for row in rows:
#         user_id = row[0]
#         prod_id = row[1]
#         value = row[2]

#         if user_id not in user_purchases:
#             user_purchases[user_id] = {}

#         user_purchases[user_id][prod_id] = value

#     # Формируем список товаров и матрицу покупок
#     products = set()
#     user_matrix = []
#     for user_id, purchases in user_purchases.items():
#         user_row = []
#         for prod_id in products:
#             if prod_id in purchases:
#                 user_row.append(purchases[prod_id])
#             else:
#                 user_row.append(0)

#         for prod_id in purchases:
#             products.add(prod_id)
#             user_row.append(purchases[prod_id])

#         user_matrix.append(user_row)

#     # Кластеризуем пользователей по товарам
#     kmeans = KMeans(n_clusters=3, random_state=0).fit(user_matrix)
#     labels = kmeans.labels_

#     # Выводим результаты кластеризации
#     for user_id, label in zip(user_purchases.keys(), str(labels)):
#         await bot.send_message(call.from_user.id, f"Пользователь {user_id} отнесен к группе {label}")

#     # Закрываем соединение с базой данных
#     cursor.close()
#     conn.close()


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)

