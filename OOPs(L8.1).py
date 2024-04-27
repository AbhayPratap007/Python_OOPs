#OOP: To map with real world scenario, we started using objects in code. This is called Object oriented Programming.
# Note: function used to decrease redundency and increase reusability.
#Class is a blueprint for creating objects.
#creating class
# class Student:
#     name = "Abhay"

#creating object(instance of class)
# s1 = Student()
# print(s1.name)

# class Student:
#     name = "Abhay"

# s1 = Student()
# #print(s1)
# print(s1.name)

# class Car:
#     color = "Blue"
#     model = "Baleno"

# car1 = Car()
# print(car1.color)
# print(car1.model)

#Construtor: __init__ Function: All classes have function __init_(), which is always executed when the class is being initiated.
#creating class
# class Student:
#     def __init__(self,fullname):
#         self.name = fullname

# #creating object
# s1 = Student("Abhay")
# print(s1.name)

#The self parameter is a reference to the current instances of the class, and is used to access variales that belongs to the class.

# class Student:
#     def __init__(self,fullname,marks):
#         self.name = fullname
#         self.marks = marks
#         print("Creating new student...")
    
# s1 = Student("Karan",56)
# print(s1.name,s1.marks)

# s2 = Student("Arjun",26)
# print(s2.name,s2.name)


# class Student:

#     #default constructor:
#     def __init__(self):
#         pass

#     #parameterized constructor
#     def __init__(self,fullname,marks):
#         self.name = fullname
#         self.marks = marks
#         print("Creating new student...")
    
# s1 = Student("Karan",56)
# print(s1.name,s1.marks)

# s2 = Student("Arjun",26)
# print(s2.name,s2.name)

#Class & Instance Attribues: Class.attr and obj.attr
#Objects occupie space in memory.

# class Student:
#     college_name = "ABC College"   #class object
#     #parameterized constructor
#     def __init__(self,fullname,marks):
#         self.name = fullname
#         self.marks = marks
#         print("Creating new student...")
    
# s1 = Student("Karan",56)
# print(s1.name,s1.marks)

# s2 = Student("Arjun",26)
# print(s2.name,s2.name)
# #print(s2.college_name)
# print(Student.college_name)

#Methods: are functions that belong to objects.
# class Student:
#     college_name = "ABC College"   #class object
#     #parameterized constructor
#     def __init__(self,fullname,marks):
#         self.name = fullname
#         self.marks = marks

#     def welcome(self):
#         print("Welcome Student",self.name)

#     def get_marks(self):
#         return self.marks
    
# s1 = Student("Karan",56)
# s1.welcome()
# print(s1.get_marks())

#Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print the averge.

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum +=val
#         print("Hi",self.name,"Your averge marks is:",sum/3)

# s1 = Student("Bruce Banner",[56,78,95])
# s1.get_avg()

# s1.name = "Tony Stark"
# s1.get_avg()

#Static Method: Method that don't use self parameter(work at clas level)

# class Student:
#     @staticmethod   #Decorators
#     def college():
#         print("ABC College")

#Decorators allow us to wrap another function in order to extend the behavior of the wrapped function,
#without parmanenetly modifying it.

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("Hello")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum +=val
#         print("Hi",self.name,"Your averge marks is:",sum/3)

# s1 = Student("Bruce Banner",[56,78,95])
# s1.get_avg()
# s1.hello()

# class Student:
#     @staticmethod   #Decorators
#     def college():
#         print("ABC College")

# s1 = Student()
# s1.college()

#Abstraction: Hiding the implementation details of a class and only showing the essential features to the user.
# class Car():
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.acc = True
#         self.brk = True
#         self.clutch = True
#         print("Car Start...")

# car1 = Car()
# car1.start()

#Encapsulation: Wrapping data and functions into a single unit(object).

#Create Account class with 2 attr - balance & account no.
#Create methods for debit, credit & printing the balance.
class Account():
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    #debit
    def debit(self,amount):
        self.balance -=amount
        print("Rs.",amount,"was debited.")
        print("Total Balance = ",self.get_balance())

    #credit
    def credit(self,amount):
        self.balance +=amount
        print("Rs.",amount,"was Credited.")
        print("Total Balance = ",self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000,632177)
acc1.debit(1000)
acc1.credit(9000)