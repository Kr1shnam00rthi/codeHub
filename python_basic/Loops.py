l=[1,2,3,4,5,6]
for x in l:
	print(x,end=" ")
	
print("\n")

for i in range(0,len(l)):
	print(l[i],end=" ")
	if i==1:
		continue # Skips only that iteration 
	elif i==4:
		break # Break the entire loopss
print("\n")

j=0
while j<len(l):
	print(l[j],end=" ")
	j+=1

