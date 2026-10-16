import numpy as np

houses = np.array([
    [3, 2000, 10],
    [2, 1500, 20],
    [4, 2500, 5]
])

more_houses = np.array([[5, 3000, 15]])

joined_houses = np.concatenate((houses, more_houses), axis=0)

print("Joined houses by rows:\n", joined_houses)

extra_data = np.array([
    [100000],
    [1200000],
    [1400000]
])

joined_columns = np.concatenate((houses, extra_data), axis=1)

print("Joined columns with extra column price:\n", joined_columns)
