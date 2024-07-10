# alisirma 1 mail kontrol
i = 1
while i == 1:
    email = str(input("Enter your email: "))
    if email.count("@") == 1:
        if (
            email.split("@")[0]
            and
            email.split("@")[1].endswith(".com") or email.split("@")[1].endswith(".org") or email.split("@")[1].endswith(".net")
        ):
            print(email.split("@")[0] + "@" + email.split("@")[1])
            break
    else:
        print("lutfen 1 adet  @ isareti koyun")

# alistirma-2 string içndeki harf sayısı bulma
cumle = str(input("cumleni gir: "))
harf = str(input("cumlede hangi harfi aramak istiyorsun: "))

print(cumle.count(harf))

# alistirma-3
yariscilar = [("Lewis Hamiltion", 312), ("Max Verstappen", 315)]

if yariscilar[0][1] < yariscilar[1][1]:
    print("Lewis Hamiltion kazandı")
else:
    print("Max Verstappen kazandı")


# alistirma-4
takim1 = str(input("takim1 gir: "))
takim2 = str(input("takim2 gir: "))

i = 1
takim1_list = []
takim2_list = []
while i < 5:
    print(f"{takim1} skorlarını gir")
    while i < 5:
        takim1_list.append(int(input(f"{i}.çeyrek skoru gir: ")))
        i += 1
    print(f"{takim2} skorlarını gir")
    i = 1
    while i < 5:
        takim2_list.append(int(input(f"{i}.çeyrek skoru gir: ")))
        i += 1
    if sum(takim1_list) > sum(takim2_list):
        print(f"{takim1} kazandı. puan: {sum(takim1_list)}")
    else:
        print(f"{takim2} kazandı. puan: {sum(takim2_list)}")