# listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.
from functools import reduce

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ciftler = list(filter(lambda x: x % 2 == 0, liste))
print(ciftler)


reduce(lambda x, y: x + y, ciftler)

