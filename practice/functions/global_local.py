# pythonda bir kapsam yani scope vardır

x = 1 # bu global scope yani her yerden ulasılabilir

for a in range(1, 3):
    print(a * x)

def say():
    #local scope
    abc = 10 # local değişken
    print(abc)

say()
print(abc) # global scope üzerinden local değişkene ulasmaya calıstık hata verdi


c = 10
def func1():
    c = 2 # global ve local değişken adları aynı oldugu için bunu lokal yeni değişken olarak ele alır
    print(c)
func1()
print(c) # burda globaldeki c değişkenini yazdırır yani 10

d = 10
def func2():
    global d # globaldeki d değişkenini ele alır
    d = 3
    print(d)

func2()
print(d)
