
try:
    f1 = open("xyz.ac")
    # print "This is TRY block"
except Exception as e:
    print e
else:
    print "Else statement"
    f1.close()
finally:
    print "Finally block"
    
    