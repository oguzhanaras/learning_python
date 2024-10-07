def mukemmel_sayi_bul(func):
    def wrapper():
        print("mukemmler sayılar")
        for i in range(1, 1001):
            toplam = 0
            for bolen in range(1, i):
                if i % bolen == 0:
                    toplam += bolen
            if toplam == i:
                print(i)
        print("asal sayılar")
        func()
    return wrapper


@mukemmel_sayi_bul
def asal():
    for i in range(2, 1000):
        is_prime = True
        for mod in range(2, i // 2 + 1):
            if i % mod == 0:
                is_prime = False
                break
        if is_prime:
            print(i)


asal()
