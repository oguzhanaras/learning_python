sayi = input("sayi gir: ")
adet = int(len(sayi))
toplam = 0
for i in sayi:
    i = int(i)
    x = i ** adet
    toplam += x

if toplam == int(sayi):
    print("armstrong number")
else:
    print("not armstrong number")