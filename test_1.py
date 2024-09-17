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