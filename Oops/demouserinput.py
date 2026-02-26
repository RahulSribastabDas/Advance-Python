class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def greet(self):
        print(f"\nHello, I am {self.name}")
        print(f"I am {self.age} years old")
        print(f"My branch is {self.branch}")

# Taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
branch = input("Enter your branch: ")

# Creating object using user input
s1 = Student(name, age, branch)
s1.greet()