liste1 = ["elma", "armut", "karpuz"]

i = 0
sonuc = []

while i < len(liste1):
    sonuc.append((i, liste1[i]))
    i += 1

print(sonuc)
# listenin elemanlarını indeksiyle beraber liste içinde tuple olarak saklar

print(list(enumerate(liste1)))


liste2 = ["a", "b", "c", "d", "e", "f", "g"]

# indeksi çift olan liste elemanlarını yazdırır
for i, j in enumerate(liste2):
    if i % 2 == 0:
        print(j)