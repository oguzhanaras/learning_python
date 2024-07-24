def find_median(numbers):
    numbers.sort()
    uzunluk = len(numbers)
    if uzunluk % 2 == 1:
        ortanca = 0
        for i in range(int((uzunluk / 2)) + 1):
            ortanca = numbers[i]
        return ortanca
    else:
        return "uzunlugu çift olanın ortancası yoktur"

print(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9]))