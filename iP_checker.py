import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

TOKEN = os.getenv("TOKEN")  # Читаем токен из переменной окружения
if not TOKEN:
    raise ValueError("Не задан токен бота в переменной окружения TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(
        text="🔍 Проверить iPhone",
        web_app=WebAppInfo(url="https://iphone-checklist.onrender.com")
    )
    markup.add(btn)
    bot.send_message(message.chat.id, "Привет! Нажми кнопку для запуска чек-листа:", reply_markup=markup)

bot.infinity_polling()
