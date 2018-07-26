class StrToUpper:
	def getInput(self):
		self.getString = raw_input("Enter a string: ")

	def printUpperCase(self):
		print("In uppercase: " + self.getString.upper())

obj = StrToUpper()

obj.getInput()
obj.printUpperCase()