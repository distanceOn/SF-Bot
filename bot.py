import telebot
from config import TOKEN
from extensions import Converter, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help_message(message):
    text = 'Для получения цены на валюту отправьте сообщение в формате: \n' \
           '<имя валюты цену которой он хочет узнать> <имя валюты в которой надо узнать цену первой валюты> <количество первой валюты>. \n' \
           'Например: USD RUB 100\n' \
           'Для получения списка доступных валют отправьте команду /values'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values_message(message):
    text = 'Доступные валюты:\n' \
           'доллар (USD),\n' \
           'евро (EUR),\n' \
           'рубль (RUB).'
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def convert_message(message):
    try:
        base, quote, amount = message.text.split(' ')
        result = Converter.get_price(base.upper(), quote.upper(), amount)
    except APIException as e:
        bot.send_message(message.chat.id, f'Ошибка: {e}')
    else:
        text = f'{amount} {base.upper()} = {result} {quote.upper()}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
