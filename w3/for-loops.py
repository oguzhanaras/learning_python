fruits = ["apple", "banana", "mango"]

for x in fruits:
    print(x)


fruits = ["apple", "banana", "mango"]

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


for x in "banana":
    print(x)


# break donguyu bitirir
fruits = ["apple", "banana", "mango"]

for x in fruits:
    print(x)
    if x == "banana":
        break


# continue
fruits = ["apple", "banana", "mango"]

for x in fruits:
    if x == "banana":
        continue
    print(x)

# range varsayılan olarak 0 dan baslar ve belirtilen sayıya kadar 1 artırarak gider
for x in range(6):
    print(x)


# deger belirtme
for x in range(2,9):
    print(x)


# artıs degeri belirtme
for x in range(2,16,2):
    print(x)

# else parametresi dongu bitince calısır. break komutu ıle dongu bitirilirse else calısmaz
for x in range(6):
    print(x)
else:
    print("dongu bitmistir")


for x in range(6):
    print(x)
    if x == 5:
        print("break calısır")
        break
else:
    print("dongu bitmistir")


# nested
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


# pass
for x in [0, 1, 2]:
    pass