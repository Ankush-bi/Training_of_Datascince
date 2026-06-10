t #////////////////////////////////////////////Assignment 1:////////////////////////////////////////////
# 1. Create a string variable with your name and perform the following operations: 
# Print the first character  
# Print the last character 
# Print the length of the string  
# Convert the string to uppercase  
# Convert the string to lowercase 
# Reverse the string using slicing 

name = "Ankush soni"
print(name[0])
print(name[10])
print("Your strlening lenth is :-",len(name))
upper_case = name.upper()
print("upper case is :-",upper_case)
lower_case = name.lower()
print("print lower case is:- ",lower_case)
print(name[::-1])

# 2. Write a Python program to perform string slicing on a given string: 
# Print the first four characters 
# Print characters from index 2 to 5 
# Print the complete string in reverse order 


str = ("Datascince and AI&ML")
print(str[:4])
print(str[2:5])
print(str[::-1])

# 3. Create a list containing numbers and perform the following operations:
# Add an element using append()
# Insert an element at a specific position
# Remove an element using remove()
# Delete the last element using pop()
# Reverse the list
# Sort the list
# Find the length of the list
# Count the occurrence of an element 

list = [1,2,3,4,5,6,7,8,9,10]
# append() is a list method used to add a new element to the end of a list
list.append(23)
print(list)

list.insert(12,24) #12 position pe 24 no. insert mtlp store ho jayga
print(list)

list.remove(1)  #remove use to , remove the value
print(list)

list.pop(8)  #8th positon se 10 pop mtlp dlt ho jayga way use of pop
print(list)

list.reverse()
print(list)

list.sort()  #The sort() method is used to arrange the elements of a list smallest to largest
print(list)

print("lenth of list is :- ",len(list))  #length

list.count(list)
print(list)


# 4. Create a tuple containing 5 subjects. Perform the following operations:
# Print the first element
# Print the last element
# Print the length of the tuple
# Print elements using slicing
# Find the maximum, minimum, and sum of numerical tuple elements 


tuple = (1,2,3,4,5,6,6,6,"hello",4.5)
print(tuple[0])
print ("lenth of tuple is :--  ",len(tuple))
print(tuple[9])
print(tuple[::-1])  #slicing
print(tuple[2:4])  #slicing



num = (12,3,4,6,7,4,6,4) #max,mini.tatal mai bus int hone chaiye warna error show hogi
maximum = max(num)
minimum = min(num)  
total = sum(num)

print("Tuple:", tuple)
print("Maximum element:", maximum)
print("Minimum element:", minimum)
print("Sum of elements:", total)


# 5. Write a Python program to demonstrate tuple packing and unpacking. 
# Create a tuple of four values and assign them to four separate variables. 


# Tuple Packing: Combining multiple values into a single tuple.
# Tuple Unpacking: Assigning tuple elements to separate variables.

# Tuple Packing
student = ("Ankush", 20, "CSE", 8.5)

# Tuple Unpacking ka matlab hai tuple ke elements ko alag-alag variables me assign karn
name, age, branch, cgpa = student


print("Name:", name)
print("Age:", age)
print("Branch:", branch)
print("CGPA:", cgpa)

# 6. Create a dictionary containing student details:
# Name
# Age
# Course
# Address 

# Perform the following operations:

# Print all keys 
# Print all values
# Print all items
# Update the Address
# Add a new key called "Branch" 

student={
    "name":"ankush",
    "class":"3rd year",
    "branch":"CSE",
    "address":"bharatpur"
}

print("keys: ",student.keys())
print("values: ",student.values())
print("items: ",student.items())
student.update({"address":"jaipur"})
print("after update :",student)
student.setdefault("branch","CSE")
print("after add branch :",student)


# 7.Write a Python program to access an element from a nested list. 
# Example: [1, 2, 3, 4, [2, 5], 7] Print the value 5 using indexing

lst = [1, 2, 3, 4, [3,6], 7]

print(lst[4][1])
print(lst[4][0])

# 8.Write a Python program to take a number as input from the user and:
# Add 10 using the += operator
# Print the updated value

num = int(input("Enter a number: "))
print(num)
num += 10
print("Add 10 in number :", num)

# 9.Write a Python program to demonstrate type casting:
# Take two numbers as input from the user
# Convert them to integers
# Print their multiplication
a = int(input("Enter a: "))
b = int(input("Enter b: "))
mul = a * b
print("Multiplication =", mul)


# 10.Create a dictionary and demonstrate the use of:
# get()
# keys()
# values()
# items()

tudent={
    "name":"Ankush",
    "age":21,
    "course":"23cs016",
    "address":"bharatpur",
}
print(student.get("name"))
print("keys: ",student.keys())
print("values: ",student.values())
print("items: ",student.items())

# 11.Create a copy of a list using copy() and print both the original and copied lists.

l1=[1,3,4,2,"hii"]
l2=l1.copy()
l2[4]= "hello"
print("Original list :",l1)
print("Copy list :",l2)