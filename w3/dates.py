import datetime

x = datetime.datetime.now()

print(x) # yıl ay gun saat dakika saniye ve mikrosaniye
print(x.year) # yıl
print(x.strftime("%A")) # gun

# olusturma
x = datetime.datetime(2020, 5, 17)

print(x)

# strftime method ayın adını goruntuler
x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


# %a hafta içi kısa gosterim.. wed
# %A hafta içi uzun gosterim.. wednesday
# %w 0-6 arası bir sayı olarak hafta içi, 0 Pazar günüdür
# %d Ayın günü 01-31
# %b Ay adı, kısa versiyon.. dec
# %B ay adı uzun version.. december