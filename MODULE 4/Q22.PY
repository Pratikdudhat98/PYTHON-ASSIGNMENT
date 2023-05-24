# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class 
A Class is like an object constructor, or a "blueprint" for creating objects.
Syntax: Class Definition

class ClassName:
    # Statement

The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
EXAMPLE :

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()