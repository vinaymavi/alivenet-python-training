inputVal = raw_input("Enter word with comma seprated : ")

valLists = inputVal.split(",")
valLists.sort()

print ",".join(valLists)