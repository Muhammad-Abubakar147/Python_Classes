f=open("File I\O\File-Lecture.txt","r")
data=f.read()#this is for reading a file 
print(data)
f.close()

#For writting more
f= open ("File I\O\File-Lecture-for-editing.txt","a")
f.write ("\nYES IAM MUHAMMAD ABUBKAR") #this will append new text in ur file
f.close()