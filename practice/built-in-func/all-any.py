def hepsi(liste):

    # liste elemanlarının hepsi true ysa true değilse false dondurur
    for i in liste:
        if not i: #elemanlar arasında false varsa not diyerek true olacagı için if içine girer ve false dondurur
            return False
    return True

liste1 = [True, False, True, True]
liste2 = [True, True, True, True]

print(hepsi(liste1))
print(hepsi(liste2))


# tüm değerler true ise true herhangi biri false ise false dondurur
all(liste1)
all(liste2)

# tum degerler false ise false herhangi bir true varsa true dondurur

print(any(liste1))
print(any(liste2))