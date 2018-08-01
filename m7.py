try:
   fh = open("mohit.txt", "r")
   fh.write("This is  exception handling!!")
except IOError:
   print("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
