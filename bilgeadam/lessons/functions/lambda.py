squared = lambda x: x * x
print(squared(5))

# with map
numbers = list(range(0, 100, 4))
print(numbers)

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)


list(map(lambda x: x % 3 == 0, range(100)))

# with filter
print(list(filter(lambda x: x % 3 == 0, range(100))))