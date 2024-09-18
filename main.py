import logging
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
)
from config import TOKEN
from bot.handlers.start import start

# from bot.handlers import myVocabulary, start, quiz
from bot.handlers.my_vocabulary import my_vocabulary
from bot.handlers.my_vocabulary_handler.add_vocabulary import add_word_handler
from bot.handlers.go_home import go_home

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.Regex("^My vocabulary$"), my_vocabulary)
    )
    #add vocabulary conversation 
    application.add_handler(add_word_handler)
    application.add_handler(
        MessageHandler(filters.Regex("^🏘 Go to main menu$"), go_home)
    )
    # application.add_handler(MessageHandler(filters.Regex('^Quiz$'), quiz))
    application.run_polling()


if __name__ == "__main__":
    main()
