def kareleri_al():
    sonuc = []

    for i in range(1, 6):
        sonuc.append(i)
    return sonuc


print(kareleri_al())


# generatorler bellekte yer tutmaz
def kareleri_al2():
    for i in range(1, 6):
        yield i ** 2


generator = kareleri_al2()
iterator = iter(generator)

next(iterator)