from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler, CommandHandler
from typing import List

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    data = query.data.split(':')
    action = data[0]
    value = data[1]
    
    if action == "page":
        page = int(value)
        keyboard = get_word_keyboard(page)
        await query.edit_message_reply_markup(reply_markup=keyboard)
    elif action == "word":
        await query.edit_message_text(f"You selected the word: {value}\nWhat would you like to do?",
                                      reply_markup=InlineKeyboardMarkup([
                                          [InlineKeyboardButton("Edit", callback_data=f"edit:{value}")],
                                          [InlineKeyboardButton("Delete", callback_data=f"delete:{value}")],
                                          [InlineKeyboardButton("Back to List", callback_data="page:0")]
                                      ]))
    elif action == "edit":
        # Here you would typically start a conversation to edit the word
        await query.edit_message_text(f"Editing word: {value}\nPlease enter the new word:")
        # Set up the next step in the conversation
        context.user_data['editing_word'] = value
    elif action == "delete":
        # Here you would delete the word from your data source
        word_list.remove(value)  # This is just for demonstration
        await query.edit_message_text(f"Deleted word: {value}")
        # Show the updated list
        keyboard = get_word_keyboard()
        await query.edit_message_text("Updated word list:", reply_markup=keyboard)
