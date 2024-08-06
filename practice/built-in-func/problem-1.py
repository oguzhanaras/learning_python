#Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.
#Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın
kenarlar = [(3, 4), (10, 3), (5, 6), (1, 9)]


def alan(item):
    return item[0] * item[1]


print(list(map(alan, kenarlar)))