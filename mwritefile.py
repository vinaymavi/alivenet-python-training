# Open a file
try:
    print("file open");
    fo = open("mohit.txt", "w")
    fo.write( "This is Python class");
except IOError as e:
            print("Error:"+e);

finally:
    fo.close()
    print("file closed");
