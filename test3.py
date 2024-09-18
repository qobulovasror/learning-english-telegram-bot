from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext

# Dictionary to store user vocabulary
user_vocabulary = {}

# Start command: displays the main menu
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("My Vocabulary", callback_data='my_vocabulary')],
        [InlineKeyboardButton("Test", callback_data='test')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome to the Vocabulary Bot! Choose an option:", reply_markup=reply_markup)

# Handler for 'My Vocabulary' section
def my_vocabulary(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    # Provide options to add or view words
    keyboard = [
        [InlineKeyboardButton("Add New Word", callback_data='add_word')],
        [InlineKeyboardButton("View My Words", callback_data='view_words')],
        [InlineKeyboardButton("Back to Main Menu", callback_data='back_to_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="My Vocabulary Section:", reply_markup=reply_markup)

# Function to handle word adding
def add_word(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text("Please send the new word to add:")
    return "ADDING_WORD"

# Function to handle word addition input
def adding_word(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    word = update.message.text

    # Add the word to the user's vocabulary
    if user_id not in user_vocabulary:
        user_vocabulary[user_id] = []
    user_vocabulary[user_id].append(word)

    update.message.reply_text(f"'{word}' has been added to your vocabulary!")

# Function to view the user's vocabulary
def view_words(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id

    # Check if the user has any words
    if user_id in user_vocabulary and user_vocabulary[user_id]:
        words = '\n'.join(user_vocabulary[user_id])
        query.edit_message_text(f"Your words:\n{words}")
    else:
        query.edit_message_text("Your vocabulary is empty!")

# Main menu callback
def back_to_menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    start(update, context)

def main() -> None:
    # Your bot token
    TOKEN = 'YOUR_BOT_TOKEN'

    # Initialize the Updater and Dispatcher
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Command handler for /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Callback handlers for sections
    dispatcher.add_handler(CallbackQueryHandler(my_vocabulary, pattern='my_vocabulary'))
    dispatcher.add_handler(CallbackQueryHandler(add_word, pattern='add_word'))
    dispatcher.add_handler(CallbackQueryHandler(view_words, pattern='view_words'))
    dispatcher.add_handler(CallbackQueryHandler(back_to_menu, pattern='back_to_menu'))

    # Message handler for adding words
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, adding_word))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()




























from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters, CallbackContext

# Import section handlers from different files
from vocabulary import vocabulary_section, add_word, view_words, adding_word

# Dictionary to store user vocabulary
user_vocabulary = {}

# States for conversation handlers
ADDING_WORD = range(1)

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("My Vocabulary", callback_data='my_vocabulary')],
        [InlineKeyboardButton("Test", callback_data='test')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome to the Vocabulary Bot! Choose an option:", reply_markup=reply_markup)

def main() -> None:
    TOKEN = 'YOUR_BOT_TOKEN'

    # Initialize the Updater and Dispatcher
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Command handler for /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Vocabulary section handlers
    dispatcher.add_handler(CallbackQueryHandler(vocabulary_section, pattern='my_vocabulary'))

    # ConversationHandler to manage adding words
    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(add_word, pattern='add_word')],
        states={
            ADDING_WORD: [MessageHandler(Filters.text & ~Filters.command, adding_word)]
        },
        fallbacks=[CallbackQueryHandler(view_words, pattern='view_words')]
    )
    dispatcher.add_handler(conv_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()






from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

user_vocabulary = {}  # Shared user vocabulary across modules

# My Vocabulary section
def vocabulary_section(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Add New Word", callback_data='add_word')],
        [InlineKeyboardButton("View My Words", callback_data='view_words')],
        [InlineKeyboardButton("Back to Main Menu", callback_data='back_to_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="My Vocabulary Section:", reply_markup=reply_markup)

# Add new word
def add_word(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text("Please send the new word to add:")
    return 1  # Move to the state ADDING_WORD

# Adding the word to the user's vocabulary
def adding_word(update: Update, context: CallbackContext) -> int:
    user_id = update.message.from_user.id
    word = update.message.text

    if user_id not in user_vocabulary:
        user_vocabulary[user_id] = []
    user_vocabulary[user_id].append(word)

    update.message.reply_text(f"'{word}' has been added to your vocabulary!")
    return -1  # End the conversation after adding

# View words in the user's vocabulary
def view_words(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id

    if user_id in user_vocabulary and user_vocabulary[user_id]:
        words = '\n'.join(user_vocabulary[user_id])
        query.edit_message_text(f"Your words:\n{words}")
    else:
        query.edit_message_text("Your vocabulary is empty!")







