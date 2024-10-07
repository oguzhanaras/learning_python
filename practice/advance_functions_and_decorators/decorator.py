def ekstra(func):
    def wrapper(sayilar):
        ciftler = []
        ciftler_toplam = 0
        tekler = []
        tekler_toplam = 0
        for sayi in sayilar:
            if sayi % 2 == 0:
                ciftler.append(sayi)
                ciftler_toplam += sayi
            else:
                tekler.append(sayi)
                tekler_toplam += sayi

        if ciftler:
            print(f"çiftler ortalaması {ciftler_toplam / len(ciftler)}")
        if tekler:
            print(f"tekler ortalaması {tekler_toplam / len(tekler)}")

        sonuc = func(sayilar)
        print(sonuc)

    return wrapper


@ekstra
def ortalama(sayilar):
    toplam = 0

    for sayi in sayilar:
        toplam += sayi
    return f"genel ortalama {toplam / len(sayilar)}"


ortalama((1, 2, 3, 4, 5, 6))
