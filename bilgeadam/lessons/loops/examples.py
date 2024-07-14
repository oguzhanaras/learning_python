# alıstırma 1: while dongusu kullanarak fibonacci serisi 0-50

f0, f1 = 0, 1
fibonacci = []

while f0 < 50:
    fibonacci.append(f0)
    print(fibonacci)
    f0, f1 = f1, f0 + f1

print(fibonacci)


# alıstırma2 0-100 arasında 100 den azalacak sekilde ekrana yazdır. 50 ye gelince breakle sonlandır

for i in range(100, 0, -1):
    print(i)
    if i == 50:
        break

