from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('catalogue').add('cart').add('contacts')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('catalogue').add('cart').add('contacts').add('admin_panel')

admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
admin_keyboard.add('add product').add('del product').add('distribution')

catalog_list = InlineKeyboardMarkup(row_width=2)
catalog_list.add(InlineKeyboardButton(text="one", callback_data="One"),
                 InlineKeyboardButton(text="two", callback_data="Two"),
                 InlineKeyboardButton(text="three", callback_data="Three"))
