from telegram import Update
from telegram.ext import ContextTypes
from bot.keyboards.keyboards import KeyboardManager

async def addvocabulary(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # await update.message.reply_text(
    #     "You need to send me a new dictionary in the following order \n\nnew_word || translation",
    #     reply_markup=KeyboardManager.addvocabulary_btns()
    # )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Please send me a new dictionary in the following order \n\nnew_word || translation",
        reply_markup=KeyboardManager.addvocabulary_btns())
    
    message = update.message.text
    print(message)
    # if '|' in message:
    #     parts = message.split('|')
    #     if len(parts) == 4:
    #         word, translation, example, synonyms = parts
    #         conn = sqlite3.connect('vocabulary.db')
    #         c = conn.cursor()
    #         c.execute("INSERT OR REPLACE INTO words VALUES (?, ?, ?, ?)", (word.strip(), translation.strip(), example.strip(), synonyms.strip()))
    #         conn.commit()
    #         conn.close()
    #         await update.message.reply_text(f'Added "{word}" to the vocabulary list.')
    #     else:
    #         await update.message.reply_text('Invalid format. Please use: word|translation|example|synonyms')
    # else:
    #     await update.message.reply_text("I don't understand. Use /add to add a new word.")