class MyClass:
    def __init__(self,msg):
        self.msg = msg

    def printer(self):
        print self.msg
my = MyClass("My name is 'My Class'")
my.printer()   