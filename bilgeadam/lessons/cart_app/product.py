class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False

    def __str__(self):   # informal representation  (for users)
        return f"{self.name} - Fiyat: {self.price} TL - Stok: {self.stock}"

    def __repr__(self):  # formal representation (for developers)
        return f"Product(name={self.name}, price={self.price}, stock={self.stock})"
