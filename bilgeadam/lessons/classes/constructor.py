class Dog:
    def __init__(self, name, age):    # yapıcı metot
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

dog1 = Dog("Miles", 5)
dog2 = Dog("doberman", 3)
dog3 = Dog("kangal", 6)


print(dog1.name, dog1.age)
print(dog2.name, dog2.age)


dog2.speak("hav")
print(dog2.description())


# upgrade

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.health_record = []

    def change_weight(self, new_weight):
        self.weight = new_weight

    def __str__(self):
        if self.weight is None:
            return f"{self.name}({self.age})"
        return f"{self.name}({self.age}), {self.weight}kg"


mars = Dog("Mars", 8)
print(mars)

mars.change_weight(25)

print(mars)

mars.health_record.append("right leg is broken")
mars.health_record.append("a bruise in the neck")

print(mars.health_record)
