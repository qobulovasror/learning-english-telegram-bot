from database.default_words import WordDB
import random

def generate_questions(table, num_questions, direction):
    words = WordDB.get_words_from_table(table, num_questions)
    questions = []
    for word in words:
        if direction == 'eng-uz':
            question = {'question': word['name'], 'answer': word['translation']}
        else:
            question = {'question': word['translation'], 'answer': word['name']}
        questions.append(question)
    random.shuffle(questions)
    return questions