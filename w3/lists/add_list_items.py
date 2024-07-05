#liste sonuna öge ekler
thisList = ["apple", "banana"]
thisList.append("orange")

print(thisList)

#listeye liste ekleme
firsList = ["apple", "banana"]
secList = ["mango", "orange"]

firsList.extend(secList)

print(firsList)

#listeye tuple da eklenebilir
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)