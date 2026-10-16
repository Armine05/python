import pandas as pd
import seaborn as sns

penguins = sns.load_dataset('penguins')

subset_penguins = penguins.iloc[20:31,[0,1,2]]
print(subset_penguins)
