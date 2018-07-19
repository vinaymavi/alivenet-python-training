class MyClass:
    MY_NAME = "My Class"
    @classmethod
    def print_my_name(cls):
        print cls.MY_NAME

MyClass.print_my_name()