def main_func(islem_adi):

    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpim(*args):
        carpma = 1
        for i in args:
            carpma *= i
        return carpma

    if islem_adi == "toplama":
        return toplama
    else:
        return carpim


toplama_fonk = main_func("toplama")

toplama_fonk(1, 2, 3, 4)

carpma_fonk = main_func("carpim")

carpma_fonk(1, 2, 3, 4)


# fonksiyonu arguman olarak gondermek
def toplama(a, b):
    return a + b


def cikarma(a, b):
    return a - b


def hesapla(func1, func2, islem_adi):
    if islem_adi == "toplama":
        print(toplama(3, 5))
    elif islem_adi == "cikarma":
        print(cikarma(10, 3))
    else:
        print("hatalı tuslama")


hesapla(toplama, cikarma, "toplama")
hesapla(toplama, cikarma, "cikarma")
