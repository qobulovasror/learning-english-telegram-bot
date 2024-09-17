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