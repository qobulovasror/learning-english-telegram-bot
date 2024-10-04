from telegram import Update
from telegram.ext import ContextTypes
from bot.keyboards.keyboards import KeyboardManager

async def go_home(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "You are in the main section! Select the desired menu",
        reply_markup=KeyboardManager.get_main_keyboard()
    )