#istenilen ifadeyi dizeden kaldırma
thisList = ["apple", "banana", "orange"]
thisList.remove("banana")

print(thisList)

#index ile pop metodu ile kaldırılabilir. index belirtilmezse son ögeyi kaldırır
thisList = ["apple", "banana", "orange"]
thisList.pop(1)

print(thisList)

thisList = ["apple", "banana", "orange"]
thisList.pop()

print(thisList)

#del istenilen indexi ya da listeyi tamamen silebilir
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

print(thislist) #dizi silindigi icin hata verir

#clear metodu listeyi bosaltır fakat silmez dizi bos doner
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
