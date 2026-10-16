import pandas as pd

data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'London'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Paris'}
]

df=pd.DataFrame(data)
print(df[df['Age'] > 25])
print("heyy")
print(df.head(1))

print(df['Age'])
print(df.columns)

print("heyyyyyy")
print(df.iloc[:, [0]])
print(df.index)

print(df.dtypes)
print(df.shape)
