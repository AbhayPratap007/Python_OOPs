# #Loops are used to repeat instructions.
# #while loop & for loop 
# # count = 1
# # while count<=5:
# #     print("Hello world",count)
# #     count = count+1

# #print("loop ended",count)  #value

# # current_lift_button = 0
# # lift_flor_Button = 5
# # while (current_lift_button < lift_flor_Button):
# #     print(current_lift_button,"You are on the way")
# #     current_lift_button +=1
# # print(current_lift_button,"You have reached over floor")


# # count = 5
# # while count>=1:
# #     print(count)
# #     count = count-1


# #Print numbers to 1 to 100.
# # i = 1
# # while i<=100:
# #     print(i)
# #     i +=1
# #Print numbers to 100 to 1.
# # i = 100
# # while i>=1:
# #     print(i)
# #     i -=1

# #Print multiplication table of a number n.
# # n = 2
# # i = 1
# # while i<=10:
# #     print(n*i)
# #     i +=1


# # nums = [1,4,9,16,25,36,49,64,100]
# # idx = 0
# # while idx<len(nums):
# #     print(nums[idx])
# #     idx +=1

# # Heroes = ["Ironman","Thor","Superman","Batman"]
# # idx = 0
# # while idx<len(Heroes):
# #     print(Heroes[idx])
# #     idx +=1

# #Search for a number x in this tuple using loop:(1,4,9,16,25,36,49,64,100)

# # nums = (1,4,9,16,25,36,49,64,100)
# # x = 9
# # i = 0
# # while i<len(nums):
# #     if (nums[i]==x):
# #         print("Found at index",i)
# #     else:
# #         print("Finding...")
# #     i +=1

# #Break and Continue
# #Break: used to terminate the loop when encountered.
# #Continue: Terminate execution in the current iteration & continues execution of the loop with the next iteration.
    
# # i = 1
# # while i<=5:
# #     print(i)
# #     if (i==3):
# #         break
# #     i +=1
# # print("End of Loop")

# # nums = (1,4,9,16,25,36,49,64,100)
# # x = 9
# # i = 0
# # while i<len(nums):
# #     if (nums[i]==x):
# #         print("Found at index",i)
# #         break
# #     else:
# #         print("Finding...")
# #     i +=1

# # i = 0
# # while i<=5: 
# #     #if (i==3):
# #     if (i%2==0):
# #         i +=1
# #         continue
# #     print(i)
# #     i +=1
# # print("End of Loop")
    
# #For loop are used to sequential traversal. For traversing list, string, tuples etc.
# # list = [1,2,3,4,5]
# # for num in list:
# #     print(num)

# # list = [1,2,3,4,5]
# # for num in list:
# #     if (num==3):
# #         print(num,"is find")
# #         break
# #     print(num,end=", ")    

# # print("End")

# # list = [1,2,3,4,5]
# # for num in list:
# #     print(num,end=", ")    
# # else:
# #     print("End")



# fruits = ["Apple","Mango","Keewi","Banana"]
# price = [12,98,45,35]

# for Fruits,Rates in zip(fruits,price):
#     print(f"Price of {Fruits} is {Rates}.")

# #Print the elements of the following list using a loop: [1,4,9,16,25,36,49,81,100]
# list = [1,4,9,16,25,36,49,81,100]
# for i in list:
#     print(i)

# #Search for a number x in this tuple using a loop: (1,4,9,16,25,36,49,81,100)
# # list = (1,4,9,16,25,36,49,81,100)
# # x = 25
# # for i in list:
# #     if (x==i):
# #         print("Find")
# #         break
# #     else:
# #         print("Finding...")
# #     print(i)

# # list = (1,4,9,16,25,36,49,81,100)
# # x = 25
# # idx = 0
# # for i in list:
# #     if (x==i):
# #         print("Find at", idx)
# #         break 
# #     idx +=1

# #range(): returns a sequence of numbers, starting from 0 by default, and increment by 1, and store before a specified number.
# #range(start,stop,step)
# # for i in range(5):
# #     print(i)

# # for i in range(2,10):
# #     print(i)

# # for i in range(2,10,2):
# #     print(i)

# # for i in range(1,10):
# #     if (i%2==0):
# #         print(i)

# # Print numbers to 1 to 100.
# # for i in range(1,101):
# #     print(i)
# # Print numbers to 100 to 1.
# # for i in range(100,0,-1):
# #     print(i)
# # Print multiplication table of a number n.
# # n = int(input("Enter number: "))
# # for i in range(1,11):
# #     print(n*i)

# #Pass Statement: pass is null statement that does nothing, it is used as a placeholder for future code.
# # for i in range(5):
# #     pass

# # print("Hello")

# #WAP to find the sum of first n number, using(while and for)
# # num = [1,2,3,4,5,6,7,8,9]
# # tot = 0
# # for i in num:
# #     tot = tot+i
# # print(tot)

# # n = 5
# # tot = 0
# # for i in range(1,n+1):
# #     tot = tot+i
# # print(tot)

# # n = 7
# # sum = 0
# # i = 1
# # while i <=n:
# #     sum +=i
# #     i +=1
# # print("Total sum =",sum)

# #WAP to find the factorial of first n numbers.

# # n = 3
# # fact = 1
# # i = 1
# # while i <=n:
# #     fact *=i
# #     i +=1
# # print("Factorial =",fact)

# # n = 3
# # fact = 1

# # for i in range(1,n+1):
# #     fact *=i

# # print("Factorial =",fact)


for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=' ')
    print()

for i in range(0,5):
    for j in range(0,6-i+1):
        print("*",end=' ')
    print()

k = 1
for i in range(0,5):
    for j in range(0,i+1):
        print(k,end=' ')
        k = k+1
    print()