class Private:
    def __init__(self):
        self._salaray=5000
    def salary(self):
        return self._salaray

o=Private()
print(o._salaray)

class Private1:
    def __init__(self):
        self.__salary=5000
    def salary(self):
        return self.__salary

o1=Private1()
print(o1.salary())


num=[1,33,4,5]

iter_num=iter(num)

print(next(iter_num))
print(next(iter_num))
print(next(iter_num))

print("---------------")
#local scope
def loc():
    x=300
    print(x)
loc()   


# enclosing scope

def fun1():
    x=200
    def fun2():
        print(x)
    fun2() 

fun1()    

#global scope
x=2000
def glo():
    print(x)
glo()


