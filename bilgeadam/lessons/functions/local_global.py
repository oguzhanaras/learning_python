# local variable

def example():
    a = 10
    print("fonksiyon içi yani local değişken", a)
example()
print(a) # a local oldugu için not defined hatası verir


# global variable
b = 5

def example_global():
    global b # global keyword u local değişkeni global yapar
    b += 2
    print("fonksion içi b:", b)

example_global()
print(b)