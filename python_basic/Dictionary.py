# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

print(len(thisdict))

# constructor

thisdict1 = dict(name = "John", age = 36, country = "Norway")
print(thisdict1)

# Access

x=thisdict["model"] # thisdict.get["model"]

x=thisdict.keys() # return list of keys

y=thisdict.values() # returns list of values

x,y=thisdict.items() # returns a key,value pairs

# Add

thisdict.update({"Year":2020})

# Remove

thisdict.pop("model")
thisdict.popitem() # removes last added item
del thisdict


# printing keys
for x in thislist.keys():
	print(x)

# printing values

for y in thislist.values():
	print(y)

# printing key,values pair

for x,y in thislist.items():
	print(x,y)
	
# nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
print(myfamily["child2"]["name"]) 
