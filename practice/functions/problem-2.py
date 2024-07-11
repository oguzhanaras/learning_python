# Problem 2
# Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.


def ebob(sayi1, sayi2):
    bolumler = []
    for i in range(sayi1 + 1):
        if sayi1 % 2 == 0:
            bolumler.append(i)
    for x in range(sayi2 + 1):
        if sayi1 % 2 == 0:
            bolumler.append(x)
    for j in bolumler[::-1]:
        if bolumler.count(j) == 2:
            return j

while True:
    islem = input("cıkmak için q devam etmek için c basın ")
    if islem == "q":
        print("program sonlanıyor")
        break
    elif islem == "c":
        sayi1 = int(input("sayi1: "))
        sayi2 = int(input("sayi2: "))
        print("ebob: ", ebob(sayi1, sayi2))
    else:
        print("lutfen q ya da c basın")