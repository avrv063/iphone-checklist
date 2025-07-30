import os
from flask import Flask, request
import telebot

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("Не задан токен бота в переменной окружения TOKEN")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

WEBHOOK_URL = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}/"  # Render даёт этот домен


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = telebot.types.KeyboardButton(
        text="🔍 Проверить iPhone",
        web_app=telebot.types.WebAppInfo(url="https://iphone-checklist.onrender.com")
    )
    markup.add(btn)
    bot.send_message(message.chat.id, "Привет! Нажми кнопку для запуска чек-листа:", reply_markup=markup)


# Flask route для обработки webhook
@app.route("/", methods=["POST"])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "", 200


if __name__ == "__main__":
    # Устанавливаем webhook (удаляем старый, если есть)
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)

    # Запускаем Flask-сервер
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
