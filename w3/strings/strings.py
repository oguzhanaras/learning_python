# stringler (dizeler) çift ya da tek tırnak ile gosterilebilir
print("hello")
print('hello')

# tırnak içinde tırnak kullanımı
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# cok satırlı dize
a = """aaskf asd d dssss
s s da   sdd ad"""
print(a)

# dizeler aynı zamanda bir dizidir
a = "hello world"
print(a[0])

#dizelerde döngü
for x in "apple":
    print(x)

deger = "bu benim degerim"

for i in deger:
    print(i)

# bir dizenin uzunlugu
dize = "bu benim uzunlugum"
print(len(dize))

# bir dizede istenilen ifadenin bulunup bulunmadıgını kontrol etme
lorem = " bu benim istenilen kelimeyi bulma özelliğim. beni kontrol et"
print("kontrol" in lorem)
print("benden" not in lorem)

# if ile kullanımı
if "kontrol" in lorem:
    print("yes kontrol var")

if "kontrol" not in lorem:
    print("yes kontrol yok")