import math

print("""
hesap makinesi

toplama için : +
cıkartma için -
çarpma için: *
bolme için: /
faktoriyel için: !
mutlak değer için: mutlak
""")


while True:
    sayi = int(input("sayi giriniz: "))
    islem = input("işlem girin")

    if islem == "+":
        sayi2 = int(input("ikinci sayi giriniz: "))
        print(sayi + sayi2)
    elif islem == "-":
        sayi2 = int(input("ikinci sayi giriniz: "))
        print(sayi - sayi2)
    elif islem == "*":
        sayi2 = int(input("ikinci sayi giriniz: "))
        print(sayi * sayi2)
    elif islem == "/":
        sayi2 = int(input("ikinci sayi giriniz: "))
        print(sayi / sayi2)
    elif islem == "!":
        print(math.factorial(sayi))
    elif islem == "mutlak":
        print(math.fabs(sayi))
