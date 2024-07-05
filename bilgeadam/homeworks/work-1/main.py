# sıcaklık dönüştürücü celsius to fahrenheit
celsius = float(input("celsius değerinde sicaklik gir: "))
fahr = celsius * 1.8 + 32
print("celsius:", celsius, "fahrenheit:", fahr)



# kilometre to mile
km = float(input("km değerinden mesafe giriniz: "))
mile = km * 0.621371
print("km:", km, "mile:", mile)


# üçgen alan
taban = int(input("taban değerini giriniz: "))
yukseklik = int(input("yukseklik değerini giriniz: "))
alan = taban * yukseklik / 2
print("alan: ", alan)



# ortalama sıcaklık
sehir = str(input("sehir gir: "))
max_sicaklik = float(input("max_sicaklik gir: "))
min_sicaklik = float(input("min_sicaklik gir: "))
ort_sicaklik = (max_sicaklik + min_sicaklik) / 2

print("sehir", sehir, "ortalama sıcaklık: ", ort_sicaklik)