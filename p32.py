class MyClass:
    def __init__(self, name):
        self.__private_name = "LOL"
        self.name = name
    
    def my_name(self):
        print self.__private_name 

my = MyClass("Ashish")
print my.name
my.my_name()