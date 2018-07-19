#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line

number=int(input("Please Enter factorial Number: "))
j=1
fact = 1
for i in range(number,0,-1): 
	fact =fact*i
	
print(fact)	