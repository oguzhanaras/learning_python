print("""*******
simple atm program
press q to quit
1- bakiye sorgulama
2- para yatırma
3- para cekme
""")

bakiye = 1000

while True:
    islem = input("islem seciniz")
    if islem == "q":
        print("program sonlandi")
        break
    elif islem == "1":
        print(f"bakiyeniz: {bakiye}")
    elif islem == "2":
        miktar = int(input("para yatırmak istediğiniz miktar girin"))

        if miktar <= 0:
            print("0 dan büyük miktar giriniz")
        else:
            bakiye += miktar
            print(f"güncel bakiye: {bakiye}")
    elif islem == "3":
        cekim = int(input("para cekmek istediğiniz miktar giriniz"))

        if bakiye - cekim < 0:
            print("bakiye yetersiz")
        else:
            bakiye -= cekim
            print(f"guncel bakiye {bakiye}")
