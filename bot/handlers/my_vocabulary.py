from telegram import Update
from telegram.ext import ContextTypes
from bot.keyboards.keyboards import KeyboardManager

async def my_vocabulary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Personal dictionaries section \n\nselect the desired menu",
        reply_markup=KeyboardManager.get_my_vocabulary_keyboard()
    )