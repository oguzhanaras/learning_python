# Alıştırma
# Müşteriler farklı türde ve sayıda ürün satın alabilirler. Her ürünün adı, fiyatı ve miktarı
# olacaktır. Ayrıca, faturaya özel notlar veya kampanya kodları gibi ekstra bilgiler de eklenebilir.

urun1 = {"ad": "Laptop", "fiyat": 1000, "miktar": 1}
urun2 = {"ad": "Telefon", "fiyat": 500, "miktar": 2}
urun3 = {"ad": "Klavye", "fiyat": 100, "miktar": 3}
urun4 = {"ad": "Fare", "fiyat": 50, "miktar": 2}

def fatura_olustur(*urunler, **ekstra):
    toplam = 0
    for urun in urunler:
        urun_tutar = urun["miktar"] * urun["fiyat"]
        toplam += urun_tutar
        print(f"{urun['ad']} {urun['miktar']} {urun_tutar}")

    for key, value in ekstra.items():
        print(f"{key}: {value}")
        if key == "kampanya" and value == "YAZ2024":
            indirim = toplam * 0.1
            print(f"yaz 2024 kampanyası ile ${indirim} indirim uygulandı")
            toplam -= indirim
        elif key == "kampanya" and value == "MOTHERSDAY":
            indirim = toplam * 0.15
            print(f"MOTHERSDAY kampanyası ile ${indirim} indirim uygulandı")
            toplam -= indirim
        if key == "kargo" and value == "express":
            print("express kargo fiyatı")
            toplam += 25
    print(f"toplam fatura tutarı: ${toplam}")

fatura_olustur(urun1, urun2, urun3, urun4)
fatura_olustur(urun1, urun2, urun3, urun4, kampanya="YAZ2024", kargo="express")

