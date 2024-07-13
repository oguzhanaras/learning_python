class Araba():
    model = "reno"
    renk = "gumus"
    beygir = 110
    silindir = 4


araba1 = Araba() # sınıftan nesne olusturma
print(araba1.beygir)
print(araba1.silindir)

print(Araba.beygir) # sınıfın özelliğine erişme

dir(Araba)


class Araba():
    model = "reno"
    renk = "gumus"
    beygir = 110
    silindir = 4
    def __init__(self): # init fonksiyonu obje olusturulunca kendi kendine cagrılır ve ilk cagrılır
        print("init func")

araba2 = Araba()  # fonksiyon cagrılmadıgı halde print calısır


class Araba():
    def __init__(self, model, renk, beygir, silindir): # self anahtar kelimesi olusturulan nesnenin referansıdır
        print("init func")
        self.model = model
        self.renk = renk
        self.beygir = beygir
        self.silindir = silindir

araba3 = Araba("reno", "gumus", 110, 4)
araba4 = Araba("pejo", "siyah", 120, 4)

print(araba3.model, araba3.renk, araba3.beygir)
print(araba4.model, araba4.renk, araba4.beygir)

# fonksiyonlardaki gibi class larda da varsayılan değer girilebilir
class deneme():
    def __init__(self, dene, dene2 = "default"):
        print("init func")
        self.dene = dene
        self.dene2 = dene2

x = deneme("dene değerini girdim fakat dene2 girmedim")
print(x.dene, "-------", x.dene2)




