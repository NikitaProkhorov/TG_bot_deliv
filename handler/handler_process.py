import aiogram
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from main import dp, bot
from handler.handler_pay import button_user_map
    

# Обработчик нажатий кнопок
@dp.callback_query_handler(lambda query: query.data == "Принят в работу")
async def handle_callback(callback_query: types.CallbackQuery):
    # Получаем ID пользователя из словаря button_user_map
    user_id = button_user_map.get(callback_query.data)
    
    if user_id:
        # Отправляем сообщение пользователю с использованием ID пользователя
        await bot.send_message(user_id, "Ваш заказ принят в работу сотрудником Monolyte Coffee!")

# Обработчик нажатий кнопок
@dp.callback_query_handler(lambda query: query.data == "Готов")
async def handle_callback(callback_query: types.CallbackQuery):
    # Получаем ID пользователя из словаря button_user_map
    user_id = button_user_map.get(callback_query.data)
    
    if user_id:
        # Отправляем сообщение пользователю с использованием ID пользователя
        await bot.send_message(user_id, "Ваш заказ готов к получению!")