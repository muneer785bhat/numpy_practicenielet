    
   # Dictionary in python is an unordered collection of data values uesed to store data values like a map ,which unl
    
    #

    
my_dict ={
        "name":"muneer",
        "age":24,
        "city":"Srinagar"
    }
    
print(my_dict)

#Accessing elements 
print(my_dict["name"])
print(my_dict.get("age"))
print(my_dict.get("cit","name"))

#Adding new values
my_dict["email"] =  "muneer@example.com"

print(my_dict)

#updating values

my_dict["age"] = 23

print(my_dict)
 
 
#Removing elements 

my_dict.pop("city")

print(my_dict)
my_dict.popitem()# remoes the last item

print(my_dict) 

#my_dict.clear()# clears te dictionary      
print(my_dict)


# Dictionary methods 

print(my_dict.keys())# return all keys present in the dictionary
print(my_dict.values())# return all values present in te dictionary
print(my_dict.items())# return all key value pairs as tuple in a list 


#Looping through a dictionary

for key in my_dict:
    print(key)
    
    for value in my_dict.values():
        print(value)
        
    for key,values in my_dict.items():
        print(f"{key}, {values}")
        
    
    
    
    # Nested Dictionary
    Students ={
        "student1":{
            "name":"muneer",
            "age":34,
            "city":"Srinagar"
            
        },
        "student2":{"name":"mehraj",
                  "age":28,
                  "city":"Srinagar"
            
        }
    }
    
    
    print(Students)
    print(Students["student1"]["name"])
    