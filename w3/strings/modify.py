#upper case
a = "hello world"
print(a.upper())

#lower case
a = " HELLO WORLD "
print(a.lower())

#bastaki ve sondaki bosluk kaldırma
print(a.strip())

#değiştirme
print(a.replace("H", "J"))

#split alt dizelere böler
a = "bu benim splice metodum"
x = a.split(" ")
print(x)

for i in x:
    print(i)

