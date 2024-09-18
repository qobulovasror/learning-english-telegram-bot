from telegram import Update
from telegram.ext import ContextTypes
from bot.keyboards.keyboards import KeyboardManager

async def train(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Currently tain section is not woking")