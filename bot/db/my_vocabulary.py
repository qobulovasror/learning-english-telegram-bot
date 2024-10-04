import sqlite3

conn = sqlite3.connect('db/myvocabulary.db')
cursor = conn.cursor()


class MyVocabulary:
    @staticmethod
    def setup_database():
        cursor.execute('''CREATE TABLE IF NOT EXISTS custom_words(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                word TEXT NOT NULL UNIQUE, 
                translation TEXT, 
                type TEXT,
                example TEXT,
                synonyms TEXT
                )''')
        conn.commit()


    @staticmethod
    def insertWord(word, translation, type, example):
        cursor.execute("INSERT OR REPLACE INTO custom_words (word, translation, type, example) VALUES (?, ?, ?, ?)", (word.strip(), translation.strip(), type.strip(), example.strip()))
        conn.commit()

    @staticmethod
    def getWord():
        cursor.execute("SELECT * FROM custom_words")
        result = cursor.fetchall()
        return result
    

    @staticmethod
    def getWordByName(name):
        cursor.execute("SELECT * FROM custom_words WHERE word=?", (name,))
        result = cursor.fetchone()
        return result
    
    @staticmethod
    def deleteWord(name):
        cursor.execute("DELETE FROM custom_words WHERE word = ?", (name, ))
        conn.commit()
        return cursor.rowcount > 0