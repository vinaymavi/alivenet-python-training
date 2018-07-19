class ListTuple:
    def set_numbers(self,n):
        self.num1 = n.split(',')
        self.num2 = tuple(self.num1)

    def get_numbers(self,n):
        print("given input as list: ", self.num1)
        print("given input as tuple: ", self.num2)

lt = ListTuple()
n = input("Enter comma seprated numbers: ")
lt.set_numbers(n)
lt.get_numbers(n)