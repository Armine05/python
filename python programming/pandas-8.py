import pandas as pd
import seaborn as sns

penguins = sns.load_dataset('penguins')

filtered_penguins_or = penguins.loc[
    (penguins['species'] == 'Adelie')|
    (penguins['island'] == 'Dream')|
    (penguins['bill_length_mm'] > 40)
]

print(filtered_penguins_or)
