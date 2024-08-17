def get_user_choice():
    print("1. Ürünleri Listele")
    print("2. Sepete Ürün Ekle")
    print("3. Sepetten Ürün Çıkar")
    print("4. Sepete Git")
    print("5. Toplam Tutarı Hesapla")
    print("6. Çıkış Yap")
    user_choice = int(input("Bir Seçenek Seçiniz: "))
    return user_choice


def display_products(products: list):
    print("\nÜrünler:")
    for product in products:
        print(product)


def get_product_choice(products: list):
    product_name = input("Ürün ismi: ")
    product_quantity = int(input("Miktar: "))

    for product in products:
        if product_name == product.name:
            return product.name, product_quantity
        else:
            continue
    p_name = False
    quantity = False
    return p_name, quantity
