import shutil
src = "source/hello1.txt"
dst = "destination"

try:
    shutil.move(src, dst)
    print "Files Moved Successfully!!"
except Exception as e: 
    print ("Error Occur: "+str(e))  
