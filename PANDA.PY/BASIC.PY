#Students Class Data
import pandas as pd

DATA = {
    "NAME": ["muhammad", "abubakar"],
    "age": [21, 32],
    "city": ["faisalabad", "samnabad"]
}

df = pd.DataFrame(DATA)
print(df)


Student_data = {
    "Name": ["Ayesha", "Khan Muhammad", "Qamar", "Ayesha Gaffar", "Amien", "Faizan", "Mlaika", "Nariha"],
    "Age": [21, 21, 20, 21, 21, 20, 21, 23],
    "city": ["Fsd", "fsd", "fsd", "fsd", "fsd", "Nya Lahore", "Dijkot", "fsd"],
    "marks": [99, 88, 77, 66, 55, 44, 33, 22],
    "salary": [2300, 2200, 3400, 7760, 756, 6733, 9800, 765]
}

df = pd.DataFrame(Student_data)
print(df.info())
print(df.describe())