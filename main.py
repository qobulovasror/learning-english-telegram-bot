import logging
from telegram.ext import Application, CommandHandler
from config import TOKEN
from bot.handlers import customVocabulary, start, test

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("test", test))
    application.add_handler(CommandHandler("myVocabulary", customVocabulary))
    
    application.run_polling()

if __name__ == '__main__':
    main()