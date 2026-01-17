"""
Tuple:
A tuple is a collection that is:
-ordered
-immutable
-allow duplicate elements
-tuple is wrritten using parenthesis"""

my_tuple = (10,20,30,40)
print(my_tuple)

t1 = ()#empty tuple

t2 = (1,2,3)#tuple with multiple elements 

t3 = (1,)#single element tuple(note the comma after 1 is mandatory)

t4 = (1,2,3,4,"Hello",True,0.5)#tuple with different data types 

print(t1)
print(t2)
print(t3)
print(t4)


#Accessing tuple elements using indexing 

print(my_tuple[0])
print(my_tuple[-1])

#Slicing 
my_tuple = (10,20,30,40)
print(my_tuple[1:3])#(20,30)->index 1 to index 2
print(my_tuple[1:])#(20,30,40)->index 1 to end
print(my_tuple[:3])#(10,20,30)->start to index 2


#tuple is immutable :means cant change the elements of tuple
my_tuple =(10,20,40)
#my_tuple[1]=25 #typeError :'tuple' object does not support item assinment
print(my_tuple)

#tuple methods(only 2 methods avaialed)
my_tuple =(10,20,30,20,40,60,70)

print(my_tuple.count(20))

print(my_tuple.index(70))



#Loooping through a tuple
t = ("apple","banana","cherry")
for item in t:
    print(item)

nums = (1,2,3,3,45,5,67,6,67)

i = 0

while i < len(nums):
    print(nums[i])
    i += 1
#tuple packing and unpackig

#packing
person = ("muneer",21,"india")

#unpacking
name,age,cuntry = person
print(name,age,cuntry)

