# A dictionary stores data as key: value pairs — 
# like a real dictionary where you look up a word (key) to find its meaning (value).
# use of di

# student={
#     "name":"krishan",
#     "class":"3rd year",
#     "branch":"CSE",
#     "college_id":"23cs048",
#     "mob_no":1234567890,
#     "address":"lalsot"
# }

# print(student)
# print ("length of student :",len(student))
# print ("type of student :",type(student))

# print("value found :->>>>>>>>>>>>>")
# print(student["name"])
# print(student["class"])
# print(student["branch"])
# print(student["college_id"])
# print(student["mob_no"])
# print(student["address"])

# print(student.get("name"))

# student["cgpa"]=7.3
# student["name"]="kalpesh"
# print(student)

# key= input("Enter your key:--- ")
# print(f"your {key} is :",student[f"{key}"])




# jaipur = {"name":"Jaipur","pin_code":23456,"Area":"Agra road","compny_name":"codeyart"}
# pushkar = jaipur.setdefault("name","default value")
# pushkar = jaipur.setdefault("ankush")  
# # setdefault me agar key already exist karti hai to uski value return karti hai aur agar key exist nahi karti hai to usko create kar deti hai aur usme value daal deti hai
# print(pushkar)  # ankush ka value none hai kyuki setdefault me value nahi di gai hai
# print(jaipur)


#update  method use karke hum dictionary me naye key value pair add kar sakte hai ya existing key ki value ko update kar sakte hai
# Dict = {"name":"ankush","age": 233,"college":"anand"}
# Dict.update( {"age":32,"num":3456787654} )
# print(Dict)

# Deep copy and shallow copy in dictionary
# Deep copy me original dictionary ke andar jo bhi changes karte hai wo copied dictionary me reflect nahi hote hai 
# aur shallow copy me original dictionary ke andar jo bhi changes karte hai wo copied
# import copy

# original = [[1, 2], [3, 4]]

# copied = copy.deepcopy(original)

# copied[0][0] = 100

# print("Original:", original)
# print("Copied:", copied)
# explain this code line by line 
# 1. import copy kara gaya hai jisse hum deep copy aur shallow copy kar sakte hai
# 2. original naam ka ek list banaya gaya hai jisme do nested list hai
# 3. copied naam ka ek variable banaya gaya hai jisme original list ka deep
#    copy banaya gaya hai
# 4. copied list ke first nested list ke first element ko 100 se replace kar diya gaya hai
# 5. original list ko print kiya gaya hai jisme changes reflect nahi hote hai kyuki humne deep copy banaya hai
# 6. copied list ko print kiya gaya hai jisme changes reflect hote hai kyuki humne copied list ke   
#    first nested list ke first element ko 100 se replace kar diya hai


#pop item method use karke hum dictionary me se kisi bhi key value pair ko remove kar sakte hai aur uski value ko return kar sakte hai
# Dict = {"name":"ankush","age": 233,"college":"anand"}
# removed_value = Dict.pop("age")
# print("Removed value:", removed_value)
# print("Updated dictionary:", Dict)  



#"""pop method me agar hum kisi aise key ko remove karne ki koshish karte hai jo dictionary me exist nahi karti hai to wo error throw karta hai"""
Dict = {"name":"ankush","age": 233,"college":"anand"}
removed_value = Dict.pop("num") # key exist nahi karti hai isliye error throw karega

print("Removed value:", removed_value)
print("Updated dictionary:", Dict)    