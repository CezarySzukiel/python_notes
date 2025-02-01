import numpy as np
import pandas as pd

ls = [44, 20, 17, 47, 23, 26, 28, 18, 15, 4, 19, 7, 46, 27]

# print(np.percenile(ls, 95))

print()

df = pd.DataFrame.from_records([
    {"id": 1, "name": "Anna", "age": 25, "gender": "F", "salary": 4000},
    {"id": 2, "name": "Tomasz", "age": 32, "gender": "M", "salary": 5000},
    {"id": 3, "name": "Katarzyna", "age": 28, "gender": "F", "salary": 4500},
    {"id": 4, "name": "Paweł", "age": 30, "gender": "M", "salary": 4800},
    {"id": 5, "name": "Magdalena", "age": 27, "gender": "F", "salary": 4200},
    {"id": 6, "name": "Jakub", "age": 29, "gender": "M", "salary": 4600},
    {"id": 7, "name": "Marta", "age": 26, "gender": "F", "salary": 4100},
    {"id": 8, "name": "Adam", "age": 31, "gender": "M", "salary": 4900},
    {"id": 9, "name": "Ewa", "age": 24, "gender": "F", "salary": 3900},
    {"id": 10, "name": "Michał", "age": 33, "gender": "M", "salary": 5100}
])

print(df.describe())

# print(df.groupby(['gender'])["salary"].mean())

print(df.loc[df["age"] >= 30]['salary'].mean())
print(df.loc[df["age"] < 30]['salary'].mean())

pivot = pd.pivot_table(df, values='salary', columns=['age', 'gender'],
                       index=df['age'].apply(lambda x: '>= 30' if x >= 30 else '< 30'), aggfunc=['sum', 'mean'])
print(pivot)
