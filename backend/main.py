from flask import Flask
import threading
import logging
from telegram.ext import Application

from config import TOKEN

#imports for bot
from database.my_vocabulary import MyVocabulary
from bot.commands.bot_commands import setup_commands

#imports for APIs
from API.words import word_api


#logger
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

app = Flask(__name__)
app.register_blueprint(word_api, url_prefix="/api")

# def run_flask():
#     app.run(port=5000)

def main():
    #setup DBs
    MyVocabulary.setup_database()

    #setup
    application = Application.builder().token(TOKEN).build()
    setup_commands(application)
    application.run_polling()

    #setup API
    # threading.Thread(target=run_flask).start()


if __name__ == "__main__":
    main()
