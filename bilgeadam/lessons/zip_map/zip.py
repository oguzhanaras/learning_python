a = [1, 2, 3]
b = ["red", "blue", "green"]
c = ["aras", "deneme", "asdsad"]

x = zip(a, b)
print(x, type(x))

print(list(x))


for i in zip(a, b):
    print(i)

# unpacking
for i, j in zip(a, b):
    print(i, j)

for i, j, k in zip(a, b, c):
    print(i, j, k)

# eslesenleri zipler eğer eslesmeyen varsa ziplemez