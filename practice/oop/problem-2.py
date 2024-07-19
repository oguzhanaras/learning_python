class Hayvan:
    def __init__(self, isim, yas, tur):
        self.isim = isim
        self.yas = yas
        self.tur = tur

    def yemek_yemek(self):
        print(f"{self.isim} yemek yiyor.")

    def ses_cikarmak(self):
        print(f"{self.isim} ses çıkarıyor.")

    def hareket_etmek(self):
        print(f"{self.isim} hareket ediyor.")

class Kopek(Hayvan):
    def __init__(self, isim, yas, tur, cins):
        super().__init__(isim, yas, tur)
        self.cins = cins

    def havlamak(self):
        print(f"{self.isim} havlıyor.")

    def kuyruk_sallamak(self):
        print(f"{self.isim} kuyruk sallıyor.")
class Kus(Hayvan):
    def __init__(self, isim, yas, tur, kanat_genisligi):
        super().__init__(isim, yas, tur)
        self.kanat_genisligi = kanat_genisligi

    def uc(self):
        print(f"{self.isim} uçuyor.")

    def ot(self):
        print(f"{self.isim} ötüyor.")

class At(Hayvan):
    def __init__(self, isim, yas, tur, kosu_hizi):
        super().__init__(isim, yas, tur)
        self.kosu_hizi = kosu_hizi

    def kisne(self):
        print(f"{self.isim} kişniyor.")

    def kos(self):
        print(f"{self.isim} {self.kosu_hizi} hızında koşuyor.")

kopek = Kopek("Karabaş", 3, "Köpek", "Golden Retriever")
kopek.yemek_yemek()
kopek.havlamak()

kus = Kus("Maviş", 1, "Kuş", 50)
kus.yemek_yemek()
kus.uc()

at = At("Şahbatur", 5, "At", 60)
at.yemek_yemek()
at.kos()
