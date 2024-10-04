from telegram.ext import (
    CommandHandler, 
    MessageHandler, 
    filters,
    MessageHandler,
    CallbackQueryHandler
  )

# from bot.handlers import myVocabulary, start, quiz
from bot.handlers.my_vocabulary.menu import my_vocabulary_menu
from bot.handlers.my_vocabulary.add_vocabulary import add_word_handler
from bot.handlers.go_home import go_home
# from database.default_words import MyVocabulary
from bot.handlers.my_vocabulary.vocabulary_list  import show_word_list, vocabulary_list_inline_btn_handler
from bot.handlers.feedback import feedback
from bot.handlers.train import train
from bot.handlers.quiz import quiz
from bot.handlers.start import start
from quiz.quiz_handler import quiz_conv_handler

def setup_commands(application):
    # application.add_handler(CommandHandler("help", help_command))
    
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
    
    
    # application.add_handler(MessageHandler(filters.Regex('^Quiz$'), quiz))

    #feedback
    application.add_handler(MessageHandler(filters.Regex('^Feedback$'), feedback))
    #Train
    application.add_handler(MessageHandler(filters.Regex('^Train$'), train))

    #for Quiz
    application.add_handler(quiz_conv_handler)