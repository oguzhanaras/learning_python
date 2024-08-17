class Person:

    number_of_people = 0
    person_list = []

    def __init__(self, name):
        self.name = name
        Person.add_person(self.name)

    @classmethod
    def num_of_people(cls):
        """ bu classmethod, sınıfın kaç tane ornegi oldugunu dondurur."""
        return cls.number_of_people

    @classmethod
    def add_person(cls, name):
        """bu classmethod, bir kişi eklendiğinde number of people değerini artırır"""
        cls.number_of_people += 1
        cls.person_list.append(name)

    def person_info(self):
        return f"my name is {self.name}"


person1 = Person("oguzhan")
person2 = Person("deniz")
person3 = Person("yunus")

print(Person.number_of_people)
print(Person.num_of_people())
print(Person.person_list)



