# # Ankush = 21
# # print(Ankush)


# # num = 32
# # print("num")


# #camel case
# myNameIsAnkush = "Ankush soni"
# print(myNameIsAnkush)

# #snake case
# my_name_is_ankush = "Ankush soni"
# print(my_name_is_ankush)



# #string........
# name = ("ankush")
# print("this is my first string :-",name)
# print("type of my straig",type(name))
# print("len of my string",len(name))
# print("indexing")

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[3])


# #sicing....///
# print(name[0:4])
# print(name[2:4])
# print(name[0:-4])
# print(name[0:4:2])
# print(name[0:4:1])


#UPPER CASE
# name = "ankush"
# upper_case = name.upper()
# print("upper case :", upper_case)


# num = "234567"
# print(len(num))


# name = "PIYUSH"
# case_fold_function = name.casefold()
# print(case_fold_function)


# name = "ankush"
# print(name.capitalize())


# name = "ankush"
# print(name.index("a"))
# print(name.count("k"))
# print(name.find("h"))


# name = "HEY ANKUSH"
# print(name.replace("HEY","BYE"))

################isalnum

# char = "hellloo356578"
# print(char.isalnum())

# char = "HELO"
# print(char.isalpha())


# name = "kumar shab"
# print(name.isalpha())


# name = "soni ji"
# print(name.split())


# intro = """My name is Ankush Soni. I am currently pursuing a Bachelor of Technology (B.Tech) degree in Computer Science and Engineering. I have a strong interest in technology, especially in Python programming, Artificial Intelligence, and Machine Learning.

# During my studies, I have worked on various academic projects and continuously improved my technical skills in programming, problem-solving, and software development. I am also familiar with tools such as Python, Jupyter Notebook, and basic data analysis concepts.

# Apart from academics, I enjoy learning new technologies, improving my communication skills, and staying updated with the latest trends in the IT industry.

# I consider myself a hardworking, quick learner, and team-oriented person. As a fresher, I am looking for an opportunity where I can apply my knowledge, gain practical experience, and contribute to the growth of the organization while developing my professional skills.

# Thank you."""

# print(intro)


##################### STRING FORCASTING


# name = "ankush"
# age = "55"

# print(f"My nama is{name} and my age is {age}")




# name = "Ankush"
# age = 21
# print(f"Hello my name is{name},and my age is{age}")

# name = input("Enter your name")
# print(f"Hello,{name}!")



# path = r"/home/user/Desktop/Training/python/main.pyFile"
# print(path)
# import os
# print(os.listdir(path))


# colleg_name = "Anand"
# college_add = "kanota"
# print(colleg_name *3)
# print(college_name * college) #this is wrong


###################### LIST#########################
# list is a collection of items which is ordered and changeable. It allows duplicate members.
# Array is a collection of items which is ordered and changeable. It allows duplicate members. But it is more efficient than list because it stores only one type of data.

# list = [1,2,3,4,5,"Hello","hey"]
# print(list)
# print(type(list))
# print(len(list))
# print(list[0])
# print(list[2:4])
# print(list[5])

# # print(list.append(100))
# list.append(100)           #use of append function is to add an element at the end of the list.
# new_list = [1,3,4,56,]     #use of extend function is to add multiple elements at the end of the list.
# print(list + new_list)     # list + new_list is used to concatenate two lists.
# list.insert(2,200)         #use of insert function is to add an element at a specific position in the list.



# list.pop()
# list.pop(0)
# list.remove("Hello")
# print(list.index("hello"))
# list.copy()
# print(lst.count(2)) 
# list.reverse()
# list.sort()

# list = [1,2,3,4,5,6,[3,4,5]]
# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,]
#print(list1+list2)   #yes
# print(list1-list2) #no
#print(list1*list2) #no
# print(list1/list2) #no
# print(list2*3) #yes


###//////////////////////// Tuple //////////////////////////
#Tuple is a collection of items which is ordered and unchangeable. It allows duplicate members.
#Duplicted
#Oderd
#Hetrogenus
#immutable

# tuple = (1,2,3,4,5,6,6,6,"hello",4.5)
# print ("This is my tuble :--  ",tuple)
# print ("lenth of tuple is :--  ",len(tuple))
# print ( "Type of my tuble :--  ",type(tuple))
# print("Indexing in python tuble>>>>>")
# print(tuple[0])
# print(tuple[1:4])
# print(tuple[-2])
# print("sicing in python tuple")
# print(tuple[2:4])
# print(tuple[::-1])  #revercing


# print(tuple.count("hello"))
# print(tuple.index(6))

###Tuple unpacking
# a,b,c = (1,2,3)
# print(a)
# print(b)
# print(c)


# a = (2,3,243,4,5,4,64,"ankush","bittu",35,34)
# print(a)
# print(type(a)) # agar numbers esse open hoge to wo tuple hi hoge 


# ///////////////////// Type casting ////////////////
tuple = (2,3,243,4,5,4,64,"ankush","bittu",35,34)
print("This is tuple before type casting :--",tuple)
print(len(tuple))
print("Type of tuple :-- ",type(tuple))

print("Type casting in python tuple")
print("tuple covert into list :--")
lst = list(tuple)


print("This is my list after type casting :--",lst)
print("Type of my list :-- ",type(lst))
lst.append(100)


#print(tuple(lst))
print("This is my list after adda any item :--",lst)
print("list covert into tuple:----")
tpl = tuple(lst)
print("This is tuple after add itrm",tpl)
