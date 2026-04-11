import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
days=[1,2,3,4,5,6,7,8,9,10]
temperature=[41.5,34,56,54,63,23,18,45.8,23.5,23]
data_df=pd.DataFrame({"days":days,"temperature":temperature})
sns.barplot(x="days",y="temperature",color="red",data=data_df)
plt.show()