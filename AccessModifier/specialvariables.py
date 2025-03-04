#Special variables in python

# print(__name__)
'''
print("This is demo.py file")
if"__name__" == "__main__":
    def add(x,y):
        print(x+y)

add(3,5)'''

# print(__doc__)

# print(__file__)

"""
class stu:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

s=stu("Ranjeet",21)
print(s.__dict__)

"""
"""
x=10
y="Ranjeet"
z=10.5
print(x.__class__)
print(y.__class__)
print(z.__class__)"""

'''
class A:
    pass

class B(A):
    pass

print(B.__bases__)'''

print(dir())