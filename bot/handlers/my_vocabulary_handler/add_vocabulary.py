from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    ContextTypes,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters
)
from bot.keyboards.keyboards import KeyboardManager
from bot.handlers.my_vocabulary import my_vocabulary

WORD, DEFINITION, EXAMPLE, CONFIRM = range(4)


# Start the add word conversation
async def start_add_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Let's add a new word to your vocabulary list! What's the word?", reply_markup=KeyboardManager.addvocabulary_btns())
    return WORD

# Get the word
async def get_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['new_word'] = update.message.text
    await update.message.reply_text(f"Great! Now, what's the definition of '{context.user_data['new_word']}'?")
    return DEFINITION

# Get the definition
async def get_definition(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['definition'] = update.message.text
    
    keyboard = [['Noun', 'Verb'], ['Adjective', 'Adverb'], ['Other'], 'Skip ⏩']
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        "Can you provide an example sentence using this word? Or press 'Skip ⏩' to skip this step.?",
        reply_markup=reply_markup
    )
    return EXAMPLE

# Get the example sentence
async def get_example(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['example'] = update.message.text
    
    # Prepare confirmation message
    confirmation = f"Here's the word you want to add:\n\n" \
                   f"Word: {context.user_data['new_word']}\n" \
                   f"Definition: {context.user_data['definition']}\n" \
                   f"Example: {context.user_data['example']}\n\n" \
                   f"Do you want to save this word? (Yes/No)"
    
    keyboard = [['Yes', 'No']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(confirmation, reply_markup=reply_markup)
    return CONFIRM

# Confirm and save the word
async def confirm_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text.lower() == 'yes':
        # Here you would typically save the word to your database
        # For this example, we'll just print it
        print(f"Saving word: {context.user_data['new_word']}")
        await update.message.reply_text(
            f"Great! I've added '{context.user_data['new_word']}' to your vocabulary list.",
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await update.message.reply_text(
            "Okay, I won't save this word.",
            reply_markup=ReplyKeyboardRemove()
        )
    
    # Clear the user data
    context.user_data.clear()
    await my_vocabulary(update, context)
    return ConversationHandler.END


# Define cancel command
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Word addition cancelled.",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


add_word_handler = ConversationHandler(
    # entry_points=[CommandHandler('➕ Add vocabulary', start_add_word)],
    entry_points=[MessageHandler(filters.Regex("^➕ Add vocabulary$"), start_add_word)],
    states={
        WORD: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_word)],
        DEFINITION: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_definition)],
        EXAMPLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_example)],
        CONFIRM: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirm_word)],
    },
    fallbacks=[MessageHandler(filters.Regex("^🏘 Go to main menu$"), cancel)],
    
)