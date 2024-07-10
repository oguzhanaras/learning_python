# fonksiyon tarafından alınan değere parametre denir

def selamla(isim):
    print(f"selam {isim}")

selamla("oguzhan")


selamla() # parametre bekleyen fonksiyona değer gonderilmezse hata verir


def varsayilan(deger = "varsayilan deger"): # parametreye varsayılan değer girebiliriz
    print(deger)

varsayilan() # varsayılan değer giriliyse parametre yollamazsak varsayılan değeri ele alır
varsayilan("aras") # eğer parametre yollarsak varsayılan değeri ezer ve gönderilen değer programda calistirilir


def bilgiler(ad = "bilgi yok", soyad = "bilgi yok", numara = "bilgi yok"):
    print(ad, soyad, numara)

bilgiler("aras") # ad kısmına aras değerini gönderir ve geri kalanı default olarak ele alır
bilgiler(numara = "151512122") # sadece istenilen parametreye deger gonderme


def toplama(*a): #parametre basına * koyunda birden çok değer alabilir ve tuple olarak işleme alır
    print(a)

toplama(1,2,3,4)