from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cow(Animal):
    def make_sound(self):
        return "Moo"

for animal in [Dog(), Cow()]:
    print(animal.make_sound())
