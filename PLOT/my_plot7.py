#scatter plot
import matplotlib.pyplot as plt
studies_hours=[1,2,3,4,5,6,7,8]
marks_achived=[10,99,88,77,66,56,45,32]
plt.scatter(studies_hours,marks_achived,color="green",marker="o",label="Student Data")
plt.title("Relationship between students marks",fontsize=14, fontweight="bold")
plt.xlabel("HOURS OF STUDY",fontsize=12, fontweight="bold")
plt.ylabel("MARKS ACHIVED",fontsize=12, fontweight="bold")
plt.grid(True)
plt.legend()
plt.show()