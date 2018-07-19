class MyClass:
    def my_name(self,msg):
        self.msg = msg
    def printer(self):
        print self.msg        
my = MyClass()
my.my_name("My name is 'My Class'")
my.printer()   