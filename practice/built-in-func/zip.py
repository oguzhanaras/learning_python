liste1 = [1, 2, 3, 4, 5]
liste2 = [2, 4, 6, 8, 10, 12]

i = 0
sonuc = []
while i < len(liste1) and i < len(liste2):
    sonuc.append((liste1[i], liste2[i]))
    i += 1
print(sonuc)

# iki listeyi tuple lar olarak eşler ve zip objesi dondurur
print(list(zip(liste1, liste2)))


for i, j in zip(liste1, liste2):
    print(i, j)