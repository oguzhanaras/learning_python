#listeye indeks numaraları ile erisilebilir
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#listeye sondan erismek istenirse negatif deger kullanılır
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#baslangıc ve bitis belirleme
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#listede içeriyor mu kontrol etme
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

if "apple" in thislist:
    print("deger listede var")
else:
    print("deger listede yok")
