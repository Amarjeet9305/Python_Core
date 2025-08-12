# To print first and last name by calling creating the class instance
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display_info(self):
        full_name = self.first_name + self.last_name  
        print(f"Full Name: {full_name}")
        print("Hello, welcome SRDT Training program!")

# Create a Instance
p = Person("Amar", "Jeet")

# Accessing method
p.display_info()



    
