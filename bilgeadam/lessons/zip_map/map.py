fruits = ['apple', 'banana', 'cherry']


x = map(len, fruits)
print(list(x))


numbers = [1, 2, 3, 4, 5]

def after_5(x):
    return x + 5

print(list(map(after_5, numbers)))