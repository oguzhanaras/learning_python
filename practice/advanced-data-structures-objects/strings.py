"python".upper() # tum karakterleri buyuk harfe cevirir
"PYTHON".lower() # tum karakterleri kuuck harfe cevirir


# ilk parametre degistirilmek istenilen harf ikincisi yerine yazılacak olan harf
"deneme seneye geleme".replace("e", "a")

"python programlama".replace(" ", "-")

"deneme".replace("me", "sene")


# verilen değer ile başlıyorsa true değilse false dondurur
"python".startswith("p")
"python".startswith("ps") # false

# verilen değer ile bitiyorsa true değilse false dondurur
"python".endswith("on")

# belirtilen değere gore elemanları ayırır ve liste döner
"python programlama dili".split(" ")

"c-python-js-css".split("-")


# varsayılan olarak bosluk karakterini ele alır. sağ ve sol boslukları siler
"    python     ".strip()

# noktaları siler
"........ python ........".strip(".")

# iterasyon yapar ve her elemanın arasına istenilen karakteri koyar
liste1 = ["T", "B", "M", "M"]

".".join(liste1)


# count istenilen karakterin verilen değerde kaç kere oldugunu dondurur

"merhaba ben ptython ogreniyorum".count("a")

# ikinci parametre olarak hangi indeksten baslayacagını belirtebiliriz
"merhaba ben ptython ogreniyorum".count("a", 5)


# find verilen değeri baştan itibaren alar ve bulursa o indeksi döndurur. bulamazsa -1 dondurur

"merhaba ben python ogreniyorum".find("e")
"merhaba ben python ogreniyorum".find("z")

# rfind ise sondan itibaren arar
"merhaba ben python ogreniyorum".rfind("e")