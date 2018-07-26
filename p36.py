class Person:
    def __init__(self, *args, **kwargs):
        self.name = "Person"
    def print_name(self):
        print self.name

class Employee(Person):
    def __init__(self, *args, **kwargs):
            Person.__init__(self)
            self.company_name = "Sapient"

    def print_company(self):
        print self.company_name

emp = Employee()
emp.print_name()
emp.print_company()