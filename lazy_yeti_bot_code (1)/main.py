
import os
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

BOT_TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Welcome to Lazy Yeti Bot!\nUse /latest, /elite, or /og to get your stock insights.")

async def latest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Sending today's FII/DII sector report... (This will auto-run after 4:30 PM daily)")

async def elite(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📈 Filtering breakout stocks from Chartink...")

async def og(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 OG Stocks filtering — confirmed breakout + strong sector + FII/DII buying.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("latest", latest))
    app.add_handler(CommandHandler("elite", elite))
    app.add_handler(CommandHandler("og", og))
    app.run_polling()

if __name__ == "__main__":
    main()
