import ui
from cart import Cart
from product import Product


def main():
    products = [
        Product("iPhone", 39999, 15),
        Product("Dell", 50999, 8),
        Product("Sony", 12499, 25),
        Product("Samsung", 19999, 12),
        Product("Apple", 17999, 20),
        Product("Logitech", 5999, 30)
    ]

    mycart = Cart()

    while True:
        choice = ui.get_user_choice()

        if choice == 1:
            ui.display_products(products)

        elif choice == 2:
            product, quantity = ui.get_product_choice(products)
            if product and quantity > 0:
                if mycart.add(product, quantity):
                    print(f"{quantity} adet {product.name} sepete eklendi.")
                else:
                    print(f"{product.name} - Stok yetersiz!")

        elif choice == 3:
            product, quantity = ui.get_product_choice(products)
            if mycart.remove(product, quantity):
                print(f"{quantity} adet {product.name} sepetten çıkarıldı.")
            else:
                print(f"{product.name} - Sepette yeterli miktar yok veya ürün mevcut değil.")

        elif choice == 4:
            print(mycart)

        elif choice == 5:
            print(f"Toplam Tutar: {mycart.total()} TL")

        elif choice == 6:
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz Seçim!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

