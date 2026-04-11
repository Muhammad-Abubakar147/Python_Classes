import pandas as pd

data=pd.read_excel("C:\Data\Python Classes\output.xlsx")
print(data)
print(data.info())
print(data.describe())