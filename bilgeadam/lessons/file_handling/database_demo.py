class Veritabani:
    def __init__(self, dosya_adi):
        self.dosya_adi = dosya_adi
        self.__veritabani_olustur()

    def __veritabani_olustur(self):  # CREATE (w)
        with open(self.dosya_adi, "w", encoding="utf-8") as file:
            file.write("mjackson,1776\n")
            file.write("dnowitski,1999\n")
            file.write("ntesla,1456\n")
            file.write("emusk,0061\n")
            file.write("mkemal,1881\n")

    def kullanici_ekle(self, kullanici_adi, sifre):  # UPDATE (a)
        with open(self.dosya_adi, "a", encoding="utf-8") as file:
            file.write(f"{kullanici_adi},{sifre}\n")
        return True

    def kullanici_listele(self):  # READ (r)
        with open(self.dosya_adi, "r", encoding="utf-8") as file:
            for counter, line in enumerate(file, start=1):
                print(f"{counter}. {line.split(",")[0]}")

    def kullanici_dogrula(self, kullanici_adi, sifre):
        with open(self.dosya_adi, "r", encoding="utf-8") as file:
            for line in file:
                kullanici_bilgi = line.strip().split(",")
                if kullanici_adi == kullanici_bilgi[0] and sifre == kullanici_bilgi[1]:
                    return True
            return False

    def kullanici_cikar(self, kullanici_adi):  # UPDATE ("r+")
        with open(self.dosya_adi, "r+", encoding="utf-8") as file:
            lines = file.readlines()

            new_lines = []
            for line in lines:
                if kullanici_adi not in line:
                    new_lines.append(line)

            file.seek(0)
            file.write("".join(new_lines))   # file.writelines(new_lines)
            file.truncate()

        return True


veritabani = Veritabani("kullanıcılar.txt")
veritabani.kullanici_listele()
veritabani.kullanici_ekle("madonna", "1234")
veritabani.kullanici_ekle("cristiano", "777")

veritabani.kullanici_dogrula("mjackson", "1776")
veritabani.kullanici_dogrula("cristiano", "777")

veritabani.kullanici_cikar("emusk")
veritabani.kullanici_cikar("madonna")