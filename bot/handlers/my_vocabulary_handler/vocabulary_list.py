from telegram import Update
from telegram.ext import ContextTypes
from bot.keyboards.keyboards import KeyboardManager

async def addvocabulary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Personal dictionaries section \n\nselect the desired menu",
        reply_markup=KeyboardManager.get_my_vocabulary_keyboard()
    )

# bot/handlers/word_list.py
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import ContextTypes, CallbackQueryHandler, CommandHandler
# from typing import List

# Simulated word list (replace with your actual data source)
# word_list = ["apple", "banana", "cherry", "date", "elderberry"]
# WORDS_PER_PAGE = 3

# def get_word_keyboard(page: int = 0) -> InlineKeyboardMarkup:
#     keyboard = []
#     start = page * WORDS_PER_PAGE
#     end = start + WORDS_PER_PAGE
    
#     for word in word_list[start:end]:
#         keyboard.append([InlineKeyboardButton(word, callback_data=f"word:{word}")])
    
#     nav = []
#     if page > 0:
#         nav.append(InlineKeyboardButton("◀️ Previous", callback_data=f"page:{page-1}"))
#     if end < len(word_list):
#         nav.append(InlineKeyboardButton("Next ▶️", callback_data=f"page:{page+1}"))
    
#     if nav:
#         keyboard.append(nav)
    
#     return InlineKeyboardMarkup(keyboard)

# async def show_word_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     keyboard = get_word_keyboard()
#     await update.message.reply_text("Here's the list of words:", reply_markup=keyboard)
