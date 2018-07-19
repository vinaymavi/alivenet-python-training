class MyClass:
    CLASS_NAME = "My Class.."

    def printer(self):
        MyClass.CLASS_NAME = "Updated Value"
        print MyClass.CLASS_NAME

my = MyClass()
my.printer()
print MyClass.CLASS_NAME