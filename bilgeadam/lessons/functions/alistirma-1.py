# Alıştırma 1: even_check() isimli bir kullanıcı tanımlı fonksiyon (user-defined function) oluşturun.
#              Bir int sayı alsın be bu sayının çift olup olmadığını döndürsün.



def even_check(sayi):
    if sayi % 2 == 0:
        return print(f"{sayi} cift sayidir")
    else:
        return print(f"{sayi} tek sayidir")

even_check(5)
even_check(6)