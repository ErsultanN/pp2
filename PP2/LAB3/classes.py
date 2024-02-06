#Exercise 1
class MyClass:
    x = 5

#Exercise 2
class MyClass:
    x = 5
p1 = MyClass()

#Exercise 3
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

#Exercise 4
class Person:
    def __init__(self , name ,age):
      self.name = name
      self.age = age

#Example 1
class MyClass:
  x = 5

#Example 2
p1 = MyClass()
print(p1.x)

#Exmaple 3
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

#Example 4
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1)

#Example 5
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)

#Example 6
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()

#Example 7
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()

#Example 8
p1.age = 40

#Example 9
del p1.age

#Example 10
del p1

#Example 11
class Person:
  pass

