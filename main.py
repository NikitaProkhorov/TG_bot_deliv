import os
import asyncio

from Sql import db_start
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv()

loop    = asyncio.new_event_loop()
bot     = Bot(token=os.environ.get('BOT_TOKEN'), parse_mode='HTML')
storage = MemoryStorage()
dp      = Dispatcher(bot, loop=loop, storage=storage)

async def on_startup(_):
     await db_start()

if __name__ == '__main__':

    from handler.handler_start import dp
    from handler.handler_pay import dp
    from handler.handler_admin import dp
    from handler.handler_count import dp
    from handler.handler_process import dp
    from FSM.FSM_deliv import dp
    from FSM.FSM_admin import dp
#     from sklearn.skl import dp
    
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

