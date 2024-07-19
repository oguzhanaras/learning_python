my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def cift_mi(sayi):
    if sayi % 2 == 0:
        return sayi
    else:
        raise ValueError
for i in my_list:
    try:
        print(cift_mi(i))
    except ValueError:
        pass