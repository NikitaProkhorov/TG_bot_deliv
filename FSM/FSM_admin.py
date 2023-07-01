import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.filters.state import State, StatesGroup

from main import dp
from keyboard.kb_admin import MenuAdm
from handler.handler_delete import self_delete_message

class Form(StatesGroup):
    login = State()

#НАЧАЛО РАБОТЫ 
@dp.callback_query_handler(text_contains='Авторизация')
async def login(call: CallbackQuery):
     
     await Form.login.set()
     await call.message.edit_caption(caption=f'Введите пароль для авторизации:')

#ОТМЕНА
@dp.callback_query_handler(text_contains="Отмена", state='*')
@dp.message_handler(Text(equals='Отмена', ignore_case=True), state='*')
async def cancel_handler(call: CallbackQuery, state: FSMContext):

    current_state = await state.get_state()
    if current_state is None:
       return
    
    await call.message.delete()
    await state.finish()

#ПРОВЕРКА ПАРОЛЯ
@dp.message_handler(state=Form.login)
async def process_comment(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['pass'] = message.text
    
    photo = open('media/Фото2.jpg', 'rb')

    if data['pass'] == '12345':
        await message.answer_photo(photo=photo, caption="Привет, (имя)! Вы успешно авторизовались в панеле администратора!", reply_markup=MenuAdm)
        await state.finish()

    elif data['pass'] != '12345':
        msg = await message.answer("Неверный пароль, попробуйте снова:")
        asyncio.create_task(self_delete_message(msg, 2))
