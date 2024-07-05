#liste içinde a harfi gençen elemanlar
myList = ["apple", "banana", "orange", "cherry"]
newList = []

for x in myList:
    if "a" in x:
        newList.append(x)

print(newList)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newList = [x for x in fruits if "a" in x]

print(newList)

liste = [1, 2, 3, 4]
liste2 = [i * 2 for i in liste if i == 2]

print(liste2)

newlist = [x for x in range(10) if x < 5]

print(newlist)

yenile = ["aras", "oguz", "merhaba"]
print(yenile)

yeni = [x.upper() for x in yenile]
print(yeni)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)




