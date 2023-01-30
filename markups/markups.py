from aiogram import types

# main menu markup
main_menu_markup = types.reply_keyboard.ReplyKeyboardMarkup(row_width=2)
btn1 = types.KeyboardButton('Погода в моём городе')
btn2 = types.KeyboardButton('Погода в другом месте')
btn3 = types.KeyboardButton('История')
btn4 = types.KeyboardButton('Установить свой город')
main_menu_markup.add(btn1, btn2, btn3, btn4)

# admin menu
admin_menu_markup = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Список пользователей')
admin_menu_markup.add(btn1)