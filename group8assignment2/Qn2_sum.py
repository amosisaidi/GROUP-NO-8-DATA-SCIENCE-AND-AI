evenlist=[]
oddlist=[]
for i in range(1,6):
	if i%2==0:
		evenlist.append(i)
	else:
		oddlist.append(i)		

print("Sum of even numbers:  ", sum(evenlist))

print("Sum of odd numbers: ", sum(oddlist))
