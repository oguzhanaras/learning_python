from practice.moduls import deneme


class Calisan():
    def __init__(self, isim, maas, departman):
        print("calisan init")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print(f"""
        isim: {self.isim}
        maas: {self.maas}
        departman: {self.departman}
        """)

    def departman_degis(self, yeni_departman):
        self.departman = yeni_departman


class Yonetici(Calisan):
    #pass  # sınıf içini boş bırakınca hata alır. pass ile hata almasını engelleyebilir ve daha sonra tanımlayabiliriz
    def zam_yap(self, zam_miktari):
        self.maas += zam_miktari



yonetici1 = Yonetici("john", 5000, "manager")
yonetici1.bilgileri_goster()
yonetici1.departman_degis("admin")
yonetici1.bilgileri_goster()


# override

# miras alan sınıf miras alınan fonksiyonlar adında fonksiyo tanımlarsa miras alınan değil kendi fonksiyonu calısır

class Deneme():
    def __init__(self, isim):
        print("deneme init")
        self.isim = isim

    def hi(self):
        print(f"hi {self.isim}")

class Deneme2(Deneme):
    def __init__(self, isim):    # miras alınan init geçersiz kalır kendi init func calısır
        print("deneme222222 init")
        self.isim = isim


denemex = Deneme2("john")
denemex.hi()


# hem miras alıp hem de ekstra bilgiler eklemek için super metodu kullanılır
class Deneme3():
    def __init__(self, isim):
        print("deneme3 init")
        self.isim = isim

    def hi(self):
        print(f"hi {self.isim}")

class Deneme4(Deneme3):
    def __init__(self, isim, yas):
        super().__init__(isim)
        print("deneme4444 init")
        self.yas = yas


my_super = Deneme4("john", 25)
my_super.hi()
print(my_super.yas)