# while
a = 0
b = 10

while a < b:
    print(f"a: {a} b: {b}")
    a += 1


todos = ["aras", "ben", "iki"]

while todos:
    todo = todos.pop()
    print(f"todo: {todo}")


c = 5
while c:
    print(f"c: {c}")
    c -= 1


# while-else
a = 0
b = 10

while a < b:
    print(f"a: {a} b: {b}")
    a += 1
else:
    print("program bitti")


# break ifadesi
a = 0
b = 10

while a < b:
    print(f"a: {a} b: {b}")
    a += 1
    if a == 5:
        print("breaking..")
        break
else:
    print("program bitti")


# continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("program bitti")



# kullanıcıya istediği zaman cıkmasına izin ver
print("""
bir kelime soyle tersini yazdırayım..
cıkmak için q ya basın
""")
while True:
    islem = input("q ile programdan cıkabilirsin")
    if islem == "q":
        print("program sonlanıyor")
        break
    else:
        print(islem[::-1])



# örnek: ziyaret edilen şehirler

my_list = []
while True:
    islem = input("gezdiğiniz sehri yazınız ya da q ile programdan cıkın")
    if islem == "q":
        print("program bitiyor")
        break
    else:
        my_list.append(islem)

for i in my_list:
    print(i)


# listelerde while
numbers = list(range(11))


while numbers:
    print(f"{numbers[-1]}'in karesi: {numbers[-1] ** 2}")
    popped = numbers.pop()
    print(f"{popped} listeden cıkarıldı")
else:
    print(f"listenin uzunlugu {len(numbers)}")
    print("program sonlanıyor")


# sozluklerle calısmak
responses = {}
active = True

while active:
    name = input("isim gir: ")
    mountain = input("hani dağa tırmanmak ister")
    responses[name] = mountain