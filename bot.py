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
    text = update.message.text.lower().strip()

    qa = {
        ("what is your name", "your name", "name"): "My name is Afrina Jahan Sadia.",
        ("when is your birthday", "birthday", "birth"): "My birthday is August 11. 🎉",
        ("favorite food", "favourite food", "food"): "My favorite foods are biryani, burger, and chicken fry.",
        ("favorite color", "favourite color", "color", "colour"): "My favorite color is baby pink.",
        ("father name", "dad name","baba", "father"): "My father's name is Israil.",
        ("mother name", "mom name","ma", "mother"): "My mother's name is China.",
        ("how many sisters", "siblings", "sister"): "I have two sisters.",
        ("elder sister","boro", "big sister"): "My elder sister's name is Tisha.",
        ("middle sister","middle", "mejo bon","mejo"): "My middle sister's name is Nisha.",
        ("youngest", "smallest", "last child","koto number","tmr number"): "I am the youngest member of my family.",
        ("which class", "class"): "I am in Admission class.",
        ("favorite hobby", "favorite work", "moja"): "I like arguing for fun.",
        ("favorite subject", "favourite subject", "subject","fav sub","sub"): "My favorite subject is Biology.",
        ("where is your village", "village","bari","town", "home town"): "My village home is in Jhenaidah.",
        ("what do you like to do", "hobby", "travel"): "I like traveling and exploring new places.",
        ("what is my dream country", "dream country", "sopner desh", "dream land"): "oh, it's switzerland.I wish I would visit this country!"
    }

    for keywords, answer in qa.items():
        if any(keyword in text for keyword in keywords):
            await update.message.reply_text(answer)
            return

    await update.message.reply_text(
        "Sorry, I don't know the answer to that question yet."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("Bot is running...")
app.run_polling(drop_pending_updates=True)
