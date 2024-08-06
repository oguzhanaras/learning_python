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