from functools import reduce

# reduce sonraki surumlerde functools modulune tasındıgı ıcın import ediyoruz
# reduce kumilatif yani birike birike toplama yapar ve islem bitince tek bir değeri dondurur
# reduce ilk 2 elemanı alır fonksiyonu uygular daha sonra sonuc ile sonraki elemanı alır ve tekrar uygular
def toplama(x, y):
    return x + y

print(reduce(toplama, [12, 18, 20, 10]))

print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))