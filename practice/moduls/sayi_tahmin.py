import random
import time

print("""
sayı tahmın oyunu
1-40 arasındaki sayıyı tahmin et. 7 hakkın var!
""")

rast_sayi = random.randint(1, 40)
kalan_hak = 7

while True:
    sayi = int(input("Sayi gir : "))
    if sayi > rast_sayi:
        kalan_hak -= 1
        print("kontrol ediliyor...")
        time.sleep(1)
        print("daha kucuk deger gir. kalan hak: ", kalan_hak)
    elif sayi < rast_sayi:
        kalan_hak -= 1
        print("kontrol ediliyor...")
        time.sleep(1)
        print("daha buyuk deger gir. kalan hak: ", kalan_hak)
    else:
        print("kontrol ediliyor...")
        time.sleep(1)
        print("dogru bildiniz. sayımız: ", sayi)
        break

    if kalan_hak == 0:
        print("hakkınız bitti.. sayımız: ", sayi)
        break