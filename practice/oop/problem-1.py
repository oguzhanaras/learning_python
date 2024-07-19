class Bilgisayar():

    def __init__(self, durum="kapali", ram=16, internet="kapali", hiz=500):
        self.durum = durum
        self.ram = ram
        self.internet = internet
        self.hiz = hiz

    def bilgisayar_ac(self):
        if self.durum == "kapali":
            self.durum = "acik"
            print("bilgisayar acıldı")
        else:
            print("bilgisayar zaten acik")

    def bilgisayar_kapa(self):
        if self.durum == "acik":
            self.durum = "kapali"
            print("bilgisayar kapandı")
        else:
            print("bilgisayar zaten kapali")

    def ram_guncelle(self, ram_degeri):
        self.ram = ram_degeri
        print("ram guncellendi")

    def internet_guncelle(self, internet_durum):
        if internet_durum == "ac":
            if self.internet == "kapali":
                self.internet = "acik"
                print("internete baglanıldı")
            else:
                print("internet baglantısı zaten acik")
        elif internet_durum == "kapa":
            if self.internet == "acik":
                self.internet = "kapali"
                print("internet baglantısı kesildi")
            else:
                print("internet baglantısı zaten kapali")
        else:
            print("hatalı tuslama")

    def hiz_guncelle(self, hiz_degeri):
        self.hiz = hiz_degeri
        print("hiz guncellendi")

    def __str__(self):
        message = f"bilgisayar durumu: {self.durum}\nbilgisayar ram: {self.ram}\nbilgisayar internet: {self.internet}\nbilgisayar hiz: {self.hiz}"
        return message

bilgisayar1 = Bilgisayar()

print("""
çıkmak için 'q' basın....
1-bilgileri goster
2-bilgisayarı aç
3-bilgisayarı kapa
4-ram guncele
5-internete baglan ya da baglantıyı kes
6- bilgisayar hızı guncelle
""")
while True:
    islem = input("yapmak istediğiniz işlemi giriniz: ")
    if islem == "q":
        print("program sonlanıyor")
        break
    elif islem == "1":
        print(bilgisayar1)
    elif islem == "2":
        bilgisayar1.bilgisayar_ac()
    elif islem == "3":
        bilgisayar1.bilgisayar_kapa()
    elif islem == "4":
        while True:
            if bilgisayar1.durum == "acik":
                deger = int(input("yeni ram değerini girin: "))
                bilgisayar1.ram_guncelle(deger)
                break
            else:
                deger = input("bilgisayar kapalıyken bu işlemi yapamazsınız. açmak için 'y', diğer işlemlere geçmek için 'n' basın: ")
                if deger == "y":
                    bilgisayar1.bilgisayar_ac()
                    deger = int(input("yeni ram değerini girin: "))
                    bilgisayar1.ram_guncelle(deger)
                    break
                elif deger == "n":
                    break
                else:
                    print("hatalı tuslama")
    elif islem == "5":
        while True:
            deger = input("acmak için 'ac', kapatmak için 'kapa', cıkmak için q yazın: ")

            if deger == "q":
                break
            elif deger == "ac":
                if bilgisayar1.durum == "acik":
                    bilgisayar1.internet_guncelle(deger)
                    break
                else:
                    deger = input("bilgisayar kapalıyken bu işlemi yapamazsınız. bilgisayarı açmak için 'y', diğer işlemlere geçmek için 'n' basın: ")
                    if deger == "y":
                        bilgisayar1.bilgisayar_ac()
                        bilgisayar1.internet_guncelle("ac")
                        break
                    elif deger == "n":
                        break
                    else:
                        print("hatalı tuslama")
            elif deger == "kapa":
                if bilgisayar1.durum == "acik":
                    bilgisayar1.internet_guncelle(deger)
                    break
                else:
                    deger = input("bilgisayar kapalıyken bu işlemi yapamazsınız. bilgisayarı açmak için 'y', diğer işlemlere geçmek için 'n' basın: ")
                    if deger == "y":
                        bilgisayar1.bilgisayar_ac()
                        bilgisayar1.internet_guncelle("kapa")
                        break
                    elif deger == "n":
                        break
                    else:
                        print("hatalı tuslama")
            else:
                print("hatalı islem")
    elif islem == "6":
        deger = int(input("yeni bilgisayar hızı giriniz: "))
        bilgisayar1.hiz_guncelle(deger)
    else:
        print("hatalı tuslama...")