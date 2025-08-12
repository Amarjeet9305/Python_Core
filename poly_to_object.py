#Write a program on Using Polymorphism method
class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

def animal_sound(animal):
    print(animal.speak())
# Function Instance calling
animal_sound(Dog())
animal_sound(Cat())
