# import logging
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
# import sqlite3

# # Set up logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# # Database setup
# def setup_database():
#     conn = sqlite3.connect('vocabulary.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS words
#                  (word TEXT PRIMARY KEY, translation TEXT, example TEXT, synonyms TEXT)''')
#     conn.commit()
#     conn.close()

# # Bot commands
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Welcome to the Vocabulary Bot! Use /add to add a new word.')

# async def add_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Please enter a new word in this format:\nword|translation|example|synonyms')

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     message = update.message.text
#     if '|' in message:
#         parts = message.split('|')
#         if len(parts) == 4:
#             word, translation, example, synonyms = parts
#             conn = sqlite3.connect('vocabulary.db')
#             c = conn.cursor()
#             c.execute("INSERT OR REPLACE INTO words VALUES (?, ?, ?, ?)", (word.strip(), translation.strip(), example.strip(), synonyms.strip()))
#             conn.commit()
#             conn.close()
#             await update.message.reply_text(f'Added "{word}" to the vocabulary list.')
#         else:
#             await update.message.reply_text('Invalid format. Please use: word|translation|example|synonyms')
#     else:
#         await update.message.reply_text("I don't understand. Use /add to add a new word.")

# async def get_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     conn = sqlite3.connect('vocabulary.db')
#     c = conn.cursor()
#     c.execute("SELECT * FROM words ORDER BY RANDOM() LIMIT 1")
#     word = c.fetchone()
#     conn.close()

#     if word:
#         response = f"Word: {word[0]}\nTranslation: {word[1]}\nExample: {word[2]}\nSynonyms: {word[3]}"
#     else:
#         response = "No words in the database yet. Add some words first!"

#     await update.message.reply_text(response)

# def main():
#     setup_database()
    
#     application = ApplicationBuilder().token('7513044020:AAG79dUso_ZztnKTNe8heLlud5mkNA0gc6E').build()

#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("add", add_word))
#     application.add_handler(CommandHandler("word", get_word))
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

#     application.run_polling()

# if __name__ == '__main__':
#     main()








# import asyncio
# import platform

# import logging
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
# from googletrans import Translator

# # Initialize the Translator
# translator = Translator()

# # Set up logging
# logging.basicConfig(level=logging.INFO)

# # Function to handle the /start command
# async def start(update: Update, context) -> None:
#     await update.message.reply_text("Salom! Yangi so'z kiriting va men sizga bir nechta gap va ularning o'zbekcha tarjimasini yarataman.")

# # Function to handle user messages (word input)
# async def handle_word(update: Update, context) -> None:
#     word = update.message.text
#     example_sentences = generate_sentences(word)  # Function to generate English sentences
#     translated_sentences = translate_to_uzbek(example_sentences)

#     response = "\n".join([f"{eng} - {uz}" for eng, uz in zip(example_sentences, translated_sentences)])
#     await update.message.reply_text(response)

# # Generate sentences using a predefined function or external API
# def generate_sentences(word):
#     # Dummy sentences for demonstration purposes
#     return [
#         f"The {word} is very useful.",
#         f"I have a {word} in my bag.",
#         f"Can you give me the {word}?"
#     ]

# # Function to translate sentences to Uzbek using Google Translate API
# def translate_to_uzbek(sentences):
#     translations = []
#     for sentence in sentences:
#         translation = translator.translate(sentence, src='en', dest='uz').text
#         translations.append(translation)
#     return translations

# # Main function to run the bot
# async def main():
#     # Add your token here
#     token = '7513044020:AAG79dUso_ZztnKTNe8heLlud5mkNA0gc6E'
#     application = ApplicationBuilder().token(token).build()

#     # Command handler for /start
#     application.add_handler(CommandHandler('start', start))

#     # Message handler for user input (words)
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_word))

#     # Run the bot
#     await application.start()
#     await application.idle()

# if __name__ == '__main__':
#   main()
#   # if platform.system() == 'Windows':
#   #   asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#   # else:  
#   #   asyncio.run(main())





# from googletrans import Translator

# translator = Translator()

# def translate_to_uzbek(sentence):
#     translation = translator.translate(sentence, src='en', dest='uz').text
#     return translation

# print(translate_to_uzbek(["This is good job."]))






# from googletrans import Translator

# translator = Translator()

# def translate_to_uzbek(sentences):
#     translations = []
#     for sentence in sentences:
#         translation = translator.translate(sentence, src='en', dest='uz').text
#         translations.append(translation)
#     return translations

# # Now you can pass a list of sentences
# print(translate_to_uzbek(["This is a good job.", "How are you?"]))






# bot/handlers/add_word.py
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    ContextTypes,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters
)

# Define states
WORD, DEFINITION, PART_OF_SPEECH, EXAMPLE, CONFIRM = range(5)

# Define cancel command
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Word addition cancelled.",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

# Start the add word conversation
async def start_add_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Let's add a new word to your vocabulary list! What's the word?")
    return WORD

# Get the word
async def get_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['new_word'] = update.message.text
    await update.message.reply_text(f"Great! Now, what's the definition of '{context.user_data['new_word']}'?")
    return DEFINITION

# Get the definition
async def get_definition(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['definition'] = update.message.text
    
    keyboard = [['Noun', 'Verb'], ['Adjective', 'Adverb'], ['Other']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        "What part of speech is this word?",
        reply_markup=reply_markup
    )
    return PART_OF_SPEECH

# Get the part of speech
async def get_part_of_speech(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['part_of_speech'] = update.message.text
    await update.message.reply_text(
        "Can you provide an example sentence using this word?",
        reply_markup=ReplyKeyboardRemove()
    )
    return EXAMPLE

# Get the example sentence
async def get_example(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['example'] = update.message.text
    
    # Prepare confirmation message
    confirmation = f"Here's the word you want to add:\n\n" \
                   f"Word: {context.user_data['new_word']}\n" \
                   f"Definition: {context.user_data['definition']}\n" \
                   f"Part of Speech: {context.user_data['part_of_speech']}\n" \
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
    return ConversationHandler.END

# Set up the conversation handler
add_word_handler = ConversationHandler(
    entry_points=[CommandHandler('add_word', start_add_word)],
    states={
        WORD: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_word)],
        DEFINITION: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_definition)],
        PART_OF_SPEECH: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_part_of_speech)],
        EXAMPLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_example)],
        CONFIRM: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirm_word)],
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)

# In your main.py or wherever you set up your application
def setup(application):
    application.add_handler(add_word_handler)