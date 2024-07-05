thisDict = {
    "name": "aras",
    "age": 33,
    "edu": "python"
}

myDict = thisDict.copy()

print(myDict)

thisDict["belge"] = "1335456"
print(thisDict)
print(myDict)


# atama yontemi ile kopyalamada değişiklikler senkrondur
thisDict = {
    "name": "aras",
    "age": 55
}

newDict = thisDict
print(newDict)

thisDict["belge"] = "5452255"
print(thisDict)
print(newDict)