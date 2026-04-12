import pandas as pd
Student_data={
    "Name":["Ayesha","Khan Muhammad","Qamar","Ayesha gaffar","Amien","Faizan","Mlaika","Nariha"],
    "Age":[21,21,20,21,21,20,21,23],
    "city":["Fsd","fsd","fsd","fsd","fsd","Nya lahore","dijkot","fsd"],
    "marks":[99,88,77,66,55,44,33,22,],
    "salary":[2300,2200,3400,7760,756,6733,9800,765,],
}
#inserting employ id

df=pd.DataFrame(Student_data)
df.index=df.index+1
df.insert(0,"Employ Id",[10,20,30,40,50,60,70,80])
print(df)