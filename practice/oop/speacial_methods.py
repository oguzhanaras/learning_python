class Kitap():
    pass

kitap = Kitap() # __init__ metodu otomatik olusturulup cagrılır
print(kitap)  # __str__ metodu ekrana yazdırılacak kısmı belirler

len(kitap) # hata verir len metodu tanımlanmamıstır


del kitap # __del__ metodu

print(kitap) # hata verir cunku sıldık