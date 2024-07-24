def tax(price):
    if price <= 0:
        raise TypeError
    elif price < 500:
        print(price + (price * 5 / 100))
    elif 500 <= price < 1000:
        print(price + (price * 10 / 100))
    else:
        print(price + (price * 20 / 100))


while True:
    islem = input("fiyat gir ya da cıkmak için q bas")
    if islem == 'q':
        print("program sonlanıyor")
        break
    try:
        tax(int(islem))
    except TypeError:
        print("0 dan buyuk değer giriniz")

