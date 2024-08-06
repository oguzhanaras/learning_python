#Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.
liste = [(3, 4, 5), (6, 8, 10), (3, 10, 7)]

#Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın

def ucgen_mi(item):
    a = item[0]
    b = item[1]
    c = item[2]

    if a + b > c and a + c > b and b + c > a:
        return True

print(list(filter(ucgen_mi, liste)))

