import shutil

try:
    fileName=input("Enter File Name:");
    shutil.move(fileName, "mohit")
    print("file move successfully")
except FileNotFoundError as e:
    print("Error:"+e)
