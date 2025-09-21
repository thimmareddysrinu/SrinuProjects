
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


# class Parent1:
#     def method1(self):
        
#         print("Method 1 from Parent 1")
# class Parent2:        
#     def method2(self):
#         print("Method 2 from Parent 2")
# class Parent3:
#     def method4(self):

#         print("Method 4 from Parent 3")
# class Parent4:
#     def method5(self):
#         print("Method 5 from Parent 4")

# class Child(Parent1, Parent2,Parent3,Parent4):
#     def method3(self):
#         self.name=Parent1()
#         print("Method 3 from Child")

# child2=Child()

# child2.method1()
# child2.method5()
# child2.method4()
# child2.method2()
# child2.method3()



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







boolname=True
intname=10
print(intname)
intname1=-5
print(intname)
floatname=10.5
strname="Hello, World!"