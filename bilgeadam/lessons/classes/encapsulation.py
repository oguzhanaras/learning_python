# bir sınıfın iç yapısını dış dünyadan saklamak için kullanılan yapıdır

class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model
        # protected attr
        self._odometer = 1000
        #private attr
        self.__fuel = 50


car1 = Car("toyota", "camry")

car1._odometer = 1500
car1.__fuel   # attr error.


class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self._odometer = 1000
        self.__fuel = 50

    def get_fuel(self):
        return self.__fuel

    def set_fuel(self, amount):
        self.__fuel += amount

    def drive(self, distance):
        if self.__fuel > distance * 0.05:
            self.__fuel -= distance * 0.05
        else:
            print("you cant drive")


car2 = Car("ford", "mustang")
car2.get_fuel()
car2.drive(100)
car2.get_fuel()
car2.set_fuel(20)
car2.get_fuel()