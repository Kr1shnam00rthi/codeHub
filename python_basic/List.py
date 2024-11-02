# Initialize lists
thislist = ["apple", "banana", "cherry"]

# Access
print(thislist[2])         # Output: cherry
print(thislist[-1])        # Output: cherry
print(thislist[1:])        # Output: ['banana', 'cherry']
print(thislist[-3:-1])     # Output: ['apple', 'banana']

# Change value
thislist[1] = "blackcurrant"
print(thislist)            # Output: ['apple', 'blackcurrant', 'cherry']

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)            # Output: ['apple', 'blackcurrant', 'watermelon']

thislist[1:3] = ["watermelon"]
print(thislist)            # Output: ['apple', 'watermelon']

# Add

# Append
thislist1 = ["apple", "banana", "cherry"]
thislist1.append("orange")
print(thislist1)          # Output: ['apple', 'banana', 'cherry', 'orange']

# Insert
thislist1.insert(0, "orange")
print(thislist1)          # Output: ['orange', 'apple', 'banana', 'cherry', 'orange']

# Extend
tropical = ["mango", "pineapple", "papaya"]
thislist1.extend(tropical) # Extend can be used with any iterable like tuple, set, dictionary (keys), etc.
print(thislist1)          # Output: ['orange', 'apple', 'banana', 'cherry', 'orange', 'mango', 'pineapple', 'papaya']

# Remove

# Remove specific item
thislist2 = ["apple", "banana", "cherry", "orange"]
thislist2.remove("apple")
print(thislist2)          # Output: ['banana', 'cherry', 'orange']

# pop() removes and returns the last item or the item at the specified index
thislist2.pop()           # Remove last element (orange)
print(thislist2)          # Output: ['banana', 'cherry']

thislist2.pop(1)          # Remove item at index 1 (cherry)
print(thislist2)          # Output: ['banana']

# del removes the list entirely from memory
del thislist1

# clear() frees the memory by removing all items from the list
thislist2.clear()
print(thislist2)          # Output: []

# Looping

# Using a for loop
for x in thislist:
    print(x)

# Using list comprehension (for printing)
[print(x) for x in thislist]

# Loop with index
for i in range(len(thislist)):
    print(thislist[i])

# List Comprehension
a = [x for x in range(10) if x > 2]
print(a)                # Output: [3, 4, 5, 6, 7, 8, 9]
# newlist = [expression for item in iterable if condition == True] 

# functions
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort() # ascending sort
thislist.sort(reverse=True) # descending sort

thislist.reverse()

# Copy lists

# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to # list1, and changes made in list1 will automatically also be made in list2
thislist4 = ["apple", "banana", "cherry"]
mylist = thislist4.copy()
print(mylist)

# Join lists

list1=["1","2","3"]
list2=[1,2,3]
print(list1+list2)

print(list1.extend(list2))

print(list1.index(2))


