file = open("simple.txt","r")

lines = file.readlines()
print("Total lines : ", len(lines))

file.close()
