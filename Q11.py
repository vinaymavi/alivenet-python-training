outputList=[]
inputVal = raw_input("Enter 4 digit binary with comma seprated : ")
lists = [val for val in inputVal.split(",")]

for x in lists:
	intDecimal = int(x,2)
	if (intDecimal%5 == 0):
		outputList.append(str(intDecimal))

print ",".join(outputList)
