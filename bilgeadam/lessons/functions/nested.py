def outer_func(arg_outer):
    def inner_func(arg_inner):
        return arg_outer + arg_inner

    return inner_func

x = outer_func(5)
print(x(7))



# Bir kafe sipariş sistemi oluşturalım. Menüde yiyecek ve içecek seçenekleri olacak.
# Yiyecek için ayrı bir menü, içecek için ayrı bir menü olacak.
# Müşteri siparişi tamamladığında toplam tutar hesaplanacak.

# Yiyecek Menü: Burger: 250 TL, Pizza: 300 TL
# İçecek Menü: Kola: 50 TL, Ayran: 40 TL

def siparis_sistemi():
    print("Bizim Cafe sipariş sistemine hoş geldiniz.")

    def yiyecek_menu():
        print("Yiyecek Menüsü:")
        print("1-Burger: 250 TL")
        print("2-Pizza : 300 TL")
        yiyecek_secim = int(input("Yiyecek seçimi yapınız: "))
        if yiyecek_secim == 1:
            print("Burger: 250 TL sepete eklendi.")
            return "Burger", 250
        elif yiyecek_secim == 2:
            print("Pizza: 300 TL sepete eklendi.")
            return "Pizza", 300
        else:
            print("Geçersiz seçim")
            return 0
    def icecek_menu():
        print("İçecek Menüsü:")
        print("1-Kola : 50 TL")
        print("2-Ayran: 40 TL")
        icecek_secim = int(input("İçecek seçimi yapınız: "))
        if icecek_secim == 1:
            print("Kola: 50 TL sepete eklendi.")
            return 50
        elif icecek_secim == 2:
            print("Ayran: 40 TL sepete eklendi.")
            return 40
        else:
            print("Geçersiz seçim")
            return 0

    toplam = 0
    secimler = {}

    while True:
        print("Ana Menü:")
        print("1-Yiyecek Menüsü")
        print("2-İçecek Menüsü")
        print("3-Çıkış")
        ana_secim = int(input("Lütfen alt menü seçiminizi yapınız:"))
        if ana_secim == 1:
            yiyecek_ismi, yiyecek_fiyat = yiyecek_menu()
            toplam += yiyecek_fiyat
            secimler[yiyecek_ismi] = 1
        elif ana_secim == 2:
            toplam += icecek_menu()
        elif ana_secim == 3:
            print(secimler)
            print(f"Toplam ödemeniz gereken tutar: {toplam} TL")
            break
        else:
            print("Geçerli bir seçimde bulununuz.")
    print("Bizi tercih ettiğiniz için teşekkürler. Yine bekleriz.")


siparis_sistemi()