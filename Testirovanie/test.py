import requests
import random
import telebot
from telebot import types
from bs4 import BeautifulSoup as b

URL = 'https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D1%80%D1%82%D0%B0%D0%BB:%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F/%D0%A6%D0%B8%D1%82%D0%B0%D1%82%D1%8B'
URL1 = 'https://www.anekdot.ru/tags/%D0%BF%D0%BE%D1%88%D0%BB%D1%8B%D0%B5'
API_KEY = '5498550016:AAFIEmPz9KjP6Dm1CbuH3qCAefHQMEH3GQo'
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    qoutes  = soup.find_all('div', class_= 'ts-Цитата')
    return [c.text for c in qoutes]

list_of_qoutes = parser(URL)
random.shuffle(list_of_qoutes)

def parser1(url1):
    t = requests.get(url1)
    soup = b(t.text, 'html.parser')
    jokes  = soup.find_all('div', class_= 'text')
    return [c.text for c in jokes]

list_of_jokes = parser1(URL1)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton("Анекдоты")
    item_2 = types.KeyboardButton("Цитаты")
    markup.add(item_1,item_2)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Анекдоты":
        bot.send_message(message.chat.id,list_of_jokes[0])
        del list_of_jokes[0]
    elif message.text=="Цитаты":
        bot.send_message(message.chat.id, list_of_qoutes[0])
        del list_of_qoutes[0]
    else:
        bot.send_message(message.chat.id, 'Нажмите на кнопку:')

bot.infinity_polling()








