import os

name = input("Enter The File name : ")
if(os.path.exists(name)):
  print("File Exist")
else:
  print("File Does not Exist")
