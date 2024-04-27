#del keyword: To delete objet properties or object itself.
#del s1.name
#del s1

# class Student:
#     def __init__(self,name):
#         self.name = name

# s1 = Student("Abhay")
# print(s1.name)
# del s1.name
# print(s1.name)

#Private(like) attriutes & methods
#Conceptual implementation in Python
#Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no  = acc_no
#         self.__acc_pass = acc_pass  #private __

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("1,2,3,4,5,6","hfjjej")
# print(acc1.acc_no)
# #print(acc1.__acc_pass)
# print(acc1.reset_pass())


# class Person:
#     __name = "anonymous"

# p1 = Person()
# print(p1.__name)

# class Person:
#     __name = "anonymous"

#     def __hello(self):
#         print("Hello person")

#     def Welcome(self):
#         self.__hello()

# p1 = Person()
# print(p1.Welcome())

#Inheritance: when one class(child/derived) derives the properties & methods of another class(parent/base)

#single level inh
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")

# class ToyatoCar(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = ToyatoCar("Fortuner")

# print(car1.start())
# print(car1.name)

#Types:
#Single inheritence
#Multi-level inheritence
#Multiple inheritence

#multilevel - inhr
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")

# class ToyatoCar(Car):
#     def __init__(self,brand):
#         self.brand = brand

# class Fortuner(ToyatoCar):
#     def __init__(self,type):
#         self.type = type

# car1 = Fortuner("Petrol")
# car1.start()

# #multiple inhr
# class A:
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A,B):
#     varC = "Welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

#Class method: A class method is bound to the class & receives the class as an implicit first argument.

# class Person:
#     name = "anonymous"

#     @classmethod
#     def changeName(cls,name):
#         cls.name = name

# p1 = Person()
# p1.changeName("Abhay")
# print(p1.name)
# print(Person.name)

#Polymorphism: operator overloading
#When the same operator is allowed to have different meaning according to the context.
#operator & Dunder Function
# a+b  #addition            a.__add__(b)
# a-b  #substraction        a.__sub__(b)
# a*b  #multiplication      a.__mul__(b)
# a/b  #division            a.__truediv__(b)
# a+b  #mod                 a.__mod__(b)

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def show(self):
#         print(self.real,"i +",self.img,"j")

#     def __add__(self, num2):   #Dunder function
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

# num1 = Complex(1,6)
# num1.show()

# num2 = Complex(2,3)
# num2.show()

# num3 = num1 + num2
# num3.show()
# num3 = num1.add(num2)
# num3.show()

#Define a Circle class to create a circle radius r using the constructor.
#Define on Area() method of the class which calculates the areaa of the circle.
#Define a Perimeter() method of the class which allows you to calculate the perimeter of the circlce.
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())

#Define a Employee class with attributes role,department and salary. This class also has showDetails() method.
#Create an Engineer class that inherits properties from employee & has additional attributs: name & age.

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role - ",self.role)
#         print("department - ",self.dept)
#         print("salary - Rs.",self.salary)

# class Enginner(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer","35","60000")

# e1 = Employee("Accountant","Finance","60,000")
# e1.showDetails()

# eng1 = Enginner("Elon",40)
# eng1.showDetails()
