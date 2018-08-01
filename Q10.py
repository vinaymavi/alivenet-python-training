inputVal = raw_input("Enter the String: ")

InputList = inputVal.split(" ")
uniqueList = list(set(InputList))
uniqueList.sort()
print " ".join(uniqueList)