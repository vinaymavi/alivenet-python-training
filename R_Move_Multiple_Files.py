import shutil
files = ['source/hello1.txt', 'source/hello2.txt', 'source/hello3.txt']

try:
    for f in files:
        shutil.move(f, 'destination')
    print "Files Moved Successfully!!"
except Exception as e: 
    print ("Error Occur: "+str(e))        