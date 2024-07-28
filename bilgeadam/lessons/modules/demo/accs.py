kullanicilar = ["ali", "veli"]
sifreler = ["123456", "1234567"]
def kayit(kullanici_adi, sifre):
    kullanicilar.append(kullanici_adi)
    sifreler.append(sifre)
    print("kayıt basarılı")

def giris(kullanici_adi, sifre):
    if kullanici_adi in kullanicilar:
        pozisyon = kullanicilar.index(kullanici_adi)
        if sifreler[pozisyon] == sifre:
            print(f"kullanici: {kullanici_adi} giriş yaptı")
            return True
        else:
            print("kullanıcı adı veya parola yanlıs")
            return False
    else:
        print("kullanıcı adı veya parola yanlıs")
        return False