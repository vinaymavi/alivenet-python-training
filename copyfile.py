#Command Line utility to copy file
import os
import shutil
from os import path

def main():
	if path.exists("democopy.txt"):
		src = path.realpath("democopy.txt")
	
	dst = "C:/Users/Deepak/Desktop/test/newcopiedfile.txt"
	shutil.copy(src, dst)

main()