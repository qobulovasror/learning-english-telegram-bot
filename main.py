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
from bot.handlers.my_vocabulary.menu import my_vocabulary_menu
from bot.handlers.my_vocabulary.add_vocabulary import add_word_handler
from bot.handlers.go_home import go_home
from bot.db.my_vocabulary import MyVocabulary
from bot.handlers.my_vocabulary.vocabulary_list  import show_word_list, vocabulary_list_inline_btn_handler
from bot.handlers.feedback import feedback
from bot.handlers.train import train
from bot.handlers.quiz import quiz

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main():
    MyVocabulary.setup_database()
    application = Application.builder().token(TOKEN).build()

    #start command
    application.add_handler(CommandHandler("start", start))
    #go home command
    application.add_handler(
        MessageHandler(filters.Regex("^🏘 Go to main menu$"), go_home)
    )

    #My vocabulary section
    application.add_handler(
        MessageHandler(filters.Regex("^My vocabulary$"), my_vocabulary_menu)
    )
    #add vocabulary conversation 
    application.add_handler(add_word_handler)

    #list of own vocabulary
    application.add_handler(
        MessageHandler(filters.Regex("^List of vocabulary$"), show_word_list)
    )
    application.add_handler(CallbackQueryHandler(vocabulary_list_inline_btn_handler))
    
    
    application.add_handler(MessageHandler(filters.Regex('^Quiz$'), quiz))

    #feedback
    application.add_handler(MessageHandler(filters.Regex('^Feedback$'), feedback))
    #Train
    application.add_handler(MessageHandler(filters.Regex('^Train$'), train))
    application.run_polling()


if __name__ == "__main__":
    main()
