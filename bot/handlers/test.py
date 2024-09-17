from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.helpers import get_random_joke

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke = get_random_joke()
    await update.message.reply_text(joke)