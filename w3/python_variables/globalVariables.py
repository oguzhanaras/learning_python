# fonksiyon dısında olusturulan degiskenlerin hepsi globaldir
x = "awesome"

def myfunc():
    print("python is " + x)

myfunc()

#global ve yerel degiskenler birbirinden bagımsız calısır
a = "my global"

def myfunction():
    a = "my local"
    print(a)

myfunction()
print(a)

#bir fonksiyon icinde global degisken olusturmak icin global anahtar kelimesi kullanılmalıdır
def myfonk():
    global x
    x = "fantastic"
    print("in local: ", x)

myfonk()
print("in global: ", x)