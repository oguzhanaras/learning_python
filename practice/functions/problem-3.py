# Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.
from functools import reduce
import operator
def ekok(sayi1, sayi2):
    i = 2
    bolenler = []
    while True:
        if sayi1 % i == 0 or sayi2 % i == 0:
            if sayi1 % i == 0 and sayi2 % i == 0:
                sayi1 /= i
                sayi2 /= i
                bolenler.append(i)
            elif sayi1 % i == 0:
                sayi1 /= i
                bolenler.append(i)
            else:
                sayi2 /= i
                bolenler.append(i)
        else:
            i += 1
        if i == 100:
            break
    ekok = [x for x in bolenler]
    print("sonuc: ", reduce(operator.mul, bolenler))


ekok(12, 24)
