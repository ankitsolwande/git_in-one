# n=5
# print(" "*(n+3) + "*"*10,"*"*10)
# for i in range(n):
#     print("*" + " "*(n-i) + "*" + " "*(i) + "*"," "*13,"*"," "*4,"*"," "*8+"*")
# print(" "*(n+3) + "*"*10," "*3,"*"," "*4,"*"," "*8+"*")
# for i in range(n):
#     print("*" + " "*(i) + "*" + " "*(n-i) + "*"," "*13,"*"," "*4,"*", " "*8+"*")
# print(" "*(n+3) + "*"*10," "*10,"*"*11)

#  Write a program to build a simple Student Management System
# using Python which can perform the following operations:
# Accept, Display, Search, Delete, Update
# Accept – This method takes details from the user like name, roll number, and marks for
# two different subjects
# Search – This method searches for a particular student from the list of students. This
# method will ask the user for roll number and then search according to the roll number
# delete – This method deletes the record of a particular student with a matching roll
# number
# Update – This method updates the roll number of the student. This method will ask for
# the old roll number and new roll number. It will replace the old roll number with a new roll
# number.

# class Brainworks:
#     clsname="Brainworks"
#     def Accept(self):
#         num_stu=int(input("enter the number of student: "))
#         for i in range(num_stu):
#             print("Enter the student record")
#             self.name1=input("Enter the name of student: ")
#             self.rollno1=int(input("Enter the roll no of student: "))
#             self.marks1=int(input("Enter the marks of student: "))
#             self.marks2=int(input("Enter the marks of student: "))
#             lst1.append([self.name1,self.rollno1,self.marks1,self.marks2])
#     def Search(self,lst):
#         self.lst=lst
#         rollno=int(input("enter the roll no of student to find the record: "))
#         for j in self.lst:
#             if j[1]==rollno:
#                 return j
#     def Delete(self,lst):
#         self.lst=lst
#         rollno=int(input("enter the roll no of student to delete the record: "))
#         for k in self.lst:
#             if k[1] == rollno:
#                 lst.remove(k)
#     def Update(self,lst):
#         self.lst=lst
#         rollno=int(input("enter the roll no of student to Update the record: "))
#         for k in self.lst:
#             if k[1] == rollno:
#                 new_num=int(input("Enter the new number: "))
#                 k[1]=new_num

# lst1=[]
# obj=Brainworks()

# obj.Accept()

# print("The whole infirmation of student is: ",obj.Search(lst1))

# print("user will be deleted successfully",obj.Delete(lst1))
# print("updated list of student is: ",lst1)

# print("the updated list  of student is: ",obj.Update(lst1))
# print(lst1)


# inheritance:
#the mech of deriving new class from and old one such that new class inherits all the properties of old class it is called inheritance:
# there are four types of inheritance in python:
# single level inheritance 
# multi-level-inheritance
# multiple inheritance
# hierarchical inheritance
# hybrid inheritance

# Encapsulation
# it is the term refers to the wrapping up of data that means combining a methods and variables in the single unit and restrict
# that access from outside of the class that means we can not access this methods and variables outside of the class. Private methods
# and variables can not accessible from outside of the class

# e.g
# using private varible
# class disp:
#     def __init__(self):
#         self.__a=20
#     def method1(self):
#         print(self.__a)

# obj=disp()
# obj.method1()
# print(obj.__a)

from abc import ABC,abstractclassmethod

class polygon(ABC):
    @abstractclassmethod
    def sides(self):
        pass
    def Area(self):
        print("My area is 900m")
class Square(polygon):
    def sides(self):
        print("squares have 4 sides")
class hexagonal(polygon):
    def sides(self):
        print("the hexagon has 8 sides")
obj=Square()
obj.sides()
obj.Area()

obj1=hexagonal()
obj1.sides()
obj1.Area()