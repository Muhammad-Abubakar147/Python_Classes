import matplotlib.pyplot as plt
Product=["condom","medicine","safety","wax","gilete"]
Sales=[1950,1000,950,1550,760]
plt.bar(Product,Sales,color="red",label="Product sales")
plt.legend()
plt.title("Sales of products in Feburary")
plt.xlabel("Names of Products")
plt.ylabel("Sales of products")
plt.savefig("Bar plot.png",dpi=300,bbox_inches="tight")
plt.show()
