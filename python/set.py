# set unordered collection of unique items
# duplicate items are not allowed
# set = {22,3,4,5,6,7,6,4,8,9,"hello",10}
# set.add(100)
# set.remove(22)
# set.remove(55)
# print(set)
# set.discard(22)  #remove kar deta hai
# set.discard(55)  #Error show nhi hota discard main


# indexing and slicing not possible in set
# set = {22,3,4,5,6,7,6,4,8,9,"hello",10}

# # Duplicate value not allow
# set = {1,2,3,4,4}
# print(set)

#<<<<<<<<<< set operations>>>>>>
# set = {1,3,5,6}
# # union(|)
# a = {1,2,3}
# b = {2,3,4}
# print(a|b)

# # Intersection
# print(a & b)

# # Diffrence
# print( a - b )

# # symmertic diffrence (^)
# print(a^b)

# # set and superset 
# a = {1,2}
# b = {1,2,3,4,5}
# print(a.issubset(b))
# print(b.issuperset(a))
# print(a.issuperset(b))



# Sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (all unique elements)
print("Union:", A.union(B))          # {1, 2, 3, 4, 5, 6}

# Intersection (common elements)
print("Intersection:", A.intersection(B))  # {3, 4}

# Difference (elements in A but not in B)
print("Difference:", A.difference(B))      # {1, 2}

# Subset (is every element of A present in B?)
print("Is {1,2} subset of A?", {1, 2}.issubset(A))  # True

# Superset (does A contain all elements of another set?)
print("Is A superset of {1,2}?", A.issuperset({1, 2}))  # True

# intersection_update (modifies the original set)
C = {1, 2, 3, 4}
C.intersection_update(B)
print("After intersection_update:", C)  # {3, 4}