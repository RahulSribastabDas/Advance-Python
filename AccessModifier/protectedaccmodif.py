class Animal:
    def __init__(self, species, sound):
        self._species = species  # Protected variable
        self._sound = sound      # Protected variable

class Dog(Animal):
    def __init__(self, breed):
        # Calling the parent constructor
        super().__init__("Dog", "Bark")
        self.breed = breed

    def display_details(self):
        # Accessing protected variables from the parent class
        print(f"Species: {self._species}")
        print(f"Sound: {self._sound}")
        print(f"Breed: {self.breed}")

# Creating a subclass object
my_dog = Dog("Golden Retriever")
my_dog.display_details()