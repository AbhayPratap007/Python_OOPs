# #String is data type that stores a sequence of characters.
# str1 = "This is a string."
# str2 = 'This is also string.'
# str3 = '''This is also string.'''
# str1 = "This is a string.\nwhere are creating it in python." #\n for next lime- escape sequence character
# print(str1)
# str1 = "This is a string.\twhere are creating it in python." #\t for tab- escape sequence character
# print(str1)

#operation
#Concatention
# str1 = "Apna"
# str2 = "College"
# print(str1 +" "+str2)
# print(str1 + str2)
#length of str  #also count spaces
# print(len(str1))
#Indexing
# '''A   B   H   A   Y 
#    0   1   2   3   4
#   -5  -4  -3  -2  -1 '''

# str = "Abhay Pratap Singh"
# print(str[0])
#Slicing - Accesing parts of a string
# print(str[6:12])
# print(str[6:12:2])  # items 6 to 12 indexing with 1 spaces like.
# print(str[6:len(str)])
# print(str[:5])
# print(str[13:])
#Negative index
# print(str[::-1])
# print(str[-12:-6])  #not include last index, so add one more(skip of "-6th" postition items like )
# print(str[-12:-7])  

#String Function
# str = "I am a coder."

# print(str.startswith("I"))  #return tre if string start with substr
# print(str.endswith("er."))  #returns true if string ends with substr
# print(str.capitalize())     #capitalizes 1st char
# print(str.replace("coder","Coder")) #replace all occurrences of old with new
# print(str.find("a"))         #return 1st index of 1st occurence
# print(str.find("p"))         #it's not in str so it will return -1 
# print(str.count("a"))        #counts the occurrence of subtr in string
# print(str.swapcase())        #convert lower into upper & upper into lowers


#WAP to input user's first name & print its length 
# name = input("Enter your first name ")
# print("Your first name",name,".It's length size",len(name))
# print("length of your first name is ", len(name))
# print(f"Your first name {name} It's length of {len(name)}")

#WAP to find the occurrence of '$' in a string.
# str = "I have 12$"
# print(str.find('$'))

#Conditional Statements
# if-elif-else(SYNTAX)  # Syntax: rules of programming
# if(condition):
    #statement1
# elif(condition):
    #statement2
# else:
    #statement3

# age = 21
# if (age>=18):
#     print("You are eligible for vote")

# age = int(input("Enter your age: "))
# if (age>=18):
#     print("Yes,You are eligible for vote")
#     print("You can apply for voter card")
# else:
#     print("No, You are not eligible for vote")

# light = "yellow" #input("Enter traffic signal light colour: ")

# if(light=="green"):
#     print("Go")   #indentation: {} like set of blocks
# elif(light=="red"):
#     print("Stop")
# else:
#     print("Wait for right signal colour")


# marks = int(input("Enter marks:"))
# if (marks>=90):
#     grade = "A"
# elif(marks>=80 and marks>90):
#     grade = "B"
# elif(marks>=70 and marks>80 ):
#     grade = "C"
# else:
#     grade = "D"

# print(f"grade of the student - {grade}")

#Nesting
# age = 12
# if(age>=18):
#     if(age>80):
#         print("He is eligible for pension")
#     else:
#         print("He is not okay for pension")
# else:
#     print("can not drive")


#WAP to check if a number entered by the user is odd or even.
# number = int(input("Enter number: "))
# if(number%2==0):
#     print("Even number")
# else:
#     print("Odd number")

#WAP to find the greatest of 3 numbers entered by the user.
# a = int(input("First number "))
# b = int(input("Second number "))
# c = int(input("Third number "))

# if(a>=b and a>=c):
#     print("A is greter than B and C")
# elif(b>=c and b>=a):
#     print("B is greter than C and A")
# else:
#     print("C is greater than A and B")

#WAP to check if a number is a nultiple of 7 of not.
# num = 89
# if(num%7==0):
#     print("Multiple of 7")
# else:
#     print("Not Multiple of 7")
