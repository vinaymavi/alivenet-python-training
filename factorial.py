def find_factorial(n):
    fact = 1
    for i in range(1,n):
        fact = fact * i

    print("Factorial of ", n ," = ", fact)

n = int(input("Enter no. to find factorial: "))

find_factorial(n)