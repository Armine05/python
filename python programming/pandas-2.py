import pandas as pd
prices=[50000,400000,65000,55000]
price_series=pd.Series(prices,name="price")
print(price_series)
print(type(price_series))
