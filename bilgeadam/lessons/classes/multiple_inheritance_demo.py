class Creature:

    def __init__(self, name):
        self.name = name

    def attack(self):
        pass

    def defence(self):
        pass


class FlyingCreature(Creature):

    def fly(self):
        print(f"{self.name} flying")


class AquaticCreature(Creature):

    def swim(self):
        print(f"{self.name} swimming")


class Dragon(FlyingCreature, AquaticCreature):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def attack(self):
        print(f"{self.name} ates puskurtuyor")

    def defence(self):
        print(f"{self.name} kanatlarıyla kendini savunuyor")


dragon1 = Dragon("ejderya", "red")


dragon1.fly()
dragon1.attack()
dragon1.defence()
dragon1.swim()

