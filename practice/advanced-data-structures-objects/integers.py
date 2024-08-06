bin(10) # 2lik tabanda yazar

hex(202) # 16lık tabanda yazar

abs(-4) # mutlak deger alir


round(4.6) # sayıyı yuvarlar
round(4.5) # 4.5 ve altını 4 e yukarısını 5 e yuvarlar

round(4.2239, 3) # sayıyı kusuratı 3 basamaklı olcak sekilde ele alır ve yuvarlar

max(3, 4, 5) # içindeki en buyuk veriyi dondurur
min(3, 5, 7, -5, 6) # içindeki en kucuk sayıyı dondurur

# min ve max fonksiyonuna sayılar liste ya da demet verilebilir
max([1, 2, 3, 4, 5,])
min((1, 2, 3, 4, 5))

# sum fonksiyonuna liste demet vb şeklinde değer yani iterable obje verilmesi gerekir
sum(3, 4) # hata

sum([1, 2, 3, 4, 5, 6])
sum((1, 2, 3, 4, 5, 6))

sum(["a", "b", "c"]) # hata
sum("11") # hata verir
sum("dene") # hata verir

pow(2, 4) # üssünü hesaplar ve 2 parametre alır. birincisi taban ikincisi üs

print(2 ** 4)

