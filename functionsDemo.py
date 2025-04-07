def greet():
                print("hi hello good evening")

greet()             

#function with formalArguments
def kow(name):
                print("hello",name)

kow("kowshik")           

#fun with return value
def ret(a,b):
                return a+b
res=ret(5,5)

print("sum:",res)

#default valuee

def gret(name="kowshik"):
                            print("hello",name)
gret()
gret("god")    #here it replace the kowshik with god 

#fun with multiple return values

def mul():
            name="kowshik"
            age=23
            return name,age 
x,y=mul()
print("name:",x,"age:",y)     

#fun with multiple arguments

def argu(*su):
            return sum(su)#----here sum is the pre-defined function
print(argu(1,2,4,5))

#dictionary keys ,values

def info(**details):
        for x,y in details.items():
                                    print(x,y)
info(name="kows",age=37)

#practice
def addd(a,b):
            print(a+b)
addd(2,4)

def details():
                    a=10
                    b=20
                    c=30
                    return a,b,c
x,y,z=details()
print(x,y,z)

def mul1(*m):
                print(m)
mul1(2,5)                
            