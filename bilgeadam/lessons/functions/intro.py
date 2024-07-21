# def keyword

def name_of_function(arg1, arg2, arg3):
    #docstring
    """
    this function prints out..
    :param arg1: first argument
    :return:
    """
    # codeblock
    pass


name_of_function(1, "iki", True)

# type
type(name_of_function)


# input almayan ve return etmeyen
def say_hello():
    """
    bu fonksiyon hello yazdırır
    :return:
    """
    print("Hello")

say_hello()

# return ile  geri değer döndürülen değer yoksa none dondurur
x = say_hello()
print(x)

help(say_hello)


def say_my_name(name):
    print(f"Hello {name}")

say_my_name("aras")


def say_hello_bye(name1: str, name2: str):
    print(f"Hello {name1} and {name2}")
    print(f"bye {name1} and {name2}")


say_hello_bye("aras", "john")
say_hello_bye("aras", name2="john") # keyword positional argumandan sonra gelmeli


def varsayilan(name1="james", name2="john"): # varsayılan değer atama
    print(f"Hello {name1} and {name2}")

varsayilan()
varsayilan(name1="aras")


def square(x):
    return x * x

print(square(3))


def add_numbers(num1: float, num2: float, num3: float):
    return num1 + num2 + num3

print(add_numbers(1.1, 3.2, 4.3))


def multiply_numbers(num1, num2, num3): return num1 * num2 * num3


numbers = list(range(0, 50, 3))
print(numbers)

def f(x):
    return 2 * x ** 2 + 3 * x + 4

print(list(map(f, numbers)))

