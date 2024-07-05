# bir değişken olusturuldugu bolgenin içinde kullanılır buna kapsam denir

# local scope
def myfunc():
    x = 300
    print(x)

myfunc()
print(x)  # burası myfunc kapsamı dısında oldugu için x i tanımaz


# fonksiyon içindeki herhangi bir fonksiyon için kullanılabilir
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

# global scope ana gövdede olusturulanlar otomatik oalrak globaldir ve localde de kullanılabilir
x = 300

def myfunc():
    print(x)

myfunc()

print(x)

x = 300

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)

# Global anahtar sözcüğünü kullanırsanız, değişken global kapsama ait olur:
def myFunc():
    global x
    x = "myglobal"
    print(x)

myFunc()
print(x)


x = 300

def myfunc():
    global x
    x = 200

myfunc()

print(x)

# nonlocal
def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1())

