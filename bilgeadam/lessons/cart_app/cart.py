from collections import defaultdict
from product import Product


class Cart:
    def __init__(self):
        self.items = defaultdict(lambda: {"price": 0, "quantity": 0})

    def add(self, product: Product, quantity: int):
        if product.update_stock(quantity):
            self.items[product]["quantity"] += quantity
            self.items[product]["price"] = product.price
            return True
        return False

    def remove(self, product, quantity=1):
        if product and quantity:
            return True
        return False

    def total(self):
        grand_total = 0
        for item in self.items.values():
            subtotal = item["price"] * item["quantity"]
            grand_total += subtotal
        return grand_total

    def display(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __len__(self):
        return len(self.items)

    def __contains__(self, item: Product) -> bool:
        return item in self.items
