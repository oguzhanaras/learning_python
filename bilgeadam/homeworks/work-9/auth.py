import sqlite3
from contextlib import contextmanager
import hashlib


current_user = None


@contextmanager
def db_connection():
    conn = sqlite3.connect("flight_reservation.db")
    try:
        yield conn
    finally:
        conn.close()


def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def register(username, password):
    with db_connection() as conn:
        cursor = conn.cursor()
        hashed_password = hash_password(password)
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            print(f"Kullanıcı {username} başarıyla kayıt oldu.")
        except sqlite3.IntegrityError:
            print("Bu kullanıcı adı zaten mevcut.")


def login(username, password):
    global current_user
    with db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user and hash_password(password) == user[2]:
            current_user = user
            print("Başarıyla giriş yapıldı.")
            return True
        else:
            print("Giriş başarısız.")
            return False


def is_logged_in():
    return current_user is not None


def logout():
    global current_user
    current_user = None
    print("Çıkış yapıldı.")
