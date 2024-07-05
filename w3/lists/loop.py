thisList = list(("apple", "banana", "orange"))
for x in thisList:
    print(x)

myList = ["apple", "banana", "orange"]

for i in range(len(myList)):
    print(myList[i])

myList = ["apple", "banana", "orange"]

i = 0
while i < len(myList):
    print(myList[i])
    i += 1

#comprehension kullanımı
myList = ["apple", "banana", "orange"]

[print(x) for x in myList]
