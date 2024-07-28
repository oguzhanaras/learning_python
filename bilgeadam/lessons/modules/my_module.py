nums = list(range(100))

e = 2.718281828459045

def doubled(x):
    return x * 2


def asal(sayi):
    if sayi == 1:
        return "asal değil"
    if sayi == 2:
        return "asal"
    for i in range(2, sayi):
        if sayi % i == 0:
            return "asal değil"
    return "asal"