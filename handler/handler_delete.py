import asyncio

from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound
from aiogram.utils import exceptions
from aiogram.types import Message
from contextlib import suppress
from aiogram import types
from main import bot


#УДАЛЕНИЕ СООБЩЕНИЙ
async def self_delete_message(message: types.Message, sleep_time):
    await asyncio.sleep(sleep_time)
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        bot.set_current(bot)
        await message.delete()


async def delete_last_three_messages(message: Message):
    try:
        last_messages = await bot.get_messages(chat_id=message.chat.id, limit=3)
        for msg in last_messages:
            await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
    except exceptions.BadRequest:
        pass  # обработка ошибки, если удаление сообщения невозможно