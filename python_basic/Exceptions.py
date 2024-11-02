# try block lets you test a block of code for errors
# except block lets you handle errors
# else block lets you execute code when there is no error
# finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
	print("Hello")

except NameError:
	print("Variable x is not defined")
	
except:
	print("An execption occured")
	
else:
	print("Nothing went wrong")
	
finally:
	print("The 'try except' is finished")
	

try:
	f=open("example.txt")
	try:
		f.write("Hello world")
	except:
		print("something went wrong")
	finally:
		f.close()
except:
	print("Someting went wrong when opening the file")
	
x=-1
if x<0:
	raise Exception("Sorry, no numbers below zero")
	
