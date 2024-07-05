class MyClass:
  x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.ad = name
        self.yas = age

p1 = Person("aras", 25)

print(p1.yas)
print(p1.ad)

#  __init__() işlevi, sınıf yeni bir nesne oluşturmak için her kullanıldığında otomatik olarak çağrılır.



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


class Person:
    def __init__(self, name, age):
        self.ad = name
        self.yas = age

    def sayName(self):
        print("hello:" + self.ad)

    def me(self):
        print(self.ad, self.yas)


p1 = Person("aras", 33)
p1.yas = 40
p1.sayName()
p1.me()


# 4 islem
class Dortislem:
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def topla(self):
        print(self.sayi1 + self.sayi2)

    def cikar(self):
        print(self.sayi1 - self.sayi2)

    def carp(self):
        print(self.sayi1 * self.sayi2)

    def bol(self):
        print(self.sayi1 / self.sayi2)


sayim = Dortislem(10, 5)
print(sayim.bol())
print(sayim.topla())


# del property
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age

print(p1.age) # silindiği için hata verir


# del object
del p1


class Person:
    pass
