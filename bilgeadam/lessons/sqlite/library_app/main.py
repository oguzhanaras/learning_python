from bilgeadam.lessons.sqlite.library_app import utils

while True:
    print("""
    kutuphane uygulamamıza hosgeldiniz
    1- uye ekle
    2- uyeleri listele
    3- kitap ekle
    4- kitapları listele
    5-kitap odunc al
    6- kitap teslim et
    7- cikis
""")

    try:
        islem = input("islem turunu seciniz(1-7): ")

        if islem == "7":
            print("program sonlanıyor...")
            break
        elif islem == "1":
            uye_adi = input("uye adı girin: ")
            uye_email = input("uye email girin: ")
            uye_yas = int(input("uye yas bilgisini giriniz: "))
            if utils.add_member(uye_adi, uye_email, uye_yas):
                print("yeni uye kaydı olusturuldu")
            else:
                print("kayıt olustururken hata")
        elif islem == "2":
            uyeler = utils.member_list()
            for uye_id, uye_adi, email, yas in uyeler:
                print(f"uye id: {uye_id}\nuye adı: {uye_adi}\nuye mail: {email}\nyas: {yas}")
        elif islem == "3":
            kitap_adi = input("kitap adı giriniz: ")
            yazar = input("yazar adını giriniz: ")
            yayin_yili = input("yayın yılını giriniz: ")
            if utils.add_book(kitap_adi, yazar, yayin_yili):
                print("yeni kitap kaydı olusturuldu")
        elif islem == "4":
            kitaplar = utils.show_books()
            for kitap_id, kitap_adi, yazar, yayin_yili in kitaplar:
                print(f"{kitap_id}, {kitap_adi}, {yazar}, {yayin_yili}")
        elif islem == "5":
            uye_id = int(input("üye id giriniz: "))
            kitap_id = int(input("kitap id giriniz: "))
            if utils.lenad_book(uye_id, kitap_id):
                print(f"{uye_id} numaralı uye {kitap_id} numaralı kitabi odunc aldı")
        elif islem == "6":
            uye_id = int(input("üye id giriniz: "))
            kitap_id = int(input("kitap id giriniz: "))
            utils.delivery_book(uye_id, kitap_id)
        else:
            print("hatali işlem")
    except:
        pass
