# union() yöntemi, her iki kümedeki tüm öğeleri içeren yeni bir küme döndürür.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


set1 = {1, 2, 3}
set2 = {"aras", "ben", "hi"}
set3 = set1 | set2

print(set3)


# birden fazla kume birlestirme
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)


# kümeler ile liste veya tuplelar birlesebilir
# | operatoru yalnızca kumelerle kumeleri birlestirirken calısır
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# update yontemi bir kumedeki tum ogeleri digerine ekler
# update() orijinal kümeyi değiştirir ve yeni bir küme döndürmez.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# !! hem union hem update yinelenen ogeleri haric tutar


# intersection metodu ortak elemanları yeni kümeye atar ve döndürür
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# & operatoru de kullanılabilir
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# insersection_update yeni küme döndürmez orjinali değiştirir
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

# difference ortak olmayan ogelerı yeni bir kume olarak dondurur
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set2.difference(set1)

set3 = set1.difference(set2)

print(set3)

# difference_update() yöntemi de ilk kümedeki diğer kümede olmayan öğeleri tutar, ancak yeni bir küme döndürmek yerine orijinal kümeyi değiştirir
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)