
# Delcarations

print("Hello")
print("He is called 'Johnny'")
A="HELLO"
print(type("hello"))
print(type(A))
B="""hello all
guys"""
print(B)

# Access string elements

var="hello world"

print(var[0])

for x in var:
	print(x,end='')
print("\n")
print("Length of string: ",len(var))

if "hello" in var:
	print("Yes")

if "a" not in var:
	print("Yes")
print("\n")

# String Slicing

var1="Hello world"
print(var1[1:5]) # start:end goes till end-1
print(var1[:5]) # :end
print(var1[2:])

print(var1[-5:-2]) # Negative indexing starts from -1

print(var1[::-1]) # reverse string
print("\n")

# Modifying Strings

var2="HelLo WorLd " 

print(var2.upper())
print(var2.lower())
print(var2.isupper())
print(var2.islower())
print(var2.count('l'))
print(var2.endswith('d')) #startswith()
print(var2.strip()) # removes whitespaces rstrip lstrip
print(var2.find("H")) # Return start index of string .index()
print(var2.replace("H","J"))
print(var2.swapcase())
print(var2.isalpha())
print(var2.isnumeric())
a=['1','2','3','4']
print("".join(a)) 
print(var2.split(" "))# Converts string to list


# Concatenation

a="Hello"
b="World"
print(a+b)
print(a+" "+b)

# String format

age=22
print(f'My age is {age}')

# Escape characters

print("single quote \'")
print("Backslash\\")
print("Newline \n")
print("Carriage Return \r hello")
print("Tab \t done")
print("Backspace \b")



