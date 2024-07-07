sayi = int(input("sayi giriniz: "))
toplam = 0

for i in range(1, sayi):
    if sayi % i == 0:
        toplam += i

if toplam == sayi:
    print("perfect number")
else:
    print("not perfect number")