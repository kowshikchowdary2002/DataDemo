# 1)All types of inheritence 
# single level inheritence

class Pen:
    a=10
    def write(self):
        print("writing")
    b=20
class Cap(Pen):
    c=30
    def open(self):
        print("opening")
pen=Pen()
print(pen.a)
print(pen.b)
pen.write()
print("----from object child------")
cap=Cap()
print(cap.a)
print(cap.b)
print(cap.c)
cap.write()
cap.open()

# multilevel inhertence-------------------------------------------------------------------------
class Customer:
    a=10
    def buy(self):
        print("buying customer")
    
class Product(Customer):
    b=20
    def sale(self):
        print("sales on cost product")
class Order(Product):
    c=30
    def quantity(self):
        print("based on the order")

customer=Customer()
product=Product()
order=Order()
print("--------multilevel------")
print("----custometr obj----")
print(customer.a)
customer.buy()
print("----product obj--------")
print(product.a)
print(product.b)
product.buy()
product.sale()
print("----order obj--------")
print(order.a)
print(order.b)
print(order.c)
order.buy()
order.sale()
order.quantity()

# multiple inhertence---------------one child multiple parents----------------------------------------------------------
class Animal:
    color="black"
    def ani(self):
        print("iam animal")
class Sounds:
    sound="bow meow chal  chal"
    def sou(self):
        print("sounding ")
class Dog(Animal,Sounds):
    breed="dog"
    def walk(self):
        print("walking dog")
print("----Animal obj--------")
animal=Animal()
print(animal.color)
animal.ani()

print("----Sounds obj--------")
sounds=Sounds()
print(sounds.sound)
sounds.sou()

print("----dog obj--------")
dog=Dog()
print(dog.color)
dog.ani()
print(dog.sound)
dog.sou()
print(dog.breed)
dog.walk()

# heirechial inhertence---------------one parent multiple childs----------------------------------------------------------
class Bird:
    def sound(self):
        print("bird sounding")
class Crow(Bird):
    def crowsound(self):
        print("crow sounding")
class Sparrow(Bird):
    def sparrowsound(self):
        print("sparrowsounding")

bird=Bird()
crow=Crow()
sparrow=Sparrow()

bird.sound()
crow.sound()
crow.crowsound()
sparrow.sound()
sparrow.sparrowsound()

#hybrid inheritence----------------------------------combination of all inhertience

#2)methood overloading and overriding
#Overriding
class Cal:
  l=10
  def add(self,a,b):
    print(a+b)
    print("iam parent")
    
class Add(Cal):
      def add(self,a,b):
        print(a+b)
        print("iam child")
add1=Add()
#add.add(2,3)
print(add1.l)
add1.add(5,15)

#3)polymorphism

class Dog:
    def speak(self):
        print("bow bow")
class Cat:
    def speak(self):
        print("meow meow")
d=Dog()
c=Cat()
def animalSound(animal):
    animal.speak()

animalSound(c)
animalSound(d)

#4) encapsulation in all modifiers
#====protected-------------
class Animal:
    def __init__(self,name):
        self._name=name
    def name(self):
        print("name=",self._name)
animal=Animal("kowshiik")
animal.name()
#======private-------------
class School:
    def __init__(self,location):
        self.__location=location
    def ide(self):
        print("location =",self.__location)

school=School("chennai")
school.ide()