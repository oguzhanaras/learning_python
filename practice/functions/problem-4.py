def sayi_yazdir(sayi):
    birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
    onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

    if 10 <= sayi < 100:
        onlar_basamagi = sayi // 10
        birler_basamagi = sayi % 10

        return f"{onlar[onlar_basamagi]} {birler[birler_basamagi]}".strip()
    else:
        return "Lütfen iki basamaklı bir sayı giriniz."

while True:
    sayi = input("cıkmak için q bas ya da sayı gir: ")
    if sayi == "q":
        print("bye")
        break
    else:
        sayi = int(sayi)
        print(sayi_yazdir(sayi))
        continue