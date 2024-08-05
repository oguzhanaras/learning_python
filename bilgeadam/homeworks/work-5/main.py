# Veri Yapısı: Elektronik ürünlerin stok durumları, birim fiyatları ve toplam satış miktarları
products = {
    'Smartphone': {'stock': 50, 'price': 1000, 'sales': 0},
    'Laptop': {'stock': 30, 'price': 2000, 'sales': 0},
    'Headphone': {'stock': 100, 'price': 100, 'sales': 0},
    'TV': {'stock': 20, 'price': 1500, 'sales': 0},
    'Camera': {'stock': 25, 'price': 800, 'sales': 0},
    'Smartwatch': {'stock': 60, 'price': 300, 'sales': 0},
    'Speaker': {'stock': 40, 'price': 150, 'sales': 0},
    'Tablet': {'stock': 35, 'price': 400, 'sales': 0}
}

# make_sale(product_name, quantity) fonksiyonu yazın.
# Fonksiyon, ürün adı (product_name) ve satılan miktarı (quantity) girdi olarak alacaktır.
# - Eğer ürün adı sistemde yoksa, "Product not found" çıktısı vermeli.
# - Eğer yeterli stok yoksa, "Insufficient stock" çıktısı vermeli.
# - Eğer satış başarılıysa, "Total Sale: [Toplam Tutar]₺" çıktısı vermeli.
# sales_analysis() fonksiyonu yazın.  Fonksiyon, toplam elde edilen geliri (toplam ciro)
# ve en çok satan ürünü hesaplamalıdır.


def make_sale(product_name, quantity):

    if product_name in products:
        product = products[product_name]

        if product["stock"] >= quantity:
            product["sales"] += quantity
            product["stock"] -= quantity
            print(f"sales completed. amount: {quantity * product["price"]}")
            sales_analysis(product, quantity * product["price"])
        else:
            return "insufficient stock"
    else:
        return "product not found"


total = 0
def sales_analysis(product_name, revenue):
    global total
    total += revenue
    p_max = 0
    p_name = ""
    for key, value in products.items():
        if value["price"] * value["sales"] > p_max:
            p_max = value["price"] * value["sales"]
            p_name = key
    print(f"""
    
best selling product {p_name}, the money made from this product: {p_max}
total selling price of all products: {total}
""")


while True:
    islem = input("programdan cıkmak icin 'q' ya, satis yapmak icin 's' ye basin")
    if islem == "q":
        print("program sonlanıyor")
        break
    elif islem == "s":
        urun_adi = input("satis eklemek istediğiniz urun adi girin")
        adet = int(input("kac adet satildiğini girin"))
        make_sale(urun_adi, adet)
    else:
        print("hatali islem tuslaması")


