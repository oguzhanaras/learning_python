# veritabanında tabloya yeni bir veri ekleme
import sqlite3

conn = sqlite3.connect("user_info.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO users (username, email, age) VALUES (?, ?, ?)", ("aras", "aras6161@ts.com", 35))

conn.commit()
conn.close()


conn = sqlite3.connect("user_info.db")
cursor = conn.cursor()


sql_query = "INSERT INTO users (username, email, age) VALUES (?, ?, ?)"
user_data = [
    ("muslera", "muslera1@gs.com", 37),
    ("arda", "arda15@real.com", 19),
    ("modric", "modric10@real.com", 39),
    ("immobile", "immobile19@bjk.com", 28)
]

cursor.executemany(sql_query, user_data)
conn.commit()
conn.close()


# adduser func
def add_user(username, email, age):
    try:
        import sqlite3
        conn = sqlite3.connect("user_info.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, age) VALUES (?, ?, ?)",
                       (username, email, age))
        conn.commit()
        conn.close()
        print("kullanıcı taboya eklendi")
        return True
    except:
        print("kullanıcı taboya eklenirken hata")
        return False


add_user("mbappe", "mbappe9@real.com", 25)
add_user("haaland", "haaland9@mnchstr@.com", 21)
