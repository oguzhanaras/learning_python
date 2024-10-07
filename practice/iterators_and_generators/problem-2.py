def asal_sayilar():
    for sayi in range(2, 1001):
        for i in range(2, int(sayi ** 0.5) + 1):
            if sayi % i == 0:
                break
        else:
            yield sayi


for asal in asal_sayilar():
    print(asal)
