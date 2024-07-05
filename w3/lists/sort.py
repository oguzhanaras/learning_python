myList = [3, 5, 7, 2, 1, 4]
myList.sort()

print(myList)

myList = ["acar", "abla", "bu"]
myList.sort()

print(myList)

# azalan sekilde sıralamak için reverse = true ifadesini kullan
myList = [3, 5, 7, 2, 1, 4]
myList.sort(reverse = True)

print(myList)


#ozel fonksıyon kullanımı
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#sort buyuk kucuk harfe duyarlıdır
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()

print(thislist)

#harfe duyarsız yapmak
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)

print(thislist)