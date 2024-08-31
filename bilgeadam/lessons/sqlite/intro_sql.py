import sqlite3  #sqlite adaptoru


# veritabanı baglantısı olusturma
connection = sqlite3.connect("user_info.db")

# bir cursor oluşturmak
cursor = connection.cursor()

# tablo olusturmak
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER
)
""")

# değişikleri kaydeder
connection.commit()

# baglantı kapama
connection.close()
