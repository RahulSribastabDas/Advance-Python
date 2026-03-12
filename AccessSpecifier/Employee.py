class Employee:
    # Constructor
    def __init__(self, name, age):
        self.name = name  # Public variable
        self.age = age    # Public variable

    # Public method
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object
emp = Employee("Alice", 28)

# Accessing public variables and methods directly from outside the class
print(f"Accessing directly -> Name: {emp.name}")
emp.display_info()