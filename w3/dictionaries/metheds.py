myFamily = {
    "child1": {
        "name": "aras",
        "age": 33
    },
    "child2": {
        "name": "oguz",
        "age": 27
    },
    "child3": {
        "name": "deneme",
        "age": 18
    }
}

# clear dicti temizler
myFamily.clear()
print(myFamily)

# copy dicti kopyalar
myCopy = myFamily.copy()
print(myCopy)


# fromkeys belirtilen key ve valuelarla dict olusturur
x = ('key1', 'key2', 'key3')
y = (0)

thisdict = dict.fromkeys(x, y)


print(thisdict)


# get belirtilen key valuesini dondurur
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")
print(x)

# items her anahtar değer çifti için bir tuple içeren bir liste döndürür
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in car.items():
    print(x)


# keys keyleri dondurur
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in car.keys():
    print(x)


# pop belirlenen keyi siler
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")
print(car)


# popitem son eklenen key value çiftini siler
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()
print(car)



# setdefault belirtilen anahtarın değerini döndürür. Anahtar mevcut değilse: anahtarı belirtilen değerle dicte ekler
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("modell", "Bronco")

print(x)
print(car)


# update Sözlüğü belirtilen anahtar-değer çiftleriyle günceller
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)

# values Returns a list of all the values in the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in car.values():
    print(x)