file = open("app.log","r")

count = 0

for line in file:
  if "ERROR" in line:
     count += 1

print("Total ERROR lines:",count)

file.close()
