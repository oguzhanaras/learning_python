#aritmetik operatorler
a = 5
b = 7

toplama = a + b
print(toplama)

cikarma = a - b
print(cikarma)

carpma = a * b
print(carpma)

bolme = a / b
print(bolme)

modulus = a % 2
print(modulus)

usAlma = a ** 2
print(usAlma)

floor = 17 // 3
print(floor)

#atama operatorleri
x = 5
print(x)

a = 3
a += 7
print(a)

a = 3
a -= 7
print(a)

a = 3
a *= 7
print(a)

a = 3
a /= 7
print(a)

a = 3
a %= 7
print(a)


#karsilastirma
print(5 == 5)

print(5 != 5)

print(5 < 7)

print(5 > 7)

print(5 <= 5)

print(5 >= 5)

#and operatoru her iki durumun dogru olması durumunda true dondurur
print(5 == 5 and 7 == 7)

#or operatoru tek durumun dogru olması durumunda true dondurur
print(5 == 5 or 5 == 9)

#aynı objeyse
x = "selam"
y = "selamlar"
print(x is y)

#iceriyor mu
x = ["apple", "banana"]
print("banana" in x)

x = ["apple", "banana"]

print("pineapple" not in x)
