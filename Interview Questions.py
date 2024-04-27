# #1. Counting vowels in a given word

# vowels = ['a','e,','i','o','u']
# word = "programming"
# count = 0
# for character in word:
#     if character in vowels:
#         count = count+1
# print(count)

# #2. Counting consonants in a given word

# vowels = ['a','e,','i','o','u']
# word = "programming"
# count = 0
# for character in word:
#     if character not in vowels:
#         count = count+1
# print(count)

# #3. counting the number of occurances of a character in a string

# word = "python"
# character = "p"
# count = 0
# for letter in word:
#     if letter == character:
#         count = count+1
# print(count)

# #4. Fibonacci Series

# fib = [0,1]

# for i in range(5):
#     fib.append(fib[-1] + fib[-2])

# print(', '.join(str(e) for e in fib))

# #5. finding the maximum number in a list

# numberlist = [15,85,35,89,125]

# maxNum = numberlist[0]
# for num in numberlist:
#     if maxNum < num:
#         maxNum = num
# print(maxNum)

# #6. finding the maximum number in a list

# numberlist = [15,85,35,89,125]

# minNum = numberlist[0]
# for num in numberlist:
#     if minNum > num:
#         minNum = num
# print(minNum)

# #7. finding the middle element in a list

# numlist = [1,2,3,4,5]
# midElement = int((len(numlist/2)))

# print(numlist[midElement])

# #8. Converting a list into a string

# lst = ["P","Y","T","H","O","N"]
# string = ''.join(lst)

# print(string)
# print(type(string))

# #9. Adding two list elements together

# list1 = [1,2,3]
# list2 = [4,5,6]

# res_lst = []
# for i in range(0, len(list1)):
#     res_lst.append(list1[i] + list2[i])
# print(res_lst)

# #10. Checking for Palindrome using extended slicing technique

# str1 = "Kayak".lower()
# str2 = "kayak".lower()

# if(str1 == str2[::-2]):
#     print("True")
# else:
#     print("False")

# #11. Counting the white spaces in a string

# string = "P r ogramm in g "
# print(string.count(' '))

# # WAP to check if list contains a palindrome of elements.Hint(use copy() mothod)

# list1 = [1,2,1]
# copy_list1 = list1.copy()

# if(list1==list1):
#     print("palindrome")
# else:
#     print("not palindrome")

# i = 0
# j = 0
# for i in range(0,6):
#     for j in range(0,i+1):
#         print("@",end=' ')
#     print()

# k = 1
# for i in range(0,6):
#     for j in range(0,i+1):
#         print(k,end=' ')
#         k = k+1
#     print()

# i = 0
# j = 0
# for i in range(0,6):
#     for j in range(0,6-i+1):
#         print("@",end=' ')
#     print()

import mysql.connector as sql

Connection = sql.connect(
    host = 'localhost',
    user = 'root',
    password = "Singh@5796",
    database = "student"
)


print(Connection)

#Create database

cursor = Connection.cursor()

cursor.execute("create database students")

cursor.execute("Show databases")

for database in cursor:
    print(database)