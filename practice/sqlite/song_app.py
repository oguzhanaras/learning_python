import sqlite3

# db connect
conn = sqlite3.connect('music.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS music (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    music_type TEXT,
    duration INTEGER
    )
""")


class Music:

    def __init__(self, name, music_type, duration):
        self.name = name
        self.music_type = music_type
        self.duration = duration

    def add_music(self):
        pass

    def delete_music(self):
        pass

    def __str__(self):
        return "bu bir muzik sınıfıdır. ad tip ve suresini icerir."


