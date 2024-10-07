import sqlite3

# db connect and create table
conn = sqlite3.connect('music.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS music (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    singer TEXT,
    album TEXT,
    production TEXT,
    duration INTEGER
    )
""")

conn.commit()
conn.close()


class Music:

    def __init__(self, name=None, singer=None, album=None, production=None, duration=None):
        self.name = name
        self.singer = singer
        self.album = album
        self.production = production
        self.duration = duration

    def add_music(self):
        self.name = input("Müzik adı giriniz: ")
        self.singer = input("Şarkıcı adı giriniz: ")
        self.album = input("Albüm adı giriniz: ")
        self.production = input("Prodüksiyon adı giriniz: ")
        self.duration = int(input("Şarkı süresini dakika biçiminde girin: "))

        conn = sqlite3.connect('music.db')
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO music (name, singer, album, production, duration)
        VALUES (?, ?, ?, ?, ?)
        """, (self.name, self.singer, self.album, self.production, self.duration))

        conn.commit()
        conn.close()
        print("Şarkı başarıyla eklendi.")

    @staticmethod
    def delete_music():
        music_id = int(input("Silmek istediğiniz şarkının ID'sini girin: "))

        conn = sqlite3.connect('music.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM music WHERE id = ?", (music_id,))

        if cursor.rowcount > 0:
            print("Şarkı başarıyla silindi.")
        else:
            print("Belirtilen ID'ye sahip şarkı bulunamadı.")

        conn.commit()
        conn.close()

    @staticmethod
    def calculate_total_duration():
        conn = sqlite3.connect('music.db')
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(duration) FROM music")
        total_duration = cursor.fetchone()[0]

        conn.close()

        if total_duration:
            print(f"Veritabanındaki toplam şarkı süresi: {total_duration} dakika.")
        else:
            print("Veritabanında hiç şarkı bulunmuyor.")

    def __str__(self):
        return f"Müzik: {self.name}, Şarkıcı: {self.singer}, Albüm: {self.album}, Prodüksiyon: {self.production}, Süre: {self.duration} dakika"
