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