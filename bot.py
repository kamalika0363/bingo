import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from credentials import bot_token, bot_user_name, URL
from dotenv import load_dotenv

global bot
global TOKEN

load_dotenv()
TOKEN = os.environ.get("BOT_TOKEN")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# async def conn(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
