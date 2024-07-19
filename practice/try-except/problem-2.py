my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def cift_mi(sayi):
    try:
        if sayi % 2 == 0:
            return print(sayi)
        else:
            raise ValueError
    except:
        print("value error")
    finally:
        print("program bitti")

cift_mi(5)
cift_mi(2)

try:
    for i in my_list:
        if i % 2 == 0:
            print(i)
except:
    print("error")