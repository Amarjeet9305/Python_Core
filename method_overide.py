class Shape:
    def area(self):
        return "Area not defined"

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5  # πr²

class Square(Shape):
    def area(self):
        return 4 * 4  # a²

for shape in [Circle(), Square()]:
    print(shape.area())
