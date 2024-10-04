from telegram import Update
from telegram.ext import ContextTypes
from bot.keyboards.keyboards import KeyboardManager

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to our bot! Select the desired menu",
        reply_markup=KeyboardManager.get_main_keyboard()
    )