from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    ContextTypes,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters
)
from bot.keyboards.keyboards import KeyboardManager
from bot.handlers.my_vocabulary.menu import my_vocabulary_menu
from database.my_vocabulary import MyVocabulary

WORD, TRANSLATION, PART_OF_SPEECH, EXAMPLE, CONFIRM = range(5)


# Start the add word conversation
async def start_add_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    keyboard = [['🔙 Go to menu']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("Let's add a new word to your vocabulary list! \nWhat's the word?", reply_markup=reply_markup)
    return WORD

# Get the word
async def get_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == '🔙 Go to menu':
        await my_vocabulary_menu(update, context)
        return ConversationHandler.END
    
    keyboard = [['🔙 Go to menu']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.user_data['new_word'] = update.message.text
    await update.message.reply_text(f"Great! Now, what's the tranlation of '{context.user_data['new_word']}'?", reply_markup=reply_markup)
    return TRANSLATION

# Get the tranlation
async def get_translation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == '🔙 Go to menu':
        await my_vocabulary_menu(update, context)
        return ConversationHandler.END
    
    context.user_data['tranlation'] = update.message.text
    
    keyboard = [['Noun', 'Verb'], ['Adjective', 'Adverb'], ['Other']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    
    await update.message.reply_text(
        "Can you provide an example sentence using this word?",
        reply_markup=reply_markup
    )
    return PART_OF_SPEECH

# Get the part of speech
async def get_part_of_speech(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['part_of_speech'] = update.message.text
    keyboard = [['Skip ⏩'], ['🔙 Go to menu']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    
    await update.message.reply_text(
        "Can you provide an example sentence using this word?",
        reply_markup=reply_markup
    )
    return EXAMPLE

# Get the example sentence
async def get_example(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == 'Skip ⏩':
        context.user_data['example'] = " "
    else:
        context.user_data['example'] = update.message.text
    
    # Prepare confirmation message
    confirmation = f"Here's the word you want to add:\n\n" \
                   f"Word: {context.user_data['new_word']}\n" \
                   f"Translation: {context.user_data['tranlation']}\n" \
                   f"Part of Speech: {context.user_data['part_of_speech']}\n" \
                   f"Example: {context.user_data['example']}\n\n" \
                   f"Do you want to save this word? (Yes/No)"
    
    keyboard = [['Yes', 'No']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    
    await update.message.reply_text(confirmation, reply_markup=reply_markup)
    return CONFIRM

# Confirm and save the word
async def confirm_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text.lower() == 'yes':
        MyVocabulary.insertWord(word=context.user_data['new_word'], 
                                translation=context.user_data['tranlation'],
                                type=context.user_data['part_of_speech'],
                                example=context.user_data['example'])
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
    await my_vocabulary_menu(update, context)
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
        TRANSLATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_translation)],
        PART_OF_SPEECH: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_part_of_speech)],
        EXAMPLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_example)],
        CONFIRM: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirm_word)],
    },
    fallbacks=[MessageHandler(filters.Regex("^🔙 Go to menu$"), cancel)],
    
)