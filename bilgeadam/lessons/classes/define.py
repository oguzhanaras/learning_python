class Dog:
    # attributes
    name = "Mars"
    age = 5

    # methods

    def bark(self):
        print("hav hav")

    def run(self):
        print("dog is running")

    def eat(self, food):
        print(f"dog is eating {food}")


print(Dog)
print(type(Dog))

## instance
dog1 = Dog()
dog2 = Dog()


print(f"dog1 name is {dog1.name}")

dog2.name = "saturn"

print(f"dog1 name is {dog2.name}")


# call methods
dog1.bark()

dog2.run()

dog1.eat("bone")



class Dog:

    # attributes
    name = "Mars"
    age = 5

    # methods

    def bark(self):
        print("hav hav")

    def run(self):
        print(f"{self.name} is running")

    def eat(self, food):
        print(f"dog is eating {food}")

    def sleep(cls):
        print("dog is sleeping")


dog1 = Dog()
dog2 = Dog()
dog3 = Dog()


#instance
dog1.bark()
dog1.run()
dog1.sleep()

#class methods
Dog.name
Dog.age