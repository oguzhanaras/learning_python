class Product:
    counter = 1

    def __init__(self, name, price, category, brand):
        self.name = name
        self.price = price
        self.category = category
        self.brand = brand
        self.id = Product.counter
        Product.counter += 1

    def generate_sku(self):
        spliced_cat = self.category[:3].upper()
        spliced_brand = self.brand[:3].upper()
        formatted_id = str(self.id).zfill(3)
        return f"{spliced_cat}-{spliced_brand}-{formatted_id}"

    def __str__(self):
        return self.generate_sku()


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        return "Ürün başarıyla eklendi"

    def remove_product(self, product_id=None, product_name=None):
        for i, item in enumerate(self.items):
            if (product_id is not None and item.id == product_id) or (product_name is not None and item.name == product_name):
                removed_item = self.items.pop(i)
                return f"Ürün kaldırıldı: {removed_item}"
        return "Ürün bulunamadı"

    def total_price(self):
        return sum(item.price for item in self.items)

    def __len__(self):
        return len(self.items)

    def __contains__(self, product_name):
        return any(item.name == product_name for item in self.items)

    @classmethod
    def discount(cls, cart, percentage):
        for item in cart.items:
            item.price -= item.price * (percentage / 100)


product1 = Product("Telefon", 1000, "Electronics", "Apple")
product2 = Product("Laptop", 5000, "Electronics", "Dell")


cart = Cart()
print(cart.add_product(product1))
print(cart.add_product(product2))

print("Toplam Fiyat:", cart.total_price())

print("Ürün Sayısı:", len(cart))

print(cart.remove_product(product_id=1))

print("Sepette Laptop var mı?", "Laptop" in cart)


Cart.discount(cart, 10)


print("Toplam Fiyat (İndirim Sonrası):", cart.total_price())

