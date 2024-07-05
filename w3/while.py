# while dongusu kosul dogru oldugusurece devam eder
i = 1
while i < 10:
    print(i)
    i += 1

# deger arttırılmazsa dongu cıkmaza girer
i = 0
while i < 5:
    print(i) # sonsuza kadar bastırır

# break kosul dogru olsa bile donguyu durdurur
i = 1

while i < 5:
    print(i)
    if i == 3:
        break
    i += 1

# continue o sırayı atlar ve devam eder. mesela 1-5 e kadar yazdıralım fakat 3 olmasın
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# while else
i = 1

while i < 6:
    print(i)
    i += 1
else:
    print("sayı 6 dan kucuk değil")