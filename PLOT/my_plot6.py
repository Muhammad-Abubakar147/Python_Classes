#histogram
import matplotlib.pyplot as plt
Students_score=[32,45,63,34,2,76,95,64,10,64,43,12,34,56,78,90,9,98,76,54,32,10,130,62,56,67,85,94,87,55,64,43,83,92,74,57,67,77,88,99,66,36,39]
plt.hist(Students_score,bins=8,color="red",edgecolor="black")
plt.xlabel("Marks of Students")
plt.ylabel("Numbers of students")
plt.title("Analysis of students of Zoology")
plt.show()