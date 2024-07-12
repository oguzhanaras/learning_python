# 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
# a2+b2=c2


def pisagor():
    for i in range(1, 101):
        a = i ** 2
        for j in range(1, 101):
            b = j ** 2
            for k in range(1, 101):
                c = k ** 2
                if a + b == c:
                    print(i, j, k)


pisagor()