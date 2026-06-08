
###################### LIST#########################
# list is a collection of items which is ordered and changeable. It allows duplicate members.
# Array is a collection of items which is ordered and changeable. It allows duplicate members. But it is more efficient than list because it stores only one type of data.

list = [1,2,3,4,5,"Hello","hey"]
print(list)
print(type(list))
print(len(list))
print(list[0])
print(list[2:4])
print(list[5])

# # print(list.append(100))
list.append(100)           #use of append function is to add an element at the end of the list.
new_list = [1,3,4,56,]     #use of extend function is to add multiple elements at the end of the list.
print(list + new_list)     # list + new_list is used to concatenate two lists.
list.insert(2,200)         #use of insert function is to add an element at a specific position in the list.



list.pop()
list.pop(0)
list.remove("Hello")
print(list.index("hello"))
list.copy()
print(list.count(2)) 
list.reverse()
list.sort()

list = [1,2,3,4,5,6,[3,4,5]]
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,]
print(list1+list2)   #yes
print(list1-list2) #no
print(list1*list2) #no
print(list1/list2) #no
print(list2*3) #yes