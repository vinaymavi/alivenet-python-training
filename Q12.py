outputList = []

for x in range(1000,3001):
	flag = 0
	for y in range(0,len(str(x))+1):
		if(y%2 == 0):
			flag=1
		else:
			break
	
if(flag ==1):
	print(x)