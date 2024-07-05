#boollar true ya da false değer döndürür

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 100
b = 90

if b > a:
    print("b is great")
else:
    print("a is great")

#herhangi bir değeri olanlar true döner
print(bool("hello"))
print(bool(15))
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])



#içi boş olanlar false döndürür
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


#fonksiyonlar bool değer döndürebilir
def myFunc():
    return True

if myFunc():
    print("dönen değer true")
else:
    print("donen deger false")

#istenilen tür de olup olmadıgını kontrol etme
x = 200
print(isinstance(x, int))