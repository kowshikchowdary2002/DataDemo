# file=open("text.txt",'r')

#con=file.read()
#print(con) # getting whole content

#con1=file.readline()
#print(con1) # only one line
# con2=file.readlines()
# print(con2)

# file.close()

# file=open("text.txt","a")

# con=file.write("hello world\n")
# con1=file.write("good bye")
# print(con1)  

# file.close()

# import os

# if os.path.exists("text.txt"):
#          with open("text.txt","r")as file:
#                  con=file.read() 
#                  print(con)
# else:
#         print("file doesnot exist")


# try:
#        with open("text.txt","r")as file:
#                  con=file.read() 
#        with open("text1.txt","w") as filewrite:
#                filewrite.write(con)
#        print("successfullu copied")
# except Exception as e:
#         print(e)
        
import os
# f=open("example1.txt","x") # Creating th new file

os.remove("example1.txt") # removes the file
os.rmdir("folder name") # removes the folder name
