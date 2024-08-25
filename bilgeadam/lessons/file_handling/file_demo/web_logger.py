# web_logg


import hashlib
import secrets
from datetime import datetime


class WebLogger:
    def __init__(self, dosya_adi):
        self.dosya_adi = dosya_adi

    def olay_kaydet(self, kullanici_adi, olay):
        with open(self.dosya_adi, "a", encoding="utf-8") as file:
            zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{zaman}]{kullanici_adi} - {olay}\n")


class KullaniciOturumu:
    def __init__(self, logger: WebLogger, kullanici_adi, sifre):
        self.logger = logger       # kaydedici nesne
        self.kullanici_adi = kullanici_adi
        self.salt = secrets.token_hex(16)      # rastgele tuz oluşturur
        self.sifre = self.__sifre_hashle(sifre)     # hashlenmiş şifre
        self.logged_in = False    # Kullanıcının oturumu aktif mi?

    def __sifre_hashle(self, sifre):
        salted_sifre = sifre + self.salt
        hashed_sifre = hashlib.sha256(salted_sifre.encode()).hexdigest()
        return hashed_sifre

    def giris_yap(self, kullanici_adi, giris_sifre):
        if not self.logged_in:
            if kullanici_adi == self.kullanici_adi and self.__sifre_dogrula(giris_sifre):
                print(f"{kullanici_adi} başarıyla giriş yaptı.")
                self.logged_in = True
                self.logger.olay_kaydet(self.kullanici_adi, "giriş yaptı.")
            else:
                print("Hatalı giriş.")
                self.logger.olay_kaydet(self.kullanici_adi, "hatalı giriş denemesi yaptı.")
        else:
            print(f"{kullanici_adi} önceden giriş yaptı.")

    def __sifre_dogrula(self, giris_sifre):
        salted_giris_sifre = giris_sifre + self.salt
        hashed_giris_sifre = hashlib.sha256(salted_giris_sifre.encode()).hexdigest()
        return hashed_giris_sifre == self.sifre

    def cikis_yap(self):
        if self.logged_in:
            print(f"{self.kullanici_adi} başarıyla çıkış yaptı.")
            self.logged_in = False
            self.logger.olay_kaydet(self.kullanici_adi, "çıkış yaptı.")
        else:
            print("Giriş yapmalısınız.")


print("1" == 1)