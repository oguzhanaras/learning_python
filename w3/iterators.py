# Yineleyici, sayılabilir sayıda değer içeren bir nesnedir.

#Yineleyici, üzerinde yineleme yapılabilen bir nesnedir, yani tüm değerler arasında gezinebilirsiniz.

#Teknik olarak, Python'da bir yineleyici, __iter__() ve __next__() yöntemlerinden oluşan yineleyici protokolünü uygulayan bir nesnedir.

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Dizeler bile yinelenebilir nesnelerdir ve bir yineleyici döndürebilirler:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# classlarda iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# ornek
class Islem:
    def __init__(self, sayi):
        self.sayi = sayi

    def __iter__(self):
        self.num = self.sayi
        return self

    def __next__(self):
        x = self.num
        self.num += 1
        return x

myObj = Islem(0)
yinele = iter(myObj)

print(next(yinele))

# stopieration yinelemeyi durdurur
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)