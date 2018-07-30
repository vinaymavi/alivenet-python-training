input_content = raw_input("Input a sentence which contains albhabet digit etc: ")
number=0
albhabet=0
symbol = 0
for x in input_content:
	
	if x.isdigit():
		number+=1
	elif x.isalpha():
		albhabet+=1
	else:
		symbol+=1

print("Digit: %d, Albhabet: %d, Symbol: %d",number,albhabet,symbol)

