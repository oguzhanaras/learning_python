import random

hak = 5
sayi = random.randint(1, 100)
while True:
    try:
        if hak > 0:
            tahmin = int(input(f"1-100 arasında bir sayı tahmin ediniz: "))
            if 0 <= tahmin <= 100:
                if tahmin == sayi:
                    print(f"doğru bildiniz.. sayımız: {sayi}")
                    break
                elif tahmin > sayi:
                    hak -= 1
                    print(f"daha kucuk bir sayı giriniz.. kalan hak: {hak}")
                elif tahmin < sayi:
                    hak -= 1
                    print(f"daha buyuk bir sayı giriniz.. kalan hak: {hak}")
            else:
                print("lutfen 1-100 arasında bir sayı girin")
        else:
            print(f"hakkınız biti... dogru sayımız: {sayi}")
            break
    except:
        print("lütfen doğru formatta sayı giriniz")

