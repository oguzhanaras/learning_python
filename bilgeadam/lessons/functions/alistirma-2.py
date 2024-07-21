# Alıştırma 2: even_check_list() isimli bir kullanıcı tanımlı fonksiyon oluşturun.
#              Verilen bir listenin içerisinde bir çift sayı olup olmadığını kontrol etsin.

mylist1 = [1, 3, 5, 7, 8, 9]  # True
mylist2 = [1, 3, 5, 7, 9, 11]  # False

def even_check_list(list):
    for i in list:
        if i % 2 == 0:
            return True
    return False

print(even_check_list(mylist1))
print(even_check_list(mylist2))