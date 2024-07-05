# tuple sıralı ve değiştirilemez koleksiyondur. yinelenen ogelere izin verir
myTuple = ("apple", "banana", "orange")

print(myTuple)

print(len(myTuple))

# tek ogeli bir tuple olusturmak için ilk ogeden sonra virgul koy yoksa hata verir
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#tuple lar str int ve bool deger alabilir
tuple1 = ("bu", "string")
tuple2 = (True, False)
tuple3 = (1, 2, 3)

# bir tuple farklı veri turleri içerebilir
tuple1 = ("aras", 15, True, False, 70)

print(type(tuple1))

# farklı tuple olusturma yontemi
thisTuple = tuple(("aras", 5, True))
