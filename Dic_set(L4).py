#Dictionary in python are used to store data values in key:value pairs.Unordered data structure.
#They are unorderd, mutable & don't allow duplicate keys. values can be change but key will be immutable.
# info = {"Name":"Abhay","Course":["Python","SQL"],"marks":(56,98)}
# print(info)
# print(type(info))
# print(info["Name"])
# info["Skill"] = "Data Analysis"  #add items
# print(info)

# dict = {}
# dict = {"State":"UP"}
# print(dict)
# dict = {}
# dict = {"State":"UP"}
# print(dict)

#Nested Dictionaries.
# student = {"name":"rahul","subject":{"phy":32,"chem":68,"math":18}}
# print(student)
# print(student["subject"]["phy"])
# #methods
# print(student.keys())
# print(student.get("name"))
# print(student.values())
# print(len(list(student.keys()))) #typecast
# print(student.items()) #key-values pair
# student.update({"city":"Pune"})
# print(student)

#Sets: Sets is the collection of the unique unordred items. Each element in the set must be unique & immutable.
# collection = {1,2,3,4}
# print(collection,"Type of set is:", type(collection),"and the length of set items are ",len(collection))
# collection1=set()
# print(collection1)

#Methods
# collection1.add(1)
# collection1.add(2)   #add items
# print(collection1)
# collection1.remove(1)  #remove items
# print(collection1)

# collection1.add((1,2,3))
# print(collection1)

# collection1.add("I am openhimmer")
# print(collection1)

# collection1.clear()#empties the set
# print(collection1)

# print(collection.pop())    #removes a random value

#union
# set = {1,2,3,4,5,6}
# set2 = {7,8,9,2}
# print(set.union(set2))
#intersection
# print(set.intersection(set2))


#Store following word meaning in a python dictionary:
#table:"a piece of furniture","list of facts & figures"
#cat:"a small animal"

# dict = {"table":["a piece of furniture","list of facts & figures"],"cat":"a small animal"}
# print(dict)

# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classroom are needed by all students.
# "python","java","C++","python","js","java","python","java","C++","C"
# subject = {"python","java","C++","python","js","java","python","java","C++","C"}
# print(len(subject))

#WAP to enter marks of 3 subjects from the user and store them in dictionary. 
# Start with an empty dict & add one by one. use subject name as key & marks as value.

# marks = {}

# physics = int(input("Enter your physics marks "))
# chemitsry = int(input("Enter your chemitsry marks "))
# math = int(input("Enter your math marks "))

# marks.update({"Phy": physics})
# marks.update({"Chem": chemitsry})
# marks.update({"Math": math})
# print(marks)

#Figure out a way to store 9 & 9.0 as seprate values in the set.

# set  = {9,"9.0"}
# print(set)

