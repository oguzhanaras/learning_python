# tuple lar degistirilemezdir fakar bunun ekstra kod yazarak bir çözümü vardır

x = ("aras", "ben", "naber")
y = list(x)

y[1] = "sen"

x = tuple(y)

print(x)

# eleman ekleme
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# tuple ları birleştirme
tuple1 = ("aras", "ben")
tuple2 = ("oguz", "sen")
x = tuple2 + tuple1

print(x)

# remove
tuple1 = ("aras", "ben")
x = list(tuple1)
x.remove("ben")
tuple1 = tuple(x)

print(tuple1)

# delete
tuple1 = ("aras", "ben")
del tuple1

print(tuple1) # silineceegi icin hata verir