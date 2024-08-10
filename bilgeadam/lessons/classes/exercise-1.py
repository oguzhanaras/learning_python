class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"the {self.color} car has {self.mileage} miles"


car1 = Car("mavi", 20_000)
car2 = Car("kirmizi", 30_000)


print(car1)
print(car2)