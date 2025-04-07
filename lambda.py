s="hi hello "

s2=lambda fun:fun.upper()

print(s2("kowshikk"))

#
p=lambda x: "positive" if x>0 else "negative" if x<0 else "zero"

print(p(0))

#
p1=lambda x: x**2

print(p1(5))

#
p2=lambda x,y: x+y

print(p2(2,130))

#
p3=[lambda arg=x: arg * 10 for x in range(1,5)]

for i in p3:
            print(i())
#even or odd
check =lambda x: "even" if x%2==0 else "odd"

print(check(2))

# lambda with multiple args

cal=lambda x,y: (x+y,x*y) ##two expressions in this we can give 3 also

print(cal(2,3)) #(5,6) it will return tuple 


#filter  list based
n=[2,3,4,5,6,7,8,10,9,12]
li=filter(lambda x: x%2==0,n) # filter() it will apply condition to the each element in list

print(list(li)) # for readable format we r using List(li)

#map
a=[1,2,3,4,5]
b= map(lambda x: x*2,a)
print(list(b))

#reduce
from functools import reduce
b=[1,2,3,4,5]
c= reduce (lambda x,y:x*y,b)
print(c)  

####
a="revature"
b=22

msg="my name is {0} and iam age {1}".format(a,b)
print(msg)

a="python"
print("this is the articl {}".format(a))


print("my name id {} and age {}".format("user",19))

def fun1(msg):

            def fun2():
                        print(msg)
            fun2()

fun1("ima kwoshhik  iam and outer function msg")
print("----------------------------------")
#decorator 
def decorator(fun):   #not mandatory to use function name as decorator but it will good practice
        def wrapper():
                import inspect
                print( inspect.signature(decorator))
                print("before calling the greet")
                fun()
                print("after calling the greet")
        return wrapper
@decorator #greet =decoartor(greet)
def greet():
        print("hi hello good morning")
        print("iam the one who called by the decorator")

greet()