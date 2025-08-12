class Character:
    def attack(self):
        print("Basic attack")

class Warrior(Character):
    def attack(self):
        print("Sword attack")

class Mage(Character):
    def attack(self):
        print("Magic attack")

players = [Warrior(), Mage()]
for p in players:
    p.attack()
