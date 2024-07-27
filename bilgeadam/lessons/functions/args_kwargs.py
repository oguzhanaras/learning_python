# arbitrary *args


def topla1(num1, num2, num3):
    return num1 + num2 + num3

print(topla1(2, 3, 4))


def topla(*args): # aldıgı değerleri bir tuple olarak saklar
    toplam = 0
    for arg in args:
        toplam += arg
    return toplam

print(topla(1, 2, 3))


# arbitrary keyword arguments **kwarg
# kwargs dict olarak saklar key value alır

def print_info(**kwargs):
    return kwargs

print_info(name="ali", age=23, city="ankara")


def print_info2(**kwargs):
    for key, value in kwargs.items():
        print(f"key: {key} value: {value}")


print_info2(name="ali", age=23, city="ankara")



def mixed_func(*args, **kwargs):
    print("positional args: ", args)
    print("keyword args: ", kwargs)

mixed_func(1, 2, 3, name="ali", age=23, city="ankara")


def scrambled(a, b, c=5, d=7, *args, **kwargs):
    print(f"positional: {a}, {b}")
    print(f"keyword: {c}, {d}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

scrambled(7, 8) # tuple ve dict boş doner
scrambled(7, 8, 5, 6, 1, 2, 3, name="ali", age=23, city="ankara")