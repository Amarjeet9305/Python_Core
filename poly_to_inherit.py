class Vehicle:
    def start(self):
        print("Vehicle started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

class Car(Vehicle):
    def start(self):
        print("Car started")

for v in [Bike(), Car()]:
    v.start()
