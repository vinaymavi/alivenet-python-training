#Question:2
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320



number = int(raw_input('Enter Your number which you wants fatorial'))

#method-1
fact = 1
while number>1:
	fact = fact*number
	number = number-1
	
print fact

#method-2

#def fact(number):
	#if number ==1:
		#return 1
	#number =  number * fact(number-1)
	#return number
	
	
#print fact(number)
	
