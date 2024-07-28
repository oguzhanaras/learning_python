# username listesi oluşturun.
# password listesi oluşturun.
# sign_up() - kayit() isimli fonksiyon yazın, bu fonksiyonun 2 argumanı olsun: userName, userPassword
# sign_in() - giris() isimli fonksiyon yazın, bu fonksiyonun 2 argumanı olsun: userName, userPassword
#                     eğer kullanıcı username listesi ve password listesindeki bilgileri
#                     doğru girerse "Welcome" yazdırsın. Diğer durumda 'hatalı giriş' yazdırsın.


# döngü oluşturun, kullanıcıdan input isteyelim: (K)ayıt / (G)iriş / (Ç)ıkış
# Kayıt yapmak isterse kullanıcıdan alınan kayıt bilgilerini listelere yazdıralım
# Giriş yapmak isterse kullanıcıdan alınan username ve password'e göre sisteme giriş yapıp
# yapamayacağı yazdırılsın.
# Hatalı girişlerde döngü doğru girişe kadar devam etsin.

import accs

secim = input("(K)ayıt / (G)iris / (C)ıkıs")

while True:
    if secim == "k":
        print("kayıt sayfasına hos geldiniz")
        kullanici_adi = input("kullanıcı adı gir: ")
        sifre = input("sifre: ")
        accs.kayit(kullanici_adi, sifre)
        accs.giris(kullanici_adi, sifre)
    elif secim == "g":
        print(f"giriş sayfasına hos geldiniz")
        kullanici_adi = input("kullanıcı adi: ")
        sifre = input("sifre: ")
        giris = accs.giris(kullanici_adi, sifre)
        if giris:
            secim = input("(ç)ıkış")
        else:
            secim = input("(g)iris / (c)ıkıs")
    elif secim == "c":
        print("baybay")
        break
    else:
        print("hatalı tercih yaptınız")