# A set is a collection which is unordered, unchangeable*, and unindexed.

thisset={1,2,3,4} # or use set() constructor
print(thisset)
thisset1 = {"apple", "banana", "cherry", True, 1, 2}
print(thisset1)

# length of set
print(len(thisset1))

# Access elements

for x in thisset1:
	print(x)
# in not in operators

# Add element

thisset1.add("orange")
print(thisset1)

thisset1.update("a","b","c")
print(thisset1)

# Remove element

thisset1.remove("a") # the item to remove does not exist, remove() will raise an error

thisset1.discard("b") # if item doesnot exist it wont rise an error

thisset1.pop() # Removes random item
thisset1.clear() # makes it empty

del thisset1 # frees the memory

# methods

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset) 

print(set1.intersection(set2)) # this will return intersection
set1.intersecation_update(set2) ## this will update in set1 intself
print(set1)

print(set1.difference(set2))
print(set1.difference_update(set2))

print(set1.symmetric_difference(set2))
