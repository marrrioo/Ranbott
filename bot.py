import telebot
import random
from telebot import types


bot = telebot.TeleBot('6063526768:AAG6RdFcaw5zxDHJur268irTn42vSn5rqms')

link = ['http://www.republiquedesmangues.fr/', 'https://puginarug.com/', 'http://www.koalastothemax.com/',
        'https://cat-bounce.com/', 'http://maninthedark.com/', 'https://chrismckenzie.com/',
        'https://smashthewalls.com/']

messsage = lambda: random.choice(link)


@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Ссылка")
    markup.add(item1)
    bot.send_message(m.chat.id,
                     'Нажми: \nСсылка на рандомный сайт',
                     reply_markup=markup)


@bot.message_handler(commands=["start"])
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Ссылка':
        answer = random.choice(link)
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True, interval=0)
