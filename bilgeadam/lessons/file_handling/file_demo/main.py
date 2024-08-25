import time

from web_logger import WebLogger, KullaniciOturumu


def main():
    logger = WebLogger("oturum_kayit.txt")

    print("Oturum Yönetim Sistemine Hoşgeldiniz!")

    username = input("Kullanıcı Adı: ")
    password = input("Şifre: ")

    # Kullanıcı oturum nesnesi oluşturun
    oturum = KullaniciOturumu(logger, username, password)

    while True:
        print("\nSeçenekler:")
        print("1. Giriş Yap\n2. Çıkış Yap\n 3. Programı Sonlandır")

        secim = input("Bir seçenek belirtin (1/2/3): ")

        if secim == "1":
            kullanici_adi = input("Kullanıcı adınızı giriniz: ")
            sifre = input("Şifrenizi giriniz: ")
            print("Giriş yapılıyor...")
            time.sleep(2)
            oturum.giris_yap(kullanici_adi, sifre)
        elif secim == "2":
            print("Çıkış yapılıyor...")
            time.sleep(2)
            oturum.cikis_yap()
        elif secim == "3":
            print("Programdan çıkılıyor...")
            time.sleep(2)
            break
        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    main()