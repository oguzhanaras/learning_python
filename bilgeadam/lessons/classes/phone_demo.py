class BasePhone:

    def __init__(self, id, brand, model, price):
        self.id = id
        self.brand = brand
        self.model = model
        self.price = price

    def show_info(self):
        return f"id: {self.id}\nBrand: {self.brand}\nModel: {self.model}\nPrice: {self.price}"

    def phone_ring_sound(self):
        print("common ring sound")

class Samsung(BasePhone):

    def __init__(self, id, brand, model, price, operating_system):
        super().__init__(id, brand, model, price)
        self.operating_system = operating_system

    def show_info(self):
        print(super().show_info(), f"\nos: {self.operating_system}")

    def phone_ring_sound(self, sound):
        print(f"phone ring sound: {sound}")


samsung1 = Samsung(1, "samsung", "note2", 700, "android")
samsung2 = Samsung(2, "samsung", "s24", 800, "android")

samsung1.show_info()
samsung2.show_info()