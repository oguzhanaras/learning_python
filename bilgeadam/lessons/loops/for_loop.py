my_list = ["aras", "ben", "sen"]

for i in my_list:
    print(i)


# range
for i in range(10):
    print(i ** 2)


# 1-20 arasındaki(20 dahil) sayıların tek ve çift olanları yazdır
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} çift sayıdır")
    else:
        print(f"{i} tek sayıdır")

# 1 den 20 ye kadar (20 dahil) olan sayıları toplayınız
toplam = 0
for i in range(1, 21):
    toplam += i
print(toplam)

toplam = 0
for i in range(1, 21):
    if i % 2 == 0:
        toplam += i
print(toplam)



# iterable objects: string lists dict set tuple range

# enumerate
fruits = ["apple", "banana", "cherry"]
enumerated_fruits = enumerate(fruits, 1)
print(list(enumerated_fruits))



# list comprehension
fruits = ["apple", "banana", "cherry", "mango"]
new_list = []

for fruit in fruits:
    if "a" in fruit:
        new_list.append(fruit)
print(new_list)


fruits = ["apple", "banana", "cherry", "mango"]
new_list = [fruit for fruit in fruits if "a" in fruit]
print(new_list)