import sys
import os
import shutil
from os import path
class FileUtility:
    def fileCopy(self,fileName,desPath):
        try:
            if path.exists(fileName):
                src = fileName
                filename1 = path.basename(src)
                if (desPath==""):
                    dstFileName = filename1+"_copy"
                else:
                    dstFileName = desPath+"/"+filename1
                
                fp = open(src)
                fileContent = fp.read();
                fileCopy = open(dstFileName,"w+")
                fileCopy.write(fileContent)
                print "File Copied"
            else:
                raise Exception("File Not Found")
        except Exception as e:
            print e

    def fileMove(self,fileName,desPath):
        try:
            if path.exists(fileName):
                src = fileName
                filename1 = path.basename(src)
                if (desPath==""):
                    dstFileName = filename1+"_copy"
                else:
                    dstFileName = desPath+"/"+filename1
                
                fp = open(src)
                fileContent = fp.read();
                fileCopy = open(dstFileName,"w+")
                fileCopy.write(fileContent)
                fp.close()
                os.unlink(src)
                print "File Moved"
            else:
                raise Exception("File Not Found")
        except Exception as e:
            print e
    
    def fileRemove(self,fileName):
        try:
            if path.exists(fileName):
                os.unlink(fileName)
                print "File ReMoved"
            else:
                raise Exception("File Not Found")
        except Exception as e:
            print e


obj = FileUtility()
fileName = sys.argv[2]
desPath =""
try:
    desPath = sys.argv[3]
except Exception as e:
    desPath = ""

if sys.argv[1]== "copy":
    obj.fileCopy(fileName,desPath)

elif sys.argv[1]== "move":
    obj.fileMove(fileName,desPath)

elif sys.argv[1]== "remove":
    obj.fileRemove(fileName)
else:
    print("Wrong input, try again")
