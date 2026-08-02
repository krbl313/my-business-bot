from telegram import Update
from telegram.ext import Application, MessageHandler, filters
import os

TOKEN = os.environ.get("TOKEN")

async def reply(update: Update, context):
    if update.effective_chat.type == "private":
        await update.message.reply_text("Отвечу позже!")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, reply))
app.run_polling()
