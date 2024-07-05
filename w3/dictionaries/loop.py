# dict keyleri döndürme
thisdict = {
    "name": "aras",
    "age": 88,
    "edu": "python"
}

for x in thisdict:
    print(x)

for x in thisdict.keys():
  print(x)

# dict value ları dondurme
thisdict = {
    "name": "aras",
    "age": 88,
    "edu": "python"
}

for x in thisdict.values():
    print(x)

# itemler arası dongu
thisdict = {
    "name": "aras",
    "age": 88,
    "edu": "python"
}

for x, y in thisdict.items():
    print("key: ", x, "value: ", y)