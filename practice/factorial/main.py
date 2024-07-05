print("""*****************
faktoriyel bulma programı
press q to exit
*****************""")

while True:
    sayi = input("sayı gir: ")
    fac = 1
    if sayi == "q":
        print("bye")
        break
    elif sayi < "0":
        print("lütfen negatif değer girmeyin")
    else:
        sayi = int(sayi)
        for i in range(1, int(sayi) + 1):
            fac *= i
        print(fac)
