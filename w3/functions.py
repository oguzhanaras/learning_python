# fonksiyonlar yalnızca cagrıldıgında calısır
# fonksiyonlar sonuc olarak veri dondurebilir
# def keyword ile function olusturulur

def sayHello():
    print("hello")

sayHello()

# arguments
def sayMyName(name):
    print("merhaba " + name)

sayMyName("aras")
sayMyName("oguz")


def info(name, age):
    print("merhaba ", name, "yaşın: ", age)

info("aras", 22)
info("oguz", 22)


# arguman sayısı belli değilse parametre yerine * koy
def myChilds(*kids):
    print("merhaba cocuklar " + kids[2])

myChilds("aras", "oguz", "han")


# key value syntax
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# defalut value belirleme
def myFunc(country = "turkey"):
    print("hello, your country is: " + country)

myFunc("norway")
myFunc()


# Bir fonksiyona herhangi bir veri türünde argüman gönderebilirsiniz (string, sayı, liste, sözlük vb.) ve fonksiyon içinde aynı veri türü olarak ele alınacaktır.
def myFunc(liste):
    for x in liste:
        print(x)

myList = ["aras", "demek", "naber"]
myFunc(myList)



# return geriye deger dondurur
def myFunc(x):
    return x * 3

print(myFunc(10))
print(myFunc(5))


# pass içerigi bos olanlara hata almamak için eklenir
def myfunction():
  pass



# Bir fonksiyonun sadece konumsal argümanlara sahip olabileceğini belirtmek için argümanlardan sonra , / ekleyin:
def my_function(x, /):
    print(x)

my_function(3)


# Bir fonksiyonun sadece anahtar kelime argümanları alabileceğini belirtmek için argümanlardan önce * ekleyin:
def my_function(*, x):
    print(x)

my_function(x = 3)


def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)





def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
