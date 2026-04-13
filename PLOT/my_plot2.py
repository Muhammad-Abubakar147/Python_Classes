#line plot
import matplotlib.pyplot as plt
Months=[1,2,3,4]
sales=[1000,1250,1340,1570]
plt.plot(Months,sales,linestyle ="--",color="blue",linewidth=2,marker="o")
plt.grid(linestyle=":",linewidth=2)
plt.xlabel("MONTHS")
plt.ylabel("SALES OF MONTH")
plt.title("COMPANY SALES OF 4 MONTHS 2025")
plt.xticks([1,2,3,4],["M1","M2","M3","M4"])
plt.legend()
plt.show()