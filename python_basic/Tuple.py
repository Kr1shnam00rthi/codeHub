# All operations of list apply except altering of data
# To alter data we need to convert tuple() to list()

# In tuples data elements are immuatable
# Join tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 
print(tuple3.count("a"))
print(tuple3.index("a"))

# unpacking tuples

fruits=('apple','banana','cherry')
(x,y,z)=fruits
print(y)
