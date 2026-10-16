import numpy as np

houses = np.array([
    [3, 2000, 10],
    [2, 1500, 20],
    [4, 2500, 5]
])

more_houses = np.array([[5, 3000, 15]])
stacked_houses_vertically=np.vstack((houses,more_houses))
print(stacked_houses_vertically)
extra_data = np.array([[1000],[2000],[1400]])
stacked_houses_horizontally=np.hstack((houses,extra_data))
print("horizontal",stacked_houses_horizontally)
