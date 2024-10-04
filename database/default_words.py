import sqlite3

conn = sqlite3.connect('database/db/words.db')
cursor = conn.cursor()


class WordDB:
    @staticmethod
    async def get_word_tables():
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name!='sqlite_sequence';")
        return [row[0] for row in cursor.fetchall()]
    
    @staticmethod
    async def get_words_from_table(table_name, num_questions):
        cursor.execute(f"SELECT name, translation FROM {table_name} ORDER BY RANDOM() LIMIT {num_questions}")
        data = [row for row in cursor.fetchall()]
        print(data)
        return data
    


    # @staticmethod
    # def insertWord(word, translation, type, example):
    #     cursor.execute("INSERT OR REPLACE INTO custom_words (word, translation, type, example) VALUES (?, ?, ?, ?)", (word.strip(), translation.strip(), type.strip(), example.strip()))
    #     conn.commit()

    # @staticmethod
    # def getWord():
    #     cursor.execute("SELECT * FROM custom_words")
    #     result = cursor.fetchall()
    #     return result
    

    # @staticmethod
    # def getWordByName(name):
    #     cursor.execute("SELECT * FROM custom_words WHERE word=?", (name,))
    #     result = cursor.fetchone()
    #     return result
    
    # @staticmethod
    # def deleteWord(name):
    #     cursor.execute("DELETE FROM custom_words WHERE word = ?", (name, ))
    #     conn.commit()
    #     return cursor.rowcount > 0