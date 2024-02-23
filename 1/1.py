a = ["banana", "alma", "kom", "sd", "sdw", "sadasd"]
banana, alma, *f = a
print(banana)
print(alma)
print(a.reverse())



class smt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
    def printarea(self):
        print(self.area())

sx = smt(2,4)


sx.printarea()

b = "asdsa"
a = b.reverse()
print(a)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Alibek", 59)

print(p1.name)
print(p1.age)