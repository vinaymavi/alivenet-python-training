import json
fb="";
fileContent="";
try:
	fp = open("a1.txt")
except Exception as e:
	print(e)
else:
	fileContent = fp.read()
	fp.close()
finally:
	print("script excute.")
	

print(fileContent)