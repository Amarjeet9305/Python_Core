class MyClass:
    def __init__(self, laptop, attendance):
        # Mandatory parameters
        self.laptop = laptop
        self.attendance = attendance

    def display(self):
        print(f"Amarjeet My Class - Laptop: {self.laptop}, Attendance: {self.attendance}")


# Creating object with mandatory details
obj = MyClass("HP EliteBook", "Present")

# Displaying the details
obj.display()
