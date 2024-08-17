##### SPECIAL METHODS, MAGIC METHODS, DUNDER (DOUBLE UNDERSCORE) METHODS #####

# __str__ method
# Yazdırılabilir bir string temsili sağlar (Informal, kullanıcılar için)
num = 12
num.__str__()
str(num)

# __repr__ method
# "Formal", resmi bir string temsili sağlar (Geliştiriciler için)
repr(num)
num.__repr__()

# __add__ method
num1 = 10
num2 = 5
print(num1 + num2)
num1.__add__(num2)

# __sub__ -
# __mul__ *
# __truediv__ /
# __floordiv__ //
# __mod__ %
print(num1 % num2)
num1.__mod__(num2)

# __pow__ **
print(num1 ** num2)
num1.__pow__(num2)
pow(num1, num2)

# __eq__ ==
print(num1 == num2)
num1.__eq__(num2)

# __ne__ !=
print(num1 != num2)
num1.__ne__(num2)

# __gt__ >
print(num1 > num2)
num1.__gt__(num2)

# __lt__ <
# __ge__ >=
# __le__ <=

# __getitem__ []
mylist = [33, 12, 66]
print(mylist[1])
mylist.__getitem__(1)

# __len__ len()
mystr = "BilgeAdam"
print(len(mystr))
mystr.__len__()

class MyString(str):
    def __len__(self):
        return 1

    def __contains__(self, item):
        return item.lower() in self.lower()


yourstr = MyString("BilgeAdam")
print(yourstr)
len(yourstr)
yourstr.__len__()

# __contains__ in
print("B" in "BilgeAdam")
yourstr.__contains__("B")
yourstr.__contains__("I")

# __setitem__
mydict = {"Oguzhan": 1, "Deniz": 2}
print(mydict)
mydict["Oguzhan"] = 3
mydict.__setitem__("Oguzhan", 1)

# __delitem__
del mydict["Deniz"]
print(mydict)

mydict.__delitem__("Oguzhan")

# __iter__ ve __next__ method
myiter = iter(mylist)
print(myiter)
print(type(myiter))

myrange = range(10)
range_iter = iter(myrange)
print(range_iter)
print(type(range_iter))

str_iter = iter(mystr)
print(str_iter)

print(next(str_iter))
print(next(str_iter))
print(next(str_iter))

list_iter = mylist.__iter__()
list_iter.__next__()

# __hash__ method
mystr = "Hello"
print(hash(mystr))

myint = 555
print(hash(myint))

myfloat = 5.2
print(hash(myfloat))

mytuple = (2, 5, 7)
print(hash(mytuple))

mylist = [2, 5, 7]
print(hash(mylist))    # TypeError: unhashable type: 'list'

mydict = {"A":1, "B":2}
print(hash(mydict))

mytuple.__hash__()

# hashlenebilen yapılar: int, float, tuple, str
# hashlenemeyen yapılar: list, dict, set

