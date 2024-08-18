# abc modulunden ABC sınıfı ve dekoratoru yuklenır
from abc import ABC, abstractmethod

# widget adında soyur bir sınıf (abstract class) olusturalım

class Widget(ABC):

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def press(self):
        pass


class Button(Widget):

    def draw(self):
        print("drawing a bottle")


btn1 = Button() #TypeError: Can't instantiate abstract class Button without an implementation for abstract method 'press'

class Button(Widget):

    def draw(self):
        print("drawing a bottle")

    def press(self):
        print("pressing a button")

btn2 = Button()

