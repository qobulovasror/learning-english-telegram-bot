from telegram import Update
from telegram.ext import ContextTypes
from bot.keyboards.keyboards import KeyboardManager

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! I'm your friendly bot. What would you like to do?",
        reply_markup=KeyboardManager.get_main_keyboard()
    )