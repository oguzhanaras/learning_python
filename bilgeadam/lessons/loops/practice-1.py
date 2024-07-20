numbers = [1, 3, 5, 7, 9, 12, 18, 21, 26]
ucun_katlari = []
for i in numbers:
    if i % 3 == 0:
        ucun_katlari.append(i)
print(ucun_katlari)

toplam = 0
for i in numbers:
    if i % 2 == 1:
        toplam += i
print(toplam)


ucun_kati = [i for i in numbers if i % 3 == 0]


# list of dictionaries
products = [
    {"name": "samsung S6", "price": 3000, "quantity": 5},
    {"name": "samsung S7", "price": 4000, "quantity": 4},
    {"name": "samsung S8", "price": 4800, "quantity": 3},
    {"name": "samsung S9", "price": 6000, "quantity": 2},
]

# 4. Alıştırma: Ürünlerin fiyatlarının toplamı nedir?
toplam = 0
for i in products:
    toplam += (i["price"] * i["quantity"])

print(toplam)



# 5. Alıştırma: Ürünler içerisinde 3500 dolardan pahalı ürünleri yazdırınız.
for i in products:
    if i["price"] > 3500:
        print(i["name"])


