str = "MY TOP"
def print_msg():
    if 1:     
        global str
        str = "GLOBAL MODIFIED"
    print str

print_msg()
print str    