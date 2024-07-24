def is_sorted(arr):
    if arr == sorted(arr):
        return True
    else:
        return False

list = [1, 2, 3, 4, 5]
list2 = [2, 1, 7, 3]
print(is_sorted(list))
print(is_sorted(list2))