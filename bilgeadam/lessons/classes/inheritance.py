# inheritance (kalıtım, miras)

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"i am {self.name} and i am {self.age} years old")

    def speak(self):
        print("i dont know what to say")


pet = Pet("max", 4)
pet.show()
pet.speak()

class Cat(Pet):
    def color(self, color):
        print(f"i am a cat. my color is {color}")

pisi = Cat("pisi", 2)

print(pisi.name, pisi.age)

pisi.color("white")
pisi.show()
pisi.speak()