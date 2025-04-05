# validate password'
import re
pattern=r"[A-Z]+[a-zA-Z0-9]+[@%*&._-]+[0-9]"

password="Kowshik123&2002"
spl="@*%&.-_"
test=re.search(pattern,password)
if test:
    print("matched")
else:
    if password.__contains__(spl) and password.startswith("A-Z"):
        print("unmatched")
    else:
        print("password must have special characters\nfirst letter must be upper case")
    

# validate URl

pattern=r"(httpsHTTPS)?+(:\\)?+[www]+\.[a-zA-Z]+\.[a-zA-Z]{2,}"

url="http:\\www.facebook.kow"

test=re.search(pattern,url)

if test:
    print("matched")
else:
    print("unmatched")


#handle all  the errors
#syntax error
try:
   exec("if True") # theasre the errors that showed before the execution we havve to hande dhynamically
   
    
except SyntaxError  as e:
    print(f"coorect the syntax: {e}")
# type error
try:
    x="g"+2
    print(x)
except Exception as e:
    print(f"Type error: {e}")

# value Error
try:
    x=int("abc")
    print(x)
except Exception as e:
    print(f"Value Error {e}")
#index error
try:
    list=[1,2,3,4]
    print(list[6])
except IndexError as e:
    print(f"error in index error {e}")
# key error
try:
    dic={
        "a":"kowshik",
        "b":45
    }
    print(dic['c'])
except KeyError as e:
    print(f"key error{e}")

#attribute error
try:
    text="kowshik"  
    text.append
except AttributeError as e:
    print("AttributeError:",e)

