print("""
asal sayı bulan program
cıkmak için q ya basın
""")

def asal(sayi):
    if sayi == 1:
        return False
    elif sayi == 2:
        return True
    else:
        for i in range(2, sayi):
            if sayi % i == 0:
                return False
        return True

while True:
    sayi = input("sayi giriniz: ")

    if sayi == "q":
        print("program sonlanıyor")
        break
    else:
        sayi = int(sayi)
        if asal(sayi):
            print(f"{sayi} asal sayıdır")
        else:
            print(f"{sayi} asal değildir")
