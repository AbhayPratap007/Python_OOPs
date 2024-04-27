#Functions: Block of statements that perform a specific task.
#def fun_name(par1,par2,...):
    #some work here
    # return value
#fun_name(arg1,arg2,...)
# def cal_sm(a,b):
#     sm = a+b
#     print(sm)
#    # return sm

# cal_sm(5,7)
# cal_sm(70,65)

# def fun():
#     print("Hello")

# fun()

# def cal_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg

# cal_avg(8,6,9)

# print("Abhay",end=" ")
# print("Pratap",end=" ")
# print("Singh",end=" ")

#Default Parameters
# def cal_prod(a=5,b=9):
#     print(a+b)
#     return a+b

# cal_prod()

#WAF to print the length of a list.(list is the parameter)
# list = ["New York","Austrlia","USA","Newzland"]

# def len_list(list):
#     print(len(list))

# len_list(list)
#WAP to print the elements of a list in a single line.(list is the parameter)
# num = [1,2,4,6,7,8,9]

# def list(num):
#     print(num)
#     #return num

# list(num)

# list = ["New York","Austrlia","USA","Newzland"]

# def print_list(list):
#     for item in list:
#         print(item,end=" ")

# print_list(list)

#WAP to find the factorial of n.(n is the parameter)

# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact *=i
# print(fact)

# def cal_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *=i
#     print(fact)

# cal_fact(5)

#WAP to convert USD to INR.

# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val,"USD =", inr_val,"INR")

# converter(1)

#Recursion: When a function calls itself repeatedly.
# def show(n):
#     if(n==0):   #Base case: like stopping criteria in loop
#         return
#     print(n)
#     show(n-1)

# show(5)

#returns n!
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * fact(n-1)

# def fact(n):
#     if(n ==1 or n==0):
#         return 1
#     return fact(n-1) * n

# print(fact(3))

#Write a recrsive function to calculate the sum of first n natural numbers.
# def cal_sum(n):
#     if(n==0):
#         return 0
#     return cal_sum(n-1) + n

# sum = cal_sum(5)
# print(sum)
#Write a recursive function to print all elements in a list.
# #Hint: use list & index as parameters.
# def print_list(list,idx=0):
#     if (idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)

# fruits = ["Mango","litchi","Banana","Pear"]

# print_list(fruits)