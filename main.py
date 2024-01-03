import telebot
from currency_converter import CurrencyConverter
from buttons import inline

bot = telebot.TeleBot('6440121870:AAGHtv7J_9M4G5EWSC7ZIZ9DmfWmkD1ehQE')
currency = CurrencyConverter()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, Введите сумму')
    bot.register_next_step_handler(message, summa)

def summa(message):
    global date
    try:
        date = int(message.text.strip())
        bot.send_message(message.chat.id, 'Выберите валюту', reply_markup = inline)
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибка, Впишите сумму')
        bot.register_next_step_handler(message, summa)
        return

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(date, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Получается {round(res, 2)}. Можете заново ввести сумму.')

        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.date.id, 'Введите валюту через слеш')
        bot.register_next_step_handler(call.message, my_currency)

def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(date, values[0], values[1])
        bot.send_message(message.chat.id, f'Получается {round(res, 2)}. Можете заново ввести сумму.')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Что-то пошло не так, попробуйте ввести заново')
        bot.register_next_step_handler(message, summa)

bot.polling(none_stop = True)
