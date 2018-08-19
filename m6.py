#simple class 
class Person:

    def myInfo(self,name,age,location):
        print("Name :",name)
        print("Age :",age)
        print("Location: :",location)

iname=input("Enter Name:")
iage=input("Enter Age:")
ilocation=input("Enter Location:")
p= Person()
p.myInfo(iname,iage,ilocation)

