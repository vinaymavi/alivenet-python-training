class Person(object):
    def __init__(self, *args, **kwargs):  
        print "Person calling." 
        super(Person,self).__init__()             
        self.name = "Person"
    def print_name(self):
        print self.name
class Developer(object):
    def __init__(self, *args, **kwargs):
        super(Developer,self).__init__()     
        print "Developer calling."
        self.type_of_developer = "Front-End"    

    def print_developer_type(self):
        print self.type_of_developer

class Employee(Person,Developer):
    def __init__(self, *args, **kwargs):
            print "Employee calling."
            super(Employee, self).__init__()
            self.company_name = "Sapient"

    def print_company(self):
        print self.company_name
emp = Employee()
emp.print_name()
emp.print_company()
emp.print_developer_type()