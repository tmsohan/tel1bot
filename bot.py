from log import logger
from dotenv import load_dotenv
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(
        f"START | User: {update.effective_user.first_name} "
        f"(@{update.effective_user.username}) | "
        f"ID: {update.effective_user.id}"
    )
    await update.message.reply_text(
        "Hello! Ask Qus as if I were you: 'How can I help you today?'"
    )


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(
        f"MESSAGE | User: {update.effective_user.first_name} "
        f"(@{update.effective_user.username}) | "
        f"ID: {update.effective_user.id} | "
        f"Text: {update.message.text}"
    )
    text = update.message.text.lower().strip()

    qa = {("which country", "country", "desh"): "I am from Bangladesh.",
        ("what is your name", "your name", "name"): "My name is alfedo de cambo.",
        ("when is your birthday", "birthday", "birth"): "My birthday is August 02. 🎉",
        ("favorite food", "favourite food", "food"): "My favorite foods are pizza, burger, and chicken fry.",
        ("favorite color", "favourite color", "color", "colour"): "My favorite color is black.",
        ("father name", "dad name","baba", "father"): "My father's name is estafow de leo  .",
        ("mother name", "mom name","ma", "mother"): "My mother's name is Chalina hatu.",
        ("how many sisters", "siblings", "sister"): "I have two sisters.",
        ("elder sister","boro", "big sister"): "My elder sister's name is casime loue.",
        ("middle sister","middle", "mejo bon","mejo"): "My middle sister's name is Nis deau.",
        ("youngest", "smallest", "last child","koto number","tmr number"): "I am the youngest member of my family.",
        ("which class", "class"): "I am in M.Sc.", 
        ("favorite hobby", "favorite work", "moja"): "I like study and explore my knowledge.",
        ("favorite subject", "favourite subject", "subject","fav sub","sub"): "My favorite subject is Math.",
        ("where is your village", "village","bari","town", "home town"): "My village home is in locato.",
        ("what do you like to do", "hobby", "travel"): "I like traveling and exploring new places.",
        ("what is my dream country", "dream country", "sopner desh", "dream land"): "oh, it's canada.I wish I would visit this country!"
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
