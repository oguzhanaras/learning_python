def add_member(uye_adi, uye_email, uye_yas):
    """
    bu fonksiyon kutuphane uygulamasında uye eklemeyi saglar
    :param uye_adi:
    :param uye_email:
    :param uye_yas:
    :return: Bool
    """

    import sqlite3

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    sql = "INSERT INTO members (member_name, email, age) VALUES (?, ?, ?)"
    parameters = (uye_adi, uye_email, uye_yas)

    cursor.execute(sql, parameters)
    conn.commit()
    conn.close()

    return True


def member_list():
    import sqlite3

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    sql = "SELECT * FROM members"

    cursor.execute(sql)
    uyeler = cursor.fetchall()
    conn.close()

    return uyeler


def add_book(kitap_adi, yazar, yayin_yili):
    import sqlite3

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    sql = "INSERT INTO books (book_name, author, year_of_book) VALUES (?, ?, ?)"
    parameters = (kitap_adi, yazar, yayin_yili)

    cursor.execute(sql, parameters)
    conn.commit()
    conn.close()

    return True


def show_books():
    import sqlite3

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    sql = "SELECT * FROM books"
    cursor.execute(sql)

    kitaplar = cursor.fetchall()
    conn.close()

    return kitaplar


def lenad_book(uye_id, kitap_id):
    import sqlite3
    from datetime import datetime

    zaman_damgasi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    sql = "INSERT INTO borrows (member_id, book_id, borrow_date) VALUES (?, ?, ?)"
    params = (uye_id, kitap_id, zaman_damgasi)

    cursor.execute(sql, params)
    conn.commit()
    conn.close()

    return True


def delivery_book(uye_id, kitap_id):
    import sqlite3
    from datetime import datetime

    zaman_damgasi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    sql = "UPDATE borrows SET delivery_date = ? WHERE member_id = ? AND book_id = ?"
    params = (zaman_damgasi, uye_id, kitap_id)

    cursor.execute(sql, params)
    conn.commit()
    conn.close()

    return True

