print("""
tam bolen bulma programı
cıkmak için q e basın
""")

def tamBolen(sayi):
    my_list = [1]
    for i in range(2, sayi + 1):
        if sayi % i == 0:
            my_list.append(i)
    return my_list

while True:
    sayi = input("bir sayi gir")
    if sayi == "q":
        print("program sonlanıyor")
        break
    else:
        sayi = int(sayi)
        print("tam bolenler", tamBolen(sayi))