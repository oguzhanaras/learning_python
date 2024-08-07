#Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek
# ekrana isim ve soyisimleri *isimlere* göre sıralı bir şekilde yazdırmaya çalışın.

names = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]
surnames = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

full_names = list(zip(names, surnames))

full_names.sort()

for i, j in full_names:
    print(i, j)