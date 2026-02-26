#StudentClass User Input
class Student:  
    def __init__(self, name, roll_number, section, city):  
        self.name = name   
        self.roll_number = roll_number  
        self.section = section
        self.city = city
    def display(self):  
        print("Name:", self.name)  
        print("Roll Number:", self.roll_number)
        print("Section:", self.section)
        print("City:", self.city)
name = input("Enter student's name: ")
roll_number = input("Enter student's roll number: ")
section = input("Enter student's section: ")
city = input("Enter student's city: ")
student = Student(name, roll_number, section, city)
student.display()

#####2
from demouserinput import Student

class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    # Make sure this is indented so it is INSIDE the class
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Branch: {self.branch}")

s= Student("Alice", 20,"CSE")
s.display()  

#access variables outside the class
print("access outside the class",s.name)
print(s.age)

#delete variable outside the class
del s.name
#print(s.name)

#modify variable outside the class
print("Before modification:", s.age)
s.age = 40
print("After modification:", s.age)

#Add new variable in existing class
s.city="Pune"
print("City:", s.city)

