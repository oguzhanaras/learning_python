import time

from kutuphane import *

print("""********************
kutuphane programına hosgeldiniz
islemler;
1. kıtapları goster
2. kitap sorgula
3. kitap ekle
4. kitap sil
5. baskı yukselt

cıkmak icin 'q' ya basın..
************************""")

kutuphane = Kutuphane()


while True:
    islem = input("yapmak istediginiz islemi secin: ")

    if islem == "q":
        print("program sonlanıyor..")
        break
    elif islem == "1":
        kutuphane.kitaplari_goster()
    elif islem == "2":
        isim = input("hangi kitabı istiyorsunuz: ")
        print("kitap sorgulanıyor...")
        time.sleep(2)

        kutuphane.kitap_sorgula(isim)
    elif islem == "3":
        isim = input("isim: ")
        yazar = input("yazar: ")
        yayin_evi = input("yayınevi: ")
        tur = input("tür: ")
        baski = int(input("baskı: "))

        yeni_kitap = Kitap(isim, yazar, yayin_evi, tur, baski)

        print("kitap ekleniyor..")
        kutuphane.kitap_ekle(yeni_kitap)
        time.sleep(2)
        print("kitap basariyla eklendi...")
    elif islem == "4":
        isim = input("silmek istediginiz kitabın adını yazın: ")

        cevap = input("emin misiniz? e/h")

        if cevap == "e":
            print("kitap siliniyor..")
            kutuphane.kitap_sil(isim)
            time.sleep(2)
            print("kitapbasariyla silindi")
    elif islem == "5":
        isim = input("hangi kıtabın baskı sayısını yukseltmek istiyorsunuz?")

        print("baskı sayısı artırılıyor")
        kutuphane.baski_yukselt(isim)
        time.sleep(2)
        print("baskı yukseltildi")
    else:
        print("hatalı tuslama")











