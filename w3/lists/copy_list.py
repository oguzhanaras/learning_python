#listeleri bu sekilde basitçe kopyalayabiliriz fakat bu durumda liste1 degisince liste2 de degisir
liste1 = [1, 2, 3, 4, 5, 6]
liste2 = liste1

print(liste2)

#copy metodu
myList = ["bu", "benim", "kopyammmm"]
kopya = myList.copy()

print(kopya)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)