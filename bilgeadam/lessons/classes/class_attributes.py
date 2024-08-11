class Person:
    country = "usa"
    number_of_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.number_of_people += 1
        self.id = Person.number_of_people


person1 = Person("tim", 19)

person2 = Person("jill", 20)

print(person2.id)



