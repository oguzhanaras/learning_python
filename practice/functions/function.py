"""
syntax def function_name(parameter1, parameter2....(option))
    function block
    do it something
    return value (option)
"""

def sayHello():
    print("Hello")
def selamla(name):
    print("merhaba", name)

sayHello()
selamla("aras")


def toplama(bir, iki, uc):
    toplam = bir + iki + uc
    print(toplam)

toplama(1,2,3)

def fac(sayi):
    faktoriyel = 1
    if sayi == 0 or sayi == 1:
        print(faktoriyel)
    else:
        while sayi >= 1:
            faktoriyel *= sayi
            sayi -= 1
        print(faktoriyel)

fac(5)
fac(6)
fac(0)
fac(1)