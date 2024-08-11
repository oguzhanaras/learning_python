class Car:

    number_of_cars = 0
    total_fuel_consumed = 0
    total_fuel_bought = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.fuel = 0
        self.odometer = 0
        Car.number_of_cars += 1

    def add_fuel(self, amount):
        self.fuel += amount
        Car.total_fuel_bought += amount
        print(f"adding {amount} lt fuel. Now fuel {self.fuel}")

    def drive(self, distance):
        fuel_needed = distance * 0.05
        if self.fuel >= fuel_needed:
            self.odometer += distance
            self.fuel -= fuel_needed
            Car.total_fuel_consumed += fuel_needed
            print(f"{self.make} {self.model} drove {distance} kilometers and consumed {fuel_needed} litres")
        else:
            print("not enough fuel")


car1 = Car("renault", "toros")
car2 = Car("toyota", "camry")
car3 = Car("porsche", "taycan")
car4 = Car("volvo", "xc90")


car1.drive(10)
car1.add_fuel(2)
car2.add_fuel(2)
car3.add_fuel(3)

car1.drive(10)

car2.drive(40)

car3.drive(100)