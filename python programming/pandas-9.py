import pandas as pd
import seaborn as sns

penguins = sns.load_dataset('penguins')

filtered_penguins_not = penguins.loc[
    ~(penguins['species'] == 'Gertoo')
]

print(filtered_penguins_not)
