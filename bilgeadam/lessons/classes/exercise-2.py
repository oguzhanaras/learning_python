class Dog:

    def __init__(self, name, age, city=None):
        self.name = name
        self.age = age
        self.city = city

    def location(self, new_city):
        self.city = new_city

    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        if self.city == None:
            return f"{self.name} {self.age} yasındadır"
        else:
            return f"{self.name} {self.age} yasındadır ve {self.city}'da yasıyor."

dog1 = Dog("mars", 25)

print(dog1)

dog1.set_age(27)
print(dog1)

dog1.city = "ankara"

print(dog1)

