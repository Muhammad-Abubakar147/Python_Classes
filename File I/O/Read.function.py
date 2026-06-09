#if we want to read any file then we will use this syntax
f = open("File I\O\Lecture-file.txt", "r")
data = f.read()
print(data)
f.close()

#If we want to read any file line by line then we will use this syntax
print("This syntax for printing line by line")
f = open("File I\O\Lecture-file.txt", "r")
line1 = f.readline() #This will print line 1
line2=f.readline() #This will print line 2 in file
print(line1)
print(line2)