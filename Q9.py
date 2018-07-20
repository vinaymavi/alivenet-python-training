output=""
inputVal=""

print("Enter multi line string: ")

while 1:
	inputVal = raw_input()
	if inputVal:
		output += inputVal.upper()+"\n"
		
	else:
		break

print output;
