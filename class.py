class Dog:
   sound="bark"
   def __init__(self,name,age,color): #here self reprsent the same class and _init_ is used as intilaizer in java like constructor
      self.name=name
      self.age=age
      self.color=color
   def __str__(self):
      return f"{self.name} is {self.age} years old and {self.color} color"  #here  'f' is formatted method 
#dog=Dog()

dog1=Dog("scoofy",3,"black") # instance of a Dog class and taking values
dog2=Dog("rocky",4,"brown")
print(dog1.sound)
print(dog1.age)
print(dog1.sound)
print(dog1.name)
print(dog1.color)

print(dog1)
print(dog2)
print("--------updation of calss variable is possible-------")
Dog.sound="meow"
print(dog1.sound)
print("--------updation of instance variable is possible----------")
dog1.name="puppy"
print(dog1.name)
print("-------aacessing and updating class varible with the instamce variable---------")
dog1.sound="bow bow"
print(dog1.sound)
print("-------aacessing and updating insatnce varible with the class variable---------")
print("it is not possible ")