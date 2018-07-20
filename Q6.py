import math
C=50
H =30
Q=[];
inputval = raw_input("Enter the number seprated by comma : ")
numList = inputval.split(",")

for index in range(0,len(numList)):
	D = int(numList[index])
	Q.append(str(int((math.sqrt((2*C*D)/H)))))

output = ",".join(Q)

print output
