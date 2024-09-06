import sqlite3


def create_connection():
    return sqlite3.connect('flight_reservation.db')


def create_tables():
    with create_connection() as conn:
        cursor = conn.cursor()

        # KULLANICILAR TABLOSU
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL
                          )''')

        # UCUSLAR TABLOSU
        cursor.execute('''CREATE TABLE IF NOT EXISTS flights (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            airline TEXT NOT NULL,
                            departure_city TEXT NOT NULL,
                            arrival_city TEXT NOT NULL,
                            departure_time TEXT NOT NULL,
                            arrival_time TEXT NOT NULL,
                            price INTEGER NOT NULL
                          )''')

        # REZERVASYON TABLOSU
        cursor.execute('''CREATE TABLE IF NOT EXISTS reservations (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            flight_id INTEGER NOT NULL,
                            reservation_date TEXT NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES users (id),
                            FOREIGN KEY (flight_id) REFERENCES flights (id)
                          )''')

        conn.commit()
