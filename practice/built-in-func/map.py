# map fonksiyonu ilk parametre olarak bir fonksiyon, ikinci parametre olarak bir iterasyon yapılabilen veri tipi alır
def double(x):
    return x * 2

print(map(double, [1, 2, 3, 4])) # burda ekrana map obje yazar. listeye cevirip kullanabiliriz

print(list(map(double, [1, 2, 3, 4])))

#lambda ile kullanımı

print(list(map(lambda x: x * 2, [1, 2, 3, 4, 5])))

# unpacking ve coklu liste kulanımı
liste1 = [1, 5, 7, 9]
liste2 = [8, 12, 7, 13]
liste3 = [6, 8, 9, 10, 12]

# x y z her iterasyon için listelerin elemanlarına eşitlenir ve carpılır.
# herhagi bir listenin elemanı eksikse orayı işleme almaz.
# ornegin liste3 5 elemanlı diğerleri 4. bu yuzden 4 kere islem yapar
print(list(map(lambda x, y, z: x * y * z, liste1, liste2, liste3)))
