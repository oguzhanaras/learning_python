list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

for i in list2:
    list1.append(i)

print(list1)

#extend metodu
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)

print(list1)