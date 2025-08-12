class Demo:
    def __init__(self, a=None, b=None):
        if a != None and b != None:
            print("Two arguments:", a + b)
        elif a != None:
            print("One argument:", a)
        else:
            print("No arguments")

Demo()
Demo(10)
Demo(10, 20)
