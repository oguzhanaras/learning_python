import sqlite3

# verilen değerde db varsa baglanir yoksa olusturur
connect = sqlite3.connect("db/kutuphane.db")

cursor = connect.cursor()

def tablo_olustur():

    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (isim TEXT, yazar TEXT, yayin_evi TEXT, sayfa_sayisi INT)")
    connect.commit()

def veri_ekle():
    cursor.execute("INSERT INTO kitaplik VALUES('istanbul hatirasi', 'ahmet umit', 'everest', 561)")
    connect.commit()

def kullanici_veri_ekle(isim, yazar, yayin_evi, sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplik VALUES(?, ?, ?, ?)", (isim, yazar, yayin_evi, sayfa_sayisi))
    connect.commit()
    print("kitap basariyla eklendi")

def verileri_al():
    cursor.execute("SELECT * FROM kitaplik")
    kitaplar = cursor.fetchall()

    for i in kitaplar:
        print(i)

def yazarlar():
    cursor.execute("SELECT yazar FROM kitaplik")
    yazarlar = cursor.fetchall()

    for i in yazarlar:
        print(i)

def ait_kitaplar(yayin_evi):
    cursor.execute("SELECT * FROM kitaplik WHERE yayin_evi = ?", (yayin_evi,))
    kitaplar = cursor.fetchall()

    if kitaplar:
        for i in kitaplar:
            print(i)
    else:
        print("bu yayınevine ait kitap yok")

def veri_guncelle(eski_yayinevi, yeni_yayinevi):
    cursor.execute("UPDATE kitaplik SET yayin_evi = ? WHERE yayin_evi = ?", (yeni_yayinevi, eski_yayinevi))
    connect.commit()
    print("yayınevi guncellendi")

def veri_sil(yazar):
    cursor.execute("DELETE FROM kitaplik WHERE yazar = ?", (yazar,))
    connect.commit()
    print("yazara ait kitaplar silindi")


# tablo_olustur()
#
# veri_ekle()

while True:
    islem = input("""
    kitap eklemek icin 'add',
    tum kitap verilerini gormek icin 'all',
    yazarları gormek için 'writer',
    yayınevine gore kitapları goruntulemek için 'ykitap',
    yayınevini yeni yayınevi değerine guncellemek için 'updateyayin'
    yazara ait kitaplari silmek için 'yazarsil',
    cıkmak icin 'q'
    yazın
    """)

    if islem == "q":
        print("program sonlanıyor")
        break
    elif islem == "add":
        isim = input("kitabın adını girin: ")
        yazar = input("yazar adı girin: ")
        yayin_evi = input("yayın evi adını girin: ")
        sayfa_sayisi = int(input("sayfa sayısını girin: "))
        kullanici_veri_ekle(isim, yazar, yayin_evi, sayfa_sayisi)
    elif islem == "all":
        verileri_al()
    elif islem == "writer":
        yazarlar()
    elif islem == "ykitap":
        yayin_evi = input("yayınevi adı girin: ")
        ait_kitaplar(yayin_evi)
    elif islem == "updateyayin":
        eski = input("değiştirmek istediğiniz yayinevini girin: ")
        yeni = input("yeni yeyınevini girin: ")
        veri_guncelle(eski, yeni)
    elif islem == "yazarsil":
        yazar = input("kitaplarını silmek istediğiniz ayzar adı girin: ")
        veri_sil(yazar)
    else:
        print("yanlis islem tuslamasi")


# baglantıyı kapatır
connect.close()

