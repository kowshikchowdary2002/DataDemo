import re

x="then name is mine"

y=re.search("^the.*mine$",x)

if y:
        print("matched")
else:
        print("not matched")

z=re.findall("ai",x)
print(z)

z=re.search("\s",x)
print(z)

z=re.split("\s",x) # it will return list and split with white spaces 
print(x)
print(z)

z=re.sub("\s","$",x) #replacing eith $-then$name$is$mine
print(z)

pattern =r"\d+"

text="my name is kow"

match=re.search(pattern,text)
if match:
        print("matched",match.group())
else:
        print("not matched")

pattern=r"(\d+)-(\d+)"

text="the event is 2023-03-01"

z=re.search(pattern,text)

if z:
        print("year",z.group(1))
        print("year",z.group(2))

pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

text="this is my mail mailgmail@.com"

m=re.search(pattern,text)

if m:
        print("okay")
else:
        print("notokay")