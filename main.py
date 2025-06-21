import telebot
from datetime import datetime
import requests

BOT_TOKEN = '8006623960:AAHbVLtKObGeSqASOuLoV1mV8EWX5uvNPxQ'
bot = telebot.TeleBot(BOT_TOKEN)

# === LIVE CMP FETCH FUNCTION ===
def get_nse_cmp(symbol):
    url = f"https://www.nseindia.com/api/quote-equity?symbol={symbol}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Referer": f"https://www.nseindia.com/get-quotes/equity?symbol={symbol}"
    }

    session = requests.Session()
    session.headers.update(headers)

    try:
        response = session.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data['priceInfo']['lastPrice']
        else:
            return "⚠️ CMP not found"
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome to Lazy Yeti Bot!\nUse /elite to get elite breakout picks.")

@bot.message_handler(commands=['elite'])
def elite_command(message):
    now = datetime.now()
    hour = now.hour
    minute = now.minute

    try:
        with open('elite.txt', 'r') as file:
            elite_data = file.read()
    except FileNotFoundError:
        elite_data = "⚠️ No elite stock data found. Try again after 4:30 PM."

    if hour < 16 or (hour == 16 and minute < 30):
        bot.reply_to(message, "📅 Market is still open. Showing yesterday’s elite picks:")
    else:
        bot.reply_to(message, "✅ Here are today’s elite breakout picks:")

    bot.send_message(message.chat.id, elite_data)

print("✅ Lazy Yeti bot is running...")
bot.polling()
