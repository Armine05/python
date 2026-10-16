import numpy as np
houses=np.array([
    [3,2000,10],
    [2,1500,20],
    [4,2500,5]
    ])
print(houses.shape)
reshaped_houses=houses.reshape(-1)
print("REshaped houses(flattened):\n", reshaped_houses)
reshaped_houses1x9=houses.reshape(1,9)
print("REshaped houses(flattened):\n", reshaped_houses1x9)
