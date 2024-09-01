import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# kitaplar tablosu (kitap adı, yazar, yayın yılı)
books_sql = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        book_name TEXT NOT NULL,
        author TEXT NOT NULL,
        year_of_book INTEGER
    )
"""

cursor.execute(books_sql)

members_sql = """
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY,
        member_name TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER
    )
"""

cursor.execute(members_sql)

# odunc islem
borrow_sql = """
    CREATE TABLE IF NOT EXISTS borrows (
        id INTEGER PRIMARY KEY,
        member_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        borrow_date TEXT NOT NULL,
        delivery_date TEXT,
        FOREIGN KEY(member_id) REFERENCES members(id),
        FOREIGN KEY(book_id) REFERENCES books(id)
    )
"""

cursor.execute(borrow_sql)

cursor.close()

