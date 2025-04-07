
# try:
#     x=10/0
#     print(x)
# except ZeroDivisionError:
#     print("it is not possiblee ro divvide by zeo")
# finally:
#     print("execution completed")


# try:
#     num=int(input("enter a number"))
#     x=10/num
#     print(x)
    

# except ValueError as e:
#     print(f"{e}")
# except ZeroDivisionError as e:
#     print(f"{e}")
# except Exception as e:
#     print(f"{e}")
# else:
#     print(x)
# finally:
#     print("execution eompleted thank you")


   

#custom execptions
 #raise
class NotEligibleForVote(Exception):
       pass

def check(age):
        if age>18:
            print("you are eligilble")
        else:
            raise NotEligibleForVote("must be greater than 18")
    
try:
        check(15)
except NotEligibleForVote as e:
           print(e)