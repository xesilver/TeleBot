from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from app import keyboards as kb
from app import DB as DB
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


async def on_startup(_):
    await DB.db_start()
    print('Bot started')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await DB.cmd_start_db(message.from_user.id)
    await message.answer_sticker("CAACAgIAAxkBAAEJOp5kfzuCDcYdc3PJ1mM1AmSWl50FdAACBh0AAooJiEqG207BPQXOGi8E")
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f"Welcome, {message.from_user.first_name}!", reply_markup=kb.main_admin)
    else:
        await message.answer(f"Welcome, admin", reply_markup=kb.main)


@dp.message_handler(text='catalogue')
async def catalogue(message: types.Message):
    await message.reply(f"There aren't any sneakers", reply_markup=kb.catalog_list)


@dp.message_handler(text='cart')
async def cart(message: types.Message):
    await message.reply(f"cart is empty")


@dp.message_handler(text='contacts')
async def contacts(message: types.Message):
    await message.reply(f"Buy sneakers {message.from_user.is_bot}")


@dp.message_handler(text='admin_panel')
async def admin_panel(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.reply(f"You have opened admin_panel", reply_markup=kb.admin_keyboard)
    else:
        await message.reply(f"Stop this")


@dp.message_handler(commands=['id'])
async def cmd_start(message: types.Message):
    await message.answer(message.from_user.id)


@dp.message_handler()
async def response(message: types.Message):
    await message.reply(f"Stop this")


@dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    if callback_query.data == "One":
        await bot.send_message(chat_id=callback_query.from_user.id, text="You picked one")
    elif callback_query.data == "Two":
        await bot.send_message(chat_id=callback_query.from_user.id, text="You picked two")
    elif callback_query.data == "Three":
        await bot.send_message(chat_id=callback_query.from_user.id, text="You picked three")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup,skip_updates=True)
