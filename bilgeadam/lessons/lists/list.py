my_list = [1,2,3,4,5]

# len uzunlugu verir
print(len(my_list))

# içerisine farklı veri tiplerini barındırabilir
sec_list = [1, 2, 3, 4, 5, "abc", 5.5, True, None, [1, {"key": "value"}]]

# elemanlara erişme
print(sec_list[2])

print(sec_list[9][1]["key"])

# birden cok
print(sec_list[:5])



list_in_list = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

print(list_in_list[1][0])
print(list_in_list[1][1])
print(list_in_list[1][1][0])


# addition
list1 = [4, 8]
list2 = [6, 2]
print(list1 + list2)

# liste elemanı değiştirme
first_list = ["orange", "apple"]
second_list = ["grapes", "avocado"]

first_list[0] = "banana"
print(first_list)

fruit_list = first_list + second_list
print(fruit_list)
fruit_list[1:3] = ["aras", "oguz"]
print(fruit_list)


# eleman ekleme
fruit_list += ["atama"]
print(fruit_list)

fruit_list += ["atama"]
print(fruit_list)

fruit_list += 5 # error


# eleman silme
my_list = [1,2,3,4,5]
del my_list[3]
print(my_list)


# aritmetik işlemler
scores = [90, 55, 67, 88, 100, 22, 34]

print(len(scores))
print(max(scores))
print(min(scores))
print(sum(scores))

print(sum(scores) / len(scores))