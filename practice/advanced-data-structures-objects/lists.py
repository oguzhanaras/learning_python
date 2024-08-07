# listenin en sonuna eleman ekler

liste = [1, 2, 3, 4, 5]

liste.append(6)
liste.append("python")

print(liste)


# extend bir listeye başka bir listenin elemanlarını eklememizi saglar
liste.extend([10, 12])

print(liste)


# insert metodu belirtilen indekse eleman ekler
liste = [1, 2, 3, 4, 5]

liste.insert(2, "python")

print(liste)


# pop ici bos bırakklırsa en sondan eleman siler ve sildiği elemanı geriye dondurur
liste = [1, 2, 3, 4, 5]

liste.pop()

# indekse gore de eleman silebilir
liste.pop(1)

print(liste)


liste = ["python", "css", "javascript"]

# remove elemanın kendisine gore silme işlemi yapar yoksa hata dondurur
liste.remove("css")

print(liste)


liste = [1, 2, 3, 4, 4, 3, 5, 6, 7]

# verilen değeri liste içinde arar ve ilk bulduğu yerin indeksini dondurur
liste.index(3)

# aramaya hangi indeksten baslayacagını ikinci parametre olarak verebiliriz
liste.index(3, 4)


# listede verilen elemandan kac tane oldugunu dondurur
liste.count(3)


liste = [3, 5, 1, 2, 6]
# sayıları kucukten buyuge karkterleri alfabeye gore sıralar
liste.sort()

print(liste)

# reverse= true olursa buyukten kucuge sıralar
liste.sort(reverse=True)
print(liste)
