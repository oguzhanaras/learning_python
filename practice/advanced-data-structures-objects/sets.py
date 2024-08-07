x = {}
type(x)

liste = [1, 1, 2, 2, 2, 3, 4,]
yeni = set(liste)

# kumelerde her elemandan 1 tane olabilir
print(yeni)


my_str = "python programlama dili"
print(set(my_str))

for i in yeni:
    print(i)


# add kumeye eleman ekler eleman varsa hata vermez fakat islem yapılmaz

my_set = {1, 2}

my_set.add(3)
my_set.add(3)

print(my_set)

set1 = {1, 2, 3, -4, 6}
set2 = {1, 2, 3, 4, 5}

# set1 de olup set2 de olmayanları dondurur
x = set1.difference(set2)

print(x)

# set2 de olup set1 de olmayanları dondurur
y = set2.difference(set1)
print(y)

# set1 de olup set2 de olamyanları alır set1 i sıfırlar ve o elemanları ekler
set1.difference_update(set2)

print(set1)


# discard kumeden varsa eleman cıkarır yoksa hiçbir şey yapmaz hata da vermez
set3 = {1, 2, 3, 4}
set3.discard(2)
print(set3)

set3.discard(15)
print(set3)


set4 = {3, 5, 7, 9}
set5 = {5, 9, 11}

# kesişimi alır (ortak olanları)
set4.intersection(set5)


# intersectionupdate kesişimi alır ve istenilen kümeye eşitler
set4.intersection_update(set5)

print(set4)

set6 = {1, 2, 3}
set7 = {4, 5, 6}
set8 = {1, 4, 7}

# ayrık kume mı yani kesişimleri (ortak olan) boşsa true doner. değilse false doner
set6.isdisjoint(set7) # true
set6.isdisjoint(set8) # false


set9 = {1, 2, 3}
set10 = {1, 2, 3, 4}
set11 = {5, 6, 7}

# alt kumesi yani elemanların hepsi o kumenin içerisinde varsa ise true değilse false dondurur.
set9.issubset(set10) # true
set9.issubset(set11) # false
set9.issubset({1, 2, 3}) # true doner

set12 = {1, 2, 3, 4}
set13 = {2, 4, 6, 7}

# iki kume elemanlarını birlestirir ve yeni kume doner
set12.union(set13)

# ıkı kume elemanlarını bırlestirir ve istenilen kumeye değer olara atar
set12.update(set13)
print(set12)