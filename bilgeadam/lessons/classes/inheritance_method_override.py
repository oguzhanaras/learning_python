class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"i am {self.name} and i am {self.age} years old")

    def speak(self):
        print("i dont know what to say")


class Cat(Pet):
    def color(self, color):
        print(f"my color is {color}")

    def speak(self):
        print("meow meow")

daisy = Cat("daisy", 2)

daisy.speak()


class Dog(Pet):
    def __init__(self, name, age, size):
        Pet.__init__(self, name, age)
        self.size = size

    def speak(self):
        print("woof")

    def body(self):
        print(f"the size of {self.name} is {self.size}")

coco = Dog("coco", 3, "small")

print(coco.name, coco.age, coco.size)
coco.speak()
coco.body()
coco.show()


# isinstance(object, class)
print(isinstance(coco, Dog))
print(isinstance(coco, Cat))
print(isinstance(coco, Pet))

# issubclass(class, classinfo)
print(issubclass(Pet, Cat))
print(issubclass(Cat, Pet))
print(issubclass(Cat, Cat))

