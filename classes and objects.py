


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

print("Hello my name is " + self.name)
print("Iam "+self.age+" years old!")

name= input("Enter Employee Name")
age= input("Enter Employee age")

p1 = Person(name, age)
p1.myfunc()
