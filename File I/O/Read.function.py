#if we want to read any file then we will use this syntax
f = open("File I\O\Lecture-file.txt", "r")
data = f.read()
print(data)
f.close()