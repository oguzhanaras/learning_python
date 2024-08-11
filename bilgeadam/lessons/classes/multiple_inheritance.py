class Mammal:

    def __init__(self, name):
        self.name = name

    def mammal_info(self):
        print("memeliler doğum yapabilir")


class WingedAnimal:

    def winged_animal_info(self):
        print("kanatlı hayvanlar ucabilir")


class Bat(Mammal, WingedAnimal):

    def bat_info(self):
        print("yarasalar kanatlı memelilerdir")


bat1 = Bat("bat1")

bat1.bat_info()
bat1.mammal_info()
bat1.winged_animal_info()


isinstance(bat1, Mammal)
isinstance(bat1, WingedAnimal)
isinstance(bat1, Bat)

issubclass(Bat, Mammal)
issubclass(Bat, Bat)
issubclass(Bat, WingedAnimal)
issubclass(Bat, (Mammal, WingedAnimal))

