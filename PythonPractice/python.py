# def isprime(n):
#     if n < 2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# print(isprime(12))


# str="name"
# print(str[::-1])

li=[3,1,2,3,4,5,6,7,8]

t=6

le=len(li)

for i in range(0,le+1):

    for j in range(1,le+1):

        if (i+j)==t:

            print(i,j)
 


