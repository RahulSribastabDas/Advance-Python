class Person:
  def info(self):
    print("I am Person and My name is Jenny")

class Teacher(Person):
  def teach(self):
    print("I tech Student in College")

class SubjectTeacher(Teacher):
  def subject(self):
    print("I am teaching Advance python subject")

sub = SubjectTeacher()
sub.info()
sub.teach()
sub.subject()