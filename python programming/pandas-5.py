import pandas as pd
import seaborn as sns
penguins=sns.load_dataset('penguins')
filtered_penguins=penguins[ 'bill_length_mm'>45]
print(filtered_penguins)

