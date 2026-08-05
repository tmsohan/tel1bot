from dotenv import load_dotenv
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! Ask me: 'When is your birthday?'"
    )


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "birth" in text or "birthday"or "bir" or "jormo" or "jormodin" or "poida" in text:
        await update.message.reply_text("Your birthday is August 11. 🎉")
    else:
        await update.message.reply_text("Sorry, I didn't understand your question.")


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("Bot is running...")
app.run_polling(drop_pending_updates=True)
