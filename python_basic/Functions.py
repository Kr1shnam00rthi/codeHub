def func():
	global x
	x="fantastic"
func()
print("Python is "+x)

def func1():
	x="krishna"
	def func2():
		nonlocal x  # The nonlocal keyword makes the variable belong to the outer function.
		x="moorthi"
	func2()
	return x
	
# pass any number of arguments to a function
def func1(*kids):
	print(kids[1],kids[2])
	
func1("krishna","moorthi","amal")

# Keyword Arguments

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 

# Default parameters

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# A lambda function can take any number of arguments, but can only have one expression.

#  lambda arguments : expression 

x= lambda a: a+10
print(x(5))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
