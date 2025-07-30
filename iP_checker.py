<<<<<<< HEAD
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

bot = telebot.TeleBot("7776420560:AAF39adDJrluTlx54gWS1n0RTjSbRq98am8")  # Вставь сюда свой токен

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(
        text="🔍 Проверить iPhone",
        web_app=WebAppInfo(url="https://iphone-checklist.onrender.com")  # Сюда — свой URL
    )
    markup.add(btn)
    bot.send_message(message.chat.id, "Привет! Нажми кнопку для запуска чек-листа:", reply_markup=markup)

bot.infinity_polling()
=======
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

bot = telebot.TeleBot("7776420560:AAF39adDJrluTlx54gWS1n0RTjSbRq98am8")  # Вставь сюда свой токен

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(
        text="🔍 Проверить iPhone",
        web_app=WebAppInfo(url="https://iphone-checklist.onrender.com")  # Сюда — свой URL
    )
    markup.add(btn)
    bot.send_message(message.chat.id, "Привет! Нажми кнопку для запуска чек-листа:", reply_markup=markup)

bot.infinity_polling()
>>>>>>> c6e7418b54b6d99e1337c3f0529169a215354019
 