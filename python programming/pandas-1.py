import pandas as pd

data = {
    'Bedrooms': [3, 2, 4, 3],
    'Size_sqft': [2000, 1500, 2500, 1800],
    'Age_years': [10, 20, 5, 15]
}

df = pd.DataFrame(data)

print(df)
print(type(df))
