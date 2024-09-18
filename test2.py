# bot/keyboards/keyboards.py
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

class KeyboardManager:
    @staticmethod
    def get_main_keyboard():
        keyboard = [
            [KeyboardButton("Add Word"), KeyboardButton("Quiz")],
            [KeyboardButton("Statistics"), KeyboardButton("Settings")]
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def get_add_word_keyboard():
        keyboard = [
            [KeyboardButton("Add Noun"), KeyboardButton("Add Verb")],
            [KeyboardButton("Add Adjective"), KeyboardButton("Back to Main")]
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def get_quiz_keyboard():
        keyboard = [
            [KeyboardButton("Multiple Choice"), KeyboardButton("Fill in the Blank")],
            [KeyboardButton("True/False"), KeyboardButton("Back to Main")]
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def get_settings_keyboard():
        keyboard = [
            [InlineKeyboardButton("Change Language", callback_data='change_language')],
            [InlineKeyboardButton("Notification Settings", callback_data='notification_settings')],
            [InlineKeyboardButton("Back to Main", callback_data='back_to_main')]
        ]
        return InlineKeyboardMarkup(keyboard)

# bot/handlers/main_handler.py
from telegram import Update
from telegram.ext import ContextTypes
from bot.keyboards.keyboards import KeyboardManager

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to the Vocabulary Builder Bot!",
        reply_markup=KeyboardManager.get_main_keyboard()
    )

async def add_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Choose a word type to add:",
        reply_markup=KeyboardManager.get_add_word_keyboard()
    )

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Select a quiz type:",
        reply_markup=KeyboardManager.get_quiz_keyboard()
    )

async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Settings:",
        reply_markup=KeyboardManager.get_settings_keyboard()
    )

# main.py
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from config import TOKEN
from bot.handlers.main_handler import start, add_word, quiz, settings

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Regex('^Add Word$'), add_word))
    application.add_handler(MessageHandler(filters.Regex('^Quiz$'), quiz))
    application.add_handler(MessageHandler(filters.Regex('^Settings$'), settings))
    
    # Add more handlers as needed
    
    application.run_polling()

if __name__ == '__main__':
    main()





























# bot/handlers/word_list.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler, CommandHandler
from typing import List

# Simulated word list (replace with your actual data source)
word_list = ["apple", "banana", "cherry", "date", "elderberry"]
WORDS_PER_PAGE = 3

def get_word_keyboard(page: int = 0) -> InlineKeyboardMarkup:
    keyboard = []
    start = page * WORDS_PER_PAGE
    end = start + WORDS_PER_PAGE
    
    for word in word_list[start:end]:
        keyboard.append([InlineKeyboardButton(word, callback_data=f"word:{word}")])
    
    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton("◀️ Previous", callback_data=f"page:{page-1}"))
    if end < len(word_list):
        nav.append(InlineKeyboardButton("Next ▶️", callback_data=f"page:{page+1}"))
    
    if nav:
        keyboard.append(nav)
    
    return InlineKeyboardMarkup(keyboard)




async def show_word_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = get_word_keyboard()
    await update.message.reply_text("Here's the list of words:", reply_markup=keyboard)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    data = query.data.split(':')
    action = data[0]
    value = data[1]
    
    if action == "page":
        page = int(value)
        keyboard = get_word_keyboard(page)
        await query.edit_message_reply_markup(reply_markup=keyboard)
    elif action == "word":
        await query.edit_message_text(f"You selected the word: {value}\nWhat would you like to do?",
                                      reply_markup=InlineKeyboardMarkup([
                                          [InlineKeyboardButton("Edit", callback_data=f"edit:{value}")],
                                          [InlineKeyboardButton("Delete", callback_data=f"delete:{value}")],
                                          [InlineKeyboardButton("Back to List", callback_data="page:0")]
                                      ]))
    elif action == "edit":
        # Here you would typically start a conversation to edit the word
        await query.edit_message_text(f"Editing word: {value}\nPlease enter the new word:")
        # Set up the next step in the conversation
        context.user_data['editing_word'] = value
    elif action == "delete":
        # Here you would delete the word from your data source
        word_list.remove(value)  # This is just for demonstration
        await query.edit_message_text(f"Deleted word: {value}")
        # Show the updated list
        keyboard = get_word_keyboard()
        await query.edit_message_text("Updated word list:", reply_markup=keyboard)

# In your main.py or wherever you set up your application
def setup(application):
    application.add_handler(CommandHandler("words", show_word_list))
    application.add_handler(CallbackQueryHandler(button_callback))

# You might also want to add a conversation handler for editing words