# Question:1
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#-------------------------------------------------------------------
    # class CheckMethod :
    #     def __init__(self):
    #         self.msg = ''

    #     def getStrig(self):
    #         self.msg = raw_input('Enter your Message\n')

    #     def printString(self):
    #         print self.msg.upper()

    # obj = CheckMethod()
    # obj.getStrig()
    # obj.printString()


# Question:2
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of
# the array should be i*j.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
#---------------------------------------------------------

# input = raw_input("Enter your two number with comma seperated")
# list_array =  input.split(',')
# list_final = []
 

# for i in range(int(list_array[0])):
#     lists = []
#     for j in range(int(list_array[1])):
#         lists.append(i*j)

#     list_final.append(lists)
# print list_final


# Question:3
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
#-------------------

# input = raw_input('Enter your message with comma seperated')
# msg_list =  input.split(',')
# msg_list.sort()
# print ','.join(msg_list)
 

# Question:4
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
# ----------------------------------
 

# lines = []
# while 1:
#         msg = raw_input()
#         if msg:
#             lines.append(msg.upper())
#         else:
#             break
# print lines



# Question:5
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
# --------------------------------------------------

# Method-1
# d = {}
# while 1:
#     msg = raw_input()
#     if msg:
#         c = msg.split(' ')
#         for n in c :
#              d.update({n:n})
#     else:
#         break

# val = d.values()
# val.sort()

# print ' '.join(val)

#Method-2
# s = raw_input()
# words = [word for word in s.split(" ")]
# print " ".join(sorted(list(set(words))))
 

# Question:6
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

input = raw_input()
result = {'digits':0,'letters':0}

for c in input:
    if c.isdigit():
        result['digits'] +=1
    elif c.isalpha():
        result['letters'] +=1
    else:
        pass

print "LETTERS".result['letters']
print "DIGITS".result['digits']





  










