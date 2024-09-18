from telegram import Update
from telegram.ext import ContextTypes
from bot.keyboards.keyboards import KeyboardManager

async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Currently feedack section is not woking")