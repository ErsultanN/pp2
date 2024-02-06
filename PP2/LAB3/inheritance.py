#Exercise 1
class Student(Person):

#Exercise 2
  class Person:
   def __init__(self, fname):
    self.firstname = fname
  def printname(self):
    print(self.firstname)
class Student(Person):
  pass
x = Student("Mike")
x.printname()

#Example 1
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()

#Example 2
class Student(Person):
  pass

#Example 3
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()

#Example 4
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

#Example 5
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

#Example 6
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

#Example 7
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
x = Student("Mike", "Olsen", 2019)

#Example 8
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)