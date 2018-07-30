output=""
inputVal = raw_input("Enter 4 digit binary number with comma seprated: ")
lists =[x for x in inputVal.split(',')]
for x in lists:
	if int(x,2)%5 == 0:
		output += ",".join(str(x))

print(output)

