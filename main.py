import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TOKEN
# from bot.handlers import myVocabulary, start, quiz
from bot.handlers.start import start
from bot.handlers.my_vocabulary import my_vocabulary

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    # application.add_handler(MessageHandler(filters.Regex('^Quiz$'), quiz))
    application.add_handler(MessageHandler(filters.Regex('^My vocabulary$'), my_vocabulary))

    application.run_polling()

if __name__ == '__main__':
    main()