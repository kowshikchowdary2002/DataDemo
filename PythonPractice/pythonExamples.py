
# import mysql.connector


# conn = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='root',
#     database='revature'
# )

# cursor = conn.cursor()


# cursor.callproc('GetMyDetails')


# for result in cursor.stored_results():
#     for row in result.fetchall():
#         print(f"Name: {row[0]}, Age: {row[1]}, Email: {row[2]}")

# cursor.close()
# conn.close()









# import array 

# a=array.array('i', [1, 2, 3])
# b=array.array('i', [4, 5, 6])
# c=a+b
# print(c)



# a1= int(input())
# a2 = int(input()) 
# a3 = int(input())
# a4 = int(input())

# a = [[a1, a2], [a3, a4]]

# def isprime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# p = []

# # Loop through matrix and check for primes
# for i in a:
#     for j in i:
#         if isprime(j):
#             p.append(j)

# print(p)


# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")


# matrix1 = [[1,2],[2,4]]

# transpose = [[0,0],[0,0]]

# for i in range(2):
#     for j in range(2):
#         transpose[i][j] = matrix1[j][i]

# if transpose == matrix1:
#     print("Yes")
# else:
#     print()


# decimal to binary

# a= 10
# b=bin(a)
# print(b)


# def longprefix(strs):
#     if not strs:
#         return ""
    
#     prefix = strs[0]
    
#     for s in strs[1:]:
#         while not s.startswith(prefix):
#             prefix = prefix[:-1]
#             if not prefix:
#                 return ""
    
#     return prefix

# print(longprefix(["fliower","fliow","flight"]))

# n=234
# a=1
# p=0
# for i in str(n):
#     digit = int(i)
#     a=digit*a
#     p=p+digit
# print(a)
# print(p)
# print(a-p)


# nums = [1,2,3,4,5,6,7,8,9]
# k = 3

# if len(nums) % k == 0:
#     print("True")
# else:
#     print("False")



#convert seconds into hrs

# def sectohr(sec):
#     h=sec//3600
#     s=sec%60
#     min=(sec%3600)//60
#     return h,s,min
# print(sectohr(125))


# import calendar
# from datetime import datetime

# def count_weekends_in_current_month():
#     now = datetime.now()
#     year = now.year
#     month = now.month

#     weekends = 0
#     month_days = calendar.monthrange(year, month)[1]

#     for day in range(1, month_days + 1):
#         weekday = datetime(year, month, day).weekday()
#         if weekday == 5 or weekday == 6:  
#             weekends += 1

#     return weekends

# print("Number of weekends this month:", count_weekends_in_current_month())



# li=[3,1,2,3,4,5,6,7,8]

# t=6

# le=len(li)

# for i in range(0,le+1):

#     for j in range(1,le+1):

#         if (i+j)==t:

#             print(i,j)
 


# list=[7,8,3,45,6,9,4,2]

# m=list[0]
# for i in range(len(list)):
#     if m<list[i]:
#         m=list[i]
#     else:
#         continue
# print("Minimum value in the list is:", m)

#1

# import re
# def parse_encoded_string(str):
#     # Split on one or more zeros using regex
#     parts = re.split('0+', str)
    
#     # Return dictionary
#     return {
#         "first_name": parts[0],
#         "last_name": parts[1],
#         "id": parts[2]
#     }

# # Example usage
# str1 = "Robert000Smith000123"
# result = parse_encoded_string(str1)
# print(result)

#2

# from collections import Counter

# def extra(str1, str2):
#     # Count characters in both strings
#     count1 = Counter(str1)
#     count2 = Counter(str2)
    
#     for char in count2:
#         if count2[char] != count1.get(char, 0):
#             return char
        
# print(extra("kowshik", "saikowshik")) 

#3

# def is_shadow(sent1, sent2):
#     words1 = sent1.lower().split()
#     words2 = sent2.lower().split()
    
    
#     if len(words1) != len(words2):
#         return False
    
    
#     for w1, w2 in zip(words1, words2):
#         if len(w1) != len(w2):
#             return False
#         if set(w1) & set(w2):  
#             return False
            
#     return True


# print(is_shadow("they are round", "fold two times"))     
# print(is_shadow("his friends", "our company"))           

#4
# from collections import Counter

# def duplicate(sentence):
#     words = sentence.lower().split()
    
#     for word in words:
#         count = Counter(word)
#         for val in count.values():
#             if val > 1:
#                 return True  
#     return False

# # Example usage
# print(duplicate("sai kowshik is good boy")) 
# print(duplicate("this is fun"))              

#5
# def ascii_to_hex(s):
#     return ' '.join(format(ord(char), '02x') for char in s)

# print(ascii_to_hex("kowshik"))   

#6
# def third(pos1, pos2):
#     winning_combos = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],    
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],    
#         [0, 4, 8], [2, 4, 6]                
#     ] 
#     for combo in winning_combos:
#         if pos1 in combo and pos2 in combo:
#             for pos in combo:
#                 if pos!=pos1 and pos!=pos2:
#                     return pos
#     return None

# print(third(1,8))

#7
# def minion_game(string):
#     vowels = 'AEIOU'
#     kevin_score = 0
#     stuart_score = 0
#     n = len(string)

#     for i in range(n):
#         if string[i] in vowels:
#             kevin_score += n - i
#         else:
#             stuart_score += n - i

#     if kevin_score > stuart_score:
#         print("Kevin", kevin_score)
#     elif stuart_score > kevin_score:
#         print("Stuart", stuart_score)
#     else:
#         print("Draw")

# minion_game("AEIOU")

