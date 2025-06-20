import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ❗ Hardcoded bot token (use env var in production)
BOT_TOKEN = "8006623960:AAHbVLtKObGeSqASOuLoV1mV8EWX5uvNPxQ"

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Welcome to Lazy Yeti Bot!\nUse /latest, /elite, or /og to get your stock insights.")

# Main
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
