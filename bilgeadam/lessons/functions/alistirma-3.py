# Alıştırma 3: Bir sayıyı parametre olarak alan ve bu sayının asal olup olmadığını kontrol eden bir Python fonksiyonu yazınız.
#Not: Bir asal sayı, 1'den büyük olan ve 1 ve kendisi dışında pozitif böleni olmayan doğal sayıdır.


def asal(sayi):
    if sayi == 1:
        return "asal değil"
    if sayi == 2:
        return "asal"
    for i in range(2, sayi):
        if sayi % i == 0:
            return "asal değil"
    return "asal"


print(asal(4))
print(asal(5))
print(asal(3))
print(asal(21))
