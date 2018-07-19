class Parent:

    def __init__(self, name):
			self.name = name	   
			print self.name

    def change_name(self, new_name):
			self.name = new_name
			print self.name
		
obj = Parent('Hament')

obj.change_name('Ram')