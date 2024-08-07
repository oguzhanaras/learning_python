#Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun.
# Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.


with open("mailler.txt", "r", encoding="utf-8") as file:

    dosya = file.read()

    mailler = dosya.split("\n")
    print(mailler)

    for mail in mailler:
        if mail.find("@") > 0 and mail.endswith(".com"):
            print(mail)
