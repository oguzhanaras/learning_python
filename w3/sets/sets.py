# Küme, sıralanmamış, değiştirilemez* ve indekslenmemiş bir koleksiyondur

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Bir set oluşturulduktan sonra öğelerini değiştiremezsiniz, ancak öğeleri kaldırabilir ve yeni öğeler ekleyebilirsiniz.
# Kümelerde aynı değere sahip iki öğe bulunamaz.

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) # tek apple gozukur

# True ve 1 değerleri setlerde aynı değer olarak kabul edilir ve yinelenen olarak değerlendirilir
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

# False ve 0 değerleri setlerde aynı değer olarak kabul edilir ve yinelenen olarak değerlendirilir
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

# len method
thisset = {"apple", "banana", "cherry", False, True, 0}
x = len(thisset)
print(x)

# data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))


thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)