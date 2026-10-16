import pandas as pd
import seaborn as sns
penguins=sns.load_dataset('penguins')
print(penguins.head())
print(penguins.tail())
#print(penguins.tail(10)
print(penguins.dtypes)
print(penguins.info())
