myList = ["apple", "banana", "cherry"]
print(myList)
myList[1] = "yenideger"
print(myList)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#degistirmek istenilenden daha fazla öge yazılırsa listeye eklenir
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#daha az veri girilirse eleman silinir
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#insert metodu ile veri ekleme
thisList = ["apple", "banana", "cherry"]
thisList.insert(2, "eklenen")
print(thislist)
