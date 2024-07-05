list1 = [1, 8, 2, 3, 4]
list2 = [5, 6, 7]

# append yöntemi veeri ekler
list1.append(15)
print(list1)

# clear metodu verileri siler ama liste yok olmaz
list2.clear()
print(list2)

#copy listeyi kopyalar
copyList = list1.copy()
print(copyList)

# count metodu istenilen veriden kaç tane oldugunu sayar
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)

print(x)

# extend metodu ver listeyi bir listeye ekler
list1.extend(list2)

print(list1)

# index metodu belirtilen değere sahip ilk elemanın indeks numarasını dondurur
x = list1.index(3)

print(x)

# belirtilen index numarasına bir öge ekler
list1.insert(1, 10)

print(list1)

# pop metodu belirtilen indexteki ögeyi kaldırır
list1.pop(1)

print(list1)

# remove belirtilen degere sahip ogeyi kaldırır
list1.remove(2)

print(list1)

# reverse sırayı tersine cevirir
list1.reverse()

print(list1)

# sort metodu listeyi sıralar
list1.sort()

print(list1)