import numpy as np

a=np.array([1,3,4])

print(a)
print(type(a))

b=np.zeros((3,2))
print(b)

c=np.ones((3,2))
print(c)

print(np.arange(0,10,2))

print(np.linspace(2,8,7)) # it is taking differencce from the startin and ending number divde by the last number

print(np.random.rand(1,3))

a1=np.array([2,4,5,6,7,8])

b1=np.array([1,3,5,7,9,4])

print(a1+b1) # operands musts have same sixe means list in the arrray
print(a1-b1)
print(a1*b1)
print(a1**b1)
print(np.sqrt(a1))
print(np.sqrt(b1))
print("---------2 dime--------")
# 2 dimensioanl array
a=np.array([[1,2],[3,4]])

b=np.array([[3,5],[7,8]])

print(np.dot(a,b)) #  multlipaction
print(np.transpose(a)) # row -col and col -row
print(np.linalg.inv(a)) # 