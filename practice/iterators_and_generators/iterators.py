liste = [1, 2, 3, 4, 5]

for i in liste:
    print(i)

iterator = iter(liste)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
