x = (1, 2, 3, 4)
print(x, "type: ", type(x))


# tek elemanlı tuple
one = (1,)

print(x[2])


# slice
print(x[:3])

# in
print(2 in x) # bool değer dondurur

print(10 not in x)


x[1] = 5 # elemanlar değişmez hata verir



tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6)
x = tuple1 + tuple2
print(x)
