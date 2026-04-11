import matplotlib.pyplot as plt
x=["MON","TUES","WED","THURS","FRI","SAT","SUN"]
Y=[12,45,67,34,2,34,567]
plt.title("Data of a single week")
plt.xlabel("weekly att")
plt.ylabel("Numerical values")
plt.plot(x, Y, marker='o')
plt.show()