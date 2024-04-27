# What is Python?
# 1. Python is simple & easy, Free & Open Source, High level Language
# 2. Developed by Guido Van Rossum
# 3. Portable

#First Program 
# print("Hello world")

# print("Abhay","Pratap","Singh")
#print("Abhay")
#Print("Pratap")
#print("Singh")
# print(23+56)

#Variables: A variable is a name given to a memory location in a program.
# name = "Abhay" #string #name is var and "Abhay" is object 
# marks = 56   #int
# price = 6.52 #float
# food_price = price
# print(name)
# print(type(name)) #DataType- int,str(' '," ",''' '''),foat,bool(True,False),None
# print("My marks is:", marks)
# print("food prices are:", food_price)
# old = False
# age = None
# print(type(old))
# print(type(age))

#Print Sum
# a = 20
# b = 14
# sum = a+b
# sub = a-b
# print(f"The sum of a and b = {sum}")
# print(f"The difference of a and b = {sub}")

#Operatosrs: An operator is a symbol that performs a certain operation between operands.
#1. Arithmetic (+,-,*,/,%,**)
#2. Relational (==,!=,>,<,>=,<=)
#3. Assignment (=,+=,-=,*=,/,\,=,%=,**=)
#4. Logical (not, and, or)

# a = 50
# b = 20
# print(a==b)
# print(a!=b)
# print(a>b)

#Logical operator
# print(not False)
# print(not True)

# val1 = True
# val2 = True
# # print("and Operators:", val1 and val2)
# print("and operator:", (a!=b) and (a>b))
# # print("or Operators:", val1 or val2)
# print("or operator:", (a==b) or (a>b))

# #Type Conversion
# a = "2"
# b = 4.5
# sum = int(a)+b  #  float(a)+b
# print(sum)

#Input Statement
# used to accept the value from user
# name = input("input your name:")
# print(type(name),name)
#age = int(input("Enter Your age"))
#print(age)

# 1. WAP to input 2 numbers and their sum.
# first = int(input("Enter first:"))
# Second = int(input("Enter Second:"))
# print("sum=",first+Second)
# a = 15
# b = 20
# sum = a+b
# print(f"Sum or a and b are {sum}")

#WAP to input side of a square & print its area.
# side = float(input("Enter Square side:"))
# area = side*side
# print(area)

#WAP to input 2 floating point numbers & print their average.
# a = float(input("Enter first:"))
# b = float(input("Enter Second:"))
# avg = (a+b)/2
# print(avg)

# WAP to input 2 int numbers, a and b. Print True if a greater than or b, if not print false.
# a = int(input("Enter first:"))
# b = int(input("Enter Second:"))
# print(a>=b)