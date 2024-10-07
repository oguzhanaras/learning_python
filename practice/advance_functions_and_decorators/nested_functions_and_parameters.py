def myfunc(*args):
    for i in args:
        print(i)


myfunc(1, 2, 3, 4, 5)


def func2(**kwargs):
    for i in kwargs.values():
        print(i)


func2(name="oguz", surname="aras")


# fonksiyonları değişken olarak tanımlama
def selamla(isim):
    print("selam", isim)


selamla("aras")

# degiskene selamla fonksiyonunu eşitliyoruz
merhaba = selamla

del selamla # selamla fonksiyonunu siliyoruz

print(type(merhaba))

merhaba("aras") # selamla fonksiyonu silindiği halde merhaba selamla olarak calısır.


# nested (içiçe) fonksiyonlar
def big_func():

    def small_func():
        print("burası kucuk fonksiyon")
    small_func()
    print("burası buyuk fonksiyon")


big_func()


def calculate(*args):
    print(args)

    def addition(args):
        result = 0
        for i in args:
            result += i
        return result
    print(addition(args))


calculate(1, 2, 3, 4, 5, 6)
