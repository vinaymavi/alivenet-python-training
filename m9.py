import shutil

try:
    fileName=input("Enter File:");
    shutil.copy(fileName,'mohit')
    print("File Copy Successfully")
except FileNotFoundError as e:
    print("Error:"+e);
