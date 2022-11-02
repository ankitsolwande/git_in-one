# # working with classes and instances
# class Car:
#     def __init__(self, make, model, year):
#         """initialize attributes to describe a car"""
#         self.make = make
#         self.model = model
#         self.year = year
# # Setting a Default Value for an Attribute
#         self.odometer = 0

#     def get_descriptive_name(self):
#         """return a neatly formatted descriptive name"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def get_odometer_reading(self):
#         """print statement showing car's mileage"""
#         print(f"my car has {self.odometer} miles on it.")

#     def update_odometer(self, mileage):
#         self.odometer = mileage

# # we can extend the method update_odometer() to do additional work so that every time odometer reading is modified
# # make sure no one can roll back the odometer reading

#     def update_odometer_conditional(self, mileage):
#         if mileage > self.odometer:
#             self.odometer = mileage
#         else:
#             print("you can't roll back an odometer.")

#     def increment_odometer(self, mileage):
#         self.odometer += mileage


# my_car = Car("audy", "a4", 2022)
# print(my_car.get_descriptive_name())
# my_car.get_odometer_reading()

# # modifying value of attributes
# # [1] Modifying an Attribute’s Value Directly -- simple way to modify the value of an attribute is to access the
# # attribute directly through an instance

# my_car.odometer = 25
# my_car.get_odometer_reading()

# # [2] Modifying an Attribute’s Value Through a Method -- instead of accessing the attribute directly, you pass the new
# # value to a method that handles the updating internally and call a method with argument

# my_car.update_odometer(22)
# my_car.get_odometer_reading()

# my_car.update_odometer_conditional(21)
# my_car.get_odometer_reading()
# my_car.update_odometer_conditional(25)
# my_car.get_odometer_reading()

# # [3] Incrementing an Attribute’s Value Through a Method
# # sometimes we need to increment attributes value by certain amount rather than changing whole value.

# my_car.increment_odometer(5)
# my_car.get_odometer_reading()


# class disp:
#     x=10
#     def __init__(self):
#         self.y=20

# t1=disp()
# t2=disp()
# t3=disp()
# t4=disp()
# print("----------------------------")
# print(t1.x,t1.y)
# print(t2.x,t2.y)
# print(t3.x,t3.y)
# print(t4.x,t4.y)
# print("----------------------------")
# disp.x=999
# t2.y=800
# print(t1.x,t1.y)
# print(t2.x,t2.y)
# print(t3.x,t3.y)
# print(t4.x,t4.y)
# print("-------------------")
# disp.x=1000000
# disp.y=90
# print(t1.x,t1.y)
# print(t2.x,t2.y)
# print(t3.x,t3.y)
# print(t4.x,t4.y)

# from functools import reduce
# l1=[3,6,8,9,3]
# l2=[4,2,6,8]
# print([int(x) for x in (str((int(reduce(lambda x,y:str(x)+str(y),l1))) +(int(reduce(lambda x,y:str(x)+str(y),l2)))))])

# n=10
# for i in range(n):
#     if i<int(n/2):
#         print(" "*(n-i)+" *"*i)
#     else:
#         print(" "*(i) + " *"*(n-i))

# import re
# str_="ab9v10h100m4"
# print("".join(list(map(lambda x ,y:int(x)*y,re.sub("[a-z]"," ",str_).split(),re.sub("[0-9]"," ",str_).split()))))

# str_="aaaabbbbcccaaannlllaaa"
# char=str_[0]
# op=""
# cnt=0
# for ch in str_ :
#     if ch == char :
#         cnt+=1
#     else:
#         op+=(char+str(cnt))
#         cnt=1
#         char=ch
# op+=(char+str(cnt))
# print(op)

# # pattern prog:
# num=10
# for i in range(num):
#     print("* "*i)
# for i in range(num,-1,-1):
#     print("* "*i)
# for i in range(num,-1,-1):
#     print(" "*(num-i),"*"*i)

# for i in range(num):
#     print(" "*(num-i),"$"*i+"*"*(num-i))

# s="ankit"
# for i in range(len(s)):
#     print("positive index: ",i,"negative index: ",i-len(s),s[i])

#bubble sort:
# lst=[90,56,80,54,12,10]
# for i in range(len(lst)-1,-1,-1):
#     for j in range(i):
#         if lst[j]>lst[j+1]:
#             x=lst[j]
#             lst[j]=lst[j+1]
#             lst[j+1]=x   
# print(lst)

# str_="vaishnavi"
# print(" ".join(set(filter(lambda x :str_.count(x)>1,str_))))
# cnt=0
# lst=[]
# op=""
# for i in str_:
#     if i in lst:
#         op+=i
#     else:
#         lst.append(i)
# print(op)
# print("".join({x for x in str_ if str_.count(x)>1}))


# s=[1,10,9,12,4,5,7]
# x=[7,4,3,2,1,6,5]
# op=dict(zip(s,x))
# print(sorted(s,key=op.get))


