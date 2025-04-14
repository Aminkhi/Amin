import telebot
import random

BOT_TOKEN = 8018160379:AAG4fWoLjHt0V-eefuEAHhLUWh2uPXlvhos

bot = telebot.TeleBot(BOT_TOKEN)

quotes = [
    "تو می‌تونی موفق بشی!",
    "هیچ‌چیز غیرممکن نیست.",
    "هر روز یه فرصته!",
    "ادامه بده، نتیجه نزدیکه."
]

@bot.message_handler(func=lambda message: True)
def send_quote(message):
    quote = random.choice(quotes)
    bot.reply_to(message, quote)

bot.polling()
