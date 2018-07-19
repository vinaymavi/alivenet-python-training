class Emp:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def function(self):
    print("Hello {0}, Your Age is {1}.".format(self.name,self.age))

	
name = raw_input('Enter Your Name:- ')
age=int(input("Enter Your Age:- "))	

e1 = Emp(name, age)
e1.function()