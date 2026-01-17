"""
LIST: A list is a colection which is ordered and changeable allows duplicate members 
Can store different data types
"""




my_list =[10,20,30,40,50,"muneer",True,5.5]

print(my_list)

#Accessing list elements using index 

numbers = [100,200,30,400,50,600]

print(numbers[0])#first element 
print(numbers[1])#second element
print(numbers[2])#tird element 
print(numbers[3])#fourth element
print(numbers[4])#fifth element
print(numbers[5])#sixth element


#Slicing in list

nums = [1,2,3,4,5]

print(nums[1:4])
print(nums[:3])
print(nums[2:])


#Modifying list elements 


nums = [10,20,30,40]
nums[1] = 200

print(nums)


#methods

a = [1,2,3,4,5]

a.append(6)
print(a)#1,2,3,4,5,6
a.extend([7,8,9,10])#  extend()->add multiple elements 
print(a)
a.insert(0,19)#insert()-> add element at specific position
print(a)
a.remove(10)#remove()-> remove specific element 
print(a)#removes 10
a.pop()#pop()-> removes last element 
print(a)
a.pop(0)#removes element at 0 index 
print(a)
a.clear()#clear()-> removes all elements from list
print(a)

b = [5,20,40,30]
print(b.index(30))#index()-> return index of specific element 

print(b.count(20))#count()-> return number of occurance of an element in a list

print(b)


b.sort()#sort()-> sort the lst in ascending order 

print(b)

a = [3,24,5,2,1]
a.sort()
print(a)
a.reverse()#reverse()-> reverse te list
print(a)


c = [10,20,30,40]
print(c)

d =c.copy()#copy()-> creates a copy of te list

print(d)

#list operations 

#1:Concatenation

a = [1,2,3]
b = [4,5,6]

print(a +b)#[1,2,3,4,5,6]


#2:Repitition

a = [1,2,3,4,5,6,7]
print(a *3)#1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7


#Looping throug  a list

fruits = ["apple","banana","cherry"]

for fruit in fruits:
    print(fruit)
nums = [1,2,3,4,5,6]
i = 0
while i < len(nums):
   print(nums[i])
   i+=1


#LIST COMPREHENSION

squares = [x**x for x in range(1,6)]

print(squares)#[1,4,9,16,25]

#difference b/w  extend() and append()

a = [1,2,3]
a.append([4,5])#adds the entire list as a single element 

print(a)#1,2,3,[4,5]

a.extend([6,7])#adds each element of the list individually

print(a)#1,2,3,[4,5],6,7