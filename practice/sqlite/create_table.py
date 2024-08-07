import sqlite3

# verilen değerde db varsa baglanir yoksa olusturur
connect = sqlite3.connect("db/kutuphane.db")

cursor = connect.cursor()

def tablo_olustur():

    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (isim TEXT, yazar TEXT, yayin_evi TEXT, sayfa_sayisi INT)")
    connect.commit()

tablo_olustur()

# baglantıyı kapatır
connect.close()

