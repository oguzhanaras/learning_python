def toplama(a, b, c):
    toplam = a + b + c
    print(toplam)
    return toplam # toplam degiskenini geri döndürür ve baska yerde kullanmamızı saglar

def ikiyleCarp(sayi):
    carpim2 = sayi * 2
    return carpim2

x = toplama(2, 3, 4)
print(ikiyleCarp(x))


def cikarma(a, b):
    x = a - b
    return x
    print("hello") # calismaz cunku returnden sonra programdan cıkar