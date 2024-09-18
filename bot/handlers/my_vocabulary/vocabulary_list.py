from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler, CommandHandler
from bot.keyboards.keyboards import KeyboardManager 
from bot.db.my_vocabulary import MyVocabulary


# async def addvocabulary(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "Personal dictionaries section \n\nselect the desired menu",
#         reply_markup=KeyboardManager.get_my_vocabulary_keyboard()
#     )

WORDS_PER_PAGE = 3

def get_word_keyboard(page: int = 0) -> InlineKeyboardMarkup:
    words = MyVocabulary.getWord()
    word_list = [row[1:2][0] for row in words]
    keyboard = []
    start = page * WORDS_PER_PAGE
    end = start + WORDS_PER_PAGE
    
    for word in word_list[start:end]:
        keyboard.append([InlineKeyboardButton(word, callback_data=f"word:{word}")])
    
    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton("◀️ Previous", callback_data=f"page:{page-1}"))
    if end < len(word_list):
        nav.append(InlineKeyboardButton("Next ▶️", callback_data=f"page:{page+1}"))
    
    if nav:
        keyboard.append(nav)
    
    return InlineKeyboardMarkup(keyboard)

async def show_word_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = get_word_keyboard()
    await update.message.reply_text(text="Here's the list of words:", reply_markup=keyboard)



async def vocabulary_list_inline_btn_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    data = query.data.split(':')
    action = data[0]
    value = data[1]
    
    if action == "page":
        page = int(value)
        keyboard = get_word_keyboard(page)
        await query.edit_message_text(text="Here's the list of words:", reply_markup=keyboard)
    elif action == "word":
        word = MyVocabulary.getWordByName(value)
        text = f"You selected the word:\n\n" \
                   f"Word: {word[1]}\n" \
                   f"Translation: {word[2]}\n" \
                   f"Part of Speech: {word[3]}\n" \
                   f"Example: {word[4]}\n\n"\
                   f"What would you like to do?"
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup([
                                          [InlineKeyboardButton("Delete", callback_data=f"delete:{value}")],
                                          [InlineKeyboardButton("Back to List", callback_data="page:0")]
                                      ]))
    elif action == "delete":
        await query.answer(text=f"You deleted the word: {value}")
        MyVocabulary.deleteWord(value)
        keyboard = get_word_keyboard()
        await query.edit_message_text("Updated word list:", reply_markup=keyboard)
