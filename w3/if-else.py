"""
Eşittir: a == b
Eşit Değil: a != b
Şundan daha az: a < b
Daha az veya eşit: a <= b
Şundan büyük: a > b
Büyük veya eşit: a >= b
"""

a = 33
b = 200
if b > a:
  print("b is greater than a")


# elif
a = 10
b = 10

if a < b:
    print("a kucuk")
elif a == b:
    print("esittir")

# else
a = 10
b = 7

if a < b:
    print("a kucuk")
elif a == b:
    print("esittir")
else:
    print("b kucuk")



a = 10
b = 7
if a > b: print("a is greater than b")



a = 2
b = 330
print("A") if a > b else print("B")


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")



# and operator iki kosul saglanınca ture doner
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# or operatoru iki kosuldan biri dogru olursa da true doner
a = 200
b = 33
c = 500

if a > b or b > a:
    print("true")

# not operatoru durumu tersine cevirir7
a = 10
b = 5

if not a > b:
    print("a b den büyüktür")
else:
    print("a b den buyuktur fakat false doner ve buraya girer")

# nested
a = 21

if a > 10:
    print("10 dan buyuktur")
    if a > 20:
        print("20 den de buyuktur")
    else:
        print("20 den buyuk değildir")


# pass
a = 33
b = 200

if b > a:
  pass