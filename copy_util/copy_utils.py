import os
import shutil
from os import path
class FileUtility:
    def fileCopy(self,fileName):
        try:
            if path.exists(fileName):
                src = path.realpath(fileName)
                dst = src+".bak"
                shutil.copy(src, dst)
                print "File Copied"
            else:
                raise Exception("File Not Found")
        except Exception as e:
            print e

    def fileMove(self,fileName):
        try:
            if path.exists(fileName):
                src = path.realpath(fileName)
                dst = src+".bak"
                shutil.move(src, dst)
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
#obj.fileCopy("a.txt")
#obj.fileMove("a.txt")
obj.fileRemove("a.txt.bak.bak")

