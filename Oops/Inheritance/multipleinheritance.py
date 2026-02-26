class father:
    def skills1(self):
        print("Father have driving skills")

class mother:
    def skills2(self):
        print("Mother have cooking skills")  

class child(father,mother):
    def skills3(self):
        print("Child have painting skills")
        
c= child()
c.skills1()                      
c.skills2()                      
c.skills3()

###example using super() method
#Multilevel Inheritance using super() keyword
class Grandparent:
    def grandparent_method(self):
        print("This is a method in the Grandparent class.")
class Parent(Grandparent):
    def parent_method(self):
        print("This is a method in the Parent class.")
class Child(Parent):
    def child_method(self):
        print("This is a method in the Child class.")
        super().parent_method()  
        super().grandparent_method()
child_instance = Child()
child_instance.child_method()