import pandas as pd
student_data={
    "name":["ali","hamza","nabeel","hfsa","nabeela","hammad","abubakar","ammar",],
    "age":[23,45,67,34,23,45,21,12],
    "salary":[2300,48800,7764,74664,664889,54000,5757,754],
    "city":["fsd","fsd","smanbad","fsd","gaha","lahore","fsd","fsd"],
    "performance":[99,88,77,66,55,44,33,22],
}
df=pd.DataFrame(student_data)
df.index=df.index+1
print(df)



print("This is posintioning of members :")

print(df.describe())


print("This is information about mamebers of company :")
print(df.info())
