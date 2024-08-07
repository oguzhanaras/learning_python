#"şiir.txt" şeklinde bir dosya oluşturun ve içinde şu satırlar yer alsın.
#Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek
# bir string oluşturun ve bu string'i ekrana yazdırın.


with open("siir.txt", "r", encoding="utf-8") as file:

    siir = file.read()
    satirlar = siir.split("\n")

    akrostis = ""

    for satir in satirlar:
        akrostis += satir[0]

    print(akrostis)

