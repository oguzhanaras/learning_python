# setler değiştirilemez fakat veri eklenir
set = {"aras", "ben"}
set.add("eklenen")

print(set)


# update
set1 = {"set", "bir"}
set2 = {"set", "iki"}

set1.update(set2)

print(set1)


# setlere list dict tuple veya obje eklenebilir
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)