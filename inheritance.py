class School:
    def __init__(self,name,address):
          self.name=name
          self.address=address

    def sound(self):
        raise NotImplementedError("sub ")

class Student(School):
     def sound(self):
          return "woof"
    
# a=School("nal","hyd")
# print(a.address)
# print(a.name)
# print(a.sound())

# b=Student("kowshik","atk")
# print(b.name)
# print(b.address)
# print(b.sound())

class Color:
    def __init__(self):
        self.name="green"
        self.lg=self.Lightgreen()
    def show(self):
         print("color",self.name)
        
    class Lightgreen():
         def __init__(self):
              self.name="lightgreen"
              self.id=2020
         def display(self):
              print("colorname",self.name)
              print("code",self.id)
              
outer=Color()

inner=outer.lg

print(outer.name)
#print(outer.Lightgreen())
#print(inner.name)
inner.display()

class Parent:
     def show(self):
          print("ima a parent class mem")    

class Child:
     def show(self):
     #     super().show()
          print("iam a chils class memn")

b=Child()
b.show()


