class MyClass:
    def __init__(self,msg):
        self.msg = msg
    def __inside(self):
        print self.msg

    def outside(self):
        self.__inside()

my = MyClass("My name is 'My Class'")
my.outside() 