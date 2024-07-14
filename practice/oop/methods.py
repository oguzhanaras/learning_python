class Yazilimci():
    def __init__(self, name, surname, number, salary, langs):
        self.name = name
        self.surname = surname
        self.number = number
        self.salary = salary
        self.langs = langs

    def bilgileri_goster(self):
        print(f"""
        isim: {self.name}
        soyisim: {self.surname}
        numara: {self.number}
        maas: {self.salary}
        diller: {self.langs}
        """)

    def zam_yap(self, zam):
        self.salary += zam

    def yeni_dil(self, dil):
        self.langs.append(dil)

yazilimci1 = Yazilimci("john", "doe", 25611212, 5000, ["python", "javascript"])
yazilimci2 = Yazilimci("jonny", "doerome", 25611212, 5000, ["python", "javascript"])

yazilimci1.bilgileri_goster()
yazilimci1.zam_yap(500)
yazilimci1.yeni_dil("django")
yazilimci1.bilgileri_goster()