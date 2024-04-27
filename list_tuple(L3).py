# List - A built in data type that stores set of values. (list-mutable/editable)It can store elements of different data types.(Hetrogeneous data types)
# similar to array but difference is only that array contains homogeneous data types(same data types)
# marks = [12,5.6,"Abhay"]
# print(type(marks),marks)
# print(marks[0])
# print(len(marks))  
# print(sum(marks[0:2])) #slicing

# marks[2]="Thakur"  #mutable
# print(marks)

# list methods
# list = [2,1,3]
# print(list)
# list.append(4)#add one element at the end
# print(list)
# list.sort()   #sort in asc order
# print(list)
# list.sort(reverse=True)  #sort in desc order
# print(list)
# list.reverse   #reverse list
# print(list)
# list.insert(0,6) #insert element at index
# print(list)
# list.remove(1) #remove first occurrenc of element, secific stored item
# print(list)
# list.pop(0)  #remove element at index
# print(list)

# Enumerate() assign an index to each items

# list1 = ["Apple","Banana","Pears"]
# en = enumerate(list1)
# print(en)

# list comprehension
# prices  = [1,2,3,4,5]
# fruits = [5,4]
# add_num = [num+2 for num in prices]
# new_nm  = [num**2 for num in prices if num%2==0]
# print(add_num)
# print(new_nm)

# Tuple: A built in data type that lets create immutable sequence of values.
# tup = (1,2,3)
# print(type(tup))
# print(tup[0])
# print(tup[0:2])
# tup = ()
# print(tup)
# tup1 = (2,)
# print(tup1)

# Tuple methods
# tup2 = (1,2,2,3,4,5)
# print(tup2.index((2)))  #returns index of first occurrence
# print(tup2.count((2)))  #counts total occurences

# WAP to ask the user to enter names of three fav movies & store them in a list.
# first_movie = input("Enter first movie name")
# second_movie = input("Enter second movie name")
# third_movie = input("Enter Third movie name")
# movies = []
# movies.append(first_movie)
# movies.append(second_movie)
# movies.append(third_movie)
# print(movies)
#--------------------------------
# first_movie = input("Enter first movie: ")
# second_movie = input("Enter Second movie: ")
# Third_movie = input("Enter third movie: ")

# list1 = []
# list1.append(first_movie)
# print(list1)
# list2 = []
# list2.append(second_movie)
# print(list2)
# list3 = []
# list3.append(Third_movie)
# print(list3)

# print(list1+list2+list3)
# -------------------------


# WAP to check if list contains a palindrome of elements.Hint(use copy() mothod)

# list1 = [1,2,1]
# copy_list1 = list1.copy()

# if(list1==list1):
#     print("palindrome")
# else:
#     print("not palindrome")

# WAP to count the number of students with the "A" grade in following tuple.
    
# grade = ("C","D","A","A","B","B","A")
# print(grade.count("A"))
# #Store the above values in a list & sort them from "A" to "D"
# grade = ["C","D","A","A","B","B","A"]
# grade.sort()
# print(grade)
# #---------------------------------
# grade1 = list(grade)
# grade1.sort()
# print(grade1)