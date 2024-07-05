dict = {
    "adi": "aras",
    "yas": 19,
    "durum": True
}

ogrenci = dict["adi"]

print(ogrenci)

# get method
dict = {
    "adi": "aras",
    "yas": 19,
    "durum": True
}

x = dict.get("durum")
print(x)

# get keys
dict = {
    "adi": "aras",
    "yas": 19,
    "durum": True
}

x = dict.keys()
print(x)

# degisiklikler sozluge yansıtılır
dict = {
    "adi": "aras",
    "yas": 19,
    "durum": True
}

x = dict.keys()
print("ilk", x)

dict["belge"] = "var"

print("ikinci", x)

# get values
dict = {
    "adi": "aras",
    "yas": 19,
    "durum": True
}


x = dict.values()
print(x)



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

# get items
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x)

# check if
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if "model" in thisdict:
    print("var")
else:
    print("err")
