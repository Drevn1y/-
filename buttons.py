from telebot import types

inline = types.InlineKeyboardMarkup(row_width=2)
btn1 = types.InlineKeyboardButton('USD/EURO', callback_data='usd/eur')
btn2 = types.InlineKeyboardButton('EURO/USD', callback_data='eur/usd')
btn3 = types.InlineKeyboardButton('USD/RUB', callback_data='usd/rub')
btn4 = types.InlineKeyboardButton('RUB/USD', callback_data='rub/usd')
btn5 = types.InlineKeyboardButton('RUB/EURO', callback_data='rub/eur')
btn6 = types.InlineKeyboardButton('EURO/RUB', callback_data='eur/rub')
btn7 = types.InlineKeyboardButton('Другое', callback_data='else')

inline.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)