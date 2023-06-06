from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardMarkup
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('catalogue').add('cart').add('contacts')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('catalogue').add('cart').add('contacts').add('admin_panel')

admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
admin_keyboard.add('add product').add('del product').add('distribution')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker("CAACAgIAAxkBAAEJOp5kfzuCDcYdc3PJ1mM1AmSWl50FdAACBh0AAooJiEqG207BPQXOGi8E")
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f"sss", reply_markup=main_admin)
    else:
        await message.answer(f"", reply_markup=main)


@dp.message_handler(text='catalogue')
async def catalogue(message: types.Message):
    await message.reply(f"There aren't any sneakers")


@dp.message_handler(text='cart')
async def cart(message: types.Message):
    await message.reply(f"cart is empty")


@dp.message_handler(text='contacts')
async def contacts(message: types.Message):
    await message.reply(f"Buy sneakers beach")


@dp.message_handler(text='admin_panel')
async def admin_panel(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.reply(f"You have opened admin_panel", reply_markup=admin_keyboard)
    else:
        await message.reply(f"Stop this")



@dp.message_handler(commands=['id'])
async def cmd_start(message: types.Message):
    await message.answer(message.from_user.id)


@dp.message_handler()
async def response(message: types.Message):
    await message.reply(f"Stop this")


if __name__ == '__main__':
    executor.start_polling(dp)
