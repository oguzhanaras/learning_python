import sqlite3
from contextlib import contextmanager
import auth
from datetime import datetime


@contextmanager
def db_connection():
    conn = sqlite3.connect("flight_reservation.db")
    try:
        yield conn
    finally:
        conn.close()


def show_flights(from_where, where):
    with db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT * FROM flights WHERE departure_city = ? AND arrival_city = ?",
                (from_where, where)
            )
            flights = cursor.fetchall()
            if flights:
                return flights
            else:
                print("Uçuş bulunamadı.")
                return None
        except sqlite3.DatabaseError as e:
            print(f"Uçuşlar gösterilirken hata meydana geldi: {e}")
            return None


def reservation(pick_fly):
    if not pick_fly.isdigit():
        print("Geçerli bir uçuş numarası girin.")
        return

    user = auth.current_user
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with db_connection() as conn:
        cursor = conn.cursor()
        try:
            params = (user[0], pick_fly, now)
            cursor.execute(
                "INSERT INTO reservations (user_id, flight_id, reservation_date) VALUES (?, ?, ?)",
                params
            )
            conn.commit()
            print("Rezervasyon başarılı!")
        except sqlite3.DatabaseError as e:
            print(f"Rezervasyon yapılırken hata meydana geldi: {e}")


def show_reservation():
    with db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM reservations WHERE user_id = ?", (auth.current_user[0],))
            reservations = cursor.fetchall()
            if reservations:
                return reservations
            else:
                print("Rezervasyon bulunamadı.")
                return None
        except sqlite3.DatabaseError as e:
            print(f"Rezervasyon bilgisi alınırken hata meydana geldi: {e}")
