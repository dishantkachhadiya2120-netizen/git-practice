import os

file = ["hello.py","Info.py","random.txt"]

for i in file:
 if os.path.exists(i):
   print(i,"file exist")
 else:
   print(i,"file does not exist")
