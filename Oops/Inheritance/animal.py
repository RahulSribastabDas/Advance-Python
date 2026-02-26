# Parent class (Base class or Superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

# Child class (Derived class or Subclass)
class Dog(Animal):
    def speak(self):
        # Calls the parent's speak method and adds more
        parent_sound = super().speak() 
        return f"{parent_sound}, but mostly Woof!"
    
    def bark(self):
        return "Woof!"

# Creating an instance of the child class
my_dog = Dog("Buddy")

# Accessing inherited attribute and methods
print(f"{my_dog.name}: {my_dog.speak()}") # Output: Buddy: Some sound, but mostly Woof!
print(f"Dog action: {my_dog.bark()}")      # Output: Dog action: Woof!