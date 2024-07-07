# range
my_range = range(5) # tek dğeri stop yani duracagı yer olarak alır
print(my_range)

my_range = range(1, 10) # iki değer koyunca baslangıc ve son oalrak alır
print(my_range)

my_range = range(1, 10, 2) # ucuncu değer adım sayısını alır
print(my_range)

my_range = range(20, 10, -1) # azaltarak ilerler
print(my_range)



# append sona eleman ekler
my_list = list(range(5))
print(my_list)

my_list.append(5)
print(my_list)


# extend liste uzatma
new_list = [6, 7, 8]
my_list.extend(new_list)
print(my_list)


list2 = [1, 2, 3]
list2.extend("aras")
print(list2)


# insert belirli indekse eleman ekler
list3 = [1, 2, 3]
list3.insert(2, "aras")
print(list3)


# remove verilen degere gore eleman siler
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)

# pop indekse gore eleman siler ve sildiği değeri return eder
my_list.pop(1)
print(my_list)


# index elemanın indexini bulur
my_list = [1, 2, 3, 3, 5, 2, 3]
print(my_list.index(3))

# count elemanın tekrar etme sayısını bulur
my_list.count(3)


# sort liste sıralama var olanı gunceller
mylist = [3, 5, 6, 2, 7, 8, 5, 3]
x = mylist.sort()
print(mylist)
print(x)


# reverse default olarak false olur true yazarsak ters dondurur
list3 = [3, 2, 1]
x = list3.reverse()
print(list3)
print(x)

alfabe = ["b", "c", "a"]
alfabe.sort()
print(alfabe)

# sorted yeni liste olusturur
mylist = [3, 5, 6, 2, 7, 8, 5, 3]
x = sorted(mylist)
print(mylist)
print(x)


# sorted reverse
mylist = [3, 5, 6, 2, 7, 8, 5, 3]
x = sorted(mylist, reverse=True)
print(mylist)
print(x)



# burda b a ya eşittir ve birisi guncellenince diğeri de guncellenir
a = [1, 2]
print(a, id(a))

b = a
print(b, id(b))

b[0] = 6
print("b: ", b, "a: ", a)


# copy
c = a.copy()

c[0] = 7
print("c: ", c)
print("a: ", a)
