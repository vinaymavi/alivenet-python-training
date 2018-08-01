import shutil
files = ['source/hello1.txt', 'source/hello2.txt', 'source/hello3.txt']

try:
    for f in files:
        shutil.copy(f, 'destination')
    print "Files Copied Successfully!!"

except Exception as e: 
    print ("Error Occur: "+str(e))     