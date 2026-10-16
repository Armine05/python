import pandas as pd
import seaborn as sns
penguins=sns.load_dataset('penguins')
filtered_penguins=penguins[['species', 'island', 'bill_length_mm']]

