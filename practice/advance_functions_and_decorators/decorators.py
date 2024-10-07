import time


def zaman_hesapla(func):
    def wrapper(sayilar):
        basla = time.time()
        sonuc = func(sayilar)
        bitis = time.time()

        print(func.__name__ + " " + str(bitis - basla) + " saniye sürdü")
        return sonuc
    return wrapper


@zaman_hesapla
def kareleri_hesapla(sayilar):
    sonuc = list()
    for i in sayilar:
        sonuc.append(i ** 2)
    return sonuc


@zaman_hesapla
def kupleri_hesapla(sayilar):
    sonuc = list()
    for i in sayilar:
        sonuc.append(i ** 3)
    return sonuc


kareler = kareleri_hesapla(range(1, 100000))
kupler = kupleri_hesapla(range(1, 100000))


print("Karelerin ilk 10 elemanı:", kareler[:10])
print("Küplerin ilk 10 elemanı:", kupler[:10])
