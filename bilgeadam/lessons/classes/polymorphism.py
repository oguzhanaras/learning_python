# aynı arayuzu paylasan farklı nesnelerin farklı davranısları sergilemesine denir

class Shape:

    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):

    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return self.edge ** 2


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


rectangle1 = Rectangle(3, 7)
square1 = Square(4)
triangle1 = Triangle(6, 3)

shapes = [rectangle1, square1, triangle1]

for shape in shapes:
    print(f"the area: {shape.area()}")




class PaymentProcessor:

    def process_payment(self, amount):
        raise NotImplementedError("subcalsses sholud implement this method")


class CreditCardPayment(PaymentProcessor):

    def process_payment(self, amount):
        print(f"processing credit card payment of {amount}")


class PayPalPayment(PaymentProcessor):

    def process_payment(self, amount):
        print(f"processing credit card payment of {amount}")


class CryptoPayment(PayPalPayment):

    def process_payment(self, amount):
        print(f"processing credit card payment of {amount}")


def process_customer_payment(payment_processor, amount):
    payment_processor.process_payment(amount)


credit_card = CreditCardPayment()
paypal = PayPalPayment()
crypto = CryptoPayment()

process_customer_payment(credit_card, 100)




