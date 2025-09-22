
# class BankAccount:
#     def __init__(self, account_number, account_holder, balance):
#         self.account_number = account_number
#         self.account_holder=account_holder
#         self.balance=balance
    
#         print(self.account_number,self.account_holder,self.balance)
# obj1=BankAccount(account_number=12345678, account_holder='John Doe', balance=1000.0)
# obj2=BankAccount(account_number=12345678, account_holder='John Smith', balance=1000.0)
# obj3=BankAccount(account_number=12345678, account_holder='FOPP Doe', balance=1000.0)
# obj4=BankAccount(account_number=12345678, account_holder='John ', balance=1000.0)
# obj5=BankAccount(account_number=12345678, account_holder='John Doe', balance=1000.0)
# obj6=BankAccount(account_number=12345678, account_holder='John Doe', balance=1000.0)
# obj7=BankAccount(account_number=12345678, account_holder='John Doe', balance=1000.0)
# obj8=BankAccount(account_number=12345678, account_holder='John Doe', balance=1000.0)
# obj9=BankAccount(account_number=12345678, account_holder='John Doe', balance=1000.0)
# obj=[obj1,obj2,obj3,obj4,obj5,obj6,obj7,obj8,obj9]
# # Create a list of tuples with (account_number, account_holder, balance)
# account_info = [
#     (i.account_number, i.account_holder, i.balance)
#     for i in obj
# ]
# print(account_info)



###### About Data types in python
# listname=["John", "Jane", "Doe"]
# print(listname)
# listname.append("Smith")
# print(listname)
# listname.remove("Jane")
# print(listname)
# listname.pop(-1)
# print("After pop at -1:", listname)
# listname.insert(1,"Alice")
# print("After insert at 1:", listname)
# remove  is not supported with index
# listname.pop(1)
# print("After pop at 1:", listname)


# dict1={"name":"srinu","age":22}
# print(dict1)
# dict1={"name":"ajay","age":22}
# print(dict1)

# dict1.update({"city":"hyd","age":24})
# print(dict1)
# dict1.pop("age")
# remove is not supported in dict
# print(dict1)
# dict1.clear()
# print(dict1)






#setname={"apple","banana","cherry","orange","apple","banana","cherry","apple","banana","cherry"}
#print(setname)

# print(setname)
#setname.add("orange")
#print(setname)
# it is remove all duplicates
# setname.remove("banana")
# pop is not supported in set
# print(setname)



#frozensetname=frozenset({"apple","banana","cherry"})

#print(frozensetname)
# frozensetname.add("orange") is not supported
#print(frozensetname)
# frozensetname.remove("banana") is not supported
# frozensetname.pop() is not supported
#frozensetname.clear() is not supported
#frozensetname.update() is not supported

# rangename=list(range(1,10,2))
# print(rangename)
# rangename.append(11)
# print(rangename)
# rangename.remove(5)
# print(rangename)
# print(rangename[2:5])

#tuplename=("apple", "banana", "cherry")
#print(tuplename)
#tuplename.add("orange") is not supported to adding any 
#print(tuplename) #is not supported

# boolname=True
# intname=10
# print(intname)
# intname1=-5
# print(intname)
# floatname=10.5
# strname="Hello, World!"




"""   adding in data types 

rollertuple=(1,2,3,4,5,1,2,3,4,5,6)
rollerlist=[1,2,3,4,5,1,2,3,4,5,6]
rollerset={1,2,3,4,5,1,2,3,4,5,6}
frozen=frozenset({1,2,3,4,5,1,2,3,4,5,6})
roller=(1,2,3,4,5,1,2,3,4,5,6)
integername=34
stringname="ashok"



print(roller)
# roller.add(34)
print("adding in tuple not occurs",)



print(rollerlist)
rollerlist.append(510)
rollerlist.append(54)
print("adding in list",rollerlist)

# rollertuple.update(380)
# print(rollertuple)
print(rollerset)
rollerset.add(340)
print("adding in set",rollerset)
print(frozen)
#frozen.add(34)
print("frozenset is adding is not working")

print(integername)
integername=78
print(integername)



print(stringname)
stringname="doing"
print(stringname)



"""



# About OOP concepts



"""
 what is OOP?

 ans: OOP stands for Object-Oriented Programming. It is a programming paradigm that uses "objects" to represent data and methods to manipulate that data. OOP focuses on the concepts of encapsulation, inheritance, polymorphism, and abstraction to create modular and reusable code.
1.inheritance

  Inheritance is a mechanism in OOP that allows one class (child class) to inherit the attributes and methods of another class (parent class). This promotes code reusability and establishes a relationship between classes.
   Types of inheritance:
  
  single inheritance: A child class inherits from only one parent class.
   mainclass -> subclass

  multiple inheritance: A child class inherits from multiple parent classes.
   mainclass -> subclass1 ->subclass2
               

  multilevel inheritance: A class is derived from a class which is also derived from another class.
    mainclass -> subclass1 -> subclass2
  
  hierarchical inheritance: Multiple child classes inherit from a single parent class.
    mainclass -> subclass1
               -> subclass2
  hybrid inheritance: A combination of two or more types of inheritance.
    mainclass -> subclass1 -> subclass2
2.polymorphism

   Polymorphism is the ability of different objects to respond to the same method call in different ways. This is often achieved through method overriding and interfaces.


3.encapsulation

   Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, or class. It restricts direct access to some of the object's components, which is a means of preventing unintended interference and misuse of the methods and data.

4.abstraction

   Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object. It helps in reducing programming complexity and increases efficiency.

5. classes and objects

    A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have. An object is an instance of a class, containing real values instead of variables.

6. overriding
    Overriding is a feature in OOP that allows a subclass to provide a specific implementation of a method that is already defined in its superclass. This is used to achieve runtime polymorphism.


"""

# Example of single inheritance
# class AnimalParent:
#     def method(self):
#         print("This is parent class method")

# class AnimalChild(AnimalParent):
#     def method1(self):
#         print("This is child class method")
# child1=AnimalChild()
# child1.method1()  
# child1.method()

# Example of multiple inheritance
# class AnimalParent1:
#     def method1(self):
#         print("This is parent class method 1")
# class AnimalParent2:
#     def method2(self):
#         print("This is parent class method 2")

# class AnimalChild(AnimalParent1, AnimalParent2):
#     def method3(self):
#         print("This is child class method 3")

# child2=AnimalChild()
# child2.method1()
# child2.method2()
# child2.method3()

#multilevel inheritance


# class GrandParent:

#     def method1(self):
#         print("This is grand parent class method 1")
# class Parent(GrandParent):        
#     def method2(self):
#         print("This is parent class method 2")
# class Child(Parent):
#     def method3(self):
#         print("This is child class method 3")

# child=Child()

# child.method1()
# child.method2()
# child.method3()

# hirearchical inheritance
# class Parent:
#     def method1(self):
#         print("This is parent class method 1")
# class Child1(Parent):
#     def method2(self):
#         print("This is child1 class method 2")
# class Child2(Parent):
#     def method3(self):
#         print("This is child2 class method 3")

# child=Child1()
# child.method1()
# child.method2()
# child1=Child2()
# child1.method1()
# child1.method3()



# hybrid inheritance

# class GrandParent:
#     def method1(self):
#         print("This is grand parent class method 1")
# class Parent1(GrandParent):
#     def method2(self):
#         print("This is parent1 class method 2")
# class Parent2(GrandParent):
#     def method3(self):
#         print("This is parent2 class method 3")
# class Child(Parent1, Parent2):        
#     def method4(self):
#         print("This is child class method 4")
# child=Child()        
# child.method1()
# child.method2()
# child.method3()
# child.method4()



# Example of overloading 




# class universitymember:
#     def __init__(self, firstname, lastname,email,memberid,address):
#         self.firstname=firstname
#         self.lastname=lastname
#         self.email=email
#         self.memberid=memberid
#         self.address=address
# class Teacher(universitymember):
#     def __init__(self, firstname, lastname, email, memberid, address, teachingsubject, salary):
#         super().__init__(firstname, lastname, email, memberid, address)
#         self.teachingsubject = teachingsubject
#         self.salary = salary
# class student(universitymember):
#     def __init__(self, firstname, lastname, email, memberid, address, Gpa, course):
#         super().__init__(firstname, lastname, email, memberid, address)
#         self.Gpa = Gpa
#         self.course = course
        

# member = universitymember("John", "Doe", "john@example.com", 2, "Some Address")
# print(member.firstname)



# overriding

# class Function():
#    def add(self,a,b,c):
#        print("Main:",a + b + c)

# # class FunctionChild(Function):
#    def add(self,a,b,c):
#        print("Child:",a + b - c)

# class FunctionGrandChild(FunctionChild):
#    def add(self,a,b,c):
#        print("GrandChild:",a * b * c)


# function1=Function()
# # function2=FunctionChild()
# # function3=FunctionGrandChild()
# function1.add(1,2,3)  
# function1.add("srinu","vas","reddy") 
# function1.add([1,2,3],[1,2,3],[4,5,6]) 
# function1.add((3,3,3),(1,2,3),(1,2,3))


#function1.add({"srinu"},{"reddy"},{"thimmareddy"})# not supported set
#function1.add({"name":"srinu"},{"name":"ashok"},{"name":"ajay"}) # not supported


# encapsulation