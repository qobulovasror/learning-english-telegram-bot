from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters
from quiz.question_generator import generate_questions
from database.default_words import WordDB
import time

CHOOSING, ANSWERING = range(2)

async def start_quiz(update, context):
    user = update.message.from_user
    tables = await WordDB.get_word_tables()
    await update.message.reply_text(
        f"Salom, {user.first_name}! Viktorinani boshlash uchun quyidagi parametrlarni tanlang:\n"
        f"1. So'zlar jadvali: {', '.join(tables)}\n"
        "2. Savollar soni\n"
        "3. Vaqt chegarasi (daqiqada)\n"
        "4. Yo'nalish (eng-uz yoki uz-eng)\n"
        "Masalan: 'Animals 10 5 eng-uz'"
    )
    return CHOOSING

async def setup_quiz(update, context):
    user_input = update.message.text.split()
    if len(user_input) != 4:
        await update.message.reply_text("Noto'g'ri format. Iltimos, qaytadan urinib ko'ring.")
        return CHOOSING

    table, num_questions, time_limit, direction = user_input
    num_questions = int(num_questions)
    time_limit = int(time_limit)

    context.user_data['quiz'] = await generate_questions(table, num_questions, direction)
    context.user_data['current_question'] = 0
    context.user_data['correct_answers'] = 0
    context.user_data['start_time'] = time.time()
    context.user_data['time_limit'] = time_limit * 60

    await send_next_question(update, context)
    return ANSWERING

async def send_next_question(update, context):
    quiz = context.user_data['quiz']
    current = context.user_data['current_question']

    if current < len(quiz):
        question = quiz[current]['question']
        await update.message.reply_text(f"Savol {current + 1}: {question}")
    else:
        await end_quiz(update, context)

async def check_answer(update, context):
    user_answer = update.message.text.lower()
    quiz = context.user_data['quiz']
    current = context.user_data['current_question']
    correct_answer = quiz[current]['answer'].lower()

    if user_answer == correct_answer:
        context.user_data['correct_answers'] += 1
        await update.message.reply_text("To'g'ri!")
    else:
        await update.message.reply_text(f"Noto'g'ri. To'g'ri javob: {correct_answer}")

    context.user_data['current_question'] += 1
    await send_next_question(update, context)

async def end_quiz(update, context):
    correct = context.user_data['correct_answers']
    total = len(context.user_data['quiz'])
    time_taken = time.time() - context.user_data['start_time']

    await update.message.reply_text(
        f"Viktorina tugadi!\n"
        f"To'g'ri javoblar: {correct}/{total}\n"
        f"Sarflangan vaqt: {time_taken:.2f} soniya"
    )
    return ConversationHandler.END

async def cancel_quiz(update, context):
    await update.message.reply_text("Viktorina bekor qilindi. Qaytadan boshlash uchun /quiz buyrug'ini yuboring.")
    context.user_data.clear()
    return ConversationHandler.END

quiz_conv_handler = ConversationHandler(
    entry_points=[CommandHandler('quiz', start_quiz)],
    states={
        CHOOSING: [MessageHandler(filters.TEXT & ~filters.COMMAND, setup_quiz)],
        ANSWERING: [MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer)]
    },
    fallbacks=[CommandHandler('cancel', cancel_quiz)]
)