
###//////////////////////// Tuple //////////////////////////
#Tuple is a collection of items which is ordered and unchangeable. It allows duplicate members.
#Duplicted
#Oderd
#Hetrogenus
#immutable

tuple = (1,2,3,4,5,6,6,6,"hello",4.5)
print ("This is my tuble :--  ",tuple)
print ("lenth of tuple is :--  ",len(tuple))
print ( "Type of my tuble :--  ",type(tuple))
print("Indexing in python tuble>>>>>")
print(tuple[0])
print(tuple[1:4])
print(tuple[-2])
print("sicing in python tuple")
print(tuple[2:4])
print(tuple[::-1])  #revercing


print(tuple.count("hello"))
print(tuple.index(6))

###Tuple unpacking
a,b,c = (1,2,3)
print(a)
print(b)
print(c)


a = (2,3,243,4,5,4,64,"ankush","bittu",35,34)
print(a)
print(type(a)) # agar numbers esse open hoge to wo tuple hi hoge 
