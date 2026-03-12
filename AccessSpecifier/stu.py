class stu:
     def __init__(self,name,age,section):
        self.name = name   # public variable
        self._age = age    # protected variable
        self.__section = section  # private variable

def display(self):
        print("Name:",self.name)
        print("Age:",self._age)
        print("Section:",self.__section)

class info(stu):
    def show(self,roll):
        self.roll = roll
        print("Inside the Dervied class")
        print("Roll No:",self.roll)
        print(self.name)  # This will raise an error because name is not defined in this class
        print(self._age)  # This will raise an error because _age is not defined in this class
        print(self.__section)  # This will raise an error because __section is not defined in this class

i=info("Ranjeet",21,"I")
i.show(101)
i.display()
print(i.name)  # This will raise an error because name is not defined in this class
print(i._age)  # This will raise an error because _age is not defined in this class
print(i.__section)  # This will raise an error because __section is not defined in this class


s=stu("Ranjeet",21,"I")
print(s.name)
print(s._age)   
# print(s.__section)  # This will raise an error because __section is a private variable
s.display()