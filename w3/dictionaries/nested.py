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

print(myFamily["child1"]["name"])

# ekleme
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myfamily)


# loop
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

for x, obj in myFamily.items():

    print(x)
    for item in obj:
        print(item + ": ", obj[item])


for x, obj in myFamily.items():

    print(x)
    for item, z in obj.items():
        print(item, z)