##### IndexError
import math

mylist = [1, 2, 3]
print(mylist[3])  # IndexError: list index out of range

##### TypError
num = 5
mystr = "Hello"

print(num + mystr)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'


def add_numbers(num1: int, num2: int):
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 + num2
    raise TypeError("Both numbers must be integers.")


add_numbers(num, mystr)


##### NameError
print(myvar)   # NameError: name 'myvar' is not defined. Did you mean: 'mystr'?


##### ZeroDivisionError
x, y = 10, 0
print(x / y)    # ZeroDivisionError: division by zero


def modified_division(num1, num2):
    if num2 == 0:
        return math.inf
    return num1 / num2


modified_division(x, y)


##### ValueError
x, y, z = 100, -100, "Hello"
math.sqrt(x)
math.sqrt(y)  # ValueError: math domain error
math.sqrt(z)  # TypeError: must be real number, not str


##### SyntaxError
# if x > 10      # SyntaxError: expected ':'
#     print("x is greater than 10")


##### IndentationError
# if x > 10:
# print("x is greater than 10")    # IndentationError: expected an indented block after 'if' statement on line 1


# AttributeError
mylist.pop()
mylist.abc()    # AttributeError: 'list' object has no attribute 'abc'

# KeyError
mydict = {"Ankara": 6, "İstanbul": 34}
mydict["Trabzon"]    # KeyError: 'Trabzon'

mydict.get("Trabzon")

# ModuleNotFoundError
import nomodule    # ModuleNotFoundError: No module named 'nomodule'
import pandas

# RecursionError
def recursive_func():
    return recursive_func()

recursive_func()    # RecursionError: maximum recursion depth exceeded


def std_dev(variance: float):
    if not isinstance(variance, float):
        raise TypeError("variance must be float")
    if variance < 0:
        raise ValueError("variance cannot be negative")
    return math.sqrt(variance)


std_dev(100.0)
std_dev(-100.0)
std_dev("abc")