# lambda işlevi kucuk anonim fonksiyondur
# Bir lambda işlevi herhangi bir sayıda bağımsız değişken alabilir, ancak yalnızca bir ifadeye sahip olabilir.


x = lambda a : a + 10
print(x(5))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))



def func(x):
    la = lambda a : a * x
    return la

degisken = func(3)

print(degisken(10))