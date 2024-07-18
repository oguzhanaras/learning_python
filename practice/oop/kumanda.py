import random
import time

class Kumanda():
    def __init__(self, tv_durum="kapali", tv_ses=0, kanal_list=["Trt"], kanal="Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_list = kanal_list
        self.kanal = kanal

    def tv_ac(self):
        if self.tv_durum == "kapali":
            print("tv aciliyor")
            self.tv_durum = "acik"
        else:
            print("tv zaten acik")

    def tv_kapat(self):
        if self.tv_durum == "acik":
            print("tv kapaniyor")
            self.tv_durum = "kapali"
        else:
            print("tv zaten kapali")

    def ses_ayar(self):
        while True:
            islem = input("ses artırmak için '>', azaltmak için '<', çıkmak için 'q' basın")

            if islem == "q":
                break
            elif islem == "<":
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                print(self.tv_ses)
            elif islem == ">":
                if self.tv_ses < 31:
                    self.tv_ses += 1
                print(self.tv_ses)
            else:
                print("hatali tuslama")
        print(f"güncel ses: {self.tv_ses}")

    def kanal_ekle(self, kanal):
        print("kanal ekleniyor...")
        time.sleep(1)

        self.kanal_list.append(kanal)


    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_list) - 1)

        self.kanal = self.kanal_list[rastgele]

        print(f"şu anki kanal: {self.kanal}")

    def __len__(self):
        return len(self.kanal_list)

    def __str__(self):
        return f"""
        tv durum: {self.tv_durum}
        tv ses: {self.tv_ses}
        kanal: {self.kanal}
        kanallar: {self.kanal_list}"""


kumanda = Kumanda()

print("""
1. tv aç
2 tv kapa
3 ses ayarları
4 kanal ekle
5 kanallar
6 rastgele kanala geç
7 tv bilgileri
cıkmak için q ya basın
""")

while True:
    islem = input("islem gir: ")
    if islem == "q":
        break
    elif islem == "1":
        kumanda.tv_ac()
    elif islem == "2":
        kumanda.tv_kapat()
    elif islem == "3":
        kumanda.ses_ayar()
    elif islem == "4":
        eklenecekler = input("eklemek istediğiniz kanalları ',' ile ayırarak girin: ")
        x = eklenecekler.split(",")
        for i in x:
            kumanda.kanal_ekle(i)
    elif islem == "5":
        x = kumanda.kanal_list
        print(x)
    elif islem == "6":
        kumanda.rastgele_kanal()
    elif islem == "7":
        print(kumanda)
    else:
        print("hatali tuslama")
