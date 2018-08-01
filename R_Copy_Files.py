import shutil
src = "source/hello1.txt"
dst = "destination"

try:
    shutil.copy(src, dst)
    print "Files Copied Successfully!!"
except Exception as e: 
    print ("Error Occur: "+str(e)) 