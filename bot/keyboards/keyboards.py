from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

class KeyboardManager:
    @staticmethod
    def get_main_keyboard():
        keyboard = [
            [KeyboardButton("Quiz"), KeyboardButton("My vocabulary")],
            [KeyboardButton("Train"), KeyboardButton("Feedback")]
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def get_my_vocabulary_keyboard():
        keyboard = [
            [KeyboardButton("List of vocabulary"), KeyboardButton("➕ Add vocabulary")],
            [KeyboardButton("🏘 Go to main menu")]
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    @staticmethod
    def get_add_word_keyboard():
        keyboard = [
            [KeyboardButton("Add Noun"), KeyboardButton("Add Verb")],
            [KeyboardButton("Add Adjective"), KeyboardButton("Back to Main")]
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    @staticmethod
    def addvocabulary_btns():
        keyboard = [
            [KeyboardButton("🏘 Go to main menu")],
            [KeyboardButton("Skip ⏩")]
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)



    @staticmethod
    def get_quiz_keyboard():
        keyboard = [
            [KeyboardButton("Multiple Choice"), KeyboardButton("Fill in the Blank")],
            [KeyboardButton("True/False"), KeyboardButton("Back to Main")]
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def get_settings_keyboard():
        keyboard = [
            [InlineKeyboardButton("Change Language", callback_data='change_language')],
            [InlineKeyboardButton("Notification Settings", callback_data='notification_settings')],
            [InlineKeyboardButton("Back to Main", callback_data='back_to_main')]
        ]
        return InlineKeyboardMarkup(keyboard)
