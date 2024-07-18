customer = {'name': 'Ahmet', 'surname': 'Çelik', 'age': 25,
'account_balance': 1200.0}

print("""
adı güncellemek ya da silmek için: name
soyadı güncellemek ya da silmek için: surname
yası guncellemek ya da silmek için: age
parayı guncellemek ya da silmek için: balance""")

while True:
    islem = input("guncellemek için: g, silmek için: s girin, çıkmak için q girin: ")

    if islem == 'g':
        guncelle = input("guncellenecek değer gir: ")
        if guncelle == "name":
            customer["name"] = input(f"su anki ad: {customer["name"]} yeni ad girin: ")
            print(customer["name"])
        elif guncelle == "surname":
            customer["surname"] = input(f"su anki soyad {customer["surname"]} yeni soyad girin: ")
            print(customer["surname"])
        elif guncelle == "age":
            customer["age"] = int(input(f"su anki yas: {customer["age"]} yeni yas: "))
            print(customer["age"])
        elif guncelle == "balance":
            customer["account_balance"] = float(input(f"su anki bakiye {customer["account_balance"]} yeni bakiye girin: "))
            print(customer["account_balance"])
        else:
            print("hatalı tuslama")
    elif islem == 's':
        sil = input("silenecek değer gir: ")

        if sil == "name":
            del customer["name"]
            print("name silindi")
        elif sil == "surname":
            del customer["surname"]
            print("surname silindi")
        elif sil == "age":
            del customer["age"]
            print("yaş silindi")
        elif sil == "balance":
            del customer["account_balance"]
            print("balance silindi")
        else:
            print("hatalı tuslama")
    elif islem == "q":
        print("program sonlanıyor")
        break
    else:
        print("hatalı tuslama")